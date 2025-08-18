def print_mirrored_pattern(start_char):
    # Convert character to ASCII and calculate number of rows
    start_ascii = ord(start_char.upper())
    n = start_ascii - ord('A') + 1

    for i in range(n):
        # Left side letters
        for j in range(n - i):
            print(chr(ord('A') + j), end=' ')
        
        # Spaces in the middle
        spaces = 2 * i - 1
        print('  ' * spaces, end='')

        # Right side letters
        for j in range(n - i - 1, -1, -1):
            if i == 0 and j == n - i - 1:
                continue  # Avoid printing the middle character twice in the first row
            print(chr(ord('A') + j), end=' ')
        
        print()

# 🚀 User input
user_char = input("Enter an uppercase character (A-Z): ").strip().upper()

# ✅ Validation
if len(user_char) == 1 and 'A' <= user_char <= 'Z':
    print_mirrored_pattern(user_char)
else:
    print("❌ Invalid input. Please enter a single uppercase letter from A to Z.")