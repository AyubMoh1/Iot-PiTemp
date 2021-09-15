with open("log.txt", "r") as file:
    for i in range(0, 20):
        file.write(str(i))

with open("data.bin", "wb") as file:
    for i in range(0, 20):
        file.write(i.to_bytes(2, byteorder="little"))