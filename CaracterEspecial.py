def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    texto = 'abcdefghijklmnopqrstuvxzwyABCDEFGHIJKLMNOPQRSTUVXZWY '
    listaOK = []
    especial = []
    for i in range(len(text)):
        if text[i] not in texto:
            especial.append(i)

    for i in range(especial[0], len(text)):
         listaOK.append(text[i])

    listaOK=''.join(listaOK)
    resultado=[]
    for i in range(len(listaOK)):
        if listaOK[i] in texto:
            resultado.append(listaOK[i])

    resultado=''.join(resultado)
    return resultado


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
