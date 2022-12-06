def part1(data):
    count = 0
    for area in data:
        first_start, first_end = [int(num) for num in area[0].split('-')]
        secon_start, secon_end = [int(num) for num in area[1].split('-')]
        if first_start<=secon_start and secon_end <= first_end: count += 1
        elif secon_start<=first_start and first_end <= secon_end: count += 1
    return count

def part2(data):
    count = 0
    for area in data:
        first_start, first_end = [int(num) for num in area[0].split('-')]
        secon_start, secon_end = [int(num) for num in area[1].split('-')]
        a = first_start <= secon_start <= first_end
        b = secon_start <= first_end <= secon_end
        c = first_start <= secon_end <= first_end
        d = secon_start <= first_start <= secon_end
        if any([a,b,c,d]): count += 1
    return count