
class SantimPayCheckoutResponse:

    def __init__(
        self,
        payment_url
    ):
       
        self.payment_url = payment_url
    

    def jsonSerialize(self):
    
        return {
        
            "payment_url" : self.payment_url,
            
        }
    
    @staticmethod
    def fromJson(url):
    
        return SantimPayCheckoutResponse(url)
