import sys
sys.path.append("../Packages")
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
import keyboard
class MulticastPingClient(DatagramProtocol):
    def startProtocol(self):
        self.transport.joinGroup(sys.argv[2])
        while True:
            key = keyboard.read_key()
            if key == "down":
                self.transport.write(bytes(key, encoding='utf-8'), (sys.argv[1], 65535))
    def datagramReceived(self, datagram, address):
        print(f"Datagram {repr(datagram)} received from {repr(address)}")
reactor.listenMulticast(int(sys.argv[1]), MulticastPingClient(), listenMultiple=True)
reactor.run()