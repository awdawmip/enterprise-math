# D25/SECOND-DIGIT-LIFT — exact composite-parameter obstruction inside both target residue classes

2026-10-24 | TASK_RESEARCH portable author lane `chatgpt-research-onhour-enterprise-math-20260923` | **EXACT FINITE COUNTEREXAMPLES TO AN ALL-INTEGER EXTENSION; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.** This is neither a counterexample to the prime-only D25 hard target nor an executed native benchmark or formally admitted Source checkpoint.

## 1. Frozen mother question and new discriminating question

Mother `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; Task publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` remains unchanged. The actual original hard target concerns **primes** `p=6m+1`, `p mod 24 in {13,19}`:
[
S_mstackrel{?}{equiv}p(4/3)^{p-1}pmod {p^3}.
]
Earlier author-side exact checks cover all 575 target primes p<=20000, and even/odd LOW seed jets and fixed-prime WZ five-port normalization are already available. These are inputs, not results recredited here.

The new methodological question is precise: does **the same unchanged rational finite sum** satisfy the congruence if the hypothesis `p is prime` is erased while `q=6m+1` and `q mod 24 in {13,19}` remain? An affirmative algebraic identity over every integer m in those two classes could then eliminate the prime-specific work. We exhibit exact counterexamples in **both prescribed residue classes**.

For arbitrary integer m>=1, define, exactly as for the original source,
[
A_m=rac{(6m)!}{3^{6m}((2m)!)^3},quad R_{m,0}=1,quad
rac{R_{m,n+1}}{R_{m,n}}=
rac{(4m+2n+1)(3n+1)(3n+2)}
{36(n+1)(2m+n+1)(4m+n+1)},
]
[
S_m=A_msum_{n=0}^{4m}(6n+12m+1)R_{m,n}.
]
This rational expression exists without a primality hypothesis. Put `q=6m+1`, `D_m=S_m-q(4/3)^{q-1}`; interpret `D_m mod q^3` only when its reduced denominator is coprime to q. All instances below satisfy this condition; no nonunit modular inverse is used.

## 2. Counterexample theorem — actual original endpoint, same residue classes

**Theorem (exact finite, unconditional):** It is false that the original source sum satisfies `S_m ≡ q(4/3)^(q-1) (mod q²)` for every positive integer m with composite `q=6m+1≡13` or `19 (mod24)`. In particular, the stronger extension modulo q³ is also false.

The following table is computed directly as exact rational numbers, then reduced modulo q³. Every row was independently reconstructed via (i) the **unmodified source recurrence**, and (ii) its independently evaluated **factorial summand**
[
R_{m,n}=rac{(4m+2n)!((2m)!)^2(3n)!}
{216^n((2m+n)!)^2(4m+n)!(n!)^2},
]
whose identity follows from matching the n=0 term and consecutive rational ratios. The two full rational sums agree exactly, not just modulo q³.

| m | q (prime factors) | q mod 24 | S_m mod q³ | q(4/3)^(q−1) mod q³ | D_m mod q³ | D_m mod q² |
|---:|---|---:|---:|---:|---:|---:|
| 14 | 85=5·17 | 13 | 563125 | 95710 | 467415 | 5015 |
| 15 | 91=7·13 | 19 | 140777 | 74620 | 66157 | 8190 |
| 19 | 115=5·23 | 19 | 945875 | 505885 | 439990 | 3565 |
| 22 | 133=7·19 | 13 | 466431 | 786828 | 2032240 | 15694 |
| 31 | 187=11·17 | 19 | 5070505 | 1103487 | 3967018 | 15521 |

All modular rational operations are well-defined: `gcd(denominator(D_m),q)=1` for every row. For each displayed `q=ab`, with distinct prime factors a,b, exact rational valuation checks give
[
v_a(D_m)=v_b(D_m)=1.
]
Thus in every case q divides `D_m` but q² **does not**. This is stronger and sharper than merely displaying a nonzero residue modulo q³.

**Why the theorem follows:** One case in either class is enough to falsify the relevant universal extension. Here the two smallest in-class composites already give nonzero residues `D_14 mod85²=5015` and `D_15 mod91²=8190`. These are certified exact rational computations with separately verified definitions and denominators. The extra three witnesses are crosschecks, not a sample-to-theorem inference.

The separately checked prime-power/composite diagnostics `q=25,49,55` also fail the all-m q³ extension, but are not needed for the theorem and **are not within the target classes**; they carry no credit toward the original prime-only hard target.

## 3. Consequence for the still-open original proof

**Prime-specific arithmetic cannot simply be erased.** A putative *unconditional all-integer-m congruence* for the same full endpoint using only `q=6m+1` and its 13/19 residue class is contradicted by q=85 and q=91. This does not forbid rational WZ identities holding for all m; the exact full five-tail WZ identity does hold over Q. It rules out an unjustified universal congruence conclusion that does not use primality or a comparably restrictive additional hypothesis. Candidate prime-only proofs should retain their Fermat/Morley/Wilson/finite-field or same-class CM/divided-power inputs precisely where needed.

**Do not misinterpret:** The unchanged D25 target continues to quantify over prime p. No prime counterexample has been found. This theorem neither proves the prime case nor executes the Source-fixed native benchmark, and it does not establish the needed full congruence `E_m≡0 (mod p²)` of the existing combined LOW/Beta–WZ normalization.

**BRC/observer:** The carrier retains the original labeled n-summands, exact signed rational numerator/denominator, `m,q`, prime-factor-wise valuations and complete summation/terminal provenance. The declared observer is the `Z/q³Z` rational residue where all denominators are units. Compression to q-adic rank data is not performed. These are external arithmetic statements, not original X6/CM dynamics; P000 and ACTIVE residual fidelity remain fixed.

## 4. Actual execution, reproducibility and continuation

The companion `20261024_onhour_d25_original_target_classes_composite_parameter_obstruction_check.py` executes the two independent `Fraction` paths, exact denominator-gcd guards, all five named same-class witnesses, and per-prime valuation equality `v_a(D)=v_b(D)=1`. It also checks the separate q=25,49,55 examples. Local execution: **8/8 finite composite witnesses verified; each pair of paths agreed exactly**. No floating point, no replacement summation truncation, no unrun benchmark declared as passed.

**Highest scientific frontier:** preserve both target-prime third-digit LOW seed proofs, source-specified upper-half p³ WZ five-port transport, and the preceding 575-prime original check. This new theorem excludes one extension-based proof route; it does not replace these results. **Next exact positive mathematical unit:** prove or refute the original prime-only joint residual `E_m=Theta_m-G_m+pY_m ≡ 0 (mod p²)` for the two classes by a true prime-dependent CM/divided-power or original-source finite WZ normalization, retaining all LOW/HIGH and both seam/terminal ports. The genuine Source-fixed native benchmark remains `NOT_RUN`; Source Researcher authority, native session/CLAIM/open/checkpoint/Result and independent review remain outstanding. Existing onhour support issue `awdawmip/enterprise-math#1539` is the relevant control owner; nothing here borrows maintenance `chatgpt-hourly-enterprise-math-20260921` identity.

**Persistence/provenance:** neutral GitHub author evidence only (`UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT`), not a canonical task checkpoint. Preserve historical staging materials separately, do not replay unknown requests. No scheduler, notification, scientific Source pin, world definition or acceptance record is altered.
