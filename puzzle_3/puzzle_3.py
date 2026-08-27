from pathlib import Path

DIRECTORY_PATH: Path = Path(__file__).resolve().parent.parent
file_path = DIRECTORY_PATH / "puzzle_3" / "input.txt"

def puzzle_3_p1():
    with open(file_path,"r",encoding="UTF-8") as file:
        rows = file.readlines()

    battery_sum = 0
    for i in rows:
        bank = i.strip()

        prev,m1,m2 = 0,0,0
        for i in bank:
            battery = int(i)
            if battery > m1:
                prev = m1
                m1 = battery
                m2 = 0
            elif battery > m2:
                m2 = battery

        val = int(str(prev)+str(m1)) if m2 == 0 else int(str(m1)+str(m2))
        print(f"Largest 2-int combination: {val}")
        battery_sum += val
    return battery_sum

def puzzle_3_p2():
    with open(file_path,"r",encoding="UTF-8") as file:
        rows = file.readlines()

    battery_sum = 0
    for i in rows:
        bank = i.strip()
        pos_dict = {i:0 for i in range(1,13)}

        for i in bank:
            battery = int(i)
            for k,v in pos_dict:
                if v > battery:
                    pos_dict[k] = battery
        
    return battery_sum


if __name__ == "__main__":
    print(puzzle_3_p2())