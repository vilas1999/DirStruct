class Tree:

    root=None
    def __init__(self,value,kind):
        self.value=value
        self.kind=kind
        self.children=[]
    
    #get hirearchy
    def get_hirearchy(self,path):
        hirearchy=[]
        start=1
        end=0
        for x in range(1,len(path)):
            if (path[x] =='/' ):
                end=x
                hirearchy.append(path[start:end])
                start=x+1
        return hirearchy

    def check_children_for_dir(self,parent_root,dir):
        for x in range(len(parent_root.children)):
            if parent_root.children[x].value==dir and parent_root.children[x].kind==0:
                return x
        return -1


    def check_if_path_exists_and_traverse(self,root_node,hirearchy_list):
        for x in range(len(hirearchy_list)):
            index=self.check_children_for_dir(root_node,hirearchy_list[x])
            if index>=0:
                root_node=root_node.children[index]
            elif index==-1:
                out1=["No such directory exists",str(False)]
                print (out1)
                return (False,root_node)
        return (True,root_node)

    def create_dir(self,path1,flag):
        main_root=self.root
        hierarchy=self.get_hirearchy(path1)
        x = len(hierarchy)-1
        stat,node1=self.check_if_path_exists_and_traverse(main_root,hierarchy[0:x])
        if stat:
            node1.children.append(Tree(hierarchy[x],flag))
            print('Added',node1.children[len(node1.children)-1].kind)
            out=[path1,str(True)]
            print(out)

    def listing(self,path):
        node=self.root
        hierarchy2=self.get_hirearchy(path)
        bool2,root1=self.check_if_path_exists_and_traverse(node,hierarchy2)
        if bool2:
            boo1,root_dir1=self.check_if_path_exists_and_traverse(node,hierarchy2)
            for x in range(len(root_dir1.children)):
                print(root_dir1.children[x].value)
    
    def check_existence_of_directory(self,root,directory1):
        if root.value==directory1:
            return 1
        for x in range(len(root.children)):
            if self.check_existence_of_directory(root.children[x],directory1)==1:
                return 1

    def search_dir(self,root_node,str_name,hierarchy):
        if root_node.value==str_name:
            for x in range(len(hierarchy)):
                print(' /',hierarchy[x],end='')
            print()    
        for y in range(len(root_node.children)):
            hierarchy.append(root_node.children[y].value)
            self.search_dir(root_node.children[y],str_name,hierarchy)
            hierarchy.pop()




