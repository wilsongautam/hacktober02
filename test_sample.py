# Favorite Colors


num_of_friends = int(input("How many friends do you want to ask? "))
favorite_colors = {}

for _ in range(num_of_friends):
    name = input("Enter friend's name: ")
    color = input(f"What is {name}'s favorite color? ").lower()
    favorite_colors[name] = color

color_count = {}
for color in favorite_colors.values():
    color_count[color] = color_count.get(color, 0) + 1

most_favorite_color = max(color_count, key=color_count.get)
print(f"The most favorite color among your friends is: {most_favorite_color}")
