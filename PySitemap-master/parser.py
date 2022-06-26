import urllib.request
import re
import os
import log
data = os.listdir('./site_url/')
key_list = "key_slov.txt"
for openf in data:
    list = open("./site_url/"+openf).read().split("\n")
    for url in list:


        urle = url #"https://e-t-a.org/kachestvo/laboratoriya/" #"https://gulyaevip.github.io/"
        keys = open(key_list).read().split("\n")
        stat_key = ""
        try:
            for key in keys:
                text = urllib.request.urlopen(urle).read()
                text = text.decode('UTF-8')
                
                result =re.findall(key, text)
              
                if len(result) > 0:
                    stat_key+= key + " "
            log.site_write(urle+","+stat_key,"./final/final.csv")
            print(urle,stat_key)
        except:
            log.log_write("ошибка сети при парсинге сайта")

# for i in list:
#     if ".html" == i[-5:]:
#         print(i)