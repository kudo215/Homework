# Programming Morse Code

class MorseCodeDictionary:
    
    def main():
        # International morse code dictionary
        myDict = {
            # Punctuation
            ' ' : ' ',
            ',' : '--..--',
            '.' : '..--..',
            # Numbers
            '0' : '-----',
            '1' : '.----',
            '2' : '..---',
            '3' : '...--',
            '4' : '....-',
            '5' : '.....',
            '6' : '-....',
            '7' : '--...',
            '8' : '---..',
            '9' : '----.',
            # Letters
            'A' : '.-',
            'B' : '-...',
            'C' : '-.-.',
            'D' : '-..',
            'E' : '.',
            'F' : '..-.',
            'G' : '--.',
            'H' : '....',
            'I' : '..',
            'J' : '.---',
            'K' : '-.-',
            'L' : '.-..',
            'M' : '--',
            'N' : '-.',
            'O' : '---',
            'P' : '.--.',
            'Q' : '--.-',
            'R' : '.-.',
            'S' : '...',
            'T' : '-',
            'U' : '..-',
            'V' : '...-',
            'W' : '.--',
            'X' : '-..-',
            'Y' : '-.-',
            'Z' : '--..'
        }
        morse = ""
        for ch in sentence:
            morse += myDict[ch.upper()]
        return morse
        sentence = input("Enter sentence: ")

        print(main[sentence])
