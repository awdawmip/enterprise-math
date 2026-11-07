#!/usr/bin/env python3
"""Exact signed Kronecker polynomial arithmetic for R468, with published R462 mathematical formulas.
Not a new mathematical assumption: coefficientwise equality with integer convolution is used.
"""
import importlib.util
from ctypes import CDLL, c_size_t, c_void_p, c_int, byref, create_string_buffer
from pathlib import Path
_accelerator=Path(__file__).resolve().parent/'R468_GMP_ACCELERATOR.so'
_lib=CDLL(str(_accelerator)) if _accelerator.exists() else None
if _lib is not None:
    _func=_lib.multiply_be
    _func.argtypes=(c_void_p,c_size_t,c_void_p,c_size_t,c_void_p,c_size_t,c_void_p)
    _func.restype=c_int

def exact_bigint_multiply(a,b):
    if a==0 or b==0:return 0
    if _lib is None:return a*b
    sign=-1 if (a<0)!=(b<0) else 1
    a=abs(a);b=abs(b)
    ba=a.to_bytes((a.bit_length()+7)//8,'big'); bb=b.to_bytes((b.bit_length()+7)//8,'big')
    out=create_string_buffer(len(ba)+len(bb)); nout=c_size_t()
    code=_func(ba,len(ba),bb,len(bb),out,len(out),byref(nout))
    if code:raise ArithmeticError('GMP output buffer exceeded')
    return sign*int.from_bytes(out.raw[:nout.value],'big')
from pathlib import Path
SRC = Path(__file__).resolve().parent/'R462_VERIFY_FROZEN_KERNEL.py'
spec=importlib.util.spec_from_file_location('r462_frozen',SRC)
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
slow=core.mul

def mul(a,b):
    if not a or not b:return []
    if len(a)*len(b)<1024:return slow(a,b)
    # Balanced-digit Kronecker substitution for integer polynomials with signed coefficients.
    bound=sum(map(abs,a))*sum(map(abs,b))
    width=bound.bit_length()+2
    mask=(1<<width)-1
    half=1<<(width-1)
    def encode(poly):
        z=0
        for c in reversed(poly):z=(z<<width)+c
        return z
    packed=exact_bigint_multiply(encode(a),encode(b))
    out=[]
    for _ in range(len(a)+len(b)-1):
        digit=packed & mask
        if digit>=half:digit-=1<<width
        out.append(digit)
        packed=(packed-digit)>>width
    if packed:raise ArithmeticError('nonzero tail')
    return out

core.mul=mul

def balanced_prod(items):
    items=list(items)
    if not items:return [1]
    while len(items)>1:
        nxt=[]
        for i in range(0,len(items)-1,2):nxt.append(mul(items[i],items[i+1]))
        if len(items)&1:nxt.append(items[-1])
        items=nxt
    return items[0]

def B_fast(s,k0,F):
    if s<2:return [0]
    m=(s-1)//2
    E=balanced_prod([[2*(k0+1-s//2+j),2] for j in range(s)])
    O=balanced_prod([[2*k0+2*j+1,2] for j in range(s//2+1)])
    suffix=[None]*(m+1);suffix[m]=[1]
    for q in range(m-1,-1,-1):
        suffix[q]=mul([2*k0-(2*q+1),2],suffix[q+1])
    prefix=[None]*(m+1);prefix[0]=[1]
    for q in range(m):
        prefix[q+1]=mul(prefix[q],[k0+1-q,1])
    from math import comb,factorial
    R=core.add(*( [comb(s-1,2*q)*(2**q)*v for v in mul(suffix[q],prefix[q])] for q in range(m+1) ))
    assert F%factorial(2*s)==0
    return [v*(F//factorial(2*s)) for v in balanced_prod([E,O,R])]

core.B=B_fast
if __name__=='__main__':
 import random
 rng=random.Random(20261102)
 for n in range(1,9):
  for _ in range(50):
   a=[rng.randrange(-10000,10001) for i in range(n+3)]
   b=[rng.randrange(-2000,2001) for i in range(5+n)]
   got=mul(a,b);ref=slow(a,b)
   assert got==ref
 for _ in range(100):
  a=rng.getrandbits(rng.randrange(1,2000))*rng.choice([-1,1]);b=rng.getrandbits(rng.randrange(1,2000))*rng.choice([-1,1])
  assert exact_bigint_multiply(a,b)==a*b
 print('R468_GMP_EXACT_INTEGER_TEST_PASS',flush=True)
 print('R468_SIGNED_KRONECKER_SMALL_EXACT_PASS',flush=True)
 got=core.s_certificate(175,detail=False)
 assert got['sha256']=='5a68b3d2ced114ee7744e5a75b8553717314a3d0ea1b5b497b0739ba09847239',got
 print('R468_S175_PUBLISHED_REGRESSION_PASS',got['sha256'],flush=True)
