from google import genai
from google.genai import Client
import os

# TODO: move model configuration to separarte Class, and make model selectable.
DEFAULT_MODEL = "gemini-2.5-flash"

def text_to_sql():
    """
    Handles the natural language to SQL generation functionality.
    Prompts the user for a natural language description of the desired SQL query,
    sends it to the generative AI model, and prints the response.
    """
    print("\n--- SQL Generation ---")
    user_input = input("Enter a description of the SQL you want to generate: ")

    if not user_input:
        print("No input provided. Returning to main menu.")
        return

    try:
        client = Client()

        # TODO: craft proper system prompt and save into a separate file
        # TODO phase 2: Defend against SQL injection
        prompt = f"Generate a SQL query based on the following description: {user_input}"
        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt
        )
        
        # Clean up the response to only show the SQL
        sql_response = response.text.strip()
        if sql_response.lower().startswith("```sql"):
            sql_response = sql_response[6:]
        if sql_response.endswith("```"):
            sql_response = sql_response[:-3]
            
        print("\nGenerated SQL:")
        print(sql_response.strip())

    except Exception as e:
        print(f"\nAn error occurred while generating SQL: {e}")

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
        text_to_sql()
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
