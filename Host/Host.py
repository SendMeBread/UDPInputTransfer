import time
import keyboard
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
class MulticastInputs(DatagramProtocol):
    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")
    def datagramReceived(self, datagram, address):
        print("Host received!")
        if b"w" in datagram:
            keyboard.send("w")
        if b"a" in datagram:
            keyboard.send("a")
reactor.listenMulticast(65535, MulticastInputs(), listenMultiple=True)
reactor.run()