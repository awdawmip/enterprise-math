"""Exact current-membership BRC quotient; TEST_ONLY, not native force dynamics.

Frozen interface B: reserve declared triples wholly in B; release the current
triple containing b in B; inspect occupancy in B and total active-event count.
No hidden-member/source/clock/cost oracle. Coefficients are the unchanged pinned
positive BRC CWM. Cost grades below count successful release commands, NOT energy.
Run: python check_membership.py
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PRIOR=ROOT/'prior/prior_triad.py'
if not PRIOR.exists():
    PRIOR=ROOT.parent/'20261007_residual_triad_interface_7c2e8a/check_triad.py'
raw=PRIOR.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='662755ef82c2f433ca57da76b4ce44d63a407612':
    raise RuntimeError('inherited assembly pin mismatch')
spec=importlib.util.spec_from_file_location('membership_old_triad',PRIOR)
s=importlib.util.module_from_spec(spec);sys.modules[spec.name]=s;spec.loader.exec_module(s)
r=s.r
CHECKS=0

def ck(ok,msg):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError(msg)

def canon(blocks):return tuple(sorted(tuple(sorted(x)) for x in blocks))
def blocks(state):return frozenset(frozenset(x) for x in state)
def used(state):return frozenset().union(*map(frozenset,state))
def cw(v):return {'C':v.count,'W':str(v.total),'M':str(v.dominant)}
def merge_at(out,key,v):out[key]=r.merge(out.get(key,r.brc.CWM_ZERO),v)

def sigma(J,B):
    traces=canon(frozenset(h)&B for h in J if frozenset(h)&B)
    return (traces,sum(not (frozenset(h)&B) for h in J))

def observed(q):return (tuple(sorted(used(q[0]))),q[1]+len(q[0]))

def full_step(J,op):
    name,arg=op; H=blocks(J)
    if name=='release':
        owner=[h for h in H if arg in h]
        if not owner:return J,0,False
        if len(owner)!=1:raise ValueError('not a disjoint event assembly')
        return canon(H-{owner[0]}),1,True
    D=frozenset(arg)
    if len(D)!=3:raise ValueError('reserve must have three distinct occurrences')
    if D&used(J):return J,0,False
    return canon(H|{D}),0,True

def abstract_step(q,op,B):
    name,arg=op;P,k0=q;H=blocks(P)
    if name=='release':
        if arg not in B:raise ValueError('release outside frozen interface')
        owner=[h for h in H if arg in h]
        if not owner:return q,0,False
        if len(owner)!=1:raise ValueError('invalid partial partition')
        return (canon(H-{owner[0]}),k0),1,True
    D=frozenset(arg)
    if len(D)!=3 or not D<=B:raise ValueError('reserve outside frozen interface')
    if D&used(P):return q,0,False
    return (canon(H|{D}),k0),0,True

def restrict(q,C):
    P,k0=q
    return (canon(frozenset(h)&C for h in P if frozenset(h)&C),
            k0+sum(not (frozenset(h)&C) for h in P))

def realize(q,start=100):
    P,k0=q;J=[];n=start
    for S in P:
        extra=tuple(range(n,n+3-len(S)));n+=len(extra);J.append(tuple(S)+extra)
    for _ in range(k0):J.append(tuple(range(n,n+3)));n+=3
    return canon(J)

def partial_catalog(B):
    """Positive BRC branching: smallest item is free or in a block of size 1..3."""
    B=tuple(sorted(B))
    if not B:return {():r.brc.CWM_ONE}
    b,rest=B[0],B[1:];out={}
    for P,w in partial_catalog(rest).items():merge_at(out,P,r.serial(w,r.brc.CWM_ONE))
    for n in range(3):
        for companions in combinations(rest,n):
            C=frozenset(companions)
            for P,w in partial_catalog(tuple(x for x in rest if x not in C)).items():
                merge_at(out,canon(P+((b,)+companions,)),r.serial(w,r.brc.CWM_ONE))
    return out

def check_quotient():
    B=frozenset(range(6));cat=partial_catalog(B)
    ck(len(cat)==789,'six-interface partial partitions')
    ck(all(v==r.brc.CWM_ONE for v in cat.values()),'unique constructor provenance')
    ops=[('release',b) for b in sorted(B)]+[('reserve',D) for D in combinations(sorted(B),3)]
    records=[];transition_digest=hashlib.sha256();tests=0;shrinks=0
    for P in sorted(cat):
        q=(P,0);finger=(observed(q),tuple(observed(abstract_step(q,('release',b),B)[0]) for b in sorted(B)))
        records.append({'partition':[list(x) for x in P],
                        'occupied':list(observed(q)[0]),
                        'release_occupancies':[list(x[0]) for x in finger[1]]})
        for k0 in (0,1):
            q=(P,k0);J=realize(q,100);J2=realize(q,1000)
            ck(sigma(J,B)==q==sigma(J2,B),'different hidden partners have same interface')
            for op in ops:
                aq,c,ok=abstract_step(q,op,B)
                for full in (J,J2):
                    f,fc,fok=full_step(full,op)
                    ck((sigma(f,B),fc,fok)==(aq,c,ok),'all primitive operations commute with projection')
                    tests+=1
                transition_digest.update(repr((q,op,aq,c,ok)).encode())
        for bits in product((0,1),repeat=6):
            C=frozenset(i for i,x in enumerate(bits) if x)
            ck(restrict(q,C)==sigma(J,C),'certified shrinking preserves invisible-event count')
            shrinks+=1
    fingerprints=[(tuple(x['occupied']),tuple(map(tuple,x['release_occupancies']))) for x in records]
    ck(len(set(fingerprints))==len(cat),'one release plus occupancy separates every partition')
    seq=[];a=[r.brc.CWM_ONE]
    for b in range(1,7):
        v=r.serial(r.edge(2),a[b-1])
        if b>=2:v=r.merge(v,r.serial(r.edge(b-1),a[b-2]))
        if b>=3:v=r.merge(v,r.serial(r.edge((b-1)*(b-2)//2),a[b-3]))
        # edge integer is ONE branch with integer weight; total, not C, counts choices here.
        a.append(v);total=r.total(partial_catalog(range(b)).values())
        ck(v.total==total.total,'BRC total recurrence counts interface patterns')
        seq.append(str(v.total))
    return {'patterns':len(cat),'counts_b_0_to_6':['1']+seq,
            'primitive_projection_checks':tests,'interface_shrink_checks':shrinks,
            'fingerprint_table':records,'transition_sha256':transition_digest.hexdigest()}

def project_family(fam,B):
    out={}
    for (J,c),v in fam.items():merge_at(out,(sigma(J,B),c),v)
    return out

def evolve(fam,op,B,abstract):
    out={};choose=(r.edge(Q(1,3)),r.edge(Q(2,3)))
    for (state,cost),v in fam.items():
        merge_at(out,(state,cost),r.serial(v,choose[0]))
        nxt,delta,_=(abstract_step(state,op,B) if abstract else full_step(state,op))
        merge_at(out,(nxt,cost+delta),r.serial(v,choose[1]))
    return out

def family_digest(fam):
    rows=sorted((repr(k),cw(v)) for k,v in fam.items())
    return hashlib.sha256(json.dumps(rows,sort_keys=True).encode()).hexdigest()

def check_joint_propagation():
    I=frozenset(range(9));B=frozenset(range(6));E=[];lookup={}
    for i,h in enumerate(combinations(range(9),3)):
        key='h'+str(i);lookup[key]=h;E.append(s.TestEvent(key,frozenset(h),r.edge(1)))
    poly=s.assemble(E,I);ck(len(poly)==1205,'all nine-occurrence disjoint-triple assemblies')
    full={(canon(lookup[h] for h in J),0):v for (J,U),v in poly.items()}
    small=project_family(full,B);initial=r.total(full.values());trace=[]
    word=[('release',0),('reserve',(0,1,2)),('release',3),('reserve',(3,4,5)),
          ('release',1),('reserve',(1,3,4)),('release',4),('reserve',(0,4,5))]*2
    for i,op in enumerate(word,1):
        full=evolve(full,op,B,False);small=evolve(small,op,B,True)
        ck(project_family(full,B)==small,'joint CWM and release-count polynomial commute')
        ck(r.total(small.values()).total==initial.total,'all apply/skip/blocked weights retained')
        trace.append({'length':i,'command':op,'full_terms':len(full),'interface_terms':len(small),
                      'interface_sha256':family_digest(small),'total':cw(r.total(small.values()))})
    return {'initial_full_assemblies':len(poly),'command_length':len(word),
            'per_command_apply_weight':'2/3','skip_weight':'1/3',
            'cost':'number of successful release commands; NOT physical energy', 'trace':trace}

def active_monomial(J,weight):
    ans={s.EMPTY:r.edge(weight)}
    for H in J:
        key='E'+','.join(map(str,H))
        ans=s.times(ans,{(frozenset((key,)),frozenset(H)):r.brc.CWM_ONE})
    ck(len(ans)==1,'joint preparation is compatible by original BRC multiplication')
    return next(iter(ans.values()))

def gadget(g,bit):
    off=6*g
    hs=((1,2,3),(4,5,6)) if bit==0 else ((1,2,4),(3,5,6))
    return [tuple(off+x for x in H) for H in hs]

def check_marginal_failure():
    fams=[{},{}];prepared=[]
    for bits in product((0,1),repeat=3):
        J=canon(h for g,bit in enumerate(bits) for h in gadget(g,bit))
        v=active_monomial(J,Q(1,4));fams[sum(bits)%2][J]=v
        prepared.append({'bits':bits,'population':'even' if sum(bits)%2==0 else 'odd',
                         'active_triples':[list(h) for h in J],'weight':cw(v)})
    for f in fams:
        ck(r.total(f.values()).total==1,'declared population has total one')
        ck(all(len(J)==6 and used(J)==frozenset(range(1,19)) for J in f),'same deterministic occupancy and event count')
    marginals=[]
    for a in range(1,19):
        for b in range(a,19):
            vals=[r.total(v for J,v in f.items() if any(a in H and b in H for H in J)) for f in fams]
            ck(vals[0]==vals[1],'all averaged pair co-memberships exactly equal in CWM')
            marginals.append({'a':a,'b':b,'CWM':cw(vals[0])})
    for size in (1,2):
        for inds in combinations(range(3),size):
            tables=[]
            for f in fams:
                t={}
                for J,v in f.items():
                    key=tuple(canon(H for H in J if min(H)>6*g and max(H)<=6*g+6) for g in inds)
                    merge_at(t,key,v)
                tables.append(t)
            ck(tables[0]==tables[1],'full one- and two-gadget joint laws agree')
    outputs=[]
    for f in fams:
        outcomes=[];accepted=r.brc.CWM_ZERO;rejected=r.brc.CWM_ZERO
        for J,v in f.items():
            cur=J;stages=[]
            for b in (1,7,13):
                cur,delta,ok=full_step(cur,('release',b));v=r.serial(v,r.brc.CWM_ONE)
                ck(delta==1 and ok,'each scripted release has an actual member')
                stages.append({'release':b,'state':canon(cur)})
            nxt,_,ok=full_step(cur,('reserve',(3,9,15)));v=r.serial(v,r.brc.CWM_ONE)
            if ok:accepted=r.merge(accepted,v)
            else:rejected=r.merge(rejected,v)
            outcomes.append({'start':canon(J),'release_trace':stages,'F_accepted':ok,
                             'final':canon(nxt),'CWM':cw(v)})
        ck(r.merge(accepted,rejected).total==1,'blocked proposals retained in marginal witness')
        outputs.append({'accepted':cw(accepted),'rejected':cw(rejected),'branches':outcomes})
    ck(outputs[0]['accepted']['W']=='1/4' and outputs[1]['accepted']['W']=='0','four-command observer distinguishes parity populations')
    return {'inventory':list(range(1,19)),'prepared_populations':prepared,
            'pair_marginals':marginals,'equal_one_two_gadget_marginals':True,
            'command_word':['release(1)','release(7)','release(13)','reserve(3,9,15)'],
            'outputs':outputs,'common_coarse_prediction_worst_error_lower_bound':'1/8'}

def check_scope_expansion():
    B=frozenset((1,));L=canon(((1,2,3),));R=canon(((1,4,5),))
    ck(sigma(L,B)==sigma(R,B),'outside partner identity legitimately hidden in old language')
    op=('reserve',(2,6,7));lo=full_step(L,op);ro=full_step(R,op)
    ck(not lo[2] and ro[2],'larger language can distinguish previously hidden partner')
    rejected=False
    try:abstract_step(sigma(L,B),op,B)
    except ValueError:rejected=True
    ck(rejected,'implementation refuses unlicensed interface enlargement')
    return {'interface':[1],'left':L,'right':R,'new_command':op,
            'left_accepts':lo[2],'right_accepts':ro[2],'out_of_scope_call_rejected':rejected}

def main():
    quotient=check_quotient();joint=check_joint_propagation()
    witness=check_marginal_failure();expansion=check_scope_expansion()
    result={'schema':'EM_MEMBERSHIP_INTERFACE_TEST_V1','status':'CONDITIONAL_UNREVIEWED_NOT_NATIVE_FORCE',
            'event_id':'EM-20261008-RESIDUAL-MEMBERSHIP-7C2E8A',
            'global_read':'50f7f62ad67b6573ef86e307fac9cb2f47a2b3a7',
            'source_read':'f7eebe767e574ff2672737814bdb62fde7dfd78a',
            'quotient':quotient,'joint_propagation':joint,'marginal_counterexample':witness,
            'scope_expansion':expansion,'assertions':CHECKS,'BRC_calls':dict(r.CALLS),
            'old_main_suites_executed':False,'native_action_law_supplied':False,
            'native_release_permission_or_cost_supplied':False,'independent_review':False}
    raw=(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    (ROOT/'results.json').write_bytes(raw)
    summary={k:result[k] for k in ('status','assertions','BRC_calls')}
    summary.update(patterns=quotient['patterns'],projection_checks=quotient['primitive_projection_checks'],
                   shrinking_checks=quotient['interface_shrink_checks'],
                   output_bytes=len(raw),output_sha256=hashlib.sha256(raw).hexdigest())
    print(json.dumps(summary,indent=2));(ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
if __name__=='__main__':main()
