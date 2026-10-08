"""Operational tomography and interventions in the inherited BRC reservation model.

No new native force, release, or physical-time law is supplied. Existing reserve/
release functions are imported unchanged; old main suites are never executed.
All branch creation/composition/aggregation calls the pinned positive CWM BRC.
Signed differences are comparison readouts, never negative branch mass.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, product, permutations

ROOT=Path(__file__).resolve().parent
P=ROOT/'prior/check_membership.py'
if not P.exists():
    P=ROOT.parent/'20261008_residual_membership_7c2e8a/check_membership.py'
raw=P.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='be1b60446e31c2c8489d1ce0db16cc1e952d11c8':
    raise RuntimeError('inherited membership source mismatch')
spec=importlib.util.spec_from_file_location('observability_pinned_membership',P)
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
r=m.r
CHECKS=0

def ck(ok,msg):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError(msg)

def cw(v):return dict(C=v.count,W=str(v.total),M=str(v.dominant))
def put(out,key,v):out[key]=r.merge(out.get(key,r.brc.CWM_ZERO),v)
def readout(J,B):return (tuple(sorted(m.used(J)&B)),len(J))

def tomography(q,B,hidden_start=100):
    """Only the initial/following occupancy+count observations enter decoding."""
    J=m.realize(q,hidden_start);observations=[readout(J,B)]
    w=r.brc.CWM_ONE
    for b in sorted(B):
        J,delta,success=m.full_step(J,('release',b))
        w=r.serial(w,r.brc.CWM_ONE)
        observations.append(readout(J,B))
    tr=tuple(observations)
    return tr,w

def decode(tr):
    recovered=[]
    for before,after in zip(tr,tr[1:]):
        old,n=before;new,k=after;removed=frozenset(old)-frozenset(new)
        ck(frozenset(new)<=frozenset(old),'release-only transcript is monotone')
        ck(n-k==int(bool(removed)),'event-count decrement matches visible release')
        if removed:recovered.append(tuple(sorted(removed)))
    ck(not tr[-1][0],'fixed full release script clears visible interface')
    return (m.canon(recovered),tr[-1][1])

def tv(a,b):
    """Total-variation comparison of normalized W readouts, not a BRC state."""
    keys=set(a)|set(b)
    return sum((abs(a.get(k,r.brc.CWM_ZERO).total-b.get(k,r.brc.CWM_ZERO).total) for k in keys),Q())/2

def test_tomography():
    B=frozenset(range(6));cat=m.partial_catalog(B);rows=[];decode_map={}
    for part in sorted(cat):
        for kappa in (0,1):
            q=(part,kappa);tr,w=tomography(q,B)
            tr2,w2=tomography(q,B,1000)
            ck(tr==tr2 and w==w2==r.brc.CWM_ONE,'hidden partners do not alter transcripts')
            ck(decode(tr)==q,'observed transcript reconstructs initial quotient')
            ck(tr not in decode_map,'fixed-script response map is injective')
            decode_map[tr]=q
            rows.append(dict(partition=part,kappa=kappa,transcript=tr,weight=cw(w)))
    # Two nontrivial normalized CWM input families on the same quotient states.
    qs=tuple(decode_map.values());families=[]
    for kind in (0,1):
        f={q:r.merge(r.edge(Q(1)),r.edge(Q(1+(i%5 if kind else (i*3)%7),3))) for i,q in enumerate(qs)}
        norm=r.edge(Q(1)/r.total(f.values()).total)
        f={q:r.serial(v,norm) for q,v in f.items()};families.append(f)
    pushed=[];finals=[]
    for f in families:
        t={};end={}
        for q,v in f.items():
            tr,w=tomography(q,B)
            put(t,tr,r.serial(v,w));put(end,tr[-1],r.serial(v,w))
        ck(r.total(t.values())==r.total(f.values()),'injective deterministic script preserves full CWM')
        ck(all(t[tr]==f[q] for tr,q in decode_map.items()),'each quotient coefficient recovered exactly')
        pushed.append(t);finals.append(end)
    dist=tv(*families)
    ck(dist==tv(*pushed),'total variation preserved by full response transcript')
    ck(tv(*finals)<=dist,'terminal snapshot can lose information')
    return dict(patterns=len(cat),quotient_states=len(qs),releases_per_state=6,
                all_state_transcripts=rows,mixture_TV=str(dist),transcript_TV=str(tv(*pushed)),
                terminal_TV=str(tv(*finals)),original_suites_executed=False)

def prepare(n):
    fams=[{},{}];labels={}
    weight=Q(1,2**(n-1))
    for bits in product((0,1),repeat=n):
        J=m.canon(h for g,bit in enumerate(bits) for h in m.gadget(g,bit))
        # Real multiplication of the inherited compatible-event basis.
        v=m.active_monomial(J,weight)
        fams[sum(bits)%2][J]=v;labels[J]=bits
    for f in fams:ck(r.total(f.values()).total==1,'explicit parity preparation normalized')
    return fams,labels

def marginal(f,inds):
    out={}
    for J,v in f.items():
        key=tuple(m.canon(h for h in J if min(h)>6*g and max(h)<=6*g+6) for g in inds)
        put(out,key,v)
    return out

def probe_bits(J,order):
    """Only records whether the released module's third member is still occupied."""
    bits=[];w=r.brc.CWM_ONE
    for g in order:
        J,delta,success=m.full_step(J,('release',6*g+1));w=r.serial(w,r.brc.CWM_ONE)
        ck(delta==1 and success,'local probe releases its actual owner')
        bits.append(int(6*g+3 in m.used(J)))
    return tuple(bits),J,w

def test_all_order_correlations():
    outputs=[]
    for n in range(3,7):
        fams,labels=prepare(n);subs=0
        for k in range(n):
            for inds in combinations(range(n),k):
                ck(marginal(fams[0],inds)==marginal(fams[1],inds),'every proper module marginal agrees in CWM')
                subs+=1
        hist=[];trace_laws=[];prefix_laws=[]
        for f in fams:
            laws=[{} for _ in range(n+1)];parity={};details=[]
            for J,v in f.items():
                observed,end,w=probe_bits(J,range(n))
                ck(observed==labels[J],'each probe recovers one membership bit from occupancy')
                val=r.serial(v,w)
                for k in range(n+1):put(laws[k],observed[:k],val)
                put(parity,sum(observed)%2,val)
                details.append(dict(initial_bits=labels[J],observed_bits=observed,weight=cw(val)))
            hist.append(parity);trace_laws.append(laws[-1]);prefix_laws.append(laws)
        for k in range(n):ck(prefix_laws[0][k]==prefix_laws[1][k],'all proper probe prefixes indistinguishable')
        ck(tv(*trace_laws)==1,'full probe transcript separates parity input supports')
        ck(hist[0].get(0,r.brc.CWM_ZERO).total==1 and hist[1].get(0,r.brc.CWM_ZERO).total==0,'parity event has probabilities one and zero')
        # Every query subset/pattern, not just one ordering, has the same mass.
        adaptive_checks=0
        for k in range(n):
            for inds in combinations(range(n),k):
                a,b=marginal(fams[0],inds),marginal(fams[1],inds)
                ck(a==b,'adaptive leaf depending on fewer than n distinct modules is balanced')
                adaptive_checks+=1
        outputs.append(dict(n=n,occurrences=6*n,branches_each=2**(n-1),
            equal_proper_marginals=subs,adaptive_leaf_scope_checks=adaptive_checks,
            proper_prefix_TV=['0']*n,full_transcript_TV='1',parity_zero_probabilities=['1','0'],
            common_prediction_worst_error_lower_bound='1/2',
            decoder='release(6*g+1), read occupancy(6*g+3); parity of recorded bits',
            lower_bound_scope='local one-module probes and their recorded bits only; not arbitrary cross-module commands'))
    return outputs

def apply_all(f,ops,apply_weight=Q(1)):
    """All branches including skip/failure are kept. No postselection."""
    f=dict(f)
    for op in ops:
        out={}
        for J,v in f.items():
            if apply_weight<1:put(out,J,r.serial(v,r.edge(1-apply_weight)))
            end,delta,ok=m.full_step(J,op)
            put(out,end,r.serial(v,r.edge(apply_weight)))
        f=out
    return f

def occupied_mass(f,b):return r.total(v for J,v in f.items() if b in m.used(J)).total

def test_no_transmission_and_cross_gate():
    fams,labels=prepare(3);out=[];separate=[]
    for parity,f in enumerate(fams):
        outside=marginal(f,(1,2))
        for a in (Q(1),Q(2,3),Q(1,5)):
            local=apply_all(f,[('release',1)],a)
            after=marginal(local,(1,2))
            ck(set(outside)==set(after),'local commands leave each remote microstate untouched')
            ck(all(outside[x].total==after[x].total for x in outside),'unconditioned remote W law unchanged')
            separate.append(dict(parity=parity,apply_weight=str(a),remote_W_TV=str(tv(outside,after)),
                before_C=r.total(outside.values()).count,after_C=r.total(after.values()).count,
                note='W invariance only; stochastic refinement may alter C and M'))
        # Intervene on local releases, but no event crosses into third module.
        after=apply_all(f,[('release',1),('release',7)])
        selected={J:v for J,v in after.items() if 3 not in m.used(J) and 9 not in m.used(J)}
        rejected={J:v for J,v in after.items() if not (3 not in m.used(J) and 9 not in m.used(J))}
        mass=r.total(selected.values()).total
        ck(mass==Q(1,4) and r.total(rejected.values()).total==Q(3,4),'selection keeps accepted and rejected raw masses')
        norm=r.edge(1/mass);conditional={J:r.serial(v,norm) for J,v in selected.items()}
        # Classify type0 of third module by the actual retained membership, no intervention on it.
        def type0_mass(f):return r.total(v for J,v in f.items() if (13,14,15) in J).total
        ck(type0_mass(after)==Q(1,2),'third-module law not changed by two local interventions')
        ck(type0_mass(conditional)==(1 if parity==0 else 0),'conditioning changes inference, not remote branch state')
        treated=apply_all(f,[('release',1),('release',7),('release',13)])
        control=apply_all(f,[('release',7),('release',13)])
        before=[occupied_mass(control,15),occupied_mass(treated,15)]
        ck(before==[Q(1,2),Q(1,2)],'no third-module effect before cross-module gate')
        gate=('reserve',(3,9,15))
        ct=apply_all(control,[gate]);tt=apply_all(treated,[gate])
        after_values=[occupied_mass(ct,15),occupied_mass(tt,15)]
        expected=Q(3,4) if parity==0 else Q(1,2)
        ck(after_values==[Q(1,2),expected],'same inherited crossing command converts joint state into remote response')
        ck(r.total(ct.values()).total==r.total(tt.values()).total==1,'cross-gate trial has no discarded branch mass')
        out.append(dict(parity=parity,unconditional_third_type0=str(type0_mass(after)),
            selected_raw_W=str(mass),rejected_raw_W='3/4',conditional_third_type0=str(type0_mass(conditional)),
            target=15,control_release_members=[7,13],treated_release_members=[1,7,13],
            before_cross_gate=list(map(str,before)),after_cross_gate=list(map(str,after_values)),
            intervention_difference=str(after_values[1]-after_values[0]),
            cross_gate=gate,physical_force_or_coordinate_claim=False))
    # Symmetric input preparation gives every ordered distinct module pair the same test.
    permutation_tests=[]
    for source,target in permutations(range(3),2):
        for parity,f in enumerate(fams):
            ops=[('release',6*g+1) for g in range(3) if g!=source]
            ctl=apply_all(f,ops+[('reserve',(3,9,15))])
            trt=apply_all(f,[('release',6*source+1)]+ops+[('reserve',(3,9,15))])
            delta=occupied_mass(trt,6*target+3)-occupied_mass(ctl,6*target+3)
            ck(delta==(Q(1,4) if parity==0 else Q()),'ordered-pair intervention contrast')
            permutation_tests.append(dict(source=source,target=target,parity=parity,delta=str(delta)))
    return dict(local_trials=separate,conditioning_and_intervention=out,ordered_pair_trials=permutation_tests)

def main():
    a=test_tomography();b=test_all_order_correlations();c=test_no_transmission_and_cross_gate()
    result=dict(schema='EM_RESIDUAL_OPERATIONAL_OBSERVABILITY_V1',
        status='CONDITIONAL_EXECUTED_BRC_NOT_NATIVE_FORCE',
        event_id='EM-20261008-RESIDUAL-OBSERVABILITY-7C2E8A',
        global_read='552f8bb63a7205e55f6878f3a0573234c2641259',
        source_read='671bbbb2a46f08f62cad08060adb682d647533d5',
        tomography=a,finite_order_blindness=b,intervention=c,
        assertions=CHECKS,inherited_helper_checks=m.CHECKS,BRC_calls=dict(r.CALLS),
        old_main_suites_executed=False,new_native_transition_law=False,
        signed_numbers_are_comparison_readouts_only=True,independent_review=False)
    data=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(data)
    summary=dict(assertions=CHECKS,inherited_helper_checks=m.CHECKS,BRC_calls=dict(r.CALLS),
        tomography_states=a['quotient_states'],max_parity_modules=6,
        causal_contrasts=c['conditioning_and_intervention'],output_bytes=len(data),output_sha256=hashlib.sha256(data).hexdigest())
    (ROOT/'summary.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(summary,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
