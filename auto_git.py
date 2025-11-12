import subprocess
import random

emojis = ["🚀", "✨", "🔥", "🐍", "🧠", "🔧", "🎯", "🌟", "💡", "📦"]

commit_message = input("Введите сообщение для коммита: ")
emoji = random.choice(emojis)
commit_message_with_emoji = f"{commit_message} {emoji}"

try:
    subprocess.run(["python", "PJ11_gitinfo_10.py"], check=True)

    subprocess.run(["git", "add", "."], check=True)

    subprocess.run(["git", "commit", "-m", commit_message_with_emoji], check=True)

    subprocess.run(["git", "push"], check=True)

    print(f"✅ Успешно! Коммит: {commit_message_with_emoji}")

except subprocess.CalledProcessError:
    print("❌ Ошибка при выполнении команд Git")
