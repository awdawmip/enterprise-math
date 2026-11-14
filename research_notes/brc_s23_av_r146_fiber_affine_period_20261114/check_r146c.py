#!/usr/bin/env python3
"""R146C endpoint-divisor mass-step law with exact integer arithmetic."""
import json
from math import gcd

def totients(n):
    p=list(range(n+1))
    for q in range(2,n+1):
        if p[q]==q:
            for x in range(q,n+1,q): p[x]-=p[x]//q
    return p

def divisor_mass(n,m,phi):
    return sum(phi[q] for q in range(2,m+1) if n%q==0)

def mass(L,m,phi):
    return (m+1)*L + m*(m-1)//2 - sum(phi[q]*((L+m)//q-(L-1)//q-1) for q in range(2,m+1))

def main():
    phi=totients(60)
    count=0; decreases=[]; mins={}
    for m in range(1,51):
        minstep=(10000,None)
        for L in range(1,501):
            direct=mass(L+1,m,phi)-mass(L,m,phi)
            endpoint=(m+1)+divisor_mass(L,m,phi)-divisor_mass(L+m+1,m,phi)
            assert direct==endpoint, (m,L,direct,endpoint)
            count+=1
            if direct<minstep[0]: minstep=(direct,L)
            if direct<0 and len(decreases)<12: decreases.append([m,L,direct])
        mins[m]=minstep
    result={"m_range":[1,50],"L_range":[1,500],"exact_checks":count,"first_negative_m":next((m for m in mins if mins[m][0]<0),None),"selected_negative_examples":decreases,"min_step_by_m_1_to_10":{str(m):[mins[m][0],mins[m][1]] for m in range(1,11)},"signature":"R146C_ENDPOINT_DIVISOR_FLOW_PASS"}
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
