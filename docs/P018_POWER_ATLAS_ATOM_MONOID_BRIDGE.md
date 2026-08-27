# P018 — Powered atlas / atom-monoid bridge and operation-neutral precision

Status: `ORDINARY MATHEMATICS PROVED / PRIOR-ART BOUNDARY RECORDED / LEAN NOT YET VERIFIED`

Scope: P018 quotient-root atlas specialization; generic numerical-set / atom-monoid theory is prior art and belongs outside P018 owner space if promoted generically.

## 1. Boundary model

For a finite nonempty boundary set `B subset N_{>0}` with `M=max B`, define the monotone eventually-zero profile

\[
q_B(x)=\#\{b\in B:b\ge x\}.
\]

Its strict-drop set is exactly `B`.

A nonnegative translation `a` is safe for `q_B` exactly when

\[
\forall b\in B,\qquad b>a\Longrightarrow b-a\in B.
\]

Equivalently, in the binary boundary word, every residue-class column modulo `a` is downward closed.

## 2. Exact numerical-set reflection

Define the reflected cofinite numerical set

\[
T_B:=\{M-b:b\in B\}\cup [M,\infty)\subseteq\mathbb N_0.
\]

Then the safe-translation set of the collapse is exactly

\[
\boxed{\mathcal S(B)=A(T_B):=\{a\in\mathbb N_0:a+T_B\subseteq T_B\}.}
\]

Proof: if `x=M-b<M`, then `x+a<M` is in `T_B` exactly when `b-a` is a boundary. Elements already at least `M` remain in the terminal tail under every nonnegative translation.

Thus the safe-translation numerical semigroup derived independently in Enterprise Math is precisely the classical **atom monoid / associated semigroup** of the reflected numerical set.

### Prior art

This generic atom-monoid structure is established numerical-set theory, not an Enterprise Math novelty. Antokoletz–Miller define atom monoids; Marzuola–Miller study the anti-atom problem; Chen–Kaplan–Lawson–O'Neill–Singhal classify numerical sets with a given atom monoid using the void poset and Frobenius-triangle constraints.

Enterprise Math should retain only the exact translation from collapse boundaries to that theory and the consequences for precision/future-language semantics.

## 3. Anti-atom fiber = same-language precision fiber

Fix a numerical semigroup `S` and choose any gauge `M >= c(S)`.

For every numerical set `T` with `A(T)=S`, define

\[
B_M(T):=\{M-t:0\le t<M,\ t\in T\}.
\]

Then

\[
\boxed{\mathcal S(B_M(T))=S.}
\]

Conversely, every boundary with maximum `M` and safe semigroup `S` arises uniquely this way.

Therefore the anti-atom fiber

\[
\{T:A(T)=S\}
\]

is exactly the family of precision boundaries with the same maximal safe translation language.

Inclusion of numerical sets is inclusion of boundary cuts, hence ordinary precision refinement.

## 4. Minimal operational core and maximal neutral envelope

For any boundary `B`, put `S=A(T_B)` and

\[
K(B):=B_M(S)=\{M-a:a\in S,\ 0\le a<M\}.
\]

Then

\[
K(B)\subseteq B,\qquad \mathcal S(K(B))=\mathcal S(B).
\]

Moreover `K(B)` is the unique smallest boundary subset with the same maximum `M` and the same safe translation language.

Under numerical-set reflection this is simply the prior-art inclusion

\[
A(T_B)\subseteq T_B.
\]

Applying the core twice changes nothing.

If `S^*` denotes the classical dual/maximal associated numerical set, prior art gives

\[
S\subseteq T\subseteq S^*
\]

for every `T` associated to `S`, with `A(S)=A(S^*)=S`. Hence, at fixed `M`,

\[
\boxed{B_M(S)\subseteq B_M(T)\subseteq B_M(S^*)}.
\]

This is the exact minimum-to-maximum interval of operation-neutral precision available to the translation language `S`; not every intermediate subset is language-tight, and the void-poset/Frobenius-triangle conditions classify the admissible ones.

## 5. Actual versus latent neutral precision

Define

\[
\rho_-(B):=|B\setminus K(B)|=|T_B\setminus S|.
\]

This counts current boundary distinctions that can be deleted without changing the safe translation language.

Define the latent neutral capacity

\[
\rho_+(B):=|S^*\setminus T_B|.
\]

Then

\[
\boxed{\rho_-(B)+\rho_+(B)=|S^*\setminus S|.}
\]

Classical numerical-set theory identifies

\[
|S^*\setminus S|=2g(S)-F(S)-1,
\]

the size of the void. Thus the void size is an exact total budget of operation-neutral precision states, split between already-present removable detail and still-addable neutral detail.

Symmetric numerical semigroups have empty void and a unique associated numerical set. In Enterprise language: they are **translation-precision rigid** — the safe translation language determines the precision realization uniquely (up to the harmless gauge `M`).

## 6. P023 refinement-width bridge

Let `Pi_B` be the plateau partition of `q_B` on a finite window containing all boundaries.

For an associated numerical set `S subseteq T subseteq S^*`, boundary inclusion gives

\[
\Pi_{B_M(T)}\le \Pi_{B_M(S)}.
\]

The canonical P023 local refinement width therefore measures the minimum reusable local detail alphabet required to retain the extra operation-neutral precision of `T` on top of the operational core `S`.

If the small elements of `S` are

\[
0=s_0<s_1<\cdots<s_k<c(S)=s_{k+1},
\]

then

\[
\boxed{
w_{\Pi_{B_M(S)}}(\Pi_{B_M(T)})
=1+\max_{0\le i\le k}\#\bigl((T\setminus S)\cap(s_i,s_{i+1})\bigr).
}
\]

The gauge `M>=c(S)` only adds common singleton-prefix cuts and does not change this nontrivial width.

The maximal same-language local-detail envelope is obtained at `T=S^*`.

For an intermediate associated set `T`, P023 refinement-width submultiplicativity gives the exact compositional bound along

\[
S\subseteq T\subseteq S^*.
\]

Thus generic anti-atom theory supplies the admissible refinement family, while P023 supplies the persistent-detail cost coordinate inside that family.

## 7. Promise-safe versus language-tight refinement

Two conditions must be separated.

1. `S subseteq A(T)`: every promised translation in `S` remains valid after refinement. This is P023-style law support.
2. `A(T)=S`: refinement is language-tight; it preserves the promised language without accidentally creating additional safe translations.

In the numerical-set literature, void-poset order ideals characterize the first support condition inside the relevant interval, while additional Frobenius-triangle constraints characterize exact atom-monoid equality.

Enterprise interpretation:

- order-ideal constraints prevent **law loss** under added precision;
- equality constraints prevent **language leakage** (accidental new safe operations).

This is a one-dimensional exact model of the already-known P023 fact that operation autonomy is not monotone under arbitrary raw refinement.

## 8. Compact nonmonotonic witness

At maximum boundary `M=4`, take

\[
B_0=\{2,4\}\subset B_1=\{2,3,4\}\subset B_2=\{1,2,3,4\}.
\]

Translation by `2` is

\[
\text{safe at }B_0,\qquad
\text{unsafe at }B_1,\qquad
\text{safe again at }B_2.
\]

So even in this one-dimensional monotone-collapse specialization, more raw precision can produce `valid -> invalid -> valid` operation autonomy.

This witness is an illustration, not a novelty claim about generic nonmonotonicity.

## 9. P018 powered-floor specialization

For the quotient-root atlas

\[
\mathcal A_{r,n}
=\left\{R_r\!\left(\left\lfloor\frac nd\right\rfloor\right):1\le d\le n\right\},
\]

let

\[
M_{r,n}=R_r(n),\qquad B_{r,n}=\mathcal A_{r,n}.
\]

The safe-translation semigroup of the powered-floor profile is therefore

\[
S_{r,n}=A(T_{B_{r,n}}).
\]

Its conductor remains the previously proved boundary formula

\[
c(S_{r,n})=M_{r,n}-P_{r,n},
\]

where `[1,P_{r,n}]` is the maximal consecutive prefix contained in the atlas.

The generic atom-monoid fact is prior art; the powered-floor specialization and its arithmetic consequences remain P018-owned.

## 10. Sharp `r=1` versus `r>1` operational-minimality split

### Theorem A — classical floor quotient is always operationally minimal

For `r=1`,

\[
B_{1,n}=\{\lfloor n/d\rfloor:1\le d\le n\},\qquad M=n.
\]

The reflected numerical set `T_{B_{1,n}}` is closed under addition.

Proof: every boundary other than `n` is at most `n/2`. Hence if `b_1,b_2 in B` and `b_1+b_2>n`, at least one of the two boundaries is `n`; the centered overflow `b_1+b_2-n` is then the other boundary. This is exactly addition closure after reflection.

Therefore

\[
\boxed{T_{B_{1,n}}=S_{1,n},\qquad \rho_-(B_{1,n})=0\quad\forall n.}
\]

The ordinary floor-quotient atlas contains no translation-neutral boundary state that can be deleted.

### Theorem B — every higher root order is eventually operationally redundant

Fix `r>=2`. Put

\[
M_n=R_r(n),\qquad
b_n=R_r(\lfloor n/2\rfloor),\qquad
z_n=2b_n-M_n.
\]

Then there exists `N_r` such that for all `n>=N_r`:

1. `z_n>0`;
2. `z_n notin B_{r,n}`;
3. the second-largest atlas state `b_n` is not in the operational core `K(B_{r,n})`.

Hence

\[
\boxed{\rho_-(B_{r,n})\ge1\quad\text{for all sufficiently large }n.}
\]

#### Proof

As `n -> infinity`,

\[
\frac{M_n}{n^{1/r}}\to1,\qquad
\frac{b_n}{n^{1/r}}\to2^{-1/r},
\]

so

\[
\frac{z_n}{n^{1/r}}
\to c_r:=2\,2^{-1/r}-1>0.
\]

Assume `z_n` belonged to the atlas for infinitely many `n`. Choose denominators `d_n` with

\[
z_n=R_r(\lfloor n/d_n\rfloor).
\]

Since `z_n^r <= n/d_n` and `z_n/n^{1/r}` stays bounded away from zero, the integers `d_n` are bounded. Along a subsequence `d_n=d` is fixed, forcing

\[
c_r=d^{-1/r}.
\]

Thus `c_r^r=1/d` would be rational.

Let `x=2^{1/r}`. By Eisenstein, `X^r-2` is irreducible over `Q`, so `1,x,...,x^{r-1}` are linearly independent over `Q`. But

\[
c_r^r=\frac{(2-x)^r}{2}
\]

has a nonzero `x^{r-1}` coefficient after reduction by `x^r=2`; hence it is irrational. Contradiction.

Therefore `z_n notin B_{r,n}` eventually.

Now `x_n=M_n-b_n` belongs to `T_{B_{r,n}}`, while for large `n`, `2x_n<M_n` and

\[
M_n-2x_n=z_n\notin B_{r,n},
\]

so `2x_n notin T_{B_{r,n}}`. Hence `x_n` is not an atom, which exactly means the reflected boundary state `b_n` is absent from `K(B_{r,n})`.

### Interpretation

There is a genuine order-of-root phase split:

\[
\boxed{
r=1:\ \text{powered atlas is always operation-minimal};\qquad
r>1:\ \text{powered atlas is eventually operation-redundant}.
}
\]

This higher-order theorem is a new Enterprise Math candidate. The quick literature search performed at this checkpoint found the generic atom-monoid/anti-atom theory but did not find this powered-floor asymptotic statement. Keep novelty status `UNRESOLVED` until a dedicated search is completed.

## 11. Concrete witness

For `r=2,n=980`,

\[
B=\{1,2,3,4,5,6,7,8,9,10,11,12,14,15,18,22,31\}.
\]

Its safe semigroup is

\[
S=\{0,13,16,17\}\cup[19,\infty).
\]

The operational core is

\[
K=B\setminus\{22\}.
\]

The obstruction is already visible from

\[
22,22\in B,\qquad 22+22-31=13\notin B.
\]

Equivalently the reflected numerical-set element `31-22=9` is present but `9+9=18` is absent, so `9` is not an atom.

Thus one quotient-root state is genuine raw precision but invisible to the entire safe-translation language.

## 12. Owner routing

Generic material to route to P023/A2 if promoted:

- boundary reflection `B <-> T_B`;
- atom-monoid identification;
- anti-atom fiber as same-language refinement family;
- operational core / maximal neutral envelope;
- void-poset interpretation of law-preserving refinements;
- P023 refinement-width coordinate on associated numerical sets.

P018 retains:

- powered-floor / quotient-root specialization;
- exact conductor/horizon/carry consequences;
- `r=1` operational minimality;
- `r>=2` eventual second-state redundancy;
- arithmetic study of the resulting numerical semigroups `S_{r,n}`.

Do not implement a second generic operation-quotient engine in P018.

## 13. Formalization status

No theorem in this note is Lean-verified at this checkpoint.

The existing P018 Lean drop-duality unit remains `NOT YET LEAN-VERIFIED`. Generic atom-monoid formalization should not be allowed to block the owner-correct bridge; first formalize the already-local powered-floor statements or consume a future shared finite-set abstraction if one is promoted.
