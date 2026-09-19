from __future__ import annotations
import json, math
from pathlib import Path

SQ3=math.sqrt(3)

def dlog_table(b):
    M=1<<b;Q=1<<(b+2);d={};x=1
    for t in range(M):d[x]=t;x=x*5%Q
    assert len(d)==M and x==1
    return d

def bit_dlog(a,b):
    Q=1<<(b+2);res=a%Q;t=0
    assert res%4==1
    for j in range(b):
        mod=1<<(j+3);rr=res%mod
        if rr==1+(1<<(j+2)):
            t|=1<<j;g=pow(5,1<<j,Q);res=res*pow(g,-1,Q)%Q
        else: assert rr==1
    assert res==1
    return t

def phase(n,b,tab=None,c=1,delta=1):
    if n==0:return None
    M=1<<b;Q=1<<(b+2);v=(n&-n).bit_length()-1;u=(n>>v)%Q
    eps=0 if u%4==1 else 1;a=u if eps==0 else (-u)%Q
    t=(tab or dlog_table(b))[a]
    return (c*t+delta*eps*(M//2)+v*(M//8))%M

def all_phases(N,b):
    tab=dlog_table(b);return [None]+[phase(n,b,tab) for n in range(1,N)]

def round_hex(x,y):
    q=x-y/SQ3;r=2*y/SQ3;s=-q-r;a,b,c=[math.floor(z+.5) for z in(q,r,s)]
    da,db,dc=abs(a-q),abs(b-r),abs(c-s)
    if da>=db and da>=dc:a=-b-c
    elif db>=dc:b=-a-c
    return a,b

def metrics(N,b):
    M=1<<b;phi=all_phases(N,b);bins=[0]*64;cells={};by_layer={}
    for n in range(N):
        if n:
            bins[phi[n]*64//M]+=1;a=2*math.pi*phi[n]/M;r=math.sqrt(n);cell=round_hex(r*math.cos(a),r*math.sin(a))
            v=(n&-n).bit_length()-1;u=(n>>v)%(1<<(b+2));eps=0 if u%4==1 else 1
        else:cell=(0,0);v=0;eps=0
        cells[cell]=cells.get(cell,0)+1;key=(*cell,eps,v);by_layer[key]=by_layer.get(key,0)+1
    mean=(N-1)/64;cv=math.sqrt(sum((x-mean)**2 for x in bins)/64)/mean
    return {'N':N,'b':b,'M':M,'cv':cv,'occupied_2d':len(cells),'occupied_ratio_2d':len(cells)/N,
            'collision_groups_2d':sum(x>1 for x in cells.values()),'maxload_2d':max(cells.values()),
            'occupied_with_eps_v2':len(by_layer),'occupied_ratio_with_eps_v2':len(by_layer)/N,
            'collision_groups_with_eps_v2':sum(x>1 for x in by_layer.values()),'maxload_with_eps_v2':max(by_layer.values())}

def main():
    bit_checks=0
    for b in range(3,13):
        tab=dlog_table(b)
        for a,t in tab.items():
            assert bit_dlog(a,b)==t;bit_checks+=1
    theorem=[]
    for b in range(3,9):
        M=1<<b
        for L in range(b+2,b+7):
            phi=all_phases(1<<L,b);h=[0]*M
            for x in phi[1:]:h[x]+=1
            pedestal=(1<<(L-b))-2;tail=(1<<(b+1))-1
            rem=[x-pedestal for x in h]
            assert min(rem)>=0 and sum(rem)==tail
            theorem.append({'b':b,'L':L,'pedestal_each':pedestal,'tail':tail,'min_remainder':min(rem),'max_remainder':max(rem),'tv_bound':tail/((1<<L)-1)})
    multiplication_pairs=0
    for b,N in ((8,4096),(11,65536)):
        phi=all_phases(N,b);M=1<<b
        for k in (2,3,5,7,11,31):
            for n in range(1,N//k):
                assert phi[k*n]==(phi[k]+phi[n])%M;multiplication_pairs+=1
    critical=[]
    for L in range(10,21):
        N=1<<L;b=math.ceil(math.log2(2*math.pi*math.sqrt(N)))
        x=metrics(N,b);x['outer_spoke_spacing']=2*math.pi*math.sqrt(N)/(1<<b);critical.append(x)
    base=metrics(65536,11);million=metrics(1000001,13)
    result={'schema':'NOLLM_DYADIC_UNIT_LOG_PHASE_VERIFICATION_V1','status':'PROVED_FINITE_MODEL_IDENTITIES_PLUS_FINITE_GEOMETRIC_OBSERVER',
            'coordinate':'n=2^v u; u=(-1)^eps 5^t mod 2^(b+2); phi=t+eps*2^(b-1)+v*2^(b-3) mod 2^b',
            'bitwise_dlog_exact_cases':bit_checks,'multiplication_pairs_checked':multiplication_pairs,
            'dyadic_histogram_theorem_checks':theorem,'base_65536_b11':base,'million_b13':million,'critical_sweep':critical,
            'proved_law':{'histogram':'H(a)=2^(L-b)-2+R(a), R(a)>=0, sum R=2^(b+1)-1 for L>=b+2',
                         'tv_bound':'TV(Phi_b on 1..2^L-1, uniform)<= (2^(b+1)-1)/(2^L-1)',
                         'fourier_bound':'every nontrivial phase Fourier coefficient has the same upper bound',
                         'critical_scaling':'b=L/2+O(1) gives O(2^(-L/2))=O(N^-1/2) global phase discrepancy bound'},
            'observer_boundary':'2D/layered hex occupancy uses floating trig/rounding and remains finite evidence'}
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
    assert base['occupied_with_eps_v2']>base['occupied_2d']
    assert million['occupied_with_eps_v2']>million['occupied_2d']
    print(json.dumps({'PASS':True,'bit_checks':bit_checks,'multiplication_pairs':multiplication_pairs,'base':base,'million':million},indent=2))
if __name__=='__main__':main()
