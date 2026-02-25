import json
import pandas as pd

# 讀取原始資料
def process_data():
    try:
        # 讀取 raw.txt
        df = pd.read_csv('data/raw.txt')
        
        # 計算統計指標
        mean_pop = df['population'].mean()
        
        # 計算總成長率
        total_growth = (df['population'].iloc[-1] - df['population'].iloc[0]) / df['population'].iloc[0]
        
        # 計算 CAGR (n=76年)
        n = 2100 - 2024
        cagr = (df['population'].iloc[-1] / df['population'].iloc[0]) ** (1/n) - 1
        
        # 整理輸出
        result = {
            "analysis": {
                "mean": round(mean_pop, 2),
                "total_growth": f"{round(total_growth * 100, 2)}%",
                "cagr": f"{round(cagr * 100, 4)}%"
            }
        }
        
        # 儲存為 cleaned.json
        with open('data/cleaned.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4)
        print("Successfully cleaned and saved data.")
        
    except FileNotFoundError:
        print("Error: data/raw.txt not found.")

if __name__ == "__main__":
    process_data()
