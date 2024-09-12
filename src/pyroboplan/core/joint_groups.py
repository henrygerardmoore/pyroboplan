class JointGroupManager:
    """
    Wrapper for pinnochio model
    Because who can come up with a better name than slapping manager on it?
    """

    def __init__(self, model, *args, **kwargs):
        self.model = model

    def make_joint_group(self, name):
        pass

    def __getitem__(self, name):
        pass

    def __setitem__(self, name):
        pass

    def __delitem__(self, name):
        pass

    def __getattr__(self, name):
        return getattr(self.model, name)
