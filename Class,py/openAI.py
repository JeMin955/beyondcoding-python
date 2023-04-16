from email import message
import os
import openai
openai.api_key = "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"

messages = []
while True:
    newMsg = {"role": "user", "content": input("Me : ")}
    messages.append(newMsg)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    messages.append(completion.choices[0].message)

    print("GePeaT : ",completion.choices[0].message["content"])

    if newMsg["content"] == "bye":
        break