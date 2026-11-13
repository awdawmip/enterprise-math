# PREFIX-578-R2 — Exact third-order mixed gate/axis cumulants on the native X6-BRC observer

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen science: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Current normative/control read: EM `main@4d4ea3c543ec82db371a9f920d771dcc1e620906`, GK `main@d88deaec073c61cef0a176bbf57c1a72cbfcc017`.

## Mathematical object and question

Extend canonical PREFIX-576 (axis 5/axis 6/gate covariance) and independent PREFIX-577-R2 (gate-only all-order rational resolvent) to first nonzero third-order *mixed* asymptotic cumulants. Scientific input stays frozen. The four-STAR native X6-BRC carrier has 48 phases, 96 ordered branch ports and six labeled actions per port. The exact PREFIX-566 future-observer quotient for `q1=q2=q3=q4=1; q5,q6,gate`, on all nine roots with `r5=r6=0`, has 37 classes, refinement growth `1,4,13,21,33,37`. Native gate edges are exactly `7→9,29→9,31→9`; `π_i=|class_i|/96`. This is a six-axis native carrier with a declared three-reward observer, not a lower-dimensional native space. Ordered action count is not physical time.

Let `R5(d), R6(d), K(d)` be cumulative native axis rewards and gate marks over `d` ordered actions, `S=R5+R6` and `D=R5-R6`. Six actions are selected equiprobably for the mathematical path-count observer.

## Theorem 578.1 (exact mixed cubic rates)

For **any initial native port** and each of the nine permitted frozen roots, the following limits exist:

```
lim_{d→∞} Cum(S(d),K(d),K(d))/d = -6053/5308416
lim_{d→∞} Cum(S(d),S(d),K(d))/d = 1/5184
lim_{d→∞} Cum(D(d),D(d),K(d))/d = 5/6912
lim_{d→∞} Cum(D(d),K(d),K(d))/d = 0.

lim_{d→∞} Cum(R5,R5,K)/d = lim Cum(R6,R6,K)/d = 19/82944
lim_{d→∞} Cum(R5,R6,K)/d = -11/82944
lim_{d→∞} Cum(R5,K,K)/d = lim Cum(R6,K,K)/d = -6053/10616832.
```

The dimensions refer to reward observables, not new spatial axes. Every `Cum` in the second block is evaluated at common depth `d`.

### Proof

**Analytic limit.** For any `a=(a5,a6,ag)∈Z³`, let `P_a(t)` be the 37-state weighted transfer matrix with entries

`P_a(t)[i,j]=Σ_{e:i→j} m(e)exp[t(a5*r5(e)+a6*r6(e)+ag*g(e))]/6`.

This is a formal moment-generating *observer* of the exact BRC transition kernel, not a classical propagator or a substitute for native BRC arithmetic. The quotient is irreducible, bipartite of period 2. Each squared cyclic-block transfer is primitive, so the positive analytic Perron eigenvalue `λ_a(t)` near `t=0` satisfies, for every fixed starting state and either depth parity, `log E exp(t a·R(d))=d log λ_a(t)+O(1)` with locally analytic bounded remainder. This holds uniformly in a small complex neighborhood and therefore after any fixed number of derivatives. Each directional cumulant rate is `c3(a)=∂³_t log λ_a(t)|0`.

**Exact algebraic recurrence.** Set `P=P_a(0)`, `πP=π`, `π1=1` and `M_j[a]_{ik}=Σ_{e:i→k}m(e)(a·r(e))^j/(6j!)`. Expand

`λ_a(t)=1+Σ_{j≥1} l_j t^j`, `v_a(t)=1+Σ_{j≥1}v_jt^j`, `πv_j=0`.

For `j=1,2,3`, calculate `u_j=Σ_{k=1}^j M_kv_{j-k}`, `l_j=πu_j`, and solve exactly

`(I-P+1π)v_j=u_j-l_j1-Σ_{k=1}^{j-1} l_kv_{j-k}`.

Because the irreducible stochastic `P` has a one-dimensional stationary eigenspace, `I-P+1π` is invertible. The eigenpair recurrence follows by coefficient comparison; its `π`-normalization is checked row by row. Hence `c3(a)=6l_3-6l_1l_2+2l_1³`.

The executed rational program reconstructs the original four-STAR edge kernel and its exact 37-state observer quotient, checks all class sizes and stationary weights, inverts `I-P+1π` exactly and checks the normalized recurrence for each requested direction. It obtains:

```
c3(K)=206963/42467328 (PREFIX-576-R2 reproduction)
c3(S)=-1/162; c3(D)=0
c3(S+K)=-175877/42467328
c3(S-K)=-23665/1572864
c3(D+K)=299123/42467328
c3(D-K)=-299123/42467328
c3(R5)=-49/5184
c3(R5+K)=-2937/524288
c3(R5-K)=-710191/42467328.
```

**Polarization.** Symmetry of third joint cumulants yields

`C(X,Y,Y)=[c3(X+Y)+c3(X-Y)-2c3(X)]/6` and
`C(X,X,Y)=[c3(X+Y)-c3(X-Y)-2c3(Y)]/6`.

Substitute the above exact fractions to obtain the four `(S,D,K)` values. The native PREFIX-566 involution exchanges axes 5 and 6 and preserves the gate bit; it implies the odd-`D` mixed rate vanishes. Finally
`C(R5,R5,K)=[C(S,S,K)+C(D,D,K)]/4`,
`C(R5,R6,K)=[C(S,S,K)-C(D,D,K)]/4` and
`C(R5,K,K)=C(S,K,K)/2`.
All asserted fractions follow. QED.

## Executed evidence and reproducibility

- `mixed_cumulants.py`: local executed, exact SymPy rational normalized-eigenvector recurrence; `mixed_cumulants_results.json` reports `ALL_ASSERTIONS_PASS`. Checks original gate edges, quotient growth and 37 class sizes, `πP=π`, exact matrix inverse/recurrence, previously proved gate mean/variance/third cumulant and previously proved `S,D` means/variances.
- `independent_dp.py`: locally executed, exact integer depth-DP on **all 96 native ports**, independently of the quotient eigenvector calculation. Carries raw moments of degree 0 to 3, checks the finite-depth polarization and `C(D,K,K)=0) at `d=1,2,4,8,16,32,64,96`. Data in `finite_depth_dp_results.json`. At depth 96 the three mixed per-depth ratios are approximately `-0.001147064489`, `0.000193571031`, `0.000696755240`, tending toward the proven exact values of approximately `-0.001140264817`, `0.000192901235`, `0.000723379630`. The finite sample is an implementation check, not a proof of the limit.

Reused exact sources: frozen native `PREFIX565_positive_marginal_certificate.py` blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`; 37-class quotient `PREFIX566_gate_quotient_certificate.py` blob `7b6613193847e4123cd0ac11107eb9b9c70290c8`; canonical joint Poisson result `2026-11-08_prefix576_joint_brc_gate_poisson_covariance.md` blob `6675709ce3344957b02402cfefc87eddd229e55e`; gate-only rank-one branch `6675bfa4a8c838b7223382ae5f6831de95552683`.

Execution boundary: locally reconstructed exact PREFIX565/566 source interface definitions rather than an imported full checkout; all known quotient-size and marked-edge checks agree. Proof and computations are author-side, not yet independently reviewed or canonically admitted.

## Next question

Calculate the full symmetric cubic tensor including unmarked `(R5,R6)` sectors, then derive fourth mixed cumulants with the same normalized-eigenvector method. Investigate whether the parameterized gate resolvent's specialization at `q5=q6=1` reduces to PREFIX-577-R2's exact degree-five squared-spectrum denominator. A six-axis joint observer would require a separate preservation check before reusing the 37-state quotient.

## Authority / session

GitHub authenticated login `awdawmip`, both repos admin. Native `em_status`, `em_session_start` and `em_control_tasks` returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE` with `operation_sent=false`; live owner, native Researcher-ID, CLAIM and Native Result remain unconfirmed, no independent Driver review. This artifact records the author's scientific frontier on a research branch without altering P000 or frozen input.


## Corollary 578.2 (complete order-three joint tensor)

The exact third-order joint cumulant tensor of `(R5,R6,K)` has ten symmetric coordinate multisets. The native axis exchange involution reduces them to six distinct rational entries; all ten follow from Theorem 578.1 and the already computed `c3(R5),c3(S)`:

| Coordinate multiset | Asymptotic third cumulant rate |
| --- | --- |
| `(5,5,5)` and `(6,6,6)` | `-49/5184` |
| `(5,5,6)` and `(5,6,6)` | `11/5184` |
| `(5,5,K)` and `(6,6,K)` | `19/82944` |
| `(5,6,K)` | `-11/82944` |
| `(5,K,K)` and `(6,K,K)` | `-6053/10616832` |
| `(K,K,K)` | `206963/42467328` |

Here `C(5,5,6)=(c3(S)-2c3(R5))/6=( -1/162 - 2(-49/5184))/6=11/5184`; the other entries are Theorem 578.1 and exact reproduction of the previously checked gate third cumulant. Thus the complete cubic homogeneous cumulant form for any observer `aR5+bR6+cK` is determined:

```
c3(aR5+bR6+cK) =
 (-49/5184)*(a^3+b^3)
 + (33/5184)*(a^2*b+a*b^2)
 + (57/82944)*(a^2+b^2)*c
 - (66/82944)*a*b*c
 - (18159/10616832)*(a+b)*c^2
 + (206963/42467328)*c^3.
```

Every coefficient above includes the binomial/multinomial multiplicity of its coordinate multiset. This formula is an exact all-direction third-order cumulant invariant for the declared three-observer quotient; future directions can be evaluated without another 37-state solve. The next new computation is the fourth-order mixed tensor.
