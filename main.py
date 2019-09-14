from create_directory import create_directory,Tree,validate_path
from create_directory import print_all_children
from list_dir import listing
from create_file import create_file
from check_existence import check_existence_of_directory,check_existence_of_file
from search import search,get_path_and_string

root1=Tree("main")
'''while True:
    path=input("Enter path ")
    while validate_path(path):
        print("No such directory exists")    
        path=input("Enter path")
    create_directory(path,root1)'''


#check format
def check_format(len1,option1):
    if len(option)-len1<5:
        return False
    '''print(option1[len1])
    print(option1[len1+1])
    print(option1[len(option1)-1])
    print(option1[len(option1)-2])    '''
    if option1[len1]=='(' and option1[len(option1)-1]==')' and (option1[len1+1]=='"' or option1[len1+1]=="'") and (option1[len(option1)-2]=='"' or option1[len(option1)-2]=="'"  ):
        return True
while True:
    option=input("Enter command:")

    #calling create directory
    if option[0:16]=="create_directory" and check_format(16,option):
        #print (validate_path(option[16+2:len(option)-2]))
        if validate_path(option[16+2:len(option)-2]):
            create_directory(option[16+2:len(option)-2],root1)
        else:
            print("No such directory exists") 

    #calling create file
    elif option[0:11]=="create_file" and check_format(11,option):
        if validate_path(option[11+2:len(option)-2]):
            create_file(root1,option[11+2:len(option)-2])

     #calling listing   
    elif option[0:4]=="list" and check_format(4,option):
        if validate_path(option[4+2:len(option)-2]):
            listing(root1,option[4+2:len(option)-2])
     #calling check_existence       
    elif option[0:15]=="check_existence" and check_format(15,option):
        print('----------------------------')
        print('For Directory:')
        if check_existence_of_directory(root1,option[15+2:len(option)-2])==1:
            print("True")
        else:
            print("False")
        print('----------------------------')        
        print('For File:')
        if check_existence_of_file(root1,option[15+2:len(option)-2])==1:
            print("True")
        else:
            print("False")
        print('----------------------------')
    #calling search   
    elif option[0:6]=="search" and check_format(6,option):
        #search()
        path,string=get_path_and_string(option[6+2:len(option)-2])
        print('path',path)
        print('string',string)
        search(root1,string,path)
        '''hierarchy=[]
        print('Directories: ')
        search(root1,option[6+2:len(option)-2],hierarchy)
        print('Files: ')
        search_file(root1,option[6+2:len(option)-2],hierarchy)'''
    else:
        print("Invalid command")