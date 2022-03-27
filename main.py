import math
import random
from tkinter import *
from tkinter import messagebox
import json

sentences_to_type = [
    '''If you're visiting this page, you're likely here because you're searching for a random sentence. 
    Sometimes a random word just isn't enough, and that is where the random sentence generator comes into play. 
    By inputting the desired number, you can make a list of as many random sentences as you want or need. 
    Producing random sentences can be helpful in a number of different ways.''',
    '''Watch as unconnected words and their meanings appear together before your eyes.
     The random word generator can be your best friend whether you are searching for a plot line for the next bestseller,
      or trying to come up with the perfect brand, blog or website name.
     It transports the entire dictionary to a click of your mouse - just have your pen and paper or keyboard ready and 
     let the creativity flow.''',
    '''While not exactly a philosophical or political tale like our first two examples, this twisty short story from 
    Dahl does delve into some shady moral territory. We are introduced to Mary Maloney: a loving wife and dedicated 
    homemaker. In just a few short paragraphs describing how she welcomes her husband home, Dahl makes us sympathize 
    with Mary — before a rash act turns her life upside down and takes the reader with her on a dark journey. '''
]

# def userText(event):
#     text_input.delete(0,END)
#     usercheck=True

count = 60
timer = None
to_be_typed = random.choice(sentences_to_type)
corrected_cpm = 0

def matching_sentence():
    global to_be_typed
    global corrected_cpm
    user_type_char_per_min = text_input.get('1.0', 'end').replace(" ", "").replace("\n", "")
    total_type_char = to_be_typed.replace(" ", "").replace("\n", "")
    i = 0
    while i != len(user_type_char_per_min):
        if user_type_char_per_min[i] == total_type_char[i]:
            corrected_cpm += 1
        i = i +1

    wpm = math.ceil(corrected_cpm / 5)
    wpm_input.delete(0, "end")
    wpm_input.insert(0, math.ceil(corrected_cpm / 5))
    cpm_input.delete(0, "end")
    cpm_input.insert(0, corrected_cpm )
    high_Score_data = {
           'cpm' : corrected_cpm,
            'wpm' : wpm

        }


    try:
        with open("high_score.json", "r") as file:
            # reading from json
            data = json.load(file)

    except FileNotFoundError:
        with open("high_score.json", "w") as file:
            json.dump(high_Score_data, file, indent=4)
    else:
        if data["cpm"] < corrected_cpm:
            # updating
            data.update(high_Score_data)
            with open("high_score.json", "w") as file:
                # finally saving data
                json.dump(data, file, indent=4)
            messagebox.showinfo(title="High score!!", message=f"You are progressing \n\n CPM : {corrected_cpm} \n\n WPM: {wpm}")
        else:
            messagebox.showinfo(title="Your score!!", message=f"You could do better than this \n\n CPM : {corrected_cpm} \n\n WPM: {wpm}")











def start_typing():
    global timer
    global count

    if count == 0:
        matching_sentence()
    else:
        timer = window.after(1000, start_typing)
        count = count - 1
        # print(count)
        timer_input.delete('0', 'end')
        timer_input.insert(0, count)






window = Tk()
window.title("Typing speed test")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)

text_label = Label(text=to_be_typed, pady=30)
text_label.grid(row=1, column=0, columnspan=3)

text_input = Text(window, height = 5, width = 80)
text_input.insert('1.0', "Type the text here")
text_input.grid(row=2, column=0 , columnspan=3)
text_input.bind("<FocusIn>", lambda args: text_input.delete('1.0', 'end'))
# text_input.bind("<Key>", lambda args: print('end'))
# text_input.bind("<Key>", start_typing)
# password_input = Entry(width=21)
# password_input.grid(row=3, column=1)
# password_button = Button(text="Generate Password")
# password_button.grid(row=3, column=2)
#
# add_button = Button(text="Add", width="36")
# add_button.grid(row=4, column=1 , columnspan=3)
space_label = Label(text="")
space_label.grid(row=3, column=0)
wpm_label = Label(text="WPM :")
wpm_label.grid(row=4, column=0, sticky='w')
wpm_input = Entry(width=5)
wpm_input.insert(0, "0")
wpm_input.grid(row=4, column=0)

cpm_label = Label(text="CPM :")
cpm_label.grid(row=4, column=1, sticky='w')
cpm_input = Entry(width=5)
cpm_input.insert(0, "0")
cpm_input.grid(row=4, column=1)

timer_label = Label(text="Timer :")
timer_label.grid(row=4, column=2, sticky="w")
timer_input = Entry(width=5)
timer_input.insert(0, "0")
timer_input.grid(row=4, column=2)

space_label = Label(text="")
space_label.grid(row=5, column=0)

start_button = Button(text="Start typing", width="36", command=start_typing)
start_button.grid(row=6, column=0 , columnspan=3)
# text_label = Label(text=random.choice(sentences_to_type), pady=30)
# text_label.grid(row=1, column=0, columnspan=3)
# text_label = Label(text=random.choice(sentences_to_type), pady=30)
# text_label.grid(row=1, column=0, columnspan=3)






window.mainloop()