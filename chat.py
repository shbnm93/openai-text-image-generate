import creds
import os
import openai

os.environ["OPENAI_KEY"] = creds.API_KEY
openai.api_key = os.environ["OPENAI_KEY"]


keep_prompting = True
while keep_prompting:
    prompt = input("Please enter in your question or prompt. Type exit if done. ")
    if prompt == "exit":
        keep_prompting = False
    else:
        # response = openai.Completion.create(model = "text-davinci-003", 
        #                                     prompt = prompt,    
        #                                     max_tokens=200)
        # print(response["choices"][0]["text"])
        chat_prompt = [
            {"role":"user", "content": prompt}
        ]
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",  
                                                messages=chat_prompt,   
                                                max_tokens=200)
        print(response["choices"][0]["message"]["content"])