import game.action as action
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    
    # Start game or load from slot if provided
    if len(argv) > 2 and argv[1] == "save" and argv[2]:
        action.load_game(argv[2])
    else:
        action.start_game()




if __name__ == "__main__":
    main()