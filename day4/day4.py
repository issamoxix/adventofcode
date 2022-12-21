file_text = open(r"C:\Users\ihaidaoui\Desktop\AdvantOfCode\day4\day4.txt", "r").read()
pairs = file_text.split("\n")

# Part 1
pair_dup = 0
for pair in pairs:
    p1, p2 = pair.split(",")
    p1_1, p1_2 = p1.split("-")
    p2_1, p2_2 = p2.split("-")
    p1_1, p1_2, p2_1, p2_2 = int(p1_1), int(p1_2), int(p2_1), int(p2_2)
    pair_1 = [i for i in range(int(p1_1), int(p1_2) + 1)]
    pair_2 = [i for i in range(int(p2_1), int(p2_2) + 1)]
    if len(pair_1) == len(pair_2):
        if p1_1 != p2_1:
            continue
        else:
            pair_dup += 1
    else:
        coli = list(set(pair_1) & set(pair_2))
        coli.sort()
        if coli == pair_1 or coli == pair_2:
            pair_dup += 1
print(pair_dup)
