# D25 — Exact W216 grade-1/grade-2 reflected reciprocity and one-carrier second-digit certificate

Date: 2026-11-09 (Asia/Hong_Kong). Classification: TASK_RESEARCH / AUTHOR_SIDE_ALL_PRIME_PROOF / EXACT_18_PRIME_REGRESSION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Immutable scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical research lane: `chatgpt-research-onhour-enterprise-math-20260923`. The separate maintenance conversation is not used. This is an author-side mathematical result, not a claim to a Source session/CLAIM, Result, review, or native H0/B0 experiment.

## 1. Exact new mirror theorem

For every prime `p=6m+1>3` define the *original* W216 coefficient

[
A_n=rac{inom{2n}{n}^2inom{3n}{n}}{216^n}
=rac{(2n)!(3n)!}{(n!)^5,216^n}.
]

For each `q` in `2m+1 \le q\le 3m`, the valuation of `A_q` is exactly one, and the valuation of `A_{p-q}` is exactly two (since all denominators are p-units). Set

[
a_q=(A_q/p)mod p,qquad b_{p-q}=(A_{p-q}/p^2)mod p.
]

Then both are nonzero elements of `F_p`, and **the following universal reflected-grade identity holds**:

[
oxed{a_q,b_{p-q}equiv (36q^3)^{-1}pmod p.}	ag{M1}
]

Consequently the original signed grade-2 tail, with precisely its original weights and cutoff,

[
T_{2,p}=sum_{n=3m+1}^{4m}(6n+1)A_n
]

is recovered entirely from the original grade-1 leading coefficients:

[
oxed{rac{T_{2,p}}{p^2}equiv
sum_{q=2m+1}^{3m}
rac{1-6q}{36q^3,a_q}pmod p.}	ag{M2}
]

This is an *exact cross-grade coupling*; it does not assert either grade separately vanishes. Every division in (M1)-(M2) is by a proven unit.

### Proof of (M1)

For integers `p\le r<2p`, Wilson's theorem gives `r!/p\equiv-(r-p)!\pmod p`. Write `n=p-q`; under the displayed range, `2q<p<3q<2p` and `p<2n<3n<2p`. Therefore

[
a_qequiv-
rac{(2q)!(3q-p)!}{(q!)^5 216^q},qquad
b_nequiv
rac{(p-2q)!(2p-3q)!}{(n!)^5 216^{p-q}}pmod p.
]

For every `1\le x<p`, the elementary reflection of Wilson's theorem is

[
x!(p-x)!equiv(-1)^x xpmod p.
]

Apply it to `x=2q`, `x=3q-p`, and `x=q`, noting `216^p\equiv216\pmod p`:

[
a_qb_{p-q}equiv-
rac{(2q)(3q-p)(-1)^{3q-p}}
{q^5(-1)^{5q}216^p}
equiv rac{6q^2}{216q^5}
=rac1{36q^3}pmod p.
]

The intermediate sign is positive because `3q-p-5q=-2q-p` is odd. This proves (M1). The change of variables `n=p-q` and `6(p-q)+1\equiv1-6q\pmod p` proves (M2). The proof is exact for every prime in the stated residue class, independently of numerical examples.

## 2. One-source-family reflection and exact reduced LIFT observer

Reuse, without reproving, the earlier grade-1 coefficient family

[
U_j=rac{(7/6)_j(1)_j(4/3)_j}{2^j(5/3)_j^3},
quad j=0,ldots,m-1,
quad K_1=A_{2m+1}/pmod p^2.
]

Its proven first-jet relation gives `a_{2m+1+j}=(K_1mod p)U_j\pmod p`. Substituting in (M2) eliminates the previously separate grade-2 coefficient family and its normalization from the remaining cancellation equation:

[
oxed{mathcal M_p=
sum_{j=0}^{m-1}
rac{1-6(2m+1+j)}
{36(2m+1+j)^3 (K_1mod p),U_j}pmod p
=rac{T_{2,p}}{p^2}pmod p.}	ag{M3}
]

For the *frozen target* primes `p\equiv13,19\pmod{24}`, the already consumed first-digit theorem and the existing grade-1 first-jet certificate imply that

[
B_p=rac{W_{0,p}-V_{mathrm{half},p}+pK_1S_0}{p^2}pmod p
]

is well-defined and, writing `S_1` for the previously derived first harmonic jet,

[
oxed{widehatTheta_p=
B_p+(K_1mod p)S_1+mathcal M_pequiv0pmod p
iff W_pequiv V_ppmod{p^3}.}	ag{M4}
]

The previous Source crosswalk supplies the *equivalence of vanishing* with the frozen `Delta_p-R_p` question; it does **not** assert numerical equality of those two observer values absent a comparison map. The all-target vanishing of (M4) remains unproved. (M3) is new: the grade-2 correction is now a reversed/inverted view of the same p-unit grade-1 carrier used to compute `S_0,S_1`. The indexed source labels `q\leftrightarrow p-q`, p-adic valuations and original signs are retained. BRC classification: `COMPOSE_APPLIED / REUSE_APPLIED`, not a name-only analogy.

Equivalently, if `V_r=(1)_r(5/6)_r(7/6)_r/[2^r(3/2)_r^3]` denotes the earlier *separately proven* grade-2 family with `K_2=A_{3m+1}/p^2mod p`, then `(K_1mod p)K_2 U_jV_{m-1-j}=(36(2m+1+j)^3)^{-1}` exactly modulo p. This is a direct mirror identification rather than another independent auxiliary model.

## 3. Actual exact experiments and p=373 witness

The attached standard-library Python checker evaluates the original *integer-binomial* coefficients modulo `p^2,p^3`, independently generates both hypergeometric `U,V` recurrence families, and checks (M1) for **all 332 reflected pairs** across the 18 primes

`7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373`.

All exact pair and summed-tail checks passed. Independent first-jet integration further checked the existing `B_p+jet_p+mirror_p=0` residue for all 18 primes; this is a finite regression, **not** a proof of universal (M4) vanishing.

At `p=373,m=62`: `K_1 modp=320`, `K_2=290`, 62 mirror pairs. The first pair is `q=125\leftrightarrow n=248`, with `a_{125}=320`, `b_{248}=181`, and `320*181=105=(36*125^3)^{-1} mod373`. The reflected sum gives `\mathcal M_{373}=266`, independently matching the previously computed `K_2S_2=266`. The full source-labelled observer remains

[
B_{373}+mathrm{jet}_{373}+mathcal M_{373}
=190+290+266=746equiv0pmod{373}.
]

Thus the new mirror law is genuinely used by the live residual, not merely noted as a side lemma.

## 4. Strict scope and next action

The original p=373 same-class native H0/B0 divided-power `[X]U mod139129` is **NOT_EXECUTED**. Issue #1559 remains the existing support path, not a newly dispatched Task. Its unknown evaluator/owner must be resolved through current Source; native rank, semilinear direction/eta, signed Green/Hesse kappa and original Delta-R remain independent acceptance conditions. Do not substitute this reflected scalar result for the native benchmark.

Next executable mathematical unit: seek a finite-field creative-telescoping or modular-curve transfer directly for the **coupled one-family** (M4), retaining `B`'s grade-0 minus Vhalf source and the first jet. Inspect whether the inverted mirror summand is a legitimate telescoping certificate in combination with the signed `B+jet` kernel; a termwise grade cancellation is already disproved at p373. Retain the original frozen science/source pins and all prior completed units, with no retroactive admission.

Authority: author-side only; Source native checkpoint not written while this lane has no recovered private session capability or verified winning claim. No effect on P000, worldview, accepted D24 RR/DR or scheduler.
