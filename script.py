import re, json

file = open("output.txt", 'r')
file_content = "".join(file.readlines())

functions = re.findall(r'([0-9]+)[0-9 ]+[^@]+@[^@]+@(.+)', file_content)

files = {}

for function in functions:
    fct_length = int(function[0])
    file_path = function[1]

    if file_path not in files:
        files[file_path] = {"min_fct": fct_length, "max_fct": fct_length, "avg_fct": fct_length, "no_of_fct": 1, "total_fct_length": fct_length}
    else:
        if fct_length < files[file_path]["min_fct"]:
            files[file_path]["min_fct"] = fct_length
        if fct_length > files[file_path]["max_fct"]:
            files[file_path]["max_fct"] = fct_length
        files[file_path]["no_of_fct"] += 1
        files[file_path]["total_fct_length"] += fct_length
        files[file_path]["avg_fct"] = files[file_path]["total_fct_length"] / files[file_path]["no_of_fct"]

format_final = []

for file in files:
    file_path = file.split('ces/src/')[1]
    category = "CES2"
    format_final.append({"name": "min_fct", "category": category, "file": file_path, "value": files[file]["min_fct"]})
    format_final.append({"name": "max_fct", "category": category, "file": file_path, "value": files[file]["max_fct"]})
    format_final.append({"name": "avg_fct", "category": category, "file": file_path, "value": files[file]["avg_fct"]})
    format_final.append({"name": "no_of_fct", "category": category, "file": file_path, "value": files[file]["no_of_fct"]})

jsn = json.dumps(format_final, indent=4)

print(jsn)