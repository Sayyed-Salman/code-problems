

class ContainsDuplicate:

    def __init__(self, nums: list) -> None:
        self.nums = nums

    def check_duplicate(self) -> bool:
        """
        Checks for duplicate returns true if found.
        """
        hashset = set()

        for n in self.nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    def remove_duplicate(self) -> list:
        """
        Removes duplicate 
        """
        hashset = set(self.nums)
        return list(hashset)


l = [1, 5, 3, 8, 0, 9, 1]
check_duplicate = ContainsDuplicate(l)
result = check_duplicate.check_for_duplicate()

if result:
    print("Duplicate Found!")
    removed_duplicates = check_duplicate.remove_duplicate()
    print(removed_duplicates)

else:
    print("No duplicates found")
    print(check_duplicate.nums)
