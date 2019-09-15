from functions import *

tree=Tree('Dir',0)
Tree.root=tree


def get_path_and_string(string):
    for x in range(len(string)):
        if string[x]==',':
            return (string[0:x-1],string[x+2:])
    return (str(-1),str(-1))


while True:
    option=input("Enter command")
    if option[0:16]=="create_directory":
        tree.create_dir(option[18:-2],0)
    elif option[0:11]=="create_file":
        tree.create_dir(option[13:-2],1)
    elif option[0:4]=="list" :
        tree.listing(option[6:-2])
    elif option[0:15]=="check_existence":
        if tree.check_existence_of_directory(Tree.root,option[17:-2]):
            print(str(True))
        else:
            print(str(False))
    elif option[0:6]=="search":
        path,string=get_path_and_string(option[8:-2])
        hiearchy=tree.get_hirearchy(path)
        bool3,root3=tree.check_if_path_exists_and_traverse(Tree.root,hiearchy)
        if bool3:
            tree.search_dir(root3,string,hiearchy)
