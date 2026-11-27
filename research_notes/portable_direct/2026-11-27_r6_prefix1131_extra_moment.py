from replay_9600_n300_gmp import *
from math import floor,ceil
from itertools import combinations
H=10**120; G=10**125
pkt=json.load(open('anchor_compact.json')); cc=[F(int(x),H) for x in pkt['center']]; W=[[F(int(x),10**140) for x in row] for row in pkt['weighted_columns_rows']];dr=[F(int(x),10**140) for x in pkt['rounding_radii']]
old=json.load(open('three_compact.json'));m=old['m']; C=old['cols'];e=old['error']
vals=list(map(int,open('new_moments.txt').read().split()));ks=[10000,10400,10800]
eb=sum(b[3] for b in basis)+F(4*(N+1)+1,H)
def down(x):
 a,b=x;v=floor(a*H);assert v==floor(b*H);return F(v,H)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
rows=[]
for k,val in zip(ks,vals):
 ints={i:integ(k,i,N+5) for i in (0,1)};row=[]
 for a,z,h,err,T in basis:
  off=int(a);half=int(2*(a-off));row.append(sum(down(c[0]*ints[half][off+n]) for n,c in enumerate(z)))
 row += [F(0)]*2
 center=dot(row,cc)-F(val,H);cols=[sum(row[i]*W[i][j] for i in range(6)) for j in range(6)]+[row[i]*dr[i] for i in range(6)]
 err=F(35,36)**k+F(1,H)+eb
 rr=dict(k=k, row=list(map(str,row)), observation=str(F(val,H)),m=floor(center*G),cols=[floor(x*G) for x in cols],error=ceil(err*G)+13)
 rows.append(rr);print(k,'center',float(center),'error',float(err),'cols',list(map(float,cols)),flush=True)
 json.dump(rows,open('extra_rows.json','w'))
