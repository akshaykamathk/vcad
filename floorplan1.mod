
param n integer > 0;	
set count := 1..n;
 	
param wvar{count} integer >=0;
param hvar{count} integer >=0;

param wmin integer >=0 ;

var x{count}, >=0 , integer;
var y{count}, >=0 , integer;

var z{count}, >=0 , binary;
var p{count,count}, >=0 , binary; 
var q{count,count}, >=0 , binary; 

param M integer >=0;

var ymin integer >=0 ;

minimize obj: ymin;

s.t. check1 {i in count} : x[i] + z[i]*hvar[i] + (1 - z[i])*wvar[i] <= wmin;
s.t. check2 {i in count} : y[i] + z[i]*wvar[i] + (1 - z[i])*hvar[i] <= ymin;
s.t. check3 {i in count, j in count}: if(i < j) then x[i] + z[i]*hvar[i] + (1 - z[i])*wvar[i] <= x[j] + M*(p[i,j] + q[i,j]);
s.t. check4 {i in count, j in count}: if(i < j) then x[i] - z[j]*hvar[j] - (1 - z[j])*wvar[j] >= x[j] - M*(1 - p[i,j] + q[i,j]);
s.t. check5 {i in count, j in count}: if(i < j) then y[i] + z[i]*wvar[i] + (1 - z[i])*hvar[i] <= y[j] + M*(1 + p[i,j] - q[i,j]);
s.t. check6 {i in count, j in count}: if(i < j) then y[i] - z[j]*wvar[j] - (1 - z[j])*hvar[j] >= y[j] - M*(2 - p[i,j] - q[i,j]);
s.t. check7 {i in count}: x[i] >=0;
s.t. check8 {i in count}: y[i] >=0;


solve;

printf "wchip = %i\nhchip = %i\n\n", wmin, ymin;

printf "Module x  y  w  h\n\n";

for {i in count}
{
for {0..0: not z[i]}
{

printf "%i      %i  %i %i  %i\n" ,i, x[i], y[i], wvar[i],hvar[i];

}

for {0..0: z[i]}
{

printf "%i      %i  %i %i  %i\n" ,i, x[i], y[i], hvar[i],wvar[i];

}


}

/*
data;

param n := 4;

param wvar :=
	     1 4
	     2 3 
	     3 6 
	     4 7 ;

param hvar :=
	      1 5 
	      2 7 
	      3 4 
	      4 8;

param wmin := 8;

param M:= 24;

end;
*/
