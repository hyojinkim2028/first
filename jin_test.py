with open("test.txt","r") as f:

    len_ = 0

    while True:

        line = f.readline()

        if line == "":
            break
      
        line = line.strip()
        if line != "":
            len_ += len(line)

    print(len_)
         

        
            

            

        