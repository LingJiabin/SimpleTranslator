import tkinter as tk
import tkinter.font as tkFont
import requests as rq
import json

source_lang = 'EN'
target_lang = 'ZH'


def http_post(text1, text2):
    content = text1.get('1.0', 'end')
    if(content == ""):
        return ""
    url = "http://124.223.61.24:1188/translate"
    headers = {'Content-Type': 'application/json'}
   
    data = {'text': content,
            'source_lang': source_lang,
            'target_lang': target_lang}
    print(data)
    timeout = 5
    try:
        response = rq.post(url, headers=headers, data=json.dumps(data),timeout=timeout)
        response.raise_for_status()
    except rq.exceptions.RequestException:
         response = rq.post(url, headers=headers, data=json.dumps(data),timeout=timeout)   
         response.raise_for_status()
         
    rspon_data = response.json() 
    if(rspon_data['code'] == 200):
        text2.delete("1.0", 'end')
        text2.insert(tk.END, rspon_data["data"])
            
    else:
        print("error code: " + rspon_data['code'])
    return response

def clear_text(text1, text2):
    text1.delete("1.0", "end")
    text2.delete("1.0", "end")

def change_translation(selected_option1, selected_option2):
    # print(selected_option1.get())
    # print(selected_option2.get())
    global source_lang
    global target_lang
    source_lang = selected_option2.get()
    target_lang = selected_option1.get()
    
    selected_option1.set(source_lang)
    selected_option2.set(target_lang)
    
    

def change_source_lang(selection):
    global source_lang
    source_lang = selection
def change_target_lang(selection):
    global target_lang
    target_lang = selection

def copy(text):
    text.event_generate("<<Copy>>")

def paste(text):
    text.event_generate("<<Paste>>")
def cut(text):
    text.event_generate("<<Cut>>")    

top_window = tk.Tk()
top_window.title("text translate")
top_window.geometry('840x520+20+20')
top_window["background"] = "#C9C9C9"

frame0 = tk.Frame(top_window)
frame1 = tk.Frame(frame0, width=100, height=40)
frame1_top = tk.Frame(frame1)
frame2 = tk.Frame(frame0, width=100, height=40)
frame2_top = tk.Frame(frame2)
frame3 = tk.Frame(top_window)


frame0.pack(side="top", fill="x")
frame1.pack(side="left", anchor="n")
frame1_top.pack(side="top")
frame2.pack(side="right", anchor="n")
frame2_top.pack(side="top")
frame3.pack(side="bottom", anchor="n", fill="x")

label1 = tk.Label(frame1_top, width=20, height=2,text="?????????:")
label2 = tk.Label(frame2_top, width=20, height=2,text="????????????:")

selected_option1 = tk.StringVar()
selected_option1.set('EN')
selected_option2 = tk.StringVar()
selected_option2.set('ZH')
option = ["EN", "ZH", "JP"]

option_menu1 = tk.OptionMenu(frame1_top, selected_option1, *option, command=change_source_lang)
option_menu2 = tk.OptionMenu(frame2_top, selected_option2, *option, command=change_target_lang)

text_font = tkFont.Font(family="Microsoft YaHei", size=10, weight="bold")



text1 = tk.Text(frame1, width=50, height=20)
text2 = tk.Text(frame2, width=50, height=20)

tk_menu1 = tk.Menu(frame1, tearoff=False)
tk_menu1.add_command(label="??????", command=lambda:copy(text1))
tk_menu1.add_command(label="??????", command=lambda:paste(text1))
tk_menu1.add_command(label="??????", command=lambda:cut(text1))

tk_menu2 = tk.Menu(frame2, tearoff=False)
tk_menu2.add_command(label="??????", command=lambda:copy(text2))
tk_menu2.add_command(label="??????", command=lambda:paste(text2))
tk_menu2.add_command(label="??????", command=lambda:cut(text2))

text1.bind("<Button-3>", lambda e: tk_menu1.post(e.x_root, e.y_root))
text2.bind("<Button-3>", lambda e: tk_menu2.post(e.x_root, e.y_root))

text1.configure(font=text_font)
text2.configure(font=text_font)

text1.pack(side="bottom")
text2.pack(side="bottom")

label1.pack(side="left")
label2.pack(side="left")
option_menu1.pack(side="right")
option_menu2.pack(side="right")

botton_c = tk.Button(frame3, text="??????", command=lambda:clear_text(text1, text2))
botton_t = tk.Button(frame3, text="??????", command=lambda:http_post(text1, text2))
botton_ch = tk.Button(frame3, text="??????", command=lambda:change_translation(selected_option1, selected_option2))

botton_c.pack(side="bottom", fill='x')
botton_t.pack(side="bottom", fill='x')
botton_ch.pack(side="bottom", fill='x')



top_window.mainloop()