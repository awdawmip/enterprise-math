from collections import Counter,defaultdict
from itertools import product
D='ABCD'; inv=dict(zip(D,'BADC'))
def J(w): return tuple(sorted(Counter(zip(w,w[1:])).items()))
def z(w): return (w.count('A')-w.count('B'),w.count('C')-w.count('D'))
def O(p,q): return (len(p),z(p),J(p),len(q),z(q),J(q),sum(x==y for x,y in zip(p,q)))
P1,P2,Q='AABAB','ABAAB','AAAAB'
assert O(P1,Q)==O(P2,Q) and P1[-2:]==P2[-2:]
assert P1[-3:]!=P2[-3:] and P1[-2]==inv[P1[-1]] and Q[-2]==inv[Q[-1]]
assert J(P1[:-2])!=J(P2[:-2])
P,Q1,Q2='AAAAAB','AABABA','ABAABA'
assert O(P,Q1)==O(P,Q2) and Q1[-3:]==Q2[-3:] and Q1[-4:]!=Q2[-4:]
assert P[-2]==inv[P[-1]] and Q1[-3]==inv[Q1[-2]] and Q2[-3]==inv[Q2[-2]]
assert O(P,Q1[:-1])==O(P,Q2[:-1])
assert J(Q1[:-3])!=J(Q2[:-3])
for n,keep in [(n,3) for n in range(1,6)]+[(n,2) for n in range(1,5)]:
    seen={}
    for c in product(D,repeat=n):
        w=''.join(c); k=(J(w),z(w),w[-keep:]);assert k not in seen or seen[k]==w
        seen[k]=w
# Independent exact native 12-direction BRC endpoint recurrence.
s={(0,)*6:(1,1)}
for n in range(1,7):
    nxt=defaultdict(lambda:[0,0])
    for at,(N,W) in s.items():
        for ax in range(6):
            for sign in (-1,1):
                v=list(at);v[ax]+=sign;v=tuple(v)
                weight=2 if ax==0 and sign==1 else 3 if ax==0 and sign==-1 else 1
                nxt[v][0]+=N;nxt[v][1]+=weight*W
    s={k:tuple(v) for k,v in nxt.items()}
    if n==5:
        assert s[(1,0,0,0,0,0)]==(1660,7020)
        assert s[(3,0,0,0,0,0)]==(105,1040)
    if n==6:
        assert s[(2,0,0,0,0,0)]==(4665,32760)
        assert s[(4,0,0,0,0,0)]==(156,2976)
print('P_SHARP: AABAB/ABAAB vs AAAAB; one CANCEL exposes AAB/ABA')
print('Q_SHARP: AAAAAB vs AABABA/ABAABA; POP_Q,CANCEL exposes AAB/ABA')
print('MIN_LENGTHS: P_tail2=5; Q_tail3=6 (ABCD exhaustive)')
print('N5_E1=1660 W5_E1=7020; N5_3E1=105 W5_3E1=1040')
print('N6_2E1=4665 W6_2E1=32760; N6_4E1=156 W6_4E1=2976')
print('STAGE406B_ASYMMETRIC_SUFFIX_PASS')
