# PREFIX-961 — Endpoint gap-six triangular sparsity and mandatory source localization

Date: 2026-11-20. Frozen scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). This is a continuation of PREFIX-960 in the **auxiliary named-XOR observation model**, not a theorem of native 6D X6/BRC dynamics. Historical provenance: EM-DIRECT-58C410 and MCP-31edc522830749ad8775ca012e02ef30 (not present execution credentials). Mathematical status: author proof plus finite exact checker; NOT_REVIEWED.

## Definitions and objective

Let p>=4, H=2^(p-1), Qp={H+1,H+3,...,2H-1}; k odd with 1<=k and k+2<H. For distinct ordered a,b in Qp let named source indices 0<=i,j,I,J<p and positive integer quotients t,T satisfy the two original equations

~~~
((k*a) XOR 2^j)-2^i=t*b,
(((k+2)*a) XOR 2^J)-2^I=T*b.
~~~

The signs are fixed by actual input bits, s=1-2*bit_j(k*a), S=1-2*bit_J((k+2)*a). Put c=2^i-s*2^j, C=2^I-S*2^J, and m=T-t. Subtracting the named equations yields the exact identity C-c=2*a-m*b. Distinct index quadruples remain distinct named witnesses even when numeric residuals agree. PREFIX-960 proved that m is in {0,...,6}; this unit analyzes m=6.

## Theorem 961.1 — Exact triangular support and count

For any named joint witness with m=6, write a=H+v and b=H+u, where u,v are odd integers in [1,H-1]. Necessarily

~~~
v-3*u >= H/2+2.                                         (1)
~~~

Consequently a>b and a>=3*H/2+5. The number A_p of ordered pairs of Qp satisfying (1), **before** checking a quotient or named bit source, is

~~~
R=H/4=2^(p-3), q=floor((R-3)/3),
A_p=0 if q<0, otherwise (q+1)*(R-2)-3*q*(q+1)/2.      (2)
~~~

For p>=4, setting h=floor(R/3) gives A_p=(3*h*h+h)/2 if R=3*h+1, and A_p=(3*h*h+3*h)/2 if R=3*h+2. In particular, A_p/|Qp|^2 tends to 1/24. At p=19, equation (2) gives A_19=715,816,960 potentially eligible pairs among |Q19|^2=17,179,869,184. Therefore the gap-six constraint alone excludes 95.83339691162109375% of ordered pairs from any full-domain search. This is a domain reduction, not an observed witness count or a runtime benchmark.

**Proof.** Every numerical signed source residual satisfies 1-H<=c,C<=2H. Therefore C-c>=1-3H. If m=6, the exact subtracted equation gives

~~~
C-c=2*a-6*b=2*v-6*u-4*H>=1-3*H,
2*(v-3*u)>=H+1.
~~~

The oddness of u and v makes v-3*u even. For p>=4, H is divisible by 8, so rounding to the next even integer proves (1). Then v>=H/2+3*u+2>=H/2+5, with v>u.

Writing v=2*r+1 and u=2*z+1 with 0<=r,z<H/2, inequality (1) is equivalent to r>=3*z+R+2. For each z from zero to floor((R-3)/3), there are exactly R-3*z-2 admissible r values. The resulting finite arithmetic progression is (2). R=2^(p-3) is either 1 or 2 mod 3; this proves the closed forms. The leading term of A_p is R^2/6 and |Qp|^2=(2R)^2, yielding 1/24. QED.

## Theorem 961.2 — Mandatory high-source indices

Every m=6 named witness satisfies all of

~~~
c>=H+9; C<=-8;
s=-1 and max(i,j)=p-1;
S=+1, J>I, J>=4.
~~~

There are two mutually exclusive source patterns:

- **Top/top first source:** c=2H; then i=j=p-1 and bit_(p-1)(k*a)=1.
- **Other first source:** c!=2H; then J=p-1 and bit_(p-1)((k+2)*a)=0.

Both statements describe **necessary** constraints. They retain the original source index labels and actual sign predicates.

**Proof.** Since a<=2H-1 and b>=H+1, C-c=2a-6b<=-2H-8. Combining this with C>=1-H gives c>=H+9, and with c<=2H gives C<=-8. Since c>H, its form 2^i-s2^j forces s=-1 and at least one of i,j=p-1 (otherwise c<=H). A negative C=2^I-S2^J forces S=+1 and J>I, and C<=-8 forces J>=4.

If c=2H, both indices equal p-1. Otherwise c<=H+H/2. Consequently C=(C-c)+c<=-H/2-8. If J<=p-2, however, C>=1-H/2; contradiction. Thus J=p-1 and the required actual high bit of the second core product is zero. QED.

## Corollary 961.3 — Earliest realizable bitwidth

No legal odd adjacent-core named witness attains m=6 for p<=5; such witnesses exist for p=6. This is a statement about the declared named-XOR domain.

**Proof.** For p=4, equation (1) has no possible odd u,v. For p<4, the source-difference bound and the possible Qp values already exclude the endpoint. For p=5, H=16 and (2) leaves only (a,b)=(29,17) or (31,17). Here c>=25; since any c!=2H is at most H+H/2=24, necessarily c=32 with i=j=4 and bit_4(k*a)=1. The required C=2a-6b+c equals -12 for a=29 and -8 for a=31, so J=4 and bit_4((k+2)*a)=0.

For a=31, every odd 1<=k<=13 has bit_4(k*31)=bit_4((k+2)*31)=1, contradicting the second zero-bit requirement. For a=29, examining (-3k) mod 32 and (-3(k+2)) mod 32 over k=1,3,...,13 shows that only k=5 has first bit 4 equal to 1 and second bit 4 equal to 0. But t=(5*29-32)/17=113/17 is not an integer. Thus p=5 is impossible.

For p=6 the exact original-source extremizer is

~~~
H=32, k=5, a=59, b=33, t=7, T=13;
(i,j)=(5,5), (I,J)=(4,5);
(295 XOR 32)-32=231=7*33;
(413 XOR 32)-16=429=13*33.
~~~

It realizes T-t=6 with all sign and domain conditions. QED.

## Finite evidence and reproducibility

The companion Python script PREFIX961_R6_GAP6_TRIANGLE_VERIFIER.py directly enumerates the original integer XOR equations, all source indices and all odd adjacent cores, **without** loading the PREFIX-955/959B pair certificates. For p=4,...,8 it enumerates the entire Qp^2 domain; p=9 uses only the triangle already proved necessary by Theorem 961.1. It also independently enumerates triangle pairs at every tested width and checks them against (2).

| p | Triangle pairs | Pair domain | Named m=6 histories | First residual c=2H | Other first residual |
|---|---:|---|---:|---:|---:|
| 4 | 0 | Full | 0 | 0 | 0 |
| 5 | 2 | Full | 0 | 0 | 0 |
| 6 | 9 | Full | 2 | 2 | 0 |
| 7 | 40 | Full | 4 | 2 | 2 |
| 8 | 165 | Full | 10 | 5 | 5 |
| 9 | 672 | Triangle only | 37 | 22 | 15 |

All found m=6 histories satisfied the triangle and high-source constraints; no failures occurred. The p=9 completeness statement uses the universal triangle theorem rather than a direct outside-triangle scan. The script emits PREFIX961_R6_EXACT_RESULTS.json, including exact per-width counts, domain labels, and named examples. All arithmetic is integer, not floating-point.

## Scope, comparison, and unfinished work

The exact domain reduction and high-index localization are **new endpoint-specific refinements** of PREFIX-960; no claim is made that previously reported 6,203 Q19 off-diagonal pairs or 8,649 combined histories have changed. The p=19 number above is the count of **potential** ordered pairs after a necessary inequality, not the number of collision witnesses and not a speedup measurement.

This is a mathematically defined auxiliary named-XOR observer. It cannot be promoted to intrinsic P000, X6 native rotations, BRC state evolution, or physical triadic events without a typed observer/operation-preservation bridge. Review status is NOT_REVIEWED. The historical R6 researcher/SID attribution is preserved, while shared TASK CLAIM and portable Activity association remain separate permissions and bookkeeping.

Next: derive the analogous exact support and high-source-type partition for gap m=5, and measure whether these necessary filters reduce the **complete** odd-divisor-fiber cost while preserving distinct named histories. Do not duplicate existing X6 group/Burnside work or interpret the XOR model as a physical native dynamics result.
