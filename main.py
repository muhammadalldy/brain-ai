import openai
import os

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
 
def ask_gpt_3_5_turbo(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question},
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_question = input("Please enter your question: ")
        if user_question.lower() == "quit":
            break
        answer = ask_gpt_3_5_turbo(user_question)
        print("GPT-3.5 Turbo Assistant:", answer)
