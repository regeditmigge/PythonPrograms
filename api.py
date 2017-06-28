import http.client
import base64
import json
import sys
import os

#控制台参数判空
if len(sys.argv) <= 1:
    print("ContractCode Empty")
    sys.exit()

#调接口
conn = http.client.HTTPConnection("接口地址")
headers = {
    'authorization': "Todo: Basic Auth String",
    'cache-control': "no-cache"
    }
conn.request("GET", "/api/EContracts/%s" % sys.argv[1], headers=headers)
res = conn.getresponse()
data = res.read()

json = json.loads(data.decode("utf-8"))

if json["ErpContractCode"] == None:
    print("Not Found File")
    sys.exit()

#Base64解码文件流
pdfBytes = base64.b64decode(json["File"]["Data"])

#保存文件
filePath = "%s\%s.pdf" % (os.path.split(os.path.realpath(__file__))[0], json["ErpContractCode"])
with open(filePath, "wb") as f:
    f.write(pdfBytes)

print(res.status)