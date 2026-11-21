# CBRC F7 Driver r446 — finite primitive-ray corrections have global defect exactly one

Date: 2026-11-21 (+08:00). Independent Driver mathematical continuation `EM-DVR-DEBB5E`. Preserve original F7 author `EM-CBRCF7-83A1D4`, original frozen Result `RR-AA38973D56330E59D315`. This result analyzes the just-published r445 finite homogeneous certificate's true infinite-domain behavior; it is not a Native Review or Result acceptance.

## Exact theorem

Retain the original integral involution `A=I+uv^T`, `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`; for `z=(a,b,c,d)`, `t=a-2b-c+2d`, so `Az=(a+t,b+t,c-t,d-t)`.

Let `q:Z²→[0,∞)` have these properties:

1. `q(0,0)=0`, `q(n,0)=1` for every `n≠0`.
2. For each nonaxial nonzero integer pair `(x,y)`, `1/2≤q(x,y)≤1`.
3. `q(n,n)=q(-n,-n)=1/2` for every nonzero integer `n`.
4. Outside **finitely many primitive signed rays**, `q(x,y)=1/2` on all nonaxial pairs. Precisely, there is a finite set of primitive rational slopes/signs whose positive integral multiples contain every nonaxial point with `q(x,y)≠1/2`.

Then its full, unrestricted defect
`E(q)=sup_{z∈Z⁴}|q((Az)_{1:2})+q((Az)_{3:4})-q(z_{1:2})-q(z_{3:4})|`
is **exactly 1**.

No J-evenness or homogeneous assumption is needed for this theorem, although the r445 function satisfies both. In particular, the rational 574-exception-ray r445 construction has `E(q_r445)=1` globally despite attaining the sharp `E_{10}=1/2` on the entire 21⁴ finite cube.

## Proof of global upper bound

Write `S(z)=q(z_1,z_2)+q(z_3,z_4)`. If each of the two slot vectors is nonzero, `S(z)∈[1,2]`. Therefore, if both `z` and `Az` have two nonzero slots, `|S(Az)-S(z)|≤1`.

If `z=(w,0)` or `z=(0,w)` has exactly one nonzero slot, consider `t=v^Tz`. If `t=0`, then `Az=z`. If `t≠0`, one of the two output slots of `Az` is the nonzero diagonal vector `(±t,±t)`, whose value is `1/2` by assumption (3).

If the other output slot is zero, applying `A²=I` shows the original `w` must itself have been this diagonal vector; hence the defect is zero. Otherwise, the other output slot is nonzero and has value in `[1/2,1]`. The original single-slot value is in `[1/2,1]`, so the defect lies in `[0,1]`. This proves the bound whenever `z` has one nonzero slot. Because `A²=I` and `D(Az)=-D(z)`, the corresponding case where only `Az` has one nonzero slot follows as well. Finally `z=0` has zero defect. All cases are exhausted: `E(q)≤1`.

## Lower bound and explicit r445 witness

Choose `z_n=(n,0,1,0)` for integers `n≥3`. Then `t=n-1` and
`Az_n=(2n-1,n-1,2-n,1-n)`. Both output pairs are nonaxial and primitive, since
`gcd(2n-1,n-1)=1=gcd(n-2,n-1)`. Their signed primitive rays change with `n`; thus, because the exceptional-ray set is finite, for all sufficiently large `n` neither output is exceptional. Consequently `S(Az_n)=1/2+1/2=1`, while `S(z_n)=1+1=2`; hence `D(z_n)=-1`, proving `E(q)≥1`.

The r445 table's exceptional primitive numerator has maximum 53; choosing `n=1000` gives explicit `Az=(1999,999,-998,-999)` with both rays outside that table, so the defect is exactly `-1`.

## Mathematical consequence

The exact r445 B=10 optimum is valid, but *finite primitive-ray overrides of a constant half-valued background* cannot produce a global F7 defect below one, regardless of how the finite exceptional rays are tuned within the stated interval. This is a stronger, structurally different tail obstruction than r443's finite-**point** correction theorem: here every exceptional ray contains infinitely many integer points.

Achieving an infinite-domain defect better than one requires a nontrivial unbounded family of directional ray values or a different global scalar background. The known global benchmark r435 (`E=4/7`) uses a nontrivial angular partition across infinitely many rays. The global unrestricted optimum remains open in `[1/2,4/7]`.

Evidence: r445 finite certificate `research_checks/CBRC_F7_R445_B10_HOMOGENEOUS_HALF_EXACT_CERT_20261121.py` at `d607c618a9fd579aa4221d671ba8db697c41345d`; r445 exact finite theorem at `22e0c11d28dc38247a81293c7e4909c4857511e2`; original r435 comparison at `80bc36253e1e4b5210dc665206a6f2bff746157c`. This proof uses only elementary case analysis, A²=I and a primitive-ray escape argument, with no formal checker or custom axiom.
