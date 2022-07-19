def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    
    greeting = func("Robel")
    print(greeting)


greet(shout)
greet(whisper)