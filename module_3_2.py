#     1 Создайте функцию send_email, которая принимает 2 обычных аргумента:
#     message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент
#     со значением по умолчанию sender = "university.help@gmail.com".
#     2 Если строки recipient и sender не содержит "@" или не оканчивается на
#     ".com"/".ru"/".net", то вывести на экран(в консоль) строку:
#     "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
#     3 Если же sender и recipient совпадают, то вывести "Нельзя отправить
#     письмо самому себе!"
#     4 Если же отправитель по умолчанию - university.help@gmail.com,
#     то вывести сообщение: "Письмо успешно отправлено с адреса <sender>
#     на адрес <recipient>."
#     5 В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!
#     Письмо отправлено с адреса <sender> на адрес <recipient>."
#     6 Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
#     7 За один вызов функции выводится только одно и перечисленных уведомлений!
#     Проверки перечислены по мере выполнения.

def send_email(message, recipient, sender = "shaaba@yandex.ru"):
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "shaaba@yandex.ru":
        print(f"Письмо успешно отправлено с {sender} на адрес {recipient}.")
        return
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, "на адрес ", recipient, ".")
        return

send_email(message = 'Доброго времени суток ', recipient = "Rokki@balboa.ru")