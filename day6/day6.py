file_text = open(r"C:\Users\ihaidaoui\Desktop\AdvantOfCode\day6\day6.txt", "r").read()
markers = file_text.split("\n")


def get_marker(datastream: str, char_start_pos: int = 0, char_init_pos: int = 4):
    char_length = 4
    print(char_start_pos,char_init_pos)
    for char in datastream[char_start_pos:char_init_pos]:
        if datastream[char_start_pos:char_init_pos].count(char) > 1:
            return get_marker(datastream, char_start_pos + 1, char_init_pos + 1)

    return datastream[char_start_pos:char_init_pos], char_init_pos



print(get_marker(markers[0], 1968, 1982))
