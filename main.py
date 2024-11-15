# 1
def tribonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n == 3:
        return [1, 1, 1]

    trib = [1, 1, 1]
    for i in range(3, n):
        trib.append(trib[-1] + trib[-2] + trib[-3])
    return trib


n = int(input("Введите количество чисел ряда Трибоначчи: "))
print(tribonacci(n))

# 2
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)

text = input("Введите строку для шифрования: ")
shift = int(input("Введите сдвиг: "))
print(caesar_cipher(text, shift))

# 3
def unique_sorted_list(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return sorted(unique_numbers)

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
print(unique_sorted_list(numbers))

# 4
def sort_words_by_length(sentence):
    words = sentence.split()
    words.sort(key=lambda word: (len(word), word))
    return words

sentence = input("Введите строку из нескольких слов: ")
print(sort_words_by_length(sentence))

# 5
def is_armstrong_number(num):
    digits = list(map(int, str(num)))
    power = len(digits)
    return num == sum(digit ** power for digit in digits)

def armstrong_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if is_armstrong_number(num)]

start = int(input("Введите начальное число диапазона: "))
end = int(input("Введите конечное число диапазона: "))
print(armstrong_numbers_in_range(start, end))