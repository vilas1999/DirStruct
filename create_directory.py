#Node class of tree
class Tree:
    def __init__(self,dir):
        self.dir=dir
        self.children=[]
        self.files=[]

#create and add nodes to root node
def create_root(root):
    name=input('Enter the name of new Directory' )
    while check_directory_name(name):
        name=input("Directory name cannot contain '\\' .Please renter")
    root_dir1=root.children.append(Tree(name))
    return root_dir1


#get hirearchy
def get_hirearchy(path):
    hirearchy=[]
    start=1
    end=0
    for x in range(1,len(path)):
        if (path[x] =='\\' ):
            end=x
            hirearchy.append(path[start:end])
            start=x+1
    return hirearchy

#checks if the children of the parent_node has the given dir
def check_children_for_dir(parent_root,dir):
    for x in range(len(parent_root.children)):
        if parent_root.children[x].dir==dir:
            return x
    return -1


#check if path exists
def check_if_path_exists(root_node,path):
    path.replace('\\','\\\\')
    hirearchy_list=get_hirearchy(path)
    for x in range(len(hirearchy_list)):
        index=check_children_for_dir(root_node,hirearchy_list[x])
        if index>=0:
            root_node=root_node.children[index]
        elif index==-1:
            print ("No such directory exists")
            return False
    return True

#trverse tree along the path
def traverse_tree(root_dir,path):
    path.replace('\\','\\\\')
    hirearchy=get_hirearchy(path)
    for x in range(len(hirearchy)):
        index=check_children_for_dir(root_dir,hirearchy[x])
        if index>=0:
            root_dir=root_dir.children[index]
        else:
            print('wvdfb')
    return root_dir


#to print all children
def print_all_children(root):
    for x in range(len(root.children)):
        print(root.children[x].dir)

#check for directory name
def check_directory_name(name):
    for x in range(len(name)):
        if name[x]=='\\':
            return True

#to add children
def add_children(parent_root,path):
    child_dir=input('Enter the name of new Directory ')
    while check_directory_name(child_dir):
        child_dir=input("Directory name cannot contain '\\' .Please renter")
    root=traverse_tree(parent_root,path)
    root.children.append(Tree(child_dir))
    print("Succesfully created ",child_dir,' at ',path)
    return parent_root

#validate path
def validate_path(path):
    # print('From validation',path,path[0],path[len(path)-1])
    if (path[0]=='\\' and path[len(path)-1]=='\\'):
        return True
    else:
        print("Enter path with '\\'")
        return False



#to create directory
def create_directory(path,root):
    if path=='\\':
        name=input('Enter the name of new Directory ')
        while check_directory_name(name):
            name=input("Directory name cannot contain '\\' .Please renter")
        root_dir1=root.children.append(Tree(name))
        print("Succesfully created ",name,' at \\')
        return root_dir1

    else:
        if check_if_path_exists(root,path):
            root=add_children(root,path)
            return root

        
