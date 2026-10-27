import yfinance as yf
import warnings

# ===============================================
# 專門處理向 Yahoo Finance 請求資料與格式轉換。
# ===============================================

warnings.filterwarnings("ignore")

def get_historical_data(ticker: str, period: str = "6mo"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    
    # 1. 過濾掉沒有收盤價的無效資料
    hist = hist.dropna(subset=['Close'])
    
    # 2. 強制依照日期（Index）由舊到新排序，解決前端線條倒退打結的問題
    hist = hist.sort_index()
    
    return {
        "dates": hist.index.strftime('%Y-%m-%d').tolist(),
        "prices": hist["Close"].tolist()
    }