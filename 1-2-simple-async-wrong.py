import asyncio
import time

# Function หาค่าเวลาที่ใช้ในการ Computing
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

# Function ที่ใช้ว่าเป็น Task อะไรและแสดงเวลาที่ใช้ในการ Computing
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')

        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()

# Function กำหนดชนิด Task และจำนวน Task
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2f} sec')

# Task A จะ run ก่อน Task B
# Result
# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3
 
# Task B: Computing 0+1
# Time: 2.02
# Task B: Computing 1+2
# Time: 3.02
# Task B: Computing 3+3
# Time: 4.03
# Task B: Sum = 6

# Time: 5.04 sec
