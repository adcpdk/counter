#get_fun.py
sentence = "The quick brown fox jumped over the lazy dog."
characters = {}

for character in sentence:
    characters[character] = characters.get(character, 0) + 1

print(characters)
#orgs = [adk, mega, sputnik]
fhand = open('glines.js','w')
fhand.write("gline = [ ['Month'")
for org in orgs:
    fhand.write(",'"+org+"'")
fhand.write("]")

# for month in months[1:-1]:
for month in months:
    fhand.write(",\n['"+month+"'")
    for org in orgs:
        key = (month, org)
        val = counts.get(key,0)
        fhand.write(","+str(val))
    fhand.write("]");

fhand.write("\n];\n")
