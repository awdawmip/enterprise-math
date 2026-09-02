# Perfect Prime AP outer conditional-covariance determinant — Research Return

Researcher-ID: `EM-PPTAPOCD1-8F31A2`
Task: `RS-PERFECT-PRIME-AP-OUTER-CONDITIONAL-COVARIANCE-DETERMINANT`
Publication: `TP2-C4B48A416649C9324011`
Claim: `chatgpt-pptapocd1-20260901-2030-8f31a2`
Execution record: `ER-7826B31D99D3787CFB78`

## Terminal verdict

`NEGATIVE_BOUNDARY / EXACT_CANONICAL_FLAG_SIGN_REGULARITY_OBSTRUCTION / PARENT_NONVANISHING_OPEN`

This return does **not** prove or refute

`det S_m(t) != 0` for every `m>=2`, `0<t<=1`.

It exactly refutes one of the strongest natural noncircular structural interfaces suggested by the accepted finite data: a universal sign-regularity theorem for the **canonical monomial flag** of `S_m(t)`, equivalently a strict alternating one-by-one Sylvester/LDL pivot theorem in the quotient basis `X,X^2,...,X^(m-1)`.

The obstruction first found in this execution is the exact rational witness

`m=15, t=4/5`.

At this witness the full outer determinant is nonzero and the matrix still has the conjectured `7+ / 7-` inertia, but the twelfth leading principal minor has the opposite sign from the universal flag pattern. Thus a proof of fixed inertia/nonvanishing cannot proceed by freezing the previously observed canonical leading-principal-minor signs.

The remaining all-`m` determinant theorem and the all-`m` residual Bernstein-positivity interface remain open.

## 1. Frozen accepted input

Use the accepted outer covariance reduction unchanged. Put `n=m-1`, `b=m^2`,
`y_j=mj`, `w_j=(-1)^j binom(n,j)`, and

`lambda_(j,s)(t)=(-1)^s binom(n,s)t^s c_s(y_j)`

with

`c_s(y)=n! / prod_(r=1)^m (y+b s+r)`.

For `1<=r,q<=n`,

`C_j(t)[r,q]
 = sum_s lambda_(j,s) z_(j,s)^(r+q)
   -(sum_s lambda_(j,s)z_(j,s)^r)
    (sum_s lambda_(j,s)z_(j,s)^q)/Dcal_j(t)`

where `z_(j,s)=y_j+b s` and `Dcal_j=sum_s lambda_(j,s)>0`.

The accepted outer matrix is

`S_m(t)=sum_(j=0)^n w_j C_j(t)`

in the quotient monomial basis `X,...,X^n`, and

`tau_m(t) != 0 <=> det S_m(t) != 0`

for `0<t<=1`.

No inner definiteness premise is used below.

## 2. The structural theorem that would have closed the route

For the canonical monomial flag define

`Delta_(m,k)(t)=det S_m(t)[1..k,1..k]`, `1<=k<=m-1`.

Finite exact data through the earlier stage and further exploratory checks suggested the very strong pattern

`sign Delta_(m,k)(t)=(-1)^(ceil(k/2))`.                      (FLAG)

If `(FLAG)` held for every `m,k,t`, then every leading principal minor would be nonzero. The ordinary one-by-one LDL decomposition would exist along the entire canonical flag, with pivot signs

`(-,+,-,+,...)`.

Consequently the inertia would be frozen noncircularly and in particular the full determinant could not vanish. This would have been a valid structural interface for the task because it excludes zero crossings by an independent flag theorem rather than assuming fixed inertia.

The task therefore tested `(FLAG)` adversarially instead of promoting it from finite observation.

## 3. Exact counterexample to canonical flag sign-regularity

At

`m=15`, `n=14`, `t=4/5`

the exact `fractions.Fraction` evaluation gives the signs of
`Delta_(15,k)(4/5)`, `k=1,...,14`, as

`[-,-,+,+,-,-,+,+,-,-,+,-,-,-]`.

The universal pattern `(FLAG)` predicts

`[-,-,+,+,-,-,+,+,-,-,+,+,-,-]`.

There is exactly one mismatch:

`Delta_(15,12)(4/5) < 0`

where `(FLAG)` requires `Delta_(15,12)(4/5)>0`.

All fourteen leading principal minors are nonzero at this witness. In particular

`det S_15(4/5)=Delta_(15,14)(4/5)<0`

is **nonzero**.

The paired exact certificate hashes the canonical reduced fractions rather than embedding 5,000-digit numerators and denominators. For the full determinant,

`SHA256("numerator/denominator") =
 0f141edcf6172842c6d5175af60c1785d1a7c3ff86b1e3eab48ef51b92f08d00`.

The full determinant numerator and denominator have respectively `17954` and `17720` bits. The checker recomputes the rational exactly from the frozen definition of `S_m(t)`.

## 4. The obstruction is a two-pivot sign exchange, not an inertia counterexample

Because every leading principal minor is nonzero at the witness, the one-by-one LDL pivot signs are exactly the signs of

`Delta_k/Delta_(k-1)`.

They are

`[-,+,-,+,-,+,-,+,-,+,-,-,+,+]`.

Thus the twelfth and thirteenth pivots have changed from the strict alternating pair

`(+,-)`

to

`(-,+)`.

The number of positive and negative pivots is nevertheless

`7 positive, 7 negative`.

By Sylvester/Jacobi inertia accounting, the exact witness therefore has

`In(S_15(4/5))=(7,7,0)`.

So this result does **not** refute the finite-data inertia conjecture. It proves something more discriminating for proof design:

`FIXED_INERTIA_POSSIBLE != FIXED_CANONICAL_1x1_LDL_FLAG`.

Any eventual structural proof must allow a noncanonical congruence, block pivots/pivot-pair exchange, another variation/signature invariant, or leave the inertia route entirely. The canonical monomial flag cannot carry a globally fixed strict sign pattern.

## 5. The twelfth flag minor actually crosses inside the admissible interval

The same exact checker gives

`Delta_(15,12)(3/4) > 0`,
`Delta_(15,12)(4/5) < 0`,
`Delta_(15,12)(1)   > 0`.

Every `Dcal_j(t)>0` on `[0,1]`, hence the entries of `S_15(t)` and its principal minors are continuous there. Therefore `Delta_(15,12)(t)` has at least

- one zero in `(3/4,4/5)`, and
- one zero in `(4/5,1)`.

This is an exact theorem-level obstruction to any argument that tries to prove the parent determinant theorem by showing that **all** canonical leading principal minors avoid zero.

It does not assert that the full determinant vanishes at either of those principal-minor crossing parameters.

## 6. What this closes and what remains open

Exactly closed in this task:

- universal canonical-monomial-flag sign regularity for `S_m(t)`;
- strict globally alternating one-by-one LDL pivots in that flag;
- any fixed-inertia proof whose load-bearing premise is precisely that canonical leading-principal-minor pattern.

Still open:

- `det S_m(t)!=0` for all `m>=2`, `0<t<=1`;
- a fixed-inertia theorem obtained from a different, genuinely structural congruence or block-pivot mechanism;
- all-`m` positivity of the double-endpoint residual Bernstein/Mobius coefficients `Bhat_m(x)`.

The exact witness is consistent with full nonvanishing and with the conjectured inertia, so it must not be promoted as a counterexample to the mother question.

## 7. Deterministic exact verification

Paired checker:

`research_checks/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DETERMINANT_CHECK_20260901.py`.

It uses only Python standard-library `fractions.Fraction` arithmetic and recomputes:

1. `Dcal_j(t)>0` in the witness evaluations;
2. the exact outer matrix `S_15(t)`;
3. all fourteen leading principal minors at `t=4/5`;
4. the unique `k=12` mismatch against `(FLAG)`;
5. the exact nonzero full determinant;
6. the `7+ / 7-` LDL pivot count;
7. the sign reversal of `Delta_(15,12)` at `3/4`, `4/5`, `1`.

Paired certificate:

`research_artifacts/PERFECT_PRIME_AP_OUTER_CONDITIONAL_COVARIANCE_DETERMINANT/flag_obstruction_certificate_20260901.json`.

Finite exact arithmetic is used only to certify the stated obstruction. No bounded computation is presented as proof of the remaining all-`m` determinant theorem.

## 8. Tool reuse and scope

The execution reused the accepted parent task's exact `Fraction` outer-covariance construction and determinant elimination rather than creating a new general-purpose tool family.

`tool_reuse_resolution = REUSE_APPLIED`.

No Working Truth, Foundation, L4, novelty, or closure of
`OBJ-ROUTE-A-PERFECT-PRIME-TABLE-CRITICAL-COFACTOR-ALL-M`
is claimed.

`method_harvest = RESULT_ONLY`.

Recommended Driver disposition:

`ACCEPT EXACT_NEGATIVE_BOUNDARY; close canonical monomial-flag / strict 1x1-LDL sign-regularity as a proof route; keep parent nonvanishing open; if continuing, require either a noncanonical/block structural invariant or the all-m residual Bernstein interface.`
