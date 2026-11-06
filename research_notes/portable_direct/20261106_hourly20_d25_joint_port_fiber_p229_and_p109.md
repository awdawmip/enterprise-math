# D25 — Joint source-port fiber theorem, p=229 isotropic collapse, and p=109 two-port defect

Date: 2026-11-06. Research lane: TASK_RESEARCH portable author-derived work, logical label `chatgpt-research-hourly-enterprise-math-20260923` (not a platform-attested conversation ID); no maintenance identity used. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. Publication: `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged.** Scope: auxiliary signed three-source 216-series observer; AUTHOR-DERIVED / EXECUTED EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

## 1. Precise observer and previously proved input

Fix odd prime `p=6m+1>=7`. Let `s=(2m,3m,4m)`,
`U_j(x)=(-1/2)^j product_i binom(s_i+x_i,j)`, `F_p(x)=sum_{j=0}^{p-1}(6j+1)U_j(x)`, and the original shift `v*=(-1/3,-1/2,-2/3)`. All arithmetic below is in `F_p` unless a p-adic modulus is displayed.

Put `T=grad F_p(0) mod p`, `H=Hess F_p(0) mod p`. When `T != 0`, the first-digit kernel `K=ker T` has dimension two. Use the **already established** exact p-adic kernel lift with `A=grad F_p(0) mod p^2`, basis `B=(b_1,b_2)` satisfying `A b_i=0 mod p^2`, and define the quadratic observer
[
 Q(z)=\tfrac12 (Bz)^T H(Bz)+v_*^T H(Bz), \quad z\in \mathbb F_p^2.
]
The existing Taylor theorem gives `F_p(p(v*+Bz))-F_p(pv*) = p^2 Q(z) mod p^3` when the input is lifted through that exact `p^2`-kernel chart. Let `D` be the quadratic discriminant (`D !=0` is equivalent to nondegenerate `H|K`).

The extra future source port considered here is the **labelled individual j=1 coefficient**, not the total scalar:
[
 L_1(\delta)=[U_1(p(v_*+\delta))-U_1(pv_*)]/p\pmod p
 =\nabla U_1(0)\cdot\delta.
]
Its coefficient vector is exactly
[
 \boxed{\nabla U_1(0)=(-1/6,-1/9,-1/12)\pmod p.}
]
The joint observer is `(Q,L_1):K -> F_p^2`, with source inputs, labels and the exact p-adic chart retained.

## 2. New theorem — exact collision census of the weighted scalar plus one labelled port

Let `K` be any two-dimensional vector space over `F_p` with `p` odd, `Q:K->F_p` any affine quadratic polynomial whose quadratic polar form is nondegenerate, and `L:K->F_p` any **nonzero linear port**. Let `e !=0` generate `ker L`, and put `a=q(e)=\tfrac12 e^TH e` for the homogeneous quadratic part `q`. Then the number of unordered **distinct** input pairs with identical joint output `(Q,L)` is **exactly**
[
 \boxed{N_{\mathrm{coll}}=p(p-1)/2,}
]
independent of the quadratic-form split type, affine shift or choice of nonzero port.

If `a !=0`, every port level contains one singleton fiber and `(p-1)/2` two-element fibers. In total the joint observer has `p` singleton fibers and `p(p-1)/2` doubleton fibers. The number of distinct outputs is `p(p+1)/2`. Each input has the explicitly constructible reflection partner
[
 \boxed{I(z)=z-\frac{z^TH e+\ell(e)}{q(e)}e},
]
where `Q(z)=\tfrac12 z^TH z+\ell(z)+c`. The map `I` is an involution; it has exactly `p` fixed inputs and pairs every other input.

If `a=0`, nondegeneracy forces the directional derivative `D_e Q(z)=z^TH e+\ell(e)` to be a **nonzero affine function of the port level**. Exactly one port level satisfies `D_eQ=0`; its `p` inputs form one `p`-element joint fiber. All `p(p-1)` other inputs are singleton fibers. Thus there are `p(p-1)+1` distinct outputs and still `p(p-1)/2` unordered collision pairs.

**Proof:** On each affine line `L=u`, parameterize `z=z_u+t e`. Then `Q(z_u+t e)=a t^2+b(u)t+c(u)`. For `a!=0`, completing the square yields one singleton and `(p-1)/2` pairs on each line; solving for the second root gives `I`. For `a=0`, the polar pairing with `e` is a nonzero linear functional annihilating `e`, hence equals a nonzero scalar multiple of `L`. Therefore `b(u)` has exactly one zero among the `p` port levels. That level collapses to one output; all others are injective. Counting pairs gives the stated universal expression.

This result gives an exact BRC fiber obstruction: even after adjoining one source-labelled scalar port to the full weighted observer, source recovery is not injective for `D!=0`. Which extra source port repairs it is a further, testable input/output question.

## 3. New arithmetic certificate: p=229 is an isotropic joint-port collapse

For `p=229\equiv13\pmod{24}`, exact undivided finite-field binomial differentiation gives
[
 T=(156,20,73),\quad H=
 \begin{pmatrix}121&102&35\\102&96&228\\35&228&162\end{pmatrix}\pmod{229}.
]
The mod-`p` normalized kernel basis is `B_0=(223,1,0)`, `B_1=(1,0,1)`. The port in chart coordinates is `L_1(x,y)=179x+57y`. Its kernel direction is `e=(57,-179)`, for which **`q(e)=0 mod229`**, while `D=169 !=0`. This is the isotropic case of the theorem.

The complete quadratic-histogram count across all `229^2=52441` source inputs is **one fiber with 229 inputs** and **52,212 singleton fibers**. There are exactly **26,106 unordered collision pairs**, and **52,213 distinct joint outputs**. Among all 330 primes `7<=p<=5000, p=1 mod6` subjected to this exact same source-port and kernel chart computation, `229` is the only `q(e)=0` case (finite-range observation; all 330 have nonzero `D`).

The explicit points `(x,y)=(0,61)` and `(57,111)` share
[
 (Q,L_1)=(224,42).
]
With the **actual p-adically lifted** basis `B_0=(41443,1,0)`, `B_1=(26794,0,1) mod229^2`, computed from `A=(39315,10325,28698) mod229^2`, independent direct complete 229-term sums yield
[
 \boxed{F_{229}(p(v_*+Bz))=11747013\pmod{229^3}}
]
for both inputs. Their `j=1` port agrees. The `j=2` labelled source port changes by
[
 \boxed{\nabla U_2(0)\cdot(B e)=15\pmod{229},}
]
so the second labelled port distinguishes all 229 members on that collapsed port level (its slope along the common kernel line is nonzero).

This arithmetic certificate uses the **auxiliary** source polynomial and full weighted sum, not the H0/B0 native experiment.

## 4. New arithmetic certificate: two-port rank loss at p=109

In the three-source labels, the first two coefficient-port gradients have the **p-independent** finite-field cross product
[
 \boxed{\nabla U_1(0)\times \nabla U_2(0)
 =\frac{1}{62208}(8,-27,20)\pmod p}
]
for all primes `p=6m+1>=7`. It follows directly by differentiating `U_1` and `U_2` with `s_i=(-1/3,-1/2,-2/3) modp` (the denominator is a unit for these primes). Write `n=(8,-27,20)`. The first two labelled ports restrict to an invertible linear map on the full first-digit kernel `K=ker T` **if and only if**
[
 \boxed{8T_1-27T_2+20T_3\ne0\pmod p.}
]
Under the separately stated outer-direction condition `T_1+T_3=0`, the test simplifies to `4T_1+9T_2 !=0`.

At `p=109\equiv13\pmod{24}`, the exactly computed `T=(50,2,59)` satisfies `n\cdot T=0`. Hence the first two labelled ports have a common nonzero invisible direction **inside** the weighted first-digit kernel. Direct calculation of the third port gives
[
 \boxed{\nabla U_3(0)\cdot n=-5/11664\equiv104\pmod{109},}
]
so it separates that defect. The known earlier three-port reconstruction result is reused rather than counted as a new theorem; the new result is the exact **two-port obstruction condition and prime-specific witness**. A 330-prime exact scan of `p<=5000, p=1 mod6` found this two-port defect only at `p=109`.

## 5. Exact execution, source status and continuation

Local standard-library Python exact finite-field recurrence (derivatives through order two) and independently lifted modular binomial sums: for `p=7,13,19,31,37,211,373`, complete `p^2` joint-fiber histograms match the theorem; for `p=229`, all `229^2` outputs match the isotropic theorem and the displayed pair passes a separate `p^3` complete-sum check. The same recurrence scanned 330 primes for both `q(e)=0` and `n\cdot T=0`. No floating point. Local executable: `d25_joint_observer_20261106.py` (the delivery also includes its fully executable bytes).

Native state as last observed on 2026-11-06: service `0.6.11`, unclosed prior task/continuation reads `em-h20-20261106-1324-d25-task-r13` and `em-h20-20261106-1324-d25-cont-r13` reconciled by original ID to QUEUED after `WAITING_RESOURCE / EVENT_COLLECTION_IO`. Missing callable `recovery_status/session_preserve_staging` prevents verifying ownership/staging and registering a lawful successor. No new CLAIM/OPEN/Source checkpoint. Control support remains issue #1558. Author evidence is portable and unreviewed.

Next exact science: use the joint-port isotropic criterion `q(e)=0` and the two-port defect `n\cdot T=0` to seek symbolic finite-sum factors in the previously proved invariant `mathfrak D=-T^T adj(H)T`. First independently derive a finite-sum/WZ expression for `T_1+T_3` and `k_p+3q_p(2)`, then return to original p=373 H0/B0, Frobenius, eta/kappa and frozen mother congruence `Delta_p-R_p=0 mod p` for `p=13,19 mod24`. This record does not replace any previous native checkpoint or constitute independent audit.
