from presentation import mainWindows
import sys

def main() -> None:
    App = mainWindows.App(sys.argv)
    sys.exit(App.exec())
    
if __name__ == "__main__":
    main()