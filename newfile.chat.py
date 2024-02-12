#pip install openai
import openai
openai.api_key= "sk-ctSXCZilnS0d0Lmzdrt6T3BlbkFJKWW3 6SKWKLtR6HhTgo7"
while True:
 ask = input("khalil vip : ")
 response= openai.Completion.create(
    model = "text-davinci-003",
    prompt=ask,
    temperature=0.9,
    max_tokens=600,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
) 
text =response['choices'][0] ['text']
print("ChatGPT :" +text)
