#basic node of tree
class Tree:
    def __init__(self,dir):
        self.dir=dir
        self.children=[]

#to add children
def add_children(parent_root,child_dir):
    child_root=Tree(child_dir)
    parent_root.children.append(child_root)

#to print all children
def print_all_children(root):
    for x in range(len(root.children)):
        print(root.children[x].dir)


#checks if the children of the parent_node has the given dir
def check_children_for_dir(parent_root,dir):
    for x in range(len(parent_root.children)):
        if parent_root.children[x].dir==dir:
            return x
    
    print("No such ﬁle or Directory")
    return -1

#returns hirearchy in list form
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

root = Tree("root")
add_children(root,'child 1')
add_children(root,'child 2')
print_all_children(root)

#check_children_for_dir(root,'child')

path=input("Enter the path")
path.replace('\\','\\\\')
print(path)
hirearchy=get_hirearchy(path)

if hirearchy[0]==root.dir:
    print('Passed root')
    for x in range(1,len(hirearchy)):
        index=check_children_for_dir(root,hirearchy[x])
        if index>=0:
            root=root.children[index]

            
        
        


        



"""path=input("Enter the path")
dir_name=input("Enter the directory name")

root = Tree("root")
add_children(root,'child 1')
add_children(root,'child 2')
print_all_children(root)

print("Inside children")

root=root.children[0]
add_children(root,'child 11')
add_children(root,'child 21')
print_all_children(root)"""


