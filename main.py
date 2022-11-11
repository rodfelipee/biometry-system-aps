# Bibliotecas
import cv2 as cv
import ctypes
import sys
from tkinter import *


class Main():
    # Inicializando a classe Main
    def __init__(self):

        # Criando a janela inicial
        self.root = Tk()
        self.root.withdraw()

        # Setando uma fonte padrao
        self.fonte = ('Calibri', '13')

        self.inicio = Toplevel()
        self.inicio.title('Biometry Login')
        self.inicio.resizable(0, 0)
        self.inicio.config(bg="#202020", height=500, width=500)
        self.centerWindow(self.inicio)

        # Label top
        self.text = Label(self.inicio, text="Bem vindo!\nSelecione abaixo o que deseja fazer:",
                          justify=CENTER, font=self.fonte, bg='#202020', fg='#ffffff')
        self.text.place(relx=0.5, rely=0.5, y=-150, anchor='s')

        # Botao Admin
        self.button1 = Button(self.inicio, text="Acessar como Administrador", justify=CENTER,
                              font=self.fonte, bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.turnCamOn())
        self.button1.place(relx=0.5, rely=0.5, y=-50, anchor='s')

        # Botao Operador
        self.button2 = Button(self.inicio, text="Acessar como Operador", justify=CENTER, font=self.fonte,
                              bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.turnCamOn())
        self.button2.place(relx=0.5, rely=0.5, y=0, anchor='s')

        # Botao adicionar rosto
        self.button3 = Button(self.inicio, text="Adicionar um novo rosto", justify=CENTER, font=self.fonte,
                              bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.changeToaddLogin())
        self.button3.place(relx=0.5, rely=0.5, y=225, anchor='s')

        # Binds
        self.inicio.bind('<Escape>', self.close)

        # Mantendo o Tk ativo em loop
        self.root.mainloop()

    def changeToaddLogin(self):
        # Tela de acesso para registrar nova face
        self.inicio.withdraw()
        self.addUserLogin()

    def addUserLogin(self):
        # Tela para adicionar um novo rosto

        # Parametros da janela
        self.addLogin = Toplevel()
        self.addLogin.title('Registrar usuario')
        self.addLogin.resizable()
        self.addLogin.config(bg='#202020', width=350, height=350)
        self.centerWindow(self.addLogin)

        # Texto / Label
        self.texto = Label(self.addLogin, text="insira a senha mestre para registrar um usuario",
                           justify=CENTER, font=self.fonte, bg='#202020', fg='#ffffff')
        self.texto.place(relx=0.5, rely=0.5, y=-100, anchor='s')

        self.entryPassw = Entry(self.addLogin, justify=CENTER, font=self.fonte,
                                bg='#505050', fg='#FFFFFF', width=25, show='*')
        self.entryPassw.place(relx=0.5, rely=0.5, y=-50, anchor='s')
        self.entryPassw.focus()

        # Botao de Submit
        self.btnEntrar = Button(self.addLogin, text='Entrar', font=self.fonte, width=25, justify=CENTER,
                                bg='#303030', fg='#ffffff', command=lambda: self.checkPassword(self.entryPassw.get()))
        self.btnEntrar.place(relx=0.5, rely=0.5, y=-0, anchor='s')

        # Botao para voltar a tela inicial
        self.btnVoltar = Button(self.addLogin, text="Voltar", font=self.fonte, width=25, justify=CENTER,
                                bg='#303030', fg='#ffffff', command=lambda: self.voltarInicio())
        self.btnVoltar.place(relx=0.5, rely=0.5, y=50, anchor='s')

        # Binds
        self.addLogin.bind('<Escape>', self.close)
        self.addLogin.bind(
            '<Return>', lambda x: self.checkPassword(self.entryPassw.get()))

    def voltarInicio(self):
        # Retorna a tela inicial
        self.addLogin.withdraw()
        self.__init__()

    def checkPassword(self, passw):
        # Valida senha
        if passw == "aps@unip":
            self.addUserCam()
        else:
            self.Mbox('Acesso Negado', 'A senha inserida está incorreta', 1)

    def close(self, event):
        # Fechar aplicacao
        sys.exit(0)

    def addUserCam(self):
        # Chama a camera para registrar uma face
        self.turnCamOn()

    def turnCamOn(self):
        # Inicializando a camera do dispositivo
        cam = cv.VideoCapture(0)

        # Loop que mantem a captura
        while (1):
            ret, frame = cam.read()
            cv.imshow("Video", frame)

            k = cv.waitKey(30) & 0xff
            if k == 27:
                break

        cam.release()
        cv.destroyAllWindows()

    def centerWindow(self, window):
        # Centraliza a janela

        window.update_idletasks()

        # Define o tamanhoda janela
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2 * frm_width

        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width

        # Obtem a posicao da janela de forma dinamica realizando um calculo com base no tamanho da tela e da janela
        x = window.winfo_screenwidth() // 2 - win_width // 2
        y = window.winfo_screenheight() // 2 - win_height // 2

        # Posiciona a janela no centro da tela
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        window.deiconify()

    def Mbox(self, title, text, style):
        # Funcao para exibir mensagem de popup custom
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)


# Validando e chamando a main
if __name__ == "__main__":
    main = Main()
