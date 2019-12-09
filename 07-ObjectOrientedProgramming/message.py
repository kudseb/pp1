class Message():
    def __init__(self):
        self.message = ''
    def set_message(self,message):
        wiad=''
        wiad+=message[0].upper()
        if len(message)>1:
            for i in range(1,len(message)):
                wiad+=message[i].lower()
        self.message = wiad +' bye'
