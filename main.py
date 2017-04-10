from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

from pprint import pprint

from index import IndexListGenerator

class Game:
    def __init__(self):
        self.actual_square = actual_square
        self.big_number = big_number
        self.small_number = small_number

class Tlacitko(Button):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 25
        
        self.rect_color = None
        self.bind(on_press=callback)
        self.set_background(0,0,0,0)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def set_background(self, r, g, b, a):
        with self.canvas.before:
            if not self.rect_color:
                self.rect_color = Color(r * 255, g * 255, b * 255, a)
                self.rect = Rectangle(size=self.size, pos=self.pos)
            else:
                self.rect_color.r = r * 255
                self.rect_color.g = g * 255
                self.rect_color.b = b * 255
                self.rect_color.a = a

    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size


class Ctverec(GridLayout):
    '''Vygeneruje ctverec 3x3 s inputy'''
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.ctverec_plocha = []
        self.spacing = [5]

        self.cols = 3
        for a in range(9):
            tlacitko = Tlacitko(callback=callback)
            self.add_widget(tlacitko)
            self.ctverec_plocha.append(tlacitko)

class SudokuScreen(GridLayout):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.spacing = [8]

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
            tlacitko = Button(text=text, font_size=25)
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
        #zruseni ramecku kolem tlacitka
        if self.aktivni_bunka and self.aktivni_bunka.background_color != (1,0,0,1):
            self.aktivni_bunka.set_background(0,0,0,0)
        instance.set_background(0,0,1,1)
        self.aktivni_bunka = instance

    def callback_keyboard(self, instance):
        self.klavesa_big = instance.text
        self.vyhodnoceni()


    def vyhodnoceni(self):
        self.aktivni_bunka.text = self.klavesa_big


        #self.vytiskni()

        #prebarveni vsech policek na bilo:
        for ctverec in self.sudoku_screen.hraci_pole:
            for ctverecek in ctverec:
                ctverecek.background_color = (1,1,1,1)

        # prochazeni jednotlivych radku seznamu pro kontrolu shody cisel v radku, sloupci ci ctverci
        for seznam_indexu in self.list_index:
            seznam_cisel = []
            for index in seznam_indexu:
                ctverecek = self.sudoku_screen.hraci_pole[index[0]][index[1]]
                try:
                    ctverecek_number = int(ctverecek.text)
                except ValueError:
                    seznam_cisel.append("")
                else:
                    seznam_cisel.append(ctverecek_number)
            print(seznam_cisel)

            #srovnavani s kontrolnim seznamem(seznam_cisel) a pribarvovani policek
            for poradi, index in enumerate(seznam_indexu):
                ctverecek = self.sudoku_screen.hraci_pole[index[0]][index[1]]
                try:
                    ctverecek_number = int(ctverecek.text)
                except ValueError:
                    pass
                else:
                    if ctverecek_number in (seznam_cisel[:poradi] + seznam_cisel[poradi+1:]):
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
