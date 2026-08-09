# Causal Absorption 05 — P011 Collision Spectrum as a Universal Basis for Symmetric Fiber-Local Integer Responses

Status: `CROSS-ROUTE RESEARCH WIP / EXACT BINOMIAL BASIS THEOREM + EXECUTABLE REFERENCE`

Suggested owner: A1/P011. This A3-branch document is only a cross-route derivation source.

For a response `phi(n)` depending only on the number `n` of indistinguishable fine histories in one collapse fiber, define the exact interaction coefficients

\[
\boxed{
a_k=\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}\phi(j).}
\]

Finite binomial inversion gives

\[
\boxed{\phi(n)=\sum_{k=0}^n a_k\binom nk.}
\]

For a finite collapse `F` with fiber sizes `m_F(y)` and `phi(0)=0`, the global symmetric fiber-local response is therefore

\[
\boxed{
R_\phi(F)=\sum_y\phi(m_F(y))
=\sum_{k=1}^N a_kJ_k(F),
}
\]

where

\[
J_k(F)=\sum_y\binom{m_F(y)}k
\]

is the P011 collision spectrum.

Thus `J_k` is an exact universal basis for every bounded symmetric integer response that depends only on fiber size. Traditional power moments become particular coordinate readings, for example

\[
n^2=n+2\binom n2,
\qquad
n^3=n+6\binom n2+6\binom n3.
\]

The merge defect also decomposes exactly:

\[
\boxed{
\Delta R_\phi=\sum_k a_k\Delta J_k.
}
\]

Every `Delta J_k` counts newly created cross-old-fiber `k`-subsets. Therefore nonnegative interaction coefficients `a_k` for `k>=2` give a direct causal sufficient condition for monotone merge response; `a_2>0` forces strict growth under every genuine merge of nonempty fibers.

Conventional uniform `k`-history collision probability is only the later count-ratio rendering

\[
\left(J_k(F),\binom Nk\right).
\]

P011 already proves that the full collision spectrum determines the entire multiset of fiber sizes. Consequently any symmetric scalar that uses only those fiber sizes, including power moments and many normalized/log entropy-style renderings, contains no additional fiber-size information beyond the exact integer spectrum. This does not derive thermodynamic entropy.

Executable sources:

- `src/enterprise_math/collision_interaction_basis.py`
- `tests/test_collision_interaction_basis.py`
