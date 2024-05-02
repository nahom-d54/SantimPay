class SantimPayCheckoutRequest:

    def __init__(
        self, 
        id,
        amount,
        paymentReason,
        successRedirectUrl,
        failureRedirectUrl,
        notifyUrl,
        cancelRedirectUrl,
        direct = False
    ):
        self.id = id
        self.amount = amount
        self.paymentReason = paymentReason
        self.successRedirectUrl = successRedirectUrl
        self.failureRedirectUrl = failureRedirectUrl
        self.notifyUrl = notifyUrl
        self.cancelRedirectUrl = cancelRedirectUrl
        self.direct = direct
    

    def jsonSerialize(self):
    
        if self.direct:
            return {
                'id' : self.id,
                'amount' : self.amount,
                'reason' : self.paymentReason,
                'notifyUrl' : self.notifyUrl,
            }
        return {
            'id' : self.id,
            'amount' : self.amount,
            'reason' : self.paymentReason,
            'successRedirectUrl' : self.successRedirectUrl,
            'failureRedirectUrl' : self.failureRedirectUrl,
            'notifyUrl' : self.notifyUrl,
            'cancelRedirectUrl' : self.cancelRedirectUrl,
        }
    

