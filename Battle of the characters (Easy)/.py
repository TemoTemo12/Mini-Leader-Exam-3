def battle(x, y):
    power1 = sum(ord(char) - ord('A') +  1 for char in x)
    power2 = sum(ord(char) - ord('A') +  1 for char in y)
    
    if power1 > power2:
        return x
    elif power2 > power1:
        return y
    else:
        return "Tie!"
    
    pass