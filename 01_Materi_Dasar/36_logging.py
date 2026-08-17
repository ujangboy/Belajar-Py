# LOGGING

import logging

# 1. BASIC CONFIG
print("==== 1. BASIC LOGGING ====")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.debug("Pesan debug untuk debugging")
logging.info("Pesan info umum")
logging.warning("Pesan warning (perhatian)")
logging.error("Pesan error (masalah)")
logging.critical("Pesan critical (kritis!)")

# 2. LOGGER OBJECT (PRAKTEK PRODUCTION)
print("\n==== 2. LOGGER OBJECT ====")

logger = logging.getLogger("aplikasi_ku")
logger.setLevel(logging.INFO)

# Handler: Console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)

# Handler: File
file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setLevel(logging.WARNING)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Tambahkan handler ke logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Aplikasi dimulai...")
logger.warning("Memori usage tinggi")
logger.error("Database connection failed")

# 3. LOG LEVELS
print("\n==== 3. LOG LEVELS ====")
print(f"DEBUG = {logging.DEBUG} (10)")
print(f"INFO = {logging.INFO} (20)")
print(f"WARNING = {logging.WARNING} (30)")
print(f"ERROR = {logging.ERROR} (40)")
print(f"CRITICAL = {logging.CRITICAL} (50)")

# 4. FORMATTER CUSTOM
print("\n==== 4. FORMATTER ====")

custom_logger = logging.getLogger("custom")
custom_logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    "[%(levelname)s] %(message)s"
))
custom_logger.addHandler(handler)

custom_logger.info("Format custom berhasil.")
custom_logger.warning("Perhatian!")

# 5. LOGGING KE FILE
print("\n==== 5. FILE HANDLER ====")

file_logger = logging.getLogger("file_logger")
file_logger.setLevel(logging.INFO)
fh = logging.FileHandler("log_pembelajaran.log", encoding="utf-8")
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
file_logger.addHandler(fh)

file_logger.info("Mencatat progres belajar Python...")
file_logger.warning("Kesalahan sintaks di baris 10")
file_logger.error("Module tidak ditemukan")

print("Cek file 'log_pembelajaran.log' untuk melihat hasil.")

# 6. EXCEPTION LOGGING
print("\n==== 6. EXCEPTION LOGGING ====")

try:
    hasil = 10 / 0
except ZeroDivisionError:
    logger.exception("Terjadi exception (akan include traceback)")

# 7. PROPAGASI LOG
print("\n==== 7. PROPAGASI ====")

root_logger = logging.getLogger()
root_logger.setLevel(logging.WARNING)
print(f"Root level: {root_logger.level}")
print("Logger anak bisa override levelnya masing-masing.")

# 8. BEST PRACTICE
print("\n==== 8. BEST PRACTICE ====")
print("- Gunakan logger object, bukan logging module langsung")
print("- Set level yang sesuai (INFO untuk dev, WARNING untuk prod)")
print("- Gunakan RotatingFileHandler untuk file besar")
print("- Jangan log password atau data sensitif")
