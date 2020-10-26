# 2. Palindroms
# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira      sula") -> True

def is_palindrome(text:str) -> bool:
    textNoExtraSpaces = " ".join(text.split())
    text_list = text.split()
    text_list.reverse()
    reverseSentence_list = []
    for word in text_list:
        temp = word[::-1]
        reverseSentence_list.append("".join(temp))
    if textNoExtraSpaces == " ".join(reverseSentence_list):
        return True
    else:
        return False

print(is_palindrome("alus    ari ira sula"))
print(is_palindrome("sula"))
print(is_palindrome("ala"))