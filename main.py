import random

def main():
    hidenWords = english_words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "xigua", "yellowfruit", "zucchini", "apricot", "blueberry", "cantaloupe", "dragonfruit", "eggplant", "grapefruit",
    "huckleberry", "imbe", "jackfruit", "kumquat", "lime", "mulberry", "nashi", "olive", "pear", "pomegranate",
    "quandong", "rambutan", "starfruit", "tomato", "ugni", "voavanga", "wolfberry", "ximenia", "yam", "ziziphus",
    "asparagus", "broccoli", "carrot", "daikon", "endive", "fennel", "garlic", "horseradish", "jicama", "kale",
    "lettuce", "mushroom", "nopales", "onion", "parsnip", "quinoa", "radish", "spinach", "turnip", "watercress",
    "yam", "zucchini", "avocado", "basil", "cilantro", "dill", "eggplant", "fennel", "ginger", "horseradish",
    "jalapeno", "kohlrabi", "leek", "mint", "oregano", "parsley", "rosemary", "sage", "thyme", "wasabi",
    "yam", "zucchini", "artichoke", "beet", "celery", "chard", "cucumber", "dandelion", "escarole", "fiddlehead"
]
    hidenWord = hidenWords[random.randint(0, len(hidenWords))]
    guessedLetters = [""]
    remainingLife = 10
    while True:
        displayHidenWord(hidenWord, guessedLetters)
        userInput = input("Enter a guessed letter: ")
        guessedLetters.append(userInput)
        displayHidenWord(hidenWord, guessedLetters)
        remainingLife -= 1
        print("Remaining life: " + str(remainingLife))


def displayHidenWord(hidenWord, guessedLetters):
    result = ""
    for letter in hidenWord:
        if letter.lower() in guessedLetters:
            result += letter 
        else:
            result += "*"
    print(result)
    return result

if __name__ == "__main__":
    main()