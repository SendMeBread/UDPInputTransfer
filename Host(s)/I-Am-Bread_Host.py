import sys
sys.path += ["../Packages/keyboard", "../Packages/twisted"]
import keyboard
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
class MulticastInputs(DatagramProtocol):
    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup(sys.argv[1])
    def datagramReceived(self, datagram, address):
        print("Host received!")
        if b"1" in datagram:
            keyboard.send("1")
        if b"2" in datagram:
            keyboard.send("2")
        if b"3" in datagram:
            keyboard.send("3")
        if b"4" in datagram:
            keyboard.send("4")
        if b"left" in datagram:
            keyboard.send("left")
        if b"right" in datagram:
            keyboard.send("right")
        if b"up" in datagram:
            keyboard.send("up")
        if b"down" in datagram:
            keyboard.send("down")
reactor.listenMulticast(int(sys.argv[2]), MulticastInputs(), listenMultiple=True)
reactor.run()