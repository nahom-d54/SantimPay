from ..types import *
from ..config import Config
from ..exceptions.santimpay_exceptions import *
import jwt as JWT
from time import time
class SantimPayCheckout:

    def __init__(self, http_client, merchant_id, private_key):
    
        self.http_client = http_client
        self.merchant_id = merchant_id
        self.private_key = private_key
    

    # : SantimPayCheckoutRequest SantimPayOptions -> SantimPayCheckoutResponse
    def create(self, santimPayCheckoutRequest: SantimPayCheckoutRequest ,  option: SantimPayOptions = None) -> SantimPayCheckoutResponse: 
        """Create checkout

        Args:
            santimPayCheckoutRequest (SantimPayCheckoutRequest): type of santim pay checkout
            option (SantimPayOptions, optional): checkout options. Defaults to None.

        Raises:
            SantimPayNetworkException: _description_

        Returns:
            SantimPayCheckoutResponse: _description_
        """
        if option == None:
            option = SantimPayOptions(False)
        

        try:

            body = santimPayCheckoutRequest.jsonSerialize()
            body['merchantId'] =  self.merchant_id
            body['signedToken'] = self.generateSignedToken(santimPayCheckoutRequest.amount, self.merchant_id)
            response = self.http_client.post(Config.API_VERSION + "/initiate-payment", json=body)
            url = response.text.replace('\u0026', '&')


            return SantimPayCheckoutResponse.fromJson(url)
        except ConnectionErrorException as e:
            raise  SantimPayNetworkException() #Exception("santim pay n exception")#SantimPayNetworkException()
        except Exception as e:#(ClientException e) {
            #SantimPaySupport.__handleException(e)

            print("exception")

    def generateSignedToken(self, amount, paymentReason):
    
        time_ = time()
        data = {
            'amount' : amount,
            'paymentReason': paymentReason,
            'merchantId': self.merchant_id,
            'generated': time_

        }
        

        jwt = JWT.encode(data, self.privateKey, algorithm='ES256')

        return jwt
    