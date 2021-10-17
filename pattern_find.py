def find_pattern(str_, pattern):
    for i in range(len(str_) - len(pattern) + 1):
        break_ = False
        for j in range(len(pattern)):
            if pattern[j] != str_[i+j] and pattern[j] != '@':
                break_ = True
                break
        if not break_:
            return i
    return -1


str_ = input()
pattern = input()
print(find_pattern(str_, pattern))
