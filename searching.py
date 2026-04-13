import json


def read_data(file_name, field):
    allowed_fields = ['unordered_numbers', 'ordered_numbers', 'dna_sequence']
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    if field not in allowed_fields:
        return None
    with open(file_name, 'r') as f:
        data = json.load(f)
    return data.get(field)


def linear_search(sequence, target):
    positions = []
    for i, value in enumerate(sequence):
        if value == target:
            positions.append(i)
    return {
        "pozice": positions,
        "pocet": len(positions)
    }

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    target_number = 0
    result = linear_search(sequential_data, target_number)

    print("Data:", sequential_data)
    print("Naše číslo:", target_number)
    print("celkem:", result)

if __name__ == "__main__":
    main()



def binary_search(numbers, hledane):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        prostredek = (left + right) // 2
        if numbers[prostredek] == hledane:
            return prostredek
        elif numbers[prostredek] < hledane:
            left = prostredek + 1
        else:
            right = prostredek - 1
    return None

def main():
    with open("sequential.json", "r") as file:
        data = json.load(file)
    numbers = data["ordered_numbers"]
    hledane = 2
    result = binary_search(numbers, hledane)
    if result is not None:
        print(f"Číslo {hledane} je na {result}. pozici v seznamu.")
    else:
        print(f"Číslo {hledane} není v seznamu :(  .")

if __name__ == "__main__":
    main()