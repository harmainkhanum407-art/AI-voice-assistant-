import datetime
import webbrowser
from urllib.parse import quote_plus


def is_exit_command(command):
    exit_words = [
        "bye",
        "goodbye",
        "exit",
        "quit",
        "stop",
        "close assistant"
    ]

    return any(word in command for word in exit_words)


def play_on_youtube(command, speak):
    """
    Search YouTube using the words spoken after 'play'.
    """

    command = command.lower().strip()

    phrases = [
        "play on youtube",
        "play in youtube",
        "play youtube",
        "play",
        "search youtube for",
        "search on youtube for",
        "search youtube"
    ]

    search_text = ""

    for phrase in phrases:
        if phrase in command:
            search_text = command.split(phrase, 1)[1].strip()
            break

    if search_text == "":
        speak("Please tell me what you want to play on YouTube.")
        return True

    youtube_url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(search_text)
    )

    speak(f"Searching YouTube for {search_text}.")
    webbrowser.open_new_tab(youtube_url)

    return True


def local_command(command, speak):
    command = command.lower().strip()

    # YouTube commands
    if (
        "youtube" in command
        and (
            "play" in command
            or "search" in command
            or "open" in command
        )
    ):
        return play_on_youtube(command, speak)

    # Greeting
    if "hello" in command or command == "hi":
        speak("Hello! How can I help you?")
        return True

    # Assistant name
    if "what is your name" in command or "your name" in command:
        speak("My name is AI Harmain. I am your AI voice assistant.")
        return True

    # General conversation
    if "how are you" in command:
        speak("I am fine. Thank you for asking.")
        return True

    # Time
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
        return True

    # Date
    if "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {today}.")
        return True

    # Open Google
    if "open google" in command:
        speak("Opening Google.")
        webbrowser.open_new_tab("https://www.google.com")
        return True

    # Thanks
    if "thank you" in command or "thanks" in command:
        speak("You are welcome.")
        return True

    return False