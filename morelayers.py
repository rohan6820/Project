with open("accuracy.txt","r") as ac:
    if ac.read()<="0.95":
        with open("c.py","r") as f:
            contents=f.readlines()

        with open("layers.txt","r") as g:
            i=25
            k=g.readlines()
            for j in k:
                
                if i in range(25,29):
                    contents.insert(i,j)
                elif i in [30,31]:
                    contents.insert(i,j)
                i+=1
            contents[35]=k[-1]

        with open("c.py","w") as l:
            l.writelines(contents)

