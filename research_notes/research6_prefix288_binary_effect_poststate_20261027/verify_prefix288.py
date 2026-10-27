#!/usr/bin/env python3
"""PREFIX-288: exact typed C4-BRC ordered-source-pair binary instrument.
Scientific model: finite source register, sigma ports, zero-extended source shift,
C4 phase control; no native heartbeat H_n dynamics are simulated.
All mass numerators are sums of four oriented BRC pairs, not positive-path shortcuts.
"""
import itertools
import json
from pathlib import Path

# Pair of signed integers encodes a Gaussian integer; C4 phases only.
Q = ((1, 0), (0, 1), (-1, 0), (0, -1))
ZERO = (0, 0)
ONE = (1, 0)

def add(a, b): return a[0] + b[0], a[1] + b[1]
def neg(a): return -a[0], -a[1]
def mul(a, b): return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]
def conj(a): return a[0], -a[1]
def scl(k,a): return k*a[0],k*a[1]
def norm(a): return a[0]**2+a[1]**2
def gsum(values):
    z=ZERO
    for v in values:z=add(z,v)
    return z

def brc_inner(a,b):
    assert len(a)==len(b)
    return gsum(mul(x,conj(y)) for x,y in zip(a,b))

def typed_source_branches(a,q,sigma,j):
    assert sigma in (-1,1) and len(a)==3 and 0<=j<=3
    phase_branch = mul(q,a[j]) if j<3 else ZERO
    shift_branch = scl(sigma,a[j-1]) if 0<=j-1<3 else ZERO
    return phase_branch,shift_branch

def brc_pair_numerator(a,b,q,sigma,j):
    """Returns 4*cross-mass of this output via all four ordered branch pairs."""
    aa=typed_source_branches(a,q,sigma,j)
    bb=typed_source_branches(b,q,sigma,j)
    return gsum(mul(x,conj(y)) for x in aa for y in bb)

def event_raw(a,b,q):
    return gsum(brc_pair_numerator(a,b,q,s,j) for s,j in ((1,1),(-1,2)))

def instrument_raw(a,q):
    return {(s,j):brc_pair_numerator(a,a,q,s,j) for s in (1,-1) for j in range(4)}

def basis(q):
    qb=conj(q)
    qb2=mul(qb,qb)
    K=(neg(q),ONE,qb)
    B=(ONE,ZERO,qb2)
    C=(ONE,scl(2,qb),neg(qb2))
    return K,B,C

def proj_raw(a,b,q):
    """Numerator of projector identity: 2 * raw event BRC bilinear."""
    _,B,C=basis(q)
    x=mul(brc_inner(a,B),conj(brc_inner(b,B)))
    y=mul(brc_inner(a,C),conj(brc_inner(b,C)))
    return add(x,y)

def raw_list(a,q):
    z=instrument_raw(a,q)
    return [z[s,j][0] for s in (1,-1) for j in range(4)]

def main():
    checks={'phase_settings':4,'source_packets':0,'input_phase_cases':0,'ordered_brc_output_bins':0,'binary_effect_bounds':0,'cross_input_projector_identities':0,'complement_instrument_conservation':0,'basis_exact_cases':0,'nonclosure_witness_checks':0}
    all_a=[]
    # 4x4x4x4x4=1024 source packets. Distinguish phase from positive mass.
    for m0,m1,m2,k1,k2 in itertools.product(range(1,5),range(1,5),range(1,5),range(4),range(4)):
        all_a.append((scl(m0,ONE),scl(m1,Q[k1]),scl(m2,Q[k2])))
    assert len(all_a)==1024
    checks['source_packets']=len(all_a)
    for q in Q:
        K,B,C=basis(q)
        for i,u in enumerate((K,B,C)):
            for j,v in enumerate((K,B,C)):
                assert brc_inner(u,v)==(scl((3,2,6)[i],ONE) if i==j else ZERO)
        expected={0:(0,3),1:(2,2),2:(18,6)}
        for i,u in enumerate((K,B,C)):
            event=event_raw(u,u,q)
            assert event==(expected[i][0],0)
            assert sum(raw_list(u,q))==4*expected[i][1]
            checks['basis_exact_cases']+=1
        for n,a in enumerate(all_a):
            b=all_a[(n*17+29)%len(all_a)]
            z=sum(norm(x) for x in a)
            raw=instrument_raw(a,q)
            assert all(v[1]==0 and v[0]>=0 for v in raw.values())
            total=sum(v[0] for v in raw.values())
            assert total==4*z
            e=raw[1,1][0]+raw[-1,2][0]
            assert 0<=e<=3*z
            assert e+(total-e)==4*z
            assert proj_raw(a,a,q)==(2*e,0)
            assert scl(2,event_raw(a,b,q))==proj_raw(a,b,q)
            checks['input_phase_cases']+=1
            checks['ordered_brc_output_bins']+=8
            checks['binary_effect_bounds']+=1
            checks['cross_input_projector_identities']+=1
            checks['complement_instrument_conservation']+=1
    A=(ONE,(0,1),ONE)
    B=(ONE,(0,-1),ONE)
    qa=Q[1]
    aa=raw_list(A,qa)
    bb=raw_list(B,qa)
    assert aa==[1,0,4,1,1,4,0,1],aa
    assert bb==[1,4,0,1,1,0,4,1],bb
    assert sum(aa)==sum(bb)==12
    assert aa[1]+aa[6]==0 and bb[1]+bb[6]==8
    assert event_raw(A,A,qa)==(0,0)
    assert event_raw(B,B,qa)==(8,0)
    # An E-only output cannot be in im(V_q), unless it is zero:
    # j=0 forces the hypothetical re-encoded source b0=0; (-,1) forces b1=0;
    # (+,2) forces b2=0. The present witness has nonzero (+,1) and (-,2).
    assert bb[1]>0 and bb[6]>0 and bb[0]>=0
    checks['nonclosure_witness_checks']+=1
    # Full post-measurement source-port amplitudes, keeping both provenance arms.
    event_branches={}
    for label,packet in (('a',A),('b',B)):
        event_branches[label]={}
        for s,j in ((1,1),(-1,2)):
            p0,p1=typed_source_branches(packet,qa,s,j)
            combined=add(p0,p1)  # amplitude is combined / 2, as declared.
            event_branches[label][f"{'plus' if s==1 else 'minus'}_{j}"]={
                'ordered_arms_raw':[list(p0),list(p1)],'coherent_raw':list(combined),
                'mass_numerator':brc_pair_numerator(packet,packet,qa,s,j)[0]}
    result={
       'status':'PREFIX288_C4_BRC_BINARY_EFFECT_EXACT_PASS',
       'model':'formal 3-source C4 ordered pair BRC; q in {1,i,-1,-i}; zero extension; two ports; four source bins',
       'arithmetic':'Gaussian integers; four provenance-preserving ordered BRC terms per output; no floating point or pi/trig/matrix evolution',
       'formula_raw':'4 M_E(a,b) = BRCcross_E(a,b) = [<a,Bq> conj(<b,Bq>)+<a,Cq> conj(<b,Cq>)]/2',
       'basis':{'Kq':'(-q,1,conj(q))','Bq':'(1,0,conj(q)^2)','Cq':'(1,2conj(q),-conj(q)^2)',
                'norms':[3,2,6], 'binary_effect_values':['0','1/4','3/4'],
                'probability_range':'0 <= P_E <= 3/4, both endpoints achieved',
                'projector_identity':'8 M_E(a,b)=<a,Bq>conj(<b,Bq>)+<a,Cq>conj(<b,Cq>)',
                'poststate_no_go':'im(V_q) intersects E-only output support only at zero; a nonzero E poststate cannot be re-encoded as a fresh 3-source packet without a larger output state type'},
       'checks':checks,
       'witness':{'q':'i','a':'(1,i,1)','b':'(1,-i,1)','raw_a':aa,'raw_b':bb,
                  'denominator':'12','P_E_a':'0','P_E_b':'2/3','P_complement_a':'1','P_complement_b':'1/3',
                  'event_source_arms':event_branches},
       'provenance':{'global_snapshot':'b2fc03d5a419f9dd1b0e0fe239d714a3d895c41d',
                      'project_input_snapshot':'cda176e1a7f322e774553d0f3f89751cf5c3371b',
                      'prior_science':'PREFIX287, commit 2e92228dd0037e80d1ec19e877c4a16217c45ba1',
                      'verification_scope':'4096 finite exact source-input/phase cases, 4096 cross-input instances; all-q algebraic theorem separately hand-derived',
                      'native_status':'not demonstrated: no full prepared H_n/model_law_id or physical detector post-state'}
    }
    dest=Path(__file__).with_name('RESULTS_PREFIX288.json')
    dest.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(result['status'])
    print(json.dumps(checks,sort_keys=True))
    print('WITNESS',result['witness']['P_E_a'],result['witness']['P_E_b'])

if __name__=='__main__':main()
