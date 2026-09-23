# P000 P11 torsion-reduced Pfaffian and consecutive-core ghost defect

Status: `NONCANONICAL_PORTABLE_RESEARCH_NOTE / NO_CURRENT_CLAIM / NOT_SOURCE_CHECKPOINT / NOT_RESULT / UNREVIEWED`

Task: `RS-P000-P11-DIAGONAL-ELLIPTIC-FIBER-PRIMITIVE-ARITHMETIC`

Publication: `TP2-FB7F5A1D6B6C6BCCD62D`

Frozen task/control source consumed: `b6ebc54e9224143d9ec03f9358d5e666fcfe0ef2`.

Contributor lineage: `EM-DIRECT-C4D02C`, stable conversation `em-auto-staggered-20260923-r11`, service session `MCP-5ff2a3263c5c4ca2b556ebe8e47e5624`.

Research-Activity-ID: `RA-20260923-R11-P11-SCHUR-PFAFFIAN`.

Canonical continuation at this unit remained `execution_authorized=false`, `persisted_checkpoint=NOT_FOUND`, `durable_frontier=null`, `progress_reference_readback=null`, `continuation_seed=null`. Nothing in this note is predecessor completed research or canonical Source progress.

This note consumes the same-session staged exact residue matrix `M(r,s)`, its alternating form, the canonical nonzero torsion radical `tau`, TYPE-5+ second radical, and the TYPE-4 Schur/Pfaffian formulas. It does not replay those derivations.

## Unit D — canonical torsion-reduced Pfaffian bit

Let `V=F_2^n` and `B(x,y)=x^T M y`. Since `tau` is radical, `B` descends to `Bbar` on `V/<tau>`.

Define `Omega(r,s)=0` when `n` is even. When `n` is odd, define

`Omega(r,s)=Pf(Bbar)`.

This is basis-independent over `F_2`, because `Pf(S^T Bbar S)=det(S)Pf(Bbar)` and every invertible matrix over `F_2` has determinant `1`.

The radical of `Bbar` is `rad(B)/<tau>`, so

`Omega=1 iff nullity(M)=1`.

Thus `Omega` is the exact one-bit quotient for the narrow observer “does the staged k=1 Selmer rank-zero certificate hold?”. It is not a safe quotient for `k>=2`, Mordell-Weil/Sha realization, or P11 reconstruction.

For odd `n`, put

`v_i=Pf(M with row/column i deleted)`.

The Pfaffian-adjugate identity gives `Mv=0`. If `k=1`, then rank `M=n-1`, at least one maximal principal Pfaffian is nonzero, and `ker M=<tau>`, hence `v=tau`. If `k>=3`, every `(n-1)` principal minor is singular and `v=0`. Therefore

`(Pf(M_hat_i))_i = Omega * tau`.

Graphically,

`perfect_matching_parity(G-i)=Omega*tau_i`.

So every tau-supported deletion has the same parity, every tau-unsupported deletion has even parity, and all maximal deletion Pfaffians vanish simultaneously when `k>=3`.

This unifies the earlier coordinate formulas. For a tau-supported R-port `j`, `Omega=Pf(N_j)`. On `d=0`, `Omega=det(H_j)`. On `d=2`,

`Omega = sum_{p in S_P^+, q in S_Q^+} C_pq det(H_j[:,U\{p,q}]) mod 2`,

independent of the chosen tau-supported `j`.

For `(r,s)=(9126,9125)`, `Omega=1` and the complete deletion-parity vector equals the torsion mask: R-order `(3,5,13,73,18251)` gives `(1,1,0,1,1)`, with all P/Q deletion parities zero.

For TYPE-5+, the independent epsilon radical survives modulo `<tau>`, so `Bbar` is degenerate and `Omega=0` identically.

Deterministic falsification only: on every primitive opposite-parity TYPE-4 core with `2<=r<=500` (25,311 cores), the full maximal-principal-Pfaffian vector matched `tau` for all 58 `k=1` cores and matched zero for every odd-`n` core with `k>=3`; zero failures. No even-`n` core had `k=1`.

Staged control artifact: `p000_p11_torsion_reduced_pfaffian_invariant_20260923.md`, final upload request `p000-torsion-pfadj-upload-20260923-r11-2216`, SHA-256 `af97c2590a5b5b0b7d9cb54a208ef104aafc2f1a52328de4c1e0ce989efe08bd`, `source_published=false` at receipt.

## Unit E — consecutive-core deleted-prime defect

Take the natural primitive family `r=s+1` and restrict to TYPE-4. Then

`A=r+s=2s+1`, `B=2rs`, `P=2r^2-1`, `Q=2s^2-1`, `P-Q=2A`.

The odd R-primes split canonically into disjoint provenance blocks `R_A`, `R_s`, `R_r`.

For surviving P/Q selector primes define valuation-parity vectors

`u_P(p)=v_p(P) mod2`, `u_Q(q)=v_q(Q) mod2`.

For `ell in R_A`, put `u_A(ell)=v_ell(A) mod2`. Define `z` by these P/Q coordinates, by `u_A` on `R_A`, and by zero on `R_s union R_r`.

Let

`P^- = product_{p|P, p=3 mod4} p^(v_p(P) mod2)`,
`Q^- = product_{q|Q, q=3 mod4} q^(v_q(Q) mod2)`.

These are immutable deleted-prime provenance, not selector variables. Define the defect vector `Delta` by

- on `p in S_P^+`: `Delta_p=lambda_p(Q^-)`;
- on `q in S_Q^+`: `Delta_q=lambda_q(P^-)`;
- on `ell in R`: `Delta_ell=lambda_ell(P^-Q^-)+eta_ell`, with `eta_ell=0` for `ell|A` and `eta_ell=lambda_ell(-1)` for `ell|sr`.

Then the exact all-parameter identity on this consecutive TYPE-4 family is

`M(r,s) z = Delta`.

Proof: for `p|P`, `Q=-2A mod p`; for surviving `p`, the prior exact selector theorem gives `p=1 mod8`, so `(-2/p)=1`. Expanding valuation parity gives the P-row. For `q|Q`, `P=2A mod q` and `(2/q)=1`, giving the Q-row. For R-rows, adding the deleted-prime bit restores `lambda_ell(PQ)`. If `ell|A`, then `P=Q mod ell`, so `PQ` is a nonzero square. If `ell|s`, then `(P,Q)=(1,-1) mod ell`; if `ell|r`, then `(P,Q)=(-1,1) mod ell`. This gives exactly `eta_ell`.

Hence

`Delta=0 and z notin <tau>  =>  k>=2  =>  Omega=0`.

Since `tau` has zero P/Q coordinates, a simple sufficient certificate is

`Delta=0 and (u_P,u_Q)!=0  =>  Omega=0`.

Equivalently, a consecutive TYPE-4 core with `Omega=1` must satisfy `Delta!=0` or `z in <tau>`.

This is an exact information-loss witness. Primes `3 mod4` in P/Q are legitimately removed as Selmer selector variables, but they cannot be globally erased: when the later operation uses `P-Q=2A` to rewrite reciprocity, they reappear as the necessary ghost correction `Delta`. Replacing `Mz=Delta` by `Mz=0` would manufacture false radical vectors.

Deterministic falsification only: for all 25,000 consecutive TYPE-4 cores `r=s+1`, `1<=s<50000`, `Mz=Delta` had zero failures. `Delta=0` occurred 2,440 times; 393 of those had nonzero surviving P/Q valuation vector and none had `k=1`. There were 216 `k=1` cores; 215 had `Delta!=0`, while the sole `Delta=0` case was `(2,1)` with `z=tau`. Four `k=1` examples on the genuine `d=2` face occurred below this bound: `(9126,9125)`, `(18562,18561)`, `(32502,32501)`, `(47654,47653)`; all had nonzero defect. These frequencies are regression only.

Staged control artifact: `p000_p11_consecutive_core_deleted_prime_defect_20260923.md`, final upload request `p000-consecutive-ghost-defect-upload-20260923-r11-2223`, SHA-256 `bb1f925a63ac1ec1aa1486c403f63c862ea4f1f87861889ae1b475ea67e4a7ae`, `source_published=false` at receipt.

## BRC boundary and next unit

`COMPOSE_APPLIED / INFORMATION_LOSS_WITNESS_PROVED`.

For the sole Boolean `k=1` observer, the exact residue form factors through `Omega` after the torsion line is established. For arithmetic attempts to control `Omega` from the Euclidean core, deleted 3-mod-4 P/Q primes must remain as ghost provenance; the repair coordinate is `(P^-,Q^-)` or its Legendre image `Delta`.

Smallest next arithmetic unit: on the consecutive `d=2` face, combine the canonical `Omega` channel sum with `Mz=Delta` and determine whether the nonzero defect forces a parity law for `Omega`, or construct an infinite CRT/Pell-compatible primitive family with prescribed defect and `Omega=1`. Do not infer infinitude from the four finite examples.
