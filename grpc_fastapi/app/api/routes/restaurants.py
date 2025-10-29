from fastapi import status
from api.router import router
from schemas.orders import OrderCreate, OrderRead
from business_logic.restaurants import process_order

@router.post(
    "",
    response_model=OrderRead,
    status_code=status.HTTP_201_CREATED,
    name="create_order"
)
def create_order(order_create: OrderCreate):
    return process_order(order_create)