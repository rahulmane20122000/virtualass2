import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
from selenium import webdriver
import selenium
import cv2
import time
from tkinter import *
# from webdriver_manager.chrome import ChromeDriverManager

engine = pyttsx3.init()
sound = engine.getProperty('voices')
# print(sound[1].id)
engine.setProperty('voice', sound[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak('good morning!')
    elif hour > 12 or hour < 16:
        speak('good afternoon!!')
    else:
        speak('good evening!!')
    speak('hello sir i am mango how may i help you')


def takecommand():
    # it takes input from mic
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.8
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print('reconising..')
        query = r.recognize_google(audio, language='en-in')
        # print(f"user said:{query}\n")
        print("user said:"+query)

    except Exception as e:
        print(e)
        print("say that again pls...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rahulmane20122000@gmail.com', 'rahulmane123')
    server.sendmail('rahulmane2012000@gmail.com', to, content)
    server.close()


def automate(query):
    url = ["https://www.google.com", "https://www.youtube.com"]
    chromedriver = '..\chromedriver_win32\chromedriver.exe'
    if 'search on google' in query:
        speak('what should i search sir')
        command = takecommand()
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(chromedriver)
        driver.get(url[0])
        searchbox = driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        searchbox.send_keys(command)
        searchbutton = driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        searchbutton.click()
    elif 'auto youtube' in query:
        speak('which video should i search for you')
        command = takecommand()
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(chromedriver)
        driver.get(url[1])
        searchbox = driver.find_element_by_name( 'search_query')
        searchbox.send_keys(command)
        searchbutton=driver.find_element_by_id('search-icon-legacy')
        searchbutton.click()
        

if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()

        if 'who is' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)

        elif 'open youtube' in query:
            speak('sure sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('sure sir')
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak('sure sir')
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            speak('sure sir')
            webbrowser.open("instagram.com")

        elif 'open stackoverflow' in query:
            speak('sure sir')
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{time}")

        elif 'send email to dharmendra mane' in query:
            try:
                speak('what should i say')
                content = takecommand()
                to = "dharmendrakumarhmane@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                speak('sorry my friend rahul i am not able to send the email')

        elif 'what is name of your creator' in query:
            speak(
                'i am created by rahul an indian electronincs and telecommunication engineer')

        elif 'i am hungry' in query:
            speak('i have best thing for you on this hungry moment')
            webbrowser.open("swiggy.com")

        #   elif 'search on google' in query:
        #       speak('what should i search')
        #       command=takecommand()
        #       chromedriver='G:\mango virtual assistance\chromedriver_win32\chromedriver'
        #       driver=webdriver.Chrome(chromedriver)
        #       driver.get('https://www.google.com')
        #       searchbox=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        #       searchbox.send_keys(command)
        #       searchbutton=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        #       searchbutton.click() 
        elif 'search on google' in query:
            automate(query)

        elif 'search on youtube' in query:
            automate(query)

        # elif 'roll dice' in query:
        #     speak('sure master')
        #     root=Tk()
        #     root.geometry("700x300")
        #     l1=Label(root,text='',font=("times",200))
        #     speak('speak roll aloud whenever you want to roll the dice')
        #     b1=takecommand()
        #     run=True
        #     while run:
        #         b1.lower()
        #         if 'roll' in b1:
        #             roll()
        #             time.sleep(10)
        #             speak('do you want to roll again')
        #             c=takecommand()
        #             if 'yes' in c:
        #                 roll()
        #             else:
        #                 run=False    
                
        #     speak('thanks for playing have a nice day')

        #     def roll():
        #         number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
        #         l1.config(text=f'{random.choice(number)}{random.choice(number)}')
        #         l1.pack()
        #     root.mainloop()     
        
        # elif 'capture image' in query:
        #    speak("ok!!! sir please give me some time to take image")
        #    cam=cv2.VideoCapture(0)
        #    while True:
        #        ret,frame=cam.read()
        #        cv2.imshow("REGISTER",frame)
        #        k=cv2.waitKey(30)
        #        if k==32:
        #            speak("please tell me your good name sir")
        #            time.sleep(2)
        #            img_name=takecommand()
        #            img="{}.png".format(img_name)
        #            cv2.imwrite(img,frame)
        #            speak('you have been sucessfully added please press escape')
        #        if k==27:
        #             break
        # cam.release()
        # cv2.destroyAllWindows()


           
        
                
       
                    


        
           