from openai import OpenAI

def ask_ai(prompt, model="gpt-3.5-turbo"):
  client = OpenAI()
  messages = [{"role": "user", "content": prompt}]
  response = client.chat.completions.create(
  model=model,
  messages=messages,
  max_tokens=50,
  temperature=0,
  )
  return response.choices[0].message.content