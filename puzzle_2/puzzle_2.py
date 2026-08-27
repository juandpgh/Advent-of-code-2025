from pathlib import Path
DIRECTORY_PATH: Path = Path(__file__).resolve().parent.parent
file_path = DIRECTORY_PATH / "puzzle_3" / "input.txt"

# PART 1

def puzzle_2_p1() -> int:
    with open("input.txt") as file:
        row = file.readline()

    id_ranges = row.split(",")
    id_sum = 0
    for str_rg in id_ranges:
        lower,upper = str_rg.split("-")

        for id in range(int(lower),int(upper)+1):
            str_id = str(id)
            if str_id == str_id[:len(str_id)//2] * 2:
                print(f"WRONG ID: {id}")
                id_sum += id
                
    return id_sum

# PART 2

def divisors(n):
    return {i for i in range(1,n) if n % i == 0}

def puzzle_2_p2() -> int:
    """
    Could be optimized by using the periodic string (s+s)[1:-1] approach.
    Doesn't check every divisor, as one is enough to add to the sum.
    """
    with open("input.txt") as file:
        row = file.readline()

    id_ranges = row.split(",")
    id_sum = 0
    for str_rg in id_ranges:
        lower,upper = str_rg.split("-")

        for id in range(int(lower),int(upper)+1):
            str_id = str(id)
            div = divisors(len(str_id))
            for i in div:
                if str_id == str_id[:i] * (len(str_id)//i):
                    print(f"WRONG ID: {id}")
                    id_sum += id
                    break
                
    return id_sum

if __name__ == "__main__":
    print(puzzle_2_p1())
    print(puzzle_2_p2())