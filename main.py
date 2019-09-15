from create_directory import create,Tree,validate_path
from list_dir import listing
from search import search,get_path_and_string
from create_directory import check_if_path_exists

root1=Tree("main")

#check format
def check_format(len1,option1):
    if len(option)-len1<5:
        return False
    if option1[len1]=='(' and option1[len(option1)-1]==')' and (option1[len1+1]=='"' or option1[len1+1]=="'") and (option1[len(option1)-2]=='"' or option1[len(option1)-2]=="'"  ):
        return True
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
        if path == "-1" and string == "-1":
            print("Invalid command")
        elif validate_path(path) and check_if_path_exists(root1,path) :
            search(root1,string,path)
        
    
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
    
