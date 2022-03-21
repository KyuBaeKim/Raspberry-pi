from threading import Thread


class Knight(Thread):
    def __init__(self, bridge, name, address): # bridfe <- Lock 공유자원이 관리한다.
        super().__init__() 
        self.bridge = bridge 
        self.name = name 
        self.address = address
    def run(self):
        print(self.name, " 기사가 도전한다.") 
        while True :
            self.bridge.across(self.name, self.address)