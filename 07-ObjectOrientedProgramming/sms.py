import message
class SMS(message.Message):
    def __init__(s,txt,nrtelnad,nrtelodb):
        message.Message.set_message(s,txt)
        s.nrtelnad=nrtelnad
        s.nrtelodb=nrtelodb
    def send(s):
        print('Wysyłanie sms...')
        print(f'{"od:":<10}{s.nrtelnad}')
        print(f'{"do:":<10}{s.nrtelodb}')
        print(f'{"Tresc:":<10}{s.message}')
s=SMS('AYYYYYyyooo','78946445','78979455',)
s.send()