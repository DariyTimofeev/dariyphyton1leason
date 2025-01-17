import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader

car_data = {
    "car_brand": "Tesla",
    "car_model": "Model S",
    "car_year": 2023,
    "car_price": 95000,
    "car_seats": 5,
    "car_options": [
        "Шкіряний салон",
        "Система підігріву сидінь",
        "Система масажу сидінь",
        "Система безключового доступу (Keyless Entry)",
        "Пам'ять положення сидінь і дзеркал",
        "Інформаційно-розважальна система із сенсорним дисплеєм",
        "Apple CarPlay/Android Auto",
        "Бездротова зарядка для смартфонів",
        "Wi-Fi точка доступу",
        "Система автоматичного гальмування",
        "Асистент утримання в смузі",
        "Контроль сліпих зон",
        "360-градусна камера огляду",
        "Парктроніки (передні та задні)",
        "Розпізнавання дорожніх знаків"
    ]
}

env = Environment(loader=FileSystemLoader('templates'))  # Шлях до шаблонів
template = env.get_template('email_template.html')

html_content = template.render(
    car_brand=car_data["car_brand"],
    car_model=car_data["car_model"],
    car_year=car_data["car_year"],
    car_price=car_data["car_price"],
    car_seats=car_data["car_seats"],
    car_options=car_data["car_options"]
)

sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
password = "your_email_password"  # Введіть пароль

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = f"Рекламний лист: {car_data['car_brand']} {car_data['car_model']}"

msg.attach(MIMEText(html_content, 'html'))

try:
    with smtplib.SMTP('smtp.example.com', 587) as server:  # Використовуйте правильний SMTP сервер
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Лист успішно надіслано!")
except Exception as e:
    print(f"Не вдалося надіслати лист: {e}")