with open('input.txt', 'r') as fi:
    calories = [line.strip() for line in fi.readlines()]
    elf_cnt = 0
    max_cal = 0
    elf_cal = 0
    max_elf = -1
    elves_cal = []
    for cal in calories:
        if cal == "":
            elf_cnt += 1
            if elf_cal > max_cal:
                max_cal = elf_cal
                max_elf = elf_cnt
            elves_cal.append(elf_cal)
            elf_cal = 0
            continue
        elf_cal += int(cal)
