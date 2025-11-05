import subprocess
import random

# Список эмодзи
emojis = ["🚀", "✨", "🔥", "🐍", "🧠", "🔧", "🎯", "🌟", "💡", "📦"]

# Сообщение коммита
commit_message = input("Введите сообщение для коммита: ")
emoji = random.choice(emojis)
commit_message_with_emoji = f"{commit_message} {emoji}"

try:
    # Добавляем все изменения
    subprocess.run(["git", "add", "."], check=True)

    # Создаём коммит с эмодзи
    subprocess.run(["git", "commit", "-m", commit_message_with_emoji], check=True)

    # Отправляем изменения на GitHub
    subprocess.run(["git", "push"], check=True)

    print(f"✅ Успешно! Коммит: {commit_message_with_emoji}")

except subprocess.CalledProcessError:
    print("❌ Ошибка при выполнении команд Git")
