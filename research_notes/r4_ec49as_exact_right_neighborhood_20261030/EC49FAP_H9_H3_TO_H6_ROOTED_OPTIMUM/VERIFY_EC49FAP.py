#!/usr/bin/env python3
"""EC49FAP: complete H3-or-H4-or-H5-or-H6-rooted H8/H9 lower-bound certificate.
Usage: python VERIFY_EC49FAP.py > EXACT_REPORT_EC49FAP.generated.json
All arithmetic is exact integer modular, with a certified Q-rank transfer.
"""
import itertools, json
from collections import defaultdict

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
START=(('N',0),('N',1),('N',2),('A',0),('A',2),
       ('B',0),('B',1),('AB',0),('BA',0))
BUCKET=('N','A','B','AB','BA')
B2=['de','ed','ce','ec']; B3=['feg','gef']
CASES={
1512:{4:['defg','edfg','fegc','gefc'],5:['fegfg','geffg'],6:['fegfgg','geffgg'],7:['fegfggg','geffggg']},
1513:{4:['defg','edfg','fegc','gefc'],5:['fegfg','geffg'],6:['fegfgf','geffgf'],7:['fegfgff','geffgff']},
2200:{4:['fegg','gefg'],5:['feggd','gefgd','feggc','gefgc'],6:['fegggf','gefggf'],7:['fegggfg','gefggfg']},
2203:{4:['fegf','geff'],5:['fegfd','geffd','fegfc','geffc'],6:['fegfgf','geffgf'],7:['fegfgff','geffgff']}}
MOD=1000003

def steps(w):return tuple(x for a in w for x in OPS[a])
def key(st):return tuple(st.count(a) for a in range(1,7))
def net(st):return tuple(st.count(a)-st.count(-a) for a in range(1,7))
def obs(st):
    ans=[]
    for state,previous in START:
        for s in st:
            if previous==1 and s==2:
                if state=='N':state='A'
                elif state=='B':state='BA'
            elif previous==2 and s==1:
                if state=='N':state='B'
                elif state=='A':state='AB'
            previous=s
        ans.append(BUCKET.index(state))
    return tuple(ans)

def rank(sigs):
    """Rank of nine-history 0/1 bucket matrix, over F_1000003."""
    basis={}
    for sig in sigs:
        for bucket in range(5):
            v=[int(x==bucket) for x in sig]
            for pivot,b in sorted(basis.items()):
                if v[pivot]:
                    f=v[pivot];v=[(x-f*y)%MOD for x,y in zip(v,b)]
            p=next((j for j,vj in enumerate(v) if vj),None)
            if p is not None:
                inv=pow(v[p],-1,MOD);basis[p]=[(x*inv)%MOD for x in v]
            if len(basis)==9:return 9
    return len(basis)

def prefixes(words):
    s=set()
    for w in words:
        st=steps(w)
        s.update(st[:i] for i in range(1,len(st)+1))
    return s

def suffixes(n):
    return [''.join(w) for w in itertools.product(OPS,repeat=n)
            if net(steps(w))==(0,)*6]

def min_rank_cost(items, free, six):
    """Exact OR-mask tree-DP: minimum paid primitive edges to span rank nine."""
    six=sorted(six)
    valid={mask for mask in range(1,64) if rank(s for i,s in enumerate(six) if mask>>i&1)==9}
    if not valid:return None
    tree={'children':{},'end':0,'prefix':()}
    for word,sig in items:
        node=tree
        for s in steps(word):
            p=node['prefix']+(s,)
            node=node['children'].setdefault(s,{'children':{},'end':0,'prefix':p})
        node['end']|=1<<six.index(sig)
    def walk(node):
        d={0:0}
        if node['end']:d[node['end']]=0
        for child in node['children'].values():
            next_d={};child_d=walk(child)
            for x,cx in d.items():
                for y,cy in child_d.items():
                    m=x|y;cost=cx+cy
                    if cost<next_d.get(m,10**9):next_d[m]=cost
            d=next_d
        extra=int(bool(node['prefix']) and node['prefix'] not in free)
        if extra:
            for mask in d:
                if mask:d[mask]+=1
        return d
    d=walk(tree)
    return min((cost for mask,cost in d.items() if mask in valid),default=None)

def check():
    z={i:suffixes(i) for i in (2,3,4,5,6)}
    assert [len(z[i]) for i in (2,3,4,5,6)]==[18,88,454,2424,13236]
    records=[]
    for id,src in CASES.items():
        by_h={2:B2,3:B3,**src}
        base=[w for h in range(2,8) for w in by_h[h]]
        for h in range(2,8):
            words=by_h[h]
            assert all(len(w)==h and net(steps(w))==(2,0,0,0,0,0) for w in words)
            assert len({key(steps(w)) for w in words})==1 and rank({obs(steps(w)) for w in words})==9
        oldkeys={key(steps(w)) for w in base}
        six={obs(steps(w)) for w in base}
        bp=prefixes(base)
        assert len(oldkeys)==4 and len(six)==6 and len(bp)==72
        groups={8:defaultdict(dict),9:defaultdict(dict)}
        for h in (8,9):
            for h0 in (3,4,5,6):
                for root in by_h[h0]:
                    for suf in z[h-h0]:
                        w=root+suf;st=steps(w);o=obs(st)
                        assert net(st)==(2,0,0,0,0,0)
                        if o in six:groups[h][key(st)][w]=o
        allkeys=set(groups[8])|set(groups[9])
        admissible={h:{k for k in groups[h] if rank(groups[h][k].values())==9}
                    for h in (8,9)}
        assert not (admissible[8]&oldkeys) and not (admissible[9]&oldkeys)
        common=sorted(admissible[8]&admissible[9])
        table=[]
        for k in common:
            a=list(groups[8][k].items());b=list(groups[9][k].items())
            d8=min_rank_cost(a,bp,six)
            # Optimistic credit: every eligible H8 path is counted as prepaid for H9.
            d9=min_rank_cost(b,bp|prefixes(groups[8][k]),six)
            assert d8 is not None and d9 is not None
            table.append({'key':list(k)[:3], 'words_h8':len(a),'words_h9':len(b),
                          'exact_min_h8_extra':d8,'optimistic_h9_extra':d9,
                          'certified_lower_bound':len(bp)+d8+d9})
        assert all(t['certified_lower_bound']>=94 for t in table)
        assert len(common)==22
        assert len(admissible[8])==34 and len(admissible[9])==50
        # Verify explicit upper-bound witness from EC49FAJ is in H5-or-H6 family.
        w8=[w+last for w in by_h[7] for last in 'cd']
        w9=[w+'fg' for w in by_h[7]]
        assert all(any(w.startswith(r) for h in (3,4,5,6) for r in by_h[h]) for w in w8+w9)
        assert len({key(steps(w)) for w in w8+w9})==1
        assert rank(obs(steps(w)) for w in w8)==9 and rank(obs(steps(w)) for w in w9)==9
        assert len(prefixes(base+w8+w9))==94
        records.append({'fixed_source_rank':id,'fixed_H2_H7_cost':72,
                        'H8_rank9_keys':len(admissible[8]),'H9_rank9_keys':len(admissible[9]),
                        'old_key_rank9_H8':len(admissible[8]&oldkeys),
                        'old_key_rank9_H9':len(admissible[9]&oldkeys),
                        'common_new_keys':len(common),'key_bounds':table,
                        'minimum_certified_bound':min(t['certified_lower_bound'] for t in table),
                        'verified_witness_cost':94})
    return {'result':'PASS','theorem':'Four fixed H2..H7 families: exact H3-or-H4-or-H5-or-H6-rooted H8/H9 optimum 94',
            'parent':'EC49FAO@d032ffb7a4dfc88f5ef5746cb47e38449654d71a',
            'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'arithmetic':'native signed X6 steps; complete 7-letter zero-net suffixes; 0/1 nine-start matrix mod 1000003; exact OR-mask prefix DP; 3^9<1000003 certifies rank over Q',
            'zero_net_suffix_counts':{str(h):len(z[h]) for h in (2,3,4,5,6)},'cases':records}

if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
