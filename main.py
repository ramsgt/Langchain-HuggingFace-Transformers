# import required packages

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error

# set verbosity to restrict warnings
#set_verbosity_error()

print('Started.....')

#Initilize HF model for summarization task
summary_pipeline = pipeline("summarization", model="facebook/bart-large-cnn", device=0)

# Warp it inside langchain
summarizer = HuggingFacePipeline(pipeline=summary_pipeline)

#Initialize HF mode to refine the summary 
refine_pipeline = pipeline("summarization", model = "facebook/bart-large-cnn", device=0)
refiner = HuggingFacePipeline(pipeline=refine_pipeline)

#Initiate the Questiona Answer pipline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", device=0)

#Create a promot template for summarization task
summary_template = PromptTemplate.from_template("Summarize the folloing text in a {length} way:\n\n{text}")

#Initiate summary model chain 
summary_chain = summary_template | summarizer | refiner

#initiate user inputs
text_to_summarizer = input("\nEnter text to summarize:\n")
length = input("\nEnter the lenth (short/medium/long):\n")

#Exucute the suummirazation task
summary = summary_chain.invoke({"text": text_to_summarizer, "length": length})
print("\n **Here is the summary**\n")
print(summary)

# Execute QA task and exit
while True:
    question = input("\nAsk a question about the summary (or type 'exit' to stop):\n")
    if question.lower() == "exit":
        break

    qa_result=qa_pipeline(question=question, context=summary)

    print("\n **Answer:**")
    print(qa_result["answer"])