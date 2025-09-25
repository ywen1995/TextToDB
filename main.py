from google import genai
from google.genai import Client
import os

from text_to_sql import TextToSql

def text_to_db():
    """
    Placeholder for the database connection and interaction functionality.
    Phase 2 TODO: Implement database connection and interaction logic
    """
    print("\n--- Database Connection ---")
    print("This functionality is not yet implemented.")
    pass


def handle_input():
    """
    Handles the main menu and user input.
    Returns 'exit' to terminate the main loop.
    """
    print("\n--- Main Menu ---")
    print("(1) SQL Generation")
    print("(2) Database Connection")
    print("(3) Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        sql_generator = TextToSql()
        sql_generator.run()
    elif choice == '2':
        text_to_db()
    elif choice == '3':
        return 'exit'
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    return None


def main():
    """
    Main server loop. Keeps looping until handle_input() returns 'exit'.
    """
    
    # Basic client configuration
    # configure_genai_client()

    print("Welcome to the Text-to-DB!")
    while True:
        if handle_input() == 'exit':
            print("Exiting Text-to-DB. Have a good day!")
            break


if __name__ == "__main__":
    main()
    pass