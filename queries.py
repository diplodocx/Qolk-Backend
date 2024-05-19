import psycopg2 as pg
import schema as sc
from connect import connect


def get_products():
    conn = connect()
    cur = conn.cursor()
    select_statement = f"""
                    SELECT * FROM products;
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

