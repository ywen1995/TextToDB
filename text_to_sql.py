import logging as log
import os

from google.genai import Client

# TODO
# 1. Make model selectable.
# 2. implement interative mode with question loop.
# 3. implement few shots and evaluation.

class TextToSql:
    """
    Handles the natural language to SQL generation functionality.
    """
    DEFAULT_MODEL = "gemini-2.5-flash"
    SYS_PROMPT_PG_PATH = "system_prompts/system_pg_generation.md"
    SYS_PROMPT_PG_ITERATIVE_PATH = "system_prompts/sp_pg_generation_iterative.md"
    SYS_PROMPT_EVAL_PATH = "system_prompts/sp_pg_evaluation.md"
    DEFAULT_SYS_PROMPT = "You are an experienced PostgreSQL database administrator. Generate accurate SQL queries based on user input."

    def __init__(self):
        """
        Initializes the TextToSql class, setting up the generative AI client.
        """
        self.client = Client()
        self.model = self.DEFAULT_MODEL
        try:
            with open("system_prompts/sp_pg_generation.md", 'r') as f:
                self.system_prompt = f.read()
        
        except Exception as e:
            log.warning(f"WARNING: reading system prompt: {e}")
            self.system_prompt = self.DEFAULT_SYS_PROMPT

    def generate_sql(self, user_prompt: str) -> str:
        """
        Generates SQL from a user prompt.

        Args:
            user_prompt: The natural language description of the SQL query.

        Returns:
            The generated SQL string, or an error message.
        """
        try:
            # TODO: The following format looks good but google genai is not working well. Test later.
            # TODO: defind againt injection.

            # contents = """
            # [
            #     {"role": "system", "content": [{"text": self.system_prompt}]},
            #     {"role": "user", "content": [{"text": user_prompt}]}
            # ]
            # """

            # in-place replacement prompt
            content = f"{self.system_prompt}\n\n## User Input\n{user_prompt}\n\n## SQL Query"

            response = self.client.models.generate_content(
                model=self.model,
                contents=content
            )

            sql_response = response.text.strip()
            if sql_response.lower().startswith("```sql"):
                sql_response = sql_response[6:]
            if sql_response.endswith("```"):
                sql_response = sql_response[:-3]
            
            return sql_response.strip()

        except Exception as e:
            return f"\nAn error occurred while generating SQL: {e}"

    def run(self):
        """
        Prompts the user for a natural language description, generates the SQL,
        and prints the response.
        """
        print("\n--- SQL Generation ---")
        user_input = input("Enter a description of the SQL you want to generate: ")

        if not user_input:
            print("No input provided. Returning to main menu.")
            return

        sql_response = self.generate_sql(user_input)
            
        print("\nGenerated SQL:")
        print(sql_response)
