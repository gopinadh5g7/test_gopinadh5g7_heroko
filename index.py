# -*- coding: utf-8 -*-
"""YouTube Livestream View BOT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YVutWC43FMwNn22jcEHUs8cuOEa7JdRj
"""

import os
import random
import string
import threading
import time
import random
from queue import Queue
import platform
import requests
!pip install colorama
from colorama import Fore, init
from IPython.display import clear_output
intro = """
███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗      ██████╗  ██████╗ ████████╗████████╗███████╗██████╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║      ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║█████╗██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔╝
╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║╚════╝██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗
███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║      ██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
 
https://github.com/KevinLage/YouTube-Livestream-Botter
"""
print(intro)
intro = ""
if platform.system() == "Windows": #checking OS
    clear = "cls"
else:
    clear = "clear"

UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3",
    "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254",
    "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536",
    "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058",
    "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
    "Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US",
    "Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU")

class main(object):
    def __init__(self):
        self.combolist = Queue()
        self.Writeing = Queue()
        self.printing = []
        self.botted = 0
        self.bots = 0
        self.alive = True
        self.killed = False
        self.combolen = self.combolist.qsize()
    def isAlive(self):
      return not self.killed
    def printservice(self): #print screen
        # while True:
            if not self.alive:
              self.killed = True
              # break
            try:
              if True:
                os.system(clear)
                clear_output(wait=True)
                print(Fore.LIGHTCYAN_EX + intro + Fore.LIGHTMAGENTA_EX)
                print(Fore.LIGHTCYAN_EX + f"bots:{self.bots}\n")
                print(Fore.LIGHTCYAN_EX + f"Botted:{self.botted}\n")
                for i in range(len(self.printing) - 10, len(self.printing)):
                    try:
                        print(self.printing[i])
                    except (ValueError, Exception):
                        pass
                time.sleep(0.1)
            except KeyboardInterrupt:
              print("Keyboard interrupt exception caught")
              # break
            except IndexError:
              hi = 1
              # pass
            except Exception as e:
              hi = 1
              # print("main: ",end="")
              # print(e)
              # pass
"Main"

class Proxy():
    global proxy_loading
    global threads
    def update(self):
      proxy_loading = '1'
      while True:
            if not self.alive:
              self.killed = True
              break
            self.choose = []
            splitted = []
            if proxy_loading == "2":
                data = open("proxys.txt", "r").read()
                splitted += data.split("\n") #scraping and splitting proxies
            else:
                # urls = ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=4200&ssl=yes",
                #         "https://www.proxy-list.download/api/v1/get?type=https&anon=elite"]
                http = []
                urls = ["https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                        "https://api.proxyscrape.com/?request=getproxies&proxytype=http",
                        "https://www.proxy-list.download/api/v1/get?type=https&anon=elite"
                        "https://www.proxy-list.download/api/v1/get?type=http&anon=elite"]
                for url in urls:
                    response = requests.get(url)
                    if response.status_code != 200:
                      pass
                    data = response.text.rstrip()
                    data = "".join([i for i in data.split("\r")])
                    # print(data)
                    http += data.split("\n") #scraping and splitting proxies
                    # break
                http = http[2::]
            if len(http) > 0:
              self.splited = http
              # print(self.splited)
            self.index = 0
            time.sleep(600)
            # break
    def isAlive(self):
      return not self.killed
    def get_proxy(self,call=0):
        if len(self.splited) < 1:
          time.sleep(10)
          return self.get_proxy(call)
        choice = random.choice(self.splited) #choose a random proxie
        if call > 3:
          return choice
        if choice in self.choose:
          return self.get_proxy(call+1)
        # else:
          # self.choose.append(choice)
        # self.index = (self.index + 1) % len(self.splited)
        # return self.splited[self.index]
        return choice
    def FormatProxy(self,proxy = None):
        if proxy == None:
          proxy = self.get_proxy()
        # print(proxyOutput)
        proxyOutput = {'https' :'https://'+proxy,"http":'http://'+proxy}
        return [proxy,proxyOutput]
    def __init__(self):
        self.choose = []
        self.splited = {}
        self.alive = True
        self.killed = False
        self.index = 0
        self.failed_proxies = dict()
        self.updated = []
        # self.update()
        t = threading.Thread(target=self.update)
        t.start()
        threads.append(self)
        time.sleep(((random.random() * 100 ) % 20) + 5)
"Proxy"

class Bot:
  def __init__(self):
    self.alive = True
    self.killed = False
  def isAlive(self):
    return not self.killed
  def run(self):
    global a
    fails = 0
    proxy = proxy1.FormatProxy()
    proxyOut = proxy[0]
    proxy = proxy[1]
    # ua = random.choice(UA)
    while True:
        if not self.alive:
          self.killed = True
          break
        try:
            ua = random.choice(UA)
            # proxy = proxy1.FormatProxy()
            s = requests.session()
            resp = s.get("https://m.youtube.com/watch?v=" + token,
                         headers={
                             'Host': 'm.youtube.com', 
                             'Proxy-Connection': 'keep-alive', 
                             'User-Agent': ua, 
                             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
                             'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7', 
                             'Accept-Encoding': 'gzip, deflate'
                          }, 
                         proxies=proxy)   # simple get request to youtube for the base URL
            if resp.status_code != 200:
              fails += 1
              pass
            # print(resp.text)
            # r = (random.random() * 10) % 3
            # time.sleep(1 + r)
            url = resp.text.split(r'videostatsWatchtimeUrl\":{\"baseUrl\":\"')[1].split(r'\"}')[0].replace(r"\\u0026",r"&").replace('%2C',",").replace("\/","/")  #getting the base url for parsing
            cl = url.split("cl=")[1].split("&")[0] #parsing some infos for the URL
            ei = url.split("ei=")[1].split("&")[0]
            of = url.split("of=")[1].split("&")[0]
            vm = url.split("vm=")[1].split("&")[0]
            # proxy = proxy1.FormatProxy()
            resp = s.get("https://s.youtube.com/api/stats/watchtime?ns=yt&el=detailpage&cpn=isWmmj2C9Y2vULKF&docid=" + token + "&ver=2&cmt=7334&ei=" + ei + "&fmt=133&fs=0&rt=1003&of=" + of +"&euri&lact=4418&live=dvr&cl=" + cl + "&state=playing&vm=" + vm + "&volume=100&c=MWEB&cver=2.20200313.03.00&cplayer=UNIPLAYER&cbrand=apple&cbr=Safari%20Mobile&cbrver=12.1.15E148&cmodel=iphone&cos=iPhone&cosver=12_2&cplatform=MOBILE&delay=5&hl=ru&cr=GB&rtn=1303&afmt=140&lio=1556394045.182&idpj=&ldpj=&rti=1003&muted=0&st=7334&et=7634",
                         headers={
                             'Host': 's.youtube.com', 
                             'Proxy-Connection': 'keep-alive', 
                             'User-Agent': ua, 
                             'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5', 
                             'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 
                             'Referer': 'https://m.youtube.com/watch?v=' + token
                          },
                         proxies=proxy)   # API GET request
            if resp.status_code != 200:
              fails += 1
              pass
            a.botted += 1
            r =  (0.5 + random.random() * 10) % 2
            time.sleep(1 + r)
            fails = 0
            proxy1.failed_proxies[proxyOut] = 0
            # break
        except KeyboardInterrupt:
            print("Keyboard interrupt exception caught")
            break
        except IndexError:
          pass
        except Exception as e:
            # print(e)
            fails+=1
            a.bots -= 1
            time.sleep(3)
            a.bots += 1
            if fails > 10:
              a.bots -= 1
              time.sleep(180)
              a.bots += 1
              fails = 0
              # ua = random.choice(UA)
              if proxyOut not in proxy1.failed_proxies.keys():
                proxy1.failed_proxies[proxyOut] = 0
              proxy1.failed_proxies[proxyOut] += 1
              if proxy1.failed_proxies[proxyOut] > 10:
                proxy1.choose.append(proxyOut)
              proxy = proxy1.FormatProxy()
              proxyOut = proxy[0]
              proxy = proxy[1]
            pass
        # time.sleep(random.random())
"Bot"

# threads = []
# proxy1 = proxy()

# p = proxy1.FormatProxy()
# s = requests.session()
# print(p)
# r = s.get("https://www.google.com",proxies=p,verify=False,timeout=10)

# print(r.text)

def worker():
  global threads,num,a
  if len(proxy1.splited) < 1:
    time.sleep(15)
  # maxthreads -= 3
  num = 3
  a.botted = 0
  # while True:
  a.bots = maxthreads
  # print("here")
  while num < maxthreads :
    num += 1
    t = Bot()
    threading.Thread(target=t.run).start()
    threads.append(t)
    # if num%250 == 0:
    #   time.sleep((random.random() * 100) % 100)
    # elif num%100 == 0:
    #   time.sleep((random.random() * 100) % 50)
    # elif num%10 == 0:
    #   time.sleep((random.random() * 100) % 25)
    # elif num%5 == 0:
    #   time.sleep((random.random() * 10) % 5)
"Worker"

threads = []
killer = False
 
proxy_loading = 1 #input("[1] Load Proxys from APIs\n[2] Load Proxys from proxys.txt\n")
 
a = main()
proxy1 = Proxy()

# t = threading.Thread(target=a.printservice)
# t.start()
# threads.append(a)
token = "BOT"
maxthreads = 500 #int(input("How many Threads? Recommended: 500 - 1000\n"))
t = threading.Thread(target=worker)
t.start()

"loaded"

token = "h0G1-ojcUV4"
if token == "" or token == "BOT":
  token = input("ID?\n")
while True:
  a.printservice()
  time.sleep(1)
  pass

# killer = True
# print(killer)
# print(len(threads))
os.system(clear)
clear_output(wait=True)
while len(threads) > 0:
  nthreads = []
  count = 0
  error = 0
  for t in threads:
    try:
      if t.isAlive() is True:
        t.alive = False
        count += 1
        nthreads.append(t)
        # print(t)
      # t.join()
    except Exception as e:
      # print(e,end="")
      error += 1
      pass
  print("count",count,"error",error)
  # time.sleep(10)
  threads = nthreads
  break
  # print("DONE")
"Killed"
