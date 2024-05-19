from fastapi import FastAPI, Depends
import queries as db
import schema as sc
from sender import bot
from config import L_CHAT  # loader chat id

app = FastAPI()


@app.get("/get_products")  # получение всех продуктов без пагинации
def read_products():
    res = db.get_products()
    return res


@app.get("/get_disposed_products")  # получение списанных продуктов без пагинации
def read_disposed_products():
    res = db.get_disposed_products()
    return res


@app.post("/add_product/{zone}")  # добавление нового продукта с отправкой сообщения о переносе
def set_product(zone: int, product: sc.ProductsModel = Depends()):
    res = db.create_product(product)
    bot.send_message(L_CHAT, f'Поместите товар {product.product_id}, {product.name} из зоны 1 в зону {zone}')
    return res


@app.get("/get_orders")  # получение списка заказов без пагинации
def read_orders():
    res = db.get_orders()
    return res


@app.patch("/close_order/{order_id}")  # закрытие заказа (меняются поля с датой закрытия)
def read_orders(order_id: int):
    res = db.update_order_status(order_id)
    return res


@app.patch("/utilize_product/{product_id}")  # утилизация с отправкой сообщения о перемещении
def read_orders(product_id: int, new_status: sc.UpdateProductStatus = Depends()):
    res = db.update_product_status(product_id, new_status.new_status)
    product = db.get_product(product_id)
    bot.send_message(L_CHAT, f'Поместите товар {product_id}, {product[0]} из зоны {product[1]} в зону утилизации')
    return res


@app.patch("/update_product_zone/{product_id}")  # перемещение товара с сообщением
def read_orders(product_id: int, new_zone: sc.UpdateProductZone = Depends()):
    res = db.update_product_zone(product_id, new_zone.new_zone)
    product = db.get_product(product_id)
    bot.send_message(L_CHAT,
                     f'Поместите товар {product_id}, {product[0]} из зоны {product[1]} в зону {new_zone.new_zone}')
    return res
