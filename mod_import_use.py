from mod_import_mod.mod_import_ex import my_json

try:
    print(my_json())
except Exception as e:
    print(f"Could not run function due to {str(e)}")

print("Trying again")
import json
print(my_json())

json.dumps