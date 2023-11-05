# function definition
def tower_of_hanoi(num_disks: int, source_tower: str, destination_tower: str, auxiliary_tower: str):
    """
    Simulates famous 'tower of hanoi' algorithm.

    Parameters:
    num_disks (int): number of disks in source_tower
    source_tower (str): label for source tower, e.g. 'S'
    destination_tower (str): label for destination tower e.g. 'D'
    auxiliary_tower (str): label for auxiliary tower e.g. 'A'
    """
    if num_disks == 1:
        print(f"disk-{num_disks}: {source_tower} -> {destination_tower}")
        return
    tower_of_hanoi(num_disks-1, source_tower,
                    auxiliary_tower, destination_tower)
    print(f"disk-{num_disks}: {source_tower} -> {destination_tower}")
    tower_of_hanoi(num_disks-1, auxiliary_tower,
                    destination_tower, source_tower)


if __name__ == "__main__":
    # Demonstration
    num_disks = int(input("Enter number of disks (greater than zero): "))
    if (num_disks > 0):
        tower_of_hanoi(num_disks=num_disks, source_tower='S',
                        destination_tower='D', auxiliary_tower='A')
        print(f"Number of steps taken: {2**num_disks - 1}")
        