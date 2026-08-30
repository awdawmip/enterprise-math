# P000 six-axis Tropical Plücker Result schema repair V3 return

Status: `SUCCESS / ZERO_MATH_DRIFT / WRITER_CONFORMANT_REFREEZE_READY`

- Task: `RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID`
- Publication: `TP2-5D981DF6C1ECF8AA26A0`
- Researcher: `EM-P000TP3-CF9AFB`
- Claim: `chatgpt-p000tp3-20260830-1742-3c8e71`
- Execution branch: `research/p000-six-axis-tropical-plucker-result-schema-repair-v3-em-p000tp3-cf9afb`
- Frozen generation-2 Result input: `RR-7F04B8A19C2D5E63AA71`
- Frozen generation-2 branch head: `24dca2acc9a8ead83e97dcb7f38c14855610239d`
- Driver review input: `issuecomment-5467875725`

Hard target:

`P000_TROPICAL_PLUCKER_REVISION_V3_WRITER_CONFORMANT_RESULT_WITH_ZERO_MATH_DRIFT`

## 1. Result

The generation-2 mathematics replays without contradiction. The mathematical delta is exactly `NONE`.

This V3 execution repairs only the Result envelope. The generation-2 Result is immutable and is not edited. Its noncanonical typed fields are replaced only in a fresh Result record produced from this fresh execution.

Canonical Result values selected for the fresh record are:

- `terminal_verdict = SUCCESS`
- `method_harvest = RESULT_ONLY`
- `independence_status = NOT_INDEPENDENT`
- `source_exposure_status = NONBLIND_DISCLOSED`

These values describe this execution accurately: it is an explicitly source-exposed, zero-drift replay/refreeze of frozen predecessor evidence and introduces no general-purpose tool family.

## 2. Exact finite valuation theorem preserved

Fix a prime `p` and set

`D_p = (Z\\{0})^6`.

For `x in D_p`, define

`W_VP(x) = (v_p(x_AB), v_p(x_AC), v_p(x_AD), v_p(x_BC), v_p(x_BD), v_p(x_CD)) in N^6`.

Let

`t1=x_AB*x_CD`, `t2=x_AC*x_BD`, `t3=x_AD*x_BC`,

`alpha=(v_p(t1),v_p(t2),v_p(t3))`,

`Q=t1-t2+t3`,

and

`delta_T=second_min(alpha)-min(alpha)`.

The preserved theorem is exactly:

`delta_T>0 => v_p(Q)=min(alpha) => Q!=0`,

hence, on `D_p`,

`Q=0 => delta_T=0`.

Proof boundary is unchanged. When `delta_T>0`, the finite minimum `m=min(alpha)` occurs once. After factoring `p^m`, the uniquely minimal signed summand is a unit modulo `p`, while the other two normalized summands are divisible by `p`. Therefore the normalized sum is nonzero modulo `p`, so `v_p(Q)=m` and `Q!=0`.

No zero-coordinate extension is admitted. If any coordinate is zero, `W_VP` is outside this theorem domain and fails closed. No convention `v_p(0)=+infinity`, no infinite `second_min-min` arithmetic, and no theorem on zero-containing states is introduced.

## 3. Exact checker and certificate replay

The generation-2 checker was copied byte-for-byte into the V3 authorized output scope:

`research_checks/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_RESULT_SCHEMA_REPAIR_V3_CHECK_20260830.py`

Its Git blob identity is unchanged from generation 2:

`sha1:a51d65fb405a7080f8e85afc4de5c028e4762731`

and its frozen SHA-256 remains:

`sha256:b5af1949f6ed4ccc180f6322db0e90fb1c26c11d23f27b0ab4bdc2094b6b58b2`.

Fresh execution of the exact checker produced:

`LOCAL_DETERMINISTIC_PASS checks=184315`.

The generation-2 certificate was likewise copied byte-for-byte into:

`research_artifacts/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_RESULT_SCHEMA_REPAIR_V3/P000_TROPICAL_PLUCKER_REVISION_V2_CERTIFICATE_REPLAY.json`

with unchanged Git blob:

`sha1:1559a53056170e16f9121d61a899761e4a4a4997`

and unchanged SHA-256:

`sha256:cef13ec131b23c62a4a1231f20c560cd25ee7b4e1659db2244a40d0d71d10434`.

The certificate and replay agree on the declared `p=3` and `p=2` finite domains, nine zero-boundary exclusions, exact integer arithmetic, and total check count `184315`.

## 4. Retained classifier facts with zero drift

For a finite six-weight vector define

`S=(w_AB+w_CD, w_AC+w_BD, w_AD+w_BC)`.

Then

`delta_T=second_min(S)-min(S)=sum(S)-max(S)-2*min(S)`,

and `delta_T=0` exactly when the minimum complementary-pair sum occurs at least twice.

The carrier `S4` action still induces full `S3` on the three complementary-pair blocks with V4 kernel. `delta_T` remains invariant under carrier `S4` and complement.

For `W_COORD` on `{-B,...,B}^6`, `q=2B+1`, the exact formulas are unchanged:

- triple ties: `q^2(q^2+1)/2`;
- exactly two equal minima: `q^2(q-1)(4q^2+q+3)/4`;
- survivors: `q^2(4q^3-q^2+2q-1)/4`.

The exact regressions remain `234/729` survivors for `B=1` and `3025/15625` for `B=2`.

The matched-control nonredundancy witness is unchanged:

`x=(-2,-2,0,2,1,1)`, `y=(-2,-1,-1,2,2,0)`

have the same Johnson coarse tuple `(0,22,18)`, the same `Q_orb=(-4,0,0)`, and the same `rho` carrier-orbit type `((0,1,1),0)`, but `delta_T(x)=0` and `delta_T(y)=3`.

This remains only a tested derived-classifier nonreconstructibility statement relative to those coarse observables.

## 5. Scope guards

The following boundaries remain mandatory:

- `delta_T` is a derived six-weight classifier only;
- it is not native P000 tropical geometry;
- it is not a collapse law;
- it is not a factorization mechanism;
- it is not a Foundation object;
- it is not a replacement for native six-dimensional P000 space;
- zero-coordinate `W_VP` semantics are not claimed.

## 6. Terminal disposition

Researcher verdict: `SUCCESS`.

Mathematical delta from generation 2: `NONE`.

Unresolved residue: the classifier remains nonnative, the zero-coordinate/+infinity extension remains unproved and excluded, and any native-collapse relation requires separately authorized research.

Next control-plane action: Driver review the fresh writer-conformant immutable Result and its dual-digest manifest. This researcher makes no downstream successor claim.
