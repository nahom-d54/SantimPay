from core.direct_pay.santimpay_direct import SantimPayDirect

class SantimPayDirectPay:

    def __init__(self, http_client, merchant_id, private_key):
    
        self.http_client = http_client
        self.telebirr = SantimPayDirect(self.http_client, merchant_id, private_key, 'Telebirr')
        self.cbe = SantimPayDirect(self.http_client, merchant_id, private_key, 'CBE Birr')
    