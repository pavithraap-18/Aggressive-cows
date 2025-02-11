def is_possible(stalls, k, mid):
    cows_placed = 1  # First cow is placed at the first stall
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= mid:
            cows_placed += 1
            last_position = stalls[i]

            if cows_placed == k:
                return True
    return False


def aggressive_cows(stalls, k):
    stalls.sort()  # Sort the stall positions

    low, high = 1, stalls[-1] - stalls[0]
    best_dist = 0

    while low <= high:
        mid = (low + high) // 2
        if is_possible(stalls, k, mid):
            best_dist = mid  # Update best answer
            low = mid + 1  # Try to maximize the minimum distance
        else:
            high = mid - 1  # Reduce search space

    return best_dist


# Example Usage
stalls = [1, 2, 8, 4, 9]
k = 3
print(aggressive_cows(stalls, k))  # Output: 3
