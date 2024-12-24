def find_the_longest_word(input_string):

    words = input_string.split()

    if not words:
        return None

    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

if __name__ == "__main__":
    test_case = {
        "input_string": "The quick brown fox jumps over the lazy dog",
        "input_string2": "Testing if this dang thing works",
        "input_string3": "Hopefully this code does the job were looking for",
        "input_string4": "",
        "input_string5": "Hello World, it is good to finaly be here"
    }

    for input_string in test_case.values():
        results = find_the_longest_word(input_string)

    expected_results = expected_results = {
    "input_string": "quick",
    "input_string2": "Testing",
    "input_string3": "Hopefully",
    "input_string4": None,
    "input_string5": "World,"
    }

    for key, input_string in test_case.items():
        results = find_the_longest_word(input_string)

        if results == expected_results[key]:
            print("Pass")
        else:
            print("Fail")