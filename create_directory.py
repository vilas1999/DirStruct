class Tree:
    def __init__(self,dir):
        self.dir=dir
        self.children=[]
        self.files=[]

#get hirearchy
def get_hirearchy(path):
    hirearchy=[]
    start=1
    end=0
    for x in range(1,len(path)):
        if (path[x] =='/' ):
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
def check_if_path_exists_and_traverse(root_node,path):
    path.replace('/','//')
    hirearchy_list=get_hirearchy(path)
    for x in range(len(hirearchy_list)):
        index=check_children_for_dir(root_node,hirearchy_list[x])
        if index>=0:
            root_node=root_node.children[index]
        elif index==-1:
            print ("No such directory exists")
            return (False,root_node)
    return (True,root_node)


#to create directory
def create(path,root,flag):
    bool1,node1=check_if_path_exists_and_traverse(root,path)
    if bool1:
        child=input('Enter the name: ')
        while '/' in child:
            child=input("Name cannot contain '/' .Please renter: ")
        bool2,root=check_if_path_exists_and_traverse(root,path)
        if flag==0:
            root.children.append(Tree(child))
        elif flag==1:
            root.files.append(child)
        print("Succesfully created ",child,' at ',path)
        return root

        
