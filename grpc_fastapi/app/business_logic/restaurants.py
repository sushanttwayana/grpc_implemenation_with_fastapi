from api.dependencies.grpc.bar import BarClient
from api.dependencies.grpc.bakery import BakeryClient
from api.dependencies.grpc.kitchen import KitchenClient

from schemas.orders import OrderCreate, OrderRead

def process_order(order: OrderCreate) -> OrderRead:
    
    bar_client = BarClient()
    bakery_client = BakeryClient()
    kitchen_client = KitchenClient()
    
    drink_status = bar_client.get_order(order.drink)['order_status']
    meal_status = kitchen_client.get_order(order.meal)['order_status']
    dessert_status = bakery_client.get_order(order.dessert)['order_status']
    
    return OrderRead(
        order_id= order.order_id,
        drink = drink_status,
        meal= meal_status,
        dessert= dessert_status
    )