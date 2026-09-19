"""Exact extraction of the tested three-region slice codec.
Not a codec for arbitrary X6 states. Source: user-visible verify_lines.py,
SHA256 b190bf460e87c855c2e4f5b4c61b75473c0422afad70bd2b7deb1663d6ee54e7.
The three function bodies below are unchanged; the public wire API wraps them.
"""
from __future__ import annotations
Point = tuple[int, int]
Code = tuple[int, int, int, int, int, int]


def encode(p: Point) -> Code:
    if len(p) != 2 or any(type(x) is not int for x in p):
        raise ValueError('exactly two integer audit coordinates required')
    m,n=p
    if m <= 0 and n >= m:
        return (0,n-m+1,1-m,0,0,0)
    if n <= 0 and m >= n+1:
        return (m-n,0,1-n,0,0,0)
    if m >= 1 and n >= 1:
        return (m,n,0,0,0,0)
    raise AssertionError('region partition incomplete')


def decode(q: Code) -> Point:
    if not isinstance(q,tuple) or len(q)!=6 or any(type(x) is not int or x<0 for x in q):
        raise ValueError('address must contain six nonnegative integers')
    a,b,c,*rest=q
    if any(rest) or (a==0)+(b==0)+(c==0)!=1:
        raise ValueError('not a valid code for this registered slice')
    if a==0: return (1-c,b-c)
    if b==0: return (a+1-c,1-c)
    return (a,b)


def code_step(q: Code, label: str) -> Code:
    """Direct local transition table, NOT implemented using decode/move/encode."""
    decode(q)
    a,b,c=q[:3]
    if label=='E1+':
        if a:
            out=(a+1,b,c)
        elif b==1:
            out=(1,0,c)
        elif c==1:
            out=(1,b-1,0)
        else:
            out=(0,b-1,c-1)
    elif label=='E1-':
        if a==0: out=(0,b+1,c+1)
        elif b==0: out=(a-1,0,c) if a>1 else (0,1,c)
        else: out=(a-1,b,0) if a>1 else (0,b+1,1)
    elif label=='E2+':
        if c==0 or a==0: out=(a,b+1,c)
        elif c==1: out=(a,1,0)
        elif a==1: out=(0,1,c-1)
        else: out=(a-1,0,c-1)
    elif label=='E2-':
        if b==0: out=(a+1,0,c+1)
        elif a==0: out=(0,b-1,c) if b>1 else (1,0,c+1)
        else: out=(a,b-1,0) if b>1 else (a,0,1)
    else: raise ValueError('unknown native move')
    answer=tuple(out)+(0,0,0)
    decode(answer)
    return answer
