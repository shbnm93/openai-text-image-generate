import creds
import os
import openai

os.environ["OPENAI_KEY"] = creds.API_KEY
openai.api_key = os.environ["OPENAI_KEY"]

# Define a list of predefined prompts
predefined_prompts = [
    "Translate the following English text to French: 'Hello, how are you?'",
    "Write a summary of the plot of the novel 'To Kill a Mockingbird'.",
    "Explain the concept of blockchain technology.",
    "Compose an email to your manager requesting a day off.",
    "Describe the process of photosynthesis in plants.",
    "What are the benefits of regular exercise for overall health?",
]

def generate_response(prompt):
    chat_prompt = [
        {"role": "user", "content": prompt}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_prompt,
        max_tokens=200
    )
    
    return response["choices"][0]["message"]["content"]

keep_prompting = True
chat_history = []

print("Welcome to the AI Chatbot. You can type 'exit' to quit at any time.")

while keep_prompting:
    print("\nChoose an option:")
    print("1. Select a predefined prompt")
    print("2. Enter your own prompt")
    print("3. Exit")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        print("Choose a predefined prompt:")
        for i, prompt in enumerate(predefined_prompts):
            print(f"{i + 1}. {prompt}")
        
        prompt_choice = input("Enter the number of the prompt you'd like to use: ")
        if prompt_choice.isdigit():
            index = int(prompt_choice) - 1
            if 0 <= index < len(predefined_prompts):
                selected_prompt = predefined_prompts[index]
                response = generate_response(selected_prompt)
                chat_history.append({"role": "user", "content": selected_prompt})
                chat_history.append({"role": "assistant", "content": response})
                print(response)
            else:
                print("Invalid prompt number. Please choose a valid option.")
        else:
            print("Invalid input. Please choose a prompt by entering its number.")
    
    elif choice == "2":
        user_prompt = input("Enter your own prompt: ")
        response = generate_response(user_prompt)
        chat_history.append({"role": "user", "content": user_prompt})
        chat_history.append({"role": "assistant", "content": response})
        print(response)
    
    elif choice == "3":
        keep_prompting = False
    
    else:
        print("Invalid choice. Please select a valid option.")
