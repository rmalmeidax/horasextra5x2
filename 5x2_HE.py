from http.client import HTTPException


class HoraExtra():
    def __init__(self,hrs_extra_50,hrs_extra_100):
        self.hrs_extra_50 = int(hrs_extra_50)
        self.hrs_extra_100 = float(hrs_extra_100)

########################################################################################################################
    #Calculo de horas 50%  ##220
    def calculo220horas (self,hora_50=0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_50 < 0:
            raise HTTPException(status_code =400, detail="Erro: Informe uma quantidade válida de horas extras.")
        vrl_hrs_salario= SalarioMinimo/ 220
        if self.hrs_extra_50 > 0 :
            qty_hrs_extra = float(self.hrs_extra_50)
            total_50 = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
            return total_50
        else:
            raise HTTPException(status_code= 400, detail = "Erro: Iforme a quantidade válida.")
########################################################################################################################
    #Calculo de horas 100%     ##220
    def calculo220_100(self,hora_110 =0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_100 < 0:
            raise HTTPException(status_code=400, detail = "Erro: Informe a quantidade válida.")
        vrl_hrs_salario = SalarioMinimo/220
        if self.hrs_extra_100 >0:
            qty_hrs_extra = float(self.hrs_extra_100)
            total_100 =(vrl_hrs_salario * 2 * qty_hrs_extra)
            return total_100
        else:
            raise HTTPException(status_code = 400, details = "Erro: Informe a quantidade válida.")

########################################################################################################################
  # Calculo de hora 50 ##210
    def calculo210horas (self,hora_50=0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_50 < 0 :
            raise HTTPException(status_code =400, detail="Erro: Informe uma quantidade válida de horas extras.")

        vrl_hrs_salario= SalarioMinimo/ 210

        if self.hrs_extra_50 > 0:
            qty_hrs_extra = float(self.hrs_extra_50)
            total_50 = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
            return total_50
        else:
            raise HTTPException(status_code = 400, detail = "Informe a quantidade válida.")


 ############################################################################################################################
#  calculo de hora 100 ##210
    def calculo210_100(self, hora_100 =0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_100 < 0:
            raise HTTPException(status_code = 400, detail ="Erro: Informe uma quantidade válida de horas extra")
        vrl_hrs_salario = SalarioMinimo / 210
        if self.hrs_extra_100 > 0 :
            qty_hrs_extra = float(self.hrs_extra_100)
            total_100 = (vrl_hrs_salario * 2 * qty_hrs_extra)
            return total_100
        else:
            raise HTTPException(status_code= 400, detail = "Erro: Informe a quantidade válida.")
# ########################################################################################################################
# Calculo de hora 50 ##200

    def calculo200horas(self, hora_50=0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_50 < 0:
            raise HTTPException(status_code=400, detail="Erro: Informe uma quantidade válida de horas extras.")

        vrl_hrs_salario = SalarioMinimo / 200

        if self.hrs_extra_50 > 0:
            qty_hrs_extra = float(self.hrs_extra_50)
            total_50 = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
            return total_50
        else:
            raise HTTPException(status_code=400, detail="Erro: Informe a quantidade válida.")
#########################################################################################################################

# Calculo de hora 100 ## 200from

    def calculo200_100(self, hora_100 =0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_100 <0:
            raise HTTPException(statuas_code =400, detail = "Erro. Informe uma quantidade válida de horas extra")
        vlr_hrs_salario = SalarioMinimo /200

        if self.hrs_extra_100 >0:
            qty_hrs_extra = float(self.hrs_extra_100)
            total_100= (vlr_hrs_salario * 2 * qty_hrs_extra)
            return total_100
        else:
            raise HTTPException(status_code = 400, detail = "Informe a quantidade valida.")


########################################################################################################################


he = HoraExtra(10, 10 )
he.calculo220horas(20)
he.calculo220_100(20)
he.calculo220horas(30)
he.calculo210_100(30)

print(f" Horas extra de 50% com total de 44 horas semanais R$ {he.calculo220horas():.2f}")
print(f" Horas extra de 50% com total de 42 horas semanais R$ {he.calculo210horas():.2f}")
# print(f" Horas extra de 50% com total de 40 horas semanais R$ {he.calculo200horas(200,0):.2f}")

print(f" Horas extra de 100% com total de 44 horas semanais R$ {he.calculo220_100():.2f}")
print(f" Horas extra de 100% com total de 42 horas semanais R$ {he.calculo210_100():.2f}")
# print(f" Horas extra de 100% com total de 40 horas semanais R$ {he.calculo200horas(0,200):.2f}")