import os


os.chdir('C:/Users/soap/Documents/files/to parse/')

#current working dir
print(os.getcwd())

#list all files in this dir
for f in os.listdir():
    #split file names in parts 
    name,exts=os.path.splitext(f)
    
    #your extension here
    if exts=='.html':
    
        #new extension here
        new_ext='.php'
        #format the name as needed
        new_name='{}{}'.format(name,new_ext)
        #remane file with new name
        os.rename(f,new_name)
