# 2. Palindroms
# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira      sula") -> True
def is_palindrome(text:str) -> bool:
    textNoExtraSpaces = " ".join(text.lower().split())
    text_list = text.lower().split()
    text_list.reverse()

    reverseSentence_list = []
    for word in text_list:
        reverseSentence_list.append("".join(word[::-1]))

    return textNoExtraSpaces == " ".join(reverseSentence_list)


#tests
print(is_palindrome("Alus    ari ira sula"))
print(is_palindrome("sula"))
print(is_palindrome("ala"))