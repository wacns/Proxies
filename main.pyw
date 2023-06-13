import requests
import datetime
import os

proxies_urls = [
    'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt',
    'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
    'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
    'https://raw.githubusercontent.com/Bardiafa/Proxy-Leecher/main/good.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/gugun0977/my-proxy-list/main/proxy-list/data.txt',
    'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt',
    'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt'
]

proxies = []

for url in proxies_urls:
    req = requests.get(url)
    proxies.extend(req.text.split('\n'))

unique_proxies = set(proxies)
proxies = list(filter(lambda x: x != '' or x != "" , unique_proxies))
with open('proxies.txt', 'w') as file:
    for proxy in proxies:
        file.write("{}\n".format(proxy.replace("\r", "")))

commit_message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S GMT+3")
readme_string = f"""# Proxies
An automated scraped proxies from various sources

| SCRAPED PROXIES | {len(proxies)}            |
|-----------------|---------------------------|
| DATE            | {commit_message}          |"""
with open('README.md', 'w') as file:
    file.write(readme_string)

os.system('git add .')
os.system('git commit -m "{}"'.format(commit_message))
os.system('git push')
