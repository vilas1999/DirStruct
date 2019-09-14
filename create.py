#Node class of tree
class Tree:
    def __init__(self,dir):
        self.dir=dir
        self.children=[]

#create root node
def root_node(dir):
    return Tree(dir)

#to print all children
def print_all_children(root):
    for x in range(len(root.children)):
        print("1",root.children[x].dir)



#returns hirearchy path as a list
def get_hirearchy(path):
    hirearchy=[]
    start=1
    end=0
    for x in range(1,len(path)):
        if (path[x] =='\\' ):
            end=x
            hirearchy.append(path[start:end])
            start=x+1
    print (hirearchy)
    return hirearchy


#checks if the children of the parent_node has the given dir
def check_children_for_dir(parent_root,dir):
    for x in range(len(parent_root.children)):
        if parent_root.children[x].dir==dir:
            return x
    return -1
 


#trverse tree along the path
def traverse_tree(root,path):
    print('enterted traversing')
    print('path',path)
    path.replace('\\','\\\\')
    hirearchy=get_hirearchy(path)
    print('hirearchy',hirearchy)
    print('root',root.dir,len(root.children))
    for x in range(len(hirearchy)):
        print('in loop')
        index=check_children_for_dir(root,hirearchy[x])
        if index>=0:
            root=root.children[index]
            print('tree traversing',root)
    return root
    



#check if directory exist
def check_if_dir_exist(root,path):
    path.replace('\\','\\\\')
    hirearchy=get_hirearchy(path)
    if hirearchy[0]==root.dir:
        for x in range(1,len(hirearchy)):
            index=check_children_for_dir(root,hirearchy[x])
            if index>=0:
                root=root.children[index]
            elif index==-1:
                print ("No such directory exists")
                return str(False)
        print('root returned from check',root.dir)       
        return True
    else:
        print("No such directory exists")

#to add children
def add_children(parent_root,path):
    child_dir=input("enter new dir name1")
    child_root=Tree(child_dir)
    root=traverse_tree(parent_root,path)
    print('child added to',root.dir)
    print("children")
    print_all_children(root)
    root.children.append(Tree(child_root))
 

# main
def create_directory(path,main):   
    if path =='\\':
        name=input('enter the dir name2 ')
        root=root_node(name)
        return root
    else:
        if check_if_dir_exist(main,path):
            add_children(main,path)
            return main

main=Tree('sample')
while True:
    path=input('enter the path')
    main=create_directory(path,main)