

#check if directory exist
def check_existence_of_directory(root,directory1):
    
    if root.dir==directory1:
        return 1
    else:
        for x in range(len(root.children)):
            if check_existence_of_directory(root.children[x],directory1)==1:
                return 1
    
#check if file exist
def check_existence_of_file(root,file_name):
    
    for i in range(len(root.files)):
        if root.files[i]==file_name:
            return 1
    for x in range(len(root.children)):
        if check_existence_of_file(root.children[x],file_name)==1:
            return 1