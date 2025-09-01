import sounddevice as sd
import numpy as np
import speech_recognition as sr

def listen_to_user(duration=5, sample_rate=16000):
    """
    Records audio for `duration` seconds and returns the recognized text.
    Uses sounddevice to capture microphone input, so PyAudio is not required.
    """
    recognizer = sr.Recognizer()

    print("🎙️ Listening for", duration, "seconds…")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, 
                       channels=1, dtype='int16')
    sd.wait()  # block until recording is finished

    audio_bytes = recording.tobytes()
    audio_data = sr.AudioData(audio_bytes, sample_rate, 2)

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"🗣️ You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Speech service is unavailable."
