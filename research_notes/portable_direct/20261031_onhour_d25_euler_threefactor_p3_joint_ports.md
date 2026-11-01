# D25: Euler–Clausen full three-factor valuation joint and five p² contacts

Date: 2026-10-31 Asia/Hong_Kong. AUTHOR-SIDE / PROVED ELEMENTARY SOURCE CLASSIFICATION / EXECUTED EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This does not certify native H0/B0, formal Source checkpoint, Result or independent review.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research conversation chatgpt-research-onhour-enterprise-math-20260923, never maintenance identity. P000 ACTIVE_LOCKED unchanged.

## 1. Original object and exact source identity

Use the existing classical Euler–Clausen rational coefficient identity, retaining its complete original indices:

\[
A_p=\sum_{j+k+\ell<p}(6(j+k+\ell)+1)2^{-j-k-\ell}e_jg_kh_\ell,
\]
\[
e_j=(-1)^j\binom{1/2}{j},\quad
g_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\quad
h_\ell=\frac{(5/6)_\ell(2/3)_\ell}{(\ell!)^2}.
\]

The frozen original target remains
\[
A_p=\sum_{n=0}^{p-1}\frac{6n+1}{216^n}\binom{2n}{n}^{2}\binom{3n}{n}
\stackrel{?}{\equiv}p\pmod{p^3},\quad p\equiv13,19\pmod{24}.
\]
The prior Euler study already identified the exceptional unit e_{(p+1)/2}. This increment classifies every simultaneous factor crossing, not a new Euler identity.

## 2. Exact factorial-crossing lemma

For a prime p≥5, 0≤N,n<p and α∈Z_p^×, let Φ_{N,α}(n)=(-N+pα)_n/n!.

For n≤N the following is an exact rational equality:
\[
\Phi_{N,\alpha}(n)=(-1)^n\binom Nn\prod_{r=N-n+1}^{N}(1-p\alpha/r).
\]
For N<n<p:
\[
\Phi_{N,\alpha}(n)
=p\alpha(-1)^N\frac{N!(n-N-1)!}{n!}
\prod_{r=1}^{N}(1-p\alpha/r)
\prod_{s=1}^{n-N-1}(1+p\alpha/s).
\]
Proof: partition the original ordered factors at their unique index t=N, factor negative integers -r before that index, pα at it, and positive integers s after it. All displayed residual factors are p-units, so v_p(Φ)=1_{n>N} exactly.

For p=6m+1, the equalities
\[
g_k=\Phi_{m,1/6}(k)\Phi_{2m,1/3}(k),\quad
h_\ell=\Phi_{5m,5/6}(\ell)\Phi_{4m,2/3}(\ell)
\]
imply, for all 0≤j,k,ℓ<p,
\[
v_p(g_k)=1_{k>m}+1_{k>2m},\quad
v_p(h_\ell)=1_{\ell>4m}+1_{\ell>5m},\quad
v_p(e_j)=1_{j>3m+1}.
\]
The last assertion uses the prior proved Euler exceptional coefficient lemma. These are valuations of original factors, not valuations of their cancelled sums; 6(j+k+ℓ)+1 may add p-divisibility.

## 3. Exactly eleven surviving source types

In the frozen classes p≥13, m≥2. Denote E-source L if j≤3m, X if j=3m+1, and U if j≥3m+2. E-factor valuations are 0,0,1 respectively. Denote G0/G1/G2 by k≤m, m<k≤2m, k>2m; H0/H1/H2 by ℓ≤4m, 4m<ℓ≤5m, ℓ>5m, with valuations 0/1/2.

The index bound j+k+ℓ≤6m and the need for factor valuation ≤2 yield exactly these eleven nonempty original source regions:

| E | G | H | factor valuation |
|---|---|---|---:|
| L | G0 | H0 | 0 |
| X | G0 | H0 | 0 |
| L | G1 | H0 | 1 |
| X | G1 | H0 | 1 |
| U | G0 | H0 | 1 |
| L | G0 | H1 | 1 |
| L | G2 | H0 | 2 |
| X | G2 | H0 | 2 |
| U | G1 | H0 | 2 |
| L | G1 | H1 | 2 |
| L | G0 | H2 | 2 |

Proof of completeness: the crossing thresholds are j_U≥3m+2, k_G1≥m+1, k_G2≥2m+1, ℓ_H1≥4m+1, ℓ_H2≥5m+1. U-H1, X-H1, G2-H1, G1-H2, X-H2 violate the n≤6m bound. U-G2-H0 has valuation 3, hence contributes zero modulo p³ where nonempty. The eleven retained regions each have threshold-index witnesses for every m≥2. All other combinations are excluded by these inequalities or valuation≥3.

Let S_{E,G,H} be the ORIGINAL weighted source sum over each such region, with 2^{-j-k-ℓ} and 6(j+k+ℓ)+1 intact. Then
\[
\boxed{A_p\equiv\sum_{\text{11 retained ports}}S_{E,G,H}\pmod{p^3}}
\]
for every p=6m+1≥13. Exactly FIVE potential valuation-two regions remain:
\[
\boxed{(L,G2,H0),\ (X,G2,H0),\ (U,G1,H0),\
       (L,G1,H1),\ (L,G0,H2).}
\]
These are distinct signed, source-labeled contacts. They need not vanish separately.

Let S_<2 be the six grade-0/1 regions and S_2 the five grade-2 regions. Always A_p≡S_<2+S_2 mod p³, with S_2∈p²Z_p. WHEN the independently established first-digit prerequisite A_p≡p mod p² applies, the original LIFT is equivalent to the single signed joint identity
\[
\boxed{(S_{<2}-p)/p^2
 +\sum_{\text{five grade-2 ports}}S_{E,G,H}/p^2\equiv0\pmod p.}
\]
This is an exact source-preserving proof obligation, NOT its universal proof. It is stronger than a crude split into three Euler-j regions: the H1/H2 partner crossings and the exceptional X-G2 contact cannot be erased.

## 4. Executed integer certificates

Actually executed Python standard library code d25_euler_joint_threefactor_guard_20261031.py. It checked all 80 primes 7≤p<1000, p≡1 mod6, including 45 frozen-class primes. For every p it independently compared (i) original 216 Pochhammer recurrence, (ii) integer binomial formula, and (iii) original fully weighted e*g*h triple-source convolution mod p³; checked all factor valuations, exact eleven-port reconstruction and grade divisibility. All 45 frozen-class samples satisfy A_p≡p mod p³; this finite observation is NOT an infinite-prime proof.

Selected grade-two contributions divided by p², in F_p:

| port | p=13 | p=19 | p=373 |
|---|---:|---:|---:|
| L/G2/H0 | 9 | 11 | 76 |
| X/G2/H0 | 2 | 5 | 111 |
| U/G1/H0 | 9 | 6 | 246 |
| L/G1/H1 | 11 | 18 | 315 |
| L/G0/H2 | 3 | 18 | 36 |
| Total grade two | 8 | 1 | 38 |
| (S_<2-p)/p² | 5 | 18 | 335 |
| Total mod p | 0 | 0 | 0 |

At p=373, every one of the five grade-two sources is nonzero, their total 784≡38 and 335+38≡0 mod373. This gives a discriminating original-source counterexample to any cancellation proof that deletes each valuation-two port independently.

## 5. Typed BRC reuse; honest next dependency

BRC COMPOSE_APPLIED. Source carrier = original (j,k,ℓ), e/g/h signed rational coefficient, original weight, p-valuation and port ID. Observer = A_p mod p³; future allowed operations include per-port WZ pairing and second-digit extraction. The quotient dropping grade≥3 is proven safe only for this Z/p³-linear readout, not for operations involving division by p³, native Frobenius or hidden source-sensitive observables. Cauchy indices are external combinatorial labels, not native Enterprise X6 axes or a native H0/B0 surrogate.

Next exact mathematical unit: produce one WZ/CM certificate for the displayed six-plus-five joint residual in both frozen p classes, using all five concrete p² contacts; do not replace the target with an equivalent Hensel-root formula or assume individual sources vanish.

Higher-priority native issue awdawmip/enterprise-math#1559 remains the original fixed p=373 H0/B0 divided-power [X]U mod 139129, actual module rank, genuine semilinear Frobenius/η, signed odd Green/Hesse, κ, Δ_p-R_p and independent reproduction. As observed in this run it was OPEN with no confirmed executor. Its responsible path is the authorized canonical owner or native evaluator, and acceptance requires actual native reproducible data. This external Euler arithmetic does not fulfill the experiment.

Control: own recovery_status research-onhour-20261031-0202-recovery-r15 via awdawmip/kimi-query-bridge#6632 succeeded; it reports a local active Researcher session, no own run/open claim and source_authority_verified=false. Preserved old staging SD-d7c23e7984c2ddaac60a stays NEUTRAL. Fresh canonical dispatch research-onhour-20261031-0205-dispatch-r15 via bridge #6633 returned FAILED / UPSTREAM_CODE_REVIEW_REQUIRED, naming five control-plane Python modules. This is NOT NO_DISPATCH. Site auth reports research_authority_granted=false/write_relay_enabled=false. An authorized maintainer must complete real code review and deployment, after which this lane can perform fresh Source recovery/dispatch. No formal CLAIM, checkpoint, Result or review is asserted by this author-side Git publication.
