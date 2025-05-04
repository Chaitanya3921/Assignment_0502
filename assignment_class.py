import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key =os.getenv("OPENAI_API_KEY")
sample_resume = """ name: Chaitanya Parvataneni 
email: Chaitanya123@gmail.com
Education: Computer Science, ABCD University (2011-2015)
Skills: Java,SpringBoot, Microservices, JavaScript, SQL, Git
Experience:
- Software developer role in abc corp(2019-2025)
  - Built REST APIs using Flask and PostgreSQL
  - Collaborated in Agile sprints with a team of 6 engineers


Projects:
- Telecomm app internal web application
- get the orders from upsteam system and generate WO's and send to appropriate systems
"""

role_prompt = "You are a hiring manager reviewing a resume. Provide detailed, professional feedback about strengths and weaknesses in the resume below:\n\n"
generic_prompt = "Evaluate this resume:\n\n"
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

# Get both responses
print("== Role-Based Response ==\n")
print(get_response(role_prompt))

print("\n== Generic Response ==\n")
print(get_response(generic_prompt))