# Technical Support Chat Assistant

## Description

This Flask application serves as a customer service chat assistant for a large electronic store. It uses the OpenAI GPT-3.5 Turbo model to generate responses in a friendly and helpful tone, providing concise answers to user queries about electronic products.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Zeros2112/technical_support_chatbot.git 

2. Navigate to the project directory
   cd technical_support_chatbot

## Usage  

   run the Flask application
   ```
   python app.py
   ```

## Configuration

Create a .env file in the project directory and add your OpenAI GPT-3.5 Turbo API key:
```
# .env
OPENAI_API_KEY=your_openai_api_key
```

## Endpoints

### Home Page
GET /: Returns the home page. 
### Chat Endpoint
POST /chat: Handles user input and returns chat responses.


## Dependencies 
* Flask==2.0.1
* openai==0.27.0
* python-dotenv==0.19.0

## Contributing
1. Report bugs, sugget features, or contribute to the codebase
2. Fork the repository and create a new branch for your contributions:
```
git checkout -b feature/new-feature

```
3. Make your changes and submit a pull request

## License
This project is licensed under the MIT License.








