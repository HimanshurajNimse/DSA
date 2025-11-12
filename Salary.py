def selection_sort(salaries):
    for i in range(len(salaries)):
        min_index = i
        for j in range(i + 1, len(salaries)):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries

def bubble_sort(salaries):
    for i in range(len(salaries)):
        for j in range(len(salaries) - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries

def display_top_five(sorted_salaries):
    print("Top 5:", [f"${s:.2f}" for s in sorted_salaries[-5:][::-1]])

def main():
    salaries = [45000, 60000, 32000, 75000, 50000, 90000, 28000, 65000]
    print("Original salaries:", [f"${s:.2f}" for s in salaries])
    sel_sorted = selection_sort(salaries.copy())
    print("\nAfter Selection Sort:", [f"${s:.2f}" for s in sel_sorted])
    display_top_five(sel_sorted)
    bub_sorted = bubble_sort(salaries.copy())
    print("\nAfter Bubble Sort:", [f"${s:.2f}" for s in bub_sorted])
    display_top_five(bub_sorted)
main()