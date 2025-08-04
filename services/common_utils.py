from flask import request,jsonify
from config import header
import requests

def isCheckStatus(id):
    url = f'https://api.changenow.io/v2/exchange/by-id?id={id}'
    response = requests.get(url, headers=header)
    return response.json()


def isGetAddress():
    try:
        data = request.get_json()
        if data:
                fromAmount_ = data["fromamount"]
                address = data["address"]
                json = {
                    "fromCurrency": "LTC",
                    "toCurrency": "LTC",
                    "fromNetwork": "LTC",
                    "toNetwork": "LTC",
                    "fromAmount": fromAmount_,
                    "toAmount": "",
                    "address": address,
                    "extraId": "",
                    "refundAddress": address,
                    "refundExtraId": "",
                    "userId": "",
                    "payload": "",
                    "contactEmail": "",
                    "source": "",
                    "flow": "standard",
                    "type": "direct",
                    "rateId": ""
                }
                r = requests.post('https://api.changenow.io/v2/exchange',headers=header,json=json)
                if r.status_code == 200:
                    print(r.json())
                    SendAddress = r.json()['payinAddress']
                    Fromamount = r.json()['fromAmount']
                    toAmount = r.json()["toAmount"]
                    id = r.json()["id"]
                    return jsonify({"보내는주소":SendAddress,"보내는돈":Fromamount,"받는돈":toAmount,"트래잭션아이디":id})
        else:
            return jsonify({"msg":"제출 형식이 올바르지 않습니다."}),404
    except Exception as e:
        return jsonify({"msg":"제출 형식이 올바르지 않습니다."}),404


def isGetStatus():
    try:
        data = request.get_json()
        id = data["id"]
        webhookurl = data["webhook"]
        res = isCheckStatus(id)
        if res["status"] == "finished":
            body = {
                "content":f'상태 : {res["status"]}\n받는 주소 : {res["payoutAddress"]}\n생성일 : {res["createdAt"]}\n네트워크 : {res["fromNetwork"]}'
            }
            requests.post(webhookurl,json=body)
            return jsonify({"msg":"success"})
        else:
            return jsonify({"msg":res["status"]})
    except:
        return jsonify({"msg":"fail"})



