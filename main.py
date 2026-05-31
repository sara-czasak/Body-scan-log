# TODO 1 : Determine exact JSON structure needed to store data
# TODO 2: Ask user about body scan info
# TODO 3: Check info correct
# TODO 4: LLM layer: pattern recognition, early crisis warning signs


print("Welcome to the Body Scan Log! Pick your option:")
print("""
--- OPTIONS ---
1. Log body scan data
2. View body scan data
3. Analyze body scan data

PLEASE TYPE 1, 2 OR 3 TO SELECT
""")

option = int(input())
if option == 1:
    print("Log body scan data")
elif option == 2:
    print("View body scan data")
elif option == 3:
    print("Analyze body scan data")
else:
    print("Please enter a valid option")
