# P023 — Label Erasure and Image Separation, Supplement 08

Status: `PROVED`  
Owner: A2 / P023 future-compatible quotient  
Pressure source: P017 L054/L052 and P024 future-safe precision  
Discipline: set images, injectivity, and decoder existence are elementary mature mathematics; the purpose here is to extract a reusable quotient/repair test.

## 1. When can an auxiliary label actually be erased?

Number-theoretic proofs often write a state as

\[
(i,x),
\]

where `i` is a shell/factor/residue-class label and `x` is the coordinate that continues into later computation.

Two unsafe defaults are common:

- once `i` has been introduced, carry it forever; or
- if the present `x` values do not collide, erase `i` forever.

P023 future-safety asks the sharper question:

> after erasing the label now, can the label still be uniquely recovered from the retained coordinate after every declared future map?

The answer is exactly an **actual-image separation** test.

## 2. Setup

Let `I` be a label set, `X` a fine state space, and let

\[
W_i\subseteq X
\qquad(i\in I)
\]

be labeled shells.

The tagged state space is the disjoint union

\[
S=\{(i,x):x\in W_i\}.
\]

The current label-erasure map is

\[
E:S\to X,
\qquad
E(i,x)=x.
\]

Let

\[
G:X\to Y
\]

be a later deterministic map.

## 3. P023-S8-T01 — Current label-erasure criterion

Status: `PROVED`.

The following are equivalent:

1. `E(i,x)=x` is injective on `S`;
2. for all `i!=j`,
   \[
   \boxed{W_i\cap W_j=\varnothing.}
   \]

### Proof

If two distinct shells share some `x`, then `(i,x)!=(j,x)` but both are sent to the same state by `E`, so `E` is not injective.

Conversely, if the shells are pairwise disjoint and `E(i,x)=E(j,y)`, then `x=y`; that state belongs to only one shell, so `i=j`, and hence `(i,x)=(j,y)`. ∎

### Meaning

If the exact retained coordinate already encodes shell identity, carrying the shell label is a duplicate state dimension.

## 4. P023-S8-T02 — Label recovery after a future map

Status: `PROVED`.

The following are equivalent:

1. there is a decoder, required only on the reachable image,
   \[
   D:G\!\left(\bigcup_iW_i\right)\to I
   \]
   such that
   \[
   D(G(x))=i
   \qquad(x\in W_i);
   \]
2. distinct shell images are pairwise disjoint:
   \[
   \boxed{
   G(W_i)\cap G(W_j)=\varnothing
   \qquad(i\ne j).
   }
   \]

### Proof

If `y=G(x_i)=G(x_j)` is realized by two distinct labels, the decoder would have to satisfy both `D(y)=i` and `D(y)=j`, impossible.

Conversely, when the images are pairwise disjoint, each reachable `y` comes from exactly one shell. Define `D(y)` to be that unique label. ∎

Thus safe future label erasure is not a heuristic: it is an **image-separation test**.

## 5. P023-S8-T03 — Label recovery and full-state recovery are different

Status: `PROVED`.

Define

\[
H:S\to Y,
\qquad
H(i,x)=G(x).
\]

Then `H` is injective on `S` if and only if both hold:

1. distinct shell images are pairwise disjoint;
2. every restriction
   \[
   G|_{W_i}:W_i\to Y
   \]
   is injective.

### Proof

This is the exact split of injectivity into cross-shell and within-shell directions.

- a cross-shell image collision merges states with different labels;
- noninjectivity within a shell merges different fine states with the same label;
- if neither collision occurs, `H` is injective. ∎

Therefore

\[
\boxed{
\text{shell label recoverable}
\not\Rightarrow
\text{full original state recoverable}.
}
\]

This distinction matters for root, bucket, and basin coordinates.

## 6. P023-S8-T04 — Safe label erasure under a declared context family

Status: `PROVED`, by applying T02 context by context.

Let

\[
\mathcal G=\{G_c:X\to Y_c\}_{c\in C}
\]

be the declared future contexts. If the task requires shell identity to remain recoverable after every context, then the label can be erased now if and only if for every `c` and every `i!=j`,

\[
\boxed{
G_c(W_i)\cap G_c(W_j)=\varnothing.
}
\]

The first context producing an overlap gives an exact witness that repair information is needed.

This is the shell-label specialization of the P023 operation-word future quotient.

## 7. A2 reinterpretation of P017 L054

In the P017 open square basin, let the label be the least prime `p` and retain the stripped cofactor

\[
q=n/p.
\]

The shells are exactly

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

L054 proves that all raw windows are pairwise disjoint for `k>=4`.

By T01,

\[
\boxed{
\text{for }k\ge4,\text{ the least-prime label }p
\text{ is already a function of the exact cofactor }q.
}
\]

Within one `p` shell, `n=pq`, so `q` recovers not only the label but the full composite state.

L054 can therefore be read as saying that the factor label is a redundant dimension in the exact stripped coordinate.

## 8. Root projection shows that “erasable now” does not mean “erasable forever”

If the next retained coordinate is only

\[
G(q)=R_2(q),
\]

then T02 requires actual separation of

\[
R_2(W_p(k)),
\]

not merely separation of the original windows.

This explains three related but different P017 layers:

- L054: exact quotient shells are disjoint from `k>=4`;
- L052: after enlarging each actual image to the candidate pair `{j_p,j_p+1}`, those coarse candidate pairs are uniformly disjoint only from `k>=15`;
- new L055: if the exact window is retained before taking its actual root image, lower-band shell identity is already recoverable from `k>=9`.

The improvement `15 -> 9` is a precision lesson rather than merely a tighter estimate:

> **enlarging candidate sets can manufacture collisions that no realized state ever attains.**

## 9. What repair means

If `G(W_i)` and `G(W_j)` overlap, it does not follow that the full original label must be retained. Only enough information to split the realized overlaps is required.

General minimal repair remains owned by P023 future-compatible quotient theory. This supplement provides a fast zero-repair criterion:

\[
\boxed{
\text{all relevant shell images pairwise disjoint}
\Longrightarrow
\text{shell-label repair cost}=0.
}
\]

## 10. Research-tool form

For factor shells, residue shells, geometric sectors, collision modes, and similar explicit labels, use the same pipeline:

1. write the actual fine-state sets `W_i`;
2. test whether the retained present coordinate already separates them;
3. for each declared future map `G_c`, compute the actual images `G_c(W_i)`;
4. erase the label while those images remain disjoint;
5. when images first overlap, compile repair only on the overlap region;
6. do not replace actual images by enlarged candidate supersets unless the resulting false-collision cost is explicitly accepted.

## 11. Executable audit

- `src/enterprise_math/label_erasure.py`
- `tests/test_p023_label_erasure.py`
- P017 specialization: `src/enterprise_math/p017_actual_root_separation.py`

The tests pin present shell disjointness, transformed label decoders, the strict difference between label recovery and full-state injectivity, and the sharp P017 actual-root threshold.

## 12. Prior-art and novelty discipline

“Pairwise disjoint images iff a label decoder exists” is elementary set theory, not a new theorem.

The Enterprise Math contribution is to use it systematically as a **zero-repair compiler** for future-safe precision and to require actual-image separation audits before auxiliary labels are carried through number-theory or engineering proofs.
