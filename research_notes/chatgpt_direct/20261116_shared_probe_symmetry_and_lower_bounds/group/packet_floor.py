"""A single four-class orbit under an order-four linear map; other classes unrestricted."""
from pathlib import Path
import sys
from generate import maps
from single_orbit import bits

def make(work,length=4):
 lin,trans,_=maps()
 eye=bytes(range(125))
 generators=sorted({a for a in lin if bytes(a[a[i]]for i in range(125))==bytes((25*((-(i//25))%5)+5*((-(i//5%5))%5)+((-i)%5)) for i in range(125))})
 # The canonical map (x,y,z) -> (2z,2y,2x) generates the witness stabilizer.
 perm=bytes(25*((2*(i%5))%5)+5*((2*(i//5%5))%5)+(2*(i//25))%5 for i in range(125))
 assert perm in generators
 subgroup={eye,perm};q=perm
 for j in range(2):
    q=bytes(perm[q[i]]for i in range(125));subgroup.add(q)
 assert len(subgroup)==4
 normalizer=[g for g in lin if any(all(g[perm[i]]==d[g[i]]for i in range(125))for d in subgroup)]
 counter={}
 with (work/'bank').open()as f,(work/f'neighbor{length}_rot').open('w')as out:
    for k in range(int(next(f))):
     s,c,n=map(int,next(f).split());masks=[]
     for _ in range(n):
        lo,hi=map(int,next(f).split());masks.append(lo|hi<<64)
     if c not in (557,744):continue
     data={}
     for m in masks:
        pts=list(bits(m));allm=[sum(1<<g[i]for i in pts)for g in subgroup if length==4 or g!=eye]
        if len(set(allm))==length and not any(x&y for j,x in enumerate(allm)for y in allm[:j]):
            u=sum(allm);data[u]=allm
     count=0
     while data:
        u=next(iter(data));allm=data[u];pts=list(bits(u))
        for g in normalizer:data.pop(sum(1<<g[i]for i in pts),None)
        print(0,u%(1<<64),u>>64,*[z for m in allm for z in (m%(1<<64),m>>64)],*[k]*length,file=out)
        count+=1
     counter[c]=count
 print(counter,flush=True)
if __name__=='__main__':make(Path(sys.argv[1]),int(sys.argv[2]) if len(sys.argv)>2 else 4)
