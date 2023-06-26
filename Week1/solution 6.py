def print_partial_string(string, start, end):
    if start < 0 or end > len(string) - 1 or start > end:
        print("Invalid start or end position.")
        return

    partial_string = string[start:end+1]
    print("Partial String:", partial_string)


user_input = input("Enter a string: ")
start_pos = int(input("Enter the start position: "))
end_pos = int(input("Enter the end position: "))

print_partial_string(user_input, start_pos, end_pos)
