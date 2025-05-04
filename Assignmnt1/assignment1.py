import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

news_article = """
The central bank has increased interest rates for the third consecutive quarter, citing persistent inflation and global economic uncertainty. 
Analysts believe this move could slow consumer spending and impact borrowing rates across sectors, including housing and small businesses. 
While some praise the decision as necessary to stabilize the economy, others worry it may lead to a recession.
"""
prompts = [
    "Summarize the following news article in one sentence.",
    "Write a concise summary (2-3 sentences) of the news article below, focusing on the key facts.",
    "Summarize the news article below with emphasis on economic impact and reactions from analysts and public."
]
outputs = []

for i, prompt in enumerate(prompts):
    print(f"\nPrompt {i+1}: {prompt}")
    full_prompt = f"{prompt}\n\n{news_article}"

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": full_prompt}
            ],
            max_tokens=200,
            temperature=0.5
        )
        output = response.choices[0].message.content
        outputs.append(output)
        print(f"\nOutput {i+1}: {output}")

    except Exception as e:
        print(f"Error with prompt {i+1}: {e}")

print("\n--- Reflection ---")
print("Now read all 3 outputs and write a brief reflection on which prompt was most effective and why.")