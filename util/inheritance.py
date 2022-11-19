from typing import Mapping

from util.common import read_yaml
import util.path as PATH


def get_inheritance() -> Mapping:
    inheritance_rate = read_yaml(PATH.INHERITANCE_RATE)
    return inheritance_rate