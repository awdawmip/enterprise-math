"""Standard-library verifier of the short modulus-3 branch exclusions.

The complete four-type bank is inherited from the earlier native exhaustive
enumeration (24,000+12,000+4,500+12,000 classes). This checker validates every
class with the original finite-menu program, all coordinate occupancy shapes,
all Farkas columns, and each negative constant using only integer arithmetic.
The bank can be reproduced by the predecessor prepare_discovery_bank.py.
"""
from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
import argparse,importlib.util,json,struct,hashlib
from parallel_family import TYPES,COUNTS,POINTS,FORMS,FIBERS

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
EXPECTED_COUNTS={(9,557):24000,(10,744):12000,(11,936):4500,(11,944):12000}
EXPECTED_SHAPES={
    (9,557):{(1,2,2,2,2)},
    (10,744):{(2,2,2,2,2)},
    (11,936):{(1,2,2,2,4),(2,2,2,2,3),(1,1,2,2,5)},
    (11,944):{(1,2,2,2,4),(1,1,2,2,5)},
}

def load_bank(path):
    raw=path.read_bytes();assert len(raw)%24==0
    rows=[]
    for lo,hi,cost,tag in struct.iter_unpack('<QQII',raw):
        t=(tag%256,cost)
        if t not in EXPECTED_COUNTS:continue
        m=lo+(hi<<64);assert m.bit_count()==t[0] and 0<m<(1<<125)
        rows.append((m,TYPES.index(t)))
    assert Counter(TYPES[t] for m,t in rows)==EXPECTED_COUNTS
    assert len({m for m,t in rows})==len(rows)
    return rows,hashlib.sha256(raw).hexdigest()

def run(bank_path,delivery_root,certificate_dir,output):
    bank,bankhash=load_bank(bank_path)
    spec=importlib.util.spec_from_file_location('native_menu_for_modular_verification',delivery_root/'fractional/proof/verify.py')
    native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
    bad,pair=native.observation_tables()
    shapes={(a,t):Counter() for a in range(3) for t in range(4)}
    global_occupancy_checks=0
    for m,t in bank:
        assert native.native_class(m,bad,pair)==TYPES[t]
        for axis,form_index in enumerate((6,1,0)):
            occ=[(m&h).bit_count() for h in FIBERS[form_index]]
            shapes[axis,t][tuple(sorted(occ))]+=1
            assert tuple(sorted(occ)) in EXPECTED_SHAPES[TYPES[t]]
            # Universal class inequality underlying 8 <= 5.
            for v in range(5):
                lhs=sum((2*(occ[a]+1))%3 for a in range(5) if a!=v)
                rhs=occ[v]-(1 if t==0 else 2 if t==1 else 0)
                assert lhs<=rhs
                global_occupancy_checks+=1
    expected_frames={d['frame']:int(d['free']) for d in json.loads((delivery_root/'lower/fractional_covers.json').read_text())['frames']}
    results=[]
    for path in sorted(certificate_dir.glob('certificate_*.json')):
        data=path.read_bytes();cert=json.loads(data);f=cert['frame'];free=int(cert['free_mask'])
        assert free==expected_frames[f] and free.bit_count()==101
        y=cert['point_and_type_multipliers'];assert len(y)==129 and all(type(v) is int for v in y)
        target=[int(free>>p&1) for p in range(125)]+list(COUNTS)
        total=sum(a*b for a,b in zip(y,target));expanded=[]
        for cut in cert['cuts']:
            q=cut['q'];a=cut['a'];lam=cut['lambda'];r=cut['rhs'];z=cut['multiplier']
            assert type(z) is int and z>=0 and q>=2 and len(a)==4
            if cut['form_index']==-1:
                weights=lam;assert len(weights)==125
            else:
                form=FORMS[cut['form_index']];assert len(lam)==5
                weights=[lam[sum(a*b for a,b in zip(form,p))%5] for p in POINTS]
            assert (sum(weights[p] for p in range(125) if free>>p&1)+sum(a[t]*COUNTS[t] for t in range(4)))%q==r
            assert 0<r<q
            total-=z*r;expanded.append((q,weights,a,z))
        minimum=None;checked=0;in_frame=0
        for m,t in bank:
            ps=list(native.points(m));slack=sum(y[p] for p in ps)+y[125+t]
            for q,weights,a,z in expanded:slack-=z*((sum(weights[p] for p in ps)+a[t])%q)
            # Simple certificates are stronger: they hold on all 52,500 rows.
            if 'global_columns_valid' in cert or not m&~free:
                assert slack>=0,(f,m,slack)
                minimum=slack if minimum is None else min(minimum,slack);checked+=1
            if not m&~free:in_frame+=1
        assert in_frame==cert['complete_candidates']
        assert total==cert['negative_constant']<0
        assert minimum==cert['minimum_column_slack']
        row={'frame':f,'free_mask':str(free),'complete_frame_candidates':in_frame,
             'integer_columns_checked':checked,'cuts':len(expanded),'minimum_column_slack':minimum,
             'negative_constant':total,'certificate_sha256':hashlib.sha256(data).hexdigest(),
             'contradiction':'8 <= 5' if total==-3 and len(expanded)==4 else None}
        results.append(row);print(json.dumps(row),flush=True)
    out={'schema':'EXACT_MODULUS3_BRANCH_EXCLUSIONS_V1','bank_sha256':bankhash,
         'native_classes_verified':len(bank),'global_occupancy_inequality_checks':global_occupancy_checks,
         'coordinate_shapes':[{'axis':a,'type':TYPES[t],'histograms':[{'shape':list(s),'count':n} for s,n in sorted(counter.items())]}
                              for (a,t),counter in sorted(shapes.items())],
         'frames':results,'scope':'Short exact explanations of three previously excluded cost-9858 core frames; no new global lower bound is asserted.'}
    output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_verified':True,'native_classes':len(bank),'occupancy_checks':global_occupancy_checks,'excluded_frames':[r['frame'] for r in results]}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--bank',type=Path,default=ROOT/'lower/work9860/bank')
    p.add_argument('--delivery-root',type=Path,default=ROOT/'delivery');p.add_argument('--certificate-dir',type=Path,default=HERE/'simple_mod3')
    p.add_argument('--output',type=Path,default=HERE/'modular_verification.json');a=p.parse_args();run(a.bank,a.delivery_root,a.certificate_dir,a.output)
