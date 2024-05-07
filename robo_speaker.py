# This program is designed to work on Windows OS

import pyttsx3

if __name__ == '__main__':
    print('==== Welcome to Robo Speaker ====')
    engine = pyttsx3.init()
    while True:
        try:
            x = input('Write what you want me to speak: ')
            if x == 'q':
                engine.say('Bye, it was nice talking to you')
                engine.runAndWait()
                break
            engine.say(x)
            engine.runAndWait()
        except:
            engine.say('Goodbye')
            engine.runAndWait()
            break
