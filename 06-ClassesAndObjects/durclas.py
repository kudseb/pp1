'''
#7
class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname="Universytet Ekonomiczny w Krakowie"
    # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    def print_fullname(self):
         print(self.fullname)
    def set_name(self,nowa):
        self.name=nowa
    def set_fullname(self,newfull):
        self.fullname=newfull
    
        
x=University()
x.print_name()
print()
#8
x.set_name('kue')
x.print_name()
print()
#9
x.print_fullname()
x.set_fullname('??????????')
x.print_fullname()
print()
'''
#10
class TV(object):
    def __init__(s):
        s.is_on=False
        #11
        s.channel_no=1
        s.channels=[]
        s.volume=0
    def on(s):
        s.is_on=True
    def off(s):
        s.is_on=False
    def vol_up(s):
        if s.volume <10:
            s.volume+=1
    def vol_down(s):
        if s.volume>0:
            s.volume-=1
    #12
    def change_channel(s,chan):
        s.channel_no=chan
    #13
    def set_channels(s,chans):
        s.channels+=chans
    def show_channels(s):
        j=1
        for i in s.channels:
            print(f'{j}. {i}')
            j+=1
    def show_status(s):
        #11
        if not(s.is_on):
            print(f"Telewizor jest wyłączony ")
        elif not(s.channels):
            print(f"Telewizor jest właczony i jest na kanale {s.channel_no}. Glośnosc :{s.volume} ")
        else:
            print(f"Telewizor jest właczony i jest na kanale {s.channel_no} {s.channels[s.channel_no-1]}. Glośnosc :{s.volume}")
            
o10=TV()
o10.show_status()
o10.on()
o10.show_status()
o10.change_channel(5)
o10.show_status()
print()
o10.set_channels(['TVP1', 'TVP2', 'Polsat' ,'TVN 5', 'Filmbox'])
o10.show_channels()
o10.vol_up()
o10.vol_up()
o10.vol_up()
o10.show_status()
print()
#16
import ksiazka
ay=ksiazka.ebook('Chodźby Góry','S.Rauy',420)
ay.open_book()
print(ay)
ay.next_page()
ay.next_page()
ay.next_page()
ay.next_page()
print(ay)
ay.close_book()
ay.next_page()