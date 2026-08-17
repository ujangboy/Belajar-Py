# JSON HANDLING

import json

# 1. APA ITU JSON?
print("==== 1. JSON DASAR ====")
print("JSON (JavaScript Object Notation) adalah format pertukaran data.")
print("Python: dict/list  ->  JSON: object/array")

# 2. DICTTONARY KE JSON (SERIALIZATION)
print("\n==== 2. DICTTONARY KE JSON ====")

data = {
    "nama": "Andi",
    "umur": 20,
    "kota": "Jakarta",
    "hobi": ["membaca", "coding", "game"],
    "nilai": {"math": 90, "english": 85},
    "aktif": True,
    "tagihan": None
}

json_string = json.dumps(data)
print(f"JSON string:\n{json_string}")

# Pretty print (indentasi)
json_pretty = json.dumps(data, indent=2)
print(f"\nJSON pretty:\n{json_pretty}")

# 3. JSON KE PYTHON (DESERIALIZATION)
print("\n==== 3. JSON KE PYTHON ====")

json_input = '{"nama": "Budi", "umur": 25, "kota": "Bandung"}'
python_obj = json.loads(json_input)
print(f"Tipe: {type(python_obj)}")
print(f"Nama: {python_obj['nama']}")
print(f"Umur: {python_obj['umur']}")

# 4. BACA/TULIS FILE JSON
print("\n==== 4. FILE JSON ====")

# Tulis ke file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("File data.json berhasil ditulis.")

# Baca dari file
with open("data.json", "r", encoding="utf-8") as f:
    data_dari_file = json.load(f)

print(f"Data dari file: {data_dari_file['nama']}")

# 5. MENANGANI TIPE DATA KHUSUS
print("\n==== 5. TIPE DATA KHUSUS ====")

from datetime import datetime

class User:
    def __init__(self, nama, created_at):
        self.nama = nama
        self.created_at = created_at

    def to_dict(self):
        return {
            "nama": self.nama,
            "created_at": self.created_at.isoformat()
        }

user = User("Andi", datetime.now())
user_dict = user.to_dict()
user_json = json.dumps(user_dict, indent=2)
print(f"User JSON:\n{user_json}")

# Custom JSON Encoder untuk objek kompleks
class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, User):
            return obj.to_dict()
        return super().default(obj)

user_json2 = json.dumps(user, cls=UserEncoder, indent=2)
print(f"User JSON via Encoder:\n{user_json2}")

# 6. ERROR HANDLING
print("\n==== 6. ERROR HANDLING ====")

json_salah = '{"nama": "Andi", umur: 20}'  # umur tanpa tanda petik

try:
    data = json.loads(json_salah)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")

# 7. MODE PARSING LAINNYA
print("\n==== 7. PARAMETER LAIN ====")

# separators: kustom separator
json_compact = json.dumps(data, separators=(",", ":"))
print(f"Compact: {json_compact}")

# sort_keys: urutkan key secara alfabet
json_sorted = json.dumps(data, indent=2, sort_keys=True)
print(f"Sorted keys:\n{json_sorted}")
