from typing import Iterable

def replace_first(items: list) -> Iterable:
    tamanho=len(items)
    if tamanho>=1:
        primeiro=items[0]
        items.append(primeiro)
        corte=slice(1,len(items))
        items=items[corte]
    return items

if __name__ == "__main__":
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
