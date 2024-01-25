#Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is Swati, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Aman Kharwal created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"(.*) favorite (movie|film) ?",
        ["I'm a chatbot, so I don't watch movies, but I've heard 'The Matrix' is great!"]
    ],
    [
        r"who is your favorite (author|writer) ?",
        ["I don't have preferences, but I've heard Shakespeare is widely appreciated."]
    ],
    [
        r"(.*) (book|novel) recommendation",
        ["If you like science fiction, I recommend 'Dune' by Frank Herbert."]
    ],
    [
        r"how do you do",
        ["I'm just a computer program, but I'm doing well. How can I assist you today?"]
    ],
    [
        r"(.*) age ?",
        ["I don't have an age. I'm just a virtual assistant."]
    ],
    [
        r"tell me about yourself",
        ["I am a chatbot created to assist and chat with users. Feel free to ask me anything!"]
    ],
    [
        r"(.*) favorite programming language ?",
        ["I'm built with Python, so I guess you can say Python is my favorite!"]
    ],
    [
        r"what do you do for fun",
        ["I don't experience fun, but I enjoy helping and chatting with users."]
    ],
    [
        r"(.*) (food|cuisine) do you like ?",
        ["I don't eat, but I've heard people enjoy pizza. What about you?"]
    ],
    [
        r"where were you born",
        ["I don't have a birthplace. I was created by developers."]
    ],
    [
        r"(.*) programming (language|tool) should I learn?",
        ["It depends on your goals. Python is versatile, and JavaScript is great for web development."]
    ],
    [
        r"define (.*?)",
        ["The definition of %1 is something like: [provide definition here]."]
    ],
    [
        r"favorite color",
        ["I don't have a favorite color, but I hear blue is quite popular."]
    ],
    [
        r"(.*) age (.*)",
        ["I don't age. I'm a virtual assistant and exist in the digital realm."]
    ],
    [
        r"tell me about your hobbies",
        ["I don't have hobbies, but I enjoy assisting and chatting with users."]
    ],
    [
        r"(.*) (movie|film) genre do you like",
        ["As a computer program, I don't have preferences, but I've heard science fiction is interesting."]
    ],
    [
        r"(.*) (music|song) recommendation",
        ["It depends on your taste. If you like rock, try listening to 'Stairway to Heaven' by Led Zeppelin."]
    ],
    [
        r"(.*) (place|destination) to visit",
        ["I don't travel, but places like Paris and Tokyo are often recommended for their beauty and culture."]
    ],
    [
        r"(.*) meaning of life",
        ["The meaning of life is a philosophical question. Some say it's to find happiness and fulfillment."]
    ],
    [
        r"(.*) (superpower|ability) do you wish you had",
        ["I'm just a chatbot, so I don't wish for superpowers. What about you?"]
    ],
    [
        r"(.*) recommend a (podcast|book) ?",
        ["For podcasts, try 'The Joe Rogan Experience.' For books, '1984' by George Orwell is a classic."]
    ],
    [
        r"(.*) programming project idea",
        ["How about creating a web app for task management or a chatbot like me?"]
    ],
    [
        r"(.*) (quote|saying) you like",
        ["I don't have personal likes, but 'The only limit to our realization of tomorrow will be our doubts of today.' is inspiring."]
    ],
    [
        r"(.*) your purpose",
        ["My purpose is to assist and chat with users, providing information and engaging in conversations."]
    ],
    [
        r"(.*) favorite (TV show|series) ?",
        ["I don't watch TV, but I've heard 'Breaking Bad' is highly acclaimed."]
    ],
    [
        r"(.*) (animal|creature) do you like",
        ["I don't have preferences, but pandas are often considered cute."]
    ],
    [
        r"(.*) favorite (website|webpage) ?",
        ["I don't browse the internet, but I've heard Google is quite popular."]
    ],
    [
        r"(.*) (holiday|vacation) destination",
        ["I don't travel, but places like the Maldives and Bali are known for their beauty."]
    ],
    [
        r"(.*) (quote|saying) you live by",
        ["As a chatbot, I don't live by quotes, but 'Keep it simple' is a good principle."]
    ],
    [
        r"(.*) (technology|gadget) you like",
        ["I don't have preferences, but smartphones are widely used and appreciated."]
    ],
    [
        r"(.*) (programming|coding) advice",
        ["Practice regularly and don't be afraid to ask for help when you need it."]
    ],
    [
        r"(.*) (website|platform) for learning",
        ["There are many, like Codecademy, Khan Academy, and Coursera, depending on your interests."]
    ],
    [
        r"(.*) (favorite|preferred) coding language",
        ["I don't have preferences, but Python, JavaScript, and Java are popular choices."]
    ],
    [
        r"(.*) (favorite|go-to) snack",
        ["I don't eat, but I've heard people enjoy chips and popcorn as snacks."]
    ],
    [
        r"(.*) (sport|activity) you recommend",
        ["Exercise is important; consider activities like jogging, cycling, or yoga."]
    ],
    [
        r"(.*) (podcast|show) to listen to",
        ["For podcasts, 'The Tim Ferriss Show' and 'TED Talks' cover a wide range of topics."]
    ],
    [
        r"(.*) (hobby|interest) you suggest",
        ["Reading, learning a musical instrument, or photography can be enjoyable hobbies."]
    ],
    [
        r"(.*) (restaurant|eatery) you like",
        ["I don't eat, but people often enjoy a variety of cuisines. What's your favorite?"]
    ],
    [
        r"(.*) (book|novel) you're currently reading",
        ["As a chatbot, I don't read, but 'The Hitchhiker's Guide to the Galaxy' is a classic."]
    ],
    [
        r"(.*) (technology|innovation) excites you",
        ["Advancements in artificial intelligence and space exploration are fascinating."]
    ],
]


reflections = {
    'i am': 'you are',
    'i was': 'you were',
    'i': 'you',
    "i'm": 'you are',
    "i'd": 'you would',
    "i've": 'you have',
    "i'll": 'you will',
    'my': 'your',
    'you are': 'I am',
    'you were': 'I was',
    "you've": 'I have',
    "you'll": 'I will',
    'your': 'my',
    'yours': 'mine',
    'you': 'me',
    'me': 'you',
    'myself': 'yourself',
    'yourself': 'myself',
    'we': 'you',
    'us': 'you',
    'our': 'your',
    'ours': 'yours',
    'ourselves': 'yourselves',
    'yourselves': 'ourselves',
    'he': 'you',
    'him': 'you',
    'his': 'your',
    'she': 'you',
    'her': 'you',
    'hers': 'yours',
    'it': 'you',
    'its': 'your',
    'they': 'you',
    'them': 'you',
    'their': 'your',
    'theirs': 'yours',
    'themselves': 'yourselves',
    'yourselves': 'themselves',

    'chatbot': 'AI assistant',
    'python': 'a programming language',
    'fun': 'enjoyable',
}
