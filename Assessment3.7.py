"""
Assessment 3.7: Sorting Algorithms
Name: (typed by the user when the program runs)
Sorting method: Insertion Sort
"""

def build_unsorted_array(full_name):
    """Make an array of letters: skip symbols/spaces and discard duplicates."""
    letters = []
    for ch in full_name.upper():
        if not ch.isalpha():          # exclude symbols, spaces, digits
            continue
        if ch in letters:             # discard duplicate letters
            continue
        letters.append(ch)
    return letters


def insertion_sort(arr):
    """Sort a COPY of the array (A-Z) using Insertion Sort."""
    result = arr.copy()               # keep the unsorted array untouched
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]  # shift larger letter to the right
            j -= 1
        result[j + 1] = key            # insert key in its correct position
    return result


def main():
    full_name = input("Enter your full name: ")

    unsorted_array = build_unsorted_array(full_name)
    if not unsorted_array:
        print("No valid letters found. Please enter a name with letters.")
        return
    sorted_array = insertion_sort(unsorted_array)

    print()
    print("Full Name      :", full_name)
    print("Unsorted Array :", unsorted_array)
    print("Sorted Array   :", sorted_array)


if __name__ == "__main__":
    main()