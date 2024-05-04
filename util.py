from dotenv import load_dotenv
from pix2text import Pix2Text
from PIL import Image
import os
import openai

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
SYSTEM_PROMPT = r"You are a professor that has a doctorate in mathematics. Your purpose is to provide the process to solve math word problems that are formatted in latex without giving the answer. Use \[...\] as delimiters for displayed mathematics and use \(...\) for in-line mathematics."

client = openai.OpenAI(api_key=API_KEY)


def gpt_solve_prob(problem: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {"role": "user", "content": f"{problem}"},
        ],
    )
    return response.choices[0].message.content


def math_ocr_latex(image: Image.Image) -> str:
    p2t = Pix2Text.from_config()
    outs = p2t.recognize(image, return_text=True)
    return outs
