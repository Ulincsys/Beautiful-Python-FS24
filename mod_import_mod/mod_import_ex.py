def my_json():
    return json.dumps({"key": "value"})

if __name__ == "__main__":
    import json
    print(my_json())