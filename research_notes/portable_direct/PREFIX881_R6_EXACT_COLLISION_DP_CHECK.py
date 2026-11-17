#!/usr/bin/env python3
"""PREFIX-881 exact signed-event / carry-borrow DP collision test. Python >=3.9."""
import json

def is_step(delta, p):
    z=abs(delta)
    return delta==0 or (z&(z-1))==0 and z<(1<<p)

def witness(p,a,d,e):
    """Return least detected old state u for two events X=(u,u+d), Y=(u+a,u+a+e), else None."""
    assert p>=1 and is_step(d,p) and is_step(e,p)
    N=1<<p
    L=max(0,-a,-d,-a-e)
    U=min(N-1,N-1-a,N-1-d,N-1-a-e)
    if L>U: return None
    states={(0,0,0):0} # (carry for u+a, borrow of u-L, borrow of U-u) => one low-bit prefix
    for i in range(p):
        nxt={}
        ai=(a>>i)&1
        # a can be negative: two's-complement low bits; require Y in [0,N) by interval
        li=(L>>i)&1; ui=(U>>i)&1
        for (c,bl,bu),low in states.items():
            for xi in (0,1):
                total=xi+ai+c
                yi=total&1; c2=total>>1
                if d and (abs(d)==(1<<i)) and xi!=(0 if d>0 else 1): continue
                if e and (abs(e)==(1<<i)) and yi!=(0 if e>0 else 1): continue
                bl2=int(xi-li-bl<0)
                bu2=int(ui-xi-bu<0)
                key=(c2,bl2,bu2)
                if key not in nxt: nxt[key]=low|(xi<<i)
        states=nxt
        if not states: return None
    # For negative a, final carry is not required to be zero: finite-width
    # two's complement arithmetic correctly yields (u+a) mod N.
    for (c,bl,bu),u in states.items():
        if bl==0 and bu==0:
            v=u+d; w=u+a; z=w+e
            if not (0<=u<N and 0<=v<N and 0<=w<N and 0<=z<N): continue
            if d and v!=(u^abs(d)): continue
            if e and z!=(w^abs(e)): continue
            return u
    return None

def brute(p,a,d,e):
    N=1<<p
    for u in range(N):
        v=u+d; w=u+a; z=w+e
        if all(0<=x<N for x in (v,w,z)) and (not d or v==(u^abs(d))) and (not e or z==(w^abs(e))): return u
    return None

def valid_events(p):
    return [0]+[s*(1<<i) for i in range(p) for s in (1,-1)]

def collision_by_dp(p,q1,q2):
    N=1<<p; E=valid_events(p)
    for a in range(0,N,q1):
        for d in E:
            for e in E:
                if a==0 and d==e: continue
                b=a+e-d
                if b%q2: continue
                u=witness(p,a,d,e)
                if u is not None:
                    return (u,u+d,u+a,u+a+e,a,b,d,e)
    return None

def collision_by_hash(p,q1,q2):
    N=1<<p; seen={}
    for u in range(N):
        for d in valid_events(p):
            v=u+d
            if not (0<=v<N and (not d or v==(u^abs(d)))):continue
            key=(u%q1,v%q2)
            if key in seen:return (*seen[key],u,v)
            seen[key]=(u,v)
    return None

def main():
    data={"schema":"PREFIX881_R6_EXACT_DP_V1","models":[],"boundary_examples":[]}
    for p in (1,2,3,4,5,6):
        E=valid_events(p); n=0; matches=0; found=0
        N=1<<p
        for a in range(-(N-1),N):
            for d in E:
                for e in E:
                    n+=1
                    x=witness(p,a,d,e); y=brute(p,a,d,e)
                    if (x is None)!=(y is None):raise AssertionError((p,a,d,e,x,y))
                    if x is not None:
                        assert x+d==(x^abs(d)) if d else True
                        assert x+a+e==((x+a)^abs(e)) if e else True
                        found+=1
                    matches+=1
        data['models'].append({'p':p,'a_delta_deltaPrime_cases':n,'feasible_cases':found,'DP_brute_agree':matches})
    for p,Q in ((4,31),(5,63),(6,15)):
        tested=collisions=no_collisions=0
        for q1 in range(1,Q+1,2):
            for q2 in range(1,Q+1,2):
                b=collision_by_hash(p,q1,q2)
                c=collision_by_dp(p,q1,q2)
                if (b is None)!=(c is None):raise AssertionError((p,q1,q2,b,c))
                tested+=1
                if b: collisions+=1
                else: no_collisions+=1
        data.setdefault('port_pair_checks',[]).append({'p':p,'Q':Q,'pairs_tested':tested,'colliding':collisions,'injective':no_collisions})
    # A near-boundary signed-gap witness excluded by PREFIX-875's conservative sufficient range
    p=32; N=1<<p; q1=(1<<19)-1; q2=q1-2; k=l=8192
    a=k*q1;b=l*q2; d=a-b; e=0
    x=witness(p,a,d,e)
    assert x is not None
    assert a+abs(d)+2>N
    assert (x%q1)==((x+a)%q1) and ((x+d)%q2)==((x+a+e)%q2)
    data['boundary_examples'].append({'p':p,'q1':q1,'q2':q2,'k':k,'l':l,'a':a,'b':b,'d':d,'e':e,'witness':{'X':[x,x+d],'Y':[x+a,x+a+e]},'previous_conservative_range_holds':False})
    print(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
