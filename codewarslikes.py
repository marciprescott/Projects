# Function to generate display text based on the names of people who liked an item
def likes(names):
    # Check if the list is empty
    # If empty, return "no one likes this"
    if not names:
        return "No one likes this"
    # Check if the list has one name
    # If one name, return "{name} likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    # Check if the list has two names
    # If two names, return "{name1} and {name2} like this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    # Check if the list has three or more names
    # If three or more names, return "{name1}, {name2} and {others_count}
    # others like this"
    if len(names) == 3:

        return f"{names[0]}, {names[1]}, and {names[2]} like this"
    if len(names) > 3:
        others_count = len(names) - 2
        return f"{names[0]}, {names[1]}, and {others_count} others like this"


names = ["Eric", "Marci", "Marlowe", "Steve", "Judy"]
print(likes(names))
