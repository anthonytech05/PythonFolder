import requests 

def createOrder():
    try :
        response = requests.post("https://open-gw-daily.palmpay-inc.com/api/v2/payment/merchant/createorder",headers={
            'Content-Type': 'application/json',
            'CountryCode': 'NG',
            'Authorization': 'Bearer 10241024',
            'Signature': 'D11A3E8CB478C0B0F40276DDA5AFD898'
            }, json={
            "requestTime":1662171389940,
            "version":"V1.1",
            "nonceStr":"IBJGAeTa4ZJQv4Z2qufomVo9eI1YnJ9Y",
            "amount":200,
            "notifyUrl":"https://xx.cn/callback/payment",
            "orderId":"testc9ffae997fc1",
            "title":"pay",
            "description": "pay some thing",
            "userId":"110",
            "userMobileNo":"07011698742",
            "currency": "NGN",
            "callBackUrl": "http://returnurl",
            "productType":"bank_transfer",
    
        })
        print(response.json())
        print(response.status_code)
        print(response.ok)
    except Exception as e :
        print(f'Error occurred : {e}')


createOrder()

