from speech import Speech
from assistant import Assistant
from commands import is_exit_command, local_command


def main():
    speech = Speech()
    assistant = Assistant(speech)

    speech.speak("Hello. I am your AI voice assistant.")
    speech.speak(
        "You can ask my name, ask the time, open YouTube, "
        "or ask me a question."
    )

    while True:
        command = speech.listen()

        if command == "":
            continue

        if is_exit_command(command):
            speech.speak("Goodbye. Have a nice day.")
            break

        handled = local_command(command, speech.speak)

        if not handled:
            assistant.reply(command)


if __name__ == "__main__":
    main()
    