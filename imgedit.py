import creds
import os
import openai

os.environ["OPENAI_KEY"] = creds.API_KEY
openai.api_key = os.environ["OPENAI_KEY"]



image_edit = openai.Image.create_edit(
    image = open("Arm.png", "rb"),
    mask=open("noArm.png", "rb"),
    prompt = "A woman wearing an arm prosthesis.",
    n=1,
    size="1024x1024"
)

print(image_edit)