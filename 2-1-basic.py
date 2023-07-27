import asyncio
import time

# Function รายงานผลว่าเริ่มหรือเสร็จแล้ว
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

# Function สร้าง Task ทั้ง 2 Task 
async def main():
    task1 = asyncio.create_task(hello(1))
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await task1
    await task2

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec') # แสดงเวลาที่ใช้ในการ Computing

# Result
# Wed Jul 26 15:01:34 2023 hello 1 started
# Wed Jul 26 15:01:34 2023 hello 2 started
# Wed Jul 26 15:01:38 2023 hello 1 done
# Wed Jul 26 15:01:38 2023 hello 2 done
# Time: 4.01 sec
