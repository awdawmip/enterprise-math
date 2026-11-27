from fractions import Fraction as F
from pathlib import Path
from prefix1116_lattice import sweep,stats,expand
import json,hashlib
G=10**85;E=400000
old=json.load(open('root_8800_result.json'));new=json.load(open('root_9200_only.json'));R,C,T=[tuple(F(int(x),G) for x in old[k]) for k in ('rho','c','d')];R2=tuple(F(int(x),G) for x in new['rho']);assert R[0]<R2[0]<=R2[1]<R[1]
prev=json.load(open('prefix1117_result.json'));pairs=prev['remaining'];assert len(pairs)==122
cnt={-1:0,0:0,1:0};gaps=[];results=[]
mid=[int((a+b)*G/2) for a,b in (R2,C,T)]
def pred(m):return (mid[0]*m*m+mid[1]*m+mid[2])//(G*m)
for m,j in pairs:
 l=R2[0]*m+C[0]+T[0]/m-F(E,m*m);u=R2[1]*m+C[1]+T[1]/m+F(E,m*m);s=-1 if l>j else 1 if u<j else 0;cnt[s]+=1
 assert s and u-l<1 and pred(m)==(j if s==-1 else j-1)
 gap=l-j if s==-1 else j-u;gaps.append(gap);results.append([m,j,s,str(gap)])
end=prev['end'];w=sweep((R2,C,T),10**8,end);a=sorted(p for x in w for p in expand(x));assert not a and len(w)==107
assert (R2[1]-R2[0])*end+(C[1]-C[0])+(T[1]-T[0])/10**8+F(2*E,10**16)<1
# Extend only until the first new ambiguity window, avoid large enumeration.
ext=[];a=[]
for i in range(10):
 ww=sweep((R2,C,T),end*2**i,end*2**(i+1));ext+=ww;a+=sorted(p for x in ww for p in expand(x))
 if a:break
assert a;first=min(a)[0];end2=ext[-1]['H']+1
assert (R2[1]-R2[0])*end2+(C[1]-C[0])+(T[1]-T[0])/10**8+F(2*E,10**16)<1
print('factor',float((R[1]-R[0])/(R2[1]-R2[0])),'counts',cnt,'min gap',float(min(gaps)))
print('sweep',stats(w),'extension',stats(ext),'counts',[x['count'] for x in ext],'first',min(a),'end',end2)
print('mid',mid)
Path('prefix1122_window_result.json').write_text(json.dumps(dict(counts=cnt,min_gap=str(min(gaps)),old_resolved=results,old_stats=stats(w),old_end=end,extension=ext,remaining=a,first=min(a),end=end2,mid=mid),indent=2)+'\n')
