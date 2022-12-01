with open('input.txt', 'r') as fi:
    calories = [line.strip() for line in fi.readlines()]
    max_cal = 0
    elf_cal = 0
    for cal in calories:
        if cal == "":
            if elf_cal > max_cal:
                max_cal = elf_cal
            elf_cal = 0
            continue
        elf_cal += int(cal)
    print(max_cal)
