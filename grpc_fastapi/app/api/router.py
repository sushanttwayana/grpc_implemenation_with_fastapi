from fastapi import APIRouter

router = APIRouter(prefix="", tags=["restaurants"]) # Prefix can be "/api/restaurants" if you want, but blog implies it's under /api/restaurants via include_router

import api.routes.restaurants