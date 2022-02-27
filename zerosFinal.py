def end_zeros(num: int) -> int:
    total = str(num)
    total_tam = len(total)
    zeros = total.strip('0')
    zeros_tam = len(zeros)
    return total_tam - zeros_tam

if __name__ == "__main__":
    print(' '); print('tamanho absoluto do número - total de zeros = ', end_zeros(100100)); print(' ')

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
