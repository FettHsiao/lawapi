import json

def clear_json_file(file_path):
    empty_data = {} 
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(empty_data, json_file, ensure_ascii=False, indent=4)


file_path = '/Users/mac/Documents/code/python/project2/law.json'

clear_json_file(file_path)
