def vacuum_cleaner(room):
    for i in range(2):
        for j in range(2):
            if room[i][j] == 1:
                print(f"Cleaning dirt at ({i}, {j})")
                room[i][j] = 0  # Clean the dirt
    print("Room is clean!")

room = [[1, 0], [0, 1]]  # 1 represents dirt, 0 is clean
vacuum_cleaner(room)
