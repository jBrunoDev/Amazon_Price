import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com.br/dp/B0D64RQ5CH"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    
    #Titulo
    title = soup.find(id="productTitle")
    if title: 
        title = title.get_text().strip()
        
    else: 
        title = "Título não encontrado"
        
          
    #Preço
    price = soup.find("span", class_="a-offscreen")
    if price: 
        price = price.get_text()
        price = price.replace("R$", "").replace(",", ".").strip()
        converted_price = float(price)
    else:   
        converted_price = "Preço não encontrado"
        
    if(converted_price < 100):
        send_email()


    print(title)
    print(converted_price)
    
    
    if(converted_price > 100):
        send_email()
    
 
    
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('xxbrunoguimaraes@gmail.com', 'aenwmyblqanbwrjq')
    
    # montar mensagem usando o módulo email para cuidar do charset
    from email.message import EmailMessage

    subject = "O preço do produto caiu!"
    body = "Confira o link: https://www.amazon.com.br/dp/B0D64RQ5CH"

    msg = EmailMessage()
    msg["From"] = 'xxbrunoguimaraes@gmail.com'
    msg["To"] = 'xxbrunoguimaraes@gmail.com'
    msg["Subject"] = subject
    msg.set_content(body, charset="utf-8")

    server.send_message(msg)
    print("Email enviado com sucesso!")

    server.quit()
    
    
    
check_price()
 
