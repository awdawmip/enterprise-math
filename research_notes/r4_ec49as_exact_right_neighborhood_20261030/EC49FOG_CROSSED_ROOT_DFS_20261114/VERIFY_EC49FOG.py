"""EC49FOG exact 32-counterfactual certificate.
Requires VERIFY_EC49FNY_INDEPENDENT.py from EC49FOF PR #2375
and frozen master_and_radius3_cases.txt, whose SHA256 is checked.
Run: python VERIFY_EC49FOG.py master_and_radius3_cases.txt
"""
import hashlib,itertools,sys
from pathlib import Path
from fractions import Fraction
import VERIFY_EC49FNY_INDEPENDENT as native

path=Path(sys.argv[1]); assert hashlib.sha256(path.read_bytes()).hexdigest()==('cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e')
root=(3,5,6,7); caches=(32279,32315); words,keysA=native.frozen(path,caches[0]); _,keysB=native.frozen(path,caches[1]); keys=(keysA,keysB)
table={(c,r):native.table(words,keys[c],r) for c in range(2) for r in root}

def options(t):
    o={l:[] for l in range(24)}
    for r in root:
        for l in t[r][0]:o[l].append(r)
    assert all(o.values())
    return o

def sort_order(c):
    t={r:table[c,r] for r in root};opt=options(t)
    one={l:min(t[r][2][1<<t[r][1][l]] for r in opt[l]) for l in opt}
    return tuple(sorted(opt,key=lambda l:(len(opt[l]),-one[l],l)))
orders=(sort_order(0),sort_order(1))

def walk(t,order):
    opt=options(t); masks={r:0 for r in root};path=[];trace=[]
    counts=[0,0,0,0] # visits, pruned, successful leaves, pruned leaves
    def dfs(d):
        counts[0]+=1
        cutoff=sum(t[r][2][masks[r]] for r in root)>155
        trace.append((tuple(path),cutoff))
        if cutoff:
            counts[1]+=1
            if d==24:counts[3]+=1
            return
        if d==24:counts[2]+=1;return
        l=order[d]
        for r in opt[l]:
            bit=1<<t[r][1][l];masks[r]|=bit;path.append(r)
            dfs(d+1)
            path.pop();masks[r]^=bit
    dfs(0)
    return tuple(counts),tuple(trace)

results={};traces={}
for mask in range(16):
    t={r:table[(mask>>j)&1,r] for j,r in enumerate(root)}
    for order in (0,1):
        results[mask,order],traces[mask,order]=walk(t,orders[order])
        print('CASE',mask,caches[order],*results[mask,order])
for x03,x07,order in itertools.product((0,1),repeat=3):
    group=[traces[x03+2*x05+4*x06+8*x07,order] for x05,x06 in itertools.product((0,1),repeat=2)]
    assert all(t==group[0] for t in group)
V={(x03,x07,o):results[x03+8*x07,o][0] for x03,x07,o in itertools.product((0,1),repeat=3)}
assert V=={(0,0,0):436,(0,0,1):397,(1,0,0):259,(1,0,1):206,(0,1,0):418,(0,1,1):361,(1,1,0):245,(1,1,1):173}
assert sum(table[0,5][2][i]!=table[1,5][2][i] for i in range(2048))==308
assert sum(table[0,6][2][i]!=table[1,6][2][i] for i in range(4096))==3
sh=[]
for i in range(3):
    value=Fraction(0)
    for bits in itertools.product((0,1),repeat=3):
        if bits[i]:continue
        more=list(bits);more[i]=1
        k=sum(bits);weight=(Fraction(1,3) if k in (0,2) else Fraction(1,6))
        value+=weight*(V[tuple(more)]-V[bits])
    sh.append(value)
assert sh==[Fraction(-547,3),Fraction(-76,3),Fraction(-166,3)]
print('EXACT_PASS cases=32, 8 reduced traces, root05_changed_masks=308, root06_changed_masks=3, Shapley=',sh)
