# A3 Partial-Move Scale Coherence Revision — Exact Result

Task: `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION`  
Publication: `TP2-E6E8A3DC37930B4CF4AA`  
Researcher: `EM-A3SCR-9FE7C5`  
Claim: `chatgpt-a3scr-20260828-2332-9fe7c5`

Status: `PASS / CORRECTED_H4_EXACT / SUPPORT_TRANSITION_PAIR_GROUPOID_CLASSIFICATION / FRAME_ONLY_IFF_REFUTED / NO_FOUNDATION_PROMOTION`

## 1. Scope and frozen inputs

This revision starts exactly at the Driver-rejected H4 unit. It preserves without recomputation:

- the A3 carrier
  \[
  \Lambda_3=\{x\in\mathbb Z^4:\sum_i x_i=0\},
  \qquad r(x)=\max_i|x_i|;
  \]
- the nested balls and shells
  \[
  B_n=\{r\le n\},\qquad S_n=B_n\setminus B_{n-1};
  \]
- the faithful 24-frame action
  \[
  R_g=\operatorname{sgn}(g)P_g|_{\Lambda_3},
  \qquad G=S_4;
  \]
- the pointer target
  \[
  a_n=(n,-n,0,0)
  \]
  with fixed residual stabilizer
  \[
  H=\operatorname{Stab}_G(a_n)=\{e,(12)\};
  \]
- depth-1 shielding and depth-2 first coupling;
- the already accepted fixed-\(H\) pair-groupoid / double-coset algebra.

The false statement is not reused: the relative frame double coset alone does **not** classify the actual state-level scale square for scale-dependent prefix support.

## 2. Explicit state and operation types

Fix a finite set of marker names \(I\). A raw finite state at scale \(n\) consists of

1. one distinguished shell pointer \(p_j\in S_j\) for each exposed shell \(1\le j\le n\); and
2. a finite named-marker map \(q:I\to B_n\).

The checker uses the equivalent serialized form of named marker-position pairs. All statements below are pointwise on marker positions and therefore extend componentwise to any finite payload alphabet or full labeling of \(B_n\).

Restriction
\[
\rho_{n+1,n}:X_{n+1}\to X_n
\]
drops the outer pointer \(p_{n+1}\) and every payload marker outside \(B_n\).

For \(1\le d\le n\), define the depth-\(d\) prefix support
\[
U_{n,d}=B_n\setminus B_{n-d}
       =\bigcup_{j=n-d+1}^{n}S_j.
\]

The exact scale-indexed action is
\[
D_{n,d}(g)x=
\begin{cases}
R_gx,&x\in U_{n,d},\\
x,&x\in B_{n-d}.
\end{cases}
\]

Because every \(R_g\) preserves radius, \(U_{n,d}\) is \(G\)-invariant. Hence
\[
D_{n,d}(gh)=D_{n,d}(g)D_{n,d}(h),
\]
so \(D_{n,d}\) is an honest finite group action on \(B_n\), not merely a partial formula.

For the pointer target \(a_n\), define
\[
\mathcal W_n(x)=\{g\in G:R_gp_n=a_n\}.
\]
If \(p_n=R_{g_n}^{-1}a_n\), then exactly
\[
\mathcal W_n(x)=Hg_n.
\]
The alignment normalization is therefore the relation
\[
C_{n,d}(x)=\{D_{n,d}(u)x:u\in Hg_n\}.
\]
If the boundary pointer is unreachable, \(C_{n,d}(x)=\varnothing\).

The maximally discriminating observation language is the raw restricted marker state. The residual-\(H\) observation is its orbit under the lower-scale action \(D_{n,d}(H)\). No arbitrary solver representative is declared canonical.

## 3. Exact support-transition theorem

Fix an edge \(n+1\to n\) and \(1\le d\le n\). The retained part of the upper-scale support is
\[
O_{n,d}
=
U_{n+1,d}\cap B_n
=
\bigcup_{j=n-d+2}^{n}S_j,
\]
while the lower-scale action has one additional shell
\[
T_{n,d}=S_{n-d+1}.
\]

Thus
\[
U_{n,d}=T_{n,d}\sqcup O_{n,d}.
\]

Write
\[
\overline D_{n+1,d}(g)=D_{n+1,d}(g)|_{B_n}.
\]

### Theorem 3.1 — support-transition representation

Define
\[
J_{n,d}(g)
=
D_{n,d}(g)\,\overline D_{n+1,d}(g)^{-1}.
\]

Then
\[
J_{n,d}(g)x=
\begin{cases}
R_gx,&x\in T_{n,d},\\
x,&x\notin T_{n,d}.
\end{cases}
\]

Consequently \(J_{n,d}:G\to\operatorname{Sym}(B_n)\) is a group homomorphism whose entire support is the single transition shell \(T_{n,d}\).

**Proof.** On \(B_{n-d}\), both scale actions are identity. On \(O_{n,d}\), both apply the same \(R_g\), hence cancel. On the single shell \(T_{n,d}\), the lower action applies \(R_g\) while the restricted upper action is identity. Radius invariance makes the three regions invariant, so composition is pointwise and the homomorphism law follows from \(R_{gh}=R_gR_h\). ∎

This is the exact term missing from the rejected frame-only H4.

### Corollary 3.2 — raw operation descent

For every \(n\ge d\ge1\),
\[
\rho_{n+1,n}D_{n+1,d}(g)
=
D_{n,d}(g)\rho_{n+1,n}
\]
on **all** raw states iff \(g=e\).

**Proof.** Equality on all states is equivalent to \(J_{n,d}(g)=1\). If \(g\ne e\), the sign-twisted \(S_4\) representation acts nontrivially on every shell \(S_k\), \(k\ge1\): the shell contains all vectors \(k(e_i-e_j)\), which span the A3 carrier, and the 24-frame representation is faithful. Therefore \(J_{n,d}(g)\) is nontrivial on \(T_{n,d}\). ∎

So nontrivial prefix moves do not descend raw across scale. Any valid normalization must either retain the transition action or pass to an observation quotient on which it acts trivially.

## 4. Complete two-aligner cross-scale factorization

Let \(g_n\) be a chosen lower-scale aligner and \(g_{n+1}\) an upper-scale aligner. Define the exact raw defect permutation
\[
F_{n,d}(g_n,g_{n+1})
=
D_{n,d}(g_n)\,
\overline D_{n+1,d}(g_{n+1})^{-1}.
\]

### Theorem 4.1 — exact factorization

\[
\boxed{
F_{n,d}(g_n,g_{n+1})
=
J_{n,d}(g_n)\,
\overline D_{n+1,d}(g_ng_{n+1}^{-1})
}
\]

and the two factors have disjoint supports \(T_{n,d}\) and \(O_{n,d}\), hence commute.

Equivalently,
\[
F_{n,d}(g_n,g_{n+1})x=
\begin{cases}
x,&r(x)\le n-d,\\[2mm]
R_{g_n}x,&r(x)=n-d+1,\\[2mm]
R_{g_ng_{n+1}^{-1}}x,&n-d+2\le r(x)\le n.
\end{cases}
\]

**Proof.** Insert
\(\overline D_{n+1,d}(g_n)^{-1}\overline D_{n+1,d}(g_n)\)
between the two scale actions and use the group-action law:
\[
D_n(g_n)\overline D_{n+1}(g_{n+1})^{-1}
=
[D_n(g_n)\overline D_{n+1}(g_n)^{-1}]
[\overline D_{n+1}(g_n)\overline D_{n+1}(g_{n+1})^{-1}].
\]
The first bracket is \(J_{n,d}(g_n)\); the second is
\(\overline D_{n+1,d}(g_ng_{n+1}^{-1})\).
Their supports are exactly the transition and overlap bands above. ∎

This splits H4 into two independent typed phenomena:

- `SUPPORT_TRANSITION`: the absolute lower aligner \(g_n\) acting on the newly exposed shell;
- `FRAME_PHASE_OVERLAP`: the relative element \(g_ng_{n+1}^{-1}\) acting where both scales already act.

The rejected theorem retained only the second factor.

## 5. Choice-independent corrected radial defect

For a reachable state, let
\[
L_n=Hg_n,\qquad L_{n+1}=Hg_{n+1}
\]
be the exact alignment left cosets.

Define the **typed support-aware pair-groupoid arrow**
\[
\Omega_{n,d}
=
(n,d;L_n,L_{n+1}).
\]

Its exact state-level defect relation is
\[
\mathfrak D(\Omega_{n,d})
=
\left\{
F_{n,d}(u,v):
u\in L_n,\ v\in L_{n+1}
\right\}.
\]

This set is representative-independent by construction. More importantly, it is complete: for every upper-path aligned output using \(v\in L_{n+1}\) and every lower-path aligned output using \(u\in L_n\), the latter is obtained from the former by the unique site permutation \(F_{n,d}(u,v)\).

Thus \(\Omega_{n,d}\), interpreted through the scale-indexed actions \(D_{n,d}\), exactly classifies the actual state-level comparison relation.

### Corrected H4 criterion

For a declared observation quotient \(Q_n\), the two normalization routes agree on a state \(x\) iff every paired path outcome identified by \(\mathfrak D(\Omega_{n,d})\) has the same \(Q_n\)-image.

For the raw state language this reduces to the fixed-point criterion for the exact \(F\)-maps. Universal raw commutation requires the full defect relation to act trivially; for a common nontrivial aligner this is impossible by Corollary 3.2.

This is an exact theorem, not a finite-radius heuristic.

## 6. Projection to the accepted fixed-H algebra

The previously accepted pair groupoid has objects \(H\backslash G\) and arrows
\[
(L_n,L_{n+1}).
\]
Its deterministic composition is
\[
(L_n,L_{n+1})\circ(L_{n+1},L_{n+2})
=
(L_n,L_{n+2}).
\]

The old frame-phase defect is the projection
\[
\pi_{\mathrm{frame}}(\Omega_{n,d})
=
Hg_ng_{n+1}^{-1}H.
\]

This is well-defined under representative changes and is exactly the accepted double-coset relation image of the pair-groupoid arrow.

The corrected hierarchy is therefore
\[
(n,d;Hg_n,Hg_{n+1})
\longmapsto
\mathfrak D(\Omega_{n,d})
\longmapsto
Hg_ng_{n+1}^{-1}H.
\]

The first map adds the scale-dependent representation \(D_{n,d}\); the second forgets the transition-shell action.

### Exact special-case recovery

The fixed-H frame algebra is H4-complete precisely at an observation level where the support-transition factor is invisible:
\[
Q_nJ_{n,d}(u)=Q_n
\quad
\text{for every relevant }u\in L_n.
\]
Under that hypothesis, only the overlap relative-phase factor survives and the accepted pair-groupoid / double-coset relation algebra is the correct quotient description.

Hence the old algebra is not wrong; it is a valid quotient after an explicit transition-annihilation hypothesis. That hypothesis was absent in the rejected parent H4.

## 7. Exact no-go for any frame-only H4 classifier

Take
\[
g=(23),\qquad p=(1,-1,0,0)\in S_1.
\]
At the edge \(3\to2\) with \(d=2\), use the same aligner at both scales:
\[
g_2=g_3=g.
\]

Then
\[
\pi_{\mathrm{frame}}=Hgg^{-1}H=H=C_0.
\]

But
\[
J_{2,2}(g)p=R_gp=(-1,0,1,0).
\]
Since
\[
H=\{e,(12)\}
\]
fixes \(p\),
\[
R_gp\notin H\cdot p.
\]

Therefore the two state-level routes remain inequivalent even after the declared residual-\(H\) quotient.

A stronger collision uses the two typed pair-groupoid arrows
\[
(2,2;H,H)
\quad\text{and}\quad
(2,2;Hg,Hg).
\]
Both project to the same frame defect \(C_0\), but their transition relations on \(p\) differ. Thus **no function of the relative double coset alone** can classify H4 for the declared prefix semantics.

This freezes the Driver counterexample as a theorem-level no-go, not merely a regression.

## 8. H5 revision — observation spectrum

The parent signature must not use the double-coset label as the whole radial defect. Replace each such component by the typed arrow or its exact state-level defect relation:
\[
\Sigma_N^{\mathrm{corr}}(x)
=
(\mathcal I_1,\Omega_1,\mathcal I_2,\Omega_2,\ldots).
\]

The diagnostic notions become:

- `FRAME_DEFECT_BIRTH_RADIUS`: first nontrivial \(\pi_{\mathrm{frame}}(\Omega_n)\);
- `SUPPORT_DEFECT_BIRTH_RADIUS`: first radius at which the \(J\)-factor acts nontrivially on the declared observation;
- `DEFECT_BIRTH_RADIUS`: minimum of the two after the declared quotient;
- `STABILIZATION_RADIUS`: first scale after which the full \(\mathfrak D(\Omega_n)\), not only its frame projection, is observation-trivial;
- `PERIODIC_SCALE_ORBIT`: periodicity of typed pair-groupoid arrows / induced defect relations;
- `BOUNDARY_TO_BULK_COLLISION`: equality of the corrected full finite signature, not merely the double-coset sequence.

The parent shielding theorem remains valid.

## 9. H6 revision — corrected minimum three-radius prototype

The old \(B_1\subset B_2\subset B_3\) phase example remains valid as a fixed-\(H\) algebra example, but it is **not** a uniform depth-2 two-edge state-level H4 prototype: the lower action \(D_{1,2}\) is outside the declared type \(d\le n\).

The smallest three-radius carrier supporting depth 2 on both adjacent edges is
\[
B_2\subset B_3\subset B_4.
\]

Use
\[
g=(23)
\]
at all three scales and compatible pointers
\[
p_k=R_g^{-1}a_k,\qquad k=2,3,4.
\]
Add payload markers
\[
q_1=a_1\in S_1,\qquad q_2=a_2\in S_2.
\]

### Edge \(4\to3\)

- scale 4 depth 2 acts on \(S_4\cup S_3\), so it fixes \(q_2\);
- after restriction, scale 3 depth 2 acts on \(S_3\cup S_2\), so it moves \(q_2\).

The boundary pointer \(p_3\) reaches \(a_3\) on both routes, but the \(q_2\) outputs are not residual-\(H\)-equivalent.

### Edge \(3\to2\)

- scale 3 depth 2 fixes \(q_1\in S_1\);
- scale 2 depth 2 acts on \(S_2\cup S_1\), so it moves \(q_1\).

Again the pointer aligns on both routes and the payload outputs are not residual-\(H\)-equivalent.

Yet on both edges
\[
Hg g^{-1}H=C_0.
\]

So the corrected three-radius regression has
\[
\text{old frame defects }(C_0,C_0)
\]
while
\[
\text{actual state squares }(\text{noncommuting},\text{noncommuting}).
\]

This is stronger and more directly diagnostic than the old `C2,C2 -> C0` compressed-phase example.

## 10. Composition and tool verdict

No new shared tool family is required.

The exact repaired object is a composition of already accepted ingredients:

- finite symmetry action \(G\curvearrowright B_n\);
- operation-safe quotient discipline;
- the fixed-\(H\) left-coset pair groupoid;
- relation/BRC semantics for nonunique aligners;
- a task-local scale-indexed support representation \(D_{n,d}\);
- the transition-shell cocycle/representation \(J_{n,d}\).

The decisive new task-local theorem is the exact factorization
\[
F=J\times(\text{overlap relative phase})
\]
on disjoint radial bands.

Tool verdict:

`COMPOSE_EXISTING_TOOLS / TASK_LOCAL_SUPPORT_TRANSITION_OPERATOR / NO_NEW_SHARED_FAMILY`

## 11. Deterministic replay

Checker:

`scripts/check_a3_shell_partial_move_scale_coherence_revision.py`

The checker verifies:

- \(D_{n,d}\) group-action laws;
- \(J_{n,d}\) group-action laws and transition-shell support;
- exhaustive two-aligner factorization on the operational \(S_4\) finite carriers;
- nontriviality of \(J\) for every nonidentity frame element checked;
- all fixed-\(H\) alignment-coset identities on radii 1–4;
- the pair-groupoid-to-double-coset projection law;
- the frozen Driver counterexample;
- the stronger `(H,H)` versus `(Hg,Hg)` frame-projection collision;
- the corrected \(B_2\subset B_3\subset B_4\) two-edge depth-2 prototype;
- residual-\(H\) inequivalence on both state-level failures.

Frozen checker certificate summary:

- group size: `24`;
- residual stabilizer size: `2`;
- left-coset objects: `12`;
- exact site factorization checks: `364032`;
- exact \(D\) homomorphism site checks: `364032`;
- exact \(J\) homomorphism site checks: `364032`;
- pair-groupoid projection representative checks: `576`;
- transition-faithfulness group checks: `96`;
- mandatory Driver counterexample: `PASS`;
- frame-only classifier: `REFUTED`;
- corrected three-radius prototype: `B2<B3<B4`;
- adjacent old frame defects: `C0,C0`;
- adjacent state-level squares: `NONCOMMUTING,NONCOMMUTING`.

## 12. Terminal classification and boundary

Hard target:

`A3_PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_EXACTLY_CLASSIFIED`

Disposition:

`SATISFIED_FOR_THE_DECLARED_PREFIX_SUPPORT_SEMANTICS`.

What is closed:

1. the exact raw operation-descent criterion;
2. the exact support-transition term omitted by the parent theorem;
3. the complete two-aligner state-level defect factorization;
4. a representative-independent support-aware pair-groupoid classifier;
5. the exact projection law to the accepted fixed-\(H\) double-coset algebra;
6. an exact no-go for frame-only H4 classification;
7. corrected H5/H6 typing and prototype.

What is not claimed:

- no general theorem for arbitrary object-dependent partial groupoids;
- no varying-\(H_n\) theorem;
- no physical interpretation of the shell model;
- no Foundation promotion;
- no claim that every useful observation quotient must retain the full raw defect.

A future successor is justified only if it changes one of those boundaries, e.g. scale-varying stabilizers, object-dependent legal domains, or non-conjugate target stabilizers. The declared prefix-support H4 itself is closed by the support-transition pair-groupoid classification above.
