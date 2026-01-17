import customtkinter as ctk
from customtkinter import *
from PIL import Image
from discord import Webhook
import aiohttp
import asyncio
import os
import threading

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

webhook_entry_counter = 0

app = ctk.CTk()
app.title('Support available on my Discord Server < -- > Made by Drowys with love')
icon_path = os.path.join(os.path.dirname(__file__),"appico.ico")
app.iconbitmap(icon_path)
app.geometry('1000x800')
app.resizable(False, False)
get_started_path = os.path.join(os.path.dirname(__file__),"get_started.png")
gray_line_y_path = os.path.join(os.path.dirname(__file__),"gray.png")

get_started_image = ctk.CTkImage(light_image=Image.open(get_started_path),
	dark_image=Image.open(get_started_path),
	size=(1000,250))

gray_line_y_image = ctk.CTkImage(light_image=Image.open(gray_line_y_path),
	dark_image=Image.open(gray_line_y_path),
	size=(2,500)) 

my_icon = ctk.CTkImage(light_image=Image.open(icon_path),
	dark_image=Image.open(icon_path),
	size=(32,32))


my_label = ctk.CTkLabel(app, text="", image=get_started_image)
my_label.place(x=0, y=0)

my_gray = ctk.CTkLabel(app, text="", image=gray_line_y_image)
my_gray.place(x=490, y=275)

my_icon = ctk.CTkLabel(app, text="", image=my_icon)
my_icon.place(x=520, y=275)


#  def
async def start_app():
    async with aiohttp.ClientSession() as session:
        burl = webhook_entry.get()
        baname = name_entry.get()
        textbox_value = text_textbox.get("1.0", "end").strip()
        webhook = Webhook.from_url(burl, session=session)
        msg = await webhook.send(textbox_value, username=baname, wait=True)

def add_textbox_placeholder(textbox, placeholder, color="gray"):
    textbox.insert("1.0", placeholder)
    textbox.configure(text_color=color)

    def on_focus_in(event):
        if textbox.get("1.0", "end").strip() == placeholder:
            textbox.delete("1.0", "end")
            textbox.configure(text_color="white")

    def on_focus_out(event):
        if textbox.get("1.0", "end").strip() == "":
            textbox.insert("1.0", placeholder)
            textbox.configure(text_color=color)

    textbox.bind("<FocusIn>", on_focus_in)
    textbox.bind("<FocusOut>", on_focus_out)

def au_bname():
    baname = name_entry.get()
    if baname == "":
        baname = "Webhook"
    webhook_name_label.configure(text=baname)
    app.after(50, au_bname)
    

    
    
def au_textbox():
    textbox_value = text_textbox.get("1.0", "end").strip()
    if textbox_value == "Enter your message here...":
        textbox_value = ""
    webhook_display.configure(state="normal")     # unlock
    webhook_display.delete("1.0", "end")          
    webhook_display.insert("1.0", textbox_value)  
    webhook_display.configure(state="disabled")   # lock
    
    app.after(50, au_textbox)
    
def start_app_wrapper():
    asyncio.run_coroutine_threadsafe(start_app(), loop)

def run_loop():
    loop.run_forever()

#  Start


start_button = ctk.CTkButton(
    app,
    text="Send",
    command=start_app_wrapper,
    corner_radius=10,
    fg_color="#3B8ED0",
    hover_color="#2F6FA1"
)
start_button.place(x=785, y=278)

webhook_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter your webhook's URL.",
    width=200
)
webhook_entry.place(x=30, y=280)

name_entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter your webhook's name.",
    width=200
)
name_entry.place(x=260, y=280)

text_textbox = ctk.CTkTextbox(
    app,
    width=430,
    height=450,
)
text_textbox.place(x=30, y=315)

webhook_name_label = ctk.CTkLabel(
    app,
    text="Webhook",
    font=ctk.CTkFont(size=16, weight="bold"),
    text_color="#999999",  
    justify="center",
    wraplength=400
)
webhook_name_label.place(x=548, y=278)


webhook_display = ctk.CTkTextbox(app, width=400, height=450)
webhook_display.place(x=525, y=315)
webhook_display.configure(state="disabled")

add_textbox_placeholder(text_textbox, "Enter your message here...")

au_bname()
au_textbox()
threading.Thread(target=run_loop, daemon=True).start()
app.mainloop()


