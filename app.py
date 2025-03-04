import sys
from datetime import datetime
import os

def main():    
    # Print environment variables
    print("OPEN_AI_KEY: ", os.environ.get('OPEN_AI_KEY'))
    print("MY_SECRET: ", os.environ.get('MY_SECRET'))

if __name__ == "__main__":
    main()
