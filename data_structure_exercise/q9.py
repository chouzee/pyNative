speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
add_item = []
for i in speed.values():
    if i not in add_item:
        add_item.append(i)
print(add_item)
