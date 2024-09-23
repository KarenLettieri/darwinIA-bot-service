# Expense Categorization Bot
This project is a Flask application that categorizes expenses based on user input using a language model. It leverages the LangChain library and Cohere's model to process and categorize expenses efficiently.

## Project Structure
The project consists of the following main files:

run.py: This file initializes and runs the Flask application.
main.py: This file defines the main Blueprint for handling HTTP requests related to expense categorization.
message_processor.py: This file contains the logic to process user messages and interact with the language model for expense categorization.

##Requirements
Before running the project, ensure you have the following installed:

Python 3.x
pip (Python package installer)
You will also need to install the necessary Python packages. Create a virtual environment and install the dependencies using the requirements.txt file.

# Installing Dependencies

# Create a virtual environment (optional but recommended)
``` python -m venv venv ```
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the required packages
``` pip install -r requirements.txt ```

## Environment Variables
Before running the application, create a .env file in the root directory of the project to store environment variables. It should include your Cohere API key:
COHERE_API_KEY=your_cohere_api_key

Replace your_cohere_api_key with your actual API key.

## Running the Application
To run the Flask application, execute the following command:
``` python run.py ```

# Conclusion
This project serves as a basic framework for categorizing expenses using natural language processing in a telegram bot.
