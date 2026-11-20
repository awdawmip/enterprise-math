# PREFIX-962 — The exact one-fifth gap-five support law

Date: 2026-11-20. Frozen science pin f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Continues PREFIX-960 and PREFIX-961 in the auxiliary named-XOR observation model. Historical R6 provenance EM-DIRECT-58C410 / MCP-31edc522830749ad8775ca012e02ef30, not current authenticated task execution. Author proof and finite exact integer checker; NOT_REVIEWED.

## Observation model

Fix p>=4, H=2^(p-1), and Qp={H+1,H+3,...,2H-1}. Take an odd k>=1 with k+2<H; a,b are distinct ordered members of Qp. A named joint witness comprises i,j,I,J in {0,...,p-1}, t,T>=1, with

~~~
((k*a) XOR 2^j)-2^i=t*b,
(((k+2)*a) XOR 2^J)-2^I=T*b.
~~~

Let s=1-2bit_j(k*a), S=1-2bit_J((k+2)*a), c=2^i-s2^j, C=2^I-S2^J. The exact residual identity is C-c=2a-(T-t)b. The current question is the necessary ordered-pair domain for gap m=T-t=5, independent of core and source indices.

## Theorem 962.1 — Exact fifth-area identity

Put a=H+v, b=H+u with u,v odd in [1,H-1], and N=H/2=2^(p-2). If a valid named history has m=5, then

~~~
2*v-5*u >= 1.                                          (1)
~~~

The number of ordered pairs (a,b) in Qp^2 satisfying (1), *before* checking any quotient or XOR bit predicate, is exactly

~~~
A5(p) = (N^2 - (-1)^p)/5.                               (2)
~~~

Every pair in this necessary domain is off-diagonal, since v=u would violate (1). Thus, for all p>=4, the arithmetic sieve excludes asymptotically four fifths of the full ordered-pair domain. At p=19, with N=131072, equation (2) gives exactly **3,435,973,837** candidate ordered pairs among 17,179,869,184. This is an exact domain count, **not** the number of genuine named witnesses.

**Proof of necessity.** The numerical source residuals always obey 1-H<=c,C<=2H, hence C-c>=1-3H. For m=5, the original-equation subtraction reads

~~~
C-c=2a-5b = -3H + 2v-5u.
~~~

It follows immediately that 2v-5u>=1. Since u,v>=1, this also gives v>u, proving the off-diagonal assertion.

**Proof of the exact cardinality.** Write u=2z+1 and v=2r+1 with 0<=r,z<N. Condition (1) becomes 4r>=10z+4, or

~~~
r >= ceil((5*z+2)/2).
~~~

Consequently admissible z satisfy 0<=z<=Z=floor((2N-4)/5), and

~~~
A5(p)=sum_{z=0}^{Z} (N-ceil((5*z+2)/2)).
~~~

Pair even and odd z. For z=2q, the ceiling is 5q+1; for z=2q+1, it is 5q+4. Thus, if Z=2q+1,

~~~
A5=(q+1)*(2N-5*(q+1)).
~~~

If Z=2q,

~~~
A5=(2q+1)*N-5*q*(q+1)-1.
~~~

Now write N=5h+r, r in {1,2,3,4}. When r=1, Z=2h-1 and the odd-Z formula yields (N^2-1)/5. For r=2 or 3, Z=2h and the even-Z formula yields (N^2+1)/5. For r=4, it yields (N^2-1)/5. Finally N=2^(p-2), whose mod-5 residue lies in {1,4} for even p and {2,3} for odd p. This is precisely (2). QED.

## Lemma 962.2 — Required opposite source parity

For every gap-five named witness, exactly one of the two numerical signed source residuals c,C is odd. For a named index pair, the numerical residual 2^i - s2^j is odd precisely when **exactly one** of i,j equals zero. Thus exactly one of the first and second named index pairs (i,j) and (I,J) has exactly one zero index.

**Proof.** Because a,b are odd, 2a-5b is odd. Therefore C-c is odd, so c and C have opposite parity. The parity of each power of two depends solely on whether its exponent is zero; subtracting or adding is identical mod 2. This proves the named index condition. QED.

This parity fact is compatible with earlier odd-gap bit filters; this unit's new combinatorial result is equation (2), an exact core-independent support cardinality.

## Exact reproduction and limited inference

The independent script PREFIX962_R6_GAP5_FIFTH_VERIFIER.py counts the eligible pair domain by direct integer enumeration and checks (2); separately it enumerates all original XOR named indices and positive quotients for every odd k with k+2<H and full Qp^2 at p=4,...,8. It verifies each observed m=5 witness against (1), the residual equation and opposite source parity, without reading earlier pair-ID certificates.

| p | Eligible ordered pairs (exact formula and direct count) | Named m=5 histories in all odd adjacent-core systems |
|---|---:|---:|
| 4 | 3 | 2 |
| 5 | 13 | 3 |
| 6 | 51 | 22 |
| 7 | 205 | 45 |
| 8 | 819 | 144 |

The code creates PREFIX962_R6_EXACT_RESULTS.json with the precise verified domain, per-width counts, an original-equation witness example and the unchanged frozen input pin. Integer arithmetic only; assertions passed in the local run. These counts support regression. Theorem 962.1 derives from the proof for arbitrary p.

## Reuse and next questions

The exact support is a pre-XOR filter for one endpoint-adjacent quotient-gap fiber and is compatible with retaining every named witness, rather than replacing sources with a Boolean pair membership. Whether applying the one-fifth filter reduces *end-to-end* Q19 divisor-fiber work depends on generation and lookup cost, and remains an experimental performance question.

PREFIX-961 and this result are exact auxiliary-integer observer theorems; no native P000/X6 triadic-event correspondence or BRC port-preservation map is claimed. Neither paper acquires a formal TASK CLAIM or independent review. Next useful work is a symbolic/algorithmic comparison of m=5 and m=6 support filters with the cached odd-divisor-fiber generator, including exact named source multiplicities and total enumeration cost.
