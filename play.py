import pandas as pd

# 讀取 Excel 檔案
xlsx_file = "circle2.xlsx"
df = pd.read_excel(xlsx_file)

# 轉換為 CSV 並儲存
csv_file = "circle2.csv"
df.to_csv(csv_file, index=False)  # index=False 去掉行索引
print("轉換完成！")