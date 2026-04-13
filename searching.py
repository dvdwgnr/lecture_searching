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
        "positions": positions,
        "count": len(positions)
    }

def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    target_number = 5
    result = linear_search(sequential_data, target_number)

    print("Data:", sequential_data)
    print("Hledané číslo:", target_number)
    print("Výsledek:", result)

if __name__ == "__main__":
    main()