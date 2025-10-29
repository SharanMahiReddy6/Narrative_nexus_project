from groq import Groq
client = Groq(api_key="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")
response = client.models.list()
print([m.id for m in response.data])
