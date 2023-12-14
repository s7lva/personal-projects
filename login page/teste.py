class ContaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Conta Interface")

        self.teste = True
        self.op = None

        self.label = Label(master, text="Escolha uma opção")
        self.label.grid(row=0, column=0, columnspan=2)

        self.option_var = IntVar()
        self.option_var.set(1)

        self.create_button = Radiobutton(master, text="1. Criar conta", variable=self.option_var, value=1)
        self.create_button.grid(row=1, column=0, padx=10)
        self.login_button = Radiobutton(master, text="2. Login", variable=self.option_var, value=2)
        self.login_button.grid(row=2, column=0, padx=10)
        self.exit_button = Radiobutton(master, text="3. Sair", variable=self.option_var, value=3)
        self.exit_button.grid(row=3, column=0, padx=10)

        self.submit_button = Button(master, text="Submit", command=self.handle_submit)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_label = Label(master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    def handle_submit(self):
        self.op = self.option_var.get()

        if self.op == 1:
            nome = input("Digite um nome: ")
            try:
                pin = int(input("Escolha um pin com no mínimo 8 caracteres: "))
            except ValueError:
                print("O pin apenas pode conter números")
                return
            numerotelemovel = input("Introduza o seu número de telemóvel: ")
            email = input("Introduza o seu email: ")
            conta = Conta(nome, email, pin, numerotelemovel)
            dados = f'Os seus dados da conta serão: {conta.get_nome()}/{conta.get_pin()}/{conta.get_numerotelemovel()}/{conta.get_email()}'
            self.result_label.config(text=dados)

        elif self.op == 2:
            email = input("Introduza o seu email: ")
            pin = input("Introduza o seu pin: ")
            dados = f'Os dados de acesso à conta são: {pin} e {email}'
            self.result_label.config(text=dados)

        elif self.op == 3:
            self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    app = ContaApp(root)
    root.mainloop()