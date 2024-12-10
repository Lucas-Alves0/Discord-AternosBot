from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import csv
import io
import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import AuthorizedSession

options = Options()
options.add_argument('--headless=new')  # Ativa o modo headless (novo padrão para versões recentes do Chrome)
options.add_argument('--disable-gpu')  # Desativa a GPU para evitar problemas em ambientes headless
options.add_argument('--window-size=1920x1080')  # Define o tamanho da janela no modo headless

user = {
    'email':'seu-email-aqui@gmail.com',
    'password':'senha1234@'
}
respostas = {
    'Qual era o seu apelido na infância?':'resp1',
    'Qual é o mês e o ano de nascimento do seu irmão mais velho? (por exemplo, janeiro de 1900)':'resp2',
    'Qual cidade você escolheu nunca visitar?':'resp3'
}
driver = webdriver.Chrome(options=options)

# Accessing Netsuite

driver.get('link do site que deseja')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(user['email'])
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(user['password'])
driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()

# Safety Ask Validation

elements = driver.find_elements(By.CSS_SELECTOR, 'td.smalltextnolink.text-opensans')

text = elements[2].text  # Get the text of the third element (0-based index)

resposta = respostas.get(text)
driver.find_element(By.XPATH, '//*[@id="null"]').send_keys(resposta)
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/table/tbody/tr[4]/td/input').click()

cookie = driver.get_cookie('JSESSIONID')

driver.close()

url = 'https://curl-do-botao-de-export/searchresults.csv'
params = {
    'searchtype': 'Transaction',
    'style': 'REPORT',
    'sortcol': 'Transction_ORDTYPE9_raw',
    'sortdir': 'ASC',
    'csv': 'Export',
    'OfficeXML': 'F',
    'pdf': '',
    'size': '1000',
    'twbx': 'F',
    'report': 'T',
    'grid': '',
    'searchid': '3353'
}
headers = {
    'cookie': 'JSESSIONID={};'.format(cookie.get('value')),
}

data_list = []

try:
    response = requests.get(url, params=params, headers=headers, verify=False)
    response.raise_for_status()  # Check for HTTP errors
    pedidos = response.text

    # Parse CSV content
    csv_reader = csv.reader(io.StringIO(pedidos))
    for row in csv_reader:
        data_list.append(row)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file(r"caminho\do\seu\arquivo.json", scopes=scope)
session = AuthorizedSession(creds)
session.verify = False


client = gspread.authorize(creds, session=session)

# Open the Google Sheet by title or ID
spreadsheet_id = 'ID da planilha do google'  # replace with your actual Google Sheet ID
sheet = client.open_by_key(spreadsheet_id).sheet1  # Replace 'sheet1' if accessing a different sheet/tab
sheet.clear()
# Update a cell (e.g., cell A1) with new data
sheet.update('A1', data_list)


print('Spreadsheet updated successfully!')
