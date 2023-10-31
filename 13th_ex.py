#FINDING A SHARED MOTIF



def longest_common_substring(strings):
    shortest_string = min(strings, key=len)
    max_length = len(shortest_string)
    longest_substring = ""
    for length in range(max_length, 0, -1):
        for start in range(max_length - length + 1):
            substring = shortest_string[start:start+length]
            if all(substring in string for string in strings):
                return substring
    return longest_substring

# Example usage
if __name__ == "__main__":
    
    strings = []
    current_string = ""
    with open("rosalind_lcsm-2.txt", "r") as file:
        for line in file:
            if line.startswith(">"):
                if current_string:
                    strings.append(current_string)
                current_string = ""
            else:
                current_string += line.strip()
        strings.append(current_string)  # Append the last string

    
    common_substring = longest_common_substring(strings)
    print("Longest common substring:", common_substring)