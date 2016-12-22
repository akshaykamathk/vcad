import networkx as nx 
import matplotlib.pyplot as plt 


#area = {'inpt': 1 ,'and': 6 , 'nand' : 8 , 'or' : 6 , 'nor' : 8 , 'xor' : 8 , 'xnor' : 6 , 'buff' : 4 , 'not' : 4 , 'from' : 1}
#height = {'inpt': 1 ,'and': 3 , 'nand' : 4 , 'or' : 3 , 'nor' : 4 , 'xor' : 4 , 'xnor' : 3 , 'buff' : 2 , 'not' : 2 , 'from' : 1}
#width = {'inpt': 1 ,'and': 2 , 'nand' : 2 , 'or' : 2 , 'nor' : 2 , 'xor' : 2 , 'xnor' : 2 , 'buff' : 2 , 'not' : 2 , 'from' : 1}

area = {'inpt': 1 ,'and': 6 , 'nand' : 8 , 'or' : 6 , 'nor' : 8 , 'xor' : 8 , 'xnor' : 6 , 'buff' : 4 , 'not' : 4 , 'from' : 1}
height = {'inpt': 1 ,'and': 3 , 'nand' : 4 , 'or' : 2 , 'nor' : 3 , 'xor' : 4 , 'xnor' : 5 , 'buff' : 2 , 'not' : 1 , 'from' : 1}
width = {'inpt': 1 ,'and': 6 , 'nand' : 6 , 'or' : 4 , 'nor' : 5 , 'xor' : 6 , 'xnor' : 7 , 'buff' : 4 , 'not' : 1 , 'from' : 1}


def load_netlist(netlist) :
	G = nx.Graph()
	Z = {}
	count = 0
	inGr = {}
	weight_dimen = {}
	height_dimen = {}
	f = open(netlist)
	content = f.readlines()
	f.close()

	i = 0
	while (i<len(content)):
	    word = content[i].split()
	    if(word[0]=='*'):
	        i = i+1
	        continue
	    else:
                count = count + 1
                Z[count] = int(word[0])
	        G.add_node(int(word[0]), A = area[word[2]],F = 0,gain = -999999, h=height[word[2]], w=width[word[2]], x=-1, y=-1, x_par = 0, y_par = 0)
    
	        ####### fanin branch ##########p
	        if(int(word[4])>0):
	            fanin = content[i+1].split()
	            i = i+1  
	            for node in fanin :
	                G.add_edge(int(node),int(word[0]),weight = 1)
	        ######## fanout branch #########
	        if(int(word[3])>1) :
	            for j in range(int(word[3])) :
	                fanout = content[i+j+1].split()
	                G.add_node(int(fanout[0]),A = area['from'],F = 0,gain = -999999, h=height['from'], w=width['from'], x=-1, y=-1, x_par = 0, y_par = 0)
	                G.add_edge(int(word[0]),int(fanout[0]),weight = 1)
	                count = count + 1
	                Z[count] = int(fanout[0])
	            i = i+int(word[3])
	        i = i+1
        

	#print 'nodes = ' ,G.nodes(data = True)
	#print 'edges = ' ,G.edges(data = True)
	for k in  range(len(Z)):
            inGr[Z[k+1]] = G.edge[Z[int(k+1)]].keys()
            weight_dimen[Z[k+1]] = G.node[Z[int(k+1)]]['w']
            height_dimen[Z[k+1]] = G.node[Z[int(k+1)]]['h']
       # print inGr 
            
       # print Z
	return inGr,weight_dimen,height_dimen,G

        nx.draw(G,with_labels=True)
        plt.savefig("iscas.png") # save as png
        plt.show() # display
