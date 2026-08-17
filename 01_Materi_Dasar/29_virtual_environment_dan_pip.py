# VIRTUAL ENVIRONMENT DAN PIP

# 1. APA ITU VIRTUAL ENVIRONMENT?
print("==== 1. VIRTUAL ENVIRONMENT ====")
print("Virtual Environment adalah lingkungan Python yang terisolasi.")
print("Setiap project bisa punya versi library yang berbeda tanpa konflik.")

# 2. CARA MEMBUAT VENV
print("\n==== 2. MEMBUAT VENV ====")
print("Command line (bisa di PowerShell atau CMD):")
print("  python -m venv venv")
print("  # Membuat folder 'venv' berisi environment terpisah")

# 3. MENGACTIFKAN VENV
print("\n==== 3. MENGACTIFKAN VENV ====")
print("Windows PowerShell:")
print("  .\\venv\\Scripts\\Activate.ps1")
print("\nWindows CMD:")
print("  venv\\Scripts\\activate.bat")
print("\nMac/Linux:")
print("  source venv/bin/activate")
print("\nSetelah aktif, prompt akan berubah menjadi (venv)")

# 4. PIP (PACKAGE MANAGER)
print("\n==== 4. PIP ====")

# Melihat versi pip
import subprocess
try:
    result = subprocess.run(["pip", "--version"], capture_output=True, text=True)
    print(f"Pip version: {result.stdout.strip()}")
except:
    print("Pip tidak terdeteksi.")

# Melihat package yang terinstall
print("\nPackage terinstall:")
result = subprocess.run(["pip", "list"], capture_output=True, text=True)
print(result.stdout)

# 5. INSTALL PACKAGE
print("\n==== 5. INSTALL PACKAGE ====")
print("Command:")
print("  pip install requests")
print("  pip install pandas==2.0.0")
print("  pip install numpy pandas matplotlib")

# 6. REQUIREMENTS.TXT
print("\n==== 6. REQUIREMENTS.TXT ====")
print("Menyimpan daftar dependencies untuk sharing.")
print("\nMembuat requirements.txt:")
print("  pip freeze > requirements.txt")
print("\nInstall dari requirements.txt:")
print("  pip install -r requirements.txt")

# Contoh isi requirements.txt:
contoh_req = """
requests==2.31.0
pandas==2.1.0
numpy==1.24.0
"""
print("\nContoh isi requirements.txt:")
print(contoh_req)

# 7. UNINSTALL DAN INFO
print("\n==== 7. PIP LAINNYA ====")
print("  pip uninstall requests")
print("  pip show requests")
print("  pip search requests  (sudah deprecated)")
print("  pip install --upgrade requests")

# 8. PIP LIST LENGKAP
print("\n==== 8. PIP LIST ====")
result = subprocess.run(["pip", "list", "--format=columns"], capture_output=True, text=True)
print(result.stdout)
