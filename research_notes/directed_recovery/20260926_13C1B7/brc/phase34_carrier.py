"""New bounded phase3+phase4 carrier audit on immutable Stage87 bundle.
Actual BRC reused unchanged; no full Stage87/Shor replay or remote write.
"""
from pathlib import Path
import sys, json, hashlib, math, time
from fractions import Fraction as F

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'stage87-source'
sys.path.insert(0,str(SOURCE))
from stage45.brc_loop_recheck import verify_vendor,CALLS
from stage83.moving_reader import signed_dot_brc as dot,solve_spd_brc,rational_matrix_columns
from stage80.fixed_phase import FixedRotor,apply_word
from stage86.phase_predictor import spd_certificate,mm,transpose,ident,mul
from stage82.gram_memory import ARITHMETIC_AUDIT

OUT=HERE/'phase34_output';OUT.mkdir(exist_ok=True)
def encode(x):
    if isinstance(x,F):return {'n':str(x.numerator),'d':str(x.denominator)}
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x
def save(name,data):
    (OUT/name).write_text(json.dumps(encode(data),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def gram(rows):return tuple(tuple(dot(a,b) for b in rows) for a in rows)
def projection_residual(v,basis):
    H=gram(basis);rhs=tuple(dot(b,v) for b in basis)
    scale=math.lcm(*(x.denominator for row in H for x in row),*(x.denominator for x in rhs))
    c=solve_spd_brc(tuple(tuple(int(x*scale) for x in row) for row in H),tuple(int(x*scale) for x in rhs))
    residual=tuple(x-dot(c,tuple(b[j] for b in basis)) for j,x in enumerate(v))
    assert all(dot(b,residual)==0 for b in basis)
    return residual,c
def integer_row(v):
    den=math.lcm(*(x.denominator for x in v))
    return tuple(int(x*den) for x in v),den
def apply_rotor(rot,v,inverse=False):
    numer,den=integer_row(v)
    got=tuple(F(x,den*rot.den) for x in rot.apply_numer(numer,inverse))
    direct,directden=apply_word(numer,den,rot.inverse_phase_word,inverse)
    assert got==tuple(F(x,directden) for x in direct)
    return got

def main():
    start=time.perf_counter_ns();vendor=verify_vendor()
    doc=json.loads((SOURCE/'stage80/RESULTS.json').read_text())
    rotors={m:FixedRotor(tuple(map(int,doc['phase_gates'][str(m)]['integer_unit_vector'])),64,{'inherited_stage':80,'phase':m}) for m in (3,4)}
    for m,rot in rotors.items():assert list(map(list,rot.word))==doc['phase_gates'][str(m)]['word_to_basis']
    D=61;e0=tuple(F(i==0) for i in range(D));S=1<<64
    n={m:(F(0),)+tuple(F(x,S) for x in rot.z[1:]) for m,rot in rotors.items()}
    directions={}
    for name,prefix,mode in [('A',( ('neg',1),('h4',0,1,2,4)),2),('D',( ('h4',2,3,59,60),),3)]:
        v,d=apply_word(tuple(int(i==mode) for i in range(D)),1,prefix,True)
        directions[name]=tuple(F(x,d) for x in v)
        assert dot(directions[name],directions[name])==1
    u,d=directions['A'],directions['D'];old=(e0,n[3],u,d);B=(e0,n[3],n[4],u,d)
    H=gram(B);cert=spd_certificate(H);oldcert=spd_certificate(gram(old))
    assert cert['full_rank_certified'] and cert['rank']==5
    assert oldcert['full_rank_certified'] and oldcert['rank']==4
    print('carrier rank5 certified, BRC calls',len(CALLS),flush=True)
    I=ident(5);native={};checks=[]
    for m,k in [(3,1),(4,2)]:
        a=F(rotors[m].z[0],S);h=H[k][k]
        assert h==1-mul(a,a)
        K=[[F(0)]*5 for _ in range(5)];K[0][0]=-2*h;K[0][k]=2*a;K[k][0]=-2*a;K[k][k]=-2
        for inv in (False,True):
            Q=transpose(K) if inv else tuple(map(tuple,K));hQ=mm(H,Q)
            L=tuple(tuple(hQ[i][j]+F(i==j) for j in range(5)) for i in range(5))
            name=f'V{m}'+('inv' if inv else '')
            native[name]=(F(1),Q,L)
            for j in range(D):
                e=tuple(F(i==j) for i in range(D));raw=apply_rotor(rotors[m],e,inv)
                y=tuple(b[j] for b in B)
                assert tuple(dot(b,raw) for b in B)==tuple(dot(row,y) for row in L)
                checks.append((name,j))
            # Exact Gram-unitarity on moment coordinates and inverse identity.
        assert mm(native[f'V{m}'][2],native[f'V{m}inv'][2])==I
    for label,k in [('A',3),('D',4)]:
        for outcome in (0,1):
            s=F(outcome==0);sign=1 if outcome else -1
            K=tuple(tuple(F(sign if i==j==k else 0) for j in range(5)) for i in range(5))
            hK=mm(H,K);L=tuple(tuple(hK[i][j]+s*F(i==j) for j in range(5)) for i in range(5))
            native[label+str(outcome)]=(s,K,L)
    r,rc=projection_residual(n[4],old);rnorm=dot(r,r);assert rnorm>0
    # A raw coordinate outside T34 supplies another legal old-quotient-equal input.
    z=None
    for j in range(D):
        cand,zc=projection_residual(tuple(F(i==j) for i in range(D)),B)
        if dot(cand,cand)>0:z=cand;zseed=j;zcoef=zc;break
    assert z is not None
    znorm=dot(z,z)
    assert all(dot(b,r)==0 and dot(b,z)==0 for b in old)
    assert all(dot(b,z)==0 for b in B)
    # Density inputs |0><0| tensor rr^T/<r,r>, zz^T/<z,z> are positive trace1.
    # Both have Z00=1 and C=0 in all39 old moments. New future V4; A1 separates.
    yr=apply_rotor(rotors[4],r);yz=apply_rotor(rotors[4],z)
    amp_r=dot(u,yr);amp_z=dot(u,yz)
    p_r=mul(amp_r,amp_r)/rnorm;p_z=mul(amp_z,amp_z)/znorm
    assert 0<p_r<=1 and p_z==0
    assert yz==z
    # Confirm old phase3 doesn't reveal either; A/D old effects all vanish.
    for inv in (False,True):
        assert apply_rotor(rotors[3],r,inv)==r and apply_rotor(rotors[3],z,inv)==z
    result={'schema':'PHASE34_CARRIER_AND_OLD39_COUNTEREXAMPLE_V1',
      'status':'AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED','activity':'RA-BC9CF141D000E1FE25AF22EA',
      'source_bundle_head':'0852cad130c1d877174d235687cf60c19f318c58',
      'source_bundle_sha256':'a0eb15a32c4db5a9fd0876f64a0ffd8dbedcd5eabb2a148c247a8886836e5a9c',
      'B_names':['e0','n3','n4','u','d'],'B':B,'H':H,'old_gram_certificate':oldcert,'new_gram_certificate':cert,
      'native_operators':native,'phase_full_column_intertwining_checks':checks,
      'each_frozen_rotor_all_columns_checked':{m:rot.full_columns_checked for m,rot in rotors.items()},
      'old_carrier_residual':{'source':'n4','projection_coefficients':rc,'residual':r,'norm_squared':rnorm},
      'second_state':{'seed_raw_mode':zseed,'projection_coefficients':zcoef,'residual':z,'norm_squared':znorm},
      'old39_equal':{'Z00':1,'Z01':0,'Z11':0,'all_C_entries':0},
      'separating_future':['V4','A1'],'probabilities':{'rho_r':p_r,'rho_z':p_z},
      'coherent_binary_moment_upper_bound':58,'upper_bound_is_minimality_proof':False,
      'future_scope':['A0','A1','D0','D1','V3','V3inv','V4','V4inv','CV3','CV3inv','CV4','CV4inv','Z0','Z1','H'],
      'vendor':vendor,'actual_BRC_core_calls':len(CALLS),'elapsed_ns':time.perf_counter_ns()-start}
    save('RESULTS.json',result);save('ARITHMETIC_CERTIFICATE.json',{'vendor':vendor,'actual_calls':CALLS,'bareiss':ARITHMETIC_AUDIT})
    print('PASS new carrier=5; old39 same; V4,A1 probabilities positive vs0;',len(CALLS),'actual BRC calls',flush=True)
    print('p_r exact fraction saved; numerator bits',p_r.numerator.bit_length(),'denominator bits',p_r.denominator.bit_length(),flush=True)

if __name__=='__main__':main()
