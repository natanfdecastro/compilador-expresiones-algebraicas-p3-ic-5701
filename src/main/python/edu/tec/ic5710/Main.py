import sys


from src.main.python.edu.tec.ic5710.LexicalAnalyser import Scanner
from src.main.python.edu.tec.ic5710.SyntaxAnalyser import SintaxAnalyser
from src.main.python.edu.tec.ic5710.configuration import NEW_PATH

def print_program(program):
    count = 1
    lines = program.split("\n")
    print("\nPROGRAM INPUT:")
    for line in lines:
        print(str(count) + ": " + line)
        count+=1

# Comando de ejecucion: python3 Main.py <programa.txt>

# Concatena la carpeta resources al path nuevo, esto para que apunte a una nueva carpeta
# Editar la ruta según computadora que se ejecuta
file = open(NEW_PATH + sys.argv[1], 'r')
program = file.read()
file.close()

# Imprime el programa ingresado.
print_program(program)

scanner = Scanner(program)
scanner.create_lexical_analysis_report()
parser = SintaxAnalyser(scanner.founded_tokens)
