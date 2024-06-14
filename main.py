# main.py
import json
from food_inventory_db import FoodInventoryDB

def main():
    # Database connection parameters
    db_params = {
        'dbname': 'food_inventory',
        'user': 'diego',
        'password': 'password',
        'host': 'localhost',
        'port': 5432
    }

    db = FoodInventoryDB(db_params)

    if db.connection:
        # Example data
        example_items = [
            {
                'item_name': 'Chicken Breast',
                'quantity': 10,
                'expiry_date': '2024-03-15',
                'calories': 165,
                'protein': 31,
                'fats': 3,
                'carbs': 0,
                'other_nutrients': {}
            },
        ]

        for item in example_items:
            db.add_inventory_item(
                item['item_name'],
                item['quantity'],
                item['expiry_date'],
                item['calories'],
                item['protein'],
                item['fats'],
                item['carbs'],
                json.dumps(item['other_nutrients'])
            )
        db.close_connection()

if __name__ == '__main__':
    main()
