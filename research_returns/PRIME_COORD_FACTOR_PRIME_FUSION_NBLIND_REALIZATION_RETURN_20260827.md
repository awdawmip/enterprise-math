# Prime Coordinate Factor — Prime Fusion N-Blind Composite-Ring Realization Return

Status: `FROZEN / AWAITING DRIVER REVIEW`

Task-ID: `RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION`  
Publication-ID: `TP2-064103C123D4486521E7`  
Researcher-ID: `EM-PCF6-79EC8F`  
Claim-ID: `chatgpt-pcf6-20260828-1420-79ec8f`  
Execution-record: `ER-4E7A1D93B6C2058F4A11`

## Primary verdict

`FUNCTORIAL_REALIZATION_OBSTRUCTED`

Hard target `PRIME_FUSION_NBLIND_REALIZATION_PROVED_OR_NO_GO` is met at exact obstruction strength.

The exact scope of the verdict is important:

- the **ambient quartic fusion algebra** does have a canonical factor-blind composite-ring realization;
- the **corrected T10 channel-oriented rank-2 mixed carrier/operator** does not descend factor-blindly in general;
- any exact free-rank-2 operator realizing the Gaussian channel at one hidden factor and the Eisenstein channel at the other exposes the hidden CRT selector as minus its trace and therefore yields a nontrivial gcd immediately.

Thus the corrected mixed realization is not an N-only constructor that precedes factor separation. At this strength it is equivalent to producing the missing asymmetry/idempotent information.

## Source and dependency pins

- task publication: `TP2-064103C123D4486521E7`, generation 2;
- taskbook blob: `sha1:03f453db8c9c9e435e279c8901cc7bd9a9815ada`;
- execution base: `main@84a62537dd5355db7a4b0e0d75072c5fc7a295bf`;
- accepted PCF1 result: `RR-B8D8679EB033E990E825`, result-record blob `5962795e98743cf8b5dba3fcfc043f508bda34a4`;
- PCF1 Driver review: `driver_reviews/PRIME_COORD_FACTOR_INFORMATION_LEAKAGE_AUDIT_DRIVER_REVIEW_20260827.md`, blob `b1bef218c80e5979a5de8f8b0c95ac2317857bf4`;
- corrected Prime Fusion package: Git blob `055bdaaca81c5ac7ab350a71acf3b69fe5e564a9`;
- historical package source: `research/PRIME_FUSION_THEOREM_PACKAGE_20260823.md@e5138e17f8c4009f5e357f43326f2812c9df1359`.

PCF1's accepted constructor boundary is preserved: algorithmic construction may consume only the unfactored modulus, independent public seeds, and factor-independent parameters. Hidden factors, CRT idempotents, pointed roots, and `M_{p,q}` remain proof-side unless reconstructed from the unfactored input.

## T1 — Canonical N-blind ambient carrier and operator

Write the unfactored input as `H` to avoid collision with the source channel `N(a,b)`. Let

`R_H=Z/HZ`,

`f=X^2+1`,

`g=X^2+X+1`,

`F=fg=X^4+X^3+2X^2+X+1`.

Define

`A_H=R_H[X]/(F)`

and let `T_H` be multiplication by `[X]`.

This is canonical from `H` alone. The integral Bezout identity

`(X+1)f-Xg=1`

implies, after base change,

`A_H ~= R_H[X]/(f) x R_H[X]/(g)`.

If proof-side `H=pq`, coefficient CRT also gives

`A_H ~= A_p x A_q`.

So the T3 fusion algebra descends fully and functorially. What is lost is not the ambient algebra, but the hidden-factor-dependent **cross-selection** needed by corrected T10.

## T2 — Exact mixed-carrier selector equivalence

Assume proof-side `H=pq`, with distinct primes `p,q>3`, and use the corrected oriented local conditions: `f` on the `p` component and `g` on the `q` component.

Let `c in R_H` be the CRT selector

`c=0 mod p`, `c=1 mod q`.

Then `c^2=c mod H`, `gcd(c,H)=p`, and `gcd(c-1,H)=q`.

Define

`h_c=(1-c)f+c g=X^2+cX+1`,

`D_c=R_H[X]/(h_c)`.

Proof-side CRT gives

`D_c ~= F_p[X]/(f) x F_q[X]/(g)`.

Its `R_H`-valued roots are exactly

`M_{p,q}={x mod pq : x^2+1=0 mod p and x^2+x+1=0 mod q}`.

Therefore a nontrivial idempotent constructs the exact corrected rank-2 mixed carrier, but that idempotent already factors the modulus by a single gcd.

## T3 — Basis-independent trace obstruction

Let `M` be any free rank-2 `R_H` module and `T in End_R_H(M)`. Suppose proof-side reductions satisfy

`charpoly(T mod p)=X^2+1`,

`charpoly(T mod q)=X^2+X+1`.

Since a rank-2 characteristic polynomial is

`X^2-tr(T)X+det(T)`,

we obtain

`tr(T)=0 mod p`,

`tr(T)=-1 mod q`,

`det(T)=1 mod H`.

Hence

`c=-tr(T) mod H`

is exactly the nontrivial CRT selector, and

`gcd(c,H)=p`.

Conversely, from such a selector `c`, multiplication by `X` on `R_H[X]/(X^2+cX+1)` has the two required local characteristic polynomials.

Thus, at exact free-rank-2 operator strength,

`CORRECTED_ORIENTED_MIXED_REALIZATION <=> NONTRIVIAL_CRT_IDEMPOTENT`,

with an explicit one-gcd extraction map from the realization to a hidden factor.

This is stronger than a failure of one proposed invariant: it shows that the desired channel-oriented rank-2 object's trace itself carries the split.

## T4 — Ambient synchronization and first observable no-go

Because `f=Phi_4` and `g=Phi_3`,

`T_H^12=I`.

For `gcd(H,6)=1`, the two ambient channel components have exact orders `4` and `3`, so the regular ambient operator has exact order `12` independently of the hidden primes.

For `Delta_k=det(T_H^k-I)`, `1<=k<=12`, the exact integer values satisfy

- `Delta_k=0` if `3|k` or `4|k`;
- `|Delta_k|=6` for the remaining odd `k`;
- `|Delta_k|=12` for the remaining even `k`.

Hence for every `H` coprime to `6`,

`gcd(H,Delta_k)` is always either `1` or the trivial value `H`.

The corresponding hidden-field rank defect is

`2*[3|k]+2*[4|k]`,

again factor-independent. The natural orbit/rank/determinant family is exactly synchronized.

More generally, for fixed `P in Z[X]`,

`det(P(T_H))=Res(F,P) mod H`.

This is the reduction of one fixed integer. If the resultant is zero the gcd is trivial `H`; if nonzero, only its finite prime support can be exposed. Therefore no finite H-independent family of polynomial-determinant probes on the universal ambient operator is a universal semiprime separator.

This no-go is deliberately scoped. It does not exclude a genuinely H-dependent asymmetry generator.

## T5 — Synchronized families and carrier degeneracies

For primes `p,q>3` satisfying the oriented algebraic split conditions `p=1 mod 4`, `q=1 mod 3`, corrected `M_{p,q}` always has four roots.

The complete fused root set of `F` modulo `pq` has size

`4(1+[p=1 mod 3])(1+[q=1 mod 4])`,

hence exactly `4`, `8`, or `16`.

It coincides with corrected `M_{p,q}` exactly when both unwanted cross-channel root sets vanish:

`p=5 mod 12`, `q=7 mod 12`.

Under the source T9 branch coupling this coincidence subfamily is

`p=5 mod 24`, `q=7 mod 12`.

This is a root-predicate coincidence only. In the `8` and `16` cases the full fused carrier strictly over-includes spurious mixed orientations. In all cases, an exact channel-labelled free-rank-2 operator has the trace/idempotent obstruction above.

## T6 — Frozen H=91 pressure witness

For `(p,q,H)=(13,7,91)`, the selector is

`c=78`.

It satisfies

`c=0 mod 13`, `c=1 mod 7`, `c^2=c mod 91`, `gcd(c,91)=13`.

The selector polynomial

`X^2+78X+1 mod 91`

has roots exactly

`{18,44,60,86}=M_{13,7}`.

The full roots of `F` are

`{9,16,18,44,60,74,81,86}`.

This preserves the corrected T10 pressure guard and demonstrates the obstruction concretely without using the finite example as proof of the general theorem.

## T7 — Exact comparison with retained Prime Fusion statements

- T3 ambient fusion algebra: **retained N-blindly**.
- T4/T5 pointed root/channel recovery: **decoder survives; pointed root is not thereby generated N-blindly**.
- T6 reciprocal-trace idempotent: **retained and becomes the exact constructor-boundary witness**.
- T8 abstract product shape: **retained proof-side; abstract product does not restore channel labels**.
- T10 corrected oriented mixed locus: **general N-blind rank-2 descent obstructed by trace/idempotent equivalence**.
- T11 sixth-power readout: **retained for an oriented root; it is a decoder after asymmetry exists, not the source of the root**.
- Ambient orbit/rank/determinant invariants: **synchronized** for the universal generator; fixed polynomial determinants reduce to fixed integer resultants.

No source theorem is silently transferred from a factor-labelled object to an N-only constructor.

## Exact checker evidence

Primary checker:

`python scripts/check_prime_coord_factor_prime_fusion_nblind_realization.py`

Authoring-time exact output:

`PCF6_CHECK_PASS source_pairs=412 public_profiles=412 selectors=412 root_classes=4:144,8:224,16:44 pressure=PASS trace_split=PASS ambient_sync=PASS`

Its `public_worker(H)` accepts only `H`. Factors are confined to a separate external theorem-verifier compartment.

Independent checker:

`python scripts/check_prime_coord_factor_prime_fusion_nblind_realization_independent.py`

Authoring-time exact output:

`PCF6_INDEPENDENT_PASS algebraic_pairs=432 root_classes=4:144,8:216,16:72 selector_equivalence=PASS fixed_cyclotomic_sync=PASS pressure=PASS`

The independent checker does not reuse the primary 4x4 matrix route. It reconstructs the selector/root classification from local cyclotomic roots and CRT.

Finite counts are regression/falsification evidence only; the main obstruction and synchronization results are exact proofs.

## Artifacts

- `research_artifacts/PRIME_COORD_FACTOR_PRIME_FUSION_NBLIND_REALIZATION/EVIDENCE_REPORT.md`
- `scripts/check_prime_coord_factor_prime_fusion_nblind_realization.py`
- `scripts/check_prime_coord_factor_prime_fusion_nblind_realization_independent.py`
- `research_execution_records/RS-PRIME-COORD-FACTOR-PRIME-FUSION-NBLIND-REALIZATION/ER-4E7A1D93B6C2058F4A11.json`
- this return.

## Limitations and exact unresolved residue

This return does **not** claim:

- a factorization speedup;
- a factoring lower bound;
- impossibility of all H-dependent algorithms;
- that finite regression proves an infinite theorem;
- that the ambient quartic fusion algebra itself fails to descend.

The smallest unresolved program object is

`N_ONLY_ASYMMETRY_GENERATOR`,

sharpened on the corrected mixed-carrier route to

`N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR`.

Any successor on this route must generate such asymmetry from `H` itself; it may not receive `p,q`, a nontrivial CRT idempotent, a pointed oriented root, or `M_{p,q}` as constructor input.

## Downstream transition recommendation

Driver should accept PCF6 as task-terminal at `FUNCTORIAL_REALIZATION_OBSTRUCTED` strength if the trace/idempotent equivalence and ambient synchronization proof are confirmed.

Do not open a larger finite root census. A mathematically meaningful successor, if desired, should target one of two sharply separated questions:

1. construct an admissible **H-dependent** N-only asymmetry/idempotent generator not reducible to fixed universal polynomial-resultant probes; or
2. prove an independently scoped obstruction for a materially broader class of H-dependent ambient observables.

Do not reinterpret the root-count-4 coincidence family as a general channel-labelled descent.

Tool-candidate disposition: `NO_NEW_SHARED_TOOL_FAMILY / TASK_LOCAL_EXACT_CHECKERS_ONLY`.
