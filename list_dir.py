from create_directory import traverse_tree,print_all_children
from create_directory import get_hirearchy,check_if_path_exists
from create_file import list_files

def listing(node,path):
    if check_if_path_exists(node,path):
        root_dir1=traverse_tree(node,path)
        print('----------------------------')
        print("Directories at ",path)
        print_all_children(root_dir1)
        print('----------------------------')
        print("Files at",path)
        list_files(node,path)
        print('----------------------------')


    