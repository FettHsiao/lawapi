from requests import post
import json

# copytoaster_key
# hZYNiEDyd5VCpP(FJS1w@UeRsgLr$QA => 刑事_Judgement
# gO(oHjM6!qyc7$iRWV@nD0GvIaTw13t => 民事_Judgement
# NGaX&K2P5G39cpKHFNSrMyK=wzPJJSb => 高等刑事_Judgement
# P7zdKSLg2_vC9Q$)bUFGqtfX6kTcpNJ => 高等民事_Judgement

# copytoaster_key = ["hZYNiEDyd5VCpP(FJS1w@UeRsgLr$QA", 
#                    "gO(oHjM6!qyc7$iRWV@nD0GvIaTw13t", 
#                    "NGaX&K2P5G39cpKHFNSrMyK=wzPJJSb", 
#                    "P7zdKSLg2_vC9Q$)bUFGqtfX6kTcpNJ"]


place = ["司法院刑事補償法庭", "臺灣高雄少年及家事法院", "智慧財產及商業法院", 
         "福建金門地方法院", "福建連江地方法院", "臺灣雲林地方法院", 
         "臺灣屏東地方法院", "臺灣臺東地方法院", "臺灣宜蘭地方法院", 
         "臺灣花蓮地方法院", "臺灣高雄地方法院", "臺灣桃園地方法院", 
         "臺灣士林地方法院", "臺灣新北地方法院", "臺灣彰化地方法院", 
         "臺灣臺中地方法院", "臺灣苗栗地方法院", "臺灣基隆地方法院", 
         "臺灣臺南地方法院", "臺灣新竹地方法院", "臺灣橋頭地方法院", 
         "臺灣臺北地方法院", "臺灣嘉義地方法院", "臺灣南投地方法院", 
         "臺灣澎湖地方法院"]
url = "https://api.droidtown.co/CopyToaster/API/"

existing_data = []
for i in place:
    payload = {
        "username": "legaltech@droidtown.co", # 請勿更改此欄位
        "copytoaster_key": "hZYNiEDyd5VCpP(FJS1w@UeRsgLr$QA", # 這裡替換成您想要搜尋的法院金鑰！
        "category": i, 
        "input_str": "用LINE恐嚇取財", # 這裡輸入您想要搜尋的文句
        "count": 1 # optional, default = 15
    }
    response = post(url, json=payload)
    # existing_data.append(response)
    data = response.json()
    existing_data.append(data)


# print(existing_data)

with open('/Users/mac/Documents/code/python/project2/law.json', 'w', encoding='utf-8') as json_file:
    json.dump(existing_data, json_file, ensure_ascii=False, indent=4)