import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
import os
init()
print(
    Fore.RED+""" __     ______      ______     ______     __         __  __     ______   __     ______     __   __     ______    
/\ \   /\  == \    /\  ___\   /\  __ \   /\ \       /\ \/\ \   /\__  _\ /\ \   /\  __ \   /\ "-.\ \   /\  ___\   
\ \ \  \ \  _-/    \ \___  \  \ \ \/\ \  \ \ \____  \ \ \_\ \  \/_/\ \/ \ \ \  \ \ \/\ \  \ \ \-.  \  \ \___  \  
 \ \_\  \ \_\       \/\_____\  \ \_____\  \ \_____\  \ \_____\    \ \_\  \ \_\  \ \_____\  \ \_\\"\_\  \/\_____\ 
  \/_/   \/_/        \/_____/   \/_____/   \/_____/   \/_____/     \/_/   \/_/   \/_____/   \/_/ \/_/   \/_____/ 
                                                                                                                
""")
def ip_tracer():
    print(Fore.RED + """ __     ______      ______   ______     ______     ______     ______     ______    
/\ \   /\  == \    /\__  _\ /\  == \   /\  __ \   /\  ___\   /\  ___\   /\  == \   
\ \ \  \ \  _-/    \/_/\ \/ \ \  __<   \ \  __ \  \ \ \____  \ \  __\   \ \  __<   
 \ \_\  \ \_\         \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/   \/_/          \/_/   \/_/ /_/   \/_/\/_/   \/_____/   \/_____/   \/_/ /_/ """)
    print(Style.RESET_ALL)
    ip_address = input('Input Ipaddress\n>')
    url = 'http://ip-api.com/csv/' + str(ip_address) + '?fields=isp'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    isp_str = str(soup)
    isp = isp_str.replace('"', '')
    print('==============================================================')
    print('Proxies ISP provider: ' + isp + '\nTake the ISP name that the program returns and google it')
    print('==============================================================')
def url_ip():
    url = input(
        'Input Url\n>'
    )
    ip = os.system('ping '+url)
    print(ip)
def selector():
    module = input(Fore.WHITE+'\n[1] Ip Tracer\n[2] Url Tracer\n')
    if module == '1':
        ip_tracer()
    if module == '2':
        url_ip()
    else:
        selector()
selector()
