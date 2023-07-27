import time

my_compute_time = 5
opponent_compute_time = 55
opponents = 24
move_pairs = 30


def main(x):
    # Loops 30 times to simulate both players making a move
    for i in range(move_pairs):
        print(f"Thinking of making a move on board {x}")
        # We think for 5 seconds
        time.sleep(my_compute_time)
        print(f"Made a move on board {x}.")
        # The opponent thinks for 5 seconds.
        time.sleep(opponent_compute_time)
        print(f"Opponent made move on board {x}")
    print(f"Finished board {x}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    # Loops 24 times because we are playing 24 opponents.
    for j in range(opponents):
        main(j)
    print(f"Finished in {round(time.perf_counter() - start_time)} secs")

# The entire exhibition takes == 720 minutes.
# my use 5 secs
# opponent use 55 secs
# 1 move_pairs = 5 + 55 = 60 secs
# 30 move_pairs = 60 * 30 = 1800 secs = 1 opponent
# 1 opponents = 1800 secs
# 24 opponents = 1800*24 = 43200 secs
# 43200/60 = 720 minutes

# if opponents = 100
# 1 opponents = 1800 secs
# 100 opponents = 1800*100 = 180000 secs
# 180000/60 = 3000 minutes
