import random

list1 = ["Споглядати", "Милуватися", "Насолоджуватися", "Відчути"]
list2 = ["пейзажем", "сходом сонця", "краєвидом", "моментом"]
list3 = ["приємно", "захопливо", "незабутньо", "надихаюче"]

def generate_phrase():
    word1 = random.choice(list1)
    word2 = random.choice(list2)
    word3 = random.choice(list3)
    return f"{word1} {word2} — це {word3}."

if __name__ == "__main__":
    print("Випадкова фраза: ")
    print(generate_phrase())
