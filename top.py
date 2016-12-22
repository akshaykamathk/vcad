from pyfn import *
from bipart import *
from load_netlist import load_netlist
import math
import subprocess
import os
import resource
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from bfs import *
from copy import deepcopy
from datetime import datetime
import networkx as nx 



print "\n\nMEMORY USED = "
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000),"\n\n"

startTime = datetime.now()

###########################################Read netlist in the desired format(Here, as a dictionarys)##########################################
G, height_dimen, weight_dimen,circuit = load_netlist('alu.isc')


nx.draw(circuit,with_labels=True)
plt.savefig("alu.png") # save as png
#plt.show() # display

if(len(G)%2 != 0):
      G[0] = [];
      weight_dimen[0] = 0;
      height_dimen[0] = 0;
print G
print 'Hi'
print weight_dimen
print '\n'
print height_dimen
print 'bye'
print len(G)

############################################Compute the total number of partitions possible#####################################################
N = len(G);
flag = 0;
while(not (((N & (N - 1)) == 0) and N > 0)):
    flag = 1;
    Q = math.log(N, 2);
    Q1 = int(Q);
    N = N - 2**Q1;
    
print "No. of total partitions = "

if flag == 0:    
    tot_part = N/2
    print  N/2
else:
    tot_part = N
    print N






# Obtained from ISCAS Netlist
"""G = {    1: [2, 3], 
	 2: [32, 1], 
	 3: [1, 38], 
	 4: [5, 6], 
	 5: [32, 4],
	 6: [4, 38], 
	 7: [8, 9], 
	 8: [41, 7], 
	 9: [49, 7], 
	 10: [11, 12], 
	 11: [41, 10], 
	 12: [49, 10], 
	 13: [14, 15], 
	 14: [13, 53], 
	 15: [13, 61], 
	 16: [17, 18], 
	 17: [16, 53], 
	 18: [16, 61], 
	 19: [20, 21], 
	 20: [66, 19], 
	 21: [72, 19], 
	 22: [24, 23], 
	 23: [66, 22], 
	 24: [72, 22], 
	 25: [26], 
	 26: [25, 27, 28, 29, 30, 31], 
	 27: [26, 85], 
	 28: [89, 26], 
	 29: [26, 92], 
	 30: [26, 94], 
	 31: [96, 26], 
	 32: [33, 2, 35, 36, 5, 34, 37], 
	 33: [32, 82], 
	 34: [32, 83], 
	 35: [32, 84], 
	 36: [32, 85], 
	 37: [32, 86], 
	 38: [40, 3, 6, 39], 
	 39: [97, 38], 
	 40: [78, 38], 
	 41: [11, 8, 42, 43, 44, 45, 46, 47, 48], 
	 42: [41, 83], 
	 43: [41, 84], 
	 44: [41, 85], 
	 45: [41, 87], 
	 46: [88, 41], 
	 47: [41, 89], 
	 48: [41, 90], 
	 49: [9, 50, 51, 12, 52], 
	 50: [49, 82], 
	 51: [49, 98], 
	 52: [49, 79], 
	 53: [14, 17, 54, 55, 56, 57, 58, 59, 60], 
	 54: [84, 53], 
	 55: [53, 85], 
	 56: [88, 53], 
	 57: [89, 53], 
	 58: [91, 53], 
	 59: [92, 53], 
	 60: [53, 93], 
	 61: [64, 65, 15, 18, 62, 63], 
	 62: [83, 61], 
	 63: [61, 87], 
	 64: [99, 61], 
	 65: [80, 61], 
	 66: [67, 68, 69, 70, 71, 20, 23], 
	 67: [66, 85], 
	 68: [89, 66], 
	 69: [66, 92], 
	 70: [66, 94], 
	 71: [66, 95], 
	 72: [73, 74, 75, 76, 77, 21, 24], 
	 73: [72, 84], 
	 74: [72, 88], 
	 75: [72, 91], 
	 76: [72, 100],
	 77: [72, 81], 
	 78: [40, 86], 
	 79: [90, 52], 
	 80: [65, 93], 
	 81: [77, 95], 
	 82: [33, 50, 97], 
	 83: [97, 34, 42, 62], 
	 84: [43, 35, 97, 54, 73], 
	 85: [97, 67, 36, 44, 55, 27], 
	 86: [37, 78, 101], 
	 87: [98, 45, 63], 
	 88: [56, 74, 98, 46], 
	 89: [57, 98, 68, 28, 47], 
	 90: [48, 102, 79], 
	 91: [99, 58, 75], 
	 92: [99, 59, 69, 29], 
	 93: [80, 60, 103], 
	 94: [100, 70, 30], 
	 95: [104, 81, 71], 
	 96: [104, 31], 
	 97: [82, 83, 84, 85, 39], 
	 98: [88, 89, 51, 101, 87], 
	 99: [64, 91, 92, 102], 
	 100: [76, 94, 103], 
	 101: [98, 86], 
	 102: [90, 99], 
	 103: [100, 93], 
	 104: [96, 95]}"""

W={}
for i in G:
        for j in G[i]:
                W[i,j]=1


#W[1,2]=2; W[2,1]=2;
#W[1,5]=5; W[5,1]=5;
#W[2,6]=5; W[6,2]=5;
#W[3,4]=3; W[4,3]=3;
#W[7,8]=2; W[8,7]=2;

N=len(G); S0=[]; P=G.keys();

print "Given set of vertices: "
print P

for i in range(0,N):
	if i < N/2:
		S0.append(1);
	else:
		S0.append(2);

print "Initial bipartition cost is %d \n" % COST(G,W,S0,P)
Part={}
Part_no=0; flag=0;

S_init=BIPARTITION(G,W,P)
P_temp=SPLIT(P,S_init)
print "Initial bipartition is ",	
for element in range(0,len(S_init)):
	print "%d,"%S_init[element],
print "\n"

print "Final bipartition cost is %d"%COST(G,W,S_init,P)


for j in range(2):
        Part[Part_no]=P_temp[j]
        Part_no+=1

count=Part_no

while((len(Part[count-1])%2==0) and (len(Part[count-1])>2)):
        for k in range(flag,count):
                B=Part[k]
                V=SUBGRAPH(G,B)
                S=BIPARTITION(V,W,B)
                P_temp=SPLIT(B,S)
                for j in range(2):
                        Part[Part_no]=P_temp[j]
                        Part_no+=1

        flag=count
        count=Part_no

P={}
k=1
partition_length=len(Part[count-1])
for i in Part.keys():
        if(len(Part[i])==partition_length):
                P[k]=Part[i]
                k+=1

edges=[]
for i in range(1,len(P)+1):
        flag1=False
        flag2=False
        for j in range(i+1,len(P)+1):
                for k in P[i]:
                        for l in G[k]:
                                if(l>k and l in P[j]):
                                        edges.append([i,j])
                                        
A={}
for i in range(len(P)):
        A[i+1]=[]

for i in range(len(edges)):
        if(edges[i]!=edges[i-1]):
                A[edges[i][0]].append(edges[i][1])

L=deepcopy(A)
for a in A:
    for b in A[a]:
        if(a not in A[b]):
            L[b].append(a)
# A is the connections between partitions 


final_part = {}
temp_num = len(Part) - 1;

for i in range(0,tot_part):
    final_part[tot_part - i] = Part[temp_num - i]

print final_part

print "\n\nMEMORY USED = "
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000),"\n\n"

print "TIME TAKEN = "
print datetime.now() - startTime, "\n\n"



def init_vertices(grid,nodes):
    for node in nodes:
        x=nodes[node][0]
        y=nodes[node][1]
        grid[x][y]=1

def block_vertices(grid,route,layer):
    for i in range(len(route)):
        x=route[i][0]
        y=route[i][1]
        #if(grid[x][y]!=1):
        grid[x][y]=layer
        
def print_grid(grid,g_w,g_h,nodes):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    
    x0,x1,x2,x3,x4,x5,x6=[],[],[],[],[],[],[]
    y0,y1,y2,y3,y4,y5,y6=[],[],[],[],[],[],[]
    
    for i in range(g_w):
        for j in range(g_h):
            if(grid[i][j]==1):
                x1.append(i)
                y1.append(j)
            if(grid[i][j]==2):
                x2.append(i)
                y2.append(j)
            if(grid[i][j]==3):
                x3.append(i)
                y3.append(j)
            if(grid[i][j]==4):
                x4.append(i)
                y4.append(j)
            if(grid[i][j]==5):
                x5.append(i)
                y5.append(j)
            if(grid[i][j]==6):
                x6.append(i)
                y6.append(j)
                
    for node in nodes:
        x0.append(nodes[node][0])
        y0.append(nodes[node][1])

                
    ax.scatter(x1,y1,color='r') #Red
    ax.scatter(x2,y2,color='g') #Green
    ax.scatter(x3,y3,color='k') #Black
    ax.scatter(x4,y4,color='m') #Magenta
    ax.scatter(x5,y5,color='y') #Yellow
    ax.scatter(x6,y6,color='c') #Cyan

    ax.scatter(x0,y0,color='b') #Blue
    
    plt.axis([0,g_w,0,g_h])
    plt.show()
    #plt.figure()

def print_route(route,g_w,g_h):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    x=[]
    y=[]
    for i in range(len(route)):
        x.append(route[i][0])
        y.append(route[i][1])

    ax.scatter(x,y)
    plt.axis([0,g_w,0,g_h])
    plt.show()


###################################################floorplanning#################################################################




optimized_height = {}
optimized_width = {}

#open a file to write the information related to number of blocks and widths and heights of each block belonging to a particular partition
res = open("result.txt", "a+");
for i in range(tot_part):
        wmin = 0;
        hmin = 0;
        counter = 1;    	
        for x in range(len(final_part[i+1])):
            wmin = wmin + weight_dimen[final_part[i+1][x]]         # chip width; can be varied. Generally, wmin = sum(width of all modules in a given partition)
    
        for x in range(len(final_part[i+1])):
            hmin = hmin + height_dimen[final_part[i+1][x]]                                                                                                                                                                                                                                       
   
        M = 0.9*max(wmin,hmin);                                                         # M = max(W,H) or M = W+H; W = chip width, H = chip height; can be varied

    
        fo = open("test.dat", "w");
        fo.write("data;\nparam n :=  ");
        
        fo.write("%s;" % str(len(final_part[i+1])));
        
        fo.write("\nparam module :=  ");
        
        for item in final_part[i+1]:
            fo.write("%s " %str(counter));
            fo.write("%s " %item);
            counter = counter + 1;
            
        fo.write(";\nparam wvar :=  ");
        
        counter = 1;
        
        for item in final_part[i+1]:
            fo.write("%s " %str(counter));
            fo.write("%s " %weight_dimen[item]);
            counter = counter + 1;


        fo.write(";");

        counter = 1;    

        fo.write("\nparam hvar :=  ");

        for item in final_part[i+1]:
            fo.write("%s " %str(counter));
            fo.write("%s " %height_dimen[item]);
            counter = counter + 1;    

        fo.write(";");

        fo.write('\nparam wmin := %d'  %wmin);
        fo.write(';\nparam M := %d'  %M);

        fo.write(";\nend;\n");
        fo.close();

        os.system("glpsol --math --tmlim 15 --pcost floorplan.mod -d test.dat -w out.txt -y out1.txt -o floorplan.out");   #can use --tmlim 10
        #os.system("sync; echo 1 > /proc/sys/vm/drop_caches");
        #os.system("sync; echo 2 > /proc/sys/vm/drop_caches");
        f = open("out1.txt","r")
	content = f.readlines()
	f.close()
	
        optimized_width[i+1] = content[0].split()[2]
        optimized_height[i+1] = content[1].split()[2]    
	
        res.writelines([l for l in open("out1.txt").readlines()])
        res.writelines("\n")
        print 'hi'
        os.remove("test.dat");
# Plotting the cost vs no. of iterations
#plt.plot(costs);
#plt.title('Graph 3');
#plt.ylabel('Cost');
#plt.xlabel('# iterations');
#plt.show();    

res.close()
print optimized_width,optimized_height




wmin = 0;
hmin = 0;
counter = 1;    	
for x in range(len(optimized_width)):
    wmin = wmin + int(optimized_width[x+1])         # chip width; can be varied. Generally, wmin = sum(width of all modules in a given partition)
for x in range(len(optimized_height)):
    hmin = hmin + int(optimized_height[x+1])                                                                                                                                                                                                                                      
   
M = 0.5*(wmin - hmin);                                                         # M = max(W,H) or M = W+H; W = chip width, H = chip height; can be varied                       

    
fo = open("test.dat", "w");
fo.write("data;\nparam n :=  ");
        
fo.write("%s;" % str(len(optimized_height)));
            
fo.write("\nparam wvar :=  ");
        
for item in optimized_width:
    fo.write("%s " %str(counter));
    fo.write("%s " %optimized_width[item]);
    counter = counter + 1;

fo.write(";");

counter = 1;    

fo.write("\nparam hvar :=  ");

for item in optimized_height:
    fo.write("%s " %str(counter));
    fo.write("%s " %optimized_height[item]);
    print item
    counter = counter + 1;    

fo.write(";");

fo.write('\nparam wmin := %d'  %wmin);
fo.write(';\nparam M := %d'  %M);

fo.write(";\nend;\n");
fo.close();

os.system("glpsol --math --pcost --tmlim 20 floorplan1.mod -d test.dat -w out2.txt -y result1.txt -o floorplan1.out");

f1 = open("result1.txt","r")
content1 = f1.readlines()
f1.close()


final_chip_width = content1[0].split()[2];
final_chip_height = content1[1].split()[2];

f2 = open("result.txt","r")
content2 = f2.readlines()
f2.close()

i = 5;
k = 5;
final_coordinates = {}
while (i<len(content1)):
    word = content1[i].split()
    x = int(word[1]);
    y = int(word[2]);
    for j in range(k,k + len(G)/tot_part):
        word = content2[j].split()
        print word
        x_d = int(word[1]);
        y_d = int(word[2]);
        final_coordinates[int(word[0])] = [x + x_d , y + y_d , int(word[3]) , int(word[4])];
    
    k = j + 7;
    i = i + 1;


print "\n\nThe Final optimized co ordinates of nodes are: \n"
print final_coordinates

print "Final chip width = "
print final_chip_width

print "\nFinal chip height = "
print final_chip_height

print "\n\nMEMORY USED = "
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000),"\n\n"
print "TIME TAKEN = "
print datetime.now() - startTime, "\n\n"
##########################################################ROUTING##############################################################################

startTime = datetime.now()

f=open('result1.txt','r')

wline=f.readline()
wline=wline.split('=')
wline=wline[1]
width=wline.split('\n')
c_w=int(width[0]) #chip width after floorplanning

hline=f.readline()
hline=hline.split('=')
hline=hline[1]
height=hline.split('\n')
c_h=int(height[0]) #chip height after floorplanning

f.readline()
f.readline()
f.readline()

g_w=5+c_w
g_h=5+c_h

grid=[[0 for y in range(g_h)] for x in range(g_w)]
b=f.readline()
nodes={}

while(b!=""):
    b=[int(s) for s in b.split() if s.isdigit()]
    #x=b[1]+int(c_w/2)-1
    #y=b[2]+int(c_h/2)-1
    x=b[1]+2
    y=b[2]+2
    w=b[3]
    h=b[4]
    nodes[b[0]]=[x,y,w,h]
    b=f.readline()
print nodes
print '\n'
print L
init_vertices(grid,nodes)
route={}
print_grid(grid,g_w,g_h,nodes)

for v in L:
    S=[nodes[v][0],nodes[v][1]]
    for u in L[v]:
        layer=1
        if u>v:
            D=[nodes[u][0],nodes[u][1]]
            print S,D
            route[v,u]=find_route(grid,S,D,layer)
            while(route[v,u]=="No path found"):
                layer+=1
                route[v,u]=find_route(grid,S,D,layer)
            block_vertices(grid,route[v,u],layer)
            print_grid(grid,g_w,g_h,nodes)

print "TIME TAKEN = "
print datetime.now() - startTime, "\n\n"
