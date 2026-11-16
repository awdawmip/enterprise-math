# X6 / LP019 — all-radius obstruction to pair-only quadratic-shell N-BRC (unit 60)

Date: 2026-11-16. Parent task `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable publication `TP2-B4A441B23DA3159232C2`. Ordinary Research lane `chatgpt-research-onhour-enterprise-math-20260923`, Researcher `EM-X6-FB6990`. **AUTHOR-PROVED mathematical reduction / AUTHOR-EXECUTED finite check / UNREVIEWED / NOT_ADMITTED**. This document is not a formal Result or independent Driver review.

## Source-frozen mathematical model

P000 V5, centered signed native Cell torsor `Z^6`, at exact commit `59538f585d037d09ef687b28715c4bc1a3f9fe03`; comparison pre-rebase `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. For a named signed native displacement `z`, define `G(z)=sum_i z_i^2`, `T(z)=sum_i |z_i|`, `s(z)=#{i:z_i != 0}`. Native primitive directions are exactly the signed coordinate-unit steps; a diagonal is a composite path, not a primitive axis. Its **positive natural N-BRC** shortest-path multiplicity is `N(z)=T(z)!/product_i |z_i|!`. Let `C_6(g)`, `M_6(g)` be the full signed endpoint count and N-BRC mass at fixed `G=g`; `C_{<=2}(g)`, `M_{<=2}(g)` sum only endpoints with at most two nonzero axes.

## Theorem A: sharp all-radius completeness criterion

For **every nonnegative integer g**,

`C_{<=2}(g)=C_6(g)` and `M_{<=2}(g)=M_6(g)` **if and only if** `g=0,1,2`.

Proof: Each nonzero integral coordinate has square at least 1, so `s(z)<=G(z)=g`. At g=0,1,2 every possible endpoint automatically has support at most 2. Conversely, for every `g>=3`, the **classical Lagrange four-square theorem** yields integers `a,b,c,d` with `g-2=a²+b²+c²+d²`. The six-axis integer vector `z=(1,1,a,b,c,d)` has native `G=g` and `s(z)>=3` because `g-2>=1`. It and its exact signed/axis permutations are omitted by the pair-only observer. Their natural N-BRC path multiplicities are strictly positive, so both omitted endpoint count and omitted BRC mass are positive. The argument is valid for all g, not only finite tested radii. It uses the named external four-square theorem as a *deductive premise*, not as a new Enterprise axiom; no claim of reproving the four-square theorem is made. □

If `lambda=(a_1,...,a_s)` is the multiset of nonzero magnitudes of this witness with positive multiplicities `m_b`, its exact signed six-axis permutation orbit contributes at least

`E(lambda)= [6!/(6-s)!] 2^s / prod_b m_b!` endpoints and

`E(lambda) (sum_i a_i)! / prod_i a_i!` natural paths

missing from a support<=2 observer. The witness construction proves a strictly positive **exact lower bound**, not a full-shell closed form for arbitrary g.

## Theorem B: exact pair-only shell existence test

For any integer `g>=0`, the pair-only signed shell is nonempty **if and only if** `g=a²+b²` for some nonnegative integers a,b. By the *classical Fermat two-square theorem*, for `g>0` this is equivalent to every prime `p=3 (mod 4)` having even exponent in g's prime factorization. Thus pair-only emptiness is an exact arithmetic membership criterion. In particular, **every g=3 (mod 4) has an empty pair-only shell** because integer squares modulo 4 are 0 or 1, so a sum of two squares cannot be 3 modulo 4. There are infinitely many such positive g, and all `g>=3` have a nonempty full six-axis shell by Theorem A. This does **not** claim the converse that every g≠3 mod4 has a pair-only representation.

## Actual finite regression

Ran the exact Python test `research_checks/X6_G_SHELL_INFINITE_SUPPORT_OBSTRUCTION_UNIT60_20261116.py` locally (exit code 0, `UNIT60_PASS 9998 7251 619`; local source SHA256 `64989541a422d4954c500dcc9a70e086a6dd8cd0e92591984055dbd4c42bc333`). It independently constructs four-square witnesses for each `g-2=1..9998` via sums of two square-pairs, verifies 9,998 full-X6 vectors and their support>=3, and checks the exact factorization two-square criterion against explicit pair enumeration for all `g=1..10000`. Outcomes: 7,251 positive radii have no support<=2 endpoint, 2,749 do, and 619 primes congruent 3 mod4 through 10,000 are all excluded as expected. The first 512 have 332 pair-empty radii, matching unit59's independent full 513-shell exact N-BRC certificate. Finite checks exercise implementations, **not** the proof of Lagrange/Fermat.

Examples of *provably missing signed-orbit* N-BRC mass (not entire shell mass): at `g=3`, `z=(1,1,0,0,0,1)`, exact orbit 160 endpoints, path mass 960; at `g=25`, `z=(1,1,1,2,3,3)`, orbit 3,840 endpoints, mass 2,128,896,000; at `g=512`, `z=(1,1,0,1,5,22)`, orbit 3,840 endpoints, mass 7,551,677,952,000; at `g=10000`, `z=(1,1,0,1,14,99)`, orbit 3,840 endpoints, mass 1,601,463,291,610,540,020,111,360,000.

## Research consequence, provenance and limits

Unit59 already checked all g=0..512 by independent full-shell algorithms (the 512-shell support loss); unit60 promotes the specific completeness obstruction to an **all-radius theorem**, leveraging external established integer-square theorems. This mathematically demonstrates why fixed two-generator R063 data cannot *by itself* determine full native six-axis quadratic/BRC shell mass, while preserving the legitimacy of the original R063 same-object experiment. It does not replace or rerun the already author-executed R063 Stage0 17 gates / 512 radii (unit50) or the original Helly test.

Complete old 28-LP source/consumer closure remains open. The purported **actual** historical erroneous singleton LP011 argmax and erroneous positive N-BRC signed-cancellation LP019 callsites are still `UNRESOLVED_PROVENANCE`: an exact counterexample to a type-unsafe transfer does not establish a historical code bug. Independent Driver `REQUEST_REVISION` review has not been performed and must remain independent from the contributing Researcher.

Evidence: [unit59 all-shell report](https://github.com/awdawmip/enterprise-math/blob/ad30516c1ddd04d0038c4c0d374895416271788a/research_notes/X6_G512_SUPPORT_COVERAGE_AND_BRC_CENSUS_UNIT59_20261116.md), [complete 513-shell certificate](https://github.com/awdawmip/enterprise-math/blob/4a49459178b7bb838f667e7a18e6abebcff36f5f/research_checks/X6_NATIVE_G_SHELL_SUPPORT_MASS_UNIT59_EXACT_513_SHELL_CERTIFICATE.json), and [unit60 exact executed checker](https://github.com/awdawmip/enterprise-math/blob/2b860013cff190115f2c07d914548afe318a9171/research_checks/X6_G_SHELL_INFINITE_SUPPORT_OBSTRUCTION_UNIT60_20261116.py). No mathematical admission is implied by preserving the source.
