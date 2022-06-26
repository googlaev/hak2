import os
site_list = open("site.txt").read().split("\n")
for i in site_list:
    url_name = i
    s = i.replace("/","_")
    file_name = "./site_url/"+s+".txt"
    comand = f'python3 main.py --url="{url_name}" --output="{file_name}" --no-verbose'
    os.system(comand)
