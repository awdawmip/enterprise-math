from pathlib import Path
from fractions import Fraction as F
from math import floor, ceil
import hashlib, json
exec(Path('prefix1128_verify.py').read_text().split('L0=10**90')[0])
G=10**100
cert=json.load(open('prefix1129_compact.json'))
lines,_,volume=scan(10**100,3*10**60,V2)
assert volume==620 and len(lines)==len(cert['centers'])==115
cols=tuple(tuple(map(int,row)) for row in cert['columns']);error=tuple(map(int,cert['uniform_error']))
centers=[tuple(map(int,row)) for row in cert['centers']]
assert len(cols)==12 and all(v>=0 for v in error) and any(a*d-b*c for a,b in cols for c,d in cols)
ns=[(-b,a) for a,b in cols+((1,0),(0,1)) if a or b]
mins=[min(F(sum(abs(x*a+y*b) for a,b in cols)-abs(x*c[0]+y*c[1])-abs(x)*error[0]-abs(y)*error[1],max(abs(x),abs(y))*G) for x,y in ns) for c in centers]
assert min(mins)>F(9671,10**89)
print('compact exact support:',len(mins),'min',float(min(mins)),'row',mins.index(min(mins))+1,'first',float(mins[0]))
# Optional replay provenance: verify every rounding payment against actual detailed output.
raw=Path('direct_all.jsonl')
if raw.exists():
    assert hashlib.sha256(raw.read_bytes()).hexdigest()==cert['source_raw_sha256']
    rows=[json.loads(line) for line in raw.read_text().splitlines()]
    assert len(rows)==len(lines)
    for line,c,r in zip(lines,centers,rows):
        assert line==tuple(int(r[k]) for k in ('q','p','h'))
        assert c==tuple(floor(F(v)*G) for v in r['cent'])
        assert cols==tuple(tuple(floor(F(v)*G) for v in col) for col in r['cols'])
        assert all(ceil(F(r['error'][i])*G)+len(cols)+1<=error[i] for i in range(2))
    print('all original rows and rounding payments verified')
