# ----------------------------------------------------------
# CodeChef Problem: CARVANS
# Concept: Array traversal and speed comparison
# ----------------------------------------------------------
 
# Input: Number of test cases
t = int(input("Enter number of test cases: "))
 
for _ in range(t):
    # Input: Number of cars
    n = int(input("\nEnter number of cars: "))
 
    # Input: Speeds of each car separated by spaces
    speeds = list(map(int, input("Enter speeds of cars: ").split()))
 
    # If speeds entered are LESS than number of cars → ERROR
    if len(speeds) != n:
        print("⚠️ Please enter exactly", n, "speeds!")
        continue  # skip this test case
 
    count = 1  # First car always maintains speed
 
    for i in range(1, n):
        if speeds[i] > speeds[i - 1]:
            speeds[i] = speeds[i - 1]
        else:
            count += 1
 
    print("✅ Number of cars maintaining speed:", count)
    