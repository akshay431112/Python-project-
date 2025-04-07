import datetime
import random

quotes = [
    "Keep grinding, you're leveling up!",
    "You’re not stuck, you’re just getting ready for your next move.",
    "Small progress is still progress 💪",
    "Code today, conquer tomorrow 🚀"
]

now = datetime.datetime.now()
greeting = "Good morning, Dev 💻" if now.hour < 12 else "Hello, Code Boss 👨‍💻"

print(greeting)
print(f"Time now: {now.strftime('%H:%M:%S')}")
print("Quote of the session: " + random.choice(quotes))

