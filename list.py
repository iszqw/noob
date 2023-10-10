import urllib.parse
import requests, logging
import json

def loggin():
    logging.basicConfig(
        format=('%(levelname)s->%(filename)s->%(asctime)s->%(message)s'),
        filename=r'Py\rz.log',
        level=logging.INFO,
        filemode='a+'
    )


def citylist():
    url = 'https://sasstest.gclme.com/api/changepower/changePowerList/gcl/selectStationCityV2?cityName=&isCity=true'
    req = requests.get(url)
    logging.info("城市列表获取成功")
    city = req.json()["data"]
    return city


def huandian(citycode,city):
    try:
        url = 'https://sasstest.gclme.com/api/changepower/changePowerList/gcl?pageSize=10&currentPage=1&longitude=120.63630718311998&latitude=31.260310926312865&location=' + citycode + '&city=' + citycode + '&isDefault=true&licensePlate=%E4%BA%ACA88880&comprehensive=1'
        headers = {
            'Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIxNzUzOTMxMDg1MyIsInNjb3BlIjpbImFsbCJdLCJzaW5nbGVMb2dpbiI6IjIiLCJleHAiOjE2OTY3MTUwMDksImF1dGhvcml0aWVzIjpbImFhIl0sImp0aSI6ImNlZjY4MTAyLTg3YzctNDc4NC05ZDIzLTNhNThjZGVjZGFiNyIsImNsaWVudF9pZCI6ImFkbWluIiwidG9rZW4iOiJnY2xsb2dpbl90b2tlbl9lYWZlZjQ4OGFlYjg0Mjc5OWE3YjMwZmE3YjQ5ZDA2YSJ9.E_s2n3IcyPl02hd_7rV1vLpA_uSjgfGshC0fxYut-1_MRae1e_cy-V1rcqU5YBlXPdbZqsmogjJf3i62M6iYpqxOICHRDPsTagi6jWXq9vGu9L0GocOgc9_k1Hbqxz8OhsNHoXn7EJ47tMLkmCA54jRJPGJ-lc9D6_zbimhn95zPFXWyaSGxS6l34CY86_EihmVZP0VWjdXZoRaQjSsWqDkCtR85RSdH8i0WquYKfsaZbDfpcYOritrlWw5lcKW0uvHLLcvjVumsJwO98Q3vmH6hm1Ite6wIQCGcrpBA-dx8h_nGWYrm8bRiTSykElMq03SB8i8Ma7Om-MbohIRETw'
        }
        req = requests.get(url=url, headers=headers)
        huandianlist = req.json()['data']['list']
        numhuandianlist = len(huandianlist)
        # print("共"+str(numhuandianlist)+"个换电站点")
        # stationPrice单价
        for i in range(numhuandianlist):
            if huandianlist[i]['stationPrice'] in ("0.00", "null"):
                # 判断单价是否为0
                print("换电站【" + huandianlist[i]['stationName'] + "】的单价为0")
                logging.info("换电站【" + huandianlist[i]['stationName'] + "】的单价为0")
            else:
                continue
    except:
        logging.error(city + "换电站列表请求失败")





def chongdian(city):
    try:
        url = 'https://sass.gclme.com/api/changepower/changePowerList/selectPileStation'
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIxNzUzOTMxMDg1MyIsInNjb3BlIjpbImFsbCJdLCJzaW5nbGVMb2dpbiI6IjIiLCJleHAiOjE2OTY3MTUwMDksImF1dGhvcml0aWVzIjpbImFhIl0sImp0aSI6ImNlZjY4MTAyLTg3YzctNDc4NC05ZDIzLTNhNThjZGVjZGFiNyIsImNsaWVudF9pZCI6ImFkbWluIiwidG9rZW4iOiJnY2xsb2dpbl90b2tlbl9lYWZlZjQ4OGFlYjg0Mjc5OWE3YjMwZmE3YjQ5ZDA2YSJ9.E_s2n3IcyPl02hd_7rV1vLpA_uSjgfGshC0fxYut-1_MRae1e_cy-V1rcqU5YBlXPdbZqsmogjJf3i62M6iYpqxOICHRDPsTagi6jWXq9vGu9L0GocOgc9_k1Hbqxz8OhsNHoXn7EJ47tMLkmCA54jRJPGJ-lc9D6_zbimhn95zPFXWyaSGxS6l34CY86_EihmVZP0VWjdXZoRaQjSsWqDkCtR85RSdH8i0WquYKfsaZbDfpcYOritrlWw5lcKW0uvHLLcvjVumsJwO98Q3vmH6hm1Ite6wIQCGcrpBA-dx8h_nGWYrm8bRiTSykElMq03SB8i8Ma7Om-MbohIRETw'
        }
        data = {
            "availableGan": True,
            "city": city,
            "comprehensiveSort": True,
            "currentPage": 1,
            "latitude": 31.260310926312865,
            "licensePlate": "京A88880",
            "longitude": 120.63630718311998,
            "pageSize": 100000,
            "stationStatus": "1",
            "tenant": "gcl",
            "type": "3802aca553164a13adca3d640db69eb3"
        }

        req = requests.post(url=url, headers=headers, data=json.dumps(data))
        chongdianlist = req.json()['data']
        for i in range(len(chongdianlist)):
            if chongdianlist[i]['electricityPrice'] in ("0.00", "-", None):
                print("充电站【" + chongdianlist[i]['name'] + "】的单价为0")
                logging.info("换电站【" + huandianlist[i]['stationName'] + "】的单价为0")
            else:
                continue
    except:
        logging.error(city + "充电站列表请求失败")



for i in range(len(citylist())):
    city = citylist()[i]["city"]
    print("==============================" + city + "==============================")
    logging.info(city)
    if city != "省直辖行政单位":# 因为这city列表里面有个【省直辖行政单位】,判断
        citycode = urllib.parse.quote(city)
        huandian(citycode,city)
    if city != "省直辖行政单位":
        chongdian(city)
    print(" ")









