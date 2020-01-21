import binascii



def main(x,y):
    isovalue = 128
    array1=[]
    pathofFile = "C:\\Users\John\\Desktop\\testing\\neuron_1024_1024_unsigned_char.raw" ##change this to where your .raw files are 
    file = open(pathofFile, "rb")
    f = open("iso1024.obj","w+") 
    with file:
        for i in range(1023):
            array2=[]
            for j in range(1023): ##max byte size
                yeet = int.from_bytes(file.read(1),byteorder='big', signed=False) ##change this
                array2.append(yeet)
            array1.append(array2)
    ##print(arr)
    arrbinary=[]
    for i in array1:
        v=[]
        for j in range(1023):
            if i[j] >= isovalue:
                v.append(1)
            else:
                v.append(0)
        arrbinary.append(v)
    ##print(arr)
    print(arrbinary)
    v=[]
    l=[]
    lol = ' 0'
    for i in range(1022): ##one less than max
        for j in range(1022): ##block = string interpretation of binary
            block = ""
            block = block + str(arrbinary[i][j])
            block = block + str(arrbinary[i][j+1])
            block = block + str(arrbinary[i+1][j+1])
            block = block + str(arrbinary[i+1][j])

            if (block == "1110"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))
        
            elif (block == "1101"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))

            elif (block == "1011"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))


            elif (block == "0111"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))
        
            elif (block == "0001"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))

            elif (block == "0010"):
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))


            elif (block == "0100"):
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))
        
            elif (block == "1000"):
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))

            elif (block == "1100"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))

            elif (block == "1001"):
                v.append("v " + str(i+.50)+" "+str(j)+ lol)
                v.append("v " + str(i+.50)+ " " +str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))
        
            elif (block == "0011"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))

            elif (block == "0110"):
                v.append("v " + str(i+.50) +" "+str(j) + lol)
                v.append("v " + str(i+.50) +" "+str(j) + lol)
                l.append("l " + str(len(v)-1) + " " + str(len(v)))


            elif (block == "0101"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+""+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))

            elif (block == "1010"):
                v.append("v " + str(i+.50)+" "+str(j) + lol)
                v.append("v " + str(i+.50)+""+str(j) + lol)
                l.append("l " + str(len(v)-1)+ " " + str(len(v)))

    print(v)
    ##f.write(v)
    with f:
        for i in v:
            f.write(i + '\n')
        for j in l:
            f.write(j + '\n')



         
main(1024,1024)

