# importando bibliotecas
from tkinter import *
from tkinter import ttk

#   cores
color1 = "#0d140f"  # preto esverdeado
color2 = "#CBF1F5"  # branco acizentada
color3 = "#ffffff"  # branco
color4 = "#A6E3E9"  # verde morno python
color5 = "#02c73d"  # verde muito claro
color6 = "#71C9CE"  # verde clarinho
color7 = "#E3FDFD"  # branco azulado


#   define a janela calculadora total
window = Tk()
window.title("Calculadora")
window.geometry("234x299")
window.config(bg=color1)

# criação do display da calculadora
frame_display = Frame(window, width=235, height=50, bg=color7)
frame_display.grid(row=0, column=0)


# criação do corpo da calculadora
frame_body = Frame(window, width=235, height=248, bg=color4)
frame_body.grid(row=1, column=0)

# b --------------- Botões do corpo  -----------------=

# Botão Label
text_value = StringVar()

app_label = Label(frame_display, textvariable=text_value, width=16,
                  height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=color7, fg=color1)
app_label.place(x=0, y=0)


#   Botão da Função clear (limpar display):
bt1 = Button(frame_body, text="C", width=13, height=2, bg=color2,
             font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt1.place(x=0, y=0)


#   Botão da função de porcentagem

bt2 = Button(frame_body, text="%", width=5, height=2, bg=color2,
             font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE, command=lambda: submiting('%'))
bt2.place(x=125, y=0)


#   Botão da função divisão

bt3 = Button(frame_body, text="/", width=5, height=2, bg=color6,
             font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt3.place(x=180, y=0)

#   Botão da função de multiplicação:
bt9 = Button(frame_body, text="X", width=5, height=2, bg=color6,
             font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt9.place(x=180, y=50)

#   Botão da função de subtração
bt13 = Button(frame_body, text="-", width=5, height=2, bg=color6,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt13.place(x=180, y=100)

#   Botão da Função Adição
bt17 = Button(frame_body, text="+", width=5, height=2, bg=color6,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt17.place(x=180, y=150)

#   Botão da função = (igual)
bt21 = Button(frame_body, text="=", width=5, height=2, bg=color4,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt21.place(x=180, y=200)

#   Botões numerados:

bt6 = Button(frame_body, text="7", width=6, height=2, bg=color2,
             font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt6.place(x=0, y=50)

bt7 = Button(frame_body, text="8", width=6, height=2, bg=color2,
             font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt7.place(x=63, y=50)

bt8 = Button(frame_body, text="9", width=5, height=2, bg=color2,
             font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt8.place(x=125, y=50)

bt10 = Button(frame_body, text="4", width=6, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt10.place(x=0, y=100)

bt11 = Button(frame_body, text="5", width=6, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt11.place(x=63, y=100)


bt12 = Button(frame_body, text="6", width=5, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt12.place(x=125, y=100)

bt14 = Button(frame_body, text="1", width=6, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt14.place(x=0, y=150)

bt15 = Button(frame_body, text="2", width=6, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt15.place(x=63, y=150)

bt16 = Button(frame_body, text="3", width=5, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt16.place(x=125, y=150)

bt18 = Button(frame_body, text="+/-", width=6, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt18.place(x=0, y=200)

bt19 = Button(frame_body, text="0", width=6, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt19.place(x=63, y=200)

bt20 = Button(frame_body, text=",", width=5, height=2, bg=color2,
              font=("Ivy 11 bold"), relief=RAISED, overrelief=RIDGE)
bt20.place(x=125, y=200)


# Variavel all_value (todos valores)
all_value = ''

# Criando função da calc


def submiting(event):
    global all_value
    all_value = all_value + str(event)
    # Mostrando o valor no display
    text_value.set(all_value)


window.mainloop()
