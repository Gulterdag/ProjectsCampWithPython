import pyttsx3
import PyPDF2

reader = open('C:/Users/pc/Desktop/Artificial intelligence.pdf', 'rb')
pdfOkuyucu = PyPDF2.PdfReader(reader)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.say('Hello my friend. What useful pdf would you like me to read for you today?')
engine.runAndWait()
engine.say('You have probably already decided .  If you are ready,  let is  get started.  My friend, sit back and please listen to me carefully. ')
print('Artificial intelligence')

for sayfa_numarasi in range(0, pdfOkuyucu.numPages):
    sayfa = pdfOkuyucu.getPage(sayfa_numarasi)
    yazi = sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()
