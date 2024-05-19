from fastapi import FastAPI, Depends
import queries as db
import schema as sc

app = FastAPI()


@app.get("/get_products")
def read_products():
    res = db.get_products()
    return res


@app.post("/add_product")
def set_product(product: sc.ProductsModel = Depends()):
    res = db.create_product(product)
    return res
