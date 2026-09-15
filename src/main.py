import sys
from utility import AppRunner

def main():
    app = AppRunner()
    
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n\nApp interrupted by user. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()