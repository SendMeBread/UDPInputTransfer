from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
import keyboard
keys = ['w', 'a', 's', 'd']
class MulticastPingClient(DatagramProtocol):
    def startProtocol(self):
        self.transport.joinGroup("228.0.0.5")
        while True:
            key = keyboard.read_key()
            if key in keys:
                self.transport.write(bytes(key, encoding='utf-8'), ("228.0.0.5", 65535))
    def datagramReceived(self, datagram, address):
        #print(f"Datagram {repr(datagram)} received from {repr(address)}")
        pass
reactor.listenMulticast(65535, MulticastPingClient(), listenMultiple=True)
reactor.run()