import pinocchio

class JointGroup:
    model : pinocchio.Model

    def __init__(self, name, manager, model : pinocchio.Model, indices):
        self.model = model
        self.joint_indices = indices
        self.name = name
        self.manager = manager
    
    def set_joint_state(self, state):
        if (len(state) != len(self.joint_indices)):
            raise IndexError(f"length of input state ({len(state)}) is not the same as the size of joint model {self.name} ({len(self.joint_indices)})")

class JointGroupManager:
    """
    Wrapper for pinnochio model
    Because who can come up with a better name than slapping manager on it?
    """

    model : pinocchio.Model
    joint_groups : dict[str, JointGroup]

    def __init__(self, model : pinocchio.Model):
        self.model = model
        self.joint_groups = {}

    def make_joint_group(self, joint_group_name, joint_names : list[str]):
        if joint_group_name in self.joint_groups:
            raise IndexError(f"{joint_group_name} already refers to a joint group. Delete and re-create the joint group if you want to re-use this name")
        joint_ids = []
        for joint_name in joint_names:
            id = self.model.getJointId(joint_name)
            if id > self.model.nq:
                names = [valid_name for valid_name in self.model.names]
                raise IndexError(f"Could not find joint {joint_name} in model. Possible names are {names}")
            joint_ids.append(id)

        joint_ids.sort()
        self.joint_groups[joint_group_name] = JointGroup(joint_group_name, self, self.model, joint_ids)

    def __setitem__(self, name, value : list[float]):
        group = self.joint_groups[name]
        group.set
        # set the state of the joints in group

    def __delitem__(self, name):
        del self.joint_groups[name]

    def __getattr__(self, name):
        return getattr(self.model, name)
