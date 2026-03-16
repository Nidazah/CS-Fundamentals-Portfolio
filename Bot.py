import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Say a command (e.g., 'search cats' or 'open youtube')...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()
    print(f"You said: {command}")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    if command.startswith("search "):
        query = command.replace("search ", "", 1)
        driver.get(f"https://www.google.com/search?q={query}")

    elif "open youtube" in command:
        driver.get("https://www.youtube.com")

    elif "open facebook" in command:
        driver.get("https://www.facebook.com")

    else:
        print("Command not recognized")

    # ⏸ Keep browser open until you press Enter
    input("Press Enter to close the browser...")

    driver.quit()

except sr.UnknownValueError:
    print("⚠️ Sorry, I could not understand what you said. Please try again.")
except sr.RequestError as e:
    print(f"⚠️ Could not request results from Google Speech Recognition service; {e}")

    # CMD : py -3.11 Bot.py