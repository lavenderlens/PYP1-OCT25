'''found in manual P 127 
0r 8-19
Or screenshot in this folder
'''

table = ["Bath", "Derby", "Gloucester", "Lancaster", "Newcastle", "Plymouth", "Salford", "Wakefield"]
table.remove("Newcastle")
table.insert(2, "Newcastle")# changed to position 2 (was 3) to match final output
print(table)
table.remove("Derby")
table.insert(3, "Derby")
print(table)
table.remove("Salford")
print(table)
table.append("Canterbury")
print(table)
table[table.index("Plymouth")] = "York"
print(table)
to_play_in_europe = table[:2]
print(to_play_in_europe)
if "Newcastle" in to_play_in_europe:
    print("Newcastle to play in Europe")
for team in table:
    print(team)
 