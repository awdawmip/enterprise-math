# D25 — second Gauss jet and signed three-shell continuation

2026-11-06 · TASK_RESEARCH author-side mathematical note, EXACT ALGEBRA / FINITE CHECKED / UNREVIEWED / NOT_ADMITTED. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3; publication TP2-B6F4FC938FF94941C1B7; Research-lane conversation chatgpt-research-onhour-enterprise-math-20260923. The native p=373 H0/B0 benchmark #1559 remains a separate pending task.

## Statement for every prime p=6m+1>3

Let d_n=(1/6)_n(1/3)_n/[2^n(n!)²], S=Σ_{0≤n<p}d_n, T=Σ nd_n, K=S+12T. Let u²=1/2, P=P_{2m}(u)=Σ_{n=0}^m e_n, e_n=(-m)_n(m+1/2)_n/[2^n(n!)²], and O=P_{2m-1}(u)/u. These polynomial expressions are rational and independent of the sign of u.

For 0≤n≤m, define f_n=binom(m,n)binom(2m,n)/2^n, A_n=H_m−H_{m−n}, B_n=H_{2m}−H_{2m−n}, A'_n=H_m^(2)−H_{m−n}^(2), B'_n=H_{2m}^(2)−H_{2m−n}^(2). For m<n≤2m define

b_n=(-1)^(m+n) m!(2m)!(n−m−1)!/[6(2m−n)! 2^n(n!)²],

D_n=(H_{n−m−1}−H_m)/6−(H_{2m}−H_{2m−n})/3.

For 2m<n<p define

c_n=(-1)^m m!(2m)!(n−m−1)!(n−2m−1)!/[18·2^n(n!)²].

All denominators are p-adic units in their specified ranges. Put

C1=Σ_{0≤n≤m}f_n(B_n−A_n)/6+Σ_{m<n≤2m}b_n,

C2=Σ_{0≤n≤m}f_n(A_n²+4A_n B_n−5B_n²−A'_n+5B'_n)/72+Σ_{m<n≤2m}b_nD_n+Σ_{2m<n<p}c_n,

D1=Σ_{0≤n≤m}(1+12n)f_n(B_n−A_n)/6+Σ_{m<n≤2m}(1+12n)b_n.

**New proven finite congruences:**

(1) S ≡ P+p C1+p² C2 (mod p³).

(2) K ≡ (2p−1)P−2(p−1)O+p D1 (mod p²).

Evaluation precision: C1 mod p², C2 mod p, D1 mod p.

## Proof

Use 1/6=−m+p/6, 1/3=−2m+p/3, m+1/2=−2m+p/2. For n≤m, expand each numerator unit with ∏(1−p x_j)=1−pΣx_j+(p²/2)[(Σx_j)²−Σx_j²] mod p³. Comparing the Gauss and terminating Legendre summands produces the first-order difference p f_n(B_n−A_n)/6 and the quadratic difference p² f_n(A_n²+4A_nB_n−5B_n²−A'_n+5B'_n)/72.

For m<n≤2m, precisely one numerator factor j=m is p-divisible; after deleting it, the remaining two progressions give d_n/p ≡ b_n(1+pD_n) mod p². For 2m<n<p, both j=m and j=2m contribute p; their remaining factorial products yield d_n/p² ≡ c_n mod p. These three disjoint index ranges prove (1). Weighting the first-order comparison by 1+12n yields K−Σ(1+12n)e_n≡pD1 mod p². Finally the exact Legendre derivative identity (1−u²)P'_{2m}=2m(P_{2m−1}−uP_{2m}) at u²=1/2 implies Σ n e_n=m(P−O), so Σ(1+12n)e_n=(2p−1)P−2(p−1)O, proving (2).

## Direct D25 target reduction and precision result

Under p|P (existing CM(-24) source theorem on p≡13,19 mod24, retaining its own unreviewed provenance), p|S and

S/p ≡ P/p+C1+pC2 (mod p²).

Let K0=(2p−1)P−2(p−1)O. Consuming the previously checked SIGNED Clausen triangle W≡S K−2p² J mod p³, the OPEN W≡p mod p³ objective becomes the exact single congruence

**(P/p+C1+pC2)(K0+pD1) ≡ 1+2p J (mod p²).**

This keeps the nonzero triangular truncation J and all three valuation bands. In particular the earlier first-jet statement S mod p² only supplies S/p mod p; the missing next digit is the explicit C2 term, including the double-p-factor upper band. The formula is a STRICTLY FINER observer interface, not a universal proof of the final cancellation.

## Executed checks (stdlib modular exact integers)

The checked program computes the original Gauss recurrence independently, Legendre coefficients independently, each of the three p-adic valuation bands by factorial/harmonic arithmetic, K from an independent Legendre three-term recurrence, and the original W using factorials. All 80 primes 7≤p≤997, p≡1 mod6 pass both new congruences; the 45 target primes additionally pass the signed triangle W comparison and full target congruence. Examples list P,S,K mod p³, C1,D1 mod p², C2,J mod p:

p=13: P=1716, C1=152, C2=10, S=988, K=1670, D1=52, J=0, W=13;
p=19: P=4769, C1=99, C2=5, S=1596, K=4382, D1=293, J=6, W=19;
p=67: P=271216, C1=3718, C2=32, S=62444, K=176556, D1=278, J=44, W=67;
p=373: P=44816696, C1=131274, C2=248, S=24495656, K=4236705, D1=57045, J=98, W=373.

Finite confirmation does not confer an all-prime proof or independent review. Script: d25_gauss_second_jet_20261106.py (same commit). Next: seek a global modular/Jacobi or multi-channel telescoper identity for (P/p+C1+pC2)(K0+pD1)−1−2pJ, keeping p=19 and 373 nonzero J as signed test cases. Native p373 original divided-power, Frobenius and κ remain PENDING_OWNER in #1559. Formal Source CLAIM/run/Result not asserted by this author-side publication.


## Next completed science unit: four-source divided residual (2026-11-06, exact corollary)

Assume the original first-digit input W≡p (mod p²), the already-stated p|P, and the signed Clausen relation. Define A=P/p+C1 (mod p²) and B=K0=(2p−1)P−2(p−1)O (mod p²). The first-digit identity supplies AB≡1 (mod p). Hence the following is **an exact equality of residue observers**, not merely a guessed cancellation:

**(W−p)/p² ≡ (AB−1)/p + B C2 + A D1 − 2J (mod p).**

Proof: from the two new jet statements, S≡p(A+pC2) (mod p³) and K≡B+pD1 (mod p²). Multiply, retain terms through p², insert W≡SK−2p²J, subtract p and divide by p². This is legal because AB−1 is p-divisible. Under the frozen scalar bridge (W−p)/p²≡Δ_p−R_p (mod p), the right side is a **four-source explicit model of the actual mother residual**, with individually identified original index/operation provenance.

Independent target-prime exact checks with the attached modular script cover all 45 p≡13,19(mod24), p≤997. Table entries are respectively ((AB−1)/p, BC2, AD1, −2J) in F_p:

- p13: (5,8,0,0); sum 0.
- p19: (2,3,7,7); sum 0.
- p67: (64,17,7,46); sum 0.
- p373: (140,259,170,177); sum 0.
- p997: (802,189,632,371); sum 0.

At p=19 all four terms are nonzero. Therefore, omitting any one channel **without changing the definitions of the others** fails even at this single target prime. This is a scoped exclusion of a specific shortcut; it makes no claim that other reorganizations are impossible.

The remaining uniform proof question is now exactly the mod-p four-channel cancellation, while the separately required native H0/B0 p373 experiment stays PENDING_OWNER. Author-side algebra and finite checks only; no formal Source Result or independent review.
