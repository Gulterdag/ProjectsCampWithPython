import pyttsx3
import webbrowser
import PyPDF2

engine = pyttsx3.init()

engine.say('  Hello ' 
           '  my friend'
           '  My Name is Turko .  '
           '  I am a personal assistant. '
           '  As my name suggests, I am a Turk.'
           '  I am from Turkey'
           '  I am here for you.  '
           '  What can I do for you. Lets start.  ')

engine.runAndWait()

response = input("")
if response == 'what is your name':
    engine.say('My name is Turko . I am a personal assistant. I have been in this business for 3 year.  My friend, I am here 7/24')

elif response == 'how are you':
    engine.say('I am very well. And you')

elif response == 'where are you from':
    engine.say('I am from Turkey.  I love Turkey very much.  I currently live in Bosnia and Herzegovina. İt is nice to live here.  Because here it is like our homeland.Living here is not difficult. You know, we have many Turkish brothers here. ')

elif response == 'how old are you':
    engine.say('I am 3 years old . If you call me small, we will fight with you.')

elif response == 'What is your horoscope':
    engine.say('My zodiac sign is Libra.I like this question , because I love zodiac signs')

elif response == 'tell me a joke':
    engine.say('Andy: Are not  you wearing your wedding ring on the wrong finger ?  '
                '   Yes I am , because I married the wrong woman')

elif response == ('who are you'):
    engine.say('Hello earthling. I am Turko , I am a gifted personal assistant. I work 24/7. I do not  give up.I do not like to brag about myself, but right now I am  the best. Nice to meet you.')

elif response == ('search the internet'):
    engine.say('what do you want me to search on the internet')
    engine.runAndWait()
    search = input(' ')
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    engine.say(search + 'için bulduklarım')

elif response ==('tell me a story'):
    reader =reader = open('C:/Users/pc/Desktop/King Arthur - 2.pdf', 'rb')
    pdfOkuyucu = PyPDF2.PdfReader(reader)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    print('I chose King Arthur for you. Then I will tell you about King Arthur.')
    for sayfa_numarasi in range(0, pdfOkuyucu.numPages):
        sayfa = pdfOkuyucu.getPage(sayfa_numarasi)
        yazi = sayfa.extractText()
        engine.say(yazi)
        engine.runAndWait()

elif response == ('sing a song'):
    engine.say('My voice is very bad. I do not want to scare you friend.')
    engine.runAndWait()
    engine.say('I can open any song you want from youtube for you. What would you like to listen to?')
    engine.runAndWait()
    search = input(' ')
    url = 'https://www.youtube.com/results?search_query='+search
    webbrowser.get().open(url)
    engine.say(search + 'için bulduklarım')

elif response == ('Do you think I am beautiful'):
    engine.say('Of course , my friend . You are the most beautiful thing I have ever seen . I feel so lucky to have you.')

elif response == ('goodbye'):
    engine.say('Goodbye my friend.   It was so nice chatting with you.   Take care of yourself. Turko loves you,  do not forget that.   always be happy.')

else:
    engine.say(response)
engine.runAndWait()