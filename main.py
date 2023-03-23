from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageOps, ImageDraw
import requests
import json
import string


dark_blue = '#38576b'


# 'api.exchangerate-api.com/v4/latest/USD'
def convert():

    moeda_from = combo_from.get()
    moeda_to = combo_to.get()
    valor = value.get()

    try:
        response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{moeda_from}')
        data = json.loads(response.text)
        result = data['rates'][moeda_to]

        result = float(valor) * float(result)
            
        simbolos = {'USD': 'US$', 'EUR': '€', 'INR': '₹', 'AOA': 'Kz', 'BRL': 'R$', 'CAD': 'C$', 'GBP': '£',
                     'AUD': 'AU$', 'MZN': 'MT', 'JPY': '¥', 'KRW': '₩', 'NZD': 'NZ $'}

        equivalente = f'{simbolos[moeda_to]} {result:,.2f}'
        app_result['text'] = equivalente

    except SyntaxError:
        messagebox.showerror(title='Error', message='Preencha os campos corretamente')
        return False
    except TypeError:
        messagebox.showerror(title='Error', message='Preencha os campos corretamente')
        return False
    except ValueError:
        messagebox.showerror(title='Error', message='Preencha os campos corretamente')
        return False
    except KeyError:
        messagebox.showerror(title='Error', message='Preencha os campos corretamente')
        return False


window = Tk()
window.title('CoinConverter')
window.geometry('340x320')
window.config(bg='#3d3939')
window.resizable(width=False, height=False)


icon = Image.open('./coin_icon.png')
icon = icon.resize((40, 40), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(icon)


frame_title = Frame(window, width=340, height=60, padx=0, pady=0, bg=dark_blue, relief='flat')
frame_title.grid(row=0, column=0)

frame_result = Frame(window, width=340, height=260, padx=0, pady=5, bg='#3d3939', relief='flat')
frame_result.grid(row=1, column=0)


app_name = Label(frame_title, image=icon, compound=LEFT, text='Coin Converter      ', height=5,
                 pady=30, padx=10, relief='raised', anchor=CENTER, font=('Arial', 24, 'bold'),
                 bg=dark_blue, fg='white')
app_name.place(x=0, y=0)

app_result = Label(frame_result, text='', width=16, height=2, relief='solid', anchor=CENTER,
                   font=('Ivy', 15, 'bold'), bg='white', fg='#3d3939')
app_result.place(x=77, y=25)

from_label = Label(frame_result, text='From:', width=8, height=1, relief='flat', anchor=NW,
                   font=('Ivy', 10, 'bold'), bg='#3d3939', fg='white')
from_label.place(x=39, y=120)

to_label = Label(frame_result, text='To:', width=8, height=1, relief='flat', anchor=NW,
                 font=('Ivy', 10, 'bold'), bg='#3d3939', fg='white')
to_label.place(x=213, y=120)

coins = ['AOA', 'BRL', 'EUR', 'INR', 'USD', 'CAD', 'GBP', 'AUD', 'MZN', 'JPY', 'KRW', 'NZD']

combo_from = ttk.Combobox(frame_result, width=8, justify=CENTER, font=('Ivy', 12, 'bold'))
combo_from.place(x=40, y=140)
combo_from['values'] = coins

combo_to = ttk.Combobox(frame_result, width=8, justify=CENTER, font=('Ivy', 12, 'bold'))
combo_to.place(x=217, y=140)
combo_to['values'] = coins


value = Entry(frame_result, width=22, justify=CENTER, font=('Ivy', 12, 'bold'), relief=SOLID)
value.place(x=75, y=180)

press = Button(frame_result, text='Convert', width=19, height=1, padx=5, bg=dark_blue, fg='white', command=convert)
press.place(x=101, y=215)


window.mainloop()
