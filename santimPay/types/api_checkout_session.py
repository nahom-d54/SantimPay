

class SantimPayCheckoutSession:


    def __init__(self, id, transcation, totalAmount, test, uuid, created_at, update_at):
    
        self.id = id
        self.transaction = transcation
        self.totalAmount = totalAmount
        self.test = test
        self.uuid = uuid
        self.created_at = created_at
        self.update_at = update_at
    

    def jsonSerialize(self):
    
        return {
            "id" : self.id,
            "transaction" : self.transaction,
            "totalAmount" : self.totalAmount,
            "test" : self.test,
            "uuid" : self.uuid,
            "created_at" : self.created_at,
            "update_at" : self.update_at,
        }
    
    @staticmethod
    def fromJson(json: dict):
        
        return SantimPayCheckoutSession(json["id"], json.get("transaction") if json.get("transaction") else None , json["totalAmount"], json["test"], json["uuid"], json["createdAt"], json["updatedAt"])
    

