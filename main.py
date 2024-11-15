from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput


class program(App):
    def __init__(self):
        super().__init__()
        self.roman_true={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        self.roman_false={1:"I",4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        self.converttype=True#якщо тру то з римських в арабські фолс навпаки
        self.text=Label(
            text='',
            size_hint=(0.65,0.1),
            pos_hint={'x':0.15,'y':0.4}
        )
        self.button_type=Button(
            text='Rum>Arab',
            size_hint=(0.1,0.1),
            pos_hint={'x':0.7,'y':0.8}
        )                     
        self.text_input=TextInput(
            text='',
            size_hint=(0.5,0.1),
            pos_hint={'x':0.15,'y':0.8}
        )

    def converte(self,args):
        num=self.text_input.text
        if self.converttype==1:
            num=list(num)
            for i in range(len(num)):
                num[i]=self.roman_true[num[i]]
            for i in range(len(num)-1):
                if abs(num[i])<abs(num[i+1]):num[i]=-num[i]
            ansver=str(sum(num))
        else:
            num=int(num)
            ansver=''
            b=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
            for i in b:
                while num>=i:
                    ansver+=(self.roman_false[i])
                    num-=i
        self.text.text=ansver




    def chage_type(self,args):
        self.converttype = 1 if self.converttype == 0 else 0
        self.button_type.text='Arab>Rum' if self.button_type.text=='Rum>Arab' else 'Rum>Arab'



    def build(self):

        layout=FloatLayout()
        
        button_coverte=Button(
            text='CONVERTE',
            size_hint=(0.65,0.1),
            pos_hint={'x':0.15,'y':0.6}
        
        )
        self.button_type.bind(on_press=self.chage_type)
        


        button_coverte.bind(on_press=self.converte)
        

        layout.add_widget(self.button_type)
        layout.add_widget(button_coverte)
        layout.add_widget(self.text_input)
        layout.add_widget(self.text)
        return(layout)


if __name__=='__main__':
    program().run()
