#importing modules
from tkinter import *
import pygame
from tkinter import filedialog

#every program must have this root
root  = Tk() 
root.title("Speaker Recognition")
root.geometry("700x450")
root.configure(bg="#1e1e1e")

pygame.mixer.init()



def addtheAudio():
    audio = filedialog.askopenfilename(initialdir='C:/Users/ASUS/Desktop/Projects/SpeakerRecog/16000_pcm_speeches/')
    audio = audio.replace("C:/Users/ASUS/Desktop/Projects/SpeakerRecog/16000_pcm_speeches/", "")
    audioList.insert(END, audio)
    return print(audio)


def cnn():
    prediction = Label(root, text="This is Shariat's Voice", bg="#1e1e1e", fg="#fff")
    prediction.place(x=280, y=320)

def onPlay():
    voice = audioList.get(ACTIVE)
    pygame.mixer.music.load(voice)
    pygame.mixer.music.play(loops=0)




#Playlist Box
audioList = Listbox(root, bg="#1f1f1f", width=60)
audioList.place(x=165, y = 50)

#Creating Menu

audioMenu = Menu(root)
root.config(menu=audioMenu)

#Add an Audio
addAudio = Menu(audioMenu)
audioMenu.add_command(label="Add one Audio", command=addtheAudio)

#creating buttons

#play button
playbtn = Button(root, text="Check", bg="#1e1e1e", fg="#fff", borderwidth=1, padx=18, pady=10, command=onPlay)
playbtn.place(x=250, y=250)


submitbtn = Button(root, text='Predict',  bg="#1e1e1e", fg="#fff", borderwidth=1, padx=15, pady=10, command=cnn)
submitbtn.place(x=350, y = 250)


#showing in using the mainloop method
root.mainloop()