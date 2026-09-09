import os
from dotenv import load_dotenv
from openai import OpenAI


class Assistant:
    def __init__(self, speech):
        self.speech = speech
        self.client = None

        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        if api_key and api_key.startswith("sk-"):
            try:
                self.client = OpenAI(api_key=api_key)
                print("OpenAI API connected.")
            except Exception as error:
                print(f"OpenAI setup error: {error}")
        else:
            print("OpenAI API key not found.")
            print("Local commands will still work.")

    def ask_openai(self, question):
        if self.client is None:
            return (
                "I can answer basic commands, but my OpenAI API key "
                "is not connected."
            )

        try:
            response = self.client.responses.create(
                model="gpt-4.1-mini",
                input=(
                    "You are a friendly voice assistant named AI Harmain. "
                    "Answer briefly and clearly because your reply will "
                    "be spoken aloud.\n\n"
                    f"User question: {question}"
                )
            )

            answer = response.output_text.strip()

            if answer:
                return answer

            return "I could not generate an answer."

        except Exception as error:
            print(f"OpenAI error: {error}")
            return "I could not connect to OpenAI right now."

    def reply(self, command):
        answer = self.ask_openai(command)
        self.speech.speak(answer)