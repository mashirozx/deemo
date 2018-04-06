import os
from os import listdir
from os.path import isfile, join

path = 'trans/'

with open('test.html', 'r',encoding='utf8') as file:
    data=file.read()

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

str = ''

for f in onlyfiles:
    str = str + '''
       <div class="mySlides fade">
            <img data-src="trans/''' + f + '''">
        </div>'''

data = data.replace('{python-work-area}', str) 
        
with open("index.html", "w",encoding='utf8') as text_file:
    print(data, file=text_file)