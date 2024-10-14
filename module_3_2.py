variants = ('.com', '.ru', '.net')
message = str(input("Напишите сообщение: "))
recipient = str(input("Введите адрес получателя: "))

def change_sender():
    sender_q = str(input("Хотите поменять адрес отправителя? (y/n): "))
    if sender_q == "y":
        sender_new = str(input("Введите адрес отправителя: "))
        sender = sender_new
        send_email(message, recipient, sender = sender_new)
    else:
        send_email(message, recipient)

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if "@" in recipient and "@" in sender and recipient.endswith(variants) and sender.endswith(variants):
        if sender == "university.help@gmail.com" and recipient != sender:
            print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        elif sender != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с "
              "адреса", sender, "на адрес", recipient)
        elif recipient == sender:
            print("Нельзя отправить письмо самому себе!")
    else:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)

change_sender()
