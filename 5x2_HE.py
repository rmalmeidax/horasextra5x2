from http.client import HTTPException


class HoraExtra():
    def __init__(self,hrs_extra_50,hrs_extra_100):
        self.hrs_extra_50 = float(hrs_extra_50)
        self.hrs_extra_100 = float(hrs_extra_100)

    def calculo220 (self):
        if not self.hrs_extra_50:
            raise HTTPException("Erro: Informe uma quantidade válida de horas extras.")
        SalarioMinimo = 1620.00
        vrl_hrs_salario= SalarioMinimo/ 220
        qty_hrs_extra = float(self.hrs_extra_50)
        resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
        return resultado

    def calculo210 (self):
        if not self.hrs_extra_50:
            raise HTTPException("Erro: Informe uma quantidade válida de horas extras.")
        SalarioMinimo = 1620.00
        vrl_hrs_salario = SalarioMinimo/ 210
        qty_hrs_extra= float(self.hrs_extra_50)
        resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
        return resultado

    def calculo200 (self):
        if not self.hrs_extra_50:
            raise HTTPException("Erro:Informe quantidade válida por hora")
        salario_minimo = float(1620.00)
        vrl_hrs_salario = salario_minimo/ 200
        qty_hrs_extra = float(self.hrs_extra_50)
        resultado = (vrl_hrs_salario * 1.50 * qty_hrs_extra)
        return resultado


he = HoraExtra(10, 8 )
print(f" Horas extra de 50% com total de 44 horas semanais R$ {he.calculo220():.2f}")
print(f" Horas extra de 50% com total de 42 horas semanais R$ {he.calculo210():.2f}")
print(f" Horas extra de 50% com total de 40 horas semanais R$ {he.calculo200():.2f}")