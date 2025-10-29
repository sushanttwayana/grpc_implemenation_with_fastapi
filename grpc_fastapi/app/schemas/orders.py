from enum import Enum
from pydantic import BaseModel
from uuid import UUID, uuid4

class DrinkEnum(str, Enum):
    coffee = "coffee"
    soda = "soda"
    beer = "beer"
    wine = "wine"
    
class MealEnum(str, Enum):
    pasta ="pasta"
    pizza = "pizza"
    meat = "meat"
    fish ="fish"
    
class DessertEnum(str, Enum):
    cookie = "cookie"
    donut = "donut"
    brownie = "brownie"
    cake = "cake"
    
class OrderBase(BaseModel):
    order_id: UUID = uuid4() #type: ignore

class OrderCreate(OrderBase):
    drink: DrinkEnum
    meal: MealEnum
    dessert: DessertEnum  

class OrderRead(OrderBase):
    drink: str
    meal: str
    dessert: str
    
