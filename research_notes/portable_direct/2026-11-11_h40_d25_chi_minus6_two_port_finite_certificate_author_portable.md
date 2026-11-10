# D25/LIFT — Legendre (-6/p) two-port split: exact 3243-prime certificate

2026-11-11, TASK_RESEARCH portable author evidence. Status: **EXACT_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED**. No native H0/B0 computation, Source CLAIM, Result, checkpoint or independent review is asserted.

**Mother objective:** ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN). **Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific pin:** awdawmip/enterprise-math@c47e13e4aba0e006366f989d6334d443f6333ae3. Reuses the *existing* 2026-11-11 finite Clausen square-root normal form at research_notes/portable_direct/2026-11-11_h40_d25_clausen_square_root_normal_form_author_portable.md (blob afa8ee5512739f302916b5e9d5909ba2c04c184c); no repeat authorship for that lemma.

## Precise finite result

For each prime p>=5 let m=floor(p/6), epsilon=(p-1-6m)/4 in {0,1}. Define in F_p[X]:

`K_p(X)=sum_{k=0}^m binom(m,k)binom(2m+epsilon,k)X^k`.

Write `A_p=K_p(1/2)`, `B_p=(1-6epsilon)K_p(1/2)+6K'_p(1/2)`, and `chi_p=(-6|p)`.

**Exact exhaustive finite theorem:** for *all 3243 primes 5<=p<=30000*, the following classification holds, with no exceptions:

- If chi_p=-1, then A_p=0 and B_p!=0 (1633 primes).
- If chi_p=+1, then B_p=0 and A_p!=0 (1610 primes).

The 24-residue count certificate is:

| p mod 24 | 1 | 5 | 7 | 11 | 13 | 17 | 19 | 23 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| B_p=0 |385|408|410|407|0|0|0|0|
| A_p=0 |0|0|0|0|407|411|408|407|

Witnesses, listing (p,A_p,B_p): (7,2,0), (13,0,6), (19,0,12), (29,25,0), (157,0,80), (373,0,171), (10007,0,1610), (10009,194,0).

**Separately proved universal selector identity:** for every prime p>=5, `(-6|p)=(-1)^floor(m/2)`. The supplementary quadratic-reciprocity laws give signs + on p mod 24 in {1,5,7,11}, and - on {13,17,19,23}; equivalently m mod 4 in {0,1} and {2,3} respectively. This character identity holds for all primes. Its prediction of the *polynomial factor that vanishes* has the certified finite range above and is an all-prime proof target, not an established universal theorem.

## Exact computation / two independent field algorithms

One verifier enumerated every prime through 30000 with an integer Eratosthenes sieve, evaluated K and its derivative via the coefficient ratio `t_{k+1}=t_k(m-k)(2m+epsilon-k)/(2(k+1)^2)`, and computed the character via Euler's criterion. An independent verifier recalculated each of the 3243 pairs by modular factorial and inverse-factorial binomial coefficients, with 6486 exact equalities passing, zero double zeros, zero neither-zero cases, and zero character mismatches. The complete prime-by-prime certificate and both Python programs are in the accompanying author-side ZIP, SHA-256 `90c4d22c9b388e53d479c8bc59b72c2b74c4794a0db55566ac7291ff64e4b5ba`.

The previously published BRC two-port law is `W_p=2^(-epsilon)A_p B_p (mod p)` and K_p is squarefree. The present finite certificate adds a *discriminating branch selector*. The epsilon/chi(-3) coordinate alone loses the branch: p=7 and p=19 both have epsilon=0 but different vanishing ports. Retaining the extra m mod 4 (equivalently chi(-6|p)) is sufficient over the certified population. It is a typed source/observer statement, not native crystalline Frobenius.

## Next scientific unit and Source recovery

Seek an all-prime proof (or counterexample) for the character-controlled port split using finite-field character sums, transformation identities or a CM representation; then lift the observer factorization towards p^3 without erasing the epsilon/Frobenius endpoint twist. The original Task still requires authenticated original-class H0/B0 divided-power module, [X]U mod p², semilinear rank and normalization, and native kappa/Delta-R mapping. Current conversation did not obtain a live own session/winning CLAIM (latest recovery_status error: SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED); this author evidence is **not** predecessor completed research under a CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS seed.

The historical four-file UR V2 bundle still requires **original 94687 bytes** and exact SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; its completed mathematics was not redone. This note is an author-side staging/provenance locator pending legal native checkpoint.

Background identities: NIST DLMF §16.12.2 (https://dlmf.nist.gov/16.12.E2). Related finite-hypergeometric character-sum literature: Z.-H. Sun, *Acta Arith.* 159 (2013), 169–200, DOI 10.4064/aa159-2-6. No exact prior-art novelty certification is claimed.
