import logging

from grpc import StatusCode
from grpc_interceptor.exceptions import NotFound, GrpcException

from pb.kitchen_pb2 import OrderResponse
from pb.kitchen_pb2_grpc import KitchenServicer

mock_meals = {
    "pasta": 10,
    "pizza": 0,
    "meat": 5,
    "fish":2
}

class KitchenBaseService(KitchenServicer):
    
    def GetOrder(self, request, context):
        # return super().GetOrder(request, context)
        kitchen_stock = mock_meals.get(request.order)
        
        if kitchen_stock is None:
            raise GrpcException(
                details="Meal not Found",
                status_code=StatusCode.NOT_FOUND,
            )
            
        
        if kitchen_stock == 0:
            raise NotFound(
                details="Meal out of stock",
                status_code= StatusCode.NOT_FOUND,
            )
            
        return OrderResponse(order_status = "DELIVERY!!!")