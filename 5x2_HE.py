from http.client import HTTPException


class HoraExtra():
    def __init__(self,hrs_extra_50,hrs_extra_100):
        self.hrs_extra_50 = int(hrs_extra_50)
        self.hrs_extra_100 = float(hrs_extra_100)

    def calculo220horas (self,hora_50=0, hora_100 =0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_50 < 0 or self.hrs_extra_100 < 0:
            raise HTTPException(status_code =400, detail="Erro: Informe uma quantidade válida de horas extras.")


        vrl_hrs_salario= SalarioMinimo/ 220

        if self.hrs_extra_50 > 0 and self.hrs_extra_100 > 0:
            qty_hrs_extra = float(self.hrs_extra_50)
            qty_hrs_extra = float(self.hrs_extra_100)
            resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra) + (vrl_hrs_salario * 2 * qty_hrs_extra)
            return resultado


        elif self.hrs_extra_50 > 0 :
            qty_hrs_extra = float(self.hrs_extra_50)
            resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
            return resultado


        elif self.hrs_extra_100 > 0 :
            qty_hrs_extra = float(self.hrs_extra_100)
            resultado = (vrl_hrs_salario * 2 * qty_hrs_extra)
            return resultado

        else:
            raise HTTPException(status_code= 400, detail = "Erro: Iforme a quantidade válida.")






    def calculo200horas (self,hora_50=0, hora_100 =0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_50 < 0 or self.hrs_extra_100 < 0:
            raise HTTPException(status_code =400, detail="Erro: Informe uma quantidade válida de horas extras.")


        vrl_hrs_salario= SalarioMinimo/ 200

        if self.hrs_extra_50 > 0 and self.hrs_extra_100 > 0:
            qty_hrs_extra = float(self.hrs_extra_50)
            qty_hrs_extra = float(self.hrs_extra_100)
            resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra) + (vrl_hrs_salario * 2 * qty_hrs_extra)
            return resultado


        elif self.hrs_extra_50 > 0 :
            qty_hrs_extra = float(self.hrs_extra_50)
            resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
            return resultado


        elif self.hrs_extra_100 > 0 :
            qty_hrs_extra = float(self.hrs_extra_100)
            resultado = (vrl_hrs_salario * 2 * qty_hrs_extra)
            return resultado

        else:
            raise HTTPException(status_code= 400, detail = "Erro: Iforme a quantidade válida.")

    def calculo220horas(self, hora_50=0, hora_100=0):
        SalarioMinimo = 1620.00
        if self.hrs_extra_50 < 0 or self.hrs_extra_100 < 0:
            raise HTTPException(status_code=400, detail="Erro: Informe uma quantidade válida de horas extras.")

        vrl_hrs_salario = SalarioMinimo / 220

        if self.hrs_extra_50 > 0 and self.hrs_extra_100 > 0:
            qty_hrs_extra = float(self.hrs_extra_50)
            qty_hrs_extra = float(self.hrs_extra_100)
            resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra) + (vrl_hrs_salario * 2 * qty_hrs_extra)
            return resultado


        elif self.hrs_extra_50 > 0:
            qty_hrs_extra = float(self.hrs_extra_50)
            resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
            return resultado


        elif self.hrs_extra_100 > 0:
            qty_hrs_extra = float(self.hrs_extra_100)
            resultado = (vrl_hrs_salario * 2 * qty_hrs_extra)
            return resultado

        else:
            raise HTTPException(status_code=400, detail="Erro: Iforme a quantidade válida.")


he = HoraExtra(10, 10 )
he.calculo220horas(10,10)
he.calculo210horas(10,10)
he.calculo200horas(10,10)

print(f" Horas extra de 50% com total de 44 horas semanais R$ {he.calculo220horas():.2f}")
print(f" Horas extra de 50% com total de 42 horas semanais R$ {he.calculo210horas():.2f}")
print(f" Horas extra de 50% com total de 40 horas semanais R$ {he.calculo200horas():.2f}")