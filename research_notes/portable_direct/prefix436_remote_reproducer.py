"""PREFIX-436 exact signed-X6 BRC / auxiliary C4 path certificate (stdlib only)."""
from pathlib import Path
import hashlib, importlib.util, itertools, math, os
p = Path(os.environ.get('BRC_SOURCE_PATH', str(Path(__file__).resolve().parents[2] / 'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py')))
b = p.read_bytes()
blob = hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()
assert blob == '300a96e3dc24bf6fff73743037a0347a8bc83176'
spec = importlib.util.spec_from_file_location('signed_brc_exact_prefix436', p)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def hist(a, b, start=0):
    h = [[(0,0,0,0) for _ in range(b+1)] for _ in range(a+1)]
    h[0][0]=(1,0,0,0)
    for i in range(a+1):
        for j in range(b+1):
            if i<a:
                h[i+1][j]=tuple(x+y for x,y in zip(h[i+1][j],h[i][j]))
            if j<b:
                v=list(h[i][j]); t=(start+i)%4
                v=v[-t:]+v[:-t] if t else v
                h[i][j+1]=tuple(x+y for x,y in zip(h[i][j+1],v))
    return h[a][b]

def amp(h):
    return (h[0]-h[2],h[1]-h[3])

def closed(a,b):
    N,r=divmod(a+b,4); K,s=divmod(a,4)
    if s>r:return (0,0)
    c=math.comb(N,K)
    if (r,s)==(2,1):return (c,c)
    if r==3 and s in (1,2):return (0,c)
    return (c,0)

for a in range(31):
    for b in range(31):
        h=hist(a,b)
        assert sum(h)==m.shortest_path_multiplicity((a,b,0,0,0,0))
        assert amp(h)==closed(a,b)

for a in range(11):
    for b in range(11-a):
        for start in (-3,0,2):
            counts=[0]*4
            for apos in itertools.combinations(range(a+b),a):
                apos=set(apos); seen_a=0; t=0
                for j in range(a+b):
                    if j in apos:seen_a+=1
                    else:t=(t+start+seen_a)%4
                counts[t]+=1
            assert hist(a,b,start)==tuple(counts)

unit=(1,)*6
for a,b in ((1,1),(1,3),(2,2),(4,4),(5,7)):
    v=(a,b,0,0,0,0)
    assert m.endpoint_weight(a+b,v,unit,unit)==m.shortest_path_multiplicity(v)
    print('CASE',a,b,'N',sum(hist(a,b)),'h',hist(a,b),'E',amp(hist(a,b)))
assert hist(1,3)==(1,1,1,1)

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def c(x,y):return (x[0]*y[1])%4
P=list(itertools.product(range(-2,3),repeat=2))
for d,e,f in itertools.product(P,repeat=3):
    assert (c(d,e)+c(add(d,e),f)-c(e,f)-c(d,add(e,f)))%4==0
for s in (-3,-2,0,1,3):
    for a,b in ((1,1),(1,3),(4,4)):
        h=hist(a,b,s); z=amp(h); v=amp(hist(a,b))
        assert z[0]*z[0]+z[1]*z[1]==v[0]*v[0]+v[1]*v[1]
assert c((1,0),(0,1))==1 and c((0,1),(1,0))==0
print('PASS_PREFIX436_LOCAL_REPRODUCER: 961 DP; 198 word-enumerations; 15625 cocycle triples; signed BRC exact blob',blob)
