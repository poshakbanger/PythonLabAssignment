def Palindrome(checkWord):  # userDefined function
    for i in range(0, int(len(checkWord) / 2)):  # 0 to halfOfWord
        if checkWord[i] != checkWord[len(checkWord) - i - 1]:  # checking 1st and last letter
            return False
    return True


word = "maam"  # Word to check
result = Palindrome(word)

if result:
    print("Palindrome")
else:
    print("Not Palindrome")