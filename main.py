from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition


class program(App):
    def __init__(self):
        super().__init__()
        self.main_screen=Screen(name='main')
        self.info_screen=Screen(name='info')
        self.sm=ScreenManager(transition=SlideTransition())
        self.roman_true={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        self.roman_false={1:"I",4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        self.converttype=True#якщо тру то з римських в арабські фолс навпаки
        self.text=Label(
            text='',
            size_hint=(0.65,0.1),
            pos_hint={'x':0.15,'y':0.4},
            font_size=(30)
        )
        self.layout_main=FloatLayout()
        self.layout_info=FloatLayout()
        self.button_type=Button(
            text='Rum>Arab',
            size_hint=(0.1,0.1),
            pos_hint={'x':0.7,'y':0.8}
        )
        self.button_type.bind(on_press=self.chage_type)

        self.Button_info=Button(
            text='Інформація',
            size_hint=(0.1,0.1),
            pos_hint={'x':0.8,'y':0.2}
        )
        self.Button_info.bind(on_press=lambda x: self.change_screen(self.sm,'info','left'))

        self.Button_back=Button(
            text='назад',
            size_hint=(0.1,0.1),
            pos_hint={'x':0.8,'y':0.2}
        )
        self.Button_back.bind(on_press=lambda x: (self.change_screen(self.sm,'main','right')))

        self.text_input=TextInput(
            text='',
            size_hint=(0.5,0.1),
            pos_hint={'x':0.15,'y':0.8},
            font_size=(30)
        )
        

    def converte(self,args):
        num=self.text_input.text
        t=0
        if self.converttype==1:
            for i in range(len(num)):
                if num[i] not in ['I','V','L','M','C','D','X']:t=1
            if t==0:
                num=list(num)
                for i in range(len(num)):
                    num[i]=self.roman_true[num[i]]
                for i in range(len(num)-1):
                    if abs(num[i])<abs(num[i+1]):num[i]=-num[i]
                ansver=str(sum(num))
            else:ansver='Введено некоректні дані'
        else:
            for i in range(len(num)):
                if num[i] not in [0,1,2,3,4,5,6,7,8,9]:t=1
            if t==0:
                num=int(num)
                ansver=''
                b=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
                for i in b:
                    while num>=i:
                        ansver+=(self.roman_false[i])
                        num-=i
            else:ansver='Введено некоректні дані'
        self.text.text=ansver




    def chage_type(self,args):
        self.converttype = 1 if self.converttype == 0 else 0
        self.button_type.text='Arab>Rum' if self.button_type.text=='Rum>Arab' else 'Rum>Arab'

    def change_screen(self, screen_manager, screen_name, direction):
        screen_manager.transition.direction = direction
        screen_manager.current = screen_name



    def build(self):

        
        
        button_coverte=Button(
            text='CONVERTE',
            size_hint=(0.65,0.1),
            pos_hint={'x':0.15,'y':0.6}
        

        )
        button_coverte.bind(on_press=self.converte)

        label_info=Label(
            text=' Прграма створена Кошинським Станіславом \n Програма конвертує арабське число в римське і навпаки\n Як користуватися: \n 1)Обираєш режим роботи (арабські в римські чи навпаки) \n 2)Вводиш своє число \n 3) натискаєш на кнопку converte \n Дякую що переглянули мою програму!!!',
            size_hint=(0.7,0.3),
            pos_hint={'x':0.15,'y':0.6},
            font_size=(30)
        )



        
        


        


        
        




        self.layout_main.add_widget(self.button_type)
        self.layout_main.add_widget(button_coverte)
        self.layout_main.add_widget(self.text_input)
        self.layout_main.add_widget(self.text)
        self.layout_main.add_widget(self.Button_info)

        
        self.layout_info.add_widget(label_info)
        self.layout_info.add_widget(self.Button_back)


        self.main_screen.add_widget(self.layout_main)
        
        self.info_screen.add_widget(self.layout_info)
        

        self.sm.add_widget(self.main_screen)
        
        self.sm.add_widget(self.info_screen)

        return self.sm


if __name__=='__main__':
    program().run()
