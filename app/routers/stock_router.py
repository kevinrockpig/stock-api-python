from fastapi import APIRouter, HTTPException
from app.services import yfinance_service

# ===============================================
# 定義 API 端點，並呼叫 Service 層處理資料。
# ===============================================

router = APIRouter()

@router.get("/{ticker}")
def get_stock_data(ticker: str):
    try:
        data = yfinance_service.get_historical_data(ticker)
        if not data["prices"]:
            raise HTTPException(status_code=404, detail="找不到該股票代號的資料")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))