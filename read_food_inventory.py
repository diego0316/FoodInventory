# read_food_inventory.py
import psycopg2
from psycopg2 import sql
import json

class FoodInventoryDB:
    def __init__(self, db_params):
        self.db_params = db_params
        self.connection = self.connect_db()

    def connect_db(self):
        try:
            connection = psycopg2.connect(**self.db_params)
            print("Connected to the database.")
            return connection
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    def get_all_inventory_items(self):
        try:
            cursor = self.connection.cursor()
            query = sql.SQL("SELECT * FROM public.food_items")
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as e:
            print(f"Error reading from the inventory: {e}")
            return []

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

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
        # Fetch all inventory items
        items = db.get_all_inventory_items()

        # Print all items
        for item in items:
            print(item)

        db.close_connection()

if __name__ == '__main__':
    main()
