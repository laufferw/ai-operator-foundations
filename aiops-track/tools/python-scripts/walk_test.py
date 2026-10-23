import os
import sys

# Get directory from command line, or use default
if len(sys.argv) > 1:
    target_dir = sys.argv[1]
else:
    target_dir = "/home/wll/lab"

file_sizes = []
                                                                                                            
   # This will walk through your lab directory                                                              
for folder_path, folder_names, file_names in os.walk(target_dir):                                   
    print(f"Folder: {folder_path}")                                                                      
    for filename in file_names:
        full_path = os.path.join(folder_path, filename)
        size = os.path.getsize(full_path)
        file_info = (full_path, size)
        file_sizes.append(file_info)

sorted_files = sorted(file_sizes, key=lambda x: x[1], reverse=True)
top_5 = sorted_files[:5]
print("Top 5 largest files:")
print(top_5)
