# 1
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @gaybernhardt #rstats'''
cleantwet = text.replace('https://t.co/lbwej0pxOd cc: @gaybernhardt #rstats' '')
print(cleantwet)

# №2


stuff = 'Exercisesnumber 1, 12, 13, and 345 are imporant 456'

key = re.findall(r'\b\d{3}\b', stuff)

print(key)

# yjvth 3

color = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fgw3d', '#8B0000']
patter = r'^#[0-9A-Fa-f]{6}$'
valid_colors = [c for c in color if (patter, c)]
print(valid_colors)

 # 4 какойто мутный,не понял
# 5 nj;t