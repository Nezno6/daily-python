def format_word_order(dictionary: dict):
    return f'{len(dictionary)}\n{" ".join(str(value) for value in dictionary.values())}'

def word_order(words: list):
    answer: dict = dict()
    for word in words:
        if word in answer:
            answer[word] += 1
        else:
            answer[word] = 1
    return format_word_order(answer)

if __name__ == "__main__":    
    print(word_order([input() for _ in range(int(input()))]))

