def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

text_messages = ["Hello!", "How are you?", "Let's meet up later.", "Have a great day!"]
sent_messages = []

send_messages(text_messages[:], sent_messages)

print("\nOriginal messages list:", text_messages)
print("Sent messages list:", sent_messages)