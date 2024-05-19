from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class StorageZonesModel(BaseModel):
    zone_id: int
    zone_type: str
    zone_size: float


class StorageStagesModel(BaseModel):
    stage_id: int
    description: str


class ClientsModel(BaseModel):
    client_id: int
    name: str
    phone: Optional[str] = None
    delivery_address: Optional[str] = None


class ProductsModel(BaseModel):
    product_id: int
    name: str = 'test'
    brand_id: int = 1
    manufacturer: str = 'test'
    is_written_off: bool = True
    production_date: datetime = '2032-04-23T10:20:30.400+02:30'
    report_date: datetime = '2032-04-23T10:20:30.400+02:30'
    storage_change_date: datetime = '2032-04-23T10:20:30.400+02:30'
    storage_zone: int = 1
    storage_stage: int = 1
    initial_cable_material: str = 'test'
    initial_cable_length: float = 0.0
    initial_cable_diameter: float = 0.0
    product_size: float = 0.0


class DisposedProductsModel(BaseModel):
    disposed_product_id: int
    name: str
    brand_id: int
    manufacturer: str
    production_date: datetime
    report_date: datetime
    storage_change_date: datetime
    cable_material: str
    cable_length: float
    cable_diameter: float
    disposal_reason: str


class OrdersModel(BaseModel):
    order_id: int
    name: str
    client_id: int
    product_id: int
    start_date: datetime
    end_date: datetime
    order_cable_material: str
    order_cable_length: float
    order_cable_diameter: float


class SensorsModel(BaseModel):
    sensor_id: int
    model: str
    manufacturer: str
    zone_id: int
    min_value: float
    max_value: float


class ReadingsModel(BaseModel):
    reading_id: int
    sensor_id: int
    humidity_value: float
    reading_time: datetime


class MovementsModel(BaseModel):
    movement_id: int
    movement_date: datetime
    cable_length: float
    product_id: int
    source_zone: int
    target_zone: int
