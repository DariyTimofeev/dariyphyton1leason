from pywebio.input import input
from pywebio.output import put_text, put_success, put_error, clear, put_markdown
import logging

questions = [
    {"question": "Яка планета є найбільшою у Сонячній системі?", "answer": "юпітер"},
    {"question": "Скільки континентів на Землі?", "answer": "7"},
    {"question": "Як називається столиця Франції?", "answer": "париж"},
    {"question": "Який метал є основним у виробництві алюмінієвої фольги?", "answer": "алюміній"},
    {"question": "Скільки кольорів у веселці?", "answer": "7"},
]


def quiz():

    name = input("Введіть своє ім'я:")
    put_markdown(f"## Привіт, {name}! Почнемо вікторину 🚀")

    score = 0

    for idx, q in enumerate(questions):
        clear()
        put_markdown(f"### Запитання {idx + 1}: {q['question']}")
        user_answer = input("Ваша відповідь:")

        if user_answer.strip().lower() == q["answer"]:
            put_success("Правильно! 🎉")
            score += 1
        else:
            put_error("Неправильно! 😞")

        logging.debug(f"Користувач '{name}' відповів '{user_answer}' на запитання '{q['question']}'")

    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    put_markdown(f"## Ви відповіли правильно на {score} з {total_questions} запитань ({percentage:.2f}%)!")

    logging.info(f"Користувач '{name}' набрав {score}/{total_questions} ({percentage:.2f}%) балів")


if __name__ == "__main__":
    from pywebio import start_server

    start_server(quiz, port=8080)