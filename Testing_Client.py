from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
import time

class MulticastPingClient(DatagramProtocol):
    def startProtocol(self):
        self.transport.joinGroup("228.0.0.5")
        self.transport.write(b"w", ("228.0.0.5", 65535))
        time.sleep(4)
        self.transport.write(b"w", ("228.0.0.5", 65535))
    def datagramReceived(self, datagram, address):
        print(f"Datagram {repr(datagram)} received from {repr(address)}")


reactor.listenMulticast(65535, MulticastPingClient(), listenMultiple=True)
reactor.run()