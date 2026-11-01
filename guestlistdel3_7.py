guests = [
    "Mingu",
    "Baskara",
    "jeonghan",
    "aries",
    "lisa",
    "songkang"
]

# kursinya ga cukup, jadi cuma bisa undang 2 orang
print("sorry, cuma bisa ngundang 2 orang.")

# hapus tamu yang tidak bisa hadir
removed_guest = guests.pop()
print(f"Sorry {removed_guest}, aku ga bisa undang kamu.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, aku ga bisa undang kamu.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, aku ga bisa undang kamu.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, aku ga bisa undang kamu.")

# kirim undangan kepada tamu yang tersisa
print("\nundangan:")

print(f"Hello {guests[0]}, kamu masih diundang makan malam.")
print(f"Hello {guests[1]}, kamu masih diundang makan malam.")

# hapus tamu yang tidak bisa hadir
del guests[0]

# Display the empty list
print("\nFinal guest list:")
print(guests)