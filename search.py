#to search directory
from create_directory import traverse_tree,get_hirearchy

def get_path_and_string(string):
    for x in range(len(string)):
        if string[x]==',':
            return (string[0:x-1],string[x+2:])


def search(root_node,str_name,path):
    hierarchy=[]
    if path=='\\':
        print('Directories: ')    
        search_for_dir(root_node,str_name,hierarchy)
        print('Files: ')
        search_file(root_node,str_name,hierarchy)
    else:
        root=traverse_tree(root_node,path)
        hierarchy=get_hirearchy(path)
        print('Directories: ')    
        search_for_dir(root,str_name,hierarchy)
        print('Files: ')
        search_file(root,str_name,hierarchy)


def search_for_dir(root_node,str_name,hierarchy):
    if root_node.dir==str_name:
        for x in range(len(hierarchy)):
            print('\\',hierarchy[x],end='')
        print()    
    
    for y in range(len(root_node.children)):
        hierarchy.append(root_node.children[y].dir)
        search_for_dir(root_node.children[y],str_name,hierarchy)
        hierarchy.pop()

#to search file
def search_file(root_node,str_name,hierarchy):
    for a in range(len(root_node.files)):
        if str_name==root_node.files[a]:
            for x in range(len(hierarchy)):
                print('\\',hierarchy[x],end='')
            print('\\',str_name)
    for y in range(len(root_node.children)):
        hierarchy.append(root_node.children[y].dir)
        search_file(root_node.children[y],str_name,hierarchy)
        hierarchy.pop()
