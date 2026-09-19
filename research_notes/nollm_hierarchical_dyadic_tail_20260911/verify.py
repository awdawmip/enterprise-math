from __future__ import annotations
import json
from collections import Counter
from pathlib import Path

L=16
N=1<<L
BASE_B=8
M=1<<BASE_B
R0=(M+5)//6
HEX_DIRS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))


def hdist(a,b):
    dq=a[0]-b[0]; dr=a[1]-b[1]
    return max(abs(dq),abs(dr),abs(dq+dr))


def ring_cell(R,j):
    j%=6*R
    side,u=divmod(j,R)
    if side==0:return (u,-R)
    if side==1:return (R,-R+u)
    if side==2:return (R-u,u)
    if side==3:return (-u,R)
    if side==4:return (-R,R-u)
    return (-R+u,-u)


def annulus(h,t0):
    R=R0+h
    return ring_cell(R,(t0*(6*R))//M)


def dlog_table(b):
    Q=1<<(b+2); MM=1<<b
    tab={}; x=1
    for t in range(MM):
        tab[x]=t; x=x*5%Q
    assert len(tab)==MM and x==1
    return tab


TABLES={b:dlog_table(b) for b in range(BASE_B, L-1)}


def carrier(n):
    if not (1<=n<N):raise ValueError(n)
    v=(n&-n).bit_length()-1
    B=max(BASE_B,L-v-2)
    Q=1<<(B+2)
    u=n>>v
    ur=u%Q
    eps=0 if ur%4==1 else 1
    a=ur if eps==0 else (-ur)%Q
    t=TABLES[B][a]
    t0=t&(M-1)
    d=B-BASE_B
    q=t>>BASE_B
    gray=q^(q>>1)
    h=2*v+eps
    cell=annulus(h,t0)
    return dict(v=v,eps=eps,B=B,d=d,t=t,t0=t0,q=q,gray=gray,h=h,cell=cell)


def hamming(a,b):
    return (a^b).bit_count()


def inverse_gray(g):
    x=0
    while g:
        x ^= g
        g >>=1
    return x


def reconstruct(st):
    d=st['d']
    q=inverse_gray(st['gray']) & ((1<<d)-1 if d else 0)
    t=st['t0']+(q<<BASE_B)
    B=BASE_B+d
    Q=1<<(B+2)
    u=pow(5,t,Q)
    if st['eps']:u=(-u)%Q
    return (1<<st['v'])*u


states=[None]+[carrier(n) for n in range(1,N)]
seen={}
for n in range(1,N):
    s=states[n]
    assert reconstruct(s)==n,(n,s,reconstruct(s))
    key=(s['cell'],s['d'],s['gray'])
    assert key not in seen,(n,seen.get(key),key)
    seen[key]=n
assert len(seen)==N-1

minus_hist=Counter()
for v in range(L):
  for eps in (0,1):
    h=2*v+eps
    if h>31:continue
    hp=2*v+(1-eps)
    for t0 in range(M):
      minus_hist[hdist(annulus(h,t0),annulus(hp,t0))]+=1
assert minus_hist==Counter({1:32*M})

x5_base=Counter();x5_tail=Counter();x5_wrap=0;x5_pairs=0
for n in range(1,(N-1)//5+1):
    a=states[n];b=states[5*n]
    assert a['v']==b['v'] and a['eps']==b['eps'] and a['B']==b['B'] and a['d']==b['d']
    assert b['t']==(a['t']+1)%(1<<a['B'])
    assert b['t0']==(a['t0']+1)%M
    bd=hdist(a['cell'],b['cell']);x5_base[bd]+=1;assert bd<=2
    hd=hamming(a['gray'],b['gray']);x5_tail[hd]+=1;assert hd<=1
    if a['t0']==M-1:
        x5_wrap+=1
        if a['d']>0:assert hd==1
        else:assert hd==0
    else:
        assert a['q']==b['q'] and hd==0
    x5_pairs+=1
assert x5_pairs==(N-1)//5

x2_base=Counter();x2_tail_retained=Counter();x2_depth=Counter();x2_pairs=0
for n in range(1,(N-1)//2+1):
    a=states[n];b=states[2*n]
    assert b['v']==a['v']+1 and b['eps']==a['eps'] and b['t0']==a['t0']
    expected_d=max(a['d']-1,0)
    assert b['d']==expected_d
    assert b['q']==(a['q'] & ((1<<expected_d)-1 if expected_d else 0))
    bd=hdist(a['cell'],b['cell']);x2_base[bd]+=1;assert bd==2
    mask=(1<<expected_d)-1 if expected_d else 0
    retained_src=a['gray']&mask
    hd=hamming(retained_src,b['gray']);x2_tail_retained[hd]+=1;assert hd<=1
    x2_depth[a['d']]+=1
    x2_pairs+=1
assert x2_pairs==(N-1)//2

depth_hist=Counter(s['d'] for s in states[1:])
weighted=sum(d*c for d,c in depth_hist.items())
base_groups=Counter(s['cell'] for s in states[1:])

result={
 'schema':'NOLLM_HIERARCHICAL_DYADIC_TAIL_VERIFICATION_V1',
 'status':'EXACT_DECLARED_HIERARCHICAL_IDENTITY_AND_LOCAL_UPDATE_CERTIFICATE',
 'population':{'L':L,'N':N,'positive':N-1},
 'base':{'b':BASE_B,'M':M,'R0':R0,'outer_R':R0+31,'base_distinct_cells':len(base_groups),'base_max_fiber':max(base_groups.values())},
 'identity':{'hierarchical_states':len(seen),'injective':len(seen)==N-1,'reconstruction_failures':0,
             'tail_depth_histogram':dict(sorted(depth_hist.items())),'max_tail_depth':max(depth_hist),
             'weighted_tail_bits':weighted,'average_tail_depth':weighted/(N-1)},
 'generator_locality':{
   'times_5':{'pairs':x5_pairs,'base_distance_histogram':dict(sorted(x5_base.items())),
              'tail_hamming_histogram':dict(sorted(x5_tail.items())),'low_base_wraps':x5_wrap,'max_tail_bit_flips':max(x5_tail)},
   'times_2':{'pairs':x2_pairs,'base_distance_histogram':dict(sorted(x2_base.items())),
              'retained_tail_hamming_histogram':dict(sorted(x2_tail_retained.items())),
              'source_tail_depth_histogram':dict(sorted(x2_depth.items())),
              'rule':'delete top tail level when d>0; among retained levels at most one Gray bit toggles'},
   'minus_1_abstract':{'declared_base_states':sum(minus_hist.values()),'base_distance_histogram':dict(sorted(minus_hist.items()))}
 },
 'proof_scope':{
   'identity':'(base cell,d,Gray(q)) reconstructs (v,eps,t0,q), then exact odd u modulo 2^(B+2)>u',
   'times_5':'BRGC is cyclic; q changes only on low t0 wrap, so at most one tail bit toggles',
   'times_2':'precision depth drops by one; Gray bits below new top are unchanged except the new top retained bit, hence <=1 toggle',
   'geometry':'base annulus uses integer ring map at b=8; x5 <=2 cells, x2=2 cells, sign flip=1 cell'
 },
 'boundaries':['integer identity retained','not Nollm runtime mapping','not X6','no semantic recall theorem','Q40 physical observer measured separately']
}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
