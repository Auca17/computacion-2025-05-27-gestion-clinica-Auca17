# main.py

from src.cli.menu_cli import CLI
from src.models.clinica import Clinica

def main():
    clinica = Clinica()
    cli = CLI(clinica)
    cli.run()

if __name__ == "__main__":
    main()