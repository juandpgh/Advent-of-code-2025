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

def puzzle_3_p2(len_str: int):
    with open(file_path,"r",encoding="UTF-8") as file:
        rows = file.readlines()

    battery_sum = 0
    #monotonic stack approach
    for i in rows:
        bank = i.strip()    

        stack = []
        to_remove = len(bank)-len_str 
        #print(len(bank),len_str,len(bank)-len_str)
        for idx,i in enumerate(bank):
            # print(f"[BANK (len = {len(bank)})]: {bank}")
            # print(f"                  "+ (idx+1)*" "+ "^")
            # print(f"[STACK (len = {len(stack)})]: {stack}")
            battery = int(i)
            while (stack and int(stack[-1]) < battery and to_remove>0):
            
                el = stack.pop() 
                to_remove -= 1
                #print(f"Popped {el}, {to_remove} elements left to remove\n")
            
            stack.append(i)
        hj = ''.join(stack[:len_str])
        #print(f"Battery is {hj}\n########\n")
        battery_sum += int(hj)
    return battery_sum


if __name__ == "__main__":
    print(puzzle_3_p1())
    print(puzzle_3_p2(12))