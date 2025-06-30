import pandas as pd

VALID_STATUSES = {"completed", "failed", "refunded"}

def validate_orders(path):
    df = pd.read_csv(path)

    if df['order_id'].duplicated().any():
        raise ValueError("Duplicate order_id found")

    if df['user_id'].isnull().any():
        raise ValueError("Null user_id found")

    if not df['amount'].gt(0).all():
        raise ValueError("Invalid amount values")

    if not df['status'].isin(VALID_STATUSES).all():
        raise ValueError("Invalid status values")

    print("All validations passed.")
