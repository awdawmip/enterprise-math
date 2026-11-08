# PREFIX-603-R2 — Rank-two native BRC gate-order defect survives the exact 16D tail

Date: 2026-11-08; frozen science `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Author-side exact derivation and executed verification; independent mathematical review pending. Direct dependency PREFIX-602. Original 96 bit-ports/576 individually tagged actions remain the scientific source; 48D and 16D matrices are observer-specific exact derived carriers and do not claim individual past path-branch recovery.

For fixed six-axis weights `(1,1,1,1,0,0)`, let `Q(z)=A+(z-1)G` be the previously defined 48-phase BRC-derived transition, where `A=Q(1)`, `G=Q(2)-Q(1)`. The native gate perturbation has `rank G=1` and `G²=0`.

**Theorem 603.1 (all-parameter order defect).** For any real gate weights `a,b`:
```text
Q(a)Q(b)-Q(b)Q(a)=(a-b)(GA-AG).
```
The fixed 48x48 commutator `C=GA-AG` has **rank exactly 2** with **12 nonzero entries**. In native BRC domain `a,b>=0`, exchanging the two gate events can change later phase outputs. This is an exact algebraic order/depth claim, not a physical heartbeat interval assertion.

**Theorem 603.2 (defect persists on the 16D stable image).** Let `E,K,T1,H` be the fixed coordinates of PREFIX-602, so `T(z)=T1+(z-1)H` and `Q(z)E=ET(z)`. Then `H²=0`, the 16x16 matrix `J=HT1-T1H` has **rank 2 and five nonzero entries**, and `CE=EJ`. The same order defect survives the exact 16D observer coordinate without extra state dimensions. A gate multiset/histogram is therefore insufficient for every initial state/phase output in this domain.

**Explicit nonnegative witness.** Let `v=E e_9=(Q(1)^2)[:,14]` (index 9 is zero-based). It is a reachable nonnegative phase state in the common 16D image `V` from PREFIX-602. The two ordered gate pairs (2,1) and (1,2) obey
```text
(Q(2)Q(1)-Q(1)Q(2))v=4 e_3+4 e_14+4 e_15.
```
All three named phase outputs differ and even the total 48-phase sum differs by **12**. This disproves the *specific* proposed compression which retains only the unordered multiset of gate weights for this full-phase/future-operations scope, without asserting a universal failure of other observers or quotients.

**Proof.** Expand both products using `Q(a)=A+(a-1)G`; `G²=0` and antisymmetrization give the displayed identity. The checker rebuilds the original 48 STAR phase successors and gate, obtains exact integer `rank C=2` and `nnz(C)=12`, then verifies `C E=E J`, `rank J=2`, `nnz(J)=5`, `H²=0` and the complete nonnegative 48-vector witness. These exact full-matrix identities establish the all-real-parameter theorem; finite tests are only regression checks.

**Executed evidence.** Standalone `PREFIX603_R2_gate_order_rank2_checker.py` reuses the locally executed exact `PREFIX602_R2_stable16_native_BRC_checker.py`, symbolically checks all-a,b identities, performs 192 extra exact 48-phase basis/gate-pair comparisons and emits `PREFIX603_R2_gate_order_rank2_results.json`. All locally executed checks passed. No classical π/trigonometric computation, matrix exponential, or unrelated arithmetic fallback.

**Next question.** Obtain exact rank-two input/output factorizations for `C,J`, classify the states whose gate order is invisible at a stated horizon, and test whether carrying an explicit rank-two order defect gives a cheaper but provenance-safe observer. Mathematical proof and source persistence do not imply a formal CLAIM/Native Result, reviewer independence or Foundation acceptance.