guests = ["Kim Mingyu", "Yoon Jeonghan", "Hong Jisoo"]

print(f"Hello {guests[0]}, maukah makan siang dengan saya?")
print(f"Hello {guests[1]}, maukah makan siang dengan saya?")
print(f"Hello {guests[2]}, maukah makan siang dengan saya?")

# satu tamu tidak bisa hadir
print(f"\nsayang sekali, {guests[1]} ga bisa makan siang.")

# ganti tamu
guests[1] = "Kim Jennie"

# kirim undangan yang baru
print("\nNew invitations:")

print(f"Hello {guests[0]}, maukah makan siang dengan saya?")
print(f"Hello {guests[1]}, maukah makan siang dengan saya?")
print(f"Hello {guests[2]}, maukah makan siang dengan saya?")