# 1-1-Simple-sync.py
import time

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
    # Result
    # 2. Time: 2.55
    
    # 4. Time: 5.93

    # 7. Time: 13.31

    # 9. time: 17.51

    # 11. time: 21.58

# แสดงผล Task แต่ละครั้ง
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        # Result
        # 1. Task A: Computing 0+1

        # 3. Task A: Computing 1+2

        # 6. Task B: Computing 0+1

        # 8. Task B: Computing 1+2

        # 10. Task B: Computing 3+3

        sleep()
        total += number

    # แสดงจำนวน Task ทั้งหมดของ A และ B รวมกัน
    print(f'Task {name}: Sum = {total}\n')
    # Result
    # 5. Task A: Sum = 3
  
    # 12. Task B: Sum = 6

start = time.time()

# กำหนดชนิด Task และจำนวน Task
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3]),
]
end = time.time()
print(f'Time: {end-start:.2f} sec')

# Result 
# 13. Time: 28.26 sec
