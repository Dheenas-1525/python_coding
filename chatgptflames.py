def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    
    # Remove common characters
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    
    count = len(name1) + len(name2)
    
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    
    pos = 0
    while len(flames) > 1:
        length = len(flames)
        steps = count - 1
        while steps > 0:
            pos += 1
            if pos >= length:
                pos = 0
            steps -= 1
        flames.pop(pos)
        if pos >= len(flames):
            pos = 0
    
    return flames[0]

# Example usage:
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
result = flames_game(name1, name2)
print(f"The relationship is: {result}")
