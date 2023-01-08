import stem
import stem.connection

from stem import Signal, process
from stem.control import Controller
from bs4 import BeautifulSoup
import requests
import re
import csv
import os
import login


payload = {
     'csrf': '',
     'username': 'RoyAnony',
     'password': 'My_darkforest_platform23#'
}

proxies = {
  'http': 'socks5h://localhost:9050',
  'https': 'socks5h://localhost:9050'
}

# def search():
#      count=0
#      a=input("enter the word to be searched")
#      f= open("link"+K+".txt",'r')
#      for i in f:
#         words=i.split()
#         for j in words:
#            if(j==a):
#             count+=1
#      print(count)
#      y=input("Do you want to Search again Y/N")
#      if y=="Y" or y=="y":
#           search()
#      else:
#          pass



# def scrape_link():
#   t=open("links.csv")
#   lst=t.readlines()
#   l=len(lst)
#   for i in range(0,l):
#     global k
#     res=requests.get(lst[i])
#     soup=BeautifulSoup(res.content, 'html.parser')
#     K=str(i)
#     b=str(soup.get_text().encode("utf-8").strip())
#     f=open("link"+K+".txt", 'w')
#     f.write(b)
#     f.close()
#     f=open("link"+K+".txt", 'r')
#     data=f.read()
#     lst=data.split(" ")
#     with open("abc"+K+".csv", 'w', newline='') as f:
#       writer=csv.writer(f)
#       writer.writerow(list)
#     x=input("Do you want to search Y/N")
#     if(X=="Y" or "y"):
#       search()
#     else:
#       pass
# def sesCreate(drk):
#      ses = requests.Session()
#      try:
#           tor_process = stem.process.launch_tor_with_config(
#                config = {
#                     'SocksPort': str(9050),
#                     'ControlPort': str(9051),
#                     'HashedControlPassword': '16:1C857CDFB72655BE60F9C611148C16CD5CEA64919BFEF7BE4E601901D2'
#                },
#                init_msg_handler = print_bootstrap_lines,
#                take_ownership = True,
#           )
#           controller = Controller.from_port(port=9051)
#           controller.authenticate("My_torcontroller_platform23#")
#           controller.signal(Signal.NEWNYM)
#      except Exception as e:
#           print("Error:", e)
#      ses = requests.Session()
#      res = ses.get(drk, proxies=proxies)
#      soup = BeautifulSoup(res.text, 'lxml')
#      payload['csrf'] = soup.find('input', attrs={'name':'csrf'})['value']

#      ses.post(drk, data=payload, proxies=proxies)
#      p = ses.get((drk+"/links"), proxies=proxies)
#      print(p.text)


def scrape_link():
  t=open("links.csv")
  lst=t.readlines()
  l=len(lst)
  # print("\n")
  # print(lst[0])
  for i in range(0,l):
    send_requests1(lst[i])
    if(lst[i].startswith('http://dkforest')):
      string=lst[i][:-2]

      login.sesCreate(string)


def send_requests1(link):
  try:
    # with Controller.from_port(port=9051) as controller:
    #   controller.authenticate()
      
    #   controller.signal(Signal.NEWNYM)
    response=requests.get(link,proxies=proxies)
    html_code=response.text
    #print(html_code)
  except Exception as e:
    print("Error:", e)



def get_links(html_source_code):
  soup = BeautifulSoup(html_source_code, 'html.parser')

# Find all the links in the HTML
  links = soup.find_all('a')

# Create an empty list to store the links
  link_list = []
  final_link_list=[]

# Iterate through the links and extract the href attribute
  for link in links:
      str = link.get('href').split("redirect_url=")
      if(len(str)==2):
        link_list.append(str[1])
  for link in link_list:
    str=link.split(".onion/")
    if(len(str)==2):
      final_link_list.append(str[0]+'.onion/')
    else:
      final_link_list.append(link)
  for link in final_link_list:
    print(link)
  with open("links.csv", 'w', newline='') as csv_file:
    writer=csv.writer(csv_file)
    for row in final_link_list:
      writer.writerow([row])
  scrape_link()



def send_request():
  # Make a request to a website through TOR
  try:
    # Send an HTTP request through the TOR network
    keyword=input("Enter keyword: ")
    response = requests.get('https://ahmia.fi/search/?q='+keyword)

    #print(response.text)
    html_source_code=response.text
    get_links(html_source_code)
  except Exception as e:
    print("Error:", e)

# Start the TOR process and create a controller
# def start_tor():
#   try:
#     # Start an instance of TOR
#     tor_process = stem.process.launch_tor_with_config(
#       config = {
#         'SocksPort': str(9050),
#         'ControlPort': str(9051)
#       },
#       init_msg_handler = print_bootstrap_lines,
#     )

#     # Create a controller object
#     controller = Controller.from_port(port = 9051)
#     controller.authenticate()

#     # Create a new circuit
#     controller.signal(Signal.NEWNYM)
#     print("New circuit created")

#     # Send an HTTP request through the TOR network
    
#   except Exception as e:
#     print("Error:", e)

# def print_bootstrap_lines(line):
#   if "Bootstrpped " in line:
#     print(line)

# Start TOR and send an HTTP request

send_request()