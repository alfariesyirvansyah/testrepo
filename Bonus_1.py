#Løsningsforslag bonusoppgave
def isAnagram(s1, s2):
    c1 = ""; c2 = ""
    for letter in s1:
        if letter.isalpha():
            c1 += letter.lower()
    for letter in s2:
        if letter.isalpha():
            c2 += letter.lower()
    return "".join(sorted(c1)) == "".join(sorted(c2))