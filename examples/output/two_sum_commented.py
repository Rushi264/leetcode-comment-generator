def twoSum(nums, target):
    """
    Finds two numbers in a list that add up to a specific target value.

    Approach:
    Uses a hashmap (dictionary in Python) to store each number in the list and its index.
    For each number, it calculates the 'complement' needed to reach the target.
    If the complement is found in the hashmap, it means we've found the two numbers.

    Time Complexity: O(n), where n is the length of the input list 'nums'.  This is because, on average,
                     hashmap lookups (checking if 'complement' is in the hashmap) take O(1) time.  We iterate
                     through the list once.

    Space Complexity: O(n), where n is the length of the input list 'nums'.  In the worst case, we might store
                      all the numbers in the list in the hashmap.
    """
    hashmap = {} # Create an empty hashmap (dictionary) to store numbers and their indices.

    for i in range(len(nums)): # Iterate through the list of numbers using a 'for' loop.
        complement = target - nums[i] # Calculate the 'complement' needed to reach the target.  The complement is the value we need to find in the rest of the array to sum to the target.

        if complement in hashmap: # Check if the complement exists as a key in the hashmap.
            return [hashmap[complement], i] # If the complement is found, return a list containing the index of the complement (from the hashmap) and the current index 'i'.

        hashmap[nums[i]] = i # If the complement is not found, add the current number 'nums[i]' and its index 'i' to the hashmap. This allows us to find it later if it is the complement of a future number.