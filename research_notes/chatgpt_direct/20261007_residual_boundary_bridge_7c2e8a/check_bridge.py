"""Source-pinned BRC boundary-memory audit; not native force dynamics.

Run: python check_bridge.py
The old signature checker is imported, not re-run. All response updates call
U2's unchanged transport_tables and positive CWM operations. Signed arithmetic
below is an explicitly declared readout of preserved positive outputs.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations, product

ROOT=Path(__file__).resolve().parent

def load(name, path, expected_blob):
    raw=path.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob != expected_blob: raise RuntimeError(f'source mismatch: {path}')
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);sys.modules[name]=obj
    spec.loader.exec_module(obj)
    return obj

router_path=ROOT/'packet_router.py'
if not router_path.exists():
    router_path=ROOT.parent/'20261007_cell_closure_u2_7f21d8'/'packet_router.py'
prior_path=ROOT/'prior/BRC_PATCH.py'
if not prior_path.exists():
    prior_path=ROOT.parent/'20261007_residual_algebra_patch_7c2e8a'/'BRC_PATCH.py'
r=load('bridge_pinned_u2',router_path,'7465f5aa16cbb8fba61ba4be80f8a6884b879c53')
o=load('bridge_prior_signature',prior_path,'e3397722b0ee88dc9810cb872a14e7889403eee5')
RHO=Q(1,4)
MAT,BULK=r.transport_tables(RHO)
BULK=dict(BULK)
CHECKS=0

def ck(value, message):
    global CHECKS
    CHECKS+=1
    if not value: raise AssertionError(message)

def signed(word):
    return tuple((p//2+1)*(1 if p%2==0 else -1) for p in word)

def sig(word,degree): return o.signature(signed(word),degree)

def endpoint(word):
    z=r.ZERO
    for p in word: z=r.advance(z,p)
    return z

def encode_cwm(x):
    return {'C':x.count,'W':str(x.total),'M':str(x.dominant)}

def scatter(incoming, weight):
    return {q:r.serial(weight,k) for q,k in MAT[incoming]}

def axes(out):
    return tuple(r.total(out.get(2*j+s,r.brc.CWM_ZERO) for s in (0,1)) for j in range(6))

def trace(word):
    """Select one word from a common seed's positive path tree, KEEP siblings.

    Single prescribed material cell at endpoint; earlier selected cells empty.
    A controlled circuit seed, not U2's isotropic material-source preparation.
    Sibling leaves and attenuated sectors remain unexpanded evidence, no
    conditional renormalization or physical selection is performed.
    """
    target=endpoint(word);z=r.ZERO;p=0;w=r.brc.CWM_ONE
    leaves=[];records=[]
    for index,q in enumerate(word):
        ck(z!=target,'chosen prefix must be bulk, not terminal material')
        options={qq:r.serial(w,k) for qq,k in BULK.items()}
        stored=r.serial(w,r.edge(1-RHO))
        ck(r.total([stored,*options.values()]).total==w.total,'prefix budget partition')
        leaves.append(stored)
        leaves.extend(v for qq,v in options.items() if qq!=q)
        records.append({'depth':index,'cell':z,'incoming':p,'selected':q,
                        'input':encode_cwm(w),'retained':encode_cwm(stored),
                        'sibling_outputs':{str(qq):encode_cwm(v) for qq,v in options.items() if qq!=q}})
        z=r.advance(z,q);p=q^1;w=options[q]
    out=scatter(p,w);stored=r.serial(w,r.edge(1-RHO))
    leaves.extend([stored,*out.values()])
    ck(r.total(leaves).total==1,'complete frontier retains unit seed budget')
    ck(r.total(out.values()).total==r.serial(w,r.edge(RHO)).total,'terminal active budget')
    return {'word':word,'z':z,'incoming':p,'arrival':w,'out':out,
            'axis':axes(out),'prefix':records,'terminal_retained':stored,
            'frontier_total':r.total(leaves)}

def compact(t, keep_prefix=False):
    result={'word':t['word'],'z':t['z'],'incoming':t['incoming'],
            'arrival':encode_cwm(t['arrival']),
            'ports':{str(q):encode_cwm(v) for q,v in t['out'].items()},
            'axes':[encode_cwm(v) for v in t['axis']],
            'terminal_retained':encode_cwm(t['terminal_retained']),
            'frontier_total':encode_cwm(t['frontier_total'])}
    if keep_prefix: result['prefix']=t['prefix']
    return result

def layer_step(layer, occupied):
    out={}
    for (source,z,p),value in layer.items():
        for q,k in MAT[p] if z in occupied else BULK.items():
            key=(source,r.advance(z,q),q^1)
            out[key]=r.merge(out.get(key,r.brc.CWM_ZERO),r.serial(value,k))
    return out


def main():
    pairs=[]
    for a,b in permutations(r.PORTS,2):
        if r.axis(a)==r.axis(b): continue
        P=(a,b,b,a);Qw=(b,a,a,b)
        ck(sig(P,2)==sig(Qw,2),'full degree-two equality')
        ck(o.readout(sig(P,2))==o.readout(sig(Qw,2)),'same z and Omega')
        left,right=trace(P),trace(Qw)
        j=r.axis(a)
        ck(left['arrival']==right['arrival'],'equal incident CWM')
        ck(left['incoming']!=right['incoming'],'different actual incoming')
        ck(left['axis'][j].total==r.serial(left['arrival'],r.edge(Q(1,12))).total,'same-axis budget')
        ck(right['axis'][j].total==r.serial(right['arrival'],r.edge(Q(1,30))).total,'cross-axis budget')
        ck(left['axis'][j]!=right['axis'][j],'declared axis response distinguishes')
        pairs.append({'a':a,'b':b,'left_incoming':left['incoming'],'right_incoming':right['incoming'],
                      'left_axis':encode_cwm(left['axis'][j]),'right_axis':encode_cwm(right['axis'][j])})
    degrees=[];P=(0,);Qw=(2,)
    for d in range(1,9):
        P,Qw=P+Qw,Qw+P
        sp,sq=sig(P,d),sig(Qw,d)
        ck(sp==sq,'all truncated CWM coefficients agree')
        ck(P[-1]!=Qw[-1],'different last letters for all tested degrees')
        left,right=trace(P),trace(Qw)
        ck(left['z']==right['z'] and left['arrival']==right['arrival'],'same endpoint and path CWM')
        j=r.axis(P[-1]);delta=left['axis'][j].total-right['axis'][j].total
        ck(delta==r.serial(left['arrival'],r.edge(RHO/5)).total,'exact response separation')
        ck(delta>0,'no exact zero at finite depth')
        degrees.append({'degree':d,'length':len(P),'coefficient_classes':len(sp),
                        'coefficient_digest':hashlib.sha256(json.dumps([
                          [list(k),encode_cwm(v)] for k,v in sorted(sp.items())],sort_keys=True).encode()).hexdigest(),
                        'left':compact(left),'right':compact(right),'response_difference':str(delta),
                        'any_common_prediction_worst_case_lower_bound':str(delta/2)})
    # Converse witness: different Omega but identical actual unary boundary.
    left,right=trace((0,2,4)),trace((2,0,4))
    ck(o.readout(sig((0,2,4),2))[1]!=o.readout(sig((2,0,4),2))[1],'distinct Omega')
    ck(left['incoming']==right['incoming'] and left['arrival']==right['arrival'],'equal unary boundary')
    ck(left['out']==right['out'],'equal next signed CWM response')
    l={(0,left['z'],left['incoming']):left['arrival']}
    rr={(0,right['z'],right['incoming']):right['arrival']}
    for d in range(3):
        l=layer_step(l,{left['z']});rr=layer_step(rr,{right['z']})
        ck(l==rr,'exact source-cell-port continuation equality')
    # One-step port observations recover every input TOTAL vector. No matrix
    # inverse/eigensolver is run; the derived signed readout formula is checked
    # against positive BRC outputs and keeps all positive input/output sectors.
    mixtures=[]
    tests=[tuple(int(j==p) for j in range(12)) for p in range(12)]
    tests += [tuple(Q(((k+1)*(j+3))%17,k+2) for j in range(12)) for k in range(24)]
    for weights in tests:
        positive={p:r.edge(w) for p,w in enumerate(weights) if w}
        out={q:r.brc.CWM_ZERO for q in r.PORTS}
        for p,w in positive.items():
            for q,v in scatter(p,w).items(): out[q]=r.merge(out[q],v)
        y=[out[q].total for q in r.PORTS];S=r.total(out.values()).total
        recovered=[]
        for j in range(6):
            b=y[2*j]+y[2*j+1];d=y[2*j]-y[2*j+1]
            h=(5*b-Q(2,3)*S)/RHO;imb=3*d/RHO
            recovered.extend(((h+imb)/2,(h-imb)/2))
        ck(tuple(recovered)==weights,'exact positive input recovered by derived observer')
        mixtures.append({'input':[str(w) for w in weights],'output':[str(w) for w in y]})
    base_left,base_right=trace((0,2,2,0)),trace((2,0,0,2))
    result={'schema':'EM_BRC_BOUNDARY_MEMORY_AUDIT_V1',
        'status':'CONDITIONAL_U2_CIRCUIT_NOT_NATIVE_FORCE_DYNAMICS',
        'source_ref':'564949b13c4e7c07c21c075a517e8f3b1bee98c3',
        'rho':str(RHO),'bulk_edge':str(BULK[0].total),
        'all_ordered_cross_axis_signed_pairs':len(pairs),'pairs':pairs,
        'degrees':degrees,'mixtures':mixtures,
        'same_degree_two_witness':[compact(base_left,True),compact(base_right,True)],
        'different_Omega_same_boundary':[compact(left),compact(right)],
        'assertions':CHECKS,'router_brc_calls':dict(r.CALLS),
        'prior_signature_brc_calls':dict(o.CALLS),'prior_internal_assertions':o.CHECKS,
        'prior_full_suite_reexecuted':False,'ordinary_classical_baseline_run':False,
        'native_five_coordinate_transmission_proved':False,'new_force_law_introduced':False}
    data=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    print(json.dumps({k:result[k] for k in ['status','all_ordered_cross_axis_signed_pairs','assertions','router_brc_calls','prior_signature_brc_calls','prior_internal_assertions']},indent=2))
    print('results_sha256',hashlib.sha256(data).hexdigest())
    print('base axis responses',base_left['axis'][0],base_right['axis'][0])

if __name__=='__main__': main()
