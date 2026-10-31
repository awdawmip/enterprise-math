# D25 — first-jet-only finite reduction of the original signed second digit

Date: 2026-10-31. Status: AUTHOR-DERIVED / EXACT MODULAR CHECK EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Parent SECOND-DIGIT-LIFT remains OPEN. No Source-native CLAIM/run, official Result or native H0/B0 experiment is inferred.

## Consumed proofs and frozen objects

- Scientific Source pin remains c47e13e4aba0e006366f989d6334d443f6333ae3.
- Original p-local model A_p = sum_{n=0}^{p-1}(6n+1) binom(2n,n)^2 binom(3n,n)/216^n.
- Already established source-faithful Clausen four-source identity: research_notes/portable_direct/20261031_onhour_d25_clausen_jet_unique_overdegree_R.md at commit 3380c77a4d5c5556d7c63698c274e8a5f537aa55, Section 4.
- Newly proved finite rational Green evaluation and exact terminal first-jet identity: research_notes/portable_direct/20261031_onhour_d25_finite_rational_green_eval_terminal_punit.md at commit 2636521cfc0716ba23ace3ae14c1497cc56a058b.
- Original signed R_p is the frozen independent overdegree/reflector. The present construction never renames it as Green Phi or native Frobenius.

## Theorem — remove J2 from the remaining target congruence without erasing the signed boundary

Fix target prime p=6l+1 with p=13 or 19 (mod 24), M=3l. Define
\[
J_r(z)=\sum_{0\le n<p} [t^r]
\frac{(-l+t/6)_n(-2l+t/3)_n}{(n!)^2}z^n,\quad r=0,1,2,\qquad \theta=z\partial_z.
\]
Let u_i=[z^i]J0 and v_i=[z^i]J1, and put
\[
L_0=J_0(1/2)/p+J_1(1/2),\quad
N_0=[(1+12\theta)J_0]_{z=1/2},\quad
N_1=[(1+12\theta)J_1]_{z=1/2}.
\]
Existing first-digit UR and Clausen results give J0(1/2)=0 (mod p) and L0*N0=1 (mod p). The quotient below is therefore p-integral.

Define the wholly first-jet p-local unit and terminal readout:
\[
S_p=\sum_{i=0}^{l}u_i\binom{p-1+i}{3l},
\quad S_p=(-1)^l\pmod p,\quad
\Gamma_p=\frac{l\,u_l v_{2l}}{3S_p}.
\]
Define a finite polynomial with **no J2 coefficient input**:
\[
F_p(z)=J_0(z)\big[(\theta/2-2l/3)J_1(z)+J_0(z)/18-\Gamma_p z^{p-1}\big].
\]
Let f_k=[y^k]F_p(1-y), 0<=k<=7l. The previous exact residue theorem gives f_M=0, and define the finite p-local evaluation:
\[
E_p=\sum_{\substack{0\le k\le7l\\k\ne M}}
f_k\frac{1-2^{M-k}}{k-M}.
\]

**Exact remaining-second-digit reduction:**
\[
\boxed{\displaystyle
\frac{A_p-p}{p^2}\equiv
\underbrace{\frac{L_0N_0-1}{p}}_{\text{integer carry}}
+\underbrace{L_0N_1}_{\text{first-jet}}
-\underbrace{12\,2^{-M}E_p}_{\text{finite Green-derived lower second jet}}
-\underbrace{R_p}_{\text{independent original signed boundary}}
\pmod p.}
\]
This is a proved **all-target algebraic reduction conditional only on the previously proved first-digit/source-identity inputs**; it is NOT a proof that the right side vanishes for every target prime. In particular, it eliminates explicit dependence on J2 coefficients in the **remaining scalar second-digit interface**, not in other observers or native H0/B0 experiments.

### Proof

The exact finite Green theorem supplies
\[
\Phi(1/2)=E_p=2^M\big[J_0\theta J_2-J_2\theta J_0\big]_{1/2}.
\]
By the already established first-digit theorem for the stated target prime classes, J0(1/2)=0 (mod p). Therefore
\[
E_p\equiv-2^M J_2(1/2)\theta J_0(1/2)\pmod p.
\]
Since N0=J0+12theta J0, this implies the **signed target bridge**
\[
\boxed{J_2(1/2)N_0\equiv-12\,2^{-M}E_p\pmod p.}
\]
The previous original Clausen source identity already proved
\[
(A_p-p)/p^2\equiv(L0N0-1)/p+L0N1+J2(1/2)N0-R_p\pmod p.
\]
Insert the signed bridge. Finally, the exact residue/top-jet theorem gives gamma=Gamma_p because S_p is a unit. Hence E_p is constructed entirely from J0,J1 and finite p-local arithmetic. Every denominator (k-M) in E_p has absolute value <=4l<p, and p does not divide 2,3,6,18 or S_p. This completes the proof.

**Observer scope matters.** J0(1/2) vanishing is a target-class mod-p fact. Outside this class the dropped term J0(1/2)*theta J2 need not vanish, and the signed bridge is not asserted. Even for target primes, reconstructing this specific product J2*N0 modulo p does not reconstruct the complete second-jet polynomial or the native class. Phi is distinct from R: e.g. at 373, E_373=1, R_373=196 (mod 373).

## Exact executed original-source check

Executed two independent Python standard-library scripts on this run. The finite Green verifier tested every p=6l+1 in [7,500] (45 primes, modulo p²). The new source bridge verifier d25_first_jet_reduction_check_20261031.py checked **all 23 primes p=13,19 (mod24), p<=500**, using independent jets modulo p³, original integer-binomial A_p modulo p³, exact signed R double sum and finite Green E. It checked J0=0 (mod p), N0 unit, the signed bridge, the original Clausen four-source equality, and the new first-jet-only formula. All passed: PASS_D25_FIRST_JET_REDUCTION_ORIGINAL_216_EXACT.

Rows (p, integer carry, L0N1, original J2N0, finite -12*2^(-M)E, signed R, full residual), all entries mod p:
- (13,0,4,9,9,0,0)
- (19,16,4,11,11,12,0)
- (37,34,20,31,31,11,0)
- (67,41,20,27,27,21,0)
- (373,81,103,12,12,196,0).

The 373 nonzero branches make the original preservation obligation explicit: 81+103+12-196=0 mod373; using E=R or setting either nonzero term to zero is invalid. This computation is exact over p-local integer rings, not finite proof of the universal cancellation.

## Next unclosed scientific/operational unit

The full target A_p=p (mod p³) for every p=13,19 (mod24) remains **OPEN**. Next attempt a finite parameter-shift WZ/CM certificate directly for the first-jet-only four-source right side above, retaining the integer carry and signed R. A useful stronger subquestion is to factor the first-jet kernel E_p into a finite telescoping relation *with* R_p (not a direct equality of the two), checking 19,67,373. Avoid returning to disproved scalar Gosper-only or divergent formal series routes.

Separate native benchmark #1559, original fixed373 H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius/eta, signed odd Green/Hesse, kappa and independent replay remains **NOT_EXECUTED / PENDING_OWNER**. Only an authorized native original-class executor may satisfy it, with original scientific pin and benchmark conditions.

Source control handoff: Research logical lane chatgpt-research-onhour-enterprise-math-20260923. Recovery receipt awdawmip/kimi-query-bridge#6632 has session pointer but no own claim/run and source_authority_verified=false. Original dispatch #6633 ended FAILED UPSTREAM_CODE_REVIEW_REQUIRED. Do not resubmit that request, do not assume service ownership or use the maintenance ID chatgpt-hourly-enterprise-math-20260921. Three prior staging artifacts remain neutral, not Source-admitted. Research identity/activity registration remains pending; this author-side proof/code publication is neither Source checkpoint nor Result. Recurring task schedule/notifications not modified.
