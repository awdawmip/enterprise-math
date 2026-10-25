# C300 — All 125 coprime reduced denominator degrees: exact prime-field pole certificate

**2026-10-25 | AUTHOR EXACT / SOURCE-EXPOSED / NO NATIVE CLAIM / NO INDEPENDENT DRIVER / NOT ADMITTED**

## Immutable starting points and scope

GLOBAL_KNOWLEDGE_V1 was read from canonical `main@124e158e394e597af0212115d43a38edc164e6bb` (00_BOOTSTRAP.md, OPERATING_MANUAL.md, P000 projection and full locked original, ACTIVE 我眼中的世界, math/BRC research policy). Enterprise Math `main@2540a16d415477e0006b18411e08a82c521103db`, project current `docs/PORTABLE_RESEARCH_PROTOCOL.md`, typed observer/joint-relation contract, and the C298 frozen portable input were read. C298 author source: `82db02673f4ef6eac9aca5bd7780bc71254d256b`; immediate C299 author source: `8d975dcda623ada2315c3f46b6eccd192a37af25`. Both predecessor author results are distinct from formal Source admission. The full reproducible data, input SHA256 manifest, verifier, and raw witnesses are in `EM_C300_ALL125_REDUCED_DENOMINATOR_EXACT_PORTABLE.zip` delivered with this run. No known source claim has been asserted.

The mathematical domain is **only** the C195/H168 **79-positive-rational-branch auxiliary function** `f_i(t)=F(v_i(t))/2^128` on 125 frozen affine paths `v_i(t)=w_i+t d_i` and their C293 short strips. It is not a theorem about native signed/phase GF(2)-BRC or P000 X6 cells.

C298 provided an integer-polynomial numerator/denominator `f_i=A_i/D_i` in `Q(t)` with positive strip denominator `D_i`. C299 proved two and only two **known** movable pole cancellations in every path at primitive linear gap factors `q_{02}` (moving slots 5 and 55) and `q_{13}` (moving slots 50 and 56), providing the *upper* reduced denominator degree 352 in 124 cases and 265 in path index 28. C299 proved this upper bound sharp only for three selected indices, leaving 122.

## Theorem (C300): all C299 degree bounds are attained

For each of the 125 frozen paths, `q_{02}q_{13}` divides `A_i` and `D_i` in `Z[t]` and
[
  A'_i=A_i/(q_{02}q_{13}),qquad D'_i=D_i/(q_{02}q_{13}).
]
Then `gcd(A'_i,D'_i)=1` in `Q[t]` up to nonzero units. The **true** reduced denominator degrees of the rational maps are precisely **352 for 124 paths** and **265 for path 28**. There is no further nonconstant polynomial cancellation on any path.

### Proof, I — exhaust the linear poles

Write the fixed 79 branch terms after pulling out primitive factors as
[
 T_j(t)=c_jprod_ell N_{jell}(t)/[s_jprod_ell q_{jell}(t)]
]
with exact integer/rational coefficients, integer numerator factors, and primitive denominator factors. C298 inventory gives **306 distinct simple primitive linear factors** in each of 124 ordinary paths, **231** in exceptional path 28. C299 exact rational residues identify exactly two canceled linear factors per path; these are distinct and pairwise coprime. There remain 304 ordinary linear factors per path and 229 exceptional factors, altogether
[
  124(304)+229=oxed{37925}
]
candidate poles to certify non-removable.

Use the Mersenne prime `p=2^61-1=2305843009213693951` (primality checked via the Lucas–Lehmer recurrence for exponent 61, 59 steps). For every remaining primitive `q=q_0+q_1 t`, put `r=-q_0/q_1 ∈ F_p`. The full verifier proves for each candidate: `q_1 mod p ≠ 0`, every branch denominator scalar is nonzero mod p, and **all other primitive denominator factors evaluate nonzero at r**; thereby the isolated residue is legal. Let `J(q)` be the branches whose denominator contains q. In the prime field form
[
  R_q =sum_{jin J(q)}c_j
  {prod_ell N_{jell}(r)over
     s_jprod_{q_{jell}
e q}q_{jell}(r)}.
]
The verifier asserts and records **37925/37925 nonzero** values `R_q≠0 (mod p)`, corresponding to the finite exhaustive domain of every path/factor in the fixed input, not a random sample. As `D_i/q` is nonzero mod p at r,
[
  A_i(r) = (D_i/q)(r),R_q 
e 0 pmod p.
]
If primitive q divided integral A_i over Q[t], Gauss's lemma would force divisibility over Z[t], contradicting the modular evaluation. Thus none of the 37925 remaining linear factors can divide A_i. The two exceptional q per path were **separately** verified by 250 exact rational residue sums `r + (-r)=0`, with each summand nonzero and no accidental other-factor collision. A vanishing modular residue is never used as proof of exact rational cancellation.

For an implementation cross-check, 14 selected nonzero residues computed by independent exact `Fraction` methods reduced to the matching field values; eight additional full original rational function evaluations were verified. Those samples only cross-check the full exhaustive verifier.

### Proof, II — no nonlinear (moving-base) poles cancel

Each moving coordinate `x_k(t)=w_k+d_k t` of nonzero slope contributes to its own branch denominator
[
   [(2-x_k(t)^2)(3-x_k(t)^2)]^3.
]
For rational nonzero slope d, the polynomials `2-x_k^2` and `3-x_k^2` are irreducible quadratics in Q[t], since their roots require sqrt(2) and sqrt(3). Such quadratics cannot divide linear gap factors.

Distinct moving slots cannot share an irreducible quadratic: at `x_k=sqrt{alpha}` with `alphain{2,3}`, any different affine coordinate has form `x_m=u+vsqrtalpha`, u,v rational. If `x_m^2=etain{2,3}`, irrational-part comparison forces uv=0. For v=0, rational `u^2=eta` impossible. Otherwise u=0 and `v^2=eta/alpha`. When `alpha
eeta`, `2/3` or `3/2` is not a rational square. When equal, `x_m=pm x_k` as affine polynomials, contradicting strictly distinct ordered positive frozen coordinates. If x_m is constant rational, its square cannot equal 2 or 3. This establishes distinctness of all quadratic factors.

At either irreducible quadratic from x_k, the own branch k has an **exact pole order 3**: its numerator is a product of a nonzero rational scalar and linear factors, none divisible by the quadratic; other 78 terms are regular at that quadratic. Consequently the full sum also has pole order exactly 3. There are 4 active moving coordinates on 124 ordinary paths and 3 on index 28. Across all paths this preserves **998 distinct quadratic families** (124*8+6), contributing denominator degree **48** or **36** respectively.

### Proof, III — degree and complexity interpretation

The complete irreducible denominator factor inventory is exhausted by the simple linear gaps and these base quadratics. Combining the noncanceled linear poles with their exact base pole orders:
[
  deg D'_{m coprime}=304+4(12)=oxed{352}
]
on 124 paths, and
[
  deg D'_{m coprime}=229+3(12)=oxed{265}
]
on path 28. This saturates C299's constructed denominators, hence `gcd(A'_i,D'_i)=1` in Q[t].

The exact C299 denominator 1-norm height majorant is independently recomputed, with maximal integer bit length **13713**. Subject to the **inherited, not independently re-run C297 full-strip outward error bound** `<2^(134-P)`, sufficient strict dyadic sign precision remains `P=352*b+13713+134` for `t=k/2^b` on a frozen strip with `f_i(t)
e 1`. This coefficient 352 is now the actual maximal denominator degree; it is **not** a computational lower bound nor a proof that the sufficient precision is optimal. There is no finite precision certificate for strict sign if f_i(t)=1 exactly.

## Exact evidence and independent limits

Deterministic author computation replays 125 source path constructions and exact factor inventories, 37925 modular residue-nonzero claims with noncollision checks, 250 exact rational zero-residue checks for the canceled poles, 998 irreducible base quadratic families by the proved model structure, 14 rational-to-modular crosschecks, eight source Fraction spotchecks, recomputed denominator height, prime Lucas–Lehmer test, and 125-path degree histogram. The **complete** compact witness table and script are in the downloadable C300 portable ZIP. All decisive arithmetic is integer, exact Fraction, or exact F_p; no floating tolerance determines a mathematical sign.

Scientific classification **AUTHOR_EXACT**; earlier C297 interval width remains inherited author evidence. This is not Lean/formal checker verification, independent Driver assessment, canonical Research Source-claim, native BRC transfer or accepted Foundation. Native EM control reads returned `CONTROL_QUOTA` and session issuance `STATIC_READONLY_SCOPE_DENIED` with `operation_sent=false`. Therefore actual current live winning owner is **unverified**, and there is no native research session, CLAIM, frozen Result or Driver review. This independent GitHub author-branch publication does not override those gates. Google Drive fallback is not used to circumvent permission denial.

## Information fidelity (BRC priority) and next exact problem

The two canceled scalar residues are genuine individually nonzero branch data `(r,-r)`. A branch-selective future operation distinguishes them even when the auxiliary scalar residue sum is zero. Thus scalar cancellation does not justify erasing branch identity, multiplicity, path/provenance, signed phase or observer-relevant residual, nor extending this auxiliary proof to P000 X6 dynamics.

**C301:** Having fixed the true coprime denominator degree on every path, calculate the exact primitive integer numerator/denominator content and improve the conservative **height** constant without losing strict sign soundness. In parallel, seek an explicitly typed native signed/phase/provenance BRC observer bridge and future-operation preservation proof. No scientific unit is claimed complete beyond the stated frozen auxiliary finite algebraic scope.
