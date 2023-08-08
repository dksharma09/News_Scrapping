from bs4 import BeautifulSoup as bs
import requests
import logging
import time

fileName = str(time.time())

logging.basicConfig(filename=f'logs/{fileName}.log', encoding='utf-8', level=logging.DEBUG)

webData = requests.get("https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html").text
beautify = bs(webData, 'html.parser')

findHeading = beautify.find('div', {'class' : 'headline__wrapper'})
heading = (findHeading.text).strip()
logging.info(f'Title : {heading}')

findContent = beautify.find_all('p', {'class' : 'paragraph inline-placeholder'})
print(len(findContent))

# findHeader2 = beautify.find_all('h2', {'class' : 'subheader'})
# print(len(findHeader2))
# print(findHeader2[0].text)
logging.info('Read the NEWS below : ')
for i in range(len(findContent)) :
    para = (findContent[i].text).strip()
    logging.info(f'{para}')

# heading = findHeading.text

# Content = findContent.text
# print(heading)
# log heading
# logging.info(f'Title : {Content}')