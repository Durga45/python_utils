emoji_map_fun = {
    "happy": "😄",
    "sad": "😢",
    "angry": "😠",
    "laugh": "😂",
    "cool": "😎",
    "party": "🥳",
    "love": "❤️",
    "thumbs_up": "👍",
    "clap": "👏",
    "wink": "😉",
    "sleepy": "😴",
    "thinking": "🤔",
    "shock": "😲",
    "robot": "🤖",
    "fire": "🔥"
}


message=input("Enter your message: ").strip()

updatedWords=[]

for word in message.split():
    cleaned=word.lower().strip(".,!?:")
    emoji=emoji_map_fun.get(cleaned,"")
    if emoji:
        updatedWords.append(f"{word} {emoji}")
    else:
        updatedWords.append(word)

updatedMessage=" ".join(updatedWords)
print("\n enhanced message\n")
print(updatedMessage)