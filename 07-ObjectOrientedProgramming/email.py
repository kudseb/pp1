import message
class Email(message.Message):
    def __init__(s,txt,mailnad,mailodb,temat):
        #super().__init__()
        message.Message.set_message(s,txt)
        s.mailnad=mailnad
        s.mailodb=mailodb
        s.temat=temat
    def send(s):
        print('Wysyłanie emaila...')
        print(f'{"od:":<10}{s.mailnad}')
        print(f'{"do:":<10}{s.mailodb}')
        print(f'{"Temat:":<10}{s.temat}')
        print(f'{"Tresc:":<10}{s.message}')
s=Email('halo','do@mail.net','od@ddd.net','duzaaa')
s.send()