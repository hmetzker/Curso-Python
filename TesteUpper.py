def is_all_upper(text: str) -> bool:
    # esta função usa um parametro do tipo str e retorna
    # um objeto do tipo booleano
    return text == text.upper()


if __name__ == '__main__':
    assert is_all_upper('maria') == False
    assert is_all_upper('Maria') == False
    assert is_all_upper('PYTHON') == True
    assert is_all_upper('44 444 555 6') == True
