import os
import json
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Load environment variables
load_dotenv()

# Get API key from the environment
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

model = ChatCohere(model="command-r-plus")

# Define the prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Categorize the following expense into one of the categories: Housing, Transportation, Food, Utilities, Insurance, Medical/Healthcare, Savings, Debt, Education, Entertainment, Other.

            Ensure the following conditions are met:
            1. **Amount** must be a positive number in USD ($), with no words (e.g., "109" is valid, but "one hundred and nine" is not).
            2. If the amount is missing, not a valid number, or includes words, respond with: **Invalid amount ❌**.
            3. Ignore any messages that are not related to expenses, such as greetings or irrelevant text, by responding with: **I only categorize expenses.**

            Input example:
            - Description: "{description}"

            Return a valid JSON object without any additional text, such that the structure is:


                "description": "<description>",
                "amount": "<amount>",
                "category": "<category>",
                "message": "<message>"


            - description is the description of the expense.
            - amount is the valid numerical amount in USD.
            - category is the appropriate expense category.
            - message is one of the following:
                - For valid expenses: `<category> expense added ✅`
                - For invalid expenses: `Invalid amount ❌`
                - For non-expense messages: `I only categorize expenses.`
            """
        ),
        MessagesPlaceholder(variable_name="description"),
    ]
)

# Chain the model and prompt
chain = prompt | model

def process_message(user_message):
    # Invoke the model with user input
    response = chain.invoke({"description": [HumanMessage(content=user_message)]})

    try:
        # Clean the response by removing extra characters
        cleaned_response = response.content.strip()

        # Remove any prefix like "json" or "JSON Response:"
        cleaned_response = cleaned_response.replace('JSON Response:', '').strip()
        cleaned_response = cleaned_response.replace('json', '').replace('`', '').strip()

        # Try parsing the cleaned response
        response_json = json.loads(cleaned_response)
        # Extract the message from the JSON
        message = response_json.get("message", "No message provided")

        return {
            "json": response_json,
            "message": message
        }

    except json.JSONDecodeError as e:
        print('Error decoding JSON:', str(e))
        print('Response content that caused the error:', cleaned_response)
        return {
            "json": None,
            "message": "Error: Could not parse the response."
        }

