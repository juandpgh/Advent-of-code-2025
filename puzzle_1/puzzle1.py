import math

## PART 1

with open("input.txt") as file:
    rows = file.readlines()
    base_pos = 50
    password = 0
    for row in rows:
        direction, movement = row[0:1], int(row[1::])

        if direction == "R":
            base_pos += movement
        else:
            base_pos -= movement

        base_pos = base_pos % 100

        if base_pos == 0:
            password += 1

    print(password)

## PART 2
with open("input.txt") as file:
    rows = file.readlines()
    base_pos = 50
    password = 0
    for row in rows:
        direction,movement = row[0:1],int(row[1::])

        if movement >= 100:
            password += math.trunc(movement / 100)
            movement = movement % 100

        if direction == "R":
            base_pos += movement
            if base_pos >= 100:
                #count when it lands on 0 as well
                password +=1
        else:
            former = base_pos
            base_pos -= movement
            if base_pos <= 0 and former != 0:
                #make sure movements from 0 to the left aren't counted
                password +=1
        base_pos = base_pos % 100
    print(password)









