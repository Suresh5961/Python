# w - replace old content, if file already there
# w - new file, if mentioned file not there

file=open("W-binariFile.txt","w")
#file.write("Hai there this is another file created by suresh in the format of pdf")
file.write("Suresh will learn how to deal with files")
file.close()
print("File",file.name,"has created")