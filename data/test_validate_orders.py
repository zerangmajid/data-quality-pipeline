import pytest
from validate_orders import validate_orders
import pandas as pd

def test_valid_file(tmp_path):
    content = "order_id,user_id,amount,status\n1,1,100,completed"
    path = tmp_path / "sample.csv"
    path.write_text(content)
    validate_orders(str(path))
