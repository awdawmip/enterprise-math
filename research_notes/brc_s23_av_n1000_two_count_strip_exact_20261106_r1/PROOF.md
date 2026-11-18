# S23 conditional AV: exact two-count reconstruction deficiency certificate (n=1000)

Date: 2026-11-06. Evidence classification: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Scientific input is frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Current behavioral policy and project runtime authority are read separately from current main. This work extends the six-point stop4-count certificate of PR #1777 at `0f0bfea44b6d75a0f2d5c8014730730740a689c5`.

## Exact model and theorem

For each `a,c in [1/2,7/8]`, define the fully tagged three-outcome law
`P_(a,c) = (a,z,1-a-z)` on (stop1,stop3,stop4), with `z=(1-a)c`. The compressed binary observer is `B_(a,c)=(z,1-z)` on (stop3,other). Repeated observations are conditionally IID given the single shared unknown pair (a,c). For `n=1000`,

`delta_1000 = inf_K sup_(a,c) TV(P_(a,c)^{tensor 1000}, B_(a,c)^{tensor 1000} K)`,

where K ranges over all stochastic kernels from binary words to full three-label words (including kernels with correlated outputs).

**Theorem (exact rational finite witness).** The explicitly defined rational number `R_20` below satisfies

`delta_1000 >= R_20 > 807/1000 = 0.807`.

Its decimal display begins `0.807079209717409305877823041742505418712304415...`. All comparisons use integer arithmetic and Python `Fraction` in `VERIFY.py`.

## Common observer fiber and disjoint classifier

Fix `z=1/4`. Define six rational stop4 probabilities:

`q=(1/28,3217/50000,10091/100000,14447/100000,9727/50000,1/4)`.

Set `a_j=3/4-q_j`, `c_j=1/(1+4q_j)`. These lie in the lawful parameter box and satisfy `(1-a_j)c_j=1/4`. Thus the six binary input laws are *identical*, and any parameter-independent K produces one common output law Q. The complete laws are `P_j=(3/4-q_j,1/4,q_j)`.

Let U be the count of stop4 outcomes in a complete 1000-word, and let S be the count of stop3. Start with six events defined by U intervals:

`I=((0,48),(49,81),(82,121),(122,168),(169,221),(222,1000))`.

The initial partition `E^0_j={U in I_j}` is the predecessor witness. Improve it using a **joint count** of stop3 and stop4, rather than U alone. The 20 mutually disjoint reassigned strips (U,source class,destination class,S lower,S upper) are:

```
(47,0,1,277,953), (48,0,1,262,952), (49,1,0,0,245), (50,1,0,0,230),
(80,1,2,264,920), (81,1,2,254,919), (82,2,1,0,244), (83,2,1,0,235),
(120,2,3,261,880), (121,2,3,254,879), (122,3,2,0,247), (123,3,2,0,241),
(167,3,4,258,833), (168,3,4,253,832), (169,4,3,0,248), (170,4,3,0,243),
(220,4,5,256,780), (221,4,5,253,779), (222,5,4,0,248), (223,5,4,0,245).
```

Move each strip from its initial class to its listed destination. Each strip has a distinct U, so the resulting `E'_j` remain a disjoint exhaustive partition of all complete words.

For fixed `U=u,S=s`, the multinomial probability under hypothesis j is a common combinatorial factor times

`L_j(u,s)=q_j^u (3/4-q_j)^(1000-u-s) (1/4)^s`.

The `(1/4)^s` factor cancels in likelihood comparisons. Since `q_j` are distinct and `a_j=3/4-q_j`, the likelihood ratio between each source and destination is monotone in s for each fixed u. In the verifier, all 20 strips are checked at both endpoints with strict *exact rational* dominance of the destination likelihood; the adjacent excluded points are also checked whenever present. Thus every reassignment strictly improves `sum_j P_j(E'_j)`.

## Exact finite sum and proof

For a rational `q=r/d`, define the exact strip mass

`M(q,u,l,h)=Pr_q(U=u,l<=S<=h)`.

Writing `m=1000-u`, the finite multinomial identity is

`M(q,u,l,h) = binom(1000,u) (4r)^u / (4d)^1000 * sum_(s=l)^h binom(m,s) d^s (3d-4r)^(m-s)`.

This identity follows by grouping the multinomial law of `(stop1,stop3,stop4)` by (U,S); it is evaluated with integer binomial coefficients and powers. Let

`A0=sum_(j=0)^5 Pr_{q_j}(U in I_j)` and
`G=sum_(u,i,j,l,h in MOVES) [M(q_j,u,l,h)-M(q_i,u,l,h)]`.

Define the exact rational certificate

`R_20=(A0+G-1)/6`.

For an arbitrary common reconstruction distribution Q, total variation satisfies
`TV(P_j^{tensor1000},Q) >= P_j(E'_j)-Q(E'_j)`.
Summing j, the Q terms sum to one; therefore
`6 sup_j TV(P_j^{tensor1000},Q) >= A0+G-1`.
Taking the infimum over stochastic K yields
`delta_1000>=R_20`.
The exact verifier proves `R_20>807/1000` with a strict integer/rational comparison. This is a theorem for **all** common stochastic kernels, independent of their output correlation structure.

## BRC information-loss interpretation and scope

The binary observer retains the tagged stop3 mass z but collapses the joint distribution of the other two tags. The witness explicitly preserves the complete stop3/stop4 count relation and shows a stronger obstruction to this quotient. The theorem concerns the frozen S23 *conditional AV statistical submodel*; its transfer to the ten-label mother target `R_beh(k,10)` is a separate observer/encoder/decoder mapping problem. The numerical decimals are display only; the certificate uses exact rational arithmetic.

Source verification files: `VERIFY.py` (complete runnable integer/Fraction certificate), `RUN_EVIDENCE.txt` (observed local stdout), `SOURCES.md` and `NEXT_TASK.md`. Independent mathematical review and formal task admission remain pending.
