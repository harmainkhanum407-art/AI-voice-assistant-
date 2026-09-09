import speech_recognition as sr
import pyttsx3


class Speech:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

        voices = self.engine.getProperty("voices")
        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text):
        print(f"AI: {text}")

        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("\nListening... Please speak now.")

            self.recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            except sr.WaitTimeoutError:
                print("No speech detected.")
                return ""

        print("Recognizing...")

        try:
            text = self.recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print(f"You: {text}")
            return text.lower().strip()

        except sr.UnknownValueError:
            print("AI: Sorry, I could not understand you.")
            return ""

        except sr.RequestError as error:
            print(f"Speech recognition error: {error}")
            self.speak("I cannot connect to the speech recognition service.")
            return ""

        except Exception as error:
            print(f"Microphone error: {error}")
            return ""