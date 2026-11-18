"""EC49EXG: exact finite support/optimistic-DP and rational witness checks."""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
import json

O={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
   'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
H=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
B=('N','A','B','AB','BA');T=(1836687,1867942,1872656,1873981)
K={2:(3,1,1),3:(4,2,1),4:(4,2,1),5:(6,4,1),6:(6,4,1),7:(6,4,1),8:(6,4,1)}
W={2:('ed','de','ec','ce'),3:('edd','ded','ecc','cec'),
   4:('edgf','degf','ecfg','cefg'),5:('edddd','deddd','ecccc','ceccc'),
   6:('edddgf','deddgf','ecccfg','ceccfg'),
   7:('edgffgd','degfgfd','ecfggfc','cefgfgc'),
   8:('edgffggf','degfgfgf','ecfggffg','cefgfgfg')}
def steps(w):return tuple(i for c in w for i in O[c])
def signature(st):
    out=0;f=1
    for ev,last in H:
        for s in st:
            if last==1 and s==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            elif last==2 and s==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            last=s
        out+=B.index(ev)*f;f*=5
    return out
def unique_words(count,prefix=''):
    if not sum(count.values()):yield prefix;return
    for ch in sorted(count):
        if count[ch]:
            count[ch]-=1;yield from unique_words(count,prefix+ch);count[ch]+=1
def fiber(h,key):
    u,v,w=key;r=u+v-h-1;a=w-1;f=u-r-2*w;g=v-r
    if min(r,a,f,g)<0:return
    for c in range(r+1):
        ct=Counter({'a':a,'c':c,'d':r-c,'e':w,'f':f,'g':g})
        for word in unique_words(ct):
            st=steps(word);s=signature(st)
            if s in T:yield word,st,s
def possible(h):
    out=set()
    for w in range(1,(h+1)//2+1):
        for r in range(h-2*w+2):
            for f in range(h-(2*w-1)-r+1):
                g=h-(2*w-1)-r-f;out.add((r+2*w+f,r+g,w))
    return out
def rank9(signatures):
    m=[[Fraction(int((s//5**i)%5==b)) for s in signatures for b in range(5)] for i in range(9)]
    row=0
    for col in range(len(m[0])):
        z=next((i for i in range(row,9) if m[i][col]),None)
        if z is None:continue
        m[row],m[z]=m[z],m[row];v=m[row][col]
        for j in range(col,len(m[0])):m[row][j]/=v
        for i in range(row+1,9):
            v=m[i][col]
            if v:
                for j in range(col,len(m[0])):m[i][j]-=v*m[row][j]
        row+=1
        if row==9:break
    return row
def main():
    avail={}
    for h in range(2,9):
        avail[h]={k for k in possible(h) if {s for _,_,s in fiber(h,k)}==set(T)}
    assert [len(avail[h]) for h in range(2,9)]==[1,3,7,13,22,34,50]
    pairs=[(a,b) for a in avail[3] for b in avail[8] if a!=b
           and all(a in avail[h] or b in avail[h] for h in range(3,9))]
    assert pairs==[((4,2,1),(6,4,1))]
    for h in range(3,9):assert [k for k in pairs[0] if k in avail[h]]==[K[h]]
    free=set()
    for h in range(2,8):
        for word,st,s in fiber(h,K[h]):free.update(st[:i] for i in range(1,len(st)+1))
    children=[{}];masks=[0];pref=[()];sigcounts=Counter()
    for word,st,s in fiber(8,K[8]):
        sigcounts[s]+=1;node=0
        for step in st:
            if step not in children[node]:
                children[node][step]=len(children)
                children.append({});masks.append(0);pref.append(pref[node]+(step,))
            node=children[node][step]
        masks[node]|=1<<T.index(s)
    @lru_cache(None)
    def dp(v):
        d={0:0}
        if masks[v]:d[masks[v]]=0
        for u in children[v].values():
            nxt={}
            for x,cx in d.items():
                for y,cy in dp(u).items():
                    q=x|y;cost=cx+cy+int(bool(y) and pref[u] not in free)
                    nxt[q]=min(nxt.get(q,10**9),cost)
            d=nxt
        return d
    assert len(children)==15887 and len(free)==11116
    assert sigcounts==Counter({s:560 for s in T})
    new=dp(0)[15];assert new==12
    paid=set();keys=set();signs=set();rows=[]
    for h in range(2,9):
        ks=set();sg=set();before=len(paid)
        for word in W[h]:
            st=steps(word)
            assert len(word)==h and tuple(st.count(i)-st.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
            ks.add(tuple(st.count(i) for i in range(1,7)));sg.add(signature(st))
            paid.update(st[:i] for i in range(1,len(st)+1))
        assert ks=={K[h]+(0,0,0)} and sg==set(T) and rank9(tuple(sg))==9
        keys.update(ks);signs.update(sg)
        rows.append({'h':h,'key':K[h],'words':W[h],'new_edges':len(paid)-before,'E_to_h':len(paid)})
    assert len(paid)==144 and len(keys)==3 and len(signs)==4
    print(json.dumps({'status':'PASS','T4_fiber_counts':[len(avail[h]) for h in range(2,9)],
         'unique_keys':K,'H8_candidates':sum(sigcounts.values()),'H8_trie_nodes':len(children),
         'earlier_free_edges':len(free),'exact_optimistic_H8_new_edges':new,
         'H7_inherited_exact_E':128,'rigorous_lower_E':140,'witness_E':144,
         'witness_M':3,'witness_S':4,'witness_rational_rank':9,'rows':rows},indent=2))
if __name__=='__main__':main()
