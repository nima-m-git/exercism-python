def is_paired(input_string):
    openers = ['{', '[', '(']
    closers = ['}', ']', ')']

    opened = []
    closed = []
    
    for char in input_string:
        if char in openers:
            opened.append(char)
        if char in closers:
            if not opened:
                return False
            index = closers.index(char)
            reverse = openers[index]
            if reverse == opened[-1]:
                opened.pop()
            else:
                return False
    return not opened



