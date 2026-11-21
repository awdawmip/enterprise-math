#!/usr/bin/env python3
"""R5 genuine-event primitive-17 next-pole exact checker; no external packages.
Every event keeps its own load. Derivatives are Euler q*d/dq before
reducing modulo Phi_17. Scientific status NOT_REVIEWED.
"""
import json
D = 17
Z = (0,)*D
U = (1,) + (0,)*16
S = {1:set(range(214,219)), 2:{214,216,217,218,219,220,221}, 4:set(range(215,222))}
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def times(a,k): return tuple(x*k for x in a)
def shift(a,n): return tuple(a[(i-n)%D] for i in range(D))
def mul(a,b):
    out=[0]*D
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[(i+j)%D]+=x*y
    return tuple(out)
def reduce(a): return [x-a[16] for x in a[:16]]
def w_factor(prices):
    w,dw=U,Z
    for p in prices:
        wnext=plus(w,times(shift(w,p),-1))
        dnext=plus(plus(dw,times(shift(dw,p),-1)),times(shift(w,p),-p))
        w,dw=wnext,dnext
    return w,dw

def genuine_mask_sum(m):
    R,DR=Z,Z
    for mask in range(1,8):
        bits=[b for b in (1,2,4) if mask&b]
        prices=sorted(set().union(*(S[b] for b in bits)))
        states={(0,)*len(bits):(U,Z)}
        for p in prices:
            next_states={}
            incidence=tuple(int(p in S[b]) for b in bits)
            for loads,(v,dv) in states.items():
                cap=min(m-1-loads[i] for i,t in enumerate(incidence) if t)
                for a in range(cap+1):
                    key=tuple(loads[i]+a*incidence[i] for i in range(len(bits)))
                    rotated=shift(v,p*a)
                    rotated_d=plus(shift(dv,p*a),times(rotated,p*a))
                    prior=next_states.get(key,(Z,Z))
                    next_states[key]=(plus(prior[0],rotated),plus(prior[1],rotated_d))
            states=next_states
        P,DP=Z,Z
        for v,dv in states.values():P,DP=plus(P,v),plus(DP,dv)
        W,DW=w_factor(prices)
        r=mul(P,W)
        dr=plus(mul(DP,W),mul(P,DW))
        sign=1 if mask.bit_count()%2 else -1
        R,DR=plus(R,times(r,sign)),plus(DR,times(dr,sign))
    return reduce(R),reduce(DR)

def result():
    rows=[]
    for m in range(13,18):
        R,DR=genuine_mask_sum(m)
        assert R==[0]*16, ('m',m,'unexpected_order6',R)
        # S4 prices 296..312 cover all residue classes mod 17.
        # Its bounded complete homogeneous sum equals 1 for m<=17.
        # D[(1-q^306)*prod_{p in S4,p!=306}(1-q^p)] at zeta17 = -306*17.
        dtotal=DR.copy();dtotal[0]-=5202
        assert dtotal!=[0]*16
        rows.append({'m':m,'DR_A':DR,'DR_total':dtotal})
    assert rows[0]['DR_total']==[-13328,-8840,-11084,-13073,-15062,-17442,-15691,-13872,-4845,5763,12614,19448,22287,19431,12818,8160]
    return {'status':'PASS','field':'Z[z]/Phi_17(z)','Euler_derivative':'D=q*d/dq',
            'true_intersections':True,'E3_order_at_most':2,
            'R_at_root_for_all_five':[0]*16,'rows':rows,
            'consequence':'for m=13..17, primitive 17 next Laurent pole order exactly 5; period mod O_m(N^3) divisible by 17',
            'independence':'direct load-state DP; no grouped h_u/h_v compression',
            'review':'NOT_REVIEWED'}
if __name__=='__main__': print(json.dumps(result(),ensure_ascii=False,indent=2))
