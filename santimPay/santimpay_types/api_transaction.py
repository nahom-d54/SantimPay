class SantimPayTransaction:


    def __init__(self, id, transaction_id, payment_type, transaction_status, created_at, updated_at):
    
        self.id = id
        self.transaction_id = transaction_id
        self.payment_type = payment_type
        self.transaction_status = transaction_status
        self.created_at = created_at
        self.updated_at = updated_at
    

    def jsonSerialize(self):
    
        return {
            "id" : self.id,
            "transactionId" : self.transaction_id,
            "paymentType" : self.payment_type,
            "transactionStatus" : self.transaction_status,
            "createdAt" : self.created_at,
            "updatedAt" : self.updated_at,
        }
    
    @staticmethod
    def fromJson(data):
    
        return SantimPayTransaction(data["id"], data["transactionId"], data["paymentType"], data["transactionStatus"], data["createdAt"], data["updatedAt"])
    

