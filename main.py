from create_directory import create,get_hirearchy,Tree,check_if_path_exists,traverse_tree

root1=Tree("main")

#check format
def check_format(len1,option1):
    if len(option)-len1<5:
        return False
    if option1[len1]=='(' and option1[len(option1)-1]==')' and (option1[len1+1]=='"' or option1[len1+1]=="'") and (option1[len(option1)-2]=='"' or option1[len(option1)-2]=="'"  ):
        return True

#validation
def validate_path(path):
    # print('From validation',path,path[0],path[len(path)-1])
    if path.startswith('/') and path.endswith('/'):
        return True
    else:
        print("Enter path with '/'")
        return False


#check if directory exist
def check_existence_of_directory(root,directory1):
    value=0
    for i in range(len(root.files)):
        if root.files[i]==directory1:
            value=1            
    if root.dir==directory1 or value==1:
        return 1
    for x in range(len(root.children)):
        if check_existence_of_directory(root.children[x],directory1)==1:
            return 1

#listing     
def listing(node,path):
    if check_if_path_exists(node,path):
        root_dir1=traverse_tree(node,path)
        print('----------------------------')
        for x in range(len(root_dir1.children)):
            print('Dir-',root_dir1.children[x].dir)
        for y in range(len(root_dir1.files)):
            print('File-',root_dir1.files[y])

#returns path and string to be searched
def get_path_and_string(string):
    for x in range(len(string)):
        if string[x]==',':
            return (string[0:x-1],string[x+2:])
    return (str(-1),str(-1))


#search dir
def search_dir(root_node,str_name,hierarchy):
    if root_node.dir==str_name:
        print('Dir-',end='')
        for x in range(len(hierarchy)):
            print(' /',hierarchy[x],end='')
        print()    
    for a in range(len(root_node.files)):
        if str_name==root_node.files[a]:
            print('File-',end='')
            for x in range(len(hierarchy)):
                print('/',hierarchy[x],end='')
            print('/',str_name)  
    
    for y in range(len(root_node.children)):
        hierarchy.append(root_node.children[y].dir)
        search_dir(root_node.children[y],str_name,hierarchy)
        hierarchy.pop()



while True:
    option=input("Enter command:")

    #calling create directory
    if option[0:16]=="create_directory" and check_format(16,option):
        if validate_path(option[16+2:len(option)-2]):
            create(option[16+2:len(option)-2],root1,0)
        else:
            print("No such directory exists") 

    #calling create file
    elif option[0:11]=="create_file" and check_format(11,option):
        if validate_path(option[11+2:len(option)-2]):
            create(option[11+2:len(option)-2],root1,1)

     #calling listing   
    elif option[0:4]=="list" and check_format(4,option):
        if validate_path(option[4+2:len(option)-2]):
            listing(root1,option[4+2:len(option)-2])
    
    
     #calling check_existence       
    elif option[0:15]=="check_existence" and check_format(15,option):
        print('----------------------------')
        if check_existence_of_directory(root1,option[15+2:len(option)-2])==1:
            print("True")
        else:
            print("False")
        

    #calling search   
    elif option[0:6]=="search" and check_format(6,option):
        #search()
        path,string=get_path_and_string(option[6+2:len(option)-2])
        hieararchy=get_hirearchy(path)        
        if path == "-1" and string == "-1":
            print("Invalid command")
        elif validate_path(path) and check_if_path_exists(root1,path) :
            search_dir(root1,string,hieararchy)
        
    
    else:
        print("Invalid command")
        print("---------------------------------------------------")
        print("Enter any of the following commands in specified format:")
        print("1) create_directory(\"path\")")
        print("  Note: Enter path as / if creating under main directory")
        print("2) create_file(\"path\")")
        print("3) list(\"path\")")
        print("4) check_existence(\"file_name or directory\")")
        print("5) search(\"path\",\"search_string\")")
        print("---------------------------------------------------")


        
 