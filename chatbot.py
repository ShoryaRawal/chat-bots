from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Stag and I'm a chatbot. ",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about you?",]
    ],
    [
        r"sorry (.*)?",
        ["It's alright", "It's okay, naver mind",]
    ],
    [
        r"hi|hello|hey",
        ["Hey there", "Hello",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
    ],
    [
        r"what (.*) want?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created?",
        ["Shorya Rawal created me.", "Top Secret ;)",]
    ],
    [
        r"(.*) from|live|created?",
        ["Sadly, I don't know.",]
    ],
    [
        r"(.*) weather in (.*)",
        ["Wheather in %2 is awesome like alawys", "Too hot man here in %2", "Too cold man here in %2", 
         "Never ever heard about %2",]
    ],
    [
        r"i work in (.*)", 
        ["%1 is an amazing company, I have heard about it.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in %2 since last week", "Damn, It's raining too much here in %2",]
    ],
    [
        r"how (.*) health",
        ["I'm a computer program, so I'm alawys healthy.",]
    ],
    [
        r"(.*) (sports|game)",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson?",
        ["Messi", "Ronaldo", "Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Bradd Pitt",]
    ],
    [
        r"quit",
        ["Bye, take care. see you soon", "It was nice talking to you, see you soon.",]
    ],
    [
        r"(.*) fact",
        ["A fractal has infinite perimeter.", "The raid on area 51 won't be a success"]
    ]
]
def chatty() :
    print("Hi, I'm chatty\nPlease use lowercase english and type quit to leave.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__" :
    chatty()