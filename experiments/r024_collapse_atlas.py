#!/usr/bin/env python3
"""R024 exact Collapse Atlas runtime candidate.

Semantics are frozen by EnterpriseMath/Arithmetic/IntegerRoot.lean:
  collapse p n = k^p iff k^p <= n < (k+1)^p.
All theorem-critical root/boundary decisions are integer exact.
"""
from __future__ import annotations

import argparse, bisect, dataclasses, hashlib, json, math, struct
from array import array
from dataclasses import dataclass

U64_MAX=(1<<64)-1


def exact_nth_root(n:int,p:int)->int:
    if p<=0 or n<0: raise ValueError
    if p==1 or n<2: return n
    if p==2: return math.isqrt(n)
    x=1<<((n.bit_length()+p-1)//p)
    while True:
        y=((p-1)*x+n//(x**(p-1)))//p
        if y>=x: break
        x=y
    while (x+1)**p<=n: x+=1
    while x**p>n: x-=1
    return x


def locate_basin(p:int,n:int)->tuple[int,int,int]:
    k=exact_nth_root(n,p)
    return k,k**p,(k+1)**p


def collapse(p:int,n:int)->int:
    return locate_basin(p,n)[1]


def initial_differences(p:int)->list[int]:
    row=[k**p for k in range(p+1)]; out=[row[0]]
    while len(row)>1:
        row=[b-a for a,b in zip(row,row[1:])]; out.append(row[0])
    return out


def boundaries_fd(p:int,n_hot:int)->array:
    d=initial_differences(p); out=array('Q')
    while d[0]<=n_hot:
        if d[0]>U64_MAX: raise OverflowError
        out.append(d[0])
        for j in range(p): d[j]+=d[j+1]
    return out


@dataclass
class BoundaryAtlas:
    p:int; n_hot:int; anchors:array
    @classmethod
    def build(cls,p:int,n_hot:int)->'BoundaryAtlas': return cls(p,n_hot,boundaries_fd(p,n_hot))
    @property
    def packed_bytes(self)->int: return len(self.anchors)*8
    def locate(self,n:int)->tuple[int,int,int]:
        if n<0: raise ValueError
        if n>self.n_hot: return locate_basin(self.p,n)
        k=bisect.bisect_right(self.anchors,n)-1
        L=int(self.anchors[k]); U=int(self.anchors[k+1]) if k+1<len(self.anchors) else (k+1)**self.p
        return (k,L,U) if L<=n<U else locate_basin(self.p,n)


@dataclass
class DenseTable:
    p:int; n_hot:int; variant:str; data:bytes; entry_bytes:int
    @classmethod
    def build(cls,p:int,n_hot:int,variant:str)->'DenseTable':
        if variant not in {'collapse_u64','root_u32','root_u32_next_u64'}: raise ValueError
        b=bytearray(); k=0; L=0; U=1
        for n in range(n_hot+1):
            while n>=U: k+=1; L=k**p; U=(k+1)**p
            if variant=='collapse_u64': b+=struct.pack('<Q',L)
            elif variant=='root_u32': b+=struct.pack('<I',k)
            else: b+=struct.pack('<IQ',k,U)
        eb={'collapse_u64':8,'root_u32':4,'root_u32_next_u64':12}[variant]
        return cls(p,n_hot,variant,bytes(b),eb)
    @property
    def packed_bytes(self)->int: return len(self.data)
    def locate(self,n:int)->tuple[int,int,int]:
        if n>self.n_hot: return locate_basin(self.p,n)
        off=n*self.entry_bytes
        if self.variant=='collapse_u64': L=struct.unpack_from('<Q',self.data,off)[0]; k=exact_nth_root(L,self.p); U=(k+1)**self.p
        elif self.variant=='root_u32': k=struct.unpack_from('<I',self.data,off)[0]; L=k**self.p; U=(k+1)**self.p
        else: k,U=struct.unpack_from('<IQ',self.data,off); L=k**self.p
        return int(k),int(L),int(U)


@dataclass
class BasinCursor:
    p:int; n:int; k:int; L:int; U:int; root_calls:int=0; boundary_updates:int=0
    @classmethod
    def from_n(cls,p:int,n:int)->'BasinCursor':
        k,L,U=locate_basin(p,n); return cls(p,n,k,L,U,1,0)
    @property
    def packed_bytes(self)->int: return 40
    @property
    def distance_to_boundary(self)->int: return self.U-self.n
    def advance(self,delta:int,crossing_threshold:int=8)->'BasinCursor':
        nn=self.n+delta
        if nn<0: raise ValueError
        if self.L<=nn<self.U: self.n=nn; return self
        if abs(delta)>crossing_threshold*max(1,self.U-self.L):
            self.k,self.L,self.U=locate_basin(self.p,nn); self.root_calls+=1; self.n=nn; return self
        steps=0
        if delta>=0:
            while nn>=self.U and steps<crossing_threshold:
                self.k+=1; self.L=self.U; self.U=(self.k+1)**self.p; self.boundary_updates+=1; steps+=1
        else:
            while nn<self.L and self.k>0 and steps<crossing_threshold:
                self.U=self.L; self.k-=1; self.L=self.k**self.p; self.boundary_updates+=1; steps+=1
        if not self.L<=nn<self.U: self.k,self.L,self.U=locate_basin(self.p,nn); self.root_calls+=1
        self.n=nn; return self


@dataclass(frozen=True)
class IntInterval:
    lo:int; hi:int
    def __post_init__(self):
        if self.lo<0 or self.hi<self.lo: raise ValueError
    @property
    def width(self)->int: return self.hi-self.lo
    @property
    def packed_bytes(self)->int: return 16
    def translate(self,c:int)->'IntInterval': return IntInterval(self.lo+c,self.hi+c)


@dataclass(frozen=True)
class RootSupportInterval:
    k_lo:int; k_hi:int
    @property
    def branch_width(self)->int: return 0 if self.k_hi<self.k_lo else self.k_hi-self.k_lo+1
    @property
    def packed_bytes(self)->int: return 16


def floor_quotient_fibre(q:int,d:int)->IntInterval: return IntInterval(q*d,(q+1)*d)
def power_basin_interval(p:int,k:int)->IntInterval: return IntInterval(k**p,(k+1)**p)
def collapsed_support(p:int,iv:IntInterval,locator=None)->RootSupportInterval:
    if iv.width==0: return RootSupportInterval(0,-1)
    f=locator or (lambda n:locate_basin(p,n))
    return RootSupportInterval(f(iv.lo)[0],f(iv.hi-1)[0])


@dataclass(frozen=True)
class FutureDescriptor:
    one_step_deltas:tuple[int,...]; suffixes:tuple[tuple[int,...],...]=()
    @property
    def diagnostic_hash64(self)->int:
        raw=json.dumps(dataclasses.asdict(self),sort_keys=True,separators=(',',':')).encode()
        return int.from_bytes(hashlib.blake2b(raw,digest_size=8).digest(),'little')

@dataclass(frozen=True)
class CompiledFuture: descriptor:FutureDescriptor; version:int
class FutureRegistry:
    def __init__(self): self._v={}; self._next=1
    def compile(self,d:FutureDescriptor)->CompiledFuture:
        if d not in self._v: self._v[d]=self._next; self._next+=1
        return CompiledFuture(d,self._v[d])

@dataclass(frozen=True)
class HazardSignature:
    future_version:int; one_step_bits:int; suffix_bits:int; one_step_count:int; suffix_count:int


def no_split_after(p:int,iv:IntInterval,d:int,locator=None)->bool: return collapsed_support(p,iv.translate(d),locator).branch_width<=1
def no_split_suffix(p:int,iv:IntInterval,ds:tuple[int,...],locator=None)->bool:
    cur=iv
    for d in ds:
        cur=cur.translate(d)
        if collapsed_support(p,cur,locator).branch_width>1: return False
    return True

def hazard_signature(p:int,iv:IntInterval,f:CompiledFuture,locator=None)->HazardSignature:
    one=sum((1<<i) for i,d in enumerate(f.descriptor.one_step_deltas) if no_split_after(p,iv,d,locator))
    suf=sum((1<<i) for i,ds in enumerate(f.descriptor.suffixes) if no_split_suffix(p,iv,ds,locator))
    return HazardSignature(f.version,one,suf,len(f.descriptor.one_step_deltas),len(f.descriptor.suffixes))

def hazard_query(sig:HazardSignature,f:CompiledFuture,kind:str,i:int)->bool:
    if sig.future_version!=f.version: raise ValueError('STALE_HAZARD_SIGNATURE')
    bits,count=(sig.one_step_bits,sig.one_step_count) if kind=='one_step' else (sig.suffix_bits,sig.suffix_count)
    if i>=count: raise IndexError
    return bool((bits>>i)&1)


class BucketHotCache:
    """Coarse bucket -> exact verified basin; all misses use exact root fallback."""
    def __init__(self,n_hot:int,p_values,capacity:int=4096):
        self.capacity=capacity; self.entries={}; self.hits=self.misses=self.root_calls=0
        self.bucket_sizes={p:max(1,n_hot//max(1,exact_nth_root(n_hot,p)+1)) for p in p_values}
    @property
    def packed_bytes(self)->int: return len(self.entries)*40+len(self.bucket_sizes)*16
    def locate(self,p:int,n:int)->tuple[int,int,int]:
        bs=self.bucket_sizes.get(p)
        if bs is None: self.misses+=1; self.root_calls+=1; return locate_basin(p,n)
        key=(p,n//bs); cand=self.entries.get(key)
        if cand is not None:
            ep,k,L,U=cand
            if ep==p and L<=n<U: self.hits+=1; return k,L,U
        self.misses+=1; self.root_calls+=1; k,L,U=locate_basin(p,n)
        if len(self.entries)>=self.capacity and key not in self.entries: self.entries.pop(next(iter(self.entries)))
        self.entries[key]=(p,k,L,U); return k,L,U


def self_check()->dict:
    checks=0
    for p in range(2,17):
        for n in [0,1,2,3,7,15,16,17,10**9,10**12,10**18,U64_MAX]:
            k,L,U=locate_basin(p,n); assert L<=n<U and L==k**p and U==(k+1)**p; checks+=1
    for p,kmax in [(2,5000),(3,2000),(4,500),(5,100)]:
        a=boundaries_fd(p,kmax**p); assert list(a)==[k**p for k in range(kmax+1)]; checks+=len(a)
    for p,nh in [(3,10**12),(4,10**15),(5,10**18)]:
        a=BoundaryAtlas.build(p,nh)
        for k,L0 in enumerate(a.anchors):
            L=int(L0); assert a.locate(L)[:2]==(k,L); checks+=1
    cur=BasinCursor.from_n(3,100**3+1); n=cur.n
    for d in [10,1000,50000,10**13,7]: n+=d; cur.advance(d); assert cur.L<=n<cur.U
    r=FutureRegistry(); f1=r.compile(FutureDescriptor((1,),((1,1,1),))); f2=r.compile(FutureDescriptor((2,),((1,1,1),)))
    sig=hazard_signature(2,IntInterval(1020,1022),f1); assert hazard_query(sig,f1,'one_step',0) and not hazard_query(sig,f1,'suffix',0)
    try: hazard_query(sig,f2,'one_step',0); raise AssertionError
    except ValueError: pass
    return {'checks':checks,'status':'OK'}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-check',action='store_true'); ap.add_argument('--locate',nargs=2,type=int,metavar=('P','N')); args=ap.parse_args()
    if args.self_check: print(json.dumps(self_check(),indent=2)); return
    if args.locate: print(json.dumps(dict(zip(('k','L','U'),locate_basin(*args.locate))),indent=2)); return
    ap.print_help()

if __name__=='__main__': main()
