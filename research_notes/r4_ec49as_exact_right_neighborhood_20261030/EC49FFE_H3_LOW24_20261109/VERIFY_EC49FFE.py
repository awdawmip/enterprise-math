"""EC49FFE exact interval-cover census and native-X6 witness (standard Python)."""
import json
from itertools import combinations, product
from math import prod

SCIENCE_PIN = 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
OPERATIONS = {'a': (-1,-1), 'c': (1,2,-1,-2), 'd': (2,1,-2,-1),
              'e': (3,1,1,-3), 'f': (1,-1), 'g': (2,-2)}
ALPHABET = 'acdefg'
DFA = ((1,2,3,1,4,5), (1,6,7,1,1,1), (2,2,8,2,2,2),
       (3,8,3,3,3,3), (4,2,7,4,4,4), (5,6,3,5,5,5),
       (6,6,8,6,6,6), (7,8,7,7,7,7), (8,8,8,8,8,8))
LABELS = (0,0,4,1,16,32,8,2,0)


def high_keys(h):
    out = []
    for z in range(1, (h+1)//2 + 1):
        for f in range(1, h+1-2*z):
            g = h+1-2*z-f
            out.append((2*z+f, g, z))
    assert len(out) == (h-1)**2//4
    return out


def low_at(k,h):
    x,y,z = k
    H=x+y-1
    return H-min(x-2*z,y) <= h < H


def census():
    rows=[]
    for triple in combinations(range(4,9),3):
        high=triple+(9,)
        low=tuple(h for h in range(3,10) if h not in high)
        choices=[high_keys(h) for h in high]
        total=prod(map(len,choices))
        feasible=sum(all(any(low_at(k,h) for k in keys) for h in low)
                     for keys in product(*choices))
        rows.append(dict(high=list(high),low=[2,3,*low],
                         inventories=total,feasible=feasible))
    assert len(rows)==10
    assert sum(r['inventories'] for r in rows)==36288
    assert sum(r['feasible'] for r in rows)==12276
    assert sum(r['feasible']>0 for r in rows)==9
    assert rows[-1]['high']==[6,7,8,9] and rows[-1]['feasible']==0
    return rows


def observer(word):
    q=0
    for c in word:q=DFA[q][ALPHABET.index(c)]
    return LABELS[q]


def complete_key(word,h):
    n={c:word.count(c) for c in ALPHABET}
    assert len(word)==h and n['e']==n['a']+1 and n['e']>=1
    z=n['e']
    y=h+1-2*z-n['f']
    x=h+1-n['g']
    assert n['c']+n['d']==x+y-h-1 and min(x,y,z)>0
    return (x,y,z)


def native_prefixes(word):
    steps=tuple(s for op in word for s in OPERATIONS[op])
    end=[0]*6
    for s in steps:end[abs(s)-1]+=1 if s>0 else -1
    assert tuple(end)==(2,0,0,0,0,0)
    return {steps[:i] for i in range(1,len(steps)+1)}


def witness():
    keys={(3,1,1),(3,2,1),(3,4,1),(3,6,1),(3,7,1)}
    words={2:['de','ed','ce','ec'],3:['deg','edg','ceg','ecg'],
           4:['fegg','gefg'],5:['deggg','edggg','ceggg','ecggg'],
           6:['fegggg','gefggg'],7:['deggggg','edggggg','ceggggg','ecggggg'],
           8:['fegggggg','gefggggg'],9:['feggggggg','gefgggggg']}
    high={4,6,8,9}
    prefix=set();used=set()
    for h,ws in words.items():
        expected={16,32} if h in high else {1,2,4,8}
        assert len(ws)==len(expected) and {observer(w) for w in ws}==expected
        for w in ws:
            k=complete_key(w,h)
            assert k in keys
            used.add(k)
            prefix|=native_prefixes(w)
    assert len(used)==5 and len(prefix)==106
    assert observer('ecg') == observer('gec') == 8
    assert complete_key('ecg',3) == complete_key('gec',3) == (3,2,1)
    modified={h:list(ws) for h,ws in words.items()}
    modified[3][3]='gec'
    altered_prefix=set()
    for h,ws in modified.items():
        for word in ws: altered_prefix |= native_prefixes(word)
    assert len(altered_prefix)==109
    return {'order_residual_variant_cost':len(altered_prefix), 'keys':[list(k) for k in sorted(used)], 'high':[4,6,8,9],
            'words':{str(h):ws for h,ws in words.items()},
            'path_count':sum(map(len,words.values())), 'native_prefix_cost':len(prefix)}


if __name__=='__main__':
    rows=census();w=witness()
    print(json.dumps({'status':'EXACT_PASS', 'scientific_pin':SCIENCE_PIN,
                      'family_count':len(rows), 'inventories':sum(r['inventories'] for r in rows),
                      'feasible':sum(r['feasible'] for r in rows),
                      'infeasible':sum(r['inventories']-r['feasible'] for r in rows),
                      'rows':rows,'witness':w},indent=2,ensure_ascii=False))
