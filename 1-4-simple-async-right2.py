import asyncio
import time

# Function หาค่าเวลาที่ใช้ในการ Computing
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

# Function ที่ใช้ว่าเป็น Task อะไรและแสดงเวลาที่ใช้ในการ Computing
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

# Function กำหนดชนิด Task และจำนวน Task
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')

# Task A กับ B run พร้อมกันแต่ Task B มีจำนวน Task มากกว่าจึงทำเสร็จทีหลัง Task A

# Result
# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.02
# Task B: Computing 1+2
# Time: 1.02
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.03
# Task B: Sum = 6

# Time: 3.04 sec
