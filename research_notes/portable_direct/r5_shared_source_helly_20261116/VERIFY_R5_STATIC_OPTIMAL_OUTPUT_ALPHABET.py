#!/usr/bin/env python3
"""Exact static choose-one source-label output alphabet for R5 cyclic graph."""
import json

def q(k,u):
    return sum((u>>i&1)*(u>>((i+1)%k)&1) for i in range(k))

def maximal(k,u):
    # A 0 can be changed to 1 without changing q exactly when both neighbors are 0.
    return all((u>>i&1) or (u>>((i-1)%k)&1) or (u>>((i+1)%k)&1)
               for i in range(k))

def extend(k,u):
    while True:
        options=[i for i in range(k) if not(u>>i&1) and q(k,u|1<<i)==q(k,u)]
        if not options:return u
        u|=1<<options[0]

def run():
    cases=0
    maximal_pair_checks=0
    counts=[]
    prev=(1,3,7)
    for k in range(3,13):
        maxima=[u for u in range(1<<k) if maximal(k,u)]
        # Each mask has a canonical source-optimal completion in its own q fiber.
        for u in range(1<<k):
            w=extend(k,u)
            assert maximal(k,w) and (u&w)==u and q(k,w)==q(k,u)
            cases+=1
        # Distinct maximal masks cannot share any one individually optimal library.
        for i,u in enumerate(maxima):
            for v in maxima[i+1:]:
                assert not(q(k,u|v)==q(k,u)==q(k,v))
                maximal_pair_checks+=1
        n=len(maxima)
        if k==3: assert n==7
        elif k==4: assert n==11
        elif k==5: assert n==21
        else: assert n==sum(counts[-3:])
        counts.append(n)
    return dict(status="PASS_R5_STATIC_OPTIMUM_ALPHABET_TRIBONACCI",
                frozen_science="435e77af0d180eac32bd1f9c4c464bc4010b7551",
                k_range=[3,12], output_state_counts=counts,
                masks_exhaustively_extended=cases, maxima_incompatibility_pairs=maximal_pair_checks,
                arithmetic="exact integer bitsets", independent_review="NOT_REVIEWED")

if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
