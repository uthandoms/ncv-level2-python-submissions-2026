mark = []
i = 0


while mark != -1:
    mark.append(mark)
    mark = int(input("Mark ( or -1 to stop): "))
    
 
    print(f"Our list has {len(mark)}elements")
    
    for x in range(len(mark)):
        print(mark[x])



