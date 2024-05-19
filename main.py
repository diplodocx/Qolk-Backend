from fastapi import FastAPI, Depends
import queries as db
import schema as sc
from mqtt_requests import send_message

app = FastAPI()


@app.get("/get_products")
def read_products():
    res = db.get_products()
    return res


@app.get("/get_disposed_products")
def read_disposed_products():
    res = db.get_disposed_products()
    return res


@app.post("/add_product")
def set_product(product: sc.ProductsModel = Depends()):
    res = db.create_product(product)
    return res


@app.get("/get_orders")
def read_orders():
    res = db.get_orders()
    return res


@app.patch("/close_order/{order_id}")
def read_orders(order_id: int):
    res = db.update_order_status(order_id)
    return res


@app.patch("/update_product_status/{product_id}")
def read_orders(product_id: int, new_status: sc.UpdateProductStatus = Depends()):
    res = db.update_product_status(product_id, new_status.new_status)
    return res


@app.post("/change_device_state/{machine_id}")
def set_product(machine_id: int, signal: sc.DeviceSignal = Depends()):
    res = send_message(machine_id, signal)
    return res
