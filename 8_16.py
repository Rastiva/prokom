# 1. Mengimpor seluruh modul
import pesan

pesan.tampilkan_pesan()


# 2. Mengimpor fungsi secara langsung
from pesan import tampilkan_pesan

tampilkan_pesan()


# 3. Mengimpor fungsi dengan nama alias
from pesan import tampilkan_pesan as fn

fn()


# 4. Mengimpor modul dengan nama alias
import pesan as mn

mn.tampilkan_pesan()


# 5. Mengimpor semua fungsi dari modul
from pesan import *

tampilkan_pesan()