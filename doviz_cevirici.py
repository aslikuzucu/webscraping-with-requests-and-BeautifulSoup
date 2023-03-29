import requests
import sys
url = "http://api.frankfurter.app/latest?from="

birinci_doviz = input("Elinizdeki dövizin birimi: ")
ikinci_doviz=input("Cevirmek istediginiz birim: ")
miktar = float(input("Cevirmek istediginiz miktarı giriniz: "))

response = requests.get(url + birinci_doviz)

json_verisi = response.json()

try:
    print(print(json_verisi["rates"][ikinci_doviz] * miktar))
except KeyError:
    sys.stderr.write("Lutfen para birimlerini dogru giriniz")
    sys.stderr.flush()
