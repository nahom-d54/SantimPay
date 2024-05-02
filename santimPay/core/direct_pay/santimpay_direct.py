from ...types import SantimPayOptions
from ...config import Config
from ...exceptions.santimpay_exceptions import *
from ...types import *
import jwt as JWT
from time import time

class SantimPayDirect:

    def __init__(self, http_client, merchant_id, private_key, payment_method):
    
        self.http_client = http_client
        self.merchant_id = merchant_id
        self.private_key = private_key
        self.payment_method = payment_method
    
    # SantimPayCheckoutRequest SantimPayOptions . SantimPayCheckoutResponse
    def create(self, santimPayCheckoutRequest: SantimPayCheckoutRequest, phone: str,  option: SantimPayOptions = None): 
    
        if option == None:
            option = SantimPayOptions(False)
        

        try:
            santimPayCheckoutRequest.direct = True
            body = santimPayCheckoutRequest.jsonSerialize() 
            body['phoneNumber'] = phone
            body['paymentMethod'] = self.payment_method
            body['merchantId'] = self.merchant_id
            body['signedToken'] = self.generateSignedToken(santimPayCheckoutRequest.amount, santimPayCheckoutRequest.paymentReason, self.payment_method, phone)
            
            response = self.http_client.post(Config.API_VERSION + "/direct-payment", json=body)
            url = response.text.replace('\u0026', '&')

        
            return SantimPayCheckoutResponse.fromJson(url)
        
        except ConnectionErrorException as e: # (ConnectionErrorException e) 
            raise SantimPayNetworkException()
        except Exception as e:# (ClientException e) 
            print("exception")
    

    def generateSignedToken(self, amount, paymentReason, paymentMethod, phone):
    
        time_ = time()
        data = {

            'amount' : amount,
            'paymentMethod' : paymentMethod,
            'phoneNumber' : phone,
            'paymentReason' : paymentReason,
            'merchantId' : self.merchant_id,
            'generated' : time_
        }
        

        jwt = JWT.encode(data, self.private_key, algorithm='ES256')

        return jwt
    


