import streamlit as st
from helper import pairs, reflections
from nltk.chat.util import Chat

def respond_to_user_input(user_input, chat):
    return chat.respond(user_input)
chat_history = []

bar = st.sidebar
with open('history.txt','r') as file:
    for file in file:
        bar.write((file))
def main():
    st.title("NLTK Chatbot UI")

    # Create Chat Bot
    chat = Chat(pairs, reflections)

    # List to store chat history

    # Input box for user to enter messages
    user_input = st.text_area("User Input:", height=50, max_chars=None, key=None)

    if st.button("Submit"):
        # Process user input and get response
        bot_response = respond_to_user_input(user_input, chat)

        # Update chat history
        chat_history.append(f"User:\n\t{user_input}\nBot:\n\t{bot_response}")
        with open('history.txt', 'a') as file:
            file.write(f"User: {user_input}\nBot: {bot_response}\n")
        with open('history.txt','r') as file:
            for file in file:
                bar.write((file))
        # Display chat history
        st.text_area("Bot :", value="\n\n".join(chat_history), height=300, max_chars=None, key=None)
        
if __name__ == '__main__':
    main()


