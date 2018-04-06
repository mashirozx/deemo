import os
from os import listdir
from os.path import isfile, join

path = 'tiny/'

with open('test.html', 'r',encoding='utf8') as file:
    data=file.read()

with open('style.css', 'r',encoding='utf8') as file:
    style=file.read()

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

str = ''

for f in onlyfiles:
    str = str + '''
       <div class="mySlides fade">
            <img class="deemo-draw" data-src="https://static.xn--ipython-y98d.tk/tiny/''' + f + '''">
        </div>'''

data = data.replace('{python-work-area}', str).replace('{python-style}', style) 
        
with open("index.html", "w",encoding='utf8') as text_file:
    print(data, file=text_file)