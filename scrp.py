# import needed libraries
from bs4 import BeautifulSoup as bs
import requests
import logging
import time

# Error Handling
try :
    # Create and Connect log file
    fileName = str(time.time())
    logging.basicConfig(filename=f'logs/{fileName}.log', encoding='utf-8', level=logging.DEBUG)

    # Fetch data from the web
    webData = requests.get("https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html").text
    beautify = bs(webData, 'html.parser')

    # Get NEWS Heading
    findHeading = beautify.find('div', {'class' : 'headline__wrapper'})
    heading = (findHeading.text).strip()
    logging.info(f'Title : {heading}')
    
    # Get NEWS Article Writer Name
    findArticleWriterName = beautify.find('a', {'class' : 'byline__link'})
    articleWriterName = (findArticleWriterName.text).strip()
    logging.info(f'Written By : {articleWriterName}')

    # Get NEWS Article latest Updated Time
    findLastUpdatedTime = beautify.find('div', {'class' : 'timestamp'})
    lastUpdatedTime = (findLastUpdatedTime.text).strip()
    logging.info(f'Time : Last {lastUpdatedTime}')
    
    # Get NEWS Article Content
    findContent = beautify.find_all('p', {'class' : 'paragraph inline-placeholder'})
    logging.info('Read the NEWS below : ')
    contentFile = ""
    for i in range(len(findContent)) :
        para = (findContent[i].text).strip()
        logging.info(f'{para}')

except Exception as e :
    logging.error(f'Error occurred : {e}')
    
# Done!!