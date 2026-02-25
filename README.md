# Global Population & Geopolitical Risk Dashboard

## 專案簡介
本專案為「AI 工具應用能力實作考」之作品。主題為建立一個整合「全球人口預測」與「伊朗地緣政治風險」的分析儀表板，旨在展示 AI 工具在金融科技與資料分析領域的實務應用能力。

## 網站連結
* **GitHub Pages 網址**: [(https://yuni0719.github.io/2026datascience/)]

## 交付項目檢核 (Checklist)
* [x] GitHub Repository (公開)
* [x] GitHub Pages 網站 (可點擊)
* [x] README 說明文件 (完整)
* [x] 一頁式 PDF 分析報告

## 檔案結構說明
* `/index.html`: 專案首頁 (Landing Page)，採用 RWD 響應式設計。
* `/data/raw.txt`: 原始人口統計數據。
* `/data/cleaned.json`: 經 Python 腳本處理後之格式化 JSON 資料。
* `/scripts/clean.py`: 用於計算平均值、成長率及 CAGR 之 Python 程式碼。

---

## AI 使用聲明 (AI Use Statement)
本專案開發過程中，積極利用生成式 AI (Gemini) 協作完成下列任務：
* **技術開發**：輔助編寫 `scripts/clean.py` 中的數學計算邏輯，以及 `index.html` 的 Tailwind CSS 佈局與 RWD 調校。
* **內容生成**：輔助蒐集伊朗地緣政治風險因子，並協助初步撰寫事實與推論之對照內容。

## Prompt 範例 (Prompt Examples)
以下為本專案實作時所使用之關鍵指令：
1. 「請撰寫 Python 程式讀取 `data/raw.txt`，並計算 2024 至 2100 年的人口平均值、總成長率與年複合成長率 (CAGR)，最後將結果輸出為 JSON 檔。」
2. 「針對伊朗地緣政治風險，建立一個風險矩陣，列出 4 個風險因子並嚴格區分『事實資料 (Fact)』與『推論 (Inference)』。」

## 資料驗證流程 (Verification Process)
為了確保數據準確性並展現嚴謹的分析態度，本專案執行以下驗證流程：
1. **權威引用**：人口數據來源嚴格引用自 **UN World Population Prospects 2024** 與 **Our World in Data**。
2. **排除 AI 數字錯誤**：在開發過程中發現不同 AI 模型針對 2100 年的預測數據存在偏差（主因是參考之報告版本不同），最終透過手動對比聯合國官方報告，**排除 AI 數字錯誤**，以確保儀表板呈現之數據符合權威發佈。
3. **事實核查**：針對地緣政治分析區塊，所有標註為「事實 (Fact)」之內容皆經過二次查核，確保非 AI 虛構之幻覺內容。

---
**Data Source**: UN World Population Prospects / Our World in Data
