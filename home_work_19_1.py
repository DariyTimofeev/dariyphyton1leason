import requests

pdf_url = 'https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf'

response = requests.get(pdf_url)

if response.status_code == 200:
    with open('Smyk-tyndyk.pdf', 'wb') as f:
        f.write(response.content)
    print('PDF файл успішно завантажено!')
else:
    print('Не вдалося завантажити PDF файл.')