import requests

url = 'https://carmax.com/cars/acura'
url = 'https://www.carmax.com/car/15527502'
url = 'http://autos.vast.com/cars'

with open('acura.html', 'w') as fh:
    resp = requests.get(url) #, verify="/etc/ssl/certs/ca-certificates.crt")
    fh.write(resp.text.encode('utf8'))

'''
acura 993
buick 1368
chrysler 1229
ford 5922
honda 3504
infinity 1485
kia 2081
lincoln 500
mercury 26
nissan 6598
saturn 14
subaru 929
volvo 366
audi 933
cadillac 1245
dodge 2698
genesis 13
hummer 1
jaguar 167
land rover 211
mazda 883
mini 476
pontiac 14
scion 231
toyota 5677
bmw 1936
chevrolet 5436
fiat 374
gmc 1616
hyundai 3067
jeep 3146
lexus 1930
mercedes benz 1974
mitsubishi 294
porsche 150
smart 98
volkswagen 1255

total cars: 58840
total pages: 1177
avg time page scrape: 39 min
avg time car scrape: 


