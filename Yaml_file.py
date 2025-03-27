import yaml

file_path = "C:/Users/sushm/Downloads/Python proj/sample_file.yaml"

try:
    with open(file_path,"r") as f:
        sample = yaml.safe_load(f)
        print("File loaded without any errors")
        print(sample)

except FileNotFoundError:
    print(f"Error: The file {file_path} is not found. Make sure you provided the correct path.")
except PermissionError:
    print(f"Error: Permission denied. The file doesn't have permission rights. Check with the owner of the file")
except yaml.YAMLError as e:
    print(f"Error: file format is incorrect. Details: {e}")
except Exception as e:
    print(f"Unexpected Error occured : {e}")