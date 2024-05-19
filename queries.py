import psycopg2 as pg
import schema as sc
from connect import connect


def get_products():
    conn = connect()
    cur = conn.cursor()
    select_statement = f"""
                    SELECT * FROM products
                    ORDER BY product_id;
                    """
    cur.execute(select_statement)
    res = cur.fetchall()
    conn.close()
    return res


def get_disposed_products():
    conn = connect()
    cur = conn.cursor()
    select_statement = f"""
                    SELECT * FROM Disposedproducts
                    ORDER BY disposed_product_id;
                    """
    cur.execute(select_statement)
    res = cur.fetchall()
    conn.close()
    return res


def get_orders():
    conn = connect()
    cur = conn.cursor()
    select_statement = f"""
                    SELECT * FROM Orders
                    ORDER BY order_id;
                    """
    cur.execute(select_statement)
    res = cur.fetchall()
    conn.close()
    return res


def create_product(product: sc.ProductsModel):
    conn = connect()
    cur = conn.cursor()
    insert_statement = f"""
                        INSERT INTO Products (name, brand_id, manufacturer, is_written_off, production_date, 
                        report_date, storage_change_date, storage_zone, storage_stage, initial_cable_material, 
                        initial_cable_length, initial_cable_diameter, product_size)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cur.execute(insert_statement, (product.name, product.brand_id, product.manufacturer, product.is_written_off,
                                   product.production_date, product.report_date, product.storage_change_date,
                                   product.storage_zone, product.storage_stage, product.initial_cable_material,
                                   product.initial_cable_length, product.initial_cable_diameter, product.product_size))
    conn.commit()
    conn.close()


def update_order_status(order_id: int):
    conn = connect()
    cur = conn.cursor()
    update_statement = f"""
                UPDATE orders 
                SET end_date = TO_TIMESTAMP(TO_CHAR(NOW(), 'YYYY-MM-DD HH24:MI:SS'), 'YYYY-MM-DD HH24:MI:SS')
                WHERE order_id = %s;             
        """

    cur.execute(update_statement, (order_id, ))
    conn.commit()
    conn.close()


def update_product_status(product_id: int, status: bool):
    conn = connect()
    cur = conn.cursor()
    update_statement = f"""
                UPDATE Products 
                SET is_written_off = %s
                WHERE product_id = %s;             
        """

    cur.execute(update_statement, (status, product_id))
    conn.commit()
    conn.close()
