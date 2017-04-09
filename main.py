from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from pprint import pprint

from index import IndexListGenerator

class Game:
    def __init__(self):
        self.actual_square = actual_square
        self.big_number = big_number
        self.small_number = small_number

class Ctverec(GridLayout):
    '''Vygeneruje ctverec 3x3 s inputy'''
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)

        self.ctverec_plocha = []
        self.cols = 3
        for a in range(9):
            text = ""
            tlacitko = Button(text=text)
            self.add_widget(tlacitko)
            tlacitko.bind(on_press=callback)
            self.ctverec_plocha.append(tlacitko)

            '''
            text_input = TextInput(multiline=False)
            self.add_widget(text_input)
            text_input.bind(text=on_change) #BIND - kdyz se zmeni text, zavola on_change

            self.ctverec_plocha.append(text_input)
            '''


class SudokuScreen(GridLayout):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.spacing = [5]

        self.hraci_pole = []
        #vytvoreni hraci plochy;
        self.cols = 3
        for a in range(9):
            ctverec = Ctverec(callback=callback)
            self.add_widget(ctverec)
            self.hraci_pole.append(ctverec.ctverec_plocha)

class KeybordScreen(GridLayout):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.spacing = [20]
        self.cols = 1
        self.add_widget(KeybordBig(callback=callback))
        self.add_widget(KeybordSmall())

class KeybordBig(GridLayout):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.spacing = [5]
        self.cols = 3
        for a in range(9):
            text = str(a+1)
            tlacitko = Button(text=text)
            self.add_widget(tlacitko)
            tlacitko.bind(on_press=callback)

class KeybordSmall(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = [5]
        self.cols = 3
        for a in range(9):
            text = str(a+1)
            tlacitko = Button(text=text)
            self.add_widget(tlacitko)

class Screen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = [20]
        self.spacing = [20]
        self.sudoku_screen = SudokuScreen(callback=self.callback, size_hint_x=2)
        self.list_index = IndexListGenerator()() # inicializace tridy + zavolani metody __call__()
        self.aktivni_bunka= None

        self.cols = 2
        self.add_widget(self.sudoku_screen)
        self.add_widget(KeybordScreen(callback=self.callback_keyboard, size_hint_x=1))

    def callback(self, instance):
        if self.aktivni_bunka:
            self.aktivni_bunka.background_color = (1,1,1,1)
        instance.background_color = (0.5,0.5,1,1)
        self.aktivni_bunka = instance

    def callback_keyboard(self, instance):
        self.klavesa_big = instance.text
        self.vyhodnoceni()


    def vyhodnoceni(self):
        self.aktivni_bunka.text = self.klavesa_big
        #self.aktivni_bunka.background_color = (1,1,1,1)

        self.vytiskni()

        #prebarveni vsech policek na bilo:
        for ctverec in self.sudoku_screen.hraci_pole:
            for ctverecek in ctverec:
                ctverecek.background_color = (1,1,1,1)

        #vybarveni spatnych policek:
        for jeden_radek in self.list_index: # pro kontrolu radku, sloupcu a ctvercu
            seznam_cisel = []
            #vytvoreni kontrolniho seznamu
            for prvek in jeden_radek:
                ctverecek = self.sudoku_screen.hraci_pole[prvek[0]][prvek[1]]
                try:
                    seznam_cisel.append(int(ctverecek.text))
                except ValueError:
                    pass
            print(seznam_cisel)
            #srovnavani s kontrolnim seznamem a pribarvovani policek
            for index, prvek in enumerate(jeden_radek):
                print(index, prvek)
                ctverecek = self.sudoku_screen.hraci_pole[prvek[0]][prvek[1]]
                try:
                    int(ctverecek.text)
                except ValueError:
                    pass
                else:
                    print(int(ctverecek.text), 'in', seznam_cisel[:index] + seznam_cisel[index+1:])

                    if int(ctverecek.text) in (seznam_cisel[:index] + seznam_cisel[index+1:]):
                        if ctverecek:
                            ctverecek.background_color = (1,0,0,1)


    def vytiskni(self):
        for ctverec in self.sudoku_screen.hraci_pole:
            for bunka in ctverec:
                print(bunka.text, end=' ')
            print()

class SudokuApp(App):
    def build(self):
        return Screen()


if __name__ == '__main__':
    SudokuApp().run()
