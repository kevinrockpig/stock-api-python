from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import stock_router

# ===============================================
# 初始化 FastAPI，設定 CORS，並註冊 Router。
# ===============================================

app = FastAPI(title="Stock Tracker API")

# 允許前端跨域請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 註冊路由
app.include_router(stock_router.router, prefix="/api/stock", tags=["Stock"])