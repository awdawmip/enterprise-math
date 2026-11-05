"""Independent Python standard-library witness verifier for EC49FBI."""
import json, collections
OP={'a':[-1,-1],'c':[1,2,-1,-2],'d':[2,1,-2,-1],'e':[3,1,1,-3],'f':[1,-1],'g':[2,-2]}
ALPHABET='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
clauses=(18,20,33,40)
BASE={2:['fe','ge'],3:['feg','gef']}
for fn in ('/mnt/data/EC49FBI_MILP_REPORT.json','/mnt/data/EC49FBI_FORCE_H5M_REPORT.json'):
    r=json.load(open(fn))
    allwords={h:list(ws) for h,ws in BASE.items()}
    for h,w,s,k in r['selected_words']:allwords.setdefault(h,[]).append(w)
    prefs=set(); keys=set(); h5M=[]
    for h in range(2,10):
        masks=0
        for w in allwords.get(h,[]):
            steps=tuple(s for c in w for s in OP[c])
            pos=collections.Counter(s for s in steps if s>0)
            key=tuple(pos.get(i,0) for i in range(1,7)); keys.add(key)
            delta=tuple(steps.count(i)-steps.count(-i) for i in range(1,7))
            assert delta==(2,0,0,0,0,0), (h,w,delta)
            assert len(w)==h and len(steps)==2*sum(key)-2
            state=0
            for c in w:state=TRANS[state][ALPHABET.index(c)]
            sig=SIG[state];masks |= sig
            assert sig in (1,2,4,8,16,32)
            if h==5 and key==(6,4,1,0,0,0):h5M.append(w)
            for j in range(len(steps)):prefs.add(steps[:j+1])
        assert all(masks&cl for cl in clauses), (h,masks)
    assert len(keys)==5,keys
    assert len(prefs)==r['incumbent_cost'],(fn,len(prefs),r['incumbent_cost'])
    assert (len(h5M)>0)==r.get('forced_H5M_at_least_one',False)
    print(fn.split('/')[-1], 'exact-prefix-count',len(prefs),'key-count',len(keys),'H5-M',h5M, 'verified')
