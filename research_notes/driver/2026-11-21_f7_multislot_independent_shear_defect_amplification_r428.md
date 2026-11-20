# F7 Driver r428 — independent shear amplification and a failure of single-column branching bounds

Date: 2026-11-21 (+08:00). Original Driver logical line: `EM-DVR-DEBB5E`. Status: self-contained mathematical theorem and exact construction, not a Native Review or admitted Result.

## Motivation and provenance

Driver r427 established a sharp `0` versus `s` defect dichotomy for the entire two-slot block-separated old-axis `GL_2(Z)` family; [source](2026-11-21_f7_all_gl2_old_axis_mixing_sharp_defect_dichotomy.md) at commit `48711a22e2feb049b3c5849b59460fc78866c8cc`. The prior r425 branching theorem gives a lower bound `(r-1)s` from *one* nonzero input column with `r` nonzero output branches. In more than two slots, simultaneous but distinct splits can force a strictly larger defect than any single-column branching count predicts.

The original CBRC F7 author `EM-CBRCF7-83A1D4` and frozen Result `RR-AA38973D56330E59D315` are separate provenance. This note is a mathematical `2k`-slot extension of the axis-block method, *not* a claim about the original two-slot marked-balance optimum.

## Definition

For any `k>=1`, set `S=[[1,0],[1,1]]` and `B_k=diag(S,...,S) in GL_{2k}(Z)` (k blocks). Let `H:Z->[0,infty)` be finite-valued with `H(0)=0` and uniform old-axis lower bound `H(t)>=s>0` for every `t!=0`. Write `Q_H(x)=sum_{i=1}^{2k}H(x_i)`, and define the worst uniform defect
```
E(B_k,H)=sup_{x in Z^(2k)} |Q_H(B_k x)-Q_H(x)|.
```

## Theorem (exact k-fold defect amplification)

For every such H,
```
                  E(B_k,H) >= k*s.
```
The bound is sharp simultaneously for all k:
```
        inf_{H(0)=0, H(nonzero)>=s} E(B_k,H) = k*s,
```
achieved by `H_s(t)=s*1_{t!=0}`.

**Proof of the universal lower bound.** Choose arbitrary nonzero integers `t_1,...,t_k` and input
```
x=(t_1,0,t_2,0,...,t_k,0).
```
Each shear block sends `(t_i,0)` to `(t_i,t_i)`. Hence
```
Q_H(B_k x)-Q_H(x)
 = sum_i [H(t_i)+H(t_i)-H(t_i)]
 = sum_i H(t_i) >= k*s.
```
This is an exact single-input estimate, with no iteration and no symmetry hypothesis.

**Proof of sharpness.** For any integer pair `(u,v)`, both `(u,v)` and `S(u,v)=(u,u+v)` have support size in `{0,1,2}`. They are simultaneously zero or nonzero, so their support sizes differ by at most one. Consequently, for `H_s`, the change of `Q_H` in each block is in `{-s,0,s}`; the total absolute change is at most `k*s`. The above `x` attains `+k*s`, so the uniform defect equals `k*s`. QED.

## Exact structural obstruction to a tempting generalization

Every column of `S` has at most two nonzero entries, and the same holds for `S^{-1}=[[1,0],[-1,1]]`. Thus for **every k**, all columns of both `B_k` and `B_k^{-1}` have support at most **2**; nevertheless their best possible fixed-separation defect is `k*s`, unbounded as k grows.

In particular, a proposed many-slot universal estimate of the form
```
min_possible_defect <= (max_{columns of B and B^{-1}} support_size - 1)*s
```
would be false already at `k=2`: its right side is `s`, while the exact minimum is `2s`. The earlier *lower* bound using one column remains valid; what fails is its assumed sharpness/upper prediction in multi-slot systems.

For k=2 the example can be written explicitly as
```
B_2 = [[1,0,0,0],
       [1,1,0,0],
       [0,0,1,0],
       [0,0,1,1]].
```
All integer inputs are covered by the proof. A bounded enumeration of `u,v∈[-4,4]` in each shear block supplies an auxiliary finite regression: each block's indicator-support difference belongs to `{-1,0,+1}`, and `(t,0)` attains `+1` for any nonzero t. This finite check is not part of the universal proof.

## F7 scope and next question

This theorem demonstrates that independent, simultaneously accessible branch opportunities add their positive defects, even without a single column of high support. It motivates an `A0`-compatible general `GL_{2s}(Z)` audit using actual multislot invariants rather than single-ray branching degree alone. The original two-slot F7 problem corresponds to k=1; for k>1 this is a conditional extension of the representation, not a revision to the frozen F7 result.

The independent evidence and control issues remain: original Result `RR-AA38973D56330E59D315` has two incorrect output-manifest SHA256 declarations, and the one original Native Review attempt ended `FAILED / NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED` (maintenance Issue #2874). Neither this proof nor the repo save repairs those native requirements.

**Layered status:** one new mathematical theorem/counterexample subunit; Native Review admitted 0; Native Result admitted 0; formal Task DONE 0; mother Objective CLOSED 0.
