# calcula a tarifa de equilíbrio em função da variação (perda ou ganho) entre dois períodos distintos

# esta versão aprimora a importação do arquivo em Excel BD2.xlsx, ou seja:
# 1- antes os nomes das planilhas não eram automaticos e tinhamos 2 importações de planilhas distintas do
# BD2.xlsx para o Pandas (planilha_1, planilha_2). Utilizamos 2 DataFrames (d_fr1 e d_fr2);
# 2- agora temos somente 1 importação da planilha BD2.xlsx e 1 DataFrame (planilha_BD2 e d_fr), ambos com
# base em pesquisas no Pandas através dos anos digitados (keys) e aos totais (values);
# 3- para auxiliar no código, utilizamos conversões da planilha e do DataFrame para uma lista e um dicionário;
# 4- Arquivo BD2.xlsx com N planilhas separadas por cada ano, contendo dados de km e pax pagantes.


import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import xlsxwriter
from tkinter import *


class CalculaTarifa:
    def __init__(self, ano_atipico, ano_referencia, tarifa_vigente, perda_custo, planilha_BD2, lista_excel):
# variáveis de entrada
        self.ano_atipico = ano_atipico                      # ano da queda de oferta/ demanda de pax
        self.ano_referencia = ano_referencia                # ano de referência relativo à ofeta/ demanda de pax
        self.tarifa_vigente = tarifa_vigente                # tarifa praticada vigente
#        self.perda_custo = np.float64(perda_custo) / 100    # perda pela retirada de veículos da frota de ônibus
        self.perda_custo = float(perda_custo) / 100         # perda pela retirada de veículos da frota de ônibus
        self.planilha_BD2 = planilha_BD2                    # planilha BD2 importada para o Pandas
        self.lista_excel = lista_excel                      # corresponde BD2.xlsx convertido em lista

#        self.df1 = df1                                      # dataFrame referente ao ano atípico
#        self.df2 = df2                                      # dataFrame referente ao ano de referência

# variáveis de saída
        self.total_ano_anterior_km = 0
        self.total_ano_anterior_pax = 0
        self.total_ano_atipico_km = 0
        self.total_ano_atipico_pax = 0
        self.tarifa_equilibrio = 0

# totais do ano atípico e do ano de referência (oferta/ demanda de pax de acordo com o planejamento)
    def soma_excel(self):
        tabelaKM = {}
        tabelaPAX = {}
        for i in range(len(self.lista_excel)):
            d_fr = pd.DataFrame(self.planilha_BD2[self.lista_excel[i]])
            tabelaKM.update({self.lista_excel[i]: d_fr['km coberto'].sum()})
            tabelaPAX.update({self.lista_excel[i]: d_fr['pax pagantes'].sum()})
            if self.ano_atipico == self.lista_excel[i]:
                self.total_ano_atipico_km = tabelaKM[self.lista_excel[i]]
                self.total_ano_atipico_pax = tabelaPAX[self.lista_excel[i]]
            if self.ano_referencia == self.lista_excel[i]:
                self.total_ano_anterior_km = tabelaKM[self.lista_excel[i]]
                self.total_ano_anterior_pax = tabelaPAX[self.lista_excel[i]]

#        self.total_ano_anterior_km = self.df2['km coberto'].sum()
#        self.total_ano_atipico_km = self.df1['km coberto'].sum()
#        self.total_ano_anterior_pax = self.df2['pax pagantes'].sum()
#        self.total_ano_atipico_pax = self.df1['pax pagantes'].sum()

        return self.total_ano_anterior_km, self.total_ano_anterior_pax, self.total_ano_atipico_km, self.total_ano_atipico_pax

# calculo do IPK de pax pagantes do ano de referência (oferta/ demanda de pax de acordo com o planejamento)
    def calcula_ipk_ano_anterior(self):
        return self.total_ano_anterior_pax / self.total_ano_anterior_km

# calculo do IPK de pax pagantes do ano atípico (ano de queda de oferta/ demanda de pax)
    def calcula_ipk_ano_atipico(self):
        return self.total_ano_atipico_pax / self.total_ano_atipico_km

# tarifa calculada em função da queda de oferta/ demanda de pax (manutenção do equilíbrio econômico-financeiro)
    def tarifa_equilibrada(self):
#        custo_atual = np.float64(self.tarifa_vigente) * self.calcula_ipk_ano_anterior()
        custo_atual = float(self.tarifa_vigente) * self.calcula_ipk_ano_anterior()
        custo_novo = custo_atual * (1 - (self.total_ano_atipico_km / self.total_ano_anterior_km * self.perda_custo))
        self.tarifa_equilibrio = custo_novo / self.calcula_ipk_ano_atipico()
        return self.calcula_ipk_ano_anterior(), self.calcula_ipk_ano_atipico(), self.tarifa_equilibrio

# mostrando gráfico de barras, com index modificado
    def mostra_grafico(self):
#        self.geraExcel = pd.DataFrame({'valor': [np.float64(self.tarifa_vigente), np.float64(self.tarifa_equilibrio)]}, index=['T-vig', 'T-eq'])
        self.geraExcel = pd.DataFrame({'valor': [float(self.tarifa_vigente), float(self.tarifa_equilibrio)]},
                                      index=['T-vig', 'T-eq'])
        self.geraExcel['valor'].plot.barh()
        return plt.show()

# gerando arquivo BD3.xlsx com as tarifas vigente e de equilíbrio
    def gera_Excel(self):
        gravaExcel = xlsxwriter.Workbook('BD3.xlsx')
        planilhaUnica = gravaExcel.add_worksheet('Tarifa de equilíbrio')

        monta_celulas = (['T-vig', self.tarifa_vigente], ['T-eq', self.tarifa_equilibrio])
        real = gravaExcel.add_format({'num_format': 'R$ #.##0,0'})
        centro = gravaExcel.add_format()
        centro.set_align('center')
        centro.set_bold()
        row = 0
        col = 0
        planilhaUnica.write(row, col + 1, 'Valores', centro)
        row += 1
        for i, j in monta_celulas:
            planilhaUnica.write(row, col, i, centro)
            planilhaUnica.write(row, col + 1, float(j), real)
            row += 1

        gravaExcel.close()
        return


if __name__ == '__main__':
# salva valores da GUI
    def inicio():
        ano_atip = text_anoAtip.get()
        ano_ref = text_anoRef.get()
        perda_oferta = text_custo.get()
        tarifa_vig = text_tarifaVig.get()
# importacão para o Pandas do arquivo em Excel, com planilhas separadas para cada ano
        planilha_0 = pd.read_excel('BD2.xlsx', None)
        lista_BD2 = list(planilha_0.keys())
        primeiraVez = False
        saida = f' '*75
        label_nada = Label(Janela, text=saida, padx=20).grid(row=7, column=0, stick=W)
# ano(s) digitado(s) fora dos limites no Pandas. Serão corrigidos pelos limites inferior e/ou superior
        if ano_atip > lista_BD2[-1]:
            ano_atip = lista_BD2[-1]
        if ano_ref < lista_BD2[0]:
            ano_ref = lista_BD2[0]
        while ano_atip <= ano_ref:
            if primeiraVez:
                saida = f'Aviso: ano-ref >= ano-atíp. Limites adotados'
                msg_erro = Label(Janela, text=saida, padx=20).grid(row=7, column=0, stick=W)
                ano_atip = lista_BD2[-1]
                ano_ref = lista_BD2[0]

            primeiraVez = True
        else:
            ct = CalculaTarifa(ano_atip, ano_ref, tarifa_vig, perda_oferta, planilha_0, lista_BD2)
            total = ct.soma_excel()
            saida = f''
            label_nada = Label(Janela, text=saida, padx=20).grid(row=8, column=0, stick=W)
            for i in range(0, len(total), 2):
                saida_km = f'KM {ano_atip} = '
                saida_pax = f'PAX {ano_atip} = '
                if i == 0:
                    saida_km = f'KM {ano_ref} = '
                    saida_pax = f'PAX {ano_ref} = '

                saida = f'{saida_km}{total[i]}'
                label_km = Label(Janela, text=saida, padx=20).grid(row=i+9, column=0, stick=W)
                saida = f'{saida_pax}{total[i + 1]}'
                label_pax = Label(Janela, text=saida, padx=20).grid(row=i+10, column=0, stick=W)

            t_eq = ct.tarifa_equilibrada()
            for i in range(len(t_eq)):
                saida_te = f'IPK {ano_atip} = '
                if i == 0:
                    saida_te = f'IPK {ano_ref} = '
                elif i == 2:
                    saida_te = f'TARIFA DE EQUILÍBRIO = '

#                saida = f'{saida_te}{str(round(t_eq[i],3))}'
                saida = f'{saida_te}{t_eq[i]}'
                label_teq = Label(Janela, text=saida, padx=20).grid(row=i+13, column=0, stick=W)

        ct.mostra_grafico()
        ct.gera_Excel()
        return

# ativa biblioteca Tkinter
    Janela = Tk()
    Janela.title(f'Calcula Tarifa de Equilíbrio')
# definir geometry
    largura = 500
    altura = 425
    largura_screen = Janela.winfo_screenwidth()
    altura_screen = Janela.winfo_screenheight()
    posx = (largura_screen - largura) / 2
    posy = (altura_screen - altura) / 2
    Janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
# Labels, grid manager
    label_anoAtip = Label(Janela, text=f'ANO ATÍPICO = ', padx=20, pady=10)
    label_anoRef = Label(Janela, text=f'ANO REFERÊNCIA = ', padx=20, pady=10)
    label_custo = Label(Janela, text=f'DIMINUIÇÃO DE CUSTO OPERACIONAL( %) = ', padx=20, pady=10)
    label_tarifaVig = Label(Janela, text=f'TARIFA VIGENTE = ', padx=20, pady=10)
    saida = f''
    label_nada = Label(Janela, text=saida)
    text_anoAtip = Entry(Janela)
    text_anoRef = Entry(Janela)
    text_custo = Entry(Janela)
    text_tarifaVig = Entry(Janela)
    cmd_Calc = Button(Janela, text=f'Calcular', command=inicio)
    cmd_Fim = Button(Janela, text=f'Fim', command=Janela.quit)
# organizar widgets
    label_anoAtip.grid(row=0, stick=W)
    label_anoRef.grid(row=1, stick=W)
    label_custo.grid(row=2, stick=W)
    label_tarifaVig.grid(row=3, stick=W)
    label_nada.grid(row=4, stick=W)
    text_anoAtip.grid(row=0, column=1)
    text_anoRef.grid(row=1, column=1)
    text_custo.grid(row=2, column=1)
    text_tarifaVig.grid(row=3, column=1)
    cmd_Calc.grid(row=5, column=0, stick=E)
    cmd_Fim.grid(row=5, column=1, stick=E)
# mainLoop()
    Janela.mainloop()
