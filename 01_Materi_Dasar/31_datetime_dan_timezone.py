# DATETIME DAN TIMEZONE

from datetime import datetime, date, time, timedelta
import time as time_mod

# 1. DATETIME DASAR
print("==== 1. DATETIME DASAR ====")

sekarang = datetime.now()
print(f"Sekarang: {sekarang}")
print(f"Tahun: {sekarang.year}")
print(f"Bulan: {sekarang.month}")
print(f"Hari: {sekarang.day}")
print(f"Jam: {sekarang.hour}")
print(f"Menit: {sekarang.minute}")
print(f"Detik: {sekarang.second}")
print(f"Microsecond: {sekarang.microsecond}")
print(f"Hari dalam minggu (0=Senin): {sekarang.weekday()}")

# 2. DATE DAN TIME TERPISAH
print("\n==== 2. DATE DAN TIME ====")

tanggal_hari_ini = date.today()
print(f"Tanggal hari ini: {tanggal_hari_ini}")
print(f"Format ISO: {tanggal_hari_ini.isoformat()}")

jam_sekarang = time(14, 30, 0)
print(f"Jam: {jam_sekarang}")
print(f"Format 24 jam: {jam_sekarang.strftime('%H:%M:%S')}")

# 3. MEMBUAT DATETIME CUSTOM
print("\n==== 3. MEMBUAT DATETIME CUSTOM ====")

ultah = datetime(2000, 1, 1, 0, 0, 0)
print(f"Ultah: {ultah}")
print(f"Hari ini: {sekarang}")
print(f"Umur (hari): {(sekarang - ultah).days}")

# 4. STRFTIME (STRING FORMAT TIME)
print("\n==== 4. STRFTIME ====")

print(f"Format Indonesia: {sekarang.strftime('%d %B %Y')}")
print(f"Format pendek: {sekarang.strftime('%d/%m/%Y')}")
print(f"Format panjang: {sekarang.strftime('%A, %d %B %Y %H:%M:%S')}")
print(f"Format ISO 8601: {sekarang.strftime('%Y-%m-%dT%H:%M:%S')}")

# Format codes:
# %Y = tahun 4 digit, %y = tahun 2 digit
# %m = bulan 01-12, %B = nama bulan, %b = nama bulan singkat
# %d = hari 01-31, %A = nama hari, %a = nama hari singkat
# %H = jam 00-23, %I = jam 01-12, %p = AM/PM
# %M = menit 00-59, %S = detik 00-59
# %f = microsecond

# 5. STRPTIME (STRING PARSE TIME)
print("\n==== 5. STRPTIME ====")

tanggal_str = "25-07-2026 14:30"
tanggal_obj = datetime.strptime(tanggal_str, "%d-%m-%Y %H:%M")
print(f"String ke datetime: {tanggal_obj}")
print(f"Tahun: {tanggal_obj.year}")

# 6. TIMEDELTA (SELISIH WAKTU)
print("\n==== 6. TIMEDELTA ====")

tgl1 = datetime(2026, 1, 1)
tgl2 = datetime(2026, 7, 25)
selisih = tgl2 - tgl1
print(f"Selisih hari: {selisih.days}")
print(f"Selisih total detik: {selisih.total_seconds()}")

# Tambah/kurang waktu
besok = sekarang + timedelta(days=1)
minggu_lalu = sekarang - timedelta(weeks=1)
print(f"Besok: {besok.date()}")
print(f"Minggu lalu: {minggu_lalu.date()}")

# 7. TIMESTAMP (UNIX TIMESTAMP)
print("\n==== 7. TIMESTAMP ====")

timestamp = sekarang.timestamp()
print(f"Timestamp sekarang: {timestamp}")
dari_timestamp = datetime.fromtimestamp(timestamp)
print(f"Dari timestamp: {dari_timestamp}")

# 8. SLEEP (JEDA)
print("\n==== 8. SLEEP ====")
print("Mulai hitung...")
time_mod.sleep(1)
print("Selesai 1 detik.")

# 9. TIMEZONE DENGAN PYTHON 3.9+ (ZONEINFO)
print("\n==== 9. TIMEZONE ====")

try:
    from zoneinfo import ZoneInfo

    # Jakarta
    tgl_jkt = datetime.now(ZoneInfo("Asia/Jakarta"))
    print(f"Jakarta: {tgl_jkt}")

    # Tokyo
    tgl_tky = datetime.now(ZoneInfo("Asia/Tokyo"))
    print(f"Tokyo: {tgl_tky}")

    # London
    tgl_lon = datetime.now(ZoneInfo("Europe/London"))
    print(f"London: {tgl_lon}")

    # UTC
    tgl_utc = datetime.now(ZoneInfo("UTC"))
    print(f"UTC: {tgl_utc}")
except ImportError:
    print("ZoneInfo tersedia di Python 3.9+. Gunakan pytz untuk versi lama.")
    print("Install: pip install pytz")
