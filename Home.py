import streamlit as st
import random
import time
from huggingface_hub import InferenceClient


def api(role,content):
	client = InferenceClient(api_key="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")
	messages = [
		{
			"role": role,
			"content": content
		
		}
	]

	stream = client.chat.completions.create(
		model="meta-llama/Llama-3.2-3B-Instruct", 
		messages=messages, 
		max_tokens=500,
		stream=True
	)

	for chunk in stream:
          yield "".join(chunk.choices[0].delta.content)
          time.sleep(0.05)






# Streamed response emulator
# def response_generator(data):
#     response = (
#         [
#             data
#         ]
#     )
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)


st.title("Llama-3.2-3B")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter your Message"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(api("user",prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




# client = InferenceClient(api_key="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")
# messages = [
# 	{
# 		"role": "user",
# 		"content": "what is nlp?"
	
# 	}
# ]

# stream = client.chat.completions.create(
# 	model="meta-llama/Llama-3.2-3B-Instruct", 
# 	messages=messages, 
# 	max_tokens=500,
# 	stream=True
# )

# mydata=[]
# for chunk in stream:
# 	mydata.append(chunk.choices[0].delta.content)
# print("".join(mydata))




