def initialize_path(grid,path,source,layer):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            path[x,y]=['w',-1,[-2,-2]]
            if(grid[x][y]==layer):
                path[x,y][0]='b'
    sx=source[0]
    sy=source[1]
    path[sx,sy]=['g',0,[-2,-2]]
    
def print_path(grid,path,route,source,target):
    if(target==source):
        route.append(source)
    #elif(path[tuple(target)][2]==[-2,-2]):
    #    print "No Path"
    else:
        parent=path[tuple(target)][2]
        print_path(grid,path,route,source,parent)
        route.append(target)

def find_route(grid,S,D,layer):
    path={}
    route=[]
    initialize_path(grid,path,S,layer)
    Q=[]
    Q.append(S)
    found=False

    while(len(Q)!=0):
        u=Q[0]
        del Q[0]
        ux=u[0]
        uy=u[1]

        #Define list of valid vertices adjacent to u
        adj=[]
        if(ux>0):
            adj.append([ux-1,uy]); # Top vertex, not present if ux==0
        if(ux<len(grid)-1):
            adj.append([ux+1,uy]); # Bottom vertex, not present if ux==g_w-1
        if(uy>0):
            adj.append([ux,uy-1]); # Left vertex, not present if uy==0
        if(uy<len(grid[0])-1):
            adj.append([ux,uy+1]); # Right vertex, not present if uy==g_h-1

        for v in adj:
            if(path[tuple(v)][0]=='w'):                 # If unvisited vertex,
                path[tuple(v)][0]='g'                   #Mark visited
                path[tuple(v)][1]=path[tuple(u)][1]+1   #Increment Distance
                path[tuple(v)][2]=u                     #Assign parent
                Q.append(v)
            if(v==D):
                path[tuple(v)][1]=path[tuple(u)][1]+1
                path[tuple(v)][2]=u
                found=True
                break
            

        path[tuple(u)][0]='b'
        if(found==True):
            print_path(grid,path,route,S,D)
            return route
    
    #print_path(grid,path,route,S,D)
    #return route
    if(found==False):
        return "No path found"
