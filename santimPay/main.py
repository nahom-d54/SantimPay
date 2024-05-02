"""
API SDK for SantimPay Payment Gateway
"""

import httpx
from .core import SantimPayCheckout, SantimPayDirectPay

class SantimPay:
    http_client = ""
    merchant_id = ""
    private_key = ""

    DEFAULT_HOST = 'https://services.santimpay.com'
    DEFAULT_TEST_HOST = 'https://testnet.santimpay.com'
    API_VERSION = '/api/v1/gateway'
    PACKAGE_VERSION = '1.0.0'
    DEFAULT_TIMEOUT = 1000 * 60 * 2
    checkout = ""
    directPay = ""

    def __init__(self, merchant_id: str, private_key: str, test = False):
    
        self.merchant_id = merchant_id
        self.private_key = private_key
        base_url = self.DEFAULT_TEST_HOST if test else self.DEFAULT_HOST
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "Accepts": "application/json",
        }

        self.http_client = httpx.Client(base_url=base_url, headers=headers)
        
        self.checkout = SantimPayCheckout(self.http_client, merchant_id, private_key)
        self.directPay = SantimPayDirectPay(self.http_client, merchant_id, private_key)
    
