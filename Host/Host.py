from threading import Thread
import keyboard
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
class MulticastInputs(DatagramProtocol):
    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")
    def datagramReceived(self, datagram, address):
        print("Host received!")
        if datagram == b"w" or datagram == "w":
            w_key()
        if datagram == b"a" or datagram == "a":
            s_key()

def w_key():
    if keyboard.is_pressed('w'):
        keyboard.release('w')
    else:
        keyboard.press('w')
def s_key():
    if keyboard.is_pressed('w'):
        keyboard.release('w')
    else:
        keyboard.press('w')
reactor.listenMulticast(65535, MulticastInputs(), listenMultiple=True)
reactor.run()