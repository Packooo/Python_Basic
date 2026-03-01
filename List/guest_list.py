##Mengundang nama untuk dinner
name = ["Mitori", "Kotomi", "Ibu"]
message = f"Hallo {name[0]}, Yuk kita makan bareng"
print(message)
message = f"Hallo {name[1]}, Yuk kita makan bareng"
print(message)
message = f"Hallo {name[2]}, Yuk kita makan bareng"
print(message)

##Menambahkan nama baru
name = ["Mitori", "Kotomi", "Ibu"]
new_name = "Adik"
name[2] = new_name
print(name)
message = f"Hallo {name[0]}, Yuk kita makan bareng"
print(message)
message = f"Hallo {name[1]}, Yuk kita makan bareng"
print(message)
message = f"Hallo {name[2]}, Yuk kita makan bareng"
print(message)

##Lebih tambah tamu
name.insert(0, "Mama")
print(name)
name.insert(2, "Ayah")
print(name)
name.append("Kakak")
print(name)

##mengurangi tamu
message = f"Maaf tidak bisa makan bareng"
print(f"{message} {name[-1]}")
print(f"{message} {name[-2]}")
print(f"{message} {name[-3]}")
print(f"{message} {name[-4]}")
name.pop()
name.pop()
name.pop()
name.pop()
print(name)
print(f"Hallo {name[0]}, Yuk kita makan bareng")
print(f"Hallo {name[1]}, Yuk kita makan bareng")


##Menghapus semua tamu
del name[0]
del name[0]
print(name)