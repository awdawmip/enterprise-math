# D25/LIFT: all-prime valuation walls and bounded character-law probe

Date: 2026-10-31 Asia/Hong_Kong. Author-side TASK_RESEARCH logical conversation chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**; P000 ACTIVE_LOCKED unchanged. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. External rational/p-adic arithmetic, not a P000 native X6 transfer.

## Theorem A — exact coefficient valuation, every prime p>=5

Define the ORIGINAL coefficient (no altered parameter or normalization)

\[
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
=\frac{(2n)!(3n)!}{(n!)^5\,216^n},\qquad 0\le n<p.
\]

For every prime p>=5,

\[
\boxed{v_p(a_n)=\lfloor 2n/p\rfloor+\lfloor3n/p\rfloor.}
\]

Proof: n<p implies v_p(n!)=0, while 2n<2p and 3n<3p imply v_p((2n)!)=floor(2n/p) and v_p((3n)!)=floor(3n/p). Since p>=5, 216 is a p-unit. Legendre's factorial formula proves the equality without any computational hypothesis. The three exact valuation walls occur at p/3, p/2 and 2p/3: valuations 0,1,2,3 on the corresponding successive half-open intervals.

For the actual weighted term (6n+1)a_n, there is exactly one index n_w with p|(6n_w+1):
- p=1(mod6): n_w=(p-1)/6; the weight is exactly p, on the valuation-zero band.
- p=5(mod6): n_w=(5p-1)/6; the weight is 5p, in the valuation-three tail. At p=5 alone, 5p=25 has *two* p-factors.

Keep this isolated weight, original coefficient, prime, band and valuation as distinct provenance-bearing variables. A weight-zero modulo p is not a zero of the unweighted coefficient.

## Theorem B — sharp full-polynomial initial prefix, every prime p>=5

Let q=floor(2p/3), W=1+6X d/dX, and F_p(X)=sum_{n=0}^{p-1}(6n+1)a_nX^n. Then

\[
\boxed{F_p(X)\equiv\sum_{n=0}^{q}(6n+1)a_nX^n\pmod{p^3}}
\]

coefficientwise in Z_(p)[X]. This q is **minimal among initial-prefix endpoints for the polynomial readout modulo p^3**.

Proof: at n=q, floor(2q/p)=floor(3q/p)=1 and p does not divide 6q+1, so its coefficient has valuation exactly 2 and cannot be omitted. At each n>=q+1, floor(2n/p)>=1 and floor(3n/p)>=2, giving v_p(a_n)>=3; multiplying by 6n+1 cannot decrease the valuation. There is no scalar X=1 non-cancellation claim here.

For p=6m+1 this recovers the previously proved GH-172 prefix q=4m; **new all-prime scope** is the p=5(mod6) class, its weight location, and the p=5 exception. At p=373, q=248 and 249 terms: reuse the earlier target-family result, do not re-claim its discovery.

## Bounded finite character-law exploration — NOT a theorem

At fixed original X=1 let A_p=F_p(1). The formal frozen D25 target is A_p ≡ p (mod p^3) only for p mod24 in {13,19}. A broader, deliberately **exploratory** signed hypothesis is

\[
\boxed{A_p\stackrel{?}{\equiv} (p/3)\,p\pmod{p^3}\quad \text{all primes }p\ge5,}
\]

where (p/3)=+1 for p=1(mod3) and -1 for p=2(mod3). This hypothesis is *not* promoted into the frozen task or claimed to be new prior art.

Actual exact Python standard-library certificate: sieve enumerated every one of the 1436 primes 5<=p<12000. By the p-unit recurrence a_(n+1)/a_n=(2n+1)(3n+1)(3n+2)/(36(n+1)^3), the sharp q-prefix computed A_p modulo p^3. **Zero counterexamples were found in that finite range**. Counts p mod24: 1:164, 5:185, 7:184, 11:181, 13:181, 17:177, 19:182, 23:182. Positive-character samples: 711; negative-character samples: 725. Frozen 13/19 classes total 363 (an extension of the previously recorded sample count below 5000, not a proof).

At 15 anchor primes p=5,7,11,13,17,19,23,31,37,43,67,73,97,157,373, independent full n=0..p-1 recurrence, integer binomial coefficient sum and exact factorial valuations agree with the reduced calculation. At p373, A_p ≡ 373 (mod 51895117), q=248. No floats, Lean, native H0/B0, divided-power or Frobenius computations. Actual marker:

    PASS_WEIGHTED_216_UNIFORM_STRATA_AND_CHARACTER_SCAN_EXACT

The accompanying .py is directly executable with Python standard library; its finite scan does NOT prove the conjecture. Theorems A and B have the finite factorial proof given above.

## Research provenance, next legal action and debts

Mother D25/LIFT/JT2 remains OPEN. Previous same-lane immutable sources: stratified coefficientwise p³ jet with exact source-labelled S+p(H+U)+p²(L-J+I), and two differential wall impulses; another Research lane's already established UR/E.2 first-digit bridge remains consumed, not re-proved. Existing higher-precision work and P000 Source pin remain intact.

The **smallest frozen unsolved mathematical obligation** is to prove the COMPLETE signed C+L-J+I=0 (mod p) for *all* p mod24={13,19}; seek a finite WZ, contiguous-relation or CM special-value certificate preserving the original 216 source, actual signed I, p²-carry and the two valuation walls. The exploratory p=5(mod6) negative branch is a discriminating external probe, not a change of formal scope. P000 native transfer/triadic geometry not claimed. Typed BRC observation (p,n,original216 coefficient, weighted operation W, v_p coefficient, v_p weight, wall, q, polynomial/scalar readout, modulus, Source pin) is only an external arithmetic information-fidelity result.

Native control: historical exact same-conversation recovery issue awdawmip/kimi-query-bridge#6424 and continuation #6425 reported execution_authorized=false, no winning current claim/open/run; protected prior staging preserved. Those reads are historical, **not** a newly verified current native status. Control support issue awdawmip/enterprise-math#1558 and native p373 H0/B0/semilinear-Frobenius experiment #1559 remain assigned. No new CLAIM, OPEN, native Source publish_checkpoint, formal activity registration, review or Result is asserted. The Git report is author-side portable evidence only. Source checkpoint and admission require new actual authorization, Source readback and independent review on the canonical path.

Next exact action: symbolic signed cancellation for the original frozen + branch; optionally search whether the ±(p/3) observation follows from a valid finite hypergeometric WZ certificate, keeping the proof obligations distinct. A next native Researcher resumes only with its genuine identity, current Source packet and legal winning claim; author-side artifacts must not be promoted to predecessor completed_units without authenticated native checkpoint evidence.
