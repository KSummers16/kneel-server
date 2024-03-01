import sqlite3
import json



def list_metals():
    # list does all
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            Select * 
            FROM Metals
        """)

        query_results = db_cursor.fetchall()

        metals = []

        
        for row in query_results:
            metal = {
                "id": row['id'],
                "metal": row['metal'],
                "price": row['price']
            }
            metals.append(metal)
        serialized_metals = json.dumps(metals)
    return serialized_metals


def update_metal(id, metal_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            UPDATE Metals
                SET
                    price = ?,
                    metal = ?
                WHERE id =?
            """,
            (metal_data['price'], metal_data['metal'], id)
        )

        rows_affected = db_cursor.rowcount
    return True if rows_affected > 0 else False