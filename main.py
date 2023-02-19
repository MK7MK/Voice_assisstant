import datetime
import pyttsx3 as pt
import speech_recognition as sr
import mypackage
import api, jokes, weather, news, browsing_sites
import requests
import randfacts


bot = pt.init()
bot.setProperty("rate", 180)
voices = bot.getProperty('voices')
bot.setProperty('voice', voices[1].id)


def speak(text):
    bot.say(text)
    bot.runAndWait()


aud = sr.Recognizer()
today=datetime.datetime.now()
speak("today is "+today.strftime("%d")+"of "+today.strftime("%b")+ "and its currently"+today.strftime("%I"))
speak("hello sir i'm your bot, what can i do for you")
with sr.Microphone() as mc:
    aud.energy_threshold = 10000
    aud.adjust_for_ambient_noise(mc, 1.2)
    speak("listening")
    print('listening')
    audio = aud.listen(mc)
    text = aud.recognize_google(audio)


if 'what' and 'about' and 'you' in text:
    speak("i'm good")
    speak('anything else')
if 'information' or 'details' or 'about this' in text:
    speak("you need info related to which topic")
    with sr.Microphone() as mc:
        aud.energy_threshold = 10000
        aud.adjust_for_ambient_noise(mc, 1.2)
        speak("listening")
        print('listening')
        audio = aud.listen(mc)
        infor = aud.recognize_google(audio)
        infor2 = browsing_sites.contt(infor)
        speak('do you want me to read a few point about your information?')
        aud.energy_threshold = 10000
        aud.adjust_for_ambient_noise(mc, 1.2)
        speak("listening")
        print('listening')
        audio = aud.listen(mc)
        infor = aud.recognize_google(audio)
        print(infor)
        inp=infor
        if 'yes' in inp:
            speak(infor2)
        speak('do you need this information to open in web browser')
        aud.energy_threshold = 10000
        aud.adjust_for_ambient_noise(mc, 1.2)
        speak("listening")
        print('listening')
        audio = aud.listen(mc)
        infor = aud.recognize_google(audio)
        print(infor)
        inp2 = infor
        if 'yes' in inp2:
            speak(f"searching about {infor} ")
            browsing_sites.function_wiki(infor)

#
# speak("do you want to continue asking")
# print("do you want to continue asking")
# with sr.Microphone() as mc:
#     aud.energy_threshold = 10000
#     aud.adjust_for_ambient_noise(mc, 1.2)
#     speak("listening")
#     print('listening')
#     audio = aud.listen(mc)
#     want_cont = aud.recognize_google(audio)
# if 'yes' in want_cont:
#     pass
# else:
#     break
if 'music' or 'video' in text:
    speak("what music or video you want")
    with sr.Microphone() as mc:
        aud.energy_threshold = 10000
        aud.adjust_for_ambient_noise(mc, 1.2)
        speak("listening")
        print('listening')
        audio = aud.listen(mc)
        mus = aud.recognize_google(audio)
        browsing_sites.function_yout(mus)

if 'google' or 'search in google' in text:
    speak("what are you looking for ")
    with sr.Microphone() as mc:
        aud.energy_threshold = 10000
        aud.adjust_for_ambient_noise(mc, 1.2)
        speak("listening")
        print('listening')
        audio = aud.listen(mc)
        gg = aud.recognize_google(audio)
        browsing_sites.function_google(gg)


if 'news' or 'headlines' in text:
    arr = news.news()
    for i in arr:
        speak(i)
        print(i)

if 'facts' or 'fact' in text:
    speak("sure sir!")
    x = randfacts.get_fact()
    print(x)
    speak("did you know", +x)

if 'jokes' or "tell funny" in text:
    arr = jokes.joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

speak("hi , current temperature in your location is "+str(weather.temp())+"degree celsius"+" and with"+str(weather.des()))
# bot.say("Monesh kumar MK")
# bot.runAndWait()
