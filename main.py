import pyttsx3 as pt
import speech_recognition as sr
bot = pt.init()
#to set voice speed
# rate=bot.getProperty("rate")
# print(rate)
bot.setProperty("rate",180)

voices=bot.getProperty('voices')
#set the voice for bot
# for i in voices:
#     print(i)
bot.setProperty('voice',voices[1].id)


def speak(text):
    bot.say(text)
    bot.runAndWait()

aud=sr.Recognizer()
print("hello sir i'm your bot , what can i do for you")
with sr.Microphone() as mc:
    aud.energy_threshold=10000
    aud.adjust_for_ambient_noise(mc,1.2)
    print('listening')
    audio=aud.listen(mc)
    text=aud.recognize_google(audio)
    # print(text)

if 'what' and 'about' and 'you' in text:
    speak("i'm good")
speak('anything else')




# bot.say("Monesh kumar MK")
# bot.runAndWait()
