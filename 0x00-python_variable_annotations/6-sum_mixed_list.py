#!/usr/bin/env python3
"""type-annotated function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """fct returns their sum as a float.
    """
    return float(sum(mxd_lst))
