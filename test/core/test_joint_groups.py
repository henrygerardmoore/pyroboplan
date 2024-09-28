import numpy as np
import pinocchio
import pytest

from pyroboplan.core.utils import (
    get_random_collision_free_state,
)

from pyroboplan.core.joint_groups import JointGroupManager
from pyroboplan.models.panda import (
    load_models,
    add_self_collisions,
    add_object_collisions,
)


# Use a fixed seed for random number generation in tests.
np.random.seed(1234)


def test_make_joint_group():
    model, _, _ = load_models()
    jg = JointGroupManager(model)
    with pytest.raises(IndexError):
        jg.make_joint_group("Test", {"foo"})

    jg.make_joint_group("Test", ["panda_finger_joint1", "panda_finger_joint2"])

    with pytest.raises(Exception):
        jg["IndexError"] = [1]


if __name__ == "__main__":
    test_make_joint_group()
