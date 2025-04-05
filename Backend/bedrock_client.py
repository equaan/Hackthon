# backend/bedrock_client.py

import boto3
from langchain.llms import Bedrock  # Adjust import as needed based on your package version
from langchain.prompts import PromptTemplate

def get_bedrock_client():
    """Initialize the Bedrock client using boto3."""
    return boto3.client("bedrock-runtime", region_name="us-east-1")

def create_llm():
    """Create and return the LLM instance using Amazon Bedrock and Langchain."""
    client = get_bedrock_client()
    model_id = "meta.llama3-2-11b-instruct-v1:0"  # Replace with your actual model ID (e.g., for Llama 2)
    return Bedrock(model_id=model_id, client=client, model_kwargs={"temperature": 0.9})

def generate_motivational_quote():
    """
    Generates a motivational quote using the generative AI model.
    The prompt instructs the model to create an uplifting, concise message.
    """
    llm = create_llm()
    prompt = (
        "You are an inspirational coach. Please generate a short, powerful, and uplifting motivational quote "
        "to encourage someone who is studying hard and striving for success."
    )
    return llm(prompt)

def generate_study_routine(user_input):
    """
    Generates a personalized study routine based on the user's input.
    If the goal indicates short-term preparation (e.g., exam prep or learning a skill), a daily plan is generated.
    For long-term goals, a weekly plan is provided.
    The response is appended with a motivational quote.
    """
    llm = create_llm()
    
    prompt_template = (
        "You are an expert study coach. A user has provided the following goal: '{user_input}'.\n"
        "Based on this input, generate a detailed study plan.\n"
        "If the goal indicates short-term preparation, provide a daily plan; if it indicates long-term preparation, provide a weekly plan with subject breakdowns and practical tips.\n"
        "Ensure the plan is clear, actionable, and motivational."
    )
    
    prompt = prompt_template.format(user_input=user_input)
    routine = llm(prompt)
    motivation = generate_motivational_quote()
    return f"{routine}\n\nMotivation: {motivation}"
