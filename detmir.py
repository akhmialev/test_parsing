import csv
import requests

MOSKOV = 'MOW'
PITER = 'SPE'
citys = [MOSKOV, PITER]

with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(
        (
            [
                'ID',
                'Наименование',
                'Старая цена',
                'Новая цена',
                'Город',
                'Ссылка на товар'
            ]
        )
    )


def fetch(url, params):
    headers = params['headers']
    return requests.get(url, headers=headers)

for city in citys:
    lenghts = fetch("https://api.detmir.ru/v2/products?filter=categories["
                    f"].alias:lego;promo:false;withregion:RU-{city}&expand=meta.facet.ages.adults,meta.facet.gender.adults,"
                    f"webp&meta=*&limit=30&offset=30&sort=popularity:desc", {
                        "headers": {
                            "accept": "*/*",
                            "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                            "cache-control": "no-cache",
                            "content-type": "application/json",
                            "pragma": "no-cache",
                            "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-ch-ua-platform": "\"Windows\"",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-site",
                            "x-requested-with": "detmir-ui",
                            "cookie": "ab2_90=ab2_90old90; ab2_33=ab2_33old33; ab2_50=44; ab3_75=ab3_75old75; ab3_33=ab3_33old33; ab3_20=ab3_20_20_1; cc=0; uid=X6NyHmLQMCd0b7gNBFJwAg==; is_shop_pos=1; _gaexp=GAX1.2.rF6aGfQwQPiBEWNbZr-EZQ.19193.2!8MwGXf_UQwWf1g2n0sBLCw.19243.0; _gcl_au=1.1.678132024.1657810986; _ym_uid=1657810987199797329; _ym_d=1657810987; _ga=GA1.2.1425530600.1657810989; _gid=GA1.2.846765658.1657810989; geoCityDM=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; geoCityDMIso=RU-MOW; geoCityDMCode=; auid=936bbfb1-e3b2-4c38-ab1f-c8c090060866; _ym_isad=1; tmr_lvid=081228f7ed04ced91f2c4005b1092baa; tmr_lvidTS=1657811009452; advcake_track_id=14d97d6d-19df-58f1-aa05-931bdabfecc5; advcake_session_id=1de6405d-011e-8e77-7c17-2d3f70a94fca; _sp_ses.2b21=*; JSESSIONID=e1fd3354-497d-4ea1-95e9-51e0cc1fdfa3; detmir-cart=a25f34ae-52af-426f-a156-b2775b808633; srv_id=cubic-front11-prod; dm_s=L-e1fd3354-497d-4ea1-95e9-51e0cc1fdfa3|kHa25f34ae-52af-426f-a156-b2775b808633|Vj936bbfb1-e3b2-4c38-ab1f-c8c090060866|gqcubic-front11-prod|qa1a173c5f-9b5b-4c16-a580-5c47fadc9734|RK1657875044228#jjuAw67x0N6EjB561kgRtyEAIqtlwBDKXfYxWC483DM; _ym_visorc=w; qrator_msid=1657875038.733.rHcbjaTUJ9U8Idk3-bf9um9kq8p1l7iv97bf7e60o8jv9asg7; mindboxDeviceUUID=27ad2bcc-8a96-498c-8651-de7f49ab0802; directCrm-session=%7B%22deviceGuid%22%3A%2227ad2bcc-8a96-498c-8651-de7f49ab0802%22%7D; _gat=1; cto_bundle=8odIqV8lMkZrRFFxOSUyQmNCd3Job3FPaWlEQXJuTnU0YlVSaDc5VGtOWWpub2ZrUU45dmdDbXdFaGVyV3VCSmQxMFFqeVFlb3dSJTJGOUNGTUpFV3dQUTVqSWU1WXlRRkFYRUI3RWZrYzJlb0hlRmVEMDh1RnlWTEEyVzZRZ1hITXloOUlaWEFzUnB6RDJqeDJpWHVXcVVBTGQlMkJINyUyQlh3JTNEJTNE; _gat_test=1; _sp_id.2b21=a2d56128-2ab9-4c27-99d2-37ef6ebf9c9f.1657810989.5.1657876690.1657838287.b7328b6f-c3fc-49e1-97cd-f26e08ee60b9; tmr_reqNum=67",
                            "Referer": "https://www.detmir.ru/",
                            "Referrer-Policy": "strict-origin-when-cross-origin"
                        },
                        "body": None,
                        "method": "GET"
                    })
    lenght = lenghts.json()['meta']['length']

    if city == 'MOW':
        city = 'Москва'
    else:
        city = "Санкт-Питербург"

    number = 0
    while number < lenght:
        number += 1
        datas = lenghts.json()

        for data in datas['items']:
            try:
                id = data['id']
                title = data['title']
                link = data['link']['web_url']
                if data['price']['price']:
                    price = data['price']['price']
                if data['old_price']['price']:
                    old_price = data['old_price']['price']
            except:
                old_price = None

        with open('data.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(
                (
                    [
                        id,
                        title,
                        old_price,
                        price,
                        city,
                        link
                    ]
                )
            )

        print(f"items {number} saved")
    print(f"Finish {city}")
