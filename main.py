import random
password_type = input("Which type of password do you want? 1.True random, or 2.Enter a phrase to generate a password out of(make sure it is all lowercase)")
password = []
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
if password_type == "True random":
    for i in range(random.randint(15,20)):
        type = random.randint(1,3)
        if type == 1:
            number = random.randint(1,9)
            password.append(str(number))
        elif type == 2:
            letter = random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
            password.append(letter)
        else:
            symbol = random.choice(symbols)
            password.append(symbol)
        random.shuffle(password)
else:
    letter_replacements = {"a": "@", "s": "$", "o": "0", "i": "1", "e": "3", "t": "7", "l": "!", "g": "9", "b": "8"}
    phrase = input("Enter your phrase: ")
    for char in phrase.lower():
        if char in letter_replacements:
            password.append(random.choice([char, letter_replacements[char],char.upper()]))
        else:
            password.append(random.choice([char,char.upper()]))
password = ''.join(password)
print(f"Your password is: {password}")
