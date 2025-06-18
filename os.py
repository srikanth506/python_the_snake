import os
os.chdir("G:\My Drive")
# os.mkdir("Core")
# os.rmdir('Cashflow_Quadrant.pdf')
# print(os.listdir())
for dirpath,dirname,filename in os.walk(os.getcwd()):
    print(dirpath,dirname,filename,sep= "\n", end = "\n---------------------------------------------------------------\n")