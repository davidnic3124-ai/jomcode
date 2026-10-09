def add_title(title, titles=None):
     if titles is None:
        titles = []
     return [*titles,title]

print(add_title("Python"))
print(add_title("SQL"))
print(add_title("React", ["Python"]))
