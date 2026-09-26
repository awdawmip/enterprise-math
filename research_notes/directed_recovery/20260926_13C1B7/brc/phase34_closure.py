"""Exact BRC effect closure; split symmetric and skew sectors as Stage87.
Independent new phase3+phase4 scope. No new phase/compiler/precision.
"""
from phase34_carrier import *
from itertools import combinations_with_replacement,combinations
from stage86.phase_predictor import Echelon

def decode(x):
    if isinstance(x,dict):
        if set(x)=={'n','d'}:return F(int(x['n']),int(x['d']))
        return {k:decode(v) for k,v in x.items()}
    if isinstance(x,list):return tuple(decode(v) for v in x)
    return x

def main():
    start=time.perf_counter_ns();vendor=verify_vendor()
    raw=(OUT/'RESULTS.json').read_bytes();data=decode(json.loads(raw));native=data['native_operators']
    pairs=tuple(combinations_with_replacement(range(5),2));index={ij:i+1 for i,ij in enumerate(pairs)}
    maps={};receipts={}
    for name,(s,K,L) in native.items():
        M=[[F(0)]*16 for _ in range(16)]
        if name.startswith('V'):M[0][0]=1
        else:
            k=3 if name[0]=='A' else 4;M[0][0]=F(name[1]=='0');M[0][index[k,k]]=1 if name[1]=='1' else -1
        for oi,(i,j) in enumerate(pairs,1):
            for (k,l),ci in index.items():M[oi][ci]=mul(L[i][k],L[j][l])+(mul(L[i][l],L[j][k]) if k!=l else 0)
        mat=tuple(map(tuple,M));nums,den,cols=rational_matrix_columns(mat)
        actual=transpose(cols);assert actual==mat
        maps[name]=actual;receipts[name]={'numerators':nums,'denominator':den}
    # Reachable effects from total mass: exact rational pivots retain real words.
    E=Echelon(16);E.append((1,)+(0,)*15,());front=[0];depths=[1]
    while front:
        new=[]
        for i in front:
            for name,M in maps.items():
                row=tuple(dot(E.originals[i],col) for col in zip(*M))
                if E.append(row,(name,)+E.words[i]):new.append(len(E.originals)-1)
        front=new;depths.append(len(E.originals));print('symmetric closure layer',len(depths)-1,'rank',len(E.originals),'BRC',len(CALLS),flush=True)
        if len(E.originals)==16:break # ambient bound already certifies closure; all transforms checked below
        assert len(depths)<18
    assert len(E.originals)==16
    transforms={}
    for name,M in maps.items():
        transforms[name]=tuple(E.coefficients(tuple(dot(e,col) for col in zip(*M))) for e in E.originals)
    for i,row in enumerate(E.originals):assert E.coefficients(row)==tuple(F(i==j) for j in range(16))
    save('SYMMETRIC_CLOSURE.json',{'rank':16,'depths':depths,'basis_rows':E.originals,'basis_words':E.words,
      'pivots':[r[0] for r in E.rows],'normalized_rows':[r[1] for r in E.rows],
      'transforms':[r[2] for r in E.rows],'pullback_closure_coordinates':transforms,'maps':maps,'map_receipts':receipts,
      'input_sha256':hashlib.sha256(raw).hexdigest(),'all_rows_reconstructed':True})
    print('symmetric16 all closure/reconstruction checks passed',flush=True)
    skewpairs=tuple(combinations(range(5),2))
    def expand(row):
        M=[[F(0)]*5 for _ in range(5)]
        for x,(i,j) in zip(row,skewpairs):M[i][j]=x;M[j][i]=-x
        return tuple(map(tuple,M))
    # CV3 exposes J_logical tensor skew(e0,n3); nonzero scalar removed.
    S=Echelon(10);S.append((1,)+(0,)*9,('CV3_SKEW_SEED',));front=[0];skewdepth=[1]
    while front:
        new=[]
        for i in front:
            M=expand(S.originals[i])
            for name,(_,_,L) in native.items():
                pulled=mm(mm(transpose(L),M),L)
                assert all(pulled[i][j]==-pulled[j][i] for i in range(5) for j in range(5))
                row=tuple(pulled[i][j] for i,j in skewpairs)
                if S.append(row,(name,)+S.words[i]):new.append(len(S.originals)-1)
        front=new;skewdepth.append(len(S.originals));print('skew closure layer',len(skewdepth)-1,'rank',len(S.originals),'BRC',len(CALLS),flush=True)
        if len(S.originals)==10:break
        assert len(skewdepth)<12
    assert len(S.originals)==10
    skewmaps={}
    for name,(_,_,L) in native.items():
        rows=[]
        for row in S.originals:
            pulled=mm(mm(transpose(L),expand(row)),L)
            rows.append(S.coefficients(tuple(pulled[i][j] for i,j in skewpairs)))
        skewmaps[name]=tuple(rows)
    for i,row in enumerate(S.originals):assert S.coefficients(row)==tuple(F(i==j) for j in range(10))
    save('SKEW_CLOSURE.json',{'rank':10,'depths':skewdepth,'pairs':skewpairs,'rows':S.originals,'words':S.words,
      'pivots':[r[0] for r in S.rows],'normalized_rows':[r[1] for r in S.rows],'transforms':[r[2] for r in S.rows],
      'pullback_closure_coordinates':skewmaps,'all_rows_reconstructed':True})
    result={'schema':'PHASE34_EXACT_EFFECT_CLOSURE_V1','status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED',
      'source_bundle_head':data['source_bundle_head'],'activity':data['activity'],
      'symmetric_internal_rank':16,'symmetric_depths':depths,'skew_internal_rank':10,'skew_depths':skewdepth,
      'logical_symmetric_rank':3,'logical_skew_rank':1,'joint_effect_dimension':3*16+10,
      'upper_bound':58,'method':'EXACT_RATIONAL_BRC_ELIMINATION_AND_TRANSPOSE_PARITY_DIRECT_SUM',
      'scope':'one coherent logical bit; frozen phase3+phase4 and inverses; A/D; H/Z/CV3/CV4',
      'actual_BRC_core_calls':len(CALLS),'vendor':vendor,'elapsed_ns':time.perf_counter_ns()-start,
      'all_scientific_products_typed':'unchanged signed_dot_brc and rational_matrix_columns; exact quotient with multiply-back',
      'no_full_Shor_regression_run':True,'finite_scope_not_hardware_or_world_dimension':True}
    save('CLOSURE_RESULTS.json',result);save('CLOSURE_ARITHMETIC_CERTIFICATE.json',{'vendor':vendor,'actual_calls':CALLS,'bareiss':ARITHMETIC_AUDIT})
    print('PASS joint exact dimension58; BRC calls',len(CALLS),flush=True)

if __name__=='__main__':main()
