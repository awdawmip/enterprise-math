"""Independent exact-rational observer witness and full signed-X6 prefix check."""
from fractions import Fraction
from collections import Counter
import json
OP={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
H=(('N',0),('N',1),('N',2),('A',0),('A',2),('B',0),('B',1),('AB',0),('BA',0))
B=('N','A','B','AB','BA')
W={2:('ce','de','ec','ed'),3:('feg','gef'),4:('fegd','gefd','gefc','fegc'),5:('fegfg','geffg'),6:('geffgd','geffgc','fegfgd','fegfgc'),7:('fegfgfg','geffgfg'),8:('fegfgfgg','geffgfgg')}
def trans(st):
    out=[]
    for ev,prev in H:
        for s in st:
            if prev==1 and s==2:
                if ev=='N':ev='A'
                elif ev=='B':ev='BA'
            elif prev==2 and s==1:
                if ev=='N':ev='B'
                elif ev=='A':ev='AB'
            prev=s
        out.append(B.index(ev))
    return tuple(out)
def rank(a):
    a=[[Fraction(x) for x in row] for row in a];r=0
    for c in range(len(a[0])):
        k=next((i for i in range(r,len(a)) if a[i][c]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];q=a[r][c]
        a[r]=[v/q for v in a[r]]
        for j in range(r+1,len(a)):
            z=a[j][c]
            if z:a[j]=[v-z*w for v,w in zip(a[j],a[r])]
        r+=1
        if r==len(a):break
    return r
def main():
    paid=set();keys=set();sigs=set();rows=[]
    for h,words in W.items():
        kk=set();ss=set();before=len(paid)
        for w in words:
            assert len(w)==h
            st=tuple(s for op in w for s in OP[op])
            pos=tuple(st.count(i) for i in range(1,7))
            assert tuple(st.count(i)-st.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
            kk.add(pos);ss.add(trans(st))
            paid.update(st[:j] for j in range(1,len(st)+1))
        assert len(kk)==1
        a=[[int(s[j]==b) for s in sorted(ss) for b in range(5)] for j in range(9)]
        assert rank(a)==9
        keys.update(kk);sigs.update(ss)
        rows.append({'h':h,'new_edges':len(paid)-before,'E':len(paid),'rankQ':9,'words':list(words)})
    assert (len(paid),len(keys),len(sigs))==(90,4,6)
    result={'status':'PASS','unit':'EC49EXH','E':90,'M':4,'S':6,'rows':rows}
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
