from classes.Disk import Disk


class Tower:
    list_of_disks: list[Disk]

    def __init__(self, list_of_disks, x_pos):
        self.list_of_disks = list_of_disks
        self.x_pos = x_pos

    # returns the tower with the disk that was added
    def add_disk(self, disk: Disk):
        self.list_of_disks.append(disk)

    # returns the tower without the disk that was removed
    def remove_disk(self):
        return self.list_of_disks.pop()

    # returns the amount of disks on each tower
    def get_amount_of_disks(self):
        return len(self.list_of_disks)

    # draws each tower with it's disks on the screen
    def add_tower_to_screen(self):
        for i, disk in enumerate(self.list_of_disks):
            disk.draw_disk(self.x_pos, i)
