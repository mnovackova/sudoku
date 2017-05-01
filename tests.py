import sys
import pytest

sys.argv = ['.']
from main import Screen

class TestVyhodnoceni:
    def inicializace_tridy(self):
        screen = Screen()
        #vymazani hraciho pole:
        for a in screen.sudoku_screen.hraci_pole:
            for ctverecek in a:
                ctverecek.text = ''
        return screen

    def test_kolize_ctverec(self):
        screen = self.inicializace_tridy()

        prvni_policko = screen.sudoku_screen.hraci_pole[0][0]
        prvni_policko.text = '1'
        druhe_policko = screen.sudoku_screen.hraci_pole[0][4]
        druhe_policko.text = '1'
        treti_policko = screen.sudoku_screen.hraci_pole[8][8]

        screen.vyhodnoceni()
        assert prvni_policko.background_color == [1,0,0,1]
        assert druhe_policko.background_color == [1,0,0,1]
        assert treti_policko.background_color == [1,1,1,1]

    def test_kolize_radek(self):
        screen = self.inicializace_tridy()

        prvni_policko = screen.sudoku_screen.hraci_pole[0][0]
        prvni_policko.text = '1'
        druhe_policko = screen.sudoku_screen.hraci_pole[1][0]
        druhe_policko.text = '1'
        treti_policko = screen.sudoku_screen.hraci_pole[0][2]

        screen.vyhodnoceni()
        assert prvni_policko.background_color == [1,0,0,1]
        assert druhe_policko.background_color == [1,0,0,1]
        assert treti_policko.background_color == [1,1,1,1]

    def test_kolize_sloupec(self):
        screen = self.inicializace_tridy()

        prvni_policko = screen.sudoku_screen.hraci_pole[0][0]
        prvni_policko.text = '1'
        druhe_policko = screen.sudoku_screen.hraci_pole[3][0]
        druhe_policko.text = '1'
        treti_policko = screen.sudoku_screen.hraci_pole[0][2]

        screen.vyhodnoceni()
        assert prvni_policko.background_color == [1,0,0,1]
        assert druhe_policko.background_color == [1,0,0,1]
        assert treti_policko.background_color == [1,1,1,1]

    def test_complete(self):
        pass
