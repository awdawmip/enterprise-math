"""EC49EXH fixed H8/M4/S6 twenty-color native-prefix trie generator."""
from collections import Counter
from pathlib import Path
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
H=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')
T4=(1836687,1867942,1872656,1873981)
T2=(1836425,1866380)
K={2:(3,1,1),3:(3,1,1),4:(4,2,1),5:(4,2,1),6:(5,3,1),7:(5,3,1),8:(5,4,1)}
T={2:T4,3:T2,4:T4,5:T2,6:T4,7:T2,8:T2}
BASE=('ce','de','ec','ed')
def native(w):return tuple(x for c in w for x in OPS[c])
def sig(st):
    val=0;pow5=1
    for ev,prev in H:
        for s in st:
            if prev==1 and s==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            elif prev==2 and s==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            prev=s
        val+=BUCKETS.index(ev)*pow5;pow5*=5
    return val
def permutations(ct,prefix=''):
    if not sum(ct.values()):yield prefix;return
    for c in sorted(ct):
        if ct[c]:
            ct[c]-=1
            yield from permutations(ct,prefix+c)
            ct[c]+=1
def fiber(h,key):
    u,v,w=key
    r=u+v-h-1;na=w-1;nf=u-r-2*w;ng=v-r
    if min(r,na,nf,ng)<0:return
    for nc in range(r+1):
        ct=Counter({'a':na,'c':nc,'d':r-nc,'e':w,'f':nf,'g':ng})
        for word in permutations(ct):
            st=native(word)
            assert len(word)==h
            assert tuple(st.count(i)-st.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
            assert tuple(st.count(i) for i in range(1,7))==key+(0,0,0)
            yield word,st,sig(st)
def build():
    parents=[-1];kids=[{}];colors=[0];prepaid=[0];counts={}
    for h in range(2,9):
        counts[h]=0
        for word,st,s in fiber(h,K[h]):
            if s not in T[h]:continue
            counts[h]+=1;v=0
            for a in st:
                if a not in kids[v]:
                    kids[v][a]=len(parents)
                    parents.append(v);kids.append({});colors.append(0);prepaid.append(0)
                v=kids[v][a]
            bit=sum(len(T[j]) for j in range(2,h))+T[h].index(s)
            colors[v]|=1<<bit
    for word in BASE:
        v=0
        for a in native(word):v=kids[v][a];prepaid[v]=1
    assert len(parents)==4101 and sum(prepaid)==28
    assert counts=={2:4,3:4,4:48,5:24,6:360,7:120,8:245}
    return parents,prepaid,colors
if __name__=='__main__':
    p,b,m=build()
    dst=Path(__file__).with_name('EC49EXH_FIXED_DP_INPUT.txt')
    with dst.open('w') as f:
        f.write(f'{len(p)} 20\n')
        for a,x,y in zip(p,b,m):f.write(f'{a} {x} {y}\n')
    print(f'PASS trie_nodes={len(p)} colors=20 h2_prepaid=28 file={dst}')
