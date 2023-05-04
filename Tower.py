from Disk import Disk


class Tower:
    def __init__(self, list_of_disks, x_pos):
        self.list_of_disks = list_of_disks
        self.x_pos = x_pos

    def add_disk(self, disk: Disk):
        self.list_of_disks.append(disk)

    def remove_disk(self):
        return self.list_of_disks.pop(-1)

    def get_amount_of_disks(self):
        return len(self.list_of_disks)

    def add_tower_to_screen(self):
        for i in range(len(self.list_of_disks)):
            Disk.draw_disk(self.list_of_disks[len(self.list_of_disks) - 1 - i], self.x_pos, i)
