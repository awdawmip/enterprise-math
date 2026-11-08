#!/usr/bin/env python3
"""Exact rational witnesses that m finite carry symbols do not fix the next symbol."""
from VERIFY_EDGE_PREFIX import alpha_interval

def symbols(N):
    lo,hi=alpha_interval(160)
    out=[0]*(N+1)
    for k in range(1,N+1):
        a=(79*k*lo).__floor__()-79*(k*lo).__floor__()
        b=(79*k*hi).__floor__()-79*(k*hi).__floor__()
        assert a==b
        out[k]=a
    return out

def witness(m,vals):
    seen={}
    for k in range(m,len(vals)-1):
        w=tuple(vals[k-m+1:k+1]); nxt=vals[k+1]
        if w in seen:
            old,old_nxt=seen[w]
            if old_nxt!=nxt:
                return old,k,old_nxt,nxt,w
        else:
            seen[w]=(k,nxt)
    raise AssertionError(('no_witness_in_prefix',m,len(vals)-1))

if __name__ == '__main__':
    vals=symbols(50000)
    for m in (1,2,4,8,16,32,64):
        k1,k2,n1,n2,word=witness(m,vals)
        assert k1>=m and k2>=m and n1!=n2
        print('PASS_NO_FINITE_MEMORY', 'm=',m,'k1=',k1,'k2=',k2,'next=',(n1,n2),'last_state=',word[-1])
