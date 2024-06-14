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

    def add_inventory_item(self, item_name, quantity, expiry_date, calories, protein, fats, carbs, other_nutrients):
        try:
            cursor = self.connection.cursor()
            insert_query = sql.SQL("""
                INSERT INTO public.food_items (item_name, quantity, expiry_date, calories, protein, fats, carbs, other_nutrients)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (item_name, quantity, expiry_date, calories, protein, fats, carbs, other_nutrients))
            self.connection.commit()
            cursor.close()
            print(f"Item '{item_name}' added to the inventory.")
        except Exception as e:
            print(f"Error adding item to the inventory: {e}")
            self.connection.rollback()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
