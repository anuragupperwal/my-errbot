from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

def chatter():
    chatbot = ChatBot("Friday")

    conversation = [
        "Hello",
        "Hi there!",
        "I am great",
        "I am doing great. What about you?",
        "I am fine, What about you?",
        "I am good, what about you?"
        "How are you doing?",
        "I'm doing great.",
        'How are you?',
        'I am good.',
        "That is good to hear",
        "Thank you.",
        "You're welcome."
        "Good bye.",
        "Great.",
        "I am bot"
        "My name is bot"
        "Same old same old.",
        "So nice of you"
    ]


    #trainer.train(conversation)

    trainer = ListTrainer(chatbot)
    bot = ChatBot(
        'Friday',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database_uri='sqlite:///database.sqlite3'
    )
    while True:
        usr_inp=input('>>')

        response = chatbot.get_response(usr_inp)
        
        if usr_inp=='exit':
            break
        yield response


