from pprint import pprint

class IndexListGenerator:
    def __call__(self):
        return self.row_list_generator() + self.column_list_generator() + self.square_list_generator()

    def row_list_generator(self):
        index1 = []
        #[0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8, 6, 6, 6, 7, 7, 7, 8, 8, 8]
        for cislo in range(0,9,3):
            for pocet_opakovani in range(3):
                for i in range(3):
                    index1.append(cislo)
                for i in range(3):
                    index1.append(cislo+1)
                for i in range(3):
                    index1.append(cislo+2)

        index2 = []
        #[0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 6, 7, 8, 6, 7, 8, 6, 7, 8, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 6, 7, 8, 6, 7, 8, 6, 7, 8, 0, 1, 2, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5, 6, 7, 8, 6, 7, 8, 6, 7, 8]
        for pocet_opakovani in range(3):
            for cislo in range(0,9,3):
                for i in range(3):
                    index2.append(cislo)
                    index2.append(cislo+1)
                    index2.append(cislo+2)

        row_index = list(zip(index1, index2))
        row_index_list = []
        for a in range(0,73,9):
            row_index_list.append(row_index[a:a+9])
        return row_index_list
        #pprint(row_index_list)

    def column_list_generator(self):
        index3 = []
        #[0, 0, 0, 3, 3, 3, 6, 6, 6, 0, 0, 0, 3, 3, 3, 6, 6, 6, 0, 0, 0, 3, 3, 3, 6, 6, 6, 1, 1, 1, 4, 4, 4, 7, 7, 7, 1, 1, 1, 4, 4, 4, 7, 7, 7, 1, 1, 1, 4, 4, 4, 7, 7, 7, 2, 2, 2, 5, 5, 5, 8, 8, 8, 2, 2, 2, 5, 5, 5, 8, 8, 8, 2, 2, 2, 5, 5, 5, 8, 8, 8]
        for cislo in range(3):
            for pocet_opakovani in range(3):
                for i in range(3):
                    index3.append(cislo)
                for i in range(3):
                    index3.append(cislo+3)
                for i in range(3):
                    index3.append(cislo+6)

        index4 = []
        #[0, 3, 6, 0, 3, 6, 0, 3, 6, 1, 4, 7, 1, 4, 7, 1, 4, 7, 2, 5, 8, 2, 5, 8, 2, 5, 8, 0, 3, 6, 0, 3, 6, 0, 3, 6, 1, 4, 7, 1, 4, 7, 1, 4, 7, 2, 5, 8, 2, 5, 8, 2, 5, 8, 0, 3, 6, 0, 3, 6, 0, 3, 6, 1, 4, 7, 1, 4, 7, 1, 4, 7, 2, 5, 8, 2, 5, 8, 2, 5, 8]
        for pocet_opakovani in range(3):
            for cislo in range(3):
                for i in range(3):
                    index4.append(cislo)
                    index4.append(cislo+3)
                    index4.append(cislo+6)

        column_index = list(zip(index3, index4))
        column_index_list = []
        for a in range(0,73,9):
            column_index_list.append(column_index[a:a+9])
        return column_index_list
        #pprint(column_index_list)

    def square_list_generator(self):
        square_index = []
        #[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]
        for index1 in range(9):
             for index2 in range(9):
                 square_index.append((index1, index2))
        square_index_list = []
        for a in range(0,73,9):
            square_index_list.append(square_index[a:a+9])
        return square_index_list
