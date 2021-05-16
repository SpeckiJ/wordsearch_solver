import csv
import argparse
from termcolor import colored

class Puzzle:
    def __init__(self, args):
        self.puzzle = self.parse_puzzle(args.puzzle)
        self.words = self.parse_words(args.words)
        self.solved = []

    def parse_puzzle(self, puzzle_name):
        puzzle = []
        with open(puzzle_name, 'r') as pfile:
            p_reader = csv.reader(pfile)
            for p_row in p_reader:
                puzzle.append(p_row)
        
        return puzzle
    
    def parse_words(self, list_name):
        words = []
        with open(list_name, 'r') as cfile:
            c_reader = csv.reader(cfile)
            for c_row in c_reader:
                words.append(str(c_row[0]).replace(' ', ''))
        
        return words

    def find_word(self):
        for word in self.words:
            #self.find_horizontal(word)
            #self.find_vertical(word)
            self.find_diagonal(word)

    def find_horizontal(self, word):
        for ri, row in enumerate(self.puzzle):
            if word in str(row):
                for i in range(0, len(word)):
                    self.solved.append((ri, str(row).find(word)- 2 + i))
                return True
            row_r = str(row)[::-1]
            if word in row_r:
                print(word)
                for i in range(0, len(word)):
                    self.solved.append((ri, len(row_r) - str(row_r).find(word) -3 - i))
                return True
        return False

    def find_vertical(self, word):
        for char in range(len(self.puzzle[0][0])):
            temp = []
            for col in range(len(self.puzzle)):
                temp.append(self.puzzle[col][0][char])
            temp = ''.join(temp)
            temp_r = temp[::-1]
            if word in str(temp):
                for i in range(0, len(word)):
                    self.solved.append((str(temp).find(word) + i, char))
                return True
            if word in str(temp_r):
                for i in range(0, len(word)):
                    self.solved.append((len(temp_r) - str(temp_r).find(word) -1 - i, char))
                return True
        return False

    def find_diagonal(self, word):
        for a in range(0, len(self.puzzle[0][0])):
            temp = []
            i = 0
            while ((a - i) >= 0) and (i < len(self.puzzle)):
                temp.append(self.puzzle[i][0][a-i])
                i+=1
            temp = ''.join(temp)
            temp_r = temp[::-1]
            print(temp)
            
        return False
            


    def output_cli(self):
        for ri, row in enumerate(self.puzzle):
            for chi, ch in enumerate(row[0]):
                if (ri, chi) in self.solved:
                    print(colored(f"{ch}", "red"),end=" ")
                else:
                    print(colored(f"{ch}", "blue"),end=" ")
            print()

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--puzzle', help='puzzle file location')
    parser.add_argument('--words', help='words file location')

    args = parser.parse_args()
    p = Puzzle(args)
    
    p.find_word()
    p.output_cli()

