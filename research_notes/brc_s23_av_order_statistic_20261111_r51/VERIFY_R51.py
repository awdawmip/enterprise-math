"""R51 exact k-rightmost phase rank/select, two-sided SB separation certificate.

Classical irrational circle-rotation auxiliary observer, not a native X6/heartbeat
arithmetic calculation. Python stdlib only; all tested comparisons integral.
Frozen scientific reference: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from math import isqrt
from bisect import bisect_right
from time import perf_counter
from heapq import nlargest
import json

S23=(262204504569236716045286,262204504569236716045287,10**24)
D_Q=10**32
sq2=isqrt(2*D_Q*D_Q)
assert sq2*sq2<2*D_Q*D_Q<(sq2+1)**2
QUAD=(sq2-D_Q,sq2+1-D_Q,D_Q)

class FloorOracle:
    def __init__(self,a,d):
        assert 0<a<d
        self.a=a;self.d=d;self.invocations=0;self.euclid_loops=0
        self.bit_peak=max(a.bit_length(),d.bit_length())
        self.base_cache={}
    def floor_sum(self,n,a,b):
        m=self.d; total=0; self.invocations+=1
        while True:
            self.euclid_loops+=1
            self.bit_peak=max(self.bit_peak, n.bit_length(), m.bit_length(),a.bit_length(),b.bit_length())
            if a>=m:
                total+=(n-1)*n*(a//m)//2
                a%=m
            if b>=m:
                total+=n*(b//m)
                b%=m
            y=a*n+b
            self.bit_peak=max(self.bit_peak,y.bit_length(),total.bit_length())
            if y<m:return total
            n,b=divmod(y,m)
            m,a=a,m
    def count(self,n,t):
        assert 0<=t<=self.d
        if n not in self.base_cache:
            self.base_cache[n]=self.floor_sum(n,self.a,self.a)
        return self.floor_sum(n,self.a,self.a+t)-self.base_cache[n]
    def kth(self,k,n):
        assert 1<=k<=n
        lo,hi=1,self.d
        q=0
        while lo<hi:
            mid=(lo+hi)//2
            q+=1
            if self.count(n,mid)>=k:hi=mid
            else:lo=mid+1
        t=lo
        assert self.count(n,t)==k and self.count(n,t-1)==k-1,('phase_collision',n,k,t)
        left,right=1,n
        while left<right:
            mid=(left+right)//2
            if self.count(mid,t)-self.count(mid,t-1):right=mid
            else:left=mid+1
        s=left
        assert self.d-(s*self.a%self.d)==t
        return s,t,q

def sb_terminal(K,A,D):
    assert K>=1 and 0<A<D
    a,i,c,j=0,1,1,1;blocks=0;steps=0
    while i+j<=K:
        u=i*A-a*D;v=c*D-j*A
        assert u>0 and v>0
        if u>v:
            z=min(u//v, (K-(i+j))//j+1)
            a,i=a+z*c,i+z*j
        else:
            z=min(v//u,(K-(i+j))//i+1)
            c,j=c+z*a,j+z*i
        blocks+=1;steps+=z
    assert c*i-a*j==1 and j<=K<i+j
    return dict(lower=(a,i),upper=(c,j),u=i*A-a*D,v=c*D-j*A,
                quot_blocks=blocks,mediants=steps)

def certify_enclosure(K,p):
    L,U,D=p
    assert 0<L<U<D
    # midpoint B/Q, whole-interval radius (U-L)/Q.
    B=L+U;Q=2*D
    st=sb_terminal(K,B,Q)
    bound=K*(U-L)
    assert min(st['u'],st['v'])>bound,(min(st['u'],st['v']),bound)
    # 0<k<=K has distance from k*midpoint to any integer >= min(u,v)/Q;
    # perturbation to either true parameter endpoint <= k*(U-L)/Q.
    return dict(mid_num=B,mid_den=Q,lower=st['lower'],upper=st['upper'],
                lower_error_numerator=st['u'],upper_error_numerator=st['v'],
                perturbation_bound_numerator=bound,
                quotient_blocks=st['quot_blocks'],mediants=st['mediants'])

def source_age_at_cut(m,H,s,A,D):
    historical=sorted(((z*A)%D,z) for z in range(m))
    cph=[v for v,z in historical]
    x=s*A%D
    ages=[None]*m
    for r in range(1,H+1):
        p=bisect_right(cph,(x-r*A)%D)-1
        z=historical[p][1]
        if ages[z] is None: ages[z]=r
    return tuple(ages)

def brute_rightmost(K,A,D):
    return sorted(range(1,K+1), key=lambda s: (s*A)%D, reverse=True)

def experiment(name,m,H,p,depth,brute=False):
    K=m+H-1
    cert=certify_enclosure(K,p)
    a,d=cert['mid_num'],cert['mid_den']
    f=FloorOracle(a,d)
    start=perf_counter()
    rows=[];terminal=None;last_same=0;first_change=None
    for k in range(1,min(depth,K)+1):
        s,t,q=f.kth(k,K)
        ages=source_age_at_cut(m,H,s,a,d)
        if terminal is None:terminal=ages
        if first_change is None:
            if ages==terminal:last_same=k
            else:first_change=dict(rank=k,index=s,ages=ages)
        rows.append(dict(rank=k,index=s,phase_gap_num=t,phase_gap_den=d,
                         age_vector=ages if k<=4 else None,binary_queries=q))
    elapsed=perf_counter()-start
    for P in (p[0],p[1]):
        assert [source_age_at_cut(m,H,rec['index'],P,p[2]) for rec in rows[:min(4,len(rows))]]==[
          source_age_at_cut(m,H,rec['index'],a,d) for rec in rows[:min(4,len(rows))]]
    if brute:
        expected=brute_rightmost(K,a,d)[:len(rows)]
        assert expected==[r['index'] for r in rows],(name,expected,rows)
        # Strict phase order stable across all params in source enclosure.
        assert brute_rightmost(K,p[0],p[2])==brute_rightmost(K,p[1],p[2])==brute_rightmost(K,a,d)
    else:
        # Independent O(K) oracle keeps only the requested k leaders, not an atlas.
        scan=nlargest(len(rows),range(1,K+1),key=lambda z:z*a%d)
        assert scan==[r['index'] for r in rows],(name,scan)
    return dict(name=name,m=m,H=H,K=K,enclosure={'lo':p[0],'hi':p[1],'den':p[2]},
                separation_certificate=cert,top=rows,terminal_vector=terminal,
                identical_terminal_cells_in_prefix=last_same,
                first_different=first_change,counts={'floorsum_invocations':f.invocations,
                'euclidean_loops':f.euclid_loops,'peak_arithmetic_bits':f.bit_peak,
                'elapsed_seconds':round(elapsed,6)},brute_crosscheck=brute)

def run():
    cases=[]
    # R50 exact S23, and R50 local quadratic witness.
    cases.append(experiment('frozen_S23_m128_H225',128,225,S23,5,True))
    cases.append(experiment('quadratic_m5_H8',5,8,QUAD,7,True))
    cases.append(experiment('quadratic_m8_H17',8,17,QUAD,6,True))
    cases.append(experiment('quadratic_m16_H25',16,25,QUAD,6,True))
    cases.append(experiment('quadratic_m17_H9',17,9,QUAD,6,True))
    cases.append(experiment('quadratic_m23_H31',23,31,QUAD,6,True))
    cases.append(experiment('quadratic_m5_H1',5,1,QUAD,5,True))
    # K is genuinely large: no cut atlas construction, exact rank and ID.
    cases.append(experiment('quadratic_K_100000',8,99993,QUAD,4,False))
    cases.append(experiment('quadratic_K_1000000',8,999993,QUAD,3,False))
    # An entirely independent rational endpoint rank oracle with explicit prefix counts,
    # on a modest finite test. This does not assume the terminal plateau algorithm.
    for case in cases[:7]:
        a=case['separation_certificate']['mid_num'];d=case['separation_certificate']['mid_den']
        for rec in case['top']:
            t=rec['phase_gap_num']
            assert sum(d-(q*a%d)<=t for q in range(1,case['K']+1))==rec['rank']
    assert cases[0]['top'][0]['index']==225
    assert cases[0]['first_different'] is not None and cases[0]['first_different']['rank']==2
    assert cases[1]['top'][0]['index']==12
    assert cases[1]['identical_terminal_cells_in_prefix']>=2
    assert cases[1]['first_different'] is not None
    result={'version':'R51_EXACT_RANK_SELECT_V1','scientific_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
            'cases':cases,'summary':{'passed_cases':len(cases),
             'total_floor_sum_invocations':sum(x['counts']['floorsum_invocations'] for x in cases),
             'total_euclidean_iterations':sum(x['counts']['euclidean_loops'] for x in cases)}}
    with open('R51_CERTIFICATE.json','w') as out:json.dump(result,out,ensure_ascii=False,indent=2)
    for x in cases:
        print('PASS_R51',x['name'],'K',x['K'],'top_indices',[t['index'] for t in x['top']],
              'identical_prefix',x['identical_terminal_cells_in_prefix'],'first_change',
              x['first_different'] and x['first_different']['rank'],'floor_calls',x['counts']['floorsum_invocations'],
              'loops',x['counts']['euclidean_loops'],'bits',x['counts']['peak_arithmetic_bits'])
    print('PASS_R51_TOTAL',result['summary'])

if __name__=='__main__':run()
