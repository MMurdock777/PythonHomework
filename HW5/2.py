def move(disks: int, origin, dest):
    if disks == 0:
        return
    else:
        tower_list = [1,2,3]
        tower_list.remove(origin)
        tower_list.remove(dest)
        free = tower_list[0]
        move(disks - 1, origin, free)
        print(f"Передвинуть диск {disks} со стержня {origin} на стержень {dest}")
        move(disks - 1, free, dest)


move(5, 1, 3)
