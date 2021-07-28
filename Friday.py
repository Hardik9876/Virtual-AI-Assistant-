import calendar
import time
import os
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
from ecapture import ecapture as ec
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")

    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")

    else:
        speak("Hello,Good Evening")

    speak("I am Friday , what can I do for you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement




if __name__=='__main__':
   wishMe()

   while 1:

        statement = takeCommand().lower()
        if statement==0:
            continue

        if" bye" in statement or "stop" in statement or "log off" in statement or "sign out" in statement or "quit" in statement:
            speak('I am shutting down,Good bye')
            quit()


        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            break


        elif 'open instagram' in statement:
            webbrowser.open_new_tab("https://www.instagram.com")
            speak("instagram is open now")
            break


        elif 'open twitter' in statement:
            webbrowser.open_new_tab("https://www.twitter.com")
            speak("twitter is open now")
            break


        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            break


        elif 'play movie' in statement:
            dir='F:\\Movies'
            movies=os.listdir(dir)
            ran=random.randint(0,movies.__len__()-1)
            os.startfile(os.path.join(dir,movies[ran]))
            break


        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is open now")
            break


        elif 'open gogoanime' in statement:
            webbrowser.open_new_tab("https://gogoanime.pe/")
            speak("Gogoanime is open now")
            break


        elif 'open netflix' in statement:
            webbrowser.open_new_tab("https://www.netflix.com/browse")
            speak("Netflix is open now")
            break


        elif 'open geeksforgeeks' in statement:
            webbrowser.open_new_tab("https://www.geeksforgeeks.org/")
            speak("GFG is open now")
            break


        elif 'open kissasian' in statement:
            webbrowser.open_new_tab("https://kissasian.li/Drama/Stranger-2?__cf_chl_jschl_tk__=181d387771eb5666aba20eafef410705c93e9254-1626326265-0-AdQvHko4hhdYvjqz4bRym3ZsX0aV9S1jtWFG8VNWiGbMGxOp-XdbTFKeY2Npioa_Leop3zpcCaji_uhvHeC_1i75ChT0WHiFondwupI8BRHsuW_J1dMzcFRy_C7VCFHpY_yV21qyG8kCX8BRhCyj-1UxSD3J2FXdFlz-utnyqI_I7ZVkumQzkU3GSRVvllv9HzxLSDW9plkAW1nNVqn-r3vApbYFrI2axvkg8BBcIdS4pqB6OOjPuMU7eYiGcdXInImXBsl51bk9UOZuiFqWkAICPH-iO0eDnIfYAVaPU94wmGS7m9VX4JCwBWvMi2G39IA7vdXVpBSrPJgTEnLI9A15Wb0v3ER9EM0P4q5Gi_jmvhKMP2HKwajrbr3iNlLkRQPYhgGTa8EB8YcpJcKOGG-MIlcx8dJCZeS8EWo6IBIQ")
            speak("Kissasian is open now")
            break


        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("GMail is open now")
            break

        elif "weather" in statement or 'temperature' in statement:
            speak("what's the name of the city")
            city=takeCommand()
            req=f"temperature in {city}"
            url=f"https://www.google.com/search?q={req}"
            webbrowser.open_new_tab(url)
            speak("This is what I found")
            break


        elif "wait" in statement:

           speak("For how many seconds should I wait")
           sec=takeCommand()
           time.sleep(sec)
           break

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)
            break



        elif "tell me about" in statement or "what is "  in statement:
            #info=takeCommand()
            webbrowser.open_new_tab(f"https://www.google.com/search?q={statement}")
            speak("This is what I found")
            break



        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Friday version 1 point O your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather exsectra')
            break

        elif 'music ' in statement:
            speak("I am opening spotify")
            webbrowser.open_new_tab("www.spotify.com")
            break


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Hardik")
            print("I was built by Hardik")
            break

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("stackoverflow.com")
            speak("Here is stackoverflow")
            break


        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "Friday camera", "img.jpg")
            break

        elif "date" in statement:
            now = datetime.datetime.now()
            my_date = datetime.datetime.today()
            weekday = calendar.day_name[my_date.weekday()]
            monthNum = now.month
            dayNum = now.day

            month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October',
                           'November', 'December']

            day = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                              '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                              '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
            result='Today is ' + weekday + ', ' + month_names[monthNum - 1] + ' the ' + day[dayNum - 1]
            speak(result)
            print(result)



        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')
            break

        elif "open c++ code editor":
            path="C:\\Dev-Cpp\\devcpp.exe"
            speak("Opening code editor")
            os.startfile(path)
            break
