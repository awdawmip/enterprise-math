#!/usr/bin/env python3
"""PREFIX-659 R6: independent exact 189-layer boundary BRC certificate.
Run: python PREFIX659_R6_EDGE_SLOT_CERTIFICATE.py
Uses stdlib Fraction/integer arithmetic for every asserted inequality.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
import json

N, DEN = 189, 1 << 18
Q, R = F(19,128), F(61,2**24)
HP, HZ = F(1,2**17), F(1,2**16)
PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
P_UP = {12:F('51525.771'),24:F('208463.104')}
V_LO = {12:F('86048.098'),24:F('346339.323')}
V_UP = {12:F('86048.099'),24:F('346339.324')}
checks = 0
def chk(x,msg):
    global checks
    assert x,msg
    checks += 1

@lru_cache(None)
def inside(n,k,a):
    return 40*(n+1)*comb(n,k)*a**k*(DEN-a)**(n-k) > DEN**n

@lru_cache(None)
def wide(n,k):
    if k>n//2: return wide(n,n-k)
    mid=k*DEN//n
    assert inside(n,k,mid)
    if k==0: ll=lh=0
    else:
        lo,hi=0,mid
        while hi-lo>1:
            m=(lo+hi)//2
            if inside(n,k,m): hi=m
            else: lo=m
        ll,lh=lo,hi
    lo,hi=mid,DEN
    while hi-lo>1:
        m=(lo+hi)//2
        if inside(n,k,m): lo=m
        else: hi=m
    rl,rh=lo,hi
    if 4*(rl-lh)>DEN:return True
    if 4*(rh-ll)<DEN:return False
    raise AssertionError(('ambiguous frozen predicate',n,k))

def rows_make():
    state={0:1}; rows=[state.copy()]
    for n in range(1,N+1):
        nxt=defaultdict(int)
        for k,v in state.items():
            nxt[k]+=v;nxt[k+1]+=v
        state={k:v for k,v in nxt.items() if wide(n,k)}
        rows.append(state.copy())
    return rows

def survival(rows,x):
    a,b=x.numerator,x.denominator
    return [F(sum(v*a**k*(b-a)**(n-k) for k,v in rows[n].items()),b**n)
            for n in range(N)]

def main():
    rows=rows_make()
    chk(len(rows)==190,'190 rows including terminal')
    chk(all(sum(rows[n].values())==2**n for n in range(25)),'first 25 intact')
    chk(sum(rows[25].values())==2**25-2,'first two losses at row 25')
    chk(all(rows[n].get(0,0)==0 for n in range(25,190)),'zero path extinct')
    chk(all(rows[n].get(0,0)==1 for n in range(25)),'zero path survives n<25')
    chk(not rows[189],'189-layer stopping bound')
    chk(all(0<=v<=comb(n,k) for n,row in enumerate(rows)
            for k,v in row.items()),'Bernstein coefficients within [0,1]')
    chk(0<Q-HZ<Q+HZ<F(1,6),'z-score neighborhood')
    chk(0<HP<Q-HZ,'disjoint edge coordinate bands')
    chk(HP*(2*HZ)/((2*R)**2)==F(16384,3721),'area ratio')
    chk(Q+HZ<F(1,2) and 1-Q-HZ>F(1,2),'eight images disjoint')
    chk((Q-HZ)*(1-Q+HZ)>F(47,441),'score denominator margin')
    chk(4*21**2*(Q-HZ)*(1-Q+HZ)>188,'score derivative <21')
    # Gamma(25,1) first clock at p=0; exact Poisson-max coefficients.
    t=survival(rows,Q)
    a=[];b=[]
    for m in range(N):
        am=F(1);bm=F(m+1)
        for n in range(25):
            w=F(comb(n+m,n),2**(n+m+1))
            am-=w;bm-=F(n+m+1,2)*w
        a.append(am);b.append(bm)
    mu=F(25)+sum(a[m]*t[m] for m in range(N))
    H=F(325)+sum(b[m]*t[m] for m in range(N))
    W=2*H-mu**2
    chk(F('89.455')<mu<F('89.456'),'mean exact bounds')
    chk(F('605.010')<W<F('605.011'),'variance exact bounds')
    # Derivative of binomial Bernstein survival s_m at Q by exact score.
    td=[]
    for n,row in enumerate(rows[:N]):
        if n==0:td.append(F(0));continue
        score=sum(F(v*Q.numerator**k*(Q.denominator-Q.numerator)**(n-k),
                    Q.denominator**n)*(k-n*Q) for k,v in row.items())
        td.append(score/(Q*(1-Q)))
    muz=sum(a[m]*td[m] for m in range(N))
    Hz=sum(b[m]*td[m] for m in range(N))
    Wz=2*Hz-2*mu*muz
    # Boundary derivative at p=0 is A_n(1)-n*A_n(0).
    sp=[F(row.get(1,0)-n*row.get(0,0))
        for n,row in enumerate(rows[:N])]
    chk(all(sp[n]==0 for n in list(range(25))+list(range(34,N))),
        'boundary slope only rows 25..33')
    chk(all(sp[n]==25 for n in range(25,34)),'nine coefficients equal 25')
    mup=F(0);Hp=F(0)
    for n in range(25,34):
        am=F(1);bm=F(n+1)
        for m in range(N):
            if not t[m]:continue
            w=F(comb(n+m,n),2**(n+m+1))*t[m]
            am-=w;bm-=F(n+m+1,2)*w
        mup+=sp[n]*am;Hp+=sp[n]*bm
    Wp=2*Hp-2*mu*mup
    chk(4<mup<5 and 547<muz<549,'mean derivative intervals')
    chk(-535<Wp<-534 and 42<Wz<43,'variance derivative intervals')
    chk(12*Wz<muz<13*Wz and Wz>0,'slot crossing')
    q0=muz/Wz
    chk(12<q0<13,'q0 lies strictly between 12 and 13')
    DMp=sum(range(N))
    DHp=sum(n*(n+1) for n in range(N))
    DWp=2*DHp+2*378*DMp
    DMz=N*21
    DHz=21*sum(range(1,N+1))
    DWz=2*DHz+2*378*DMz
    chk((DMp,DHp,DWp)==(17766,2250360,17931816),'boundary bounds')
    chk((DMz,DHz,DWz)==(3969,377055,3754674),'interior bounds')
    result={'schema':'EM_PREFIX659_R6_EXACT_EDGE_WITNESS_AND_SLOT_TRANSITION_V1',
      'date':'2026-11-10','frozen_science_pin':PIN,
      'exact_witness':['0','19/128'],'layers':N,
      'strict_mu_interval':['89.455','89.456'],
      'strict_W_interval':['605.010','605.011'],
      'slot_transition_q0':'mu_z/W_z',
      'slot_transition_strict_interval':['12','13'],
      'selected_edge_rectangle':{'p':['0',str(HP)],'z':[str(Q-HZ),str(Q+HZ)]},
      'old_eight_squares_center':['3/20','1/8'],
      'old_eight_squares_half_width':str(R),
      'single_rectangle_area_ratio_to_old_square':'16384/3721',
      'new_orbit_rectangle_count':8,
      'derivative_bounds':{'p_mu':str(DMp),'p_H':str(DHp),'p_W':str(DWp),
                           'z_mu':str(DMz),'z_H':str(DHz),'z_W':str(DWz)},
      'q_values':{},
      'arithmetic':'Exact stdlib Fraction and integer bisection',
      'proof_status':'AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED',
      'scope':'frozen two-direction BRC observer on full [0,1]^2, real q in [12,24]'}
    for q in (12,24):
        v=q*q*W-q*mu
        chk(V_LO[q]<v<V_UP[q],'exact q-variance strict interval')
        dp=q*q*Wp-q*mup;dz=q*q*Wz-q*muz
        chk(dp<0,'negative p-inward slope')
        if q==12:chk(-451<dz<-449,'negative q12 z slope')
        else:chk(11344<dz<11347,'positive q24 z slope')
        kp=q*q*DWp+q*DMp
        kz=q*q*DWz+q*DMz
        loss=HP*kp+HZ*kz
        old_loss=2*R*kz
        gap=V_LO[q]-P_UP[q]-loss-old_loss
        chk(gap>0,'all new rectangle points beat old square')
        chk(gap>(2600 if q==12 else 10000),'strict useful gap')
        lo,hi=(-77041,-77039) if q==12 else (-308046,-308044)
        chk(lo<dp<hi,'inward slope enclosure')
        result['q_values'][str(q)]={
          'witness_variance_strict':[str(V_LO[q]),str(V_UP[q])],
          'inward_p_derivative_strict_integer_enclosure':[lo,hi],
          'z_derivative_strict_integer_enclosure':[-451,-449] if q==12 else [11344,11347],
          'p_gradient_cap':str(kp),'z_gradient_cap':str(kz),
          'edge_rectangle_loss_upper':str(loss),
          'previous_eight_squares_excess_upper':str(old_loss),
          'strict_new_rectangle_over_all_old_squares_lower':str(gap)}
    g12=F(result['q_values']['12']['strict_new_rectangle_over_all_old_squares_lower'])
    g24=F(result['q_values']['24']['strict_new_rectangle_over_all_old_squares_lower'])
    chk(g12>2600 and g24>10000,'endpoint margins positive')
    chk(12*min(g12/12,g24/24)>2600,'all real q by affine interpolation')
    result['uniform_q_interval']=['12','24']
    result['strict_gap_for_all_q_and_all_new_old_pairs']='>2600'
    result['checks_passed']=checks
    result['result']='ALL_CHECKS_PASS'
    print(json.dumps(result,indent=2,ensure_ascii=False))
    print('ALL_CHECKS_PASS',checks)

if __name__=='__main__':main()
