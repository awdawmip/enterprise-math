# CBRC F7 — Rank-Two Balanced Mixing Existence and Selector Classification — Same-Task Theorem Repair

Researcher-ID: `EM-CBRCF7-83A1D4`  
Task-ID: `RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION`  
Publication-ID: `TP2-6F3A8C21D4B7095E1F62`  
Revision claim: `chatgpt-cbrc-f7-revision-20260903-83a1d4`  
Execution branch: `research/cbrc-f7-revision-em-cbrcf7-83a1d4`  
Reviewed frozen Result: `RR-7435C09299E80E4BAE04`  
Reviewed frozen head: `569eb4fc4fee91d4c06d18efd3e33754e1ae702e`

Primary task verdict after repair:

`F7_NO_BALANCED_RANK_TWO_MIXING_EXISTS`

Revision disposition:

`OLD_LEMMA_3_3_STANDALONE_STATEMENT_RETRACTED / TASK_LEVEL_NO_GO_REPROVED_BY_A0_J_AWARE_BLOCK_RANK_CLASSIFICATION`

No F8 successor is authorized by this return.

---

## 0. Executive result

The Driver's `REQUEST_REVISION / SAME_TASK_ID` was mathematically justified.

The prior F7 return used a load-bearing Lemma 3.3 asserting, in effect, that every
period-free non-whole-slot-block-monomial exact separable conservation law in
rank two becomes quadratic on a finite-index lattice. That standalone statement
is **false**.

An exact counterexample is

\[
f(n,m)=n^2+|m|
\]

with the unimodular two-slot map

\[
A(n_1,m_1,n_2,m_2)=(n_1,m_2,n_2,m_1).
\]

Then

\[
f(n_1,m_1)+f(n_2,m_2)
=
f(n_1,m_2)+f(n_2,m_1),
\]

`f` is nonnegative, `J`-even under `(n,m)->(-n,m)`, period-free, and is not a
single quadratic polynomial on any lattice `N Z^2`. The map is not a product
or swap of whole slots. It fails F7 only because its first elementary old
input has old projection in one output slot only, so A0 fails.

Therefore this revision does **not** attempt to disguise the old proof sketch
as a proof. It replaces it with a narrower but exact theorem that uses the
actual F7 hypotheses, in particular A0 and inherited `J` invariance.

The corrected theorem is:

> **A0/J-aware rank-two obstruction.**  
> Let `f:Z^2 -> R_{>=0}` satisfy
>
> 1. `f(0,0)=0`;
> 2. `f(-n,m)=f(n,m)`;
> 3. `n != 0 => f(n,m)>0`;
> 4. for
>    \[
>    A=\begin{pmatrix}P&Q\\R&S\end{pmatrix}\in GL_4(Z),
>    \]
>    the exact conservation identity
>    \[
>    f(Px+Qy)+f(Rx+Sy)=f(x)+f(y) \tag{E}
>    \]
>    holds for all `x,y in Z^2`;
> 5. the first old elementary column obeys A0:
>    the old coordinates of `Pe` and `Re` are both nonzero.
>
> Then no such `A` exists.

This theorem is sufficient for the frozen F7 problem and does not use the
numerical balance value `1/2`. Hence the prior F7 primary no-go survives, but
for a corrected reason.

The repair is exact, not a bounded `GL_4(Z)` census. The accompanying checker
certifies the algebraic identities and regression witnesses but explicitly
does not substitute finite enumeration for the infinite-lattice theorem.

---

## 1. Provenance / blind-boundary disclosure

This conversation claimed the already-published V2 task only after the Driver
had returned the prior Result for same-task revision.

Before opening the blind packet in this revision, the following execution
stamp was frozen:

`research_execution_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/EXECUTION_STAMP_EM-CBRCF7-83A1D4_20260903.json`.

After the migrated taskbook was opened, its strict firewall was seen to forbid
pre-freeze F3/F3R/F3R2 mathematical history. This conversation's pre-existing
project context contained high-level metadata naming some earlier F3/F3R/F3R2
tasks, although it did not expose the F7 blind packet or prior F7 proof payload.
Accordingly this revision **does not assert a fresh `TARGET_LEAK_AUDIT_PASS`**.

The scope disclosure is frozen at:

`research_execution_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/REVISION_SCOPE_DISCLOSURE_EM-CBRCF7-83A1D4_20260903.json`.

This is a post-freeze theorem repair. It preserves the original execution's
already-frozen raw discovery provenance but does not re-certify that provenance
under a new clean-blind claim.

The mathematical source used after that disclosure is the authorized F7 blind
packet:

`research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@bc046c8d77910ddb1f42b572a736d9d938ecbb9c`.

The accepted F4 rank-one free-block theorem is reused only in the period branch:

`research_reports/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_RETURN_20260823.md@f0a0edc9ef5d8e0ea1b21727f5a7c92f681e09a5`.

No downstream wave, ring, norm, complex/quadratic carrier interpretation, or
named transform semantics is used in this proof repair.

---

## 2. Frozen envelope reduction retained

The prior finite torsion-fiber reduction is sound and is retained unchanged.

For the F6-minimal carrier

\[
C_2=Z e\oplus Z f\oplus\langle\tau\mid 3\tau=0\rangle,
\]

write a free point as `(n,m)`. Define

\[
f(n,m)=\min_{a\in Z/3} q(ne+mf+a\tau).
\]

Because the torsion fiber is finite and the inherited unary relations act as in
the blind packet:

1. `f>=0`;
2. `f(0,0)=0`;
3. `n != 0 => f(n,m)>0`;
4. `f(-n,m)=f(n,m)`;
5. `f(1,0)=1`.

For the free quotient of the additive automorphism, write

\[
A=\begin{pmatrix}P&Q\\R&S\end{pmatrix}\in GL_4(Z),
\qquad P,Q,R,S\in M_2(Z).
\]

Minimizing exact pair conservation over the nine input torsion labels gives

\[
f(Px+Qy)+f(Rx+Sy)=f(x)+f(y) \tag{E}
\]

for all `x,y in Z^2`.

The remainder of this return proves that (E), nonnegativity, `J`-evenness,
old-projection positivity, invertibility, and A0 are inconsistent.

---

## 3. Exact mixed-difference isolation

For `u in Z^2`, write

\[
\Delta_u f(z)=f(z+u)-f(z).
\]

Apply the mixed input difference
`Delta_h^x Delta_k^y` to (E). One obtains

\[
\Delta_{Ph}\Delta_{Qk}f(Px+Qy)
+
\Delta_{Rh}\Delta_{Sk}f(Rx+Sy)=0. \tag{D}
\]

Because `A` is onto `Z^4`, the two output variables

\[
u=Px+Qy,\qquad v=Rx+Sy
\]

vary independently over `Z^2`. Therefore there is a constant `C(h,k)` such
that

\[
\Delta_{Ph}\Delta_{Qk}f \equiv C(h,k),
\qquad
\Delta_{Rh}\Delta_{Sk}f \equiv -C(h,k). \tag{D1}
\]

This is the only generic finite-difference identity needed below.

### Independence lemma

If functions `phi_i:Z->R` satisfy

\[
\phi_1(z_1)+\cdots+\phi_r(z_r)=0
\]

for independently arbitrary `z_i`, then every `phi_i` is constant. This follows
by varying one coordinate at a time.

We will use this same observation in the new-axis hub branch.

---

## 4. Integrality / finite-index saturation

This is one of the points that the Driver correctly required to be explicit.

### Lemma 4.1 — full-rank image saturation

For an integer `2x2` matrix `B` with `d=det B != 0`,

\[
B\,\operatorname{adj}(B)=d I_2.
\]

Hence

\[
d Z^2\subseteq \operatorname{im}B. \tag{S}
\]

Thus every rational full-rank block supplies all lattice directions after a
single integer dilation.

### Lemma 4.2 — rank-one saturation

For a nonzero integer rank-one block `B`, its rational image is a rational line
`L_B`. If `ell_B` is a primitive integer generator of
`L_B \cap Z^2`, then for some positive integer `c_B`,

\[
c_B Z\,\ell_B\subseteq \operatorname{im}B.
\]

Therefore one common integer `N` can simultaneously clear every determinant
and rank-one content appearing in a fixed block-rank case.

For

\[
F(z)=f(Nz),
\]

identity (E) remains true with the same integer matrix `A`, and every
constant-difference statement needed below becomes an ordinary integer-lattice
statement for `F`.

No rational-direction integration is used without this dilation.

---

## 5. Period branch is impossible

Let

\[
\operatorname{Per}(f)=\{w\in Z^2:f(z+w)=f(z)\ \forall z\}.
\]

If `w=(a,b)` is a period, then `f(w)=f(0)=0`. Old-projection positivity forces
`a=0`. Hence every nonzero period is a pure new-direction period and

\[
\operatorname{Per}(f)=\{0\}\times kZ
\]

for some `k>=1`.

The period subgroup of the pair scalar is exactly
`Per(f) \oplus Per(f)`: if `(u,v)` is a pair period, then
`Delta_u f(x)+Delta_v f(y)=0` for independent `x,y`, so both first
differences are constants; global nonnegativity forces both constants to be
zero by forward/backward iteration. Since `A` preserves the pair scalar exactly
and is invertible, it preserves this subgroup and descends to an automorphism of

\[
(Z e\oplus Z/k f)^2.
\]

Define the finite-fiber envelope

\[
g(n)=\min_{m\bmod k} f(n,m).
\]

Then

- `g(0)=0`;
- `g(n)>0` for `n!=0`;
- `g(-n)=g(n)`;
- the descended free `2x2` old-coordinate block exactly conserves
  `g(n)+g(p)`.

The accepted F4 rank-one free-block theorem therefore forces that descended
old block to be a signed permutation. But A0 says the first old input has
nonzero old projection in both output slots. A signed permutation has exactly
one nonzero entry in its first column.

Contradiction.

Thus any branch that creates a nonzero period is terminally impossible.

---

## 6. Finite-index quadratic branch is impossible

Suppose for some positive integer `N` the dilated envelope

\[
F(n,m)=f(Nn,Nm)
\]

has constant second differences in a full rank-two basis. Exact finite
difference integration gives a degree-at-most-two polynomial on `Z^2`.

Explicitly, if
`Delta_e^2 F=A_0`, `Delta_e Delta_f F=B_0`, and
`Delta_f^2 F=C_0` are constants, subtract

\[
A_0 {n\choose 2}+B_0 nm+C_0 {m\choose 2}.
\]

The residual has all second differences zero, hence is affine on `Z^2`.
This proves exact polynomial integration without any continuity assumption.

Because `F(-n,m)=F(n,m)` and `F(0,0)=0`, the resulting polynomial has the form

\[
F(n,m)=\alpha n^2+\beta m^2+\gamma m. \tag{Q}
\]

Nonnegativity on all integer multiples of the coordinate axes gives

\[
\alpha\ge0,\qquad \beta\ge0.
\]

Old-projection positivity gives

\[
\alpha=F(1,0)>0.
\]

Write

\[
Pe=(a,b),\qquad Re=(c,d).
\]

A0 gives `a!=0` and `c!=0`.

Set `y=0` in (E), then apply it to `x=t e` for the dilated function `F`:

\[
F(tPe)+F(tRe)=F(te).
\]

Comparing the `t^2` coefficients gives

\[
\alpha(a^2+c^2)+\beta(b^2+d^2)=\alpha. \tag{Q1}
\]

But `a,c` are nonzero integers, so `a^2+c^2>=2`. Since `alpha>0` and
`beta>=0`, the left side is strictly larger than or equal to `2 alpha`, while
the right side is `alpha`.

Contradiction.

Thus every exact route to finite-index quadraticity is also terminally
impossible.

---

## 7. Block-rank classification

We now classify the possible ranks of `P,Q,R,S`. This replaces the false
standalone Lemma 3.3.

### 7.1 Any zero block is impossible

- If `P=0`, then `Pe=0`, contradicting A0.
- If `R=0`, then `Re=0`, contradicting A0.

Suppose `Q=0`. Since `A` is block triangular and unimodular,

\[
P,S\in GL_2(Z).
\]

From (E) with `x=0`,

\[
f(Sy)=f(y).
\]

Therefore, for fixed `x` and arbitrary `z=Sy`,

\[
f(z+Rx)-f(z)=f(x)-f(Px),
\]

a constant independent of `z`. A globally nonnegative function cannot have a
nonzero constant first difference along a nonzero step in both forward and
backward iteration. Hence that constant is zero, so every `Rx` is a period.
In particular `Re` is a period, but A0 gives it nonzero old projection,
contradicting Section 5.

The case `S=0` is symmetric: `Q,R in GL_2(Z)`, `f(Qy)=f(y)`, and every `Px`
is a period; `Pe` violates A0 plus Section 5.

Hence all four blocks are nonzero.

### 7.2 A row containing two rank-two blocks gives full quadraticity

Suppose `rank P=rank Q=2`. By Lemma 4.1 choose `N` such that

\[
N Z^2\subseteq \operatorname{im}P\cap\operatorname{im}Q.
\]

For `F(z)=f(Nz)`, (D1) implies

\[
\Delta_u\Delta_v F
\]

is constant for every `u,v in Z^2`. Hence `F` is quadratic, contradicting
Section 6.

The same argument applies to `rank R=rank S=2`.

### 7.3 A rank-two/rank-one row creates a hub

Suppose, for example, `rank P=2` and `rank Q=1`. After one common dilation,
there is a nonzero primitive line direction `ell` such that for

\[
F(z)=f(Nz)
\]

one has

\[
\Delta_\ell\Delta_v F\equiv C(v)
\qquad\forall v\in Z^2. \tag{H}
\]

Call the rational line `L=span_Q(ell)` a **hub line**.

`J`-invariance transports hubs to hubs. If `L` and `JL` are distinct, they are
independent in the rational plane `Q^2`; on the finite-index lattice generated by the two hub
directions all three basis second differences are constant. This is the
quadratic branch, already impossible.

Therefore a nonquadratic hub must be a rational `J`-invariant line. The only
such lines are

\[
E=\mathbf Q e,\qquad F=\mathbf Q f.
\]

The same reasoning applies to any rank-two/rank-one row ordering.

#### 7.3.1 Old-axis hub `E`

After an additional dilation, exact integration of

\[
\Delta_e^2 F=\text{const},
\qquad
\Delta_e\Delta_f F=\text{const}
\]

gives

\[
F(n,m)=\alpha n^2+\eta nm+\lambda n+h(m).
\]

`J`-evenness kills the mixed and old-linear terms:

\[
F(n,m)=\alpha n^2+h(m).
\]

Here `h(m)=F(0,m)>=0`, `h(0)=0`, and old positivity gives `alpha>0`.

The axis specialization of (E) yields

\[
\alpha(a^2+c^2)t^2+h(bt)+h(dt)=\alpha t^2.
\]

A0 gives `a,c!=0`, hence `a^2+c^2>=2`, while `h>=0`. Contradiction.

#### 7.3.2 New-axis hub `F`

Exact integration and `J`-evenness give

\[
F(n,m)=g(n)+\beta m^2+\gamma m, \tag{Hf}
\]

where `g` is even, `g(0)=0`, and `g(n)>0` for `n!=0`.

If `g` has any constant mixed second difference

\[
\Delta_a\Delta_b g=\text{const}
\]

with nonzero integers `a,b`, then `g` is quadratic on a finite-index
arithmetic progression. Indeed, for `L=lcm(|a|,|b|)`,

\[
(T^L-1)^2
=
\Bigl(1+T^{|a|}+\cdots+T^{L-|a|}\Bigr)
\Bigl(1+T^{|b|}+\cdots+T^{L-|b|}\Bigr)
(T^{|a|}-1)(T^{|b|}-1).
\]

Thus `Delta_L^2 g` is constant, so `g(Lk)` is an exact quadratic polynomial in
`k`. Since the `m` part in (Hf) is already quadratic, this is the impossible
finite-index quadratic branch.

It remains to assume that no such nonzero-step second difference of `g` is
constant.

Apply mixed differences in any two distinct input coordinate variables to the
four-coordinate conservation identity. The input side has zero mixed
difference because (Hf) is coordinate-separable. Since `A` is onto, the four
output coordinates vary independently. By the independence lemma, for every
output row each corresponding one-variable mixed difference is constant.

In particular, if either old-output row (rows 1 and 3 of `A`) had two nonzero
entries in distinct input columns, `g` would have a forbidden constant
`Delta_a Delta_b` with `a,b!=0`.

Hence each old-output row has support size at most one.

A0 says entries `(1,1)` and `(3,1)` are both nonzero. Therefore both old rows
are supported only in the first input column, so they are linearly dependent.
Then `det A=0`, contradicting `A in GL_4(Z)`.

Thus every rank-two/rank-one hub branch is impossible.

### 7.4 Residual case: all four blocks have rank one

This is the only nonzero block-rank pattern not already eliminated.

Factor each integer rank-one block as

\[
P=p\alpha,\quad Q=q\beta,\quad R=r\gamma,\quad S=s\delta,
\]

where `p,q,r,s` are nonzero integer columns and
`alpha,beta,gamma,delta` are nonzero integer row covectors.

Invertibility forces the two output directions in each row to be independent
and the two input covectors for each input slot to be independent.

A direct determinant factorization gives

\[
\det A
=
-\det[p\ q]\,
 \det[r\ s]\,
 \det\!\begin{bmatrix}\alpha\\ \gamma\end{bmatrix}\,
 \det\!\begin{bmatrix}\beta\\ \delta\end{bmatrix}. \tag{R1}
\]

Every factor on the right is a nonzero integer. Since `det A=±1`, each factor
has absolute value one. In particular,

\[
C=\begin{bmatrix}\alpha\\ \gamma\end{bmatrix}\in GL_2(Z). \tag{R2}
\]

Set `y=0` in (E). In the integral channel coordinates

\[
(u,v)=C x=(\alpha x,\gamma x),
\]

we obtain an exact global separable representation

\[
F_C(u,v)=g(u)+h(v), \tag{R3}
\]

where

\[
g(u)=f(pu),\qquad h(v)=f(rv).
\]

Both are nonnegative.

Inherited `J` becomes

\[
K=CJC^{-1}\in GL_2(Z),\qquad K^2=I,\quad\det K=-1. \tag{R4}
\]

`J`-invariance of `f` says

\[
g(k_{11}u+k_{12}v)+h(k_{21}u+k_{22}v)
=
g(u)+h(v). \tag{R5}
\]

There are only three integral conjugacy behaviors relevant here.

#### (a) Both rows of `K` are mixed

If

\[
k_{11}k_{12}\ne0,\qquad k_{21}k_{22}\ne0,
\]

take the mixed `Delta_u Delta_v` of (R5). The two transformed coordinates are
independent because `K` is invertible, so

\[
\Delta_{k_{11}}\Delta_{k_{12}}g=\text{const},
\qquad
\Delta_{k_{21}}\Delta_{k_{22}}h=\text{const}.
\]

By the exact univariate finite-index lemma above, both `g` and `h` are
quadratic on arithmetic progressions. Since `C` is unimodular, `f` is
quadratic on a finite-index sublattice of `Z^2`.

This is the impossible quadratic branch.

#### (b) `K` is triangular but not diagonal

Up to exchanging channel names,

\[
K=
\begin{pmatrix}\varepsilon&0\\ t&-\varepsilon\end{pmatrix},
\qquad \varepsilon=\pm1,\quad t\ne0.
\]

If `epsilon=-1`, (R5) gives

\[
g(-u)+h(tu+v)=g(u)+h(v).
\]

For fixed `u=1`, `Delta_t h(v)` is constant in `v`. Since `h>=0` on the whole
integer line, that constant must be zero; hence `h` has nonzero period `t`.

If `epsilon=1`, (R5) gives

\[
h(tu-v)=h(v).
\]

At `u=0` this is reflection invariance `h(-v)=h(v)`; at `u=1` it is reflection
about `t/2`. Their composition gives `h(v+t)=h(v)`.

Since `C` is unimodular, a nonzero period in either channel corresponds under
`C^{-1}` to a nonzero lattice period of `f`. Thus the triangular non-diagonal
case creates a nonzero period of `f`, already impossible by Section 5.

The upper-triangular cases are identical with `g` and `h` exchanged.

#### (c) `K` is diagonal

Then the integral channel covectors `alpha,gamma` are `J` eigen-covectors. A
unimodular eigen-covector basis for

\[
J(n,m)=(-n,m)
\]

is, up to sign and order, exactly the old/new coordinate covectors. Therefore
one of `alpha(e)`, `gamma(e)` is zero.

But

\[
Pe=p\,\alpha(e),\qquad Re=r\,\gamma(e).
\]

So one of the elementary outputs is zero already on the free quotient,
contradicting A0.

#### Off-diagonal monomial swap cannot occur integrally

For completeness, write

\[
C=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad \det C=\pm1.
\]

An exact calculation gives

\[
CJC^{-1}
=
\frac1{\det C}
\begin{pmatrix}
-ad-bc & 2ab\\
-2cd & ad+bc
\end{pmatrix}. \tag{R6}
\]

If this were a pure off-diagonal channel swap, its diagonal entries would
vanish. Then `ad+bc=0`, while

\[
\det C=ad-bc=2ad,
\]

which cannot equal `±1` for integers `a,d`.

Hence the all-rank-one residual has no fourth case.

This completes the block-rank classification.

---

## 8. Corrected F7 no-go theorem

Sections 7.1–7.4 exhaust all rank patterns of the four nonzero `2x2` blocks.

Every branch yields one of:

1. direct A0 failure;
2. a nonzero period, eliminated by the accepted rank-one descended theorem;
3. finite-index quadraticity, eliminated by the A0 coefficient inequality;
4. a new-axis hub row-support singularity;
5. an integral eigenchannel residual, again directly violating A0.

Therefore there is no

\[
A\in GL_4(Z)
\]

satisfying the exact free conservation identity together with nonnegativity,
old-projection positivity, inherited `J` invariance, and A0.

Since these properties are consequences of any F7 pair `(M,q)`, no F7 pair
exists.

Thus:

`F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_CLASSIFIED = NO_GO`.

The numerical elementary balance equation `q(u)=q(v)=1/2` was not needed.

---

## 9. Selector / participation consequences retained

Because the feasible model set is empty:

- `F7_NEW_FREE_DIRECTION_PARTICIPATION_CLASSIFIED = NO_SUCCESSFUL_MODEL`;
- `F7_RANK_TWO_FREE_BLOCK_CONSTRAINTS_CLASSIFIED = FEASIBLE_SET_EMPTY`;
- `F7_SCALAR_AND_MIXING_SELECTOR_STATUS_CLASSIFIED = EMPTY`;
- `F7_MIXING_PHYSICAL_EQUIVALENCE_AND_MINIMUM_STATUS_CLASSIFIED = EMPTY_QUOTIENT`.

These are task-level consequences only. They do not promote A0, the F6
working extension, or any downstream semantic interpretation to Foundation
truth.

---

## 10. Why the old Lemma 3.3 must stay retracted

The exact counterexample

\[
f(n,m)=n^2+|m|,
\quad
A(n_1,m_1,n_2,m_2)=(n_1,m_2,n_2,m_1)
\]

shows that the following implication is false:

> period-free + exact separable conservation + non-whole-slot-block-monomial
> `A` ⇒ finite-index quadratic `f`.

Indeed:

- `A` is unimodular;
- conservation is an identity;
- `f` is nonnegative and `J`-even;
- a period `(a,b)` would force `a=0` from the coefficient of `n`, then `b=0`
  from the two tails of `|m+b|=|m|`;
- on any `N Z^2`, the restriction to the new axis is `|Nm|`, which cannot be
  one quadratic polynomial for positive and negative integers;
- `A` is not whole-slot block-monomial.

What fails is exactly A0.

So the repair is not merely a longer proof of the old sentence. It is a
change in intermediate theorem statement while preserving the same F7 task
verdict.

This distinction is mandatory for future reuse: the old standalone
period/quadratic lemma must not be cited as a theorem.

---

## 11. Deterministic checker

Task-local checker:

`research_checks/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_CHECK_20260903.py`

It certifies:

1. the exact old-Lemma-3.3 counterexample and its A0 failure;
2. `B adj(B)=det(B) I` saturation across exact integer regressions;
3. the exact translation-operator identity giving the univariate finite-index
   quadratic lemma;
4. the all-rank-one determinant factorization (R1);
5. the integral `J`-channel conjugacy trichotomy over a deterministic `GL_2(Z)`
   regression window plus the exact parity obstruction to off-diagonal swap;
6. the A0 coefficient and row-support algebra used in the hub branches;
7. all four explicit witness ablations inherited from the frozen F7 result,
   including the exact split-channel witness that conserves the scalar and
   satisfies A0/balance only after dropping `J` invariance.

The checker records:

`bounded_search_used_as_universal_proof = false`.

Local deterministic replay before commit:

`PASS`

with payload SHA-256:

`b81e60d2e5f649d11c17f685f644b107ca08f303932c87de45076e1f9ff09794`.

No general-purpose tool was created; the artifact is task-local. Therefore no
tool-candidate / promote-tool workflow is triggered.

---

## 12. Ten mandatory ablations

The revision preserves all ten legacy ablation questions. A1–A4 are replayed
by exact witnesses in the revision checker; A5–A10 are theorem-scope
implications.

### A1 — remove A0

Exact survivor remains:

`DROP_A0 -> EXACT_SURVIVOR_EXISTS`.

The inherited witness is balanced and conserving, but one elementary output has
zero old projection. This is also exactly why the counterexample to old Lemma
3.3 does not refute the corrected F7 theorem.

### A2 — remove free-projection zero separation

Exact six-periodic survivor remains:

`DROP_FREE_PROJECTION_ZERO_SEPARATION -> EXACT_SURVIVOR_EXISTS`.

The witness is balanced, A0-compatible, and conserving, but has a nonzero old
state with scalar zero.

### A3 — remove unary invariance of q

Exact split-channel survivor remains:

`DROP_UNARY_INVARIANCE -> EXACT_SURVIVOR_EXISTS`.

The existing `UNARY_DROP` matrix preserves

\[
q_{\neg J}(n,m)
=
\frac12\bigl(1_{n-m\ne0}+1_{n-2m\ne0}\bigr),
\]

and satisfies A0/balance, but

\[
q_{\neg J}(2,1)=1/2,\qquad q_{\neg J}(-2,1)=1,
\]

so `J` invariance fails. This directly matches the corrected all-rank-one
channel analysis.

### A4 — remove exact global marked conservation

The inherited involutory marked automorphism still satisfies the remaining
elementary marked conditions but has an explicit input with

`Q_in=1/2`, `Q_out=1`.

Effect:

`DROP_EXACT_GLOBAL_CONSERVATION -> EXACT_MARKED_AUTOMORPHISM_EXISTS`.

### A5 — remove elementary balance

Balance is not used anywhere in the corrected obstruction.

Effect:

`DROP_ELEMENTARY_BALANCE -> NO_GO_PERSISTS`.

### A6 — remove additive invertibility of M

The corrected proof uses surjectivity/invertibility in three essential places:
independent output variation in (D1), descent of the pair-period subgroup, and
the determinant/unit classification of the all-rank-one residual.

Effect:

`DROP_ADDITIVE_INVERTIBILITY -> CURRENT_NO_GO_PROOF_OPENS / OUTSIDE_F7_SCOPE`.

No noninvertible no-go is claimed.

### A7 — remove marker relabeling equivalence

This changes only physical-class quotient bookkeeping; the admissible set is
already empty.

Effect:

`DROP_MARKER_RELABELING_EQUIVALENCE -> NO_EFFECT_ON_EXISTENCE`.

### A8 — remove inverse-orientation equivalence

Again this changes only class identification after existence.

Effect:

`DROP_INVERSE_ORIENTATION_EQUIVALENCE -> NO_EFFECT_ON_EXISTENCE`.

### A9 — remove named tau preservation

The corrected proof never requires `M` to fix the named torsion generator.
It requires only that an additive automorphism preserve the characteristic
torsion subgroup setwise, so the finite torsion-fiber bijection used to derive
(E) remains valid.

Effect:

`DROP_NAMED_TAU_PRESERVATION -> NO_GO_PERSISTS`
while additive automorphism is retained.

### A10 — force the new free direction f to remain spectator

This narrows the model class. The old-projection dynamics reduce directly to
the accepted rank-one positive-separation free-block obstruction, so A0 fails.

Effect:

`FORCE_F_SPECTATOR -> NO_GO_PERSISTS`.

Thus the corrected proof has no theorem/model mismatch against the mandatory
ten-ablation packet.

---

## 13. Driver-facing boundary

Requested Driver action:

`REVIEW SAME TASK / DO NOT OPEN F8`

The Driver should verify specifically:

1. the retraction of old standalone Lemma 3.3 is accepted rather than hidden;
2. the envelope reduction (E) remains unchanged;
3. the period descent correctly invokes only the accepted F4 free-block theorem;
4. the finite-index saturation is explicit and sufficient;
5. the rank-two/rank-one hub branches cover every case containing a rank-two
   block;
6. the all-rank-one determinant factorization and integral `J`-conjugacy
   classification are exact;
7. no bounded checker result is substituted for the universal theorem;
8. no fresh clean-blind / target-leak pass is claimed by this revision context.

If accepted, the correct task-level conclusion is still

`F7_NO_BALANCED_RANK_TWO_MIXING_EXISTS`.

No Working Truth promotion, Foundation promotion, ring/norm/square-law/wave
semantics, novelty claim, or F8 successor is granted by this return.
