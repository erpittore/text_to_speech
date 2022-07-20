import pyttsx3

engine = pyttsx3.init()
words = 'Hello mamacita I am your personal assistant'
words2 = 'With time I will become stronger than Ultron!'
voices = engine.getProperty('voices')
engine.setProperty('rate', 140)
engine.setProperty('voice', voices[2].id)#change the number to get  diiferent voice otherwise delete this line for the default voice
engine.say(words)
engine.say(words2)
engine.runAndWait()

