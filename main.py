import cv2 as cv
import sys
from tkinter import *

#Inicializando a classe Main
class Main():
    def __init__(self):

        # Criando a janela inicial
        self.root = Tk()
        self.root.title('Biometry Login')
        self.root.bind('<Escape>', self.close)
        self.root.config(bg="#202020", height=500, width=500)

        # Setando uma fonte padrao
        self.fonte = ('Calibri', '13')

        # Label top
        self.text = Label(self.root, text="Bem vindo!\nSelecione abaixo o que deseja fazer:",
                          justify=CENTER, font=self.fonte, bg='#202020', fg='#ffffff')
        self.text.place(relx=0.5, rely=0.5, y=-150, anchor='s')

        # Botao Adm
        self.button1 = Button(self.root, text="Acessar como Administrador", justify=CENTER,
                              font=self.fonte, bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.connectCam())
        self.button1.place(relx=0.5, rely=0.5, y=-50, anchor='s')

        # Botao Operador
        self.button2 = Button(self.root, text="Acessar como Operador", justify=CENTER, font=self.fonte,
                              bg="#323232", fg="#FFFFFF", width=25, command=lambda: self.connectCam())
        self.button2.place(relx=0.5, rely=0.5, y=0, anchor='s')

        self.root.mainloop()

    # Fechar aplicacao
    def close(self, event):
        sys.exit(0)

    # Inicializando a camera do dispositivo
    def connectCam(self):
        cam = cv.VideoCapture(0)

        while(1):
            ret, frame = cam.read()
            cv.imshow("Video", frame)

            k = cv.waitKey(30) & 0xff
            if k == 27:
                break

        cam.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    main = Main()
