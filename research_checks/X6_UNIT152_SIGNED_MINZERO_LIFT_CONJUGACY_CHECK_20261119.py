#!/usr/bin/env python3
"""Exact source-independent finite check of native signed X6/min-zero lift update.
Mathematical interpretation pinned to Enterprise Math X6 2026-09-05; no frozen source mutation.
"""
import hashlib
import itertools
import json
from collections import Counter

D=(1,1,1,0,0,0)
STEPS=tuple(tuple(s if i==j else 0 for i in range(6)) for j in range(6) for s in (-1,1))

def ensure(p,msg):
    if not p: raise RuntimeError(msg)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def lift(z):
    h=min(z[:3]);w=tuple(z[i]-h for i in range(3))
    return (w,h,tuple(z[3:]))
def unlift(state):
    w,h,tail=state
    return tuple(x+h for x in w)+tail

def skew_step(state,j,s):
    w,h,tail=state
    if j<3:
        raw=list(w);raw[j]+=s
        t=min(raw)
        return (tuple(x-t for x in raw),h+t,tail)
    tail=list(tail);tail[j-3]+=s
    return (w,h,tuple(tail))

def count_quotient_returns(L):
    # 3-coordinate signed alphabet only; a quotient class is represented by min-zero.
    native=Counter({(0,0,0):1}); observed=Counter({(0,0,0):1})
    result=[]
    for n in range(L+1):
        native_zero=native.get((0,0,0),0)
        obs_zero=observed.get((0,0,0),0)
        # independent observed fiber tally from raw native endpoints
        fiber=sum(v for z,v in native.items() if len(set(z))==1)
        ensure(obs_zero==fiber,f"fiber pushforward mismatch {n}")
        result.append({"length":n,"native_zero":native_zero,"observed_zero":obs_zero,"hidden":obs_zero-native_zero,"native_support":len(native),"quotient_support":len(observed)})
        if n==L: break
        new=Counter();newobs=Counter()
        for z,v in native.items():
            for j in range(3):
                for s in (-1,1):
                    u=list(z);u[j]+=s;new[tuple(u)]+=v
        for w,v in observed.items():
            for j in range(3):
                for s in (-1,1):
                    u=list(w);u[j]+=s;m=min(u)
                    newobs[tuple(x-m for x in u)]+=v
        native,observed=new,newobs
    return result


def main():
    states=0;transitions=0; t_hist=Counter()
    for z in itertools.product(range(-2,3),repeat=6):
        state=lift(z)
        ensure(unlift(state)==z,'bad inverse')
        ensure(min(state[0])==0,'bad canonical state')
        states+=1
        for j in range(6):
            for s in (-1,1):
                step=STEPS[2*j+(0 if s==-1 else 1)]
                actual=lift(add(z,step))
                upd=skew_step(state,j,s)
                ensure(actual==upd, f'bad skew: {z} {j} {s}')
                ensure(unlift(upd)==add(z,step),'bad native reconstruction')
                if j<3:
                    t_hist[str(upd[1]-state[1])]+=1
                transitions+=1
    ensure(states==15625 and transitions==187500, 'domain count')
    # Inductively, each labelled signed word keeps exact native endpoint, not only observer class.
    for L in range(7):
        for word in itertools.product(range(6),repeat=L):
            z=(0,)*6;sk=lift(z)
            for idx in word:
                j=idx//2;s=(-1,1)[idx%2]
                z=add(z,STEPS[idx]);sk=skew_step(sk,j,s)
            ensure(unlift(sk)==z and lift(z)==sk,'path prefix mismatch')
    observed=count_quotient_returns(8)
    ensure(observed[3]['native_zero']==0 and observed[3]['observed_zero']==12,'L3 mismatch')
    ensure(observed[6]['hidden']==180,'L6 hidden mismatch')
    # finite observer memory modulo q is not sufficient for unbounded native invariants
    for q in range(1,13):
        z0=(0,0,0,0,0,0);z1=(q,q,q,0,0,0)
        a=lift(z0);b=lift(z1)
        ensure(a[0]==b[0] and a[2]==b[2] and a[1]%q==b[1]%q,'finite memory witness')
        ensure(sum(x*x for x in z0)!=sum(x*x for x in z1),'native norm collision')
    result={
        "schema":"ENTERPRISE_MATH_X6_UNIT152_SIGNED_MINZERO_LIFT_CERT_V1",
        "status":"EXACT_FINITE_EXECUTED_AUTHOR_UNREVIEWED_NOT_ADMITTED",
        "frozen_science_commit":"59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "source_math":"native signed X6 torsor Z6; three-axis D=(1,1,1,0,0,0) derived observer",
        "state_cube":"[-2,2]^6", "state_count":states,"labelled_transitions":transitions,
        "skew_depth_delta_histogram":dict(sorted(t_hist.items())),
        "labelled_path_words_length_at_most_6":sum(6**i for i in range(7)),
        "observed_return_up_to_8_three_axis":observed,
        "finite_depth_modulo_q_witnesses":12,
        "original_R063_six_file_benchmark_executed":False,
        "native_source_module_imported":False,
        "checks_always_on_under_optimized_python":True,
    }
    print(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
