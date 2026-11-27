from fractions import Fraction as F
P={(0,0):F(1,16),(0,1):F(3,16),(1,0):F(9,16),(1,1):F(3,16)}
Q={(0,0):F(1,9),(0,1):F(2,9),(1,0):F(4,9),(1,1):F(2,9)}
sets={
'A':[(F(1,2),F(0),F(1,4)),(F(1,2),F(0),F(3,4))],
'B':[(F(1,5),F(0),F(0)),(F(4,5),F(0),F(5,8))],
'C':[(F(4,5),F(0),F(3,8)),(F(1,5),F(0),F(1))],
}
def moments(s):
    return tuple(sum(w*f(x,y) for w,x,y in s) for f in
      (lambda x,y:x,lambda x,y:y,lambda x,y:y*y,lambda x,y:y**3,
       lambda x,y:x*y,lambda x,y:x*y*y,lambda x,y:x*y**3))
def law(s,src):
    out={}
    for w,x,y in s:
        for u in (0,1):
            for (r,t),p in src.items():
                for name,v in [('A',1-y),('B',y*(1-y)),('C',y*y*(1-y)),('D',y**3)]:
                    key=(u,r,t,r^u,name)
                    out[key]=out.get(key,F(0))+w*(x if u else 1-x)*p*v
    assert len(out)==32 and sum(out.values())==1
    return out
def tv(p,q):
    return sum(abs(p[k]-q[k]) for k in p)/2
ms={name:moments(s) for name,s in sets.items()}
assert all(m[:3]==(0,F(1,2),F(5,16)) and m[4:]==(0,0,0) for m in ms.values())
assert (ms['B'][3],ms['A'][3],ms['C'][3])==(F(25,128),F(7,32),F(31,128))
for src in (P,Q):
    a,b,c=[law(sets[k],src) for k in ('A','B','C')]
    assert (tv(a,b),tv(a,c),tv(b,c))==(F(3,128),F(3,128),F(3,64))
    for name,l in zip(('A','B','C'),(a,b,c)):
        assert sum(w for k,w in l.items() if k[-1]=='D')==ms[name][3]
assert F(5,16)**2/F(1,2)==F(25,128)
assert F(5,16)-(F(1,2)-F(5,16))**2/F(1,2)==F(31,128)
print('STAGE286B_COMPACT_INDEPENDENT_ORDERED_REPLAY_PASS')
print('source_models=2; fully_labeled_leaves_per_source=32; tv_diameter=3/64; minimax_radius=3/128')
