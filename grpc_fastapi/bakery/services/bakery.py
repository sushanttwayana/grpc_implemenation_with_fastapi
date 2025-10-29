import logging

from grpc import StatusCode
from grpc_interceptor.exceptions import NotFound, GrpcException

from pb.bakery_pb2 import OrderResponse
from pb.bakery_pb2_grpc import BakeryServicer

mock_deserts = {
    "cookie": 10,
    "donut": 0,
    "brownie": 5,
    "cake":2
}

class BakeryBaseService(BakeryServicer):
    
    def GetOrder(self, request, context):
        # return super().GetOrder(request, context)
        dessert_stock = mock_deserts.get(request.order)
        
        if dessert_stock is None:
            raise GrpcException(
                details="Dessert not Found",
                status_code=StatusCode.NOT_FOUND,
            )
            
        
        if dessert_stock == 0:
            raise NotFound(
                details="Dessert out of stock",
                status_code= StatusCode.NOT_FOUND,
            )
            
        return OrderResponse(order_status = "DELIVERY!!!")