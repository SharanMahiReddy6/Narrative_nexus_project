from groq import Groq
client = Groq(api_key="YOUR_GROQ_API_KEY")
response = client.models.list()
print([m.id for m in response.data])
