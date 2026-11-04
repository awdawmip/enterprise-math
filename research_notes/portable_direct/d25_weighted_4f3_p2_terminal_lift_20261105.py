"""Exact D25 weighted reversed 4F3 p^2 source checker. Author-side, not H0/B0."""
import json
from pathlib import Path

def primes(limit=10000):
    table=bytearray([1])*(limit+1)
    table[0:2]=b'\x00\x00'
    for a in range(2,int(limit**0.5)+1):
        if table[a]:
            table[a*a::a]=b'\x00'*((limit-a*a)//a+1)
    return [p for p in range(7,limit+1) if table[p] and p%6==1]

def check(p):
    assert p>=7 and p%6==1
    n=(p-1)//6
    q=p*p
    g=[1]
    for k in range(n-1):
        numerator=2*(k+1)*(6*k+5)*(6*k+7)
        denominator=9*(2*k+3)**3
        assert denominator%p != 0
        g.append(g[-1]*numerator*pow(denominator,-1,q)%q)
    h=[(3*k+2)*v%q for k,v in enumerate(g)]
    for k in range(1,n):
        scaled=9*(3*k-1)*k*(2*k+1)**3*h[k] - 2*(3*k+2)*k*k*(6*k-1)*(6*k+1)*h[k-1]
        assert scaled%q == 0, (p,k,scaled%q)
    terminal= -2*(3*n+2)*n*n*(6*n-1)*(6*n+1)*h[-1]*pow(72,-1,q)%q
    predicted= -p*g[-1]*pow(288,-1,q)%q
    assert terminal==predicted, (p,terminal,predicted)
    assert terminal%p==0 and terminal!=0
    terminal_half=terminal*pow(2,-n,q)%q
    assert terminal_half!=0 and terminal_half%p==0
    observer=sum(v*pow(2,-k,q) for k,v in enumerate(h))%q
    return dict(p=p,n=n,terminal_mod_p2=terminal,terminal_div_p_mod_p=(terminal//p)%p,
                terminal_at_half_mod_p2=terminal_half,g_last_mod_p2=g[-1],
                weighted_observer_mod_p2=observer)

def main():
    data=[check(p) for p in primes()]
    result={"schema":"D25_WEIGHTED_REVERSED_4F3_P2_LIFT_CHECK_V1",
            "checked":len(data),"failures":0,
            "range":"p=6n+1, 7<=p<=10000",
            "anchors":[a for a in data if a["p"] in (7,13,19,139,373)],
            "note":"Exact integer checks; NOT native H0/B0. Mathematics proven by finite recurrence."}
    print(json.dumps(result,indent=2))
if __name__=="__main__":
    main()
