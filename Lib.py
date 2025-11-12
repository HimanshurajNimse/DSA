def compute_average_borrow(members):
    if len(members) == 0:
        return 0
    return sum(members) / len(members)

def find_book_extremes(books):
    if len(books) == 0:
        return None, None
    
    # find book with max and min borrow count
    max_book = None
    min_book = None
    max_count = -1
    min_count = float('inf')

    for book, count in books.items():
        if count > max_count:
            max_count = count
            max_book = book
        if count < min_count:
            min_count = count
            min_book = book

    return max_book, min_book

def count_zero_borrowers(members):
    count = 0
    for m in members:
        if m == 0:
            count += 1
    return count

def most_frequent_borrowed(books):
    if len(books) == 0:
        return []

    # Count frequencies of borrow values
    freq = {}
    for count in books.values():
        freq[count] = freq.get(count, 0) + 1

    # find the borrow count that occurs the most
    max_freq = 0
    for f in freq.values():
        if f > max_freq:
            max_freq = f

    # return all books having that count
    result = []
    for book, count in books.items():
        if freq[count] == max_freq:
            result.append(book)

    return result

def display_statistics(members_dict, books):
    members = list(members_dict.values())

    avg = compute_average_borrow(members)
    max_book, min_book = find_book_extremes(books)
    zero_borrowers = count_zero_borrowers(members)
    most_freq_books = most_frequent_borrowed(books)

    print(f"Average books borrowed per member: {avg:.2f}")
    print(f"Most borrowed book: {max_book}")
    print(f"Least borrowed book: {min_book}")
    print(f"Members with 0 books borrowed: {zero_borrowers}")
    print(f"Books borrowed with most frequent borrow count: {most_freq_books}")

# Example Data
members = {
    "vinay": 3,
    "saif": 0,
    "shubham": 5,
    "alok": 2,
    "ansh": 4,
    "abhishek": 2
}

books = {
    "harry potter": 12,
    "the alchemist": 9,
    "inferro": 8,
    "1984": 9,
    "the great gandhi": 14,
    "moby dick": 6
}

display_statistics(members, books)