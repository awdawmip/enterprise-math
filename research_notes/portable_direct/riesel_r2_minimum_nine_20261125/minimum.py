from pathlib import Path
from collections import Counter
from functools import cache
from math import gcd,lcm
from itertools import product
import json,sys
import zero_input as z
A=9807947978443488306255509703402695727949968778703073231931137913705883712843
S=11356718000553566643685496313583434507970452519839503606327232707476034989690
P=(7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417)
Q0=(5,13,19,73)
HI=(2521,1711081,430839361,15169173997557864184867895400813639018421,17369459529909057773233442461)
dir0=Path(__file__).parent
def read(n):return json.loads((dir0/n).read_text())
inv=read('low_inventory.json')
F={int(q):r['f'] for r in inv for q in r['primeFactors']}|{q:105 for q in HI}
D={int(q):r['d'] for r in inv for q in r['primeFactors']}|{q:1260 for q in HI}
G=read('templates.json');H={int(h):tuple(qs) for h,qs in G['by_h'].items()}
G8=read('eight_templates.json')['types']
W8={int(q):r[0] for r in read('eight_inventory.json').values() for q in r[2]}
FIX={(3,0):19,(3,1):73,(6,5):38737}
@cache
def r(q,b):
    u=pow(2,-(4+6*b),q);si=pow(S,-1,q)
    return tuple(sorted({(u-A)*si%q,(-u-A)*si%q}))
@cache
def lower_budget(k):
    a=A+S*k;answer=set(FIX)
    for q,f in W8.items():
        x=a*a*256%q
        for b in range(f):
            if x==1:answer.add((f,b));break
            x=x*4096%q
    return next((len(t)+2 for t in sorted(G8,key=len) if all(tuple(s) in answer for s in t)),None)
def options(qs,b,is_w=False):
    return tuple(sorted((x,q, (2+3*b if is_w else b)%F[q]) for q in qs for x in r(q,(2+3*b if is_w else b)%F[q])))
C=[tuple(options(tuple(z.GROUPS[group]),b) for group,b in x['slots']) for x in z.patterns()[5:]]
W=[tuple(options(H[h],b,True) for h,b in t if h!=2) for t in G['shapes'] if len(t)==5]
GE=H[7]+H[35]+HI
T=[]
for j in range(3):
    T.append(tuple([options(H[5],b,True) for b in (0,3)]+[options(HI if i==j else GE,b,True) for i,b in enumerate((21,26,31))]))
assert (len(C),len(W),len(T))==(42,215,3)
def inspect(k,slots,tag,i):
    if tag=='C':ps=list(P)+(list(Q0[:2]))
    else:
        ps=list(P)+list(Q0)
        if tag=='W' and [2,1] in [t for t in G['shapes'] if len(t)==5][i]:ps.append(38737)
    ps+= [s[1] for s in slots]
    assert len(ps)==29 and len(set(ps))==29
    a=A+S*k
    ords={q:next(d for d in range(1,100000) if pow(2,d,q)==1) for q in ps}
    per=lcm(*ords.values())
    all0=(1<<per)-1;ms={}
    for q in ps:
        x=a*a%q
        ans=0
        for j in range(ords[q]):
            if x==1:
                repeat=((1<<per)-1)//((1<<ords[q])-1)
                ans|=repeat<<j
            x=x*2%q
        ms[q]=ans
    hit=0
    for x in ms.values():hit|=x
    assert hit==all0
    holes=[]
    for q in ps:
        hit=0
        for p,x in ms.items():
            if p!=q:hit|=x
        if hit!=all0:holes.append([q, ((all0&~hit)&-(all0&~hit)).bit_length()-1 or per])
    return dict(root=str(a),k=k,supplement=ps[20:],tail_slots=slots,geometry=[tag,i],cover_period=per,
                private_indices=holes,all_old_survive_single_deletion=[q for q in P if q not in [x[0] for x in holes]])
def search(cap,entries):
    stats=Counter(); best=cap; record=None
    def visit(res,mod,slots,left,tag,i,used):
        nonlocal best,record
        stats['nodes']+=1
        if not left:
            for k in range(res,best,mod):
                stats['complete_under_bound']+=1
                if lower_budget(k) is None:
                    best=k; record=(i,tag,slots)
                    stats['improvements']+=1
                    break
            return
        # Fewest compatible signed classes under current bound is an exact branching heuristic.
        branch=None
        for j,x in enumerate(left):
            cut=[]
            for b,q,p in x:
                if q in used:continue
                if mod>=best:
                    if res%q==b:cut.append((res,q,p))
                else:
                    x1=res+mod*((b-res)*invmod(mod,q)%q)
                    if x1<best: cut.append((x1,q,p))
            if not cut:stats['empty_pruned']+=1;return
            if branch is None or len(cut)<len(branch[1]):
                branch=(j,cut)
                if len(cut)==1:break
        j,x=branch
        for k,q,p in sorted(x):
            if k>=best:break
            visit(k,mod*q,slots+[(k%q,q,p)],left[:j]+left[j+1:],tag,i,used|{q})
    for tag,L in entries:
        for i,t in enumerate(L):visit(0,1,[],t,tag,i,set())
    answer=inspect(best,record[2],record[1],record[0]) if record else None
    return {'cap':cap,'stats':dict(stats),'answer':answer}
@cache
def invmod(m,q):return pow(m,-1,q)
if __name__=='__main__':
  bound=int(sys.argv[1]) if len(sys.argv)>1 else 10**9
  result={tag:search(bound,[(tag,shapes)]) for tag,shapes in (('W',W),('C',C),('T',T))}
  result['global']=search(bound,[('W',W),('C',C),('T',T)])
  print(json.dumps(result,indent=2))
