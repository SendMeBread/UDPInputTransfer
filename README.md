<h1>Keyboard Input Transfer (via UDP)</h1>
<h2>This system takes keyboard input from a client computer and sends it to the host computer...</h2>
<h3>(Made for a group of friends, still in development)</h3>

---

<h4>The caveat is that each client can only send <strong>one</strong> input.</h4>

<h3>Host Example:</h3>

```python3
#Required Python3 host libraries:
import keyboard
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
class MulticastInputs(DatagramProtocol):
    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")
    def datagramReceived(self, datagram, address):
	#Send keystrokes to host (this) computer
	#Print("Host recieved!) Use for debugging
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
#Start listening for clients
reactor.listenMulticast(65535, MulticastInputs(), listenMultiple=True)
reactor.run()
```

---

<h3>Client Example:</h3>

```python3
from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol
import keyboard
class MulticastPingClient(DatagramProtocol):
    def startProtocol(self):
        self.transport.joinGroup("228.0.0.5")
        while True:
            key = keyboard.read_key()
            if key == "a": #If the A key was pressed
                self.transport.write(bytes(key, encoding='utf-8'), ("228.0.0.5", 65535)) #send a string, "a"
    def datagramReceived(self, datagram, address):
        #print(f"Datagram {repr(datagram)} received from {repr(address)}") Use for debugging
	pass
#Start looking for hosts on the network
reactor.listenMulticast(65535, MulticastPingClient(), listenMultiple=True)
reactor.run()
```
