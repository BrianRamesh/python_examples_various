class person_bmi:
    def __init__(self,x=1.75,y=73):
        self.heigth=x
        self.weigth=y

    def bmi(self):
        bmi_temp = self.weigth/(self.heigth*self.heigth)
        return round(bmi_temp,2)

#first enter heigth in brackets then weigth
def bmi_category(my_bmi):
    if(my_bmi<18.5):
        return 'Underweight'
    elif(my_bmi>=18.8 and my_bmi<24.9):
        return 'Normal or Healthy weight'
    elif (my_bmi >= 25.0 and my_bmi < 29.9):
        return 'Overweight'
    else:
        return ('obese')
#just for brian used unpacking method
briandata=[1.74,72]
brian=person_bmi(*briandata)

nicos=person_bmi(1.82,65)
simos=person_bmi(1.78,61)
jean = person_bmi(1.67,51)

family_bmi = [brian.bmi(), nicos.bmi(),simos.bmi(),jean.bmi()]
print(family_bmi)

#mapping
family_bmi_category= list(map(bmi_category,family_bmi))
print(family_bmi_category)


