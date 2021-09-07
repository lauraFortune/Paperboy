
from tkinter import * # imports all from tkinter
import tkinter as tk # use tk shortcut
from tkinter import ttk # ttk themed elements
from PIL import ImageTk, Image # for image processing
from datetime import datetime # for clock
from pyglet import font # for importing fonts
from tkinter.font import Font # for defining font classes
import webbrowser # for opening url link
import requests # http requests to news api
#========= my files
import news_api
import backend
from models import *

#======================================================== ADD FONTS
font.add_file("fonts/pixel_operator/PixelOperator8.ttf")
font.add_file("fonts/pixel_operator/PixelOperator-Bold.ttf")
font.add_file("fonts/LLPIXEL3.ttf")

#======================================================== WRAPPER FUNCTIONS
def save_story(news_story, cat_index): # wraps back end function
    backend.save(news_api.categories[cat_index], news_story.image, news_story.url, news_story.publish_date, news_story.title, news_story.description)
    news_api.resetMyNewsCategory() # clears the 'mynews' articles array so it can refresh

def delete_story(storyID): # wraps back end function
    backend.delete(storyID)
    news_api.resetMyNewsCategory()  # clears the 'mynews' articles array so it can refresh
    news_maker(3,True)

def show_stories():
        news_maker(3,True)
        
            

#======================================================== DEFINE ROOT
root = tk.Tk()
#======================================================== FONT 

btn_font = Font(family="Pixel Operator", size=12)
title_font = Font(family="Pixel Operator Bold", size=12, weight="bold")
text_font = Font(family="Pixel Operator", size=10)
logo_font = Font(family="LLPixel", size=24)

root.option_add("*Font", text_font)

#======================================================== WINDOW SETUP
root.geometry("800x500")
root.title("news") 
root.iconbitmap("images/paperboy.ico") # favicon

#======================================================== BANNER
#banner frame
banner = tk.Frame(root, bg="#65FDCA")
banner.pack(fill="x")
#logo
logo = tk.Label(banner, bg="#65FDCA", text="Paperboy", font=logo_font)
logo.pack(pady=10, side="left", padx=(30,0))
#clock
def update_time():
    dateTime = datetime.now()
    str = dateTime.strftime("%m/%d/%Y %H:%M:%S")
    clock.config(text = str)
    clock.after(1000, update_time)
 
clock = Label(banner, font=title_font, bg="white")

clock.pack(side="right", padx=(0,30))
update_time()

#======================================================== MENU
#menu frame
menu = tk.Frame(root)
menu.pack(fill="x")
# menu buttons
mynews_image = PhotoImage(file="images/computer.png")
category_image = PhotoImage(file="images/folder.png")

btn1 = tk.Button(menu, text="Sports", cursor="hand2", font=btn_font, activebackground="#e3e1e1", image=category_image, compound=TOP, borderwidth=0, command=lambda: news_maker('0',False))
btn1.pack(side="right", padx=(0,40), pady=(10, 10))
btn2 = tk.Button(menu, text="Business", cursor="hand2", font=btn_font, activebackground="#e3e1e1", image=category_image, compound=TOP, borderwidth=0, command=lambda: news_maker('1',False))
btn2.pack(side="right")
btn3 = tk.Button(menu, text="Technology", cursor="hand2", font=btn_font, activebackground="#e3e1e1", image=category_image, compound=TOP, borderwidth=0, command=lambda: news_maker('2',False))
btn3.pack(side="right")
mybtn = tk.Button(menu, text="My News", cursor="hand2", font=btn_font, activebackground="#e3e1e1", image=mynews_image, compound=TOP, borderwidth=0, command=show_stories)
mybtn.pack(side="left", padx=(40,0), pady=(10, 10))
#======================================================== NEWSFEED
canvas = Canvas(root) # create canvas for news feed
canvas.pack(side=LEFT, fill=BOTH, expand=True)
# scrollbar
my_scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview) # add scrollbar to canvas
my_scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=my_scrollbar.set) # configure canvas to scrollbar
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

innerFrame = Frame(canvas) # create frame inside canvas
canvas.create_window((0,0), window=innerFrame, anchor="nw") # add innerframe to window in canvas


def news_maker(index, showingMyNews):
    
    global innerFrame
    innerFrame.destroy()
    innerFrame = Frame(canvas) # create frame inside canvas
    canvas.create_window((0,0), window=innerFrame, anchor="nw") # add innerframe to window in canvas
    innerFrame.bind('<Configure>', lambda e: canvas.configure(scrollregion = innerFrame.bbox("all")))

    category = news_api.news.categories[int(index)].articles

    for i in range(len(category)):
        
        #news image        
        url = category[i].image
        imageUrlValid = False
        try:
            news_image = Image.open(requests.get(url,stream=True).raw)
        except:
            news_image = Image.open("images/error404.png")

        news_image = news_image.resize((160,90))
        imgSmall = news_image.resize((32,32),resample=Image.BOX)
        news_image = imgSmall.resize(news_image.size,Image.NEAREST)  
        news_photo = ImageTk.PhotoImage(news_image)
        news_photo_label = ttk.Label(innerFrame, image=news_photo)
        news_photo_label.image = news_photo
        news_photo_label.grid(row=i, column=0, padx=(45,20), pady=20)

        article_data = Frame(innerFrame)
        article_data.grid(row=i, column=1, sticky="nw", pady=20)         

        url_label = Label(article_data, fg="grey", font=text_font, wraplength=400, text="view story online -->",  cursor="hand2")
        url_label.pack(fill="x")
        url_label.bind("<Button-1>", lambda e, url=category[i].url: webbrowser.open_new(url))
        # print(category[i].url)

        title_label = ttk.Label(article_data, text=category[i].title, font=title_font, wraplength=400)
        title_label.pack(fill="x")
        desc_label = ttk.Label(article_data, text=category[i].description, font=text_font, wraplength=400)
        desc_label.pack(fill="x")
    
        if showingMyNews == False:
            # save image
            save_image = Image.open("images/flop.png")
            save_photo = ImageTk.PhotoImage(save_image)
            save_photo_label = Button(innerFrame, fg="#0fd694", text="Save", image=save_photo, cursor="hand2", compound=TOP,borderwidth=0, activebackground="#e6e6e6", command=lambda categoryIndex=index,storyIndex=i: save_story(category[storyIndex], int(categoryIndex)))
            save_photo_label.image = save_photo
            save_photo_label.grid(row=i, column=2, sticky="sw", pady=20, padx=(80,0))
        else:
            delete_Image = Image.open("images/trash.png")
            delete_photo = ImageTk.PhotoImage(delete_Image)
            #print(category[i].image)
            delete_photo_label = Button(innerFrame, fg="#e30967", text="Delete", image=delete_photo, cursor="hand2", compound=TOP,borderwidth=0, activebackground="#e6e6e6", command=lambda storyID=category[i].savedID: delete_story(storyID))
            delete_photo_label.image = delete_photo
            delete_photo_label.grid(row=i, column=2, sticky="sw", pady=20, padx=(80,0))


def welcome():
    welcomeMessage = "Welcome, \n OMG - I can't believe you downloaded 'PaperBoyTM' you must be out of your mind! Either way, 'Welcome!' and enjoy the ride"
    instructions = "Select a topic from the folders above to view the latest news from your location\n\n Hit the save button to store your favourite news articles \n\n The 'My News' section is where you will find all of your saved stories  :)\n\n"
    welcomeMessage_label = ttk.Label(innerFrame, text=welcomeMessage, font=logo_font, wraplength=600)
    welcomeMessage_label.pack(padx=(75, 150), pady=(20,0)) 
    instructions_label = ttk.Label(innerFrame, text=instructions, font=logo_font, wraplength=600)
    instructions_label.pack(padx=(75, 150), pady=(20,0)) 
    

#======================================================== CALL NEWS BUILDER FUNCTION SO NEWS IS PRE LOADED
welcome()
news_api.buildNewsObject()

#======================================================== RUN APP
root.mainloop()

