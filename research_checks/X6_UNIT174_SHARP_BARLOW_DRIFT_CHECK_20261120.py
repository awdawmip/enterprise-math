#!/usr/bin/env python3
"""Independent integer checks for frozen Barlow drift bound and exact sharpness.
No repository/source imports; reconstructs the documented signs and index semantics.
"""
from itertools import product
import hashlib, json, sys


def prefix_imbalance(pattern, k):
    n=len(pattern)
    if k>=0:
        return sum(pattern[i%n] for i in range(k))
    return -sum(pattern[i%n] for i in range(k,0))


def frozen_algorithm(pattern):
    n=len(pattern)
    d=abs(sum(pattern))
    vals=[0]
    for k in range(1,n):
        vals.append(abs(n*abs(prefix_imbalance(pattern,k))-d*k))
        vals.append(abs(n*abs(prefix_imbalance(pattern,-k))-d*k))
    return max(vals)


def one_signed_prefix_formula(pattern):
    n=len(pattern)
    d=sum(pattern)
    p=0
    bound=0
    for k in range(1,n):
        p+=pattern[k-1]
        bound=max(bound,abs(n*p-d*k))
    return bound


def long_imbalance(pattern,k):
    n=len(pattern)
    q,r=divmod(abs(k),n)
    if k>=0:
        return q*sum(pattern)+sum(pattern[:r])
    suffix=sum(pattern[-r:]) if r else 0
    return -(q*sum(pattern)+suffix)


def error(pattern,k):
    return abs(len(pattern)*abs(long_imbalance(pattern,k))-abs(sum(pattern))*abs(k))


def main():
    total=0; short_sites=0; far_sites=0; zeros=0; nonzero=0; failures=[]; sharp_witnesses=[]
    for n in range(1,11):
        for p in product((-1,1),repeat=n):
            total+=1
            a=frozen_algorithm(p)
            b=one_signed_prefix_formula(p)
            if a!=b: failures.append(["old_vs_sharp",p,a,b])
            if b==0: zeros+=1
            else: nonzero+=1
            for k in range(-4*n,4*n+1):
                short_sites+=1
                if error(p,k)>b: failures.append(["finite",p,k,error(p,k),b])
            for k in (-1_000_001*n,-1_000_000*n,-999_999*n-3,-n*n-1,n*n+1,999_999*n+3,1_000_000*n,1_000_001*n):
                far_sites+=1
                if error(p,k)>b: failures.append(["large",p,k,error(p,k),b])
            # Sharpness must be attained by one k in [-4L,4L] or a large compatible drift phase.
            candidates=list(range(-4*n,4*n+1))
            candidates+= [j*n+r for j in range(10) for r in range(n)]
            candidates+= [-j*n-r for j in range(10) for r in range(n)]
            best=max((error(p,k),k) for k in candidates)
            if best[0]!=b: failures.append(["sharp_attain",p,b,best])
            if p==(1,1,-1,-1,-1): sharp_witnesses.append({"pattern":p,"bound":b,"k_minus_3":error(p,-3),"k_47":error(p,47)})
    out={"schema":"X6_UNIT174_BARLOW_DRIFT_EXACT_CERTIFICATE_V1", "task_id":"RS-X6-LEGACY-PLANE-RECONCILIATION","historical_pin":"fd2bcff10ca6e147348b6c1236027fc0d2877df3","claim":"min_C_for_all_signed_layers_equals_max_{0<=r<L}|L*P_r-D*r|","period_max":10,"period_words_tested":total,"checked_short_signed_layers":short_sites,"checked_far_signed_layers":far_sites,"zero_optimal_bound_patterns":zeros,"positive_optimal_bound_patterns":nonzero,"violations":len(failures),"failure_examples":failures[:5],"specific_witnesses":sharp_witnesses,"run_mode": "independent_python_integer", "frozen_source_directly_executed":False,"native_r063_benchmark_rerun":False,"result":"PASS" if not failures else "FAIL"}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))
    if failures: sys.exit(1)
if __name__=='__main__':main()
