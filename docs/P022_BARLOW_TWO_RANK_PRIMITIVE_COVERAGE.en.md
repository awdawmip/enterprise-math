# P022 — Two-Rank Primitive Coverage for Franel-Defect Independence

Status: `PROVED WIP / STRICTLY WEAKER SUFFICIENT CRITERION`  
Owner: `program/p022-geometry-v2`  
Depends on: primitive-defect pivot; primitive successor-capture theorem  
Prior-art boundary: triangular valuation certificates and primitive-divisor arguments are classical; P022 owns the exact two-rank Franel-defect specialization.

## 1. Old sufficient condition was too strong

The first primitive-divisor strategy asked for one primitive Franel prime directly at every composite-boundary rank `n`:

\[
2n-1\text{ composite}
\quad\Longrightarrow\quad
\exists p_n:\ p_n\text{ primitive at }F_n.
\]

Then

\[
v_{p_n}(D_n)>0
\]

and all earlier defect entries on that row vanish, giving a triangular valuation certificate.

The successor-capture theorem proves that the primitive event need not occur at rank `n` itself.

## 2. P022-LI48 — two-rank candidate window for a composite defect column

Fix a composite-boundary defect

\[
D_n,
\qquad 2n-1\text{ composite}.
\]

There are at most two automatic primitive source ranks:

### Current rank

A primitive Franel prime at rank `n` gives

\[
\boxed{v_p(D_n)=+v_p(F_n).}
\]

### Previous rank

If

\[
2n-3\text{ is prime},
\]

then rank `n-1` is a prime-boundary rank. Any primitive Franel prime there has no defect column at `n-1`, but the successor theorem gives

\[
\boxed{v_p(D_n)=-v_p(F_{n-1}).}
\]

Thus the automatic source window is

\[
\boxed{
\{n\}
\cup
\bigl(\{n-1\}\text{ if }2n-3\text{ is prime}\bigr).
}
\]

The sign is irrelevant for rank: both positive and negative nonzero valuations are valid pivots.

## 3. P022-LI49 — two-rank triangular certificate

For every composite-boundary index `n<=N`, choose exactly one primitive prime marker from an allowed source rank in the window above.

Because a prime has only one first Franel rank, markers attached to distinct source ranks are distinct. For each chosen row:

- all earlier Franel terms are p-units by primitiveness;
- all earlier defect columns therefore have valuation zero;
- the selected defect column has the nonzero signed pivot described above.

Hence the valuation matrix is triangular.

Therefore:

\[
\boxed{
\text{two-rank primitive coverage of every composite }D_n
\Longrightarrow
\{2,D_n\}\text{ are multiplicatively independent on that finite prefix}.
}
\]

If every chosen primitive depth is one, every diagonal entry is `+1` or `-1`, so the certificate is unimodular:

\[
\boxed{|\det V|=1.}
\]

## 4. Why this strictly weakens the research hypothesis

The theorem no longer asks every composite `F_n` to generate its own new primitive row. A primitive event from the immediately preceding **prime-boundary** rank can be consumed one step later.

This is not merely a sign convention. A negative successor pivot is as strong as a positive current pivot for exact integer independence.

A concrete prefix through segment 14 can be certified by the markers

\[
\begin{array}{c|c|c|c}
D_n & \text{source rank} & \text{primitive prime} & \text{pivot}\\\hline
D_5 & 4 & 173 & -1\\
D_8 & 7 & 41 & -1\\
D_{11} & 10 & 61 & -1\\
D_{13} & 12 & 176459 & -1\\
D_{14} & 14 & 12148537 & +1
\end{array}
\]

Together with the tail pivot this gives diagonal

\[
\boxed{(1,-1,-1,-1,-1,1),}
\]

hence an exact unimodular finite certificate.

This example deliberately uses predecessor markers even where a current-rank primitive may also exist; its purpose is to demonstrate the weaker theorem interface.

## 5. Relation to twin-prime deferral

The previous rank can serve `D_n` precisely when

\[
2n-3\text{ is prime}
\]

and `2n-1` is composite. If both neighbors of a primitive rank are prime, that primitive event lies at a twin-prime center and this one-step coverage mechanism is deferred.

Thus the global primitive-divisor problem is no longer aligned one-to-one with composite columns. The correct combinatorial object is a **capture map from primitive ranks to composite defect columns**.

## 6. New global frontier

The old question

> does every composite-boundary `F_n` have a primitive divisor?

can now be replaced by the strictly weaker question

> does every composite defect column receive at least one primitive event from its two-rank capture window, or—when it does not—can older/global valuation rows still complete the defect lattice?

The latter keeps the proven 150-column global valuation machinery in play and avoids discarding useful negative or returning valuation rows.

No infinite two-rank primitive-coverage theorem is claimed yet.

## 7. Executable assets

- `src/enterprise_math/p022_barlow_two_rank_primitive_coverage.py`
- `tests/test_p022_barlow_two_rank_primitive_coverage.py`
