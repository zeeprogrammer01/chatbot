import random
import sqlite3


def respond(message):
    if message in messages:
        bot_message = random.choice(messages[message])
    else:
        bot_message = random.choice(messages["default"])
    return bot_message


conn = sqlite3.connect('chatbot.db')

c = conn.cursor()

# c.execute("""CREATE TABLE chatMessages(
# input text,
# response text

# )""")

messages = [('Hello', 'Hi I am Chatbot!'),
            ('How are you?', 'I am good'),
            ('How is the weather today?', 'It is really cold today'),
            ('What can you do?', 'I can answer your queries and give you reccomendations'),
            ('Bye', 'Thanks for your time')]

c.executemany('INSERT INTO chatMessages VALUES(?,?);', messages)

c.execute("SELECT * FROM chatMessages ")

print(c.fetchall())
conn.commit()

conn.close()
