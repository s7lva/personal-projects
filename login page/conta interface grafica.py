import tkinter as tk
from tkinter import ttk
from Conta import Conta

def open_new_page():
    new_page = tk.Toplevel(window)
    new_page.title("Create account page")
    
    

    nome_var = tk.StringVar()
    pin_var = tk.StringVar()
    numero_var = tk.StringVar()
    email_var = tk.StringVar()

    ttk.Entry(new_page, textvariable=nome_var, width=30).pack(pady=10)
    ttk.Entry(new_page, textvariable=pin_var, show="*", width=30).pack(pady=10)
    ttk.Entry(new_page, textvariable=numero_var, width=30).pack(pady=10)
    ttk.Entry(new_page, textvariable=email_var, width=30).pack(pady=10)

    
    ttk.Button(new_page, text="create", command=lambda: fazer_login(nome_var.get(), pin_var.get(), numero_var.get(), email_var.get())).pack()
def Open_nova_page():
    nova_page = tk.Toplevel(window)
    nova_page.title("Login page")
    

    pin_var = tk.StringVar()
    numero_var = tk.StringVar()

    ttk.Entry(nova_page, textvariable=numero_var, show= "-" ,width=30).pack(pady=10)
    ttk.Entry(nova_page, textvariable=pin_var, show="~", width=30).pack(pady=10)

    ttk.Button(nova_page, text="login", command=lambda: fazer_login(pin_var.get(), numero_var.get())).pack()


 

def criar_conta(nome, pin, numero, email):
    
    if not nome or not pin or not numero or not email:
        print("Por favor, preencha todos os campos.")
        return

    if len(pin) != 4 or not pin.isdigit():
        print("PIN inválido. Deve ter 4 dígitos.")
        return
    
    if not numero.isdigit():
        print("Número de telefone inválido. Deve conter apenas dígitos.")
        return
    
    if "@" not in email or "." not in email:
        print("Endereço de e-mail inválido.")
        return

    conta = Conta(nome, pin, numero, email)
    print(f"Conta criada: {conta.nome}, {conta.pin}, {conta.numero_telefone}, {conta.email}")




def fazer_login(numero, pin):
    # Aqui você faria a lógica de verificação do login

    if not numero or not pin:
        print("Por favor, prenencha todos os campos")
        return

    if not numero.isdigit():
        print("Numero de telefone inválido. Deve conter apenas digitos")
        return  

    print(f"Fazendo login com o numero: {pin} e pin: {numero}")
    print("login feito ")




window = tk.Tk()
window.title("Menu de app")

botao_criar_conta = ttk.Button(window, text="Create account", command=open_new_page)
botao_criar_conta.pack(pady=10)

botao_login = ttk.Button(window, text="Login", command=Open_nova_page)
botao_login.pack(pady=10)

botao_sair = ttk.Button(window, text="Sair", command=window.quit)
botao_sair.pack(pady=10)






window.mainloop()



