import sqlite3
import json


# def list_orders():
#     # list does all
#     with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         db_cursor.execute("""
#             Select * 
#             FROM Orders
#         """)

#         query_results = db_cursor.fetchall()

#         orders = []

        
#         for row in query_results:
#             order = {
#                 "id": row['id'],
#                 "metal_id": row['metal_id'],
#                 "size_id": row['size_id'],
#                 "style_id": row['style_id']
#             }
#             orders.append(order)
#         serialized_orders = json.dumps(orders)
#     return serialized_orders

def list_orders(url):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        orders = []
        if '_expand' in url['query_params']:
            db_cursor.execute("""
                SELECT
                    o.id,
                    o.style_id,
                    o.metal_id,
                    o.size_id,
                    m.id metalId,
                    m.metal metalMetal,
                    m.price metalPrice,
                    si.id sizeId,
                    si.carets sizeCarets,
                    si.price sizePrice,
                    st.id styleId,
                    st.style styleStyle,
                    st.price stylePrice
                FROM Orders o
                JOIN Metals m ON m.id = o.metal_id
                JOIN Sizes si on si.id = o.size_id
                JOIN Styles st on st.id = o.style_id
            """)

            query_results = db_cursor.fetchall()
            for row in query_results:
                style = {
                    "id": row['styleId'],
                    "style": row['styleStyle'],
                    "price": row['stylePrice']
                }
                size = {
                    "id": row['sizeId'],
                    "carets": row['sizeCarets'],
                    "price": row['sizePrice']
                }
                metal = {
                    "id": row['metalId'],
                    "metal": row['metalMetal'],
                    "price": row['metalPrice']
                }
                order = {
                    "id": row['id'],
                    "metal_id": row['metal_id'],
                    "size_id": row['size_id'],
                    "style_id": row['style_id'],
                    "metal": metal,
                    "size": size,
                    "style": style
                }
                orders.append(order)
        else:
            db_cursor.execute("""
                SELECT
                    o.id,
                    o.metal_id,
                    o.size_id,
                    o.style_id
                From Orders o
            """)
            query_results = db_cursor.fetchall()
            for row in query_results:
                order = {
                    "id": row['id'],
                    "metal_id": row['metal_id'],
                    "size_id": row['size_id'],
                    "style_id": row['style_id']
                }
                orders.append(order)
        serialized_orders = json.dumps(orders)
    return serialized_orders


def retrieve_order(pk):
    #retrirve does 1
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        where o.id = ?
        """,(pk,))
        query_results = db_cursor.fetchone()

        dictionary_version_of_object = dict(query_results)
        serialized_order = json.dumps(dictionary_version_of_object)
    return serialized_order


def add_order(data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()


        db_cursor.execute(
            """
                INSERT INTO Orders (metal_id, style_id, size_id)
                VALUES (?,?,?);
            """,
                (
                    data["metal_id"],
                    data["style_id"],
                    data["size_id"],
                ),
            )
        rows_affected = db_cursor.rowcount
    return True if rows_affected > 0 else False


def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders where id = ?
        """, (pk,)
        )
        number_of_rows_deleted = db_cursor.rowcount
    return True if number_of_rows_deleted > 0 else False