def swapFileData(file1,file2):
    with open(file1,"r") as f1:
        data_a=f1.read()
    with open(file2,"r") as f2:
        data_b=f2.read()
    with open(file1,"w") as f1:
        f1.write(data_b)
    with open(file2,"w") as f2:
        f2.write(data_a)