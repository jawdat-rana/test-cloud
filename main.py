import requests
from bs4 import BeautifulSoup

numbers = ['3422817264']

success = 0
fail = 0

#crawler
for n in numbers:

  try:
    url = 'http://lifetech.tech/?number={}'.format(n)
    page = requests.get(url)
  
  except Exception as err:
    print(err)
    fail += 1
    continue
  
  else:
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find("table")

    success += 1

    # this should be stored as it is in some DB
    # and later processed by a separate ETL process
    print(table)

print('Success: {}, Fails: {}'.format(success, fail))
