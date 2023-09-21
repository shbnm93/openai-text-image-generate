import creds
import os
import openai

os.environ["OPENAI_KEY"] = creds.API_KEY
openai.api_key = os.environ["OPENAI_KEY"]


keep_prompting = True
while keep_prompting:
    prompt = input("Please enter  your image prompt. Type exit if done. ")
    n = int(input("Please input the number of images you want to generate."))
    if prompt == "exit":
        keep_prompting = False
    else:
        image_gen = openai.Image.create(prompt=prompt,  
                                        n=n,    
                                        size="1024x1024")
        for img in range(0, n):
            print(image_gen["data"][img]["url"])