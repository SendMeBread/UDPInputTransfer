import sys
sys.path += ["../Packages/keyboard", "../Packages/twisted"]
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
import keyboard
class MulticastPingClient(DatagramProtocol):
    def startProtocol(self):
        self.transport.joinGroup(sys.argv[1])
        while True:
            key = keyboard.read_key()
            if key == "3":
                self.transport.write(bytes(key, encoding='utf-8'), (sys.argv[1], 65535))
    def datagramReceived(self, datagram, address):
        print(f"Datagram {repr(datagram)} received from {repr(address)}")
reactor.listenMulticast(int[sys.argv[2]], MulticastPingClient(), listenMultiple=True)
reactor.run()