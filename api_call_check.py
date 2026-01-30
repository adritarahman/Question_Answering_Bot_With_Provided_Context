from gradio_client import Client

client = Client("Adrita03/QnA_with_context")
result = client.predict(
	question="What is the name of the dog?",
	context="Alice is a software engineer. She lives in Seattle. Alice has a dog named Buddy. In her free time, she likes to bake chocolate cakes. ",
	api_name="/get_answer"
)
print(result)

