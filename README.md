# Asha AI Chatbot

An AI-powered career guidance chatbot for women built using Dialogflow and Flask.

## Features

- Interactive chatbot UI with custom styling
- Responsive design that works on mobile and desktop
- Provides career guidance and job recommendations
- Integrated with Dialogflow for natural language processing

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- A Google Cloud Platform account with Dialogflow enabled

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/koradiaishita/asha-ai-chatbot.git
   cd asha-ai-chatbot
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python main.py
   ```

4. Open your browser and navigate to:
   - Main site: `http://localhost:8080/`
   - Standalone chatbot: `http://localhost:8080/chatbot`

## Usage

The chatbot offers two deployment options:

1. **Embedded in the main application** - Access via the homepage at `/`
2. **Standalone chatbot page** - Access directly at `/chatbot`

You can interact with the chatbot by:
- Clicking on the chat bubble in the bottom right corner
- Typing your queries about career guidance, jobs, etc.
- The chatbot will respond with helpful information and guidance

## Configuration

The chatbot is configured with the following parameters:
- Project ID: `gen-ai-guru-gdg-pune`
- Agent ID: `b2c5e90b-20ef-4b0c-96d1-49537c77a2cf`
- Location: `asia-south1`

## Customization

You can customize the chatbot's appearance by modifying the CSS variables in either:
- `chatbot.html` - For the standalone version
- `templates/index.html` - For the embedded version

## Troubleshooting

If the chatbot doesn't load properly:
1. Check browser console for errors
2. Ensure your network can access Google's Dialogflow services
3. Verify that the Dialogflow agent is properly configured

## License

This project is open source and available under the [MIT License](LICENSE).