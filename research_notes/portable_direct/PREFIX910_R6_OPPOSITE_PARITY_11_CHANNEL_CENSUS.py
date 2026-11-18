"""Independent Python 3 stdlib exact integer census for PREFIX-909."""
import math
L,H,N,Q=262145,524287,2**32,131072
T=33*N
old={2**h for h in range(1,18)}
for i in range(2,18):
 for j in range(1,i):old.update((2**i+2**j,2**i-2**j))
mid=set()
for m in range(3,8192,2):
 for i in range(2,18):
  for j in range(1,i):
   for v in (2**i+2**j,2**i-2**j):
    if v%m==0 and 0<v//m<=H-L and (v//m)%2==0 and v//m not in old:mid.add(v//m)
hi=set()
for m in range(1,8192,2):
 for i in range(18,31):
  for j in range(1,18):
   for v in (2**i+2**j,2**i-2**j):
    if v%m==0 and 0<v//m<=H-L and (v//m)%2==0 and v//m not in old and v//m not in mid:hi.add(v//m)
U={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285}
U.update(range(400011,400522,2));U.update(range(480011,480522,2))
for q in range(L,H+1,2):
 if any((2**h-1)%q==0 or (2**h+1)%q==0 for h in range(1,32)):U.add(q)
P={510000+t+194*r for t in (1,3,5) for r in range(64)}
D907={2**i+s*2**j for i in range(18,23) for j in range(1,18) for s in (-1,1)}
D908={2**i+s for i in range(1,20) for s in (-1,1)}
assert tuple(map(len,(old,mid,hi,U,P,D907,D908)))==(258,276,857,552,192,169,37)
gaps=old|mid|hi
def covered(a,b):
 return (a*b<T or a in U or b in U or (a//math.gcd(a,b))*b<N
  or 33*((N+a-1)//a)>b or 33*((N+b-1)//b)>a or a in P or b in P
  or abs(a-b) in gaps or 3*a-b in D907 or 3*b-a in D907
  or 2*a-b in D908 or 2*b-a in D908)
def enc(a,b):return ((a-L)//2)*Q+(b-L)//2
def dec(z):return L+2*(z//Q),L+2*(z%Q)
def trans(z):return (z%Q)*Q+z//Q

# PREFIX-910: full exact expansion; reuse C908 builder from verified PREFIX-909.
# Every old R909 member is checked in either orientation.
R909=set()
for k,ell in ((3,2),(4,1),(4,3)):
 for i in range(1,23):
  for s in (-1,1):
   d=2**i+s
   for a in range(L,H+1,2):
    b,r=divmod(k*a-d,ell)
    if r==0 and L<=b<=H and b%2==1:R909.add(enc(a,b))
assert len(R909)==1900472

families=((5,2),(5,4),(6,1),(6,5),(7,2),(7,4),(7,6),(8,1),(8,3),(8,5),(8,7))
results=[];new=set()
for k,ell in families:
 assert math.gcd(k,ell)==1 and (k-ell)%2==1 and k>ell
 seen=set();tests=0
 for i in range(1,23):
  for s in (-1,1):
   d=2**i+s
   for a in range(L,H+1,2):
    b,r=divmod(k*a-d,ell)
    if r or not(L<=b<=H) or b%2==0:continue
    x=1-k%2 if s==1 else k%2
    y=x+k*a
    assert 0<=x<N and 0<=y<N and 0<=x+2**i<N and 0<=y-s<N
    assert (x^2**i)==x+2**i and (y^1)==y-s
    assert y-x==k*a and (y-s)-(x+2**i)==ell*b
    seen.add(enc(a,b));tests+=1
 fresh={z for z in seen if z not in R909 and trans(z) not in R909 and not covered(*dec(z))}
 results.append((k,ell,tests,len(seen),len(fresh)))
 new.update(fresh)
overlap=sum(trans(z) in new for z in new)
added=2*len(new)-overlap
expected=[
 (5,2,78643,78643,34493),(5,4,812650,792989,408202),
 (6,1,43690,43690,27887),(6,5,716531,699055,364840),
 (7,2,56174,56174,27775),(7,4,271508,266826,116177),
 (7,6,636632,621029,325427),(8,1,32768,32768,9371),
 (8,3,54613,54613,26551),(8,5,327680,321127,149296),
 (8,7,575775,561732,295775)]
assert results==expected
assert (len(new),overlap,added)==(1785732,8,3571456)
assert (7780668986+added,Q*Q-7780668986-added)==(7784240442,9395628742)
print('PREFIX910_PYTHON_EXACT_PASS',results,'oriented',len(new),'transpose',overlap,'added',added,'C910',7780668986+added)
