import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(f"Gefundene Stimmen: {[v.id for v in voices]}")
