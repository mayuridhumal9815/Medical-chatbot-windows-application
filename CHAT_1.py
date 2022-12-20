import nltk
from textblob import TextBlob 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from PIL import Image , ImageTk
from keras.models import load_model
model = load_model('TRIAL_MODEL.h5')
import json
import random
import sqlite3
import tkinter as tk
import pyttsx3 
import PIL.Image
import speech_recognition as sr

converter = pyttsx3.init() 

converter.setProperty('rate', 150) 

converter.setProperty('volume', 1.0) 

intents = json.loads(open('intents2.json').read())

words = pickle.load(open('WORDS.pkl','rb'))
classes = pickle.load(open('CLASSES.pkl','rb'))


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    if 'CHICKEN POX' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='CHICKEN POX'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'FEVER' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='FEVER'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'COUGH' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='COUGH'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'COLD' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='COLD'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Contact Dermatitis' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Contact Dermatitis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Eye Allergies' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Eye Allergies'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Sinus Infection' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Sinus Infection'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Allergic Rhinitis' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Allergic Rhinitis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Food Allergy' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Food Allergy'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    if 'Anaphylaxis' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Anaphylaxis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'Acne' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Acne'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
     
    if 'Eczema' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Eczema'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'hives' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='hives'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'dark circles' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='dark circles'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'Blackheads' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='Blackheads'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'psoriasis' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='psoriasis'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'dry, cracked skin' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='dry, cracked skin'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    
    if 'ulcers' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='ulcers'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'rosacea' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='rosacea'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'open sores or lesions' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='open sores or lesions'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d
    
    if 'ringworm' in res:
        db = sqlite3.connect(r'C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/Doctors.db')
        c = db.cursor()
        find = ("SELECT Name,Contact,Address FROM List WHERE Disease='ringworm'")
        c.execute(find)
        d = c.fetchall()
        print(res , d)
        return res , d   
    else:
        print(res)
        return res 

#Creating GUI with tkinter
import tkinter
from tkinter import *


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.configure(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: \n" + str(res) + '\n')
        
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
from translate import Translator 

def SPEECH():
    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say Something...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            import time
            language = 'en'
            time.sleep(5)
            print('You Said : {}'.format(text))
            return str(text)
    #listen()
    msg = listen()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.configure(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + str(res) + '\n\n')
        converter.say(str(res)) 
        converter.runAndWait() 

            
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)



def SPEECHM():
    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say Something...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            translator= Translator(from_lang="English",to_lang="Marathi")
            translation = translator.translate(text)
            print(translation)
            
            import time
           # language = 'en'
            time.sleep(1)
            print('You Said : {}'.format(translation))
            return str(translation)
    #listen()
    msg = listen()
    en_blob = TextBlob(str(msg))
    translated = (en_blob.translate(to='en'))
    print(translated)
    print(type(translated))
    abc=str(translated)
    print(abc)
    print(type(abc))
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.configure(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        res = chatbot_response(abc)
        ChatLog.insert(END, "Bot:\n " + "\n"+ str(res)+ '\n\n')
        converter.say(str(res)) 
        converter.runAndWait() 

            
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
    
# def SPEECHH():
#     def listen():
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Say Something...")
#             audio = r.listen(source)
#             text = r.recognize_google(audio)
#             translator= Translator(from_lang="English",to_lang="Hindi")
#             translation = translator.translate(text)
#             print(translation)
            
#             import time
#            # language = 'en'
#             time.sleep(1)
#             print('You Said : {}'.format(translation))
#             return str(translation)
#     #listen()
#     msg = listen()
#     en_blob = TextBlob(str(msg))
#     translated = (en_blob.translate(to='en'))
#     print(translated)
#     print(type(translated))
#     abc=str(translated)
#     print(abc)
#     print(type(abc))
#     EntryBox.delete("0.0",END)

#     if msg != '':
#         ChatLog.configure(state=NORMAL)
#         ChatLog.insert(END, "You: " + msg + '\n\n')
#         ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
#         res = chatbot_response(abc)
#         ChatLog.insert(END, "Bot:\n " + "\n"+ str(res)+ '\n\n')
#         converter.say(str(res)) 
#         converter.runAndWait() 

            
            
#         ChatLog.config(state=DISABLED)
#         ChatLog.yview(END)
    


base = tk.Toplevel()
base.title("Chat bot")
#base.geometry("600x600")
base.resizable(width=tk.TRUE, height=tk.TRUE)
w, h = base.winfo_screenwidth(), base.winfo_screenheight()
base.geometry("%dx%d+0+0" % (w, h))
load_bg = PIL.Image.open(r"C:/Users/admin/Desktop/21CG120-Medical chatbot-windows application/Sem II/100 Project-Spyder/21CG120_Medical_Chatbot_voice/im9.jpg")
load_bg = load_bg.resize((w,h))
render_bg = ImageTk.PhotoImage(load_bg)
bg = tk.Label(base, image = render_bg , height=h, width= w)
bg.image = render_bg
bg.place(x=0,y=10)
#Create Chat window
ChatLog = tk.Text(base, bd=2, bg="white",fg="black", height="15", width="200", font="Arial",)

#ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = tk.Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = tk.Button(base, font=("Verdana",12,'bold'), text="Send", width="15", 
                    bd=0, bg="pink3", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = tk.Text(base, bd=1, bg="pink",width="40", height="1", font=("Arial",15))
#EntryBox.bind("<Return>", send)

c=StringVar()
#Place all components on the screen
head = tk.Label(base,width=75,text="Medical Assistance Chat Bot System",font=("times",30,"italic"),bg="pink",fg="black")
head.place(x=0,y=0)
scrollbar.place(x=500,y=20, height=520)
ChatLog.place(x=10,y=52, height=400, width=500)
EntryBox.place(x=150, y=450, height=100, width=370)
SendButton.place(x=10, y=450, height=100)

head = tk.Label(base,width=20,text="Voice Communication",font=("times",25,"italic"),bg="pink",fg="black")
head.place(x=950,y=350)
# label_1 = Label(base, text="Select Language",height=2,width=20,font=("bold", 10),bg='lightblue4',fg='white')
# label_1.place(x=950,y=420)

# list1 = ['English','Marathi','Hindi'];

# droplist=OptionMenu(base,c, *list1)
# droplist.config(height=2,width=20)
# c.set('Select language') 
# droplist.place(x=1150,y=420)
#Button(frame_alpr1, text='After Selecting Language... Press Button and Talk....',height=5,width=50,font=('times', 14, ' bold '),bg='brown',fg='white',command=translate_text).place(x=30,y=180)

button2 = tk.Button(base,text="English",command=SPEECH,font=('Times New Roman',15,'bold'),width=20,bg='#FF8040',fg='black')
button2.place(x=1000,y=450)
button3 = tk.Button(base,text="Marathi",command=SPEECHM,font=('Times New Roman',15,'bold'),width=20,bg='#FF8040',fg='black')
button3.place(x=1000,y=520)
#button4 = tk.Button(base,text="Hindi",command=SPEECHH,font=('Times New Roman',15,'bold'),width=20,bg='#FF8040',fg='black')
#button4.place(x=1000,y=590)


base.mainloop()


from random import sample
s = ["Whole body fainting", "light-headedness", "low blood pressure", "dizziness", "flushing", "difficulty breathing", "rapid breathing", "shortness of breath", "wheezing"]
len(s)
sample(s,7)