# Langchain-HuggingFaces-Transformers-Python
This repository contains code and examples for integrating LangChain with Hugging Face Transformers. It provides tools to leverage pre-trained models for various natural language processing tasks within the LangChain framework.

## Features
- Easy integration with Hugging Face Transformers models.
- Support for a wide range of NLP tasks including **Summrization** and **Question Answering**.
- Examples demonstrating how to use different models with LangChain.
- Customizable pipelines for specific use cases.

## Installation
- Create a Virtual Environment
  1. For Windows (Command Prompt)
  ```
  python -m venv env
  env\Scripts\activate
  ```
  2. For macOS/Linux (Terminal)
  ```
  python -m venv env
  source env/bin/activate
  ```
To install the required packages, run:
```
pip install -r requirements.txt
``` 
## Usage

### Summarization Example
## Step 1: 
*Enter text to summarize:*

 Generative AI (GenAI) is a rapidly growing field of artificial intelligence that focuses on creating new content such as text, images, code, audio, and video by learning patterns from large datasets. It is used in many areas like healthcare for drug discovery, automotive for autonomous systems, education for personalized learning, and business for customer service chatbots and content creation. GenAI is also widely applied in creative fields such as art, design, film, and music, enabling professionals to generate new ideas and save time. One of the top GenAI products is ChatGPT by OpenAI, which is known for its conversational capabilities, knowledge assistance, and productivity tools. Another leading product is Google Gemini, which combines advanced reasoning and multimodal features to handle both text and image-based tasks. A third top product is Anthropic’s Claude, valued for its safer, more aligned AI responses and efficiency in handling large-scale knowledge tasks. These products are being adopted in industries like IT, marketing, research, and customer engagement to reduce manual work and improve efficiency. GenAI also powers copilots in programming, such as GitHub Copilot, helping developers write and debug code faster. With its ability to process vast amounts of data and generate human-like responses, GenAI is becoming a trusted partner for decision-making and innovation. Overall, GenAI is transforming industries by enhancing productivity, creativity, and problem-solving capabilities at scale

## Step 2:
*Enter the lenth (short/medium/long):*
long

### output:
Generative AI (GenAI) is a rapidly growing field of artificial intelligence. It focuses on creating new content such as text, images, code, audio, and video by learning patterns from large datasets. It is used in many areas like healthcare for drug discovery, automotive for autonomous systems, education for personalized learning, and business for customer service chatbots.

## Step 3:
*Ask a question about the summary (or type 'exit' to stop):*  
GenAI focus areas?

### output:
creating new content

*Ask a question about the summary (or type 'exit' to stop):*  
where is GenAI used?

### output:
healthcare

*Ask a question about the summary (or type 'exit' to stop):*   
What are learning patterns?

### output:
large datasets

*Ask a question about the summary (or type 'exit' to stop):*   
exit


### Important Note:
The models used in this repository may require significant computational resources. It is recommended to run them on a machine with a powerful GPU for optimal performance.
