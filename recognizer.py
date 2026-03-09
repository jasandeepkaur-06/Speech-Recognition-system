import speech_recognition as sr

# Function to recognize speech
def recognize_speech():

    recognizer = sr.Recognizer()

    # Use microphone as audio source
    with sr.Microphone() as source:

        print("Speak something...")

        # Reduce background noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen to audio from microphone
        audio = recognizer.listen(source)

    try:

        # Convert speech to text using Google API
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Could not understand audio"

    except sr.RequestError:
        return "Network error"    