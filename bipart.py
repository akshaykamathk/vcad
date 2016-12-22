from pyfn import *

def BIPARTITION(V,W,B):
	N=len(V); S0=[];

	for i in range(0,N):
		if i < N/2:
			S0.append(1);
		else:
			S0.append(2);
		
	S=list(S0); S_best=list(S0); p0=-1; p=p0; y=0; R=50;
	while(y<R):
		C_pre=COST(V,W,S,B);
		S=PERTURB(V,W,S,B,p);
		C_cur=COST(V,W,S,B);
		if(C_pre==C_cur):
			p=p-1;
		else:
			p=p0;
		
		if(COST(V,W,S,B)<COST(V,W,S_best,B)):
			S_best=list(S);
			y=y-R;
		else:
			y=y+1;
	
	return S_best
