# scrape Swiggy.com Using API(Powai-Area)
import requests

cookies = {
    '__SW': 'f76AvCZZCXG9fzk0amM-_eHh0Lq_M0lq',
    '_device_id': '0573426e-4518-d586-c2ab-51a7406cb00c',
    'fontsLoaded': '1',
    '_gcl_au': '1.1.2115920340.1673284454',
    'WZRK_G': 'f5953fb76e1344f08ca5a21268b0d82b',
    '_gid': 'GA1.2.907159929.1673284454',
    'dadl': 'true',
    'userLocation': '{%22address%22:%22Powai%20Lake%2C%20Powai%2C%20Mumbai%2C%20Maharashtra%20400076%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Powai%22%2C%22lat%22:19.1272655%2C%22lng%22:72.9048498}',
    '_session_tid': 'f60345624240ba62031597ded26477d14f11a541bfb547c2611cf806f65836026ce158c76a305042c8885a907c25fe25e732d68d084b93b519286afc1c2fb0a07442357e5c399e8522f33ddfc53883eae0bfc49cfdc1cb06725f977181bc31c5e49990190c129e1a37c04a6e9539dd6b',
    '_is_logged_in': '1',
    '_sid': '4rof934d-673d-43cc-803c-8fa151271b85',
    '_gat_0': '1',
    '_ga': 'GA1.1.2067750835.1673284454',
    '_ga_34JYJ0BCRN': 'GS1.1.1673421846.7.0.1673421858.0.0.0',
    'WZRK_S_W86-ZZK-WR6Z': '%7B%22p%22%3A2%2C%22s%22%3A1673421844%2C%22t%22%3A1673421846%7D',
}

headers = {
    'authority': 'www.swiggy.com',
    '_fetch_req_': 'true',
    'accept': '/',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # 'cookie': '__SW=f76AvCZZCXG9fzk0amM-_eHh0Lq_M0lq; _device_id=0573426e-4518-d586-c2ab-51a7406cb00c; fontsLoaded=1; _gcl_au=1.1.2115920340.1673284454; WZRK_G=f5953fb76e1344f08ca5a21268b0d82b; _gid=GA1.2.907159929.1673284454; dadl=true; userLocation={%22address%22:%22Powai%20Lake%2C%20Powai%2C%20Mumbai%2C%20Maharashtra%20400076%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Powai%22%2C%22lat%22:19.1272655%2C%22lng%22:72.9048498}; _session_tid=f60345624240ba62031597ded26477d14f11a541bfb547c2611cf806f65836026ce158c76a305042c8885a907c25fe25e732d68d084b93b519286afc1c2fb0a07442357e5c399e8522f33ddfc53883eae0bfc49cfdc1cb06725f977181bc31c5e49990190c129e1a37c04a6e9539dd6b; _is_logged_in=1; _sid=4rof934d-673d-43cc-803c-8fa151271b85; _gat_0=1; _ga=GA1.1.2067750835.1673284454; _ga_34JYJ0BCRN=GS1.1.1673421846.7.0.1673421858.0.0.0; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A2%2C%22s%22%3A1673421844%2C%22t%22%3A1673421846%7D',
    'if-none-match': 'W/"a2e3-ocsURp0gM6dQjJzFnnpM3kuaBxI"',
    'referer': 'https://www.swiggy.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76',
}

params = {
    'lat': '19.1272655',
    'lng': '72.9048498',
    'page_type': 'DESKTOP_WEB_LISTING',
}

# get data from Swiggy API
response = requests.get('https://www.swiggy.com/dapi/restaurants/list/v5', params=params, cookies=cookies, headers=headers)

s_data = response.text

import json

# convert data in json format 
j_data = json.loads(s_data) 
#print(j_data)

# Fetching restaurants data from nested dictionary (json-format).
#no_of_records = j_data["data"]["cards"][2]["data"]["data"]["cards"]
#print(no_of_records)

v = j_data["data"]["cards"][2]["data"]["data"]["cards"]
len(v)
mylist=[]
for items in range (0,len(v)):
    my_dict = {}
    name = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["name"]
    area = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["locality"]      
    timing = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["slaString"]      
    distance = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["lastMileTravelString"]  
    c = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]
    d = c.get("aggregatedDiscountInfo")
    if d == None:
        discount = "Discount not avaliable"
    else :
        discount = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["aggregatedDiscountInfo"]["header"]          
    delivery_fees = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["feeDetails"]["fees"][0]["fee"]     
    rating = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["avgRating"]
    cost = j_data["data"]["cards"][2]["data"]["data"]["cards"][items]["data"]["costForTwoString"]   

    my_dict["Name"] = name
    my_dict["Area"] = area
    my_dict["Timing"] = timing
    my_dict["Distance"] = distance
    my_dict["Discount"] = discount
    my_dict["Delivery Fee"] = delivery_fees
    my_dict["Rating"] = rating
    my_dict["Cost"] = cost
    mylist.append(my_dict)
#print(mylist)

import pandas as pd

ex_df = pd.DataFrame(mylist)    #contain all frame data
print(ex_df)
#ex_df.to_excel('Swiggy_scrapp_data.xlsx')   #excel-sheet of powai area restaurants data


