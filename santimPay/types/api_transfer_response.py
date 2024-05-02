import urllib.parse
from . import SantimPayTransaction

urldecode = urllib.parse.unquote
class SantimPayTransferResponse:

    def __init__(
        self,
        session_id,
        url,
        otp,
        transaction
    ):
        self.transaction = transaction
        self.session_id = session_id
        self.url = url
        self.otp = otp
    

    def jsonSerialize(self):
    
        return {
            "session_id" : self.session_id,
            "url" : self.url,
            "otp" : self.otp,
            "transaction" : self.transaction,
        }
    
    @staticmethod
    def fromJson(data):
    
        return SantimPayTransferResponse(data["sessionId"], urldecode(data["url"]) if data.get("url") else "", urldecode(data["otp"]) if data.get("otp") else "", SantimPayTransaction.fromJson(data["transaction"]) if data.get("transaction") else None)
    
