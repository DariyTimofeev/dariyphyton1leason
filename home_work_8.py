from pywebio.input import input
from pywebio.output import put_text, put_success, put_error, clear
from pywebio import start_server
import logging

def school_quiz():
    questions = [
        {"question": "Яка планета є найбільшою у Сонячній системі?", "answer": "юпітер"},
        {"question": "Скільки континентів на Землі?", "answer": "7"},
        {"question": "Як називається столиця Франції?", "answer": "париж"},
        {"question": "Який метал є основним у виробництві алюмінієвої фольги?", "answer": "алюміній"},
        {"question": "Скільки кольорів у веселці?", "answer": "7"}
    ]

    user_name = input("Введіть ваше ім'я:")
    logging.info(f"Користувач розпочав вікторину: {user_name}")

    score = 0

    for index, item in enumerate(questions):
        clear()
        user_answer = input(item["question"]).strip().lower()  # Отримуємо відповідь користувача
        if user_answer == item["answer"]:
            put_success("Відповідь вірна!")
            score += 1
        else:
            put_error(f"Неправильно. Правильна відповідь: {item['answer']}")

        logging.debug(
            f"Запитання {index + 1}: '{item['question']}' | Відповідь: '{user_answer}' | Очікувана відповідь: '{item['answer']}'")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    put_text(f"{user_name}, ви набрали {score} балів із {total_questions} ({percentage:.2f}%).")
    logging.info(
        f"Користувач {user_name} завершив вікторину з результатом {score}/{total_questions} ({percentage:.2f}%).")
school_quiz()