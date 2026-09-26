"""Typed sparse deterministic BRC compiler for complete modular permutations.

This is a positive branch compiler, not a signed propagation replacement. Every
arithmetic column is constructed by reuse of actually executed BRC full-adder
columns. Signed/residual fibres are transported without contracting their labels.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, os, sys

SOURCE=Path(os.environ.get("BRC_STAGE87_SOURCE", "D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source")).resolve()
sys.path.insert(0,str(SOURCE))
from stage45.brc_loop_recheck import core_power, verify_vendor, CALLS
from stage78.shor_benchmark import full_adder_columns,denominators,gcd_brc

def integer(x):
    return isinstance(x,int) and not isinstance(x,bool)

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

@lru_cache(None)
def native_adder():
    vendor=verify_vendor()
    columns=full_adder_columns()  # actual canonical positive BRC 12-state execution
    if len(columns)!=8:raise AssertionError("incomplete full-adder input columns")
    return columns,{"vendor":vendor,"entrypoint":"stage78.shor_benchmark.full_adder_columns",
      "positive_BRC_input_states":12,"input_columns":8,"columns":columns,
      "observer":"retained input triple -> (sum bit, carry bit)",
      "scope":"exact integer label compiler; not a reversible physical erasure"}

def add_unsigned(left,right,width):
    """BRC digit transducer with input/carry provenance, including final carry."""
    if not integer(width) or width<1 or any(not integer(v) or not 0<=v<(1<<width) for v in (left,right)):
        raise ValueError("unsigned integers must fit the declared width")
    columns,_=native_adder();carry=0;value=0;cells=[]
    for bit in range(width):
        x=(left>>bit)&1;y=(right>>bit)&1;code=(x<<2)|(y<<1)|carry
        digit,next_carry=columns[code]
        cells.append((bit,code,digit,next_carry))
        value|=digit<<bit;carry=next_carry
    return value,carry,{"left":left,"right":right,"width":width,
      "cells":tuple(cells),"low":value,"carry":carry}

def verify_add_trace(trace):
    value,carry,rebuilt=add_unsigned(trace["left"],trace["right"],trace["width"])
    if digest(rebuilt)!=digest(trace):raise ValueError("BRC addition trace does not replay")
    return value,carry

@dataclass(frozen=True)
class SparsePermutation:
    """One positive unit branch for EVERY source basis label, with retained word.

    Dense embedding E(P)[i,j]=1 iff j=targets[i]. Provenance is intentionally
    separate from the endpoint projection: inverse/compose do not erase words.
    """
    targets: tuple[int,...]
    provenance: dict

    def __post_init__(self):
        n=len(self.targets)
        if not n or any(not integer(z) or not 0<=z<n for z in self.targets) or len(set(self.targets))!=n:
            raise ValueError("complete bijective basis columns required")

    def __getitem__(self,source):return self.targets[source]
    def __len__(self):return len(self.targets)

    def then(self,other):
        if len(self)!=len(other):raise ValueError("carrier mismatch")
        return SparsePermutation(tuple(other[z] for z in self.targets),
          {"operation":"serial","left":self.provenance,"right":other.provenance,
           "word_retention":"left then right; equal endpoints do not identify provenance"})

    def inverse(self):
        inv=[0]*len(self)
        for y,z in enumerate(self.targets):inv[z]=y
        return SparsePermutation(tuple(inv),{"operation":"inverse","of":self.provenance,
          "word_retention":"inverse edge labels retain original edge identity"})

    def controlled(self):
        n=len(self)
        return SparsePermutation(tuple(range(n))+tuple(n+z for z in self.targets),
          {"operation":"controlled_direct_sum","of":self.provenance,"control_labels":(0,1)})

    def dense_embedding(self):
        return tuple(tuple(F(int(j==self[i])) for j in range(len(self))) for i in range(len(self)))

    def native_dense_check(self):
        """Bounded implementation evidence; not needed by the universal theorem."""
        mat=core_power(self.dense_embedding(),1)
        for source,row in enumerate(mat):
            if any(v!=int(target==self[source]) for target,v in enumerate(row)):
                raise AssertionError("sparse columns differ from actual BRC kernel")
        return {"basis_columns":len(self),"matrix_entries":len(self)**2,"all_match":True}

    def transport_rows(self,rows):
        """Rows may be signed; all fibre coordinates remain uninterpreted."""
        if len(rows)!=len(self):raise ValueError("complete input carrier required")
        out=[None]*len(self)
        for source,row in enumerate(rows):out[self[source]]=row
        return tuple(out)

@lru_cache(None)
def compile_modular_permutation(N,b):
    """All-column certificate, built by repeated typed addition, never b*y%N.

    Extends work y>=N by identity, exactly as frozen Stage78. Non-coprime b is
    rejected by the complete bijection check; no order/factors enter the API.
    """
    if not integer(N) or N<2 or not integer(b) or not 0<=b<N:
        raise ValueError("N>=2 and integer 0<=b<N required")
    n=(N-1).bit_length();size=1<<n;width=n+1;modulus=1<<width
    columns,receipt=native_adder();r=0;targets=[];steps=[]
    for y in range(N):
        targets.append(r)
        s,overflow,add=add_unsigned(r,b,width)
        if overflow:raise AssertionError("r+b must fit n+1 bits")
        reduced,borrow_complement,subtract=add_unsigned(s,modulus-N,width)
        following=reduced if borrow_complement else s
        if not 0<=following<N:raise AssertionError("one subtraction must reduce the sum")
        steps.append({"source":y,"target":r,"add_b":add,"subtract_N":subtract,
          "reduction_carry":borrow_complement,"next_residue":following,
          "edge_id":f"modmul:{N}:{b}:column:{y}"})
        r=following
    if r!=0:raise AssertionError("N repeated additions must return to zero")
    targets.extend(range(N,size))
    certificate={"schema":"BRC_SPARSE_MODULAR_PERMUTATION_V1","status":"AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED",
      "N":N,"b":b,"width":n,"arithmetic_width":width,"size":size,
      "native_adder":receipt,"steps":tuple(steps),"targets":tuple(targets),
      "identity_tail":{"first":N,"last_exclusive":size},
      "retained_records":"all source columns, addition cells, subtraction cells, carry and edge IDs",
      "resource_counts":{"targets":size,"modular_additions":N,"adder_digit_applications":2*N*width},
      "scope":"complete positive unit permutation; arbitrary retained signed/complex/vector fibres by transport"}
    permutation=SparsePermutation(tuple(targets),{"operation":"modular_compiler",
      "N":N,"b":b,"certificate_sha256":digest(certificate)})
    return permutation,certificate

def sparse_modular_columns(N,b):
    """Tuple-returning injection point for StreamingProgram's table factory."""
    return compile_modular_permutation(N,b)[0].targets

def sparse_modular_power_chain(N,a,t):
    """Certified b_i=a^(2^i) and tables; each next b is the column table[b]."""
    if not integer(N) or N<2 or not integer(a) or not 1<=a<N or not integer(t) or t<0:
        raise ValueError("N>=2, 1<=a<N, nonnegative width required")
    b=a;powers=[];tables=[];origins=[]
    for i in range(t):
        permutation,certificate=compile_modular_permutation(N,b)
        powers.append(b);tables.append(permutation.targets)
        following=permutation[b]
        origins.append({"bit":i,"b":b,"square_source":b,"square_target":following,
          "certificate_sha256":digest(certificate)})
        b=following
    return tuple(powers),tuple(tables),tuple(origins)

@lru_cache(None)
def sparse_modular_power_trace(N,a,e):
    """Positive deterministic square-and-multiply, with all reused column IDs."""
    if not integer(N) or N<2 or not integer(a) or not 1<=a<N or not integer(e) or e<0:
        raise ValueError("N>=2, 1<=a<N, nonnegative exponent required")
    original=e;b=a;y=1;steps=[];bit=0
    while e:
        permutation,certificate=compile_modular_permutation(N,b)
        out=permutation[y] if e&1 else y;following=permutation[b]
        steps.append({"bit":bit,"exponent_bit":e&1,"input":y,"output":out,
          "b":b,"next_b":following,"certificate_sha256":digest(certificate),
          "column_used":y if e&1 else None,"square_column":b})
        y=out;b=following;e>>=1;bit+=1
    return {"N":N,"a":a,"exponent":original,"value":y,"steps":tuple(steps),
      "scope":"actual BRC adder-compiled modular columns; no order or factors input"}

def sparse_modular_power_brc(N,a,e):
    return sparse_modular_power_trace(N,a,e)["value"]

def sparse_classical_postprocess(N,a,t,k):
    """Original CF candidates/reasons, replacing only modular-power execution.

    gcd_brc remains the actual positive Euclidean trace. Equality includes the
    rejected-candidate order and the explicit lack of a minimal-order claim.
    """
    if k==0:return {"status":"ZERO_PHASE_RETRY","factors":[]}
    rejected=[]
    for q in denominators(k,1<<t,N-1):
        if sparse_modular_power_brc(N,a,q)!=1:
            rejected.append((q,"NOT_RETURNING_EXPONENT"));continue
        if q%2:
            rejected.append((q,"ODD_RETURNING_EXPONENT"));continue
        h=sparse_modular_power_brc(N,a,q//2)
        fs=sorted({gcd_brc(h-1,N),gcd_brc(h+1,N)}-{1,N})
        if fs:return {"status":"FACTORS","verified_returning_exponent":q,"minimal_order_claimed":False,"factors":fs}
        rejected.append((q,"TRIVIAL_GCD_RETRY"))
    return {"status":"NO_FACTOR_THIS_READOUT","factors":[],"rejected":rejected}

def verify_modular_certificate(certificate):
    if certificate.get("schema")!="BRC_SPARSE_MODULAR_PERMUTATION_V1":raise ValueError("wrong type")
    N,b=certificate["N"],certificate["b"]
    if not integer(N) or N<2 or not integer(b) or not 0<=b<N:raise ValueError("invalid N,b")
    n=(N-1).bit_length();size=1<<n;width=n+1;modulus=1<<width
    if (certificate["width"],certificate["arithmetic_width"],certificate["size"])!=(n,width,size):raise ValueError("width mismatch")
    _,receipt=native_adder()
    if digest(certificate["native_adder"])!=digest(receipt):raise ValueError("native provenance differs")
    if len(certificate["steps"])!=N:raise ValueError("missing input basis columns")
    targets=[];r=0
    for y,step in enumerate(certificate["steps"]):
        if (step["source"],step["target"])!=(y,r) or step["edge_id"]!=f"modmul:{N}:{b}:column:{y}":raise ValueError("column origin differs")
        targets.append(r)
        if tuple(step["add_b"][k] for k in ("left","right","width"))!=(r,b,width):raise ValueError("wrong addition inputs")
        s,overflow=verify_add_trace(step["add_b"])
        if overflow:raise ValueError("overflow")
        if tuple(step["subtract_N"][k] for k in ("left","right","width"))!=(s,modulus-N,width):raise ValueError("wrong reduction inputs")
        reduced,carry=verify_add_trace(step["subtract_N"])
        r=reduced if carry else s
        if step["reduction_carry"]!=carry or step["next_residue"]!=r or not 0<=r<N:raise ValueError("wrong retained reduction")
    if r:raise ValueError("full modular addition loop did not close")
    targets.extend(range(N,size))
    if tuple(certificate["targets"])!=tuple(targets):raise ValueError("target projection differs")
    if certificate["identity_tail"]!={"first":N,"last_exclusive":size}:raise ValueError("tail changed")
    expected={"targets":size,"modular_additions":N,"adder_digit_applications":2*N*width}
    if certificate["resource_counts"]!=expected:raise ValueError("resource counts changed")
    SparsePermutation(tuple(targets),{"verified":digest(certificate)})
    return {"complete_columns":size,"adder_digit_applications":2*N*width,"certificate_sha256":digest(certificate),"verified":True}
