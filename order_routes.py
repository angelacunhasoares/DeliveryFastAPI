from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@order_router.get("/")
async def pedidos():
    return {"message": "Welcome to the Order API"}