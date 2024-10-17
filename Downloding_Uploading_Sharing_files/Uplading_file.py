import requests
from bs4 import BeautifulSoup
url = 'https://removal.ai/upload'
file = open("me.jpg", 'rb')
# '<input type="file" class="form-control rm-upload-file" id="rm_free_upload_file" '
#  'name="rm_file_upload" '
#  'accept="image/png,image/jpg,image/jpeg">'

req = requests.get(url=url,files={"rm_file_upload":file})

with open('req.html','w') as html:
    html.write(req.text)

soup = BeautifulSoup(req.text, 'html.parser')



d_link = soup.find('a', class_='rm-bt-main-color rm-bt rm-bt-download rm-bt-download-preview rm-transition rm-text-center')
href = d_link['href']

image = requests.get(href).content
with open("bg.png", 'wb') as file:
    file.write(image)
