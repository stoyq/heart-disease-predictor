import pytest
import os
import numpy as np
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.describe_data import describe_data

test_data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [20, 10, 30], 'col3': [1.0, 2.0, 3.0]})

def test_size():
    result = describe_data(test_data)
    assert len(result) == 3

def test_return_type():
    result = describe_data(test_data)
    assert isinstance(result, list)

def test_all_items_are_dataframes():
    result = describe_data(test_data)
    assert all(isinstance(item, pd.DataFrame) for item in result)

def test_debug_output_types():
    result = describe_data(test_data)

    for i, item in enumerate(result):
        print(i, type(item))
