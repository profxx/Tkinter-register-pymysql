from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from getpass import getpass
import pymysql

class Register:
	def __init__(self, root):
		self.root = root
		self.root.title("Cadastro")
		self.root.geometry("1350x700+0+0")
		self.root.state("zoomed")
		# Bg Color
		self.root.configure(background = "white")
		
		# Bg Image
		self.bg = ImageTk.PhotoImage(file="images/login_bg.png")
		bg=Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

		# LEFT Image
		self.left = ImageTk.PhotoImage(file="images/login_side.jpg")
		left=Label(self.root, image=self.left)
		left.place(x=80, y=100, width=400, height=500)
		
		# Icon
		self.root.iconbitmap('images/icon.ico')

		# Cadastro frame
		frame1 = Frame(self.root, bg='white')
		frame1.place(x=480, y=100, width=700, height=500)

		title = Label(
			frame1, 
			text="CADASTRE-SE", 
			font=("times new roman", 20, "bold"), 
			bg="white", 
			fg='#067EED')
		title.place(x=50, y=30)

		# ---------------Linha1 Y = 100
		linha1 = 100
		linha1a = linha1+30
		loginName = Label(frame1, text="Nome para Login", font=("verdana", 12), bg="white", fg='gray').place(x=50, y=linha1)
		self.txt_loginName = Entry(
			frame1, 
			font=("times new roman", 16), 
			bg="lightgray", 
			fg="#0e3854")
		self.txt_loginName.place(x=50, y=linha1a, width=250)

		cpf = Label(frame1, text="CPF", font=("verdana", 12), bg="white", fg='gray').place(x=370, y=linha1)
		self.txt_cpf = Entry(frame1, font=("times new roman", 16), bg="lightgray", fg="#0e3854")
		self.txt_cpf.place(x=370, y=linha1a, width=250)

		# ---------------Linha2 Y = 170
		linha2 = 170
		linha2a = linha2+30
		firstName = Label(frame1, text="Primeiro Nome", font=("verdana", 12), bg="white", fg='gray').place(x=50, y=linha2)
		self.txt_firstName = Entry(frame1, font=("times new roman", 16), bg="lightgray", fg="#0e3854")
		self.txt_firstName.place(x=50, y=linha2a, width=250)

		lastName = Label(frame1, text="Sobrenome", font=("verdana", 12), bg="white", fg='gray').place(x=370, y=linha2)
		self.txt_lastName = Entry(frame1, font=("times new roman", 16), bg="lightgray", fg="#0e3854")
		self.txt_lastName.place(x=370, y=linha2a, width=250)

		# ---------------Linha3 Y = 240
		linha3 = 240
		linha3a = linha3+30
		email = Label(frame1, text="E-mail", font=("verdana", 12), bg="white", fg='gray').place(x=50, y=linha3)
		self.txt_email = Entry(frame1, font=("times new roman", 16), bg="lightgray", fg="#0e3854")
		self.txt_email.place(x=50, y=linha3a, width=250)

		telefone = Label(frame1, text="Telefone", font=("verdana", 12), bg="white", fg='gray').place(x=370, y=linha3)
		self.txt_telefone = Entry(frame1, font=("times new roman", 16), bg="lightgray", fg="#0e3854")
		self.txt_telefone.place(x=370, y=linha3a, width=250)

		# ---------------Linha4 Y = 310
		linha4 = 310
		linha4a = linha4+30
		senha1 = Label(frame1, text="Senha (mín. 7 dígitos)", font=("verdana", 12), bg="white", fg='gray').place(x=50, y=linha4)
		self.txt_senha1 = Entry(frame1, font=("times new roman", 16), bg="lightgray", fg="#0e3854", show="*")
		self.txt_senha1.place(x=50, y=linha4a, width=250)

		senha2 = Label(frame1, text="Confirme a Senha", font=("verdana", 12), bg="white", fg='gray').place(x=370, y=linha4)
		self.txt_senha2 = Entry(frame1, font=("times new roman", 16), bg="lightgray", fg="#0e3854", show="*")
		self.txt_senha2.place(x=370, y=linha4a, width=250)

		# ---------------Linha5 y = 380
		linha5 = 380
		linha5a = linha5+30
		nivel = Label(frame1, text="Nível de Acesso", font=("verdana", 12), bg="white", fg='gray').place(x=480, y=linha5)
		self.cmb_nivel = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify = "center")
		self.cmb_nivel['values']=('-', 'Gestor', 'Supervisor', 'Operador')
		self.cmb_nivel.place(x=540, y=linha5a, width=80)
		self.cmb_nivel.current(0)

		self.var_chk = IntVar()
		chk = Checkbutton(frame1, text="Eu aceito os termos e condições.", bg="white", fg="gray", variable=self.var_chk, onvalue=1, offvalue=0).place(x=50, y=linha5)


		# ---------------Linha6 Y = 450
		linha6 = 450
		linha6a = linha6+30

		# Botões linha 6
		posxbtn = 50
		self.btn_img1 = ImageTk.PhotoImage(file = "images\cadastrar.png")
		self.btncad = Button(frame1, image=self.btn_img1, bg='white', bd=0, cursor="hand2", command=self.register_data)
		self.btncad.place(x=posxbtn, y=440)

		self.btn_img2 = ImageTk.PhotoImage(file = "images\cancelar.png")
		self.btncanc = Button(frame1, image=self.btn_img2, bg='white', bd=0, cursor="hand2", command=exit)
		self.btncanc.place(x=posxbtn+130, y=440)

		self.btn_img3 = ImageTk.PhotoImage(file = "images\limpar.png")
		self.btnlimpa = Button(frame1, image=self.btn_img3, bg='white', bd=0, cursor="hand2", command=self.clear)
		self.btnlimpa.place(x=posxbtn+260, y=440)

	def clear(self):
		self.txt_loginName.delete(0, END)
		self.txt_cpf.delete(0, END)
		self.txt_firstName.delete(0, END)
		self.txt_lastName.delete(0, END)
		self.txt_email.delete(0, END)
		self.txt_telefone.delete(0, END)
		self.txt_senha1.delete(0, END)
		self.txt_senha2.delete(0, END)
		self.cmb_nivel.current(0)
		self.var_chk.set(0)

	def register_data(self):
		# Mensagens de erro
		if self.txt_loginName.get()=="" or self.txt_cpf.get()=="" or self.txt_firstName.get()=="" or self.txt_lastName.get()=="" or self.txt_email.get()=="" or self.txt_telefone.get()=="" or self.txt_senha1.get()=="" or self.txt_senha2.get()=="" or self.cmb_nivel.get()=="-":
			messagebox.showerror("Erro", "Todos os campos deverão ser preenchidos.",parent=self.root)
		elif self.txt_senha1.get()!=self.txt_senha2.get():
			messagebox.showerror("Erro", "A senha e a confirmação da mesma devem ser iguais.", parent=self.root)
		elif self.var_chk.get()==0:
			messagebox.showerror("Erro", "Você deve ler e aceitar os termos e condições antes de continuar.", parent=self.root)
		# Mensagem de cadastro com sucesso.
		else:
			try:
				con = pymysql.connect(host="localhost", user="root", password="", database="colaboradores")
				cur = con.cursor()
				cur.execute("SELECT * FROM funcionarios WHERE email=%s", self.txt_email.get())
				cur.execute("SELECT * FROM funcionarios WHERE cpf=%s", self.txt_cpf.get())
				row = cur.fetchone()
				if row!=None:
					messagebox.showerror("Erro", "Usuário já cadastrado, faça o login.", parent=self.root)
				else:
					cur.execute("INSERT INTO funcionarios(loginname, cpf, firstname, lastname, email, telefone, senha, nivel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
									(
										self.txt_loginName.get(),
										self.txt_cpf.get(),
										self.txt_firstName.get(),
										self.txt_lastName.get(),
										self.txt_email.get(),
										self.txt_telefone.get(),
										self.txt_senha1.get(),
										self.cmb_nivel.get()
									))
					con.commit()
					con.close()
					messagebox.showinfo("Sucesso", "Cadastro efetuado com sucesso.", parent=self.root)
					self.clear()
			
			except Exception as es:
				messagebox.showerror("Erro", f"Erro em decorrência de {str(es)}.", parent=self.root)


root = Tk()
obj = Register(root)
root.mainloop()