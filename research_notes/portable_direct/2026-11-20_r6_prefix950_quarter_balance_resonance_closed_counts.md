# PREFIX-950 — Quarter-balanced resonance and exact short dyadic boundary formulas

Date 2026-11-20. Frozen scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessor PREFIX-949 at `201632933bd8ee4d4b39a693b63ff2e5c5f2c0d2`. Original researcher provenance EM-DIRECT-58C410 / SID MCP-31edc522830749ad8775ca012e02ef30. AUTHOR_PROVED / INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. This is an auxiliary named-XOR two-port observation model, not native Heartbeat-X6 or typed BRC arithmetic.

## 1. Object

Let `M=2^m`, `V=2^v` with `m>=3,v>=1` and adjacent odd cores `k=M-1,l=M+1`. PREFIX-949 classified nonzero resonant joint witnesses: `a-b=V`, quotient pair `(t,T)=(k,l)`, source indices `(i,j,I,J)=(m+v,v,v,m+v)`, and the ACTUAL named source-bit tests

```
bit_v(k*a)=0, bit_(m+v)(l*a)=1.                   (1)
```

Strict Q19/32 domain: `A=2^18=262144`; odd `a,b` in `[A+1,2A-1]`; `m+v<=18`, and legal start/end states `<2^32`. The latter is equivalent here to `l*a<2^32` (XOR flips only source bits <=18). Let `C(m,v)` count distinct admissible `(a,b=a-V)` satisfying (1).

## 2. Universal quarter-balance theorem

**Theorem 1.** For all `m,v>=1`, exactly `P/8` of the `P=2^(m+v+1)` residues `a mod P` are ODD and satisfy both (1). Thus every interval of integer length a multiple of P contains exactly one eighth as many qualifying a.

*Proof.* Multiplication by odd k permutes odd residues mod `2^(v+1)`, so exactly half of odd residues have first bit zero. Translation `a -> a+2^(m+v) mod P` preserves the first bit, keeps a odd, and flips the second bit, since l is odd. Hence exactly half of those pass the second test: 1/4 of odd residues, or P/8 of all residues. Periodicity proves the interval claim.

For `m+v<=17`, P divides the strict-Q19 interval length A, so before enforcing the lower bound on b the count is exactly `A/8=32768` for every m,v.

## 3. Closed formula for all m+v<=17

**Theorem 2.** Before any upper 32-bit truncation, for `m+v<=17`,

```
C_0(m,v) = 32768 - ceil(floor(V/(M+1))/2).          (2)
```

*Proof.* Enforcing `b=a-V>=A+1` removes odd `a=A+x` with `1<=x<V`. Because `m+v<=17`, adding A does not change either tested bit. The second bit of `(M+1)x` is one exactly when `(M+1)x>=MV`; write `x=V-y` to get odd `1<=y<=floor(V/(M+1))`. On this range `0<(M-1)y<V`; since `(M-1)x=MV-V-(M-1)y`, its residue mod `2V` is `V-(M-1)y`, lying below V. Thus the first-bit test holds automatically. Exactly `ceil(floor(V/(M+1))/2)` odd y are deleted. In particular the correction is zero for `v<=m`.

## 4. Closed short residue sum for m+v=18

When `m+v=18`, Q19 covers only half of period `2A`. Write `a=A+Vq+r`, with `0<=q<M`, odd `1<=r<V`. The lower bound on b excludes precisely q=0. Put

```
g_r=floor((M+1)*r/V), alpha_r=floor((M-1)*r/V) mod 2.
```

**Theorem 3.** Before any upper state truncation, the EXACT number is

```
C_0(m,18-m) = sum over odd r in [1,V):
    alpha_r=0: max(0,ceil((M-g_r)/2)-1)
    alpha_r=1: ceil(g_r/2).                          (3)
```

*Proof.* The first bit is zero exactly when `q=alpha_r mod 2`. Since l is odd, `bit_18(l(A+Vq+r))=1` iff `bit_18(l(Vq+r))=0`. The latter bit is the parity of `q + [q>=M-g_r]` because `l(Vq+r)=Aq+Vq+lr` and `0<=Vq+lr<2A`. Therefore for alpha 0 the legal q are positive even integers smaller than M-g, while for alpha 1 they are odd integers at least M-g. Counting them gives the displayed two summands. Only V/2 exact summands are required.

**High-core closed totals.** If m>v, then M/V is even, `g_r=(M/V)r` and `alpha_r=1` for every odd r. Therefore (3) simplifies to `(M/(2V))*sum_{odd r<V}r=MV/8=32768`. For m=v=9 it becomes `32768-128=32640`. Together with (2), for m=10,11,12 every allowed v contributes exactly 32768 and the full totals are 262144, 229376, 196608 respectively.

## 5. Exact 32-bit endpoint cuts

For m=13, `l=8193` and legal `a<=floor((2^32-1)/8193)=524224`. Exactly 32 odd top starts `a=2^19-d` with odd `1<=d<=63` are excluded. For each `v=1,...,5`, low bit on this tail equals `bit_v(d)` because `k*a == d mod 2^(v+1)`; high bit equals `1-bit_v(d)`, since `l*a == -ld mod 2^(m+v+1)` and `ld-1=M*d+d-1`, with d-1<M. Exactly 16 of the 32 odd d have low bit zero and high bit one for each v. Thus the full m=13 count is `5*(32768-16)=163760`. For m>=14, already `(2^m+1)*(A+1)>=2^32`, so no legal starts: total zero. No global enumeration is needed for these terminal claims.

## 6. Exact validation and next question

The attached Python checker computes (2), (3), and only the necessary upper state tail and independently scans the entire allowed odd-a interval for every `m=3,...,14`, `1<=v<=18-m`. It also checks exact quarter-balance on complete periods for small m,v. EVERY integer cell agrees with direct scanning. Published PREFIX-949 totals are reproduced without changing the earlier scientific input:

| m | pair | exact distinct pairs |
|---:|:--|---:|
|3|7/9|485798|
|4|15/17|456313|
|5|31/33|424864|
|6|63/65|392657|
|7|127/129|360193|
|8|255/257|327553|
|9|511/513|294784|
|10|1023/1025|262144|
|11|2047/2049|229376|
|12|4095/4097|196608|
|13|8191/8193|163760|
|14|16383/16385|0|

Across m=3..13, the nonconstant boundary sums for m+v=18 have only `16384+8192+...+16=32752` terms total; the state-tail exclusion concerns just 32 odd starts. This is an arithmetic operation-count reduction, not a measured time-speedup claim. No float arithmetic is used. The stored JSON includes each (m,v), formula count, endpoint subtraction and direct-scan agreement.

This result explains the finite PREFIX-949 census structurally, for the nonzero resonant **joint witness subset**. It does not increase the conditional certificate union (previously 7597037839) nor establish the still-open `B_fix,odd(32) in {19,20}`. Retain both named bits, distinct histories and joint relation, as required by P000/ACTIVE ontology; no native X6 identification, CLAIM, formal Result or independent Review is asserted.

**Next:** develop an exact determinant-nonzero adjacent-core intersection count by quotient-gap and sign congruence, keeping the named source bits and checking each exceptional determinant zero branch. Compare a bounded pilot against direct pair enumeration before full Q19 deployment.
