# A3 Recursive Shell Alignment Tomography Redispatch — Radial Relation Coherence

Task: `RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY`  
Publication: `TP2-78C59019AE494DF41F65`  
Researcher: `EM-A3SHELL-6F4B92`  
Claim: `chatgpt-a3shell-20260828-1543-6f4b92`  
Status: `EXACT THEOREM PACKAGE / FIXED-STABILIZER COHERENCE CLOSED / NO FOUNDATION PROMOTION`

## 1. Redispatch target

The first finite package on Draft PR #779 established the exact A3 carrier, the residual pointer stabilizer

\[
H=\{e,(12)\}\le S_4,
\]

the seven radial double-coset classes in \(H\backslash S_4/H\), and the minimal non-single-valued witness

\[
C_2C_2=\{C_0,C_2\}.
\]

This redispatch answers the coherence question at the strongest scope justified by the frozen model:

> Whenever all scale aligners live in one group \(G\) and the residual stabilizer is a fixed subgroup \(H\), the double-coset radial defect has a canonical associative set-valued composition. It is exactly the quotient of the pair groupoid on \(H\backslash G\). Single-valued defect-only composition is possible for all defects exactly when \(H\) is normal.

Thus the first package exposed **loss of determinism**, not loss of associativity.

The remaining frontier begins only when the stabilizer varies with scale, legal moves form a genuine partial groupoid rather than one group, or restriction changes the admissible interface relation.

## 2. Universal fixed-stabilizer theorem

Let \(G\) be a group and \(H\le G\). Write

\[
\mathcal D=H\backslash G/H
\]

for the set of double cosets. For \(A,B\in\mathcal D\), define

\[
A\star B=\{C\in\mathcal D:C\subseteq AB\}.
\]

Equivalently, \(C\in A\star B\) iff \(C\cap AB\ne\varnothing\). Extend the product to subsets of \(\mathcal D\) by union.

### Theorem 2.1 — exact double-coset decomposition

For \(A=HgH\) and \(B=HkH\),

\[
AB=HgHkH
\]

is left- and right-\(H\)-invariant and hence is a disjoint union of double cosets.

**Proof.** If \(x\in AB\) and \(h_1,h_2\in H\), then \(h_1xh_2\in H(AB)H=AB\). The \(H\times H\) orbits for left/right multiplication are exactly the double cosets. Therefore

\[
AB=\bigcup_{C\in A\star B}C.
\]

No enlargement or approximation occurs. ∎

### Theorem 2.2 — associative relation-valued composition

For all \(A,B,C\in\mathcal D\),

\[
(A\star B)\star C=A\star(B\star C).
\]

The double coset \(H\) is a two-sided identity. Inversion

\[
(HgH)^*=Hg^{-1}H
\]

is an involution and satisfies

\[
(A\star B)^*=B^*\star A^*.
\]

**Proof.** By Theorem 2.1, the union of double cosets in \((A\star B)\star C\) is \((AB)C\), while the union for \(A\star(B\star C)\) is \(A(BC)\). Group multiplication is associative, so these equal \(H\)-bi-invariant subsets have the same unique double-coset decomposition. The identity and involution laws follow from \(HA=AH=A\) and \((AB)^{-1}=B^{-1}A^{-1}\). ∎

This is the exact relation/BRC layer required by the taskbook. No representative selection is needed.

## 3. Exact criterion for deterministic compression

### Theorem 3.1 — all support products are single-valued iff \(H\trianglelefteq G\)

The following are equivalent:

1. every \(A\star B\) contains exactly one double coset;
2. \(H\) is normal in \(G\);
3. the double-coset defect reduces to the ordinary quotient-group law.

**Proof.** If \(H\trianglelefteq G\), every double coset is an ordinary coset and \((Hg)(Hk)=Hgk\).

Conversely, suppose every support product is single-valued. Fix \(g\in G\). The product

\[
(HgH)\star(Hg^{-1}H)
\]

contains \(H\), because \(gg^{-1}=e\). Hence single-valuedness forces the entire set product into \(H\), giving \(gHg^{-1}\subseteq H\). Applying the same argument to \(g^{-1}\) and conjugating back gives \(H\subseteq gHg^{-1}\). Therefore \(gHg^{-1}=H\) for every \(g\), so \(H\trianglelefteq G\). ∎

Therefore no deterministic binary operation on the seven A3 defect labels can reproduce all exact paths while retaining the same compression.

## 4. Minimal deterministic lift: pair groupoid

Let

\[
\Omega=H\backslash G
\]

be the left-coset set. The pair groupoid has one arrow \((x,y):y\to x\) for every \(x,y\in\Omega\), with

\[
(x,y)\circ(y,z)=(x,z).
\]

Define

\[
\delta(Hg,Hk)=Hgk^{-1}H.
\]

### Theorem 4.1 — well-definedness

Replacing \(g\) by \(h_1g\) and \(k\) by \(h_2k\), with \(h_1,h_2\in H\), changes \(gk^{-1}\) to \(h_1gk^{-1}h_2^{-1}\), which lies in the same double coset. ∎

### Theorem 4.2 — exact projection of composition

For every composable triple \(x,y,z\in\Omega\),

\[
\delta(x,z)\in\delta(x,y)\star\delta(y,z).
\]

Conversely, if \(C\in A\star B\), then there are \(x,y,z\in\Omega\) with adjacent defects \(A,B\) and endpoint defect \(C\).

**Proof.** Write \(x=Hg, y=Hk, z=H\ell\). Then

\[
g\ell^{-1}=(gk^{-1})(k\ell^{-1}),
\]

which proves the first statement.

For exactness choose \(a\in A\), \(b\in B\) with \(ab\in C\), and set

\[
x=Ha,\qquad y=H,\qquad z=Hb^{-1}.
\]

Then \(\delta(x,y)=A\), \(\delta(y,z)=B\), and \(\delta(x,z)=HabH=C\). ∎

So the double-coset law has neither missing nor spurious outputs. It loses exactly the middle left-coset/interface state needed for single-valued composition.

## 5. Orbital relation formulation

For each \(A\in\mathcal D\), define

\[
R_A=\{(x,y)\in\Omega^2:\delta(x,y)=A\}.
\]

Then

\[
R_A\circ R_B=\bigcup_{C\in A\star B}R_C.
\]

For finite \(\Omega\), let \(M_A\) be the 0/1 adjacency matrix of \(R_A\). There are exact nonnegative integers \(p_{AB}^{C}\) with

\[
M_AM_B=\sum_C p_{AB}^{C}M_C.
\]

Here \(p_{AB}^{C}\) counts the admissible middle alignment cosets for any endpoint pair of type \(C\); right \(G\)-transitivity makes this count constant. Matrix associativity yields

\[
\sum_D p_{AB}^{D}p_{DC}^{E}=\sum_D p_{BC}^{D}p_{AD}^{E}.
\]

Thus the boolean relation lift has an exact integer multiplicity refinement.

## 6. Exact \(S_4/H\) certificate

Return to

\[
G=S_4,\qquad H=\{e,(12)\}.
\]

There are 12 left-coset objects and seven double-coset classes.

| class | representative | size | orbital valency |
|---|---|---:|---:|
| \(C_0\) | \(e\) | 2 | 1 |
| \(C_1\) | \((34)\) | 2 | 1 |
| \(C_2\) | \((23)\) | 4 | 2 |
| \(C_3\) | \((234)\) | 4 | 2 |
| \(C_4\) | \((243)\) | 4 | 2 |
| \(C_5\) | \((24)\) | 4 | 2 |
| \(C_6\) | \((13)(24)\) | 4 | 2 |

The class involution is

\[
(0,1,2,3,4,5,6)^*=(0,1,2,4,3,5,6).
\]

### Complete support table

Each entry gives the exact possible endpoint class set; for example `0,2` means \(\{C_0,C_2\}\).

| \(\star\) | \(C_0\) | \(C_1\) | \(C_2\) | \(C_3\) | \(C_4\) | \(C_5\) | \(C_6\) |
|---|---|---|---|---|---|---|---|
| \(C_0\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| \(C_1\) | 1 | 0 | 4 | 5 | 2 | 3 | 6 |
| \(C_2\) | 2 | 3 | 0,2 | 1,3 | 5,6 | 4,6 | 4,5 |
| \(C_3\) | 3 | 2 | 5,6 | 4,6 | 0,2 | 1,3 | 4,5 |
| \(C_4\) | 4 | 5 | 1,4 | 0,5 | 3,6 | 2,6 | 2,3 |
| \(C_5\) | 5 | 4 | 3,6 | 2,6 | 1,4 | 0,5 | 2,3 |
| \(C_6\) | 6 | 6 | 3,5 | 2,4 | 3,5 | 2,4 | 0,1 |

The checker verifies all \(7^3=343\) associativity triples.

### Deterministic-compression obstruction

For adjacent labels \(C_2,C_2\), the exact pair-groupoid census gives

\[
\#\{(x,y,z):\delta(x,y)=C_2,\delta(y,z)=C_2,\delta(x,z)=C_0\}=24,
\]

\[
\#\{(x,y,z):\delta(x,y)=C_2,\delta(y,z)=C_2,\delta(x,z)=C_2\}=24.
\]

Thus no deterministic law \(\mu(C_i,C_j)=C_k\) can reproduce every exact path. This strengthens the earlier three-radius witness from one representative example to a complete 48-triple orbital split.

### Integer refinement examples

The exact structure constants include

\[
M_2M_2=2M_0+M_2,
\]

\[
M_2M_3=2M_1+M_3,
\]

\[
M_6M_6=2M_0+2M_1.
\]

The positive supports agree exactly with the support table, and all 343 weighted associativity identities pass.

## 7. Interpretation for radial tomography

The exact information hierarchy is

\[
g_n\leadsto Hg_n\leadsto(Hg_n,Hg_{n+1})\leadsto Hg_ng_{n+1}^{-1}H.
\]

1. \(g_n\): representative aligner; gauge-dependent.
2. \(Hg_n\): exact aligned-coset state after removing target stabilizer redundancy.
3. \((Hg_n,Hg_{n+1})\): exact deterministic radial transport arrow.
4. \(Hg_ng_{n+1}^{-1}H\): frame-independent compressed radial defect; generally relation-valued under composition.

For three scales,

\[
(Hg_n,Hg_{n+1})\circ(Hg_{n+1},Hg_{n+2})=(Hg_n,Hg_{n+2})
\]

is deterministic, while the compressed labels satisfy only

\[
\Delta_{n,n+2}\in\Delta_{n,n+1}\star\Delta_{n+1,n+2}.
\]

There is no associativity defect: the uncertainty is exactly the erased middle coset \(Hg_{n+1}\).

## 8. Tool and ontology verdict

The strengthened verdict is

\[
\boxed{\texttt{COMPOSE_EXISTING_TOOLS}}.
\]

Use T7 finite symmetry for \(G,H\) and cosets, T8 relation observables for \(R_A\), T9 holonomy/gluing for staged versus direct transport, T0/BRC for relation composition, and T6 operation-safe quotient for deciding whether the middle coset may be erased.

No new shared primitive, physical Rubik ontology, Euclidean gauge ontology, NollM ontology, or Foundation axiom is promoted.

## 9. Closed and open scope

Closed by this redispatch:

`FIXED_STABILIZER_RADIAL_RELATION_COHERENCE`

For every group \(G\) and fixed \(H\le G\):

1. double-coset support multiplication is exact and associative;
2. it has identity and involution;
3. it is the exact relation image of the pair groupoid on \(H\backslash G\);
4. deterministic defect-only composition for all pairs exists iff \(H\) is normal;
5. finite orbital relations admit exact integer structure constants.

For the A3 \(S_4/H\) instance, the checker certifies the complete table, 343/343 boolean associativity triples, 1728/1728 pair-groupoid triples, 343/343 weighted associativity triples, and the exact 24/24 split for \(C_2,C_2\).

Remaining residue:

`SCALE_VARYING_STABILIZER_OR_PARTIAL_MOVE_GROUPOID_COHERENCE_OPEN`

A genuine successor must change at least one fixed-\(H\) hypothesis: scale-dependent \(H_n\), incoherent restriction transport, partial/object-dependent legal moves, non-conjugate target stabilizers, or an observation quotient that loses information not representable by an orbital relation. Enlarging the same finite \(S_4/H\) census is not a successor.

## 10. Replay

Deterministic checker:

`python scripts/check_a3_recursive_shell_alignment_tomography_redispatch.py`

Expected terminal lines:

- `A3_RADIAL_RELATION_COHERENCE_CHECK=PASS`
- `DOUBLE_COSET_SUPPORT_ASSOCIATIVITY=343/343`
- `PAIR_GROUPOID_TRIPLES=1728/1728`
- `WEIGHTED_ORBITAL_ASSOCIATIVITY=343/343`
- `C2*C2={C0,C2};ENDPOINT_TRIPLES=C0:24,C2:24`
- `SINGLE_VALUED_DEFECT_COMPOSITION=REFUTED_FOR_NONNORMAL_H`
- `EXACT_RELATIONAL_LIFT=PAIR_GROUPOID_ON_12_LEFT_COSETS`

Machine-readable certificate:

`research_artifacts/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_REDISPATCH/s4_h_orbital_certificate.json`
