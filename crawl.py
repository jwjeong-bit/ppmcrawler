# encoding: utf-8
from urllib.request import urlopen
import xmltodict
import json
import sys
import io
from bs4 import BeautifulSoup
import time


region = input('지역명을 입력하세요: ')
yourKey = 'nvJVV6KxQO22I%2FM9V54%2BjEqdDHxsowmlKJ6aJSiHjqUrEZ8x4rLz4IPAJxs%2BipIRoeZw%2Fks6K%2BXFKD5HSWo2tw%3D%3D'
timefile = open("./time.tmp","r")

if float(timefile.read()) < (float(time.time()) - 900) : #15분 경과시
    #get new data
    print ('http get')
    html = urlopen('http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName='+ region +
                   '&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey='+ nvJVV6KxQO22I%2FM9V54%2BjEqdDHxsowmlKJ6aJSiHjqUrEZ8x4rLz4IPAJxs%2BipIRoeZw%2Fks6K%2BXFKD5HSWo2tw%3D%3D+'&ver=1.3')
    data = BeautifulSoup(html.read(), 'html.parser')

    #new cache write
    print ('writing cache...')
    cachef = open("./cache.tmp", 'w')
    cachef.write(str(data))
    cachef.close()

    timef = open("./time.tmp", 'w')
    timef.write(str(time.time()))
    timef.close()
else :
    print ('read cache')
    print ('cache file was made at ' + timefile.read())
    cachefile = open("./cache.tmp", "r")
    data = BeautifulSoup(cachefile.read(), 'html.parser')
    cachefile.close()
timefile.close()
##캐시 종료

result_time = data.datatime.get_text()
result_grade = data.pm10grade.get_text()
result_grade1 = data.pm25grade.get_text()
result_val = data.pm10value.get_text()
result_val1 = data.pm25value.get_text()


print (str (result_time) + '에 측정한 ' + region + '의 대기오염 정보입니다:')

print ('미세먼지 (PM10): ' + str(result_val) + '㎍/㎥ '),

if result_grade == '1' :
    print ("좋음")
elif result_grade == '2' :
    print ("보통")
elif result_grade == '3' :
    print ("나쁨")
elif result_grade == '4' :
    print ("매우나쁨")


print ('초미세먼지 (PM2.5): ' + str(result_val1) + '㎍/㎥ '),

if result_grade1 == '1' :
    print ("좋음")
elif result_grade1 == '2' :
    print ("보통")
elif result_grade1 == '3' :
    print ("나쁨")
elif result_grade1 == '4' :
    print ("매우나쁨")
