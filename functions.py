class Tree:

    root=None
    def __init__(self,value,kind):
        self.value=value
        self.kind=kind
        self.children=[]
    


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
                return [False,root_node]
                
        return (True,root_node)       

    def create_dir(self,path1):
        main_root=self.root
        hierarchy=path1.split("/")[1:-1]
        x = len(hierarchy)-1
        stat,node1=self.check_if_path_exists_and_traverse(main_root,hierarchy[0:x])
        if stat:
            node1.children.append(Tree(hierarchy[x],0))
            return(path1,str(True))            
        else:
            return(['No such directory exist',str(False)])

    def create_file(self,path1):
        main_root=self.root
        hierarchy=path1.split("/")[1:-1]
        x = len(hierarchy)-1
        stat,node1=self.check_if_path_exists_and_traverse(main_root,hierarchy[0:x])
        if stat:
            node1.children.append(Tree(hierarchy[x],1))
            return(path1,str(True))            
        else:
            return(['No such directory exist',str(False)])


    def listing(self,path):
        node=self.root
        hierarchy2=path.split("/")[1:-1]
        bool2,root1=self.check_if_path_exists_and_traverse(node,hierarchy2)
        if bool2:
            return root1.children
    
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




