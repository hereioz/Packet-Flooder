import socket, random, argparse, time


class __main__:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Packet Sniffer')
        self.parser.add_argument('-i',  dest='IP', type=str ,help='Destnation IP Address', required=True)
        self.parser.add_argument('-p',  dest='Port', type=int ,help='Destnation Port', required=True)
        self.parser.add_argument('-c',  dest='Count', default=999**99999, type=int ,help='Packet Sent Count', required=False)
        self.parser.add_argument('-v', dest='pCount', default="y", type=str ,help='Print Packet Send Count [Y/n]', required=False)
        self.parser.add_argument('-s',  dest="sleep", default=0, type=int ,help='Sleep Time Between Packets', required=False)
        self.parser.add_argument('-m', dest='message', default="random", type=str , help="Data to Sent", required=False)
        self.args = self.parser.parse_args()
        
    def getPcount(self):
        if (self.args.pCount.lower() == "y"):
            self.pCount = True
        else:
            self.pCount = False

        return self.pCount



class Sniffer:
    def __init__(self, ip, port, count, pCount, sleep, data):
        self.ip = ip
        self.port = port
        self.counter = 0
        self.count = count
        self.pCount = pCount
        self.sleep = sleep
        self.data = data

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect(self):
        self.connection.connect((self.ip, int(self.port)))

    def send(self):
        for i in range(0, self.count):
            try:
                if (self.data == "random"):
                    self.connection.send(random._urandom(10)*100)
                else:
                    self.connection.send(self.data.encode("utf-8"))
                    
                self.counter+=1
                if (self.pCount):
                    print(f"Sending... {self.counter}", end="\r")
                    
                time.sleep(self.sleep)
                
            except KeyboardInterrupt:
                self.counter = 0
                break
        print("")
        
    def close(self):
        self.connection.close()


main = __main__()
Sniffing = Sniffer(main.args.IP, main.args.Port, main.args.Count, main.getPcount(), main.args.sleep, main.args.message)
Sniffing.connect()
Sniffing.send()
Sniffing.close()
