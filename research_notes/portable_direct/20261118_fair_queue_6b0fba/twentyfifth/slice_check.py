"""Static X6/FCC observations; run with --repo /path/to/enterprise-math."""
import argparse
import ast
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys

V5 = 'experiments/x6_nonfcc_carrier_v5_20260906/check_fcc_basis_decoder.py'
CORE = 'src/enterprise_math/brc_weighted.py'
V5_HASH = '7eb40eb44983dc2f684adf982e2eaa77602137576551d3323198b820862976ad'
CORE_HASH = '4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f'


def run(repo):
    hashes = {k: sha256((repo/k).read_bytes()).hexdigest() for k in (V5,CORE)}
    assert hashes == {V5:V5_HASH, CORE:CORE_HASH}
    raw = {s.targets[0].id:ast.literal_eval(s.value) for s in ast.parse((repo/V5).read_text()).body
           if isinstance(s,ast.Assign) and isinstance(s.targets[0],ast.Name) and s.targets[0].id in ('NAMES','V')}
    names, cols = raw['NAMES'], raw['V']
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    assert Path(brc.__file__).resolve() == (repo/CORE).resolve()
    audit = sha256()

    @lru_cache(None)
    def branch(a,b):
        return brc.cwm_propagate(brc.cwm_edge(a),brc.cwm_edge(b))

    @lru_cache(None)
    def dot(a,b):
        """Individual summands keep slot and sign. Difference is taken at the two typed ports."""
        pos,neg = brc.CWM_ZERO, brc.CWM_ZERO
        for x,y in zip(a,b,strict=True):
            if x and y:
                v = branch(abs(x),abs(y))
                if (x>0)==(y>0):
                    pos = brc.cwm_recoalesce(pos,v)
                else:
                    neg = brc.cwm_recoalesce(neg,v)
        audit.update(repr((a,b,pos.count,int(pos.total),neg.count,int(neg.total))).encode()+b'\n')
        return int(pos.total-neg.total)

    def cross(a,b):
        return tuple(dot((a[(j+1)%3],-a[(j+2)%3]),(b[(j+2)%3],b[(j+1)%3])) for j in range(3))

    def det(a):
        return dot(a[0],cross(a[1],a[2]))

    def dual(v):
        d=det(v)
        return tuple((cross(v[(i+1)%3],v[(i+2)%3]),d) for i in range(3))

    def decode(v,y):
        out=[]
        for a,d in v:
            q,r=divmod(dot(a,y),d)
            assert r==0
            out.append(q)
        return tuple(out)

    def gram(v):
        return tuple(tuple(dot(x,y) for y in v) for x in v)

    charts=list(combinations(range(6),3))
    bases={s:dual(tuple(cols[i] for i in s)) for s in charts if det(tuple(cols[i] for i in s))}
    stars=[s for s in charts if s not in bases]
    normals=[cross(cols[s[0]],cols[s[1]]) for s in stars]
    assert len(bases)==16 and len(stars)==4
    rotations=[]
    incidences=Counter()
    for s in bases:
        face=len(set(''.join(names[i] for i in s)))==3
        kind='FACE' if face else 'PATH'
        v=[cols[i] for i in s]
        for h,normal in zip(stars,normals):
            d=len(set(s)&set(h))
            row=[dot(normal,col) for col in v]
            assert all(k in (0,2,-2) for k in row) and sum(x==0 for x in row)==d
            incidences[kind,d]+=1
        iso, optimal, named_iso=0,0,False
        for signs in product((1,-1),repeat=3):
            vs=tuple(tuple(t*c for c in col) for col,t in zip(v,signs))
            g=gram(vs)
            gp=tuple(tuple(g[(i+1)%3][(j+1)%3] for j in range(3)) for i in range(3))
            iso+=g==gp
            if signs==(1,1,1):
                named_iso=g==gp
            if not face and all(g[i][j]<=0 for i,j in combinations(range(3),2)):
                # det(gp - lambda*g) at lambda=1/2,1,2. Work with integer numerator.
                assert all(det(tuple(tuple(b*gp[i][j]-a*g[i][j] for j in range(3))
                                     for i in range(3)))==0 for a,b in ((1,2),(1,1),(2,1)))
                optimal+=1
        assert iso==(2 if face else 0) and optimal==(0 if face else 2)
        rotations.append([','.join(names[i] for i in s),kind,iso,named_iso,optimal])

    global_gauges=Counter()
    for signs in product((1,-1),repeat=6):
        faces=0
        for s in bases:
            if len(set(''.join(names[i] for i in s)))==3:
                faces+=all(signs[i]*signs[j]*dot(cols[i],cols[j])==1 for i,j in combinations(s,2))
        global_gauges[faces]+=1
    assert global_gauges=={0:24,1:16,2:24}

    def embedded(s,coordinates):
        return tuple(coordinates[s.index(i)] if i in s else 0 for i in range(6))

    def lifts(y,q=None):
        outputs=set()
        for s,rows in bases.items():
            digits=decode(rows,y)
            if q is not None:
                digits=tuple(v%q for v in digits)
            outputs.add(embedded(s,digits))
        return outputs

    def encode(x):
        return tuple(dot(tuple(col[j] for col in cols),x) for j in range(3))

    cube=Counter()
    for y in product(range(-4,5),repeat=3):
        if sum(y)%2:
            continue
        out=lifts(y)
        assert all(encode(x)==y for x in out)
        on=sum(dot(v,y)==0 for v in normals)
        c=sum(i==0 for i in y)
        expected=1 if c==3 else 5 if on==2 else 10 if (on==1 or c==2) else 13 if c else 16
        assert len(out)==expected
        cube[len(out)]+=1

    # The reference FACE is an integral basis of L, including for even q.
    v0=tuple(cols[i] for i in (0,1,3))
    r0=tuple(zip(*v0))
    residues={}
    for q in (2,3,4,5,6,7,8,9,10,12):
        counts=Counter()
        for a in product(range(q),repeat=3):
            y=tuple(dot(row,a) for row in r0)
            counts[len(lifts(y,q))]+=1
        odd=q%2
        expected={1:1,5:6*(q-1),7:1-odd,
                  10:4*(q-1)*(q-2)+3*(q-2+odd),
                  13:3*((q-1)*(q-3) if odd else (q-2)**2),
                  16:(q-1)*(q-3)**2-(1-odd)}
        assert counts==Counter({k:v for k,v in expected.items() if v})
        residues[q]=dict(sorted(counts.items()))

    y=(2,4,8)
    face=(-1,3,0,5,0,0)
    path=(-1,0,0,8,0,3)
    assert encode(face)==encode(path)==y and len(lifts(y))==16
    def valid(x):
        support={i for i,w in enumerate(x) if w}
        return any(support<=set(s) for s in bases)
    def step(x,i):
        return tuple(dot((1,1),(v,int(j==i))) for j,v in enumerate(x))
    assert valid(step(face,1)) and not valid(step(path,1))
    return {'source_hashes':hashes, 'global_gauges_by_isometric_faces':dict(sorted(global_gauges.items())),'rotations_chart_kind_isometry_gauges_named_and_chain_gauges':rotations,
            'incidences_kind_shared_axes':{str(k):v for k,v in sorted(incidences.items())},
            'full_integer_fibres_in_coordinate_box_minus4_to4':dict(sorted(cube.items())),
            'modular_fibre_cardinality_counts':residues,'collision':{'y':y,'face':face,'path':path,'plus_axis':names[1]},
            'brc':{'unique_ordered_dot_inputs':dot.cache_info().misses,'cached_dot_calls':dot.cache_info().hits,
                   'distinct_propagated_weight_pairs':branch.cache_info().misses,'signed_port_audit_sha256':audit.hexdigest()}}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,required=True)
    print(json.dumps(run(parser.parse_args().repo),indent=2))
