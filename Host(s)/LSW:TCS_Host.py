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
            keyboard.send("1")
        if b"a" in datagram:
            keyboard.send("2")
        if b"s" in datagram:
            keyboard.send("3")
        if b"d" in datagram:
            keyboard.send("4")
        if b"k" in datagram:
            keyboard.send("left")
        if b"j" in datagram:
            keyboard.send("right")
        if b"q" in datagram:
            keyboard.send("up")
        if b"e" in datagram:
            keyboard.send("down")
reactor.listenMulticast(65535, MulticastInputs(), listenMultiple=True)
reactor.run()