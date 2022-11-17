# Bibliotecas
import cv2 as cv
import face_recognition as fr
import ctypes
import sys
import numpy as np
from tkinter import *


class Main():
    # Inicializando a classe Main
    def __init__(self):

        # Criando a janela inicial
        self.root = Tk()
        self.root.withdraw()

        # Definindo uma fonte padrao
        self.fonte = ('Calibri', '13')

        # Janela de inicio e configuracoes
        self.inicio = Toplevel()
        self.inicio.title('Biometry Login')
        self.inicio.resizable(0, 0)
        self.inicio.config(bg="#202020", height=500, width=500)
        self.centerWindow(self.inicio)

        # Label top
        self.text = Label(self.inicio, text="Bem vindo!\nSelecione abaixo o que deseja fazer:",
                          justify=CENTER, font=self.fonte, bg='#202020', fg='#ffffff')
        self.text.place(relx=0.5, rely=0.5, y=-150, anchor='s')

        # Botao nivel 3
        self.button1 = Button(self.inicio, text="Acesso nivel 3", justify=CENTER,
                              font=self.fonte, bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.validateUser())
        self.button1.place(relx=0.5, rely=0.5, y=-50, anchor='s')

        # Botao nivel 2
        self.button2 = Button(self.inicio, text="Acesso nivel 2", justify=CENTER, font=self.fonte,
                              bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.validateUser())
        self.button2.place(relx=0.5, rely=0.5, y=0, anchor='s')

        # Botao nivel 1
        self.button3 = Button(self.inicio, text="Acesso nivel 1", justify=CENTER, font=self.fonte,
                              bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.validateUser())
        self.button3.place(relx=0.5, rely=0.5, y=50, anchor='s')

        # Botao adicionar rosto
        self.button4 = Button(self.inicio, text="Adicionar um novo rosto", justify=CENTER, font=self.fonte,
                              bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.changeToaddLogin())
        self.button4.place(relx=0.5, rely=0.5, y=225, anchor='s')

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

        #Caixa para inserir a senha
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
        # Valida a senha
        if passw == "aps@unip":
            self.addUserCam()
        else:
            self.Mbox('Acesso Negado', 'A senha inserida esta incorreta', 0)

    def close(self, event):
        # Fechar aplicacao
        sys.exit(0)

    def addUserCam(self):
        # Inicializando a camera do dispositivo
        cam = cv.VideoCapture(0)
        img_count = 0

        # Mensagem informativa ao abrir a camera
        self.Mbox('Info', 'Pressione a tecla Space para capturar uma imagem.', 0)

        # Loop que mantem a captura
        while not cv.waitKey(5) & 0xff == 27:
            ret, frame = cam.read()
            cv.imshow("Video", frame)

            if cv.waitKey(5) == 32:
                # Definindo o caminho e salvando a imagem capturada
                img_name = "./img/img_frame_{}.png".format(img_count)
                cv.imwrite(img_name, frame)
                img_count += 1
                self.Mbox('Imagem Salva!','A imagem foi salva com sucesso na pasta "img"', 0)

        cam.release()
        cv.destroyAllWindows()

    def validateUser(self):
        # Realizando a validacao de usuarios junto da camera

        # Inicializando a camera do dispositivo
        cam = cv.VideoCapture(0)

        # Carregando imagem do perfil nivel 3
        nivel3_face_load = fr.load_image_file("./img/nv3/hasbulla_ministro.jpg")
        nivel3_face_encode = fr.face_encodings(nivel3_face_load)

        # Carregando imagem do perfil nivel 2
        nivel2_face_load = fr.load_image_file("./img/nv2/fallen_diretor.png")
        nivel2_face_encode = fr.face_encodings(nivel2_face_load)

        # Carregando imagem do perfil nivel 1
        nivel1_face_load = fr.load_image_file("./img/nv1/ellon_geral.jpg")
        nivel1_face_encode = fr.face_encodings(nivel1_face_load)

        face_locations = []
        face_encodings = []
        s = True

        # Loop que mantem a captura
        while not cv.waitKey(5) & 0xff == 27:
            # Executando leitura da camera
            ret, frame = cam.read()
            # Redimensionando o frame
            small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
            # convertendo o frame de bgr para rgb
            rgb_small_file = small_frame[:, :, ::-1]
            if s:
                face_locations = fr.face_locations(rgb_small_file)
                face_encodings = fr.face_encodings(rgb_small_file, face_locations)

                # Comparacao nivel 3
                for face_encoding in face_encodings:
                    nivel3_matches = fr.compare_faces(nivel3_face_encode, face_encoding)
                    nivel3_face_distance = fr.face_distance(nivel3_face_encode, face_encoding)
                    nivel3_best_match_index = np.argmin(nivel3_face_distance)

                    # Validando a imagem
                    if nivel3_matches[nivel3_best_match_index]:
                        self.Mbox('Acesso Permitido', 'Perfil Ministro!\nAcesso nível 3!\nVoce esta autorizado a utilizar o sistema!', 0)

                # Comparacao nivel 2
                for face_encoding in face_encodings:
                    nivel2_matches = fr.compare_faces(
                        nivel2_face_encode, face_encoding)
                    nivel2_face_distance = fr.face_distance(
                        nivel2_face_encode, face_encoding)
                    nivel2_best_match_index = np.argmin(nivel2_face_distance)
                    # Validando a imagem
                    if nivel2_matches[nivel2_best_match_index]:
                        self.Mbox('Acesso Permitido', 'Perfil Diretor!\nAcesso nível 2!\nVoce esta autorizado a utilizar o sistema!', 0)

                # Comparacao nivel 1
                for face_encoding in face_encodings:
                    nivel1_matches = fr.compare_faces(
                        nivel1_face_encode, face_encoding)
                    nivel1_face_distance = fr.face_distance(
                        nivel1_face_encode, face_encoding)
                    nivel1_best_match_index = np.argmin(nivel1_face_distance)
                    # Validando a imagem
                    if nivel1_matches[nivel1_best_match_index]:
                        self.Mbox('Acesso Permitido', 'Perfil Geral!\nAcesso nível 2!\nVoce esta autorizado a utilizar o sistema!', 0)

            # Exibindo a imagem da camera
            cv.imshow("Video", frame)

        cam.release()
        cv.destroyAllWindows()

    def close(self, event):
        # Fechar aplicacao
        sys.exit(0)

    def centerWindow(self, window):
        # Centraliza a janela

        window.update_idletasks()

        # Define o tamanho da janela
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
