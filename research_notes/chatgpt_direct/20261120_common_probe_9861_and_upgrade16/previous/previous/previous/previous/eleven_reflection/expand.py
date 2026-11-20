from pathlib import Path
from itertools import product,permutations
here=Path.cwd()
def mirror(i):return 25*((5-i//25)%5)+i%25
G=[]
for c,signs,p,t in product([1,2],product([-1,1],repeat=3),[(0,1,2),(0,2,1)],product(range(5),repeat=2)):
 a=[]
 for i in range(125):
  v=(i//25,i//5%5,i%5);u=[(c*signs[j]*v[p[j]]+((0,)+t)[j])%5 for j in range(3)];a.append(25*u[0]+5*u[1]+u[2])
 G.append(bytes(a))
assert len(set(G))==800
def move(m,g):return sum(1<<g[i]for i in m)
if __name__=='__main__':
 db={};orbits={}
 for line in (here/'root11rows').read_text().splitlines():
  *q,c=map(int,line.split())
  m=sum(1<<i for i in q);u=m|sum(1<<mirror(i)for i in q)
  if u in db and db[u][0]<=c:continue
  orb={}
  for g in G:
   a=move(q,g);b=move([mirror(i)for i in q],g);orb[a|b]=(c,a)
  rep=min(orb)
  for z,(cc,a) in orb.items():
   if z not in db or db[z][0]>cc:db[z]=cc,a
  orbits[rep]=True
 with (here/'all11').open('w')as out:
  for u,(c,m)in db.items():print(c,m%2**64,m>>64,file=out)
 with (here/'first11').open('w')as out:
  for x in sorted(orbits):
   c,m=db[x];print(m%2**64,m>>64,file=out)
 print('supports',len(db),'orbits',len(orbits))
