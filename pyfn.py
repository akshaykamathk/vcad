import random
import math 

def COST(V,W,S,B):
	cutsize=0;								# Initialize cutsize
	for i in range(len(S)):					# For each vertex in the vertex set
		if(S[i]==1):						# If the vertex belongs to the first partition
			adj=V[B[i]]						# Obtain the list of its adjacent vertices
			for j in adj:					# For each adjacent vertex
				if(S[B.index(j)]==2):		# If it belongs to the second partition
					cutsize+=W[B[i],j];		# Increment the cutsize with the edge weight 
	return cutsize;							# Return the cutsize
	
def PERTURB(V,W,S,B,p):
	move=[]
	for b in range(len(B)):
		St=list(S)
		St[b]=3-S[b];
		gain=COST(V,W,S,B)-COST(V,W,St,B);
		r=random.randint(p,0);
		if (gain > r):
			S=list(St);
			move.append(b)
	if(len(move)!=0):
		S=MAKESTATE(S,move)
	return S
	
def MAKESTATE(S,move):	
	k=partn(S,1)-partn(S,2);
	idx=-1	
	while(k!=0):
		j=move[idx]
		if(k<0):
			if(S[j]==2):
				S[j]=1;
		else:
			if(S[j]==1):
				S[j]=2;
		k=partn(S,1)-partn(S,2);
		idx-=1
	return S
	
def partn(S,idx):
	count=0
	for i in range(0,len(S)):
		if(S[i]==idx):
			count+=1
	return count
	
def SUBGRAPH(G,B):
	V={}
	for i in B:
		V[i]=list(G[i])
		
	for v in V:
		U=list(V[v])
		for u in U:
			if u not in B:
				V[v].remove(u)
	
	return V
	
def SPLIT(B,S):
	V1=[]
	V2=[]
	for i in range(len(S)):
		if(S[i]==1):
			V1.append(B[i])
		else:
			V2.append(B[i])
	return [V1,V2]
