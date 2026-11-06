#!/usr/bin/env python3
"""Independent p^4 finite-difference check of p=5113 third labelled-source jet."""
def direct_sum_p4(p,t):
    assert p==5113
    m=(p-1)//6; a,b,c=2*m,3*m,4*m; q=p**4
    a+=p*t; c+=p*t
    n_a=n_b=n_c=1
    w=1
    total=0
    invneg2=pow(-2,-1,q)
    for j in range(b+1):
        total=(total+(6*j+1)*w*n_a*n_b*n_c)%q
        if j==b: break
        inverse=pow(j+1,-1,q)
        n_a=n_a*(a-j)*inverse%q
        n_b=n_b*(b-j)*inverse%q
        n_c=n_c*(c-j)*inverse%q
        w=w*invneg2%q
    return total
if __name__=="__main__":
    p=5113; q=p**4
    v=[direct_sum_p4(p,t) for t in range(4)]
    assert v==[610854945333422,135964409472485,269664176976589,628728155215035]
    diff=(v[3]-3*v[2]+3*v[1]-v[0])%q
    assert diff==300218278356662 and diff//p**3==2246
    print("values_t0_3",v)
    print("third_difference",diff,"normalized",diff//p**3,"PASS")
