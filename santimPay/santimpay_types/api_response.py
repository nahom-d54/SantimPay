class SantimPayAPIResponse:

    def __init__(self, error, msg, data):
    
        self.error = error
        self.msg = msg
        self.data = data
    
    @staticmethod
    def fromJson(json):
    
        return SantimPayAPIResponse(json["error"], json["msg"], json["data"])
    
