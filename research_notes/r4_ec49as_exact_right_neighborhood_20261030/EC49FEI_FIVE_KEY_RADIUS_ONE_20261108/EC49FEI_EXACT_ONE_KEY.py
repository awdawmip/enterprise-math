"""EC49FEI. Exhaustive one-BRC-key replacement census, exact integer set-cover DP.
Dependency: EC49FEH_EXACT_CERT.py, original signed X6 grammar, science pin
fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json
from itertools import product
import EC49FEH_EXACT_CERT as E
BASE=((3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1))
SIGNATURES={4:(16,32),5:(1,2,4,8),6:(16,32),
            7:(16,32),8:(1,2,4,8),9:(16,32)}

def high_keys(h):
    """Enumerate exact nonnegative primitive-operator counts, not nearby triples."""
    out=[]
    for z in range(1,(h+1)//2+1):
        for r in range(h-2*z+2):
            for f in range(h-2*z+2-r):
                g=h-2*z+1-r-f
                k=(r+2*z+f,r+g,z)
                signatures={s for _,s in E.pool(h,k)}
                if {16,32}<=signatures:out.append(k)
    return sorted(set(out))

def solve_inventory(keys, early):
    assert len(keys)==len(set(keys))==5
    groups=[]
    for h,signatures in SIGNATURES.items():
        available={(w,s) for k in keys for w,s in E.pool(h,k)}
        if set(s for _,s in available)!={1,2,4,8} and h in (5,8):
            # A quota-four horizon might use alternate hitting choices
            # outside the certified family. No such case occurs here.
            raise AssertionError(('unexpected high signature at quota-four',h,keys))
        for s in signatures:
            paths={E.native(w) for w,t in available if t==s}
            assert paths,(keys,h,s)
            groups.append(paths)
    return E.depth_cover(early,groups)

def main():
    possibilities={h:high_keys(h) for h in (4,6,7,9)}
    assert list(map(len,possibilities.values()))==[2,6,9,16]
    h2=tuple(next(w for w,s in E.pool(2,BASE[0]) if s==t) for t in (1,2,4,8))
    early_variants=[h2+(a,b) for a,b in product(
        [w for w,s in E.pool(3,BASE[0]) if s==16],
        [w for w,s in E.pool(3,BASE[0]) if s==32])]
    assert len(early_variants)==4
    records=[]
    for i,h in enumerate((4,6,7,9),1):
        for k in possibilities[h]:
            if k==BASE[i]:continue
            keys=list(BASE);keys[i]=k
            values=[];depths=[]
            for early in early_variants:
                val,per_depth=solve_inventory(keys,early)
                values.append(val);depths.append(per_depth)
            records.append({'h':h,'old':BASE[i],'new':k,'all_four_bounds':values,
                            'depth_covers':depths,'min_lower_bound':min(values)})
    assert len(records)==29
    assert all(min(item['all_four_bounds'])>=98 for item in records)
    assert len({tuple(item['all_four_bounds']) for item in records})==len(set(item['min_lower_bound'] for item in records))
    return {'scope':'original 22-path signature quotas, global 5-full-positive-BRC-key budget, all path and within-horizon key mixing',
            'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'base_keys':BASE,'high_keys_by_horizon':possibilities,
            'theoretical_inventory_envelope':2*6*9*16,
            'early_four':early_variants,'neighbor_count':len(records),
            'minimum_one_key_change_lower_bound':min(x['min_lower_bound'] for x in records),
            'records':records}

if __name__=='__main__':print(json.dumps(main(),indent=2))
