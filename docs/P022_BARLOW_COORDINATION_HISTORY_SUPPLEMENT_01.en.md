# P022 — Coordination History Reconstructs the Global Geodesic Multiplicity Spectrum

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE SPECIALIZATION / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: `P022_BARLOW_COORDINATION_HISTORY.*`, `P022_GEODESIC_MULTIPLICITY.*`, Barlow prefix normal form  
Cross-route relevance: P010/P011 history and multiplicity; P018/P023/P024 observation sufficiency

## 1. Stronger question

The coordination-history theorem already proves

\[
(S_0,S_1,\ldots,S_n)
\Longrightarrow
T_n,
\]

where `T_n` is the total number of shortest paths from the root to the complete radius-`n` shell.

A total can hide the distribution of witnesses across endpoints.  Define the global radius-`n` geodesic multiplicity spectrum

\[
\boxed{
\mathcal M_n(m)
=
\#\{v:d(0,v)=n,\ g(0,v)=m\}.
}
\]

Equivalently, store the finite set of nonzero pairs

\[
\{(m,\mathcal M_n(m))\}.
\]

It simultaneously recovers

\[
S_n=\sum_m\mathcal M_n(m)
\]

and

\[
T_n=\sum_m m\,\mathcal M_n(m).
\]

The question is whether coordination **history**, not merely terminal coordination, already determines this stronger witness distribution.

## 2. P022-CH06 — one layer's multiplicity histogram depends only on height and absolute drift

Fix shell radius `n` and unsigned target height

\[
q=|k|\le n.
\]

The Barlow prefix normal form is

\[
P_k=(A+3)^{(q-|\delta_k|)/2}
B_{\operatorname{sgn}\delta_k}^{|\delta_k|}.
\]

Literal order inside the traversed stacking prefix has disappeared.

Changing the sign of `delta_k` exchanges `B_+` and `B_-`, which is an axial-coordinate reflection.  It changes the coordinate labels of endpoints but not the multiset of shortest-path multiplicities on that layer.

Therefore the layer histogram

\[
\boxed{
\mathcal M_{n,q,d}
\quad(d=|\delta_k|)
}
\]

is a function only of the three integers

\[
(n,q,d).
\]

No literal stacking word, signed orientation, or layer history is required once these integers are given.

This statement is stronger than the earlier layer-total formula: it preserves the entire endpoint multiplicity histogram.

## 3. P022-CH07 — coordination history reconstructs the global spectrum

The previous history theorem reconstructs for every height `q`

\[
P_q
=
\{|\delta_q|,|\delta_{-q}|\},
\]

the unordered two-sided absolute-drift pair.

At height `q>0`, the two signed layers contribute spectra

\[
\mathcal M_{n,q,|\delta_q|}
\]

and

\[
\mathcal M_{n,q,|\delta_{-q}|}.
\]

The **global** shell spectrum forgets which endpoint came from the positive or negative layer. Hence only the multiset union of these two histograms matters, and that union is symmetric under exchanging the two drift values.

The central layer `q=0` is fixed.

Consequently

\[
\boxed{
(S_0,S_1,\ldots,S_n)
\Longrightarrow
\mathcal M_n.
}
\]

Applying the same construction at every prefix radius gives

\[
\boxed{
\mathcal H_S(n)
\Longrightarrow
(\mathcal M_0,\ldots,\mathcal M_n).
}
\]

Thus the old map

\[
\mathcal H_S(n)\Longrightarrow\mathcal H_T(n)
\]

is only the first-moment shadow of a stronger history factorization.

## 4. The reverse already fails at radius two

FCC and HCP have the same shortest-path total history through radius two:

\[
(T_0,T_1,T_2)=(1,12,84).
\]

But their radius-two spectra are

\[
\boxed{
\mathcal M_2^{FCC}=\{1:12,\ 2:24,\ 4:6\},
}
\]

and

\[
\boxed{
\mathcal M_2^{HCP}=\{1:18,\ 2:18,\ 3:2,\ 4:6\}.
}
\]

Hence path-total history cannot reconstruct the global multiplicity spectrum even at this very small radius.

This refines the observation order:

\[
\boxed{
\mathcal H_S
\;\Rightarrow\;
\mathcal M
\;\Rightarrow\;
\mathcal H_T
}
\]

with the right implication strict on the FCC/HCP example.

## 5. P022-CH08 — global spectrum is still not coordinate-labelled geometry

The stronger reconstruction has a sharp boundary.

Take two one-sided length-four prefixes

\[
w=(+,-,+,+),
\qquad
w'=(+,-,-,-).
\]

Their signed imbalance trajectories are

\[
(1,0,1,2)
\]

and

\[
(1,0,-1,-2),
\]

so their **absolute** imbalance histories are identical:

\[
(1,0,1,2).
\]

Therefore any coordination history that uses one of these as one side and keeps the other side fixed is identical, and CH07 gives the same global multiplicity spectrum.

But at layer three the signed drifts are `+1` and `-1`.  The Barlow support shapes are reflected.  For example the horizontal coordinate `(2,0)` belongs to the minimal vertical support for the `+1` orientation but not for the `-1` orientation.

Thus

\[
\boxed{
\mathcal H_S
\not\Rightarrow
\text{coordinate-labelled layer distance/support field}.
}
\]

The lost information is orientation-sensitive, not witness-count-sensitive.

So history does not magically reconstruct the microscopic state. It reconstructs exactly the observables that factor through the hidden two-channel absolute-drift process.

## 6. Observation hierarchy after adding history

For this Barlow specialization we now have the strict conceptual chain

\[
\text{coordinate-labelled geometry}
\longrightarrow
\text{unsigned-height layer spectra}
\longrightarrow
\text{global multiplicity spectrum}
\longrightarrow
\text{path total}
\longrightarrow
\text{existence}.
\]

Coordination history is sufficient for the **global multiplicity spectrum**, but not for the first node.

The important project-level lesson is not that one history observable is universally superior.  It is:

> a retained observation history can become a sufficient state for a richer future language when the hidden transition law makes the missing state recursively observable.

The two-channel injectivity theorem supplies that condition here; the three-channel quadratic counterexample from the parent history note shows that the condition is not automatic.

## 7. Executable verification

Added:

- `src/enterprise_math/p022_barlow_history_multiplicity.py`;
- `tests/test_p022_barlow_history_multiplicity.py`.

The reference reconstruction was cross-checked in-session against direct Barlow endpoint enumeration for every periodic sign pattern of period at most four through radius four: 150 pattern-radius cases, with no mismatch.  This bounded reconstruction supports the ordinary proof but is not a substitute for canonical integration/CI.
