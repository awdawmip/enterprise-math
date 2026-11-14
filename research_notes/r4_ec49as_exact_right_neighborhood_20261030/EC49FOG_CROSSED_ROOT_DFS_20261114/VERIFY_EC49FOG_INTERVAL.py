"""Single-trace root05/root06 interval-bound certificate for EC49FOG.
Source: original frozen native signed-prefix word inventory; imports the exact original independent trie routine.
"""
from pathlib import Path
import sys,itertools,hashlib
import VERIFY_EC49FNY_INDEPENDENT as native
source=Path(sys.argv[1]);assert hashlib.sha256(source.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
words,a=native.frozen(source,32279);_,b=native.frozen(source,32315);R=(3,5,6,7)
D={(c,r):native.table(words,keys,r) for c,keys in enumerate((a,b)) for r in R}
for r in (5,6):assert D[0,r][0]==D[1,r][0]

def options(t):
    opts={l:[] for l in range(24)}
    for r in R:
        for l in t[r][0]: opts[l].append(r)
    assert all(opts.values());return opts

def order_for(c):
    t={r:D[c,r] for r in R};opts=options(t)
    one={l:min(t[r][2][1<<t[r][1][l]] for r in opts[l]) for l in opts}
    return tuple(sorted(opts,key=lambda l:(len(opts[l]),-one[l],l)))
orders=(order_for(0),order_for(1))

def check(x3,x7,o):
    T={3:D[x3,3],5:D[0,5],6:D[0,6],7:D[x7,7]}; O=orders[o]; opts=options(T)
    chosen=[]; mask={r:0 for r in R};n=0;pruned=0;safe_live=999;safe_cut=999;nontriv=0;maxwidth=0
    def dfs(d):
        nonlocal n,pruned,safe_live,safe_cut,nontriv,maxwidth
        n+=1
        fixed=T[3][2][mask[3]]+T[7][2][mask[7]]
        lo=hi=fixed
        for r in (5,6):
            ca=D[0,r][2][mask[r]];cb=D[1,r][2][mask[r]]
            lo+=min(ca,cb);hi+=max(ca,cb)
        base=sum(T[r][2][mask[r]] for r in R)
        assert lo<=base<=hi
        maxwidth=max(maxwidth,hi-lo)
        if hi!=lo:nontriv+=1
        if base>155:
            pruned+=1;safe_cut=min(safe_cut,lo-155)
            assert lo>155,(x3,x7,o,chosen,lo,hi)
            return
        safe_live=min(safe_live,155-hi)
        assert hi<=155,(x3,x7,o,chosen,lo,hi)
        if d==24:return
        l=O[d]
        for r in opts[l]:
            bit=1<<T[r][1][l];mask[r]|=bit;chosen.append(r);dfs(d+1);chosen.pop();mask[r]^=bit
    dfs(0)
    return n,pruned,safe_live,safe_cut,nontriv,maxwidth

print('root03_B root07_B order_B visits pruned min_live_slack min_cut_slack changed_interval_prefixes max_interval_width')
for x3,x7,o in itertools.product((0,1),repeat=3):
    print(x3,x7,o,*check(x3,x7,o))
print('EC49FOG_SINGLE_TRACE_INTERVAL_CERT_PASS 8 traces cover 32 root-table/priority configurations')
