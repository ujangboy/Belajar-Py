# CONTEXT MANAGERS

# 1. KONSEP CONTEXT MANAGER
print("==== 1. KONSEP ====")
print("Context manager mengelola resource (file, koneksi DB, lock).")
print("Otomatis setup (__enter__) dan cleanup (__exit__).")
print("Sintaks: with statement")

# 2. WITH STATEMENT DENGAN FILE (CONTOH UMUM)
print("\n==== 2. CONTOH DENGAN FILE ====")

with open("temp_ctx.txt", "w") as f:
    f.write("Data contoh\n")

print("File ditutup otomatis setelah keluar with.")

# 3. MEMBUAT CONTEXT MANAGER SENDIRI (CLASS)
print("\n==== 3. CUSTOM CONTEXT MANAGER (CLASS) ====")

class TimerCM:
    def __enter__(self):
        import time
        self.start = time.time()
        return self  # Nilai yang dikembalikan ke variabel 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Waktu: {self.elapsed:.4f} detik")
        return False  # Jangan tekan exception

with TimerCM() as timer:
    import time
    time.sleep(0.5)
    print("Kode di dalam with berjalan...")
print(f"Elapsed: {timer.elapsed:.4f}")

# 4. MEMBUAT CONTEXT MANAGER DENGAN DECORATOR
print("\n==== 4. CONTEXT MANAGER DENGAN DECORATOR ====")

from contextlib import contextmanager

@contextmanager
def timer_decorator():
    import time
    start = time.time()
    yield  # Pause di sini, kembalikan kontrol ke with block
    end = time.time()
    print(f"Waktu: {end - start:.4f} detik")

with timer_decorator():
    import time
    time.sleep(0.3)
    print("Kode di dalam with decorator...")

# 5. CONTOH LAIN: LOCK DENGAN THREADING
print("\n==== 5. CONTOH LOCK ====")

import threading

lock = threading.Lock()

with lock:
    print("Critical section, hanya satu thread yang bisa masuk")
    # Lakukan operasi thread-safe

# 6. CONTEXTLIB LAINNYA
print("\n==== 6. FITUR CONTEXTLIB ====")

# suppress: sembunyikan exception tertentu
from contextlib import suppress

with suppress(ZeroDivisionError):
    hasil = 10 / 0
    print("Ini tidak akan dicetak")

print("Program lanjut setelah suppress.")

# redirect_stdout: arahkan print ke file
from contextlib import redirect_stdout
with open("output_redirect.txt", "w") as f:
    with redirect_stdout(f):
        print("Ini masuk ke file, bukan ke layar")

with open("output_redirect.txt", "r") as f:
    print(f"Isi file redirect: {f.read().strip()}")

# ExitStack: kelola banyak context manager sekaligus
print("\n==== 7. EXITSTACK ====")

from contextlib import ExitStack

files = ["file1.txt", "file2.txt", "file3.txt"]
with ExitStack() as stack:
    opened = [stack.enter_context(open(f, "w")) for f in files]
    for i, f in enumerate(opened):
        f.write(f"Data {i}\n")
    print(f"Membuka {len(opened)} file sekaligus.")

# 8. BEST PRACTICE
print("\n==== 8. BEST PRACTICE ====")
print("- Gunakan with untuk resource yang perlu cleanup")
print("- Jangan gunakan try-finally manual jika bisa pakai with")
print("- Context manager bersihkan resource meskipun ada exception")
