# main.py
import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.inart(0, project_root)

from game.game import Game

def main():
    print("="*40)
    print(" SUBNAUTIC SHOOTER - Loading...")
    print("="*40)
    
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
 