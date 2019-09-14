from create_directory import check_if_path_exists,traverse_tree
from create_directory import validate_path

def create_file(node,path):
    if check_if_path_exists(node,path):
        root_dir1=traverse_tree(node,path)
        file_name=input("Enter file name: ")
        root_dir1.files.append(file_name)
        print('Created file ', file_name,' at ',path)
    
def list_files(node,path):
    if check_if_path_exists(node,path):
        root_dir1=traverse_tree(node,path)
        for x in range(len(root_dir1.files)):
            print(root_dir1.files[x])    
