# ARGPARSE DAN CLI (COMMAND LINE INTERFACE)

import argparse
import sys

# 1. DASAR ARGPARSE
print("==== 1. ARGPARSE DASAR ====")

parser = argparse.ArgumentParser(
    description="Program contoh argparsing",
    epilog="Contoh: python script.py --nama Andi --umur 20"
)

parser.add_argument("--nama", type=str, required=True, help="Nama pengguna")
parser.add_argument("--umur", type=int, default=18, help="Umur pengguna")
parser.add_argument("--kota", type=str, default="Jakarta", help="Kota asal")

# Parse args
args = parser.parse_args()  # Di CLI, ini baca sys.argv
print(f"Nama: {args.nama}")
print(f"Umur: {args.umur}")
print(f"Kota: {args.kota}")

# 2. JENIS ARGUMEN
print("\n==== 2. JENIS ARGUMEN ====")

parser2 = argparse.ArgumentParser()
parser2.add_argument("input_file", type=str, help="File input yang akan diproses")
parser2.add_argument("-o", "--output", type=str, default="hasil.txt", help="File output")
parser2.add_argument("-v", "--verbose", action="store_true", help="Mode verbose")
parser2.add_argument("-n", "--jumlah", type=int, default=1, help="Jumlah perulangan")
parser2.add_argument("--tipe", choices=["text", "json", "csv"], default="text")

# Simulasi parse (karena kita di dalam Python script, bukan CLI)
test_args = ["data_input.txt", "-o", "output.csv", "-v", "-n", "3", "--tipe", "json"]
args2 = parser2.parse_args(test_args)

print(f"Input: {args2.input_file}")
print(f"Output: {args2.output}")
print(f"Verbose: {args2.verbose}")
print(f"Jumlah: {args2.jumlah}")
print(f"Tipe: {args2.tipe}")

# 3. ARGUMENT TYPES
print("\n==== 3. TIPE ARGUMENT ====")

parser3 = argparse.ArgumentParser()
parser3.add_argument("--angka", type=int)
parser3.add_argument("--float", type=float)
parser3.add_argument("--bool", type=lambda x: x.lower() in ["true", "1", "ya"])
parser3.add_argument("--list", type=lambda s: s.split(","))

args3 = parser3.parse_args(["--angka", "10", "--float", "3.14", "--bool", "true", "--list", "a,b,c"])
print(f"Int: {args3.angka}, Float: {args3.float}")
print(f"Bool: {args3.bool}, List: {args3.list}")

# 4. SUBCOMMANDS (SEPERTI GIT)
print("\n==== 4. SUBCOMMANDS ====")

parser4 = argparse.ArgumentParser()
subparsers = parser4.add_subparsers(dest="command", help="Sub-commands")

# Subcommand: add
parser_add = subparsers.add_parser("add", help="Tambah item")
parser_add.add_argument("item", type=str, help="Nama item")
parser_add.add_argument("--jumlah", type=int, default=1)

# Subcommand: remove
parser_remove = subparsers.add_parser("remove", help="Hapus item")
parser_remove.add_argument("item", type=str)

# Subcommand: list
parser_list = subparsers.add_parser("list", help="Tampilkan semua item")

test_args4 = ["add", "Buku", "--jumlah", "2"]
args4 = parser4.parse_args(test_args4)

print(f"Command: {args4.command}")
if args4.command == "add":
    print(f"Menambah '{args4.item}' sebanyak {args4.jumlah}")
elif args4.command == "remove":
    print(f"Menghapus '{args4.item}'")
elif args4.command == "list":
    print("Menampilkan semua item")

# 5. CUSTOM HELP DAN ERROR
print("\n==== 5. HELP DAN ERROR ====")

parser5 = argparse.ArgumentParser(add_help=False)
parser5.add_argument("--nama", required=True, help="Nama pengguna")
parser5.add_argument("--usia", type=int, help="Usia pengguna (harus positif)", choices=range(0, 150))

try:
    args5 = parser5.parse_args(["--nama", "Andi", "--usia", "25"])
    print(f"Parsing berhasil: {args5}")
except SystemExit:
    print("Error parsing arguments.")

# 6. MENGUBAH HELP DEFAULT
print("\n==== 6. HELP FORMAT ====")

parser6 = argparse.ArgumentParser(
    prog="belajar.py",
    description="Script untuk belajar Python dasar",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Contoh penggunaan:
  python belajar.py --nama Andi --umur 20
  python belajar.py add Laptop
  python belajar.py list
    """
)
parser6.add_argument("--nama", type=str, help="Nama pengguna")
parser6.add_argument("--umur", type=int, help="Umur pengguna")

# print(parser6.format_help())  # Uncomment untuk melihat help format

# 7. BEST PRACTICE
print("\n==== 7. BEST PRACTICE ====")
print("- Gunakan -- untuk optional, tanpa untuk positional")
print("- Berikan help yang jelas untuk setiap argument")
print("- Gunakan type untuk casting otomatis")
print("- Gunakan choices untuk membatasi nilai")
print("- Gunakan required=True untuk argument wajib")
