"""R50: exact upper one-sided record/last-cell certificate; stdlib Python.
Scientific inputs: frozen S23/AV interval from R49; sqrt(2)-1 is independent example.
No floating point. All comparisons at two rational enclosure endpoints.
"""
from math import isqrt
from bisect import bisect_right
from hashlib import sha256
import json

D_S=10**24
S23=(262204504569236716045286,262204504569236716045287,D_S)
D_Q=10**32
sqrt2=isqrt(2*D_Q*D_Q)
assert sqrt2*sqrt2<2*D_Q*D_Q<(sqrt2+1)**2
QUAD=(sqrt2-D_Q,sqrt2+1-D_Q,D_Q)

def height(n,theta,D):
    return (n*theta)%D

def upper_best_brute(K,T,D):
    return min(range(1,K+1),key=lambda k:D-height(k,T,D))

def sb_full_to_limit(K,T,D):
    a,i,c,j=0,1,1,1
    st=[(a,i,c,j)]
    while i+j<=K:
        if (a+c)*D<(i+j)*T: a,i=a+c,i+j
        else:c,j=a+c,i+j
        st.append((a,i,c,j))
    return st

def sb_batched(K,T,D):
    a,i,c,j=0,1,1,1
    blocks=[]
    while i+j<=K:
        u=i*T-a*D
        v=c*D-j*T
        assert u>0 and v>0
        if u>v:
            k=min(u//v,(K-(i+j))//j+1)
            assert k>=1
            a,i=a+k*c,i+k*j
            blocks.append(('lower',k,i+j))
        else:
            k=min(v//u,(K-(i+j))//i+1)
            assert k>=1
            c,j=c+k*a,j+k*i
            blocks.append(('upper',k,i+j))
    return (a,i,c,j),blocks

def sb_first_error_leq(qnum,T,D):
    """First upper Stern-Brocot state with c-j*theta <= qnum/D.
    Batched subtraction performs only Euclidean quotient blocks; never skips
    a crossing inside an upper-neighbor run.
    """
    a,i,c,j=0,1,1,1
    blocks=[]
    while True:
        u=i*T-a*D
        v=c*D-j*T
        assert u>0 and v>0
        if v<=qnum:return (a,i,c,j),blocks
        if u>v:
            k=u//v
            a,i=a+k*c,i+k*j
            blocks.append(('lower',k))
        else:
            run=v//u
            crossing=(v-qnum+u-1)//u
            k=min(run,crossing)
            assert k>=1
            c,j=c+k*a,j+k*i
            blocks.append(('upper',k))

def independent_first_threshold(qnum,T,D,K):
    for state in sb_full_to_limit(K,T,D):
        a,i,c,j=state
        if c*D-j*T<=qnum:return state
    raise AssertionError('no threshold stage reached')

def calc_age(m,H,j,T,D):
    cuts=sorted(((z*T)%D,z) for z in range(m))
    vals=[p for p,z in cuts];out=[None]*m
    for r in range(1,H+1):
        x=((j-r)*T)%D
        p=(bisect_right(vals,x)-1)%m
        label=cuts[p][1]
        if out[label] is None:out[label]=r
    return tuple(out)

def plateau_at_cuts(m,H,T,D):
    K=m+H-1
    phase_order=sorted(range(K+1),key=lambda s:height(s,T,D))
    cuts=sorted((height(z,T,D),z) for z in range(m))
    values=[x for x,z in cuts]
    def ages_at(s):
        x=height(s,T,D);out=[None]*m
        for r in range(1,H+1):
            p=(bisect_right(values,(x-r*T)%D)-1)%m
            z=cuts[p][1]
            if out[z] is None:out[z]=r
        return tuple(out)
    reference=ages_at(phase_order[-1]);left=len(phase_order)-1
    while left and ages_at(phase_order[left-1])==reference:
        left-=1
    witness=None if left==0 else ages_at(phase_order[left-1])
    return {'start_index':phase_order[left], 'cut_cell_count':len(phase_order)-left,
            'previous_cut_index':None if left==0 else phase_order[left-1],
            'previous_age':witness, 'last_age':reference, 'phase_order':phase_order}

def trial(name,m,H,pack,selected_pre=None):
    lo,hi,D=pack;K=m+H-1
    # All phase/boundary comparisons for the finite K-cut atlas are stable.
    assert all((k*lo)//D==(k*hi)//D for k in range(-K,K+1))
    refs=[];state=[]
    for T in (lo,hi):
        full=sb_full_to_limit(K,T,D)
        batched,blocks=sb_batched(K,T,D)
        assert full[-1]==batched
        a,i,c,j=batched
        assert j==upper_best_brute(K,T,D)
        assert j<=K<i+j
        # This is a certificate of minimal upper error among denominators 1..K.
        v=c*D-j*T
        assert 0<v<D
        assert v==min(D-height(k,T,D) for k in range(1,K+1))
        before=[(idx,t[3],t[2]*D-t[3]*T) for idx,t in enumerate(full[:-1]) if t[3]!=j]
        assert all(err>v for idx,q,err in before)
        refs.append(dict(c=c,j=j,phases=K+1,batched_blocks=len(blocks),unit_mediants=len(full)-1,block_steps=blocks,
                         lastcell_error_num=v,lower_denom=i,upper_denom=j))
        state.append(calc_age(m,H,j,T,D))
    assert refs[0]['c']==refs[1]['c'] and refs[0]['j']==refs[1]['j']
    assert refs[0]['block_steps']==refs[1]['block_steps']
    assert state[0]==state[1]
    s=refs[0]['j'];assert all(calc_age(m,H,s,T,D)==state[0] for T in (lo,hi))
    # For each upper Farey stage with v <= q*, its labelled state is the last-cell state.
    for idx,T in enumerate((lo,hi)):
        full=sb_full_to_limit(K+100,T,D)
        for a,i,c,j in full:
            if 0<c*D-j*T<=refs[idx]['lastcell_error_num']:
                assert calc_age(m,H,j,T,D)==state[0]
    plateaux=[plateau_at_cuts(m,H,T,D) for T in (lo,hi)]
    assert plateaux[0]==plateaux[1]
    assert plateaux[0]['last_age']==state[0]
    # Right-half-open cut-cell maximality: the previous cell is different.
    plateau=plateaux[0]
    crossings=[]
    for T in (lo,hi):
        s0=plateau['start_index']
        qplateau=((s0*T//D)+1)*D-s0*T
        selected,trace=sb_first_error_leq(qplateau,T,D)
        assert selected==independent_first_threshold(qplateau,T,D,K)
        crossings.append({'first_upper_c':selected[2], 'first_upper_j':selected[3],
                          'threshold_num':qplateau,'quotient_blocks':len(trace), 'steps':trace})
    assert [(x['first_upper_c'],x['first_upper_j']) for x in crossings][0]==[(x['first_upper_c'],x['first_upper_j']) for x in crossings][1]
    cert={'name':name,'m':m,'H':H,'K':K,'enclosure':{'low':lo,'high':hi,'denominator':D},
          'minimizer':{'s_star':s,'ceil_s_theta':refs[0]['c']},
          'endpoint_records':refs,'lastcell_age':state[0],
          'all_labels_covered':all(v is not None for v in state[0]),
          'maximal_suffix_transfer_crossing':crossings,
          'maximal_suffix_plateau':{'start_index':plateau['start_index'],
             'cut_cell_count':plateau['cut_cell_count'],
             'previous_cut_index':plateau['previous_cut_index'],
             'previous_age':plateau['previous_age']},
          'age_sha256':sha256(json.dumps(state[0],separators=(',',':')).encode()).hexdigest()}
    if selected_pre is not None:
        for T in (lo,hi):
            actual=calc_age(m,H,selected_pre,T,D)
            assert actual!=state[0]
        cert['pre_threshold_witness']={'upper_denominator':selected_pre,'age':calc_age(m,H,selected_pre,lo,D)}
    print('PASS',name,'K',K,'s*',s,'CF_blocks',refs[0]['batched_blocks'],
          'unit_mediants',refs[0]['unit_mediants'],'all_covered',cert['all_labels_covered'])
    return cert

def main():
    tests=[('frozen_s23_128_225',128,225,S23,61),
           ('sqrt2_minus_1_5_8',5,8,QUAD,2),
           ('sqrt2_minus_1_6_12',6,12,QUAD,7),
           ('sqrt2_minus_1_5_1_uncovered',5,1,QUAD,None),
           ('sqrt2_minus_1_3_8',3,8,QUAD,2),
           ('sqrt2_minus_1_8_12',8,12,QUAD,7)]
    out=[trial(*args) for args in tests]
    e=out[1];assert e['minimizer']['s_star']==12
    assert e['pre_threshold_witness']['age']!=e['lastcell_age']
    assert e['maximal_suffix_plateau']['start_index']==7
    assert e['maximal_suffix_plateau']['cut_cell_count']==2
    assert e['maximal_suffix_transfer_crossing'][0]['first_upper_j']==7
    frozen=out[0];assert frozen['minimizer']=={'s_star':225,'ceil_s_theta':59}
    assert frozen['all_labels_covered'] and max(frozen['lastcell_age'])==164
    assert frozen['maximal_suffix_plateau']['start_index']==225
    assert frozen['maximal_suffix_plateau']['cut_cell_count']==1
    assert frozen['maximal_suffix_transfer_crossing'][0]['first_upper_j']==225
    # Certified containment of the irrational in both open enclosures:
    lo,hi,D=QUAD
    assert (lo+D)**2<2*D*D<(hi+D)**2
    # Emit deterministic exact rational certificates for reproducibility.
    fn='R50_CERTIFICATE.json'
    with open(fn,'w',encoding='utf-8') as f:
        json.dump({'schema':'EM_R50_EXACT_ONE_SIDED_RECORD_CERTIFICATE_V1','tests':out},f,ensure_ascii=False,indent=2)
        f.write('\n')
    print('PASS_R50_6_EXACT_FAMILIES',fn)
if __name__=='__main__':main()
