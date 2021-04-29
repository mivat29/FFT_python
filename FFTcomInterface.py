#   Algoritmo de FFT em Python que permite acelerar o processo de interpolação 
#   de uma grande quantidade de dados por polinomios trigonométricos.
#   Aluno:  Otávio Augusto Amorim de Oliveira
#   Código: 766906
#
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

#Função que faz o grafico da FFT
def mostrar():
    #Número de Pontos de Sinal
    n = int(num.get())
    
    #Período da onda, podemos considerar como se fosse o tempo 
    T = float(taxa.get())
    
    #Frequencia da onda 1
    fr1 = int(f1.get())
    
    #Frequencia da onda 2
    fr2 = int(f2.get())
    
    #Frequencia Angular
    w = 2.0*np.pi/T
    
    #Criando os sinais
    t  = np.linspace(0,T,n) # n números, de 0 a T -> tempo 
    s1 = np.cos(fr1*w*t) #sinal 1
    s2 = np.cos(fr2*w*t)# sinal 2
    
    #Soma dos sinais criados
    s = s1+s2

    freq = np.fft.fftfreq(n) #base de tempo para frequencia
    masc = freq >0  #filtra os valores, mostrando só os valores positivos 
    
    #Mostrando o Sinal 
    fft_calc = np.fft.fft(s)
    
    plt.figure(1)
    plt.title("Sinal Original") #titulo do grafico
    plt.ylabel("Amplitude") #nome do eixo y
    plt.xlabel("Tempo (s)") #nome do eixo x
    plt.plot(t,s)  #plota o grafico
    
    #Mostrando o Sinal da FFT
    plt.figure(2)
    plt.title("Sinal FFT") #titulo do grafico
    plt.ylabel("Amplitude") #nome do eixo y
    plt.xlabel("Frequência (Hz)") #nome do eixo x
    plt.grid(True)
    plt.plot(freq[masc],fft_calc[masc]) #mostra o grafico da fft 
    plt.show()
    
#Função que faz o grafico da IFFT    
def mostrarinv():
    #Número de Pontos de Sinal
    n = int(num.get())
    
    #Período da onda, podemos considerar como se fosse o tempo 
    T = float(taxa.get())
    
    #Frequencia da onda 1
    fr1 = int(f1.get())
    
    #Frequencia da onda 2
    fr2 = int(f2.get())
    
    #Frequencia Angular
    w = 2.0*np.pi/T
    
    #Criando os sinais
    t  = np.linspace(0,T,n) # n números, de 0 a T -> tempo 
    s1 = np.cos(fr1*w*t) #sinal 1
    s2 = np.cos(fr2*w*t)# sinal 2
    
    #Soma dos sinais criados
    s = s1 + s2

    freq = np.fft.fftfreq(n) #base de tempo para frequencia
    masc = freq > 0  #filtra os valores, mostrando só os valores positivos
    
    #Calculo do Sinal
    fft_inversa = np.fft.ifft(s)
    
    plt.figure(1)
    plt.title("Sinal Original")#titulo do grafico
    plt.ylabel("Amplitude") #nome do eixo y
    plt.xlabel("Tempo (s)") #nome do eixo x
    plt.plot(t,s)
    
    #Mostrando o Sinal da FFT invertida 
    plt.figure(2)
    plt.title("Sinal IFFT") #titulo do grafico
    plt.ylabel("Amplitude") #nome do eixo y
    plt.xlabel("Frequência (Hz)") #nome do eixo x
    plt.grid(True)
    plt.plot(fft_inversa[masc],freq[masc])#mostra o grafico da ifft 
    plt.show()    
    
app=Tk()
app.title("Transformada Rápida de Fourier")
app.geometry("300x200")
app.configure(background="#dde")

#Label responsavel pela entrada do numero de pontos
Label(app,text="Nº de Pontos de Sinal", background="#fff", foreground="#009", anchor=W).place(x=10,y=40,width=120,height=20)
num=Entry(app)
num.place(x=150, y=40, width=100, height=20)

#Label responsável pela distancia do eixo x
Label(app,text="Período/Tempo", background="#fff", foreground="#009", anchor=W).place(x=10,y=65,width=120,height=20)
taxa=Entry(app)
taxa.place(x=150, y=65, width=100, height=20)

#Label responsável pela frequencia da onda 1
Label(app,text="Frequência 1", background="#fff", foreground="#009", anchor=W).place(x=10,y=90,width=120,height=20)
f1=Entry(app)
f1.place(x=150, y=90, width=100, height=20)

#Label responsável pela frequencia da onda 2
Label(app,text="Frequência 2", background="#fff", foreground="#009", anchor=W).place(x=10,y=115,width=120,height=20)
f2=Entry(app)
f2.place(x=150, y=115, width=100, height=20)

#Botao para mostrar na tela
Button(app,text="MOSTRAR FFT", command=mostrar).place(x=90,y=150,width=90,height=20)
Button(app,text="MOSTRAR IFFT", command=mostrarinv).place(x=200,y=150,width=90,height=20)
app.mainloop() 

#   Referências:
#   https://www.monolitonimbus.com.br/transformada-de-fourier-em-python/
#   https://www.ritchievink.com/blog/2017/04/23/understanding-the-fourier-transform-by-example/
#   https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html
#   https://docs.python.org/pt-br/3/library/tk.html           


