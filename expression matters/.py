def expression_matter(a, b, c):
    results = [
        a + b + c,
        a * b * c,
        (a + b ) * c,
        a * (b + c),
        (a * b) + c
    ]
    return max(results)

print(expression_matter(1, 2, 3))