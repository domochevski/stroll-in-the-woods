import game/action as action

if __name__ == "__main__":
    main()

def main(sys.argv = None):
    if sys.argv[1] == "save" and sys.argv[2]:
        action.start_game(sys.argv[2])
    else:
        action.start_game()