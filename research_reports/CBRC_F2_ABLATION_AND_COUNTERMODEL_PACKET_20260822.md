# CBRC F2 — Ablation and Countermodel Packet

Researcher-ID: `EM-CBRC-F2-CB605B`  
Task-ID: `RS-CBRC-F2-OBSERVABLE-NONSIGN-RECOALESCENCE-FORWARD-CLASSIFICATION`

All countermodels below are derived from the blind F2 carrier unless an explicit inert enlargement is stated.

## 1. Baseline exact model

`C1 = Z e (+) <tau | 3 tau=0>`

Write `z=(n,a)`.

`R(n,a)=(n,a+n)`, `J(n,a)=(-n,-a)`, `S(n,a)=(n,-a)`.

Baseline observable family:

`rho(z)=f([z]_G)`

with:

- `rho(0)=0`;
- `rho(Omega_1)=1`;
- `rho(Omega_T)=t>0`;
- all remaining orbit values arbitrary nonnegative.

## 2. Remove O3 — absolute non-sign invisibility

Result:

`NO_WIDENING_ON_DECLARED_ELEMENTARY_DOMAIN`.

Reason: O5 gives

`rho(R^k e)=rho(e)`,

and O6 gives

`rho(JR^k e)=rho(R^k e)`.

Together with O2, every signed/transported elementary state already has value `1`.

Therefore O3 is logically redundant given O2+O5+O6 on the declared scalar domain.

Smallest countermodel: none exists while O2, O5, O6 remain.

## 3. Remove O4 — distinguishable alternative additivity

O4 acts on a separate tagged bookkeeping layer and does not constrain the unmarked `rho`.

Without O4, keep the entire baseline unmarked readout and assign an arbitrary tagged total to two distinguishable elementary alternatives, e.g.

`T_tag(1,1)=7`

instead of `2`.

All unmarked O1/O2/O3/O5/O6/O7/O8/O9/O10 remain unchanged.

Widening:

`TAGGED_TOTAL_FREE`.

## 4. Remove O5 — common transport invariance

Keep O1–O4 and O6–O10.

Define:

- `rho(0)=0`;
- all elementary states have value `1`;
- pure nonzero torsion has value `1`;
- for `|n|=2`, set value `2` if `a=0`, value `3` if `a!=0`;
- assign `1` elsewhere.

This is `J`- and `S`-invariant and respects absolute single-branch invisibility, but

`rho(2,0)=2 != 3=rho(2,1)`.

Thus same-sign relative non-sign transport becomes scalar-visible when common transport invariance is removed.

Widening:

`SAME_SIGN_RELATIVE_CLASS_SPLITS`.

## 5. Remove O6 — global sign invariance

Keep isolated elementary sign invisibility from O3.

Define:

- `rho(0)=0`;
- `rho(z)=1` for `|n|=1`;
- `rho(z)=1` for nonzero pure torsion;
- for all other `n>0`, set `rho=2`;
- for all other `n<0`, set `rho=3`.

This remains common-transport and reversal invariant, but

`rho(2,0)=2 != 3=rho(-2,0)`.

Widening:

`GLOBAL_SIGN_CLASSES_SPLIT`.

## 6. Remove O7 — reversal / serialization invariance

O5 and O6 still collapse the minimal two-path pure-torsion orientations, so the F2 minimal witness is unchanged.

The first new reversal-sensitive split occurs when `n` is divisible by `3`.

Define on `|n|=3`, `a!=0`:

- `rho(3,1)=rho(-3,2)=5`;
- `rho(3,2)=rho(-3,1)=6`.

This preserves J-invariance and common transport because `R` is trivial on the torsion coordinate when `3|n`, but violates reversal:

`rho(3,1) != rho(S(3,1)) = rho(3,2)`.

Widening:

`REVERSAL_SPLIT_FIRST_AT_ABS_N_3`.

The serialization-swap portion is independently redundant once aggregation is commutative and O8 holds.

## 7. Remove O8 — aggregate presentation independence

Now allow the scalar to depend on the erased presentation rather than only its sum.

Two same-sign presentations have the same aggregate:

`P_equal = (e,e) -> (2,0)`

and

`P_unequal = (R e, R^2 e) -> (2,0)`.

Define a presentation scalar:

- zero aggregate -> `0`;
- one elementary -> `1`;
- two nonzero alternatives with equal transport labels -> `2`;
- two nonzero alternatives with unequal transport labels -> `3`.

Common transport shifts all transport labels together and preserves equal-versus-unequal; reversal negates all labels and preserves it; swapping branches preserves it.

Yet:

`rho(P_equal)=2 != 3=rho(P_unequal)`

for the same aggregate coefficient.

Widening:

`PRESENTATION_PROVENANCE_BECOMES_SCALAR`.

This demonstrates why O8 is load-bearing.

## 8. Remove O9 — composition compatibility

Permit depth-indexed scalar tables.

For the same nonzero pure-torsion coefficient, set:

`rho_depth2(tau)=2`

and

`rho_depth3(tau)=3`.

At each fixed depth the rule may satisfy O1–O8 and O10, but there is no single full-domain readout compatible with composition.

Widening:

`DEPTH_INDEXED_READOUTS_ALLOWED`.

## 9. Remove O10 — non-sign relative sensitivity

Define the signed-layer count:

`rho(n,a)=|n|`.

Then:

- `rho(0)=0`;
- every elementary state has value `1`;
- common transport, global sign, and reversal leave the value invariant;
- the rule is aggregate- and composition-compatible.

But:

`rho(tau)=0=rho(0)`.

Hence the F1 hidden sheet may remain completely scalar-silent when O10 is removed.

Widening:

`F1_TORSION_MAY_BE_OBSERVATIONALLY_SILENT`.

## 10. Remove minimal-carrier requirement

Construct the inert enlargement

`C' = C1 (+) Z/2 xi`.

Let `R,J,S` act as before on `C1` and trivially on `xi` (with `J xi=-xi=xi` in order two). Let the scalar ignore the inert coordinate.

The original witness

`e + J R e = -tau`

remains observable exactly as before.

Therefore infinitely many nonminimal supercarriers become admissible once minimality is removed.

Smallest exhibited widening:

`C1 (+) Z/2`.

Result:

`C1_PLUS_INERT_Z2_IS_ADMISSIBLE_NONMINIMAL_EXTENSION`.

## 11. Selector countermodels

### S1 tagged upper bound removed

Choose `rho(Omega_T)=3`; retain all invariances and normalization. O1–O10 still hold, but the value exceeds the tagged total of the two-branch witness.

### S2 zero separation removed

Choose one nonzero higher orbit, e.g. `Omega_3^0`, to have value `0`; keep `rho(Omega_T)>0`. O1–O10 still hold.

### S3 monotonicity removed

Choose `u_2=5`, `u_4=1`. O1–O10 remain valid.

### S4 linear copy scaling imposed

For `tau!=0` with `3 tau=0`, O10 requires `rho(tau)>0`, whereas linear copy scaling would force

`0=rho(3tau)=3rho(tau)`.

Therefore the selector is incompatible with the accepted observable torsion carrier.

## 12. Deterministic evidence

The checker exhaustively instantiates all mandatory ablations on its declared exact finite window.

Checker digest:

`8d3a47d9f755826dce69c8a198ef0092bfb668a630c7737a3b864b60227f92d3`

Status:

`ALL_MANDATORY_ABLATIONS_CLASSIFIED`
