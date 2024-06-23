from requests import post
import json

# copytoaster_key
# hZYNiEDyd5VCpP(FJS1w@UeRsgLr$QA => 刑事_Judgement
# gO(oHjM6!qyc7$iRWV@nD0GvIaTw13t => 民事_Judgement
# NGaX&K2P5G39cpKHFNSrMyK=wzPJJSb => 高等刑事_Judgement
# P7zdKSLg2_vC9Q$)bUFGqtfX6kTcpNJ => 高等民事_Judgement


url = "https://api.droidtown.co/CopyToaster/API/"
payload = {
    "username": "legaltech@droidtown.co", # 請勿更改此欄位
    "copytoaster_key": "hZYNiEDyd5VCpP(FJS1w@UeRsgLr$QA", # 這裡替換成您想要搜尋的法院金鑰！
    "category": "臺灣台北地方法院", # 這裡輸入您想搜尋的法院名稱
    "input_str": "用LINE恐嚇取財", # 這裡輸入您想要搜尋的文句
    "count": 1 # optional, default = 15
}

# print(post(url, json=payload).json())

response = post(url, json=payload)
# print(response)
data = response.json()
print(data)

# with open('/Users/mac/Documents/code/python/project2/law.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data, json_file, ensure_ascii=False, indent=4)