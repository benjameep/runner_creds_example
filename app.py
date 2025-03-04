import sys
from datetime import datetime
import os

def main():    
    # Print environment variables
    print("OPEN_API_KEY: ", os.environ.get('OPEN_API_KEY'))
    print("SECRET_KEY: ", os.environ.get('SECRET_KEY'))

if __name__ == "__main__":
    main()
