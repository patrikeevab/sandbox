names = input().split(",")
phones = input().split(",")

for i in range(len(names)):
    print(f"{names[i]}: {phones[i]}")
