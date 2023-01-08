import stem, time, requests
import stem.connection
from bs4 import BeautifulSoup
from stem import Signal, process
from stem.control import Controller
from urllib.request import Request, urlopen

payload = {
     'csrf': '',
     'username': 'RoyAnony',
     'password': 'My_darkforest_platform23#'
}


torProxy = {
     'http': 'socks5h://localhost:9050',
     'https': 'socks5h://localhost:9050'
}

#drk = 'http://dkforestseeaaq2dqz2uflmlsybvnq2irzn4ygyvu53oazyorednviid.onion'
try:
     tor_process = stem.process.launch_tor_with_config(
          config = {
               'SocksPort': str(9050),
               'ControlPort': str(9051),
               'HashedControlPassword': '16:1C857CDFB72655BE60F9C611148C16CD5CEA64919BFEF7BE4E601901D2'
          },
          #init_msg_handler = print,
          take_ownership = True,
     )
     controller = Controller.from_port(port=9051)
     controller.authenticate("My_torcontroller_platform23#")
     controller.signal(Signal.NEWNYM)
except Exception as e:
     print("Error:", e)

def sesCreate(drk):
     print(drk)
     ses = requests.Session()
     # try:
     #      tor_process = stem.process.launch_tor_with_config(
     #           config = {
     #                'SocksPort': str(9050),
     #                'ControlPort': str(9051),
     #                'HashedControlPassword': '16:1C857CDFB72655BE60F9C611148C16CD5CEA64919BFEF7BE4E601901D2'
     #           },
     #           init_msg_handler = print_bootstrap_lines,
     #           take_ownership = True,
     #      )
     #      controller = Controller.from_port(port=9051)
     #      controller.authenticate("My_torcontroller_platform23#")
     #      controller.signal(Signal.NEWNYM)
     # except Exception as e:
     #      print("Error:", e)
     ses = requests.Session()
     res = ses.get(drk, proxies=torProxy)
     soup = BeautifulSoup(res.text, 'lxml')
     payload['csrf'] = soup.find('input', attrs={'name':'csrf'})['value']

     ses.post(drk, data=payload, proxies=torProxy)
     p = ses.get((drk+"/links"), proxies=torProxy)
     print(p.text)


# def print_bootstrap_lines(line):
#      if "Bootstrpped " in line:
#           print(line)



