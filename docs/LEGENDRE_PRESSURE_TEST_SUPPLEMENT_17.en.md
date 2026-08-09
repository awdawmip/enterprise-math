# Legendre Pressure Test — Supplement 17

Status: `ACTIVE RESEARCH NOTE`  
Scope: multiplicity-preserving mirror CRT capacity refinement  
Depends on: canonical P017-L020, L046–L048, and L052  
Discipline: this note does **not** prove Legendre's conjecture. The CRT algebra is classical; historical novelty of this square-basin specialization is unverified.

## 1. Semantic absorption first

Canonical P017-L020 already proves the square-basin smooth-tail dichotomy. For

\[
k^2<n<(k+1)^2,
\]

write the full `k`-smooth core, with prime-power multiplicity retained, as

\[
S_k(n)=\prod_{p\le k}p^{v_p(n)},
\qquad Q_k(n)=\frac{n}{S_k(n)}.
\]

Then `Q_k(n)=1` or `Q_k(n)` is one prime `>k`, and the state is prime exactly when `S_k(n)=1`.

Therefore this supplement does **not** introduce that classification again. Its only new project-level increment is to feed the already-canonical full cores into the mirror CRT cell rather than discarding their prime-power multiplicities.

## 2. L053 — Full-core mirror CRT capacity refinement

Fix `k>=2`, put

\[
M=k(k+1),
\]

and let `1<=r<k` be an anchor-surviving radius for which both mirror states

\[
n_-=M-r,
\qquad
n_+=M+r
\]

are composite. Define their canonical L020 full smooth cores

\[
S_-=S_k(n_-),
\qquad
S_+=S_k(n_+),
\qquad
S=S_-S_+.
\]

Then:

1. `S_->1`, `S_+>1`;
2. `gcd(S_-,S_+)=1`;
3. `S` is odd and `gcd(S,M)=1`;
4. with
   \[
   w\equiv rM^{-1}\pmod S,
   \]
   one has
   \[
   w\equiv1\pmod{S_-},
   \qquad
   w\equiv-1\pmod{S_+},
   \qquad
   w^2\equiv1\pmod S;
   \]
5. with
   \[
   e\equiv\frac{1+w}{2}\pmod S,
   \]
   one has
   \[
   e^2\equiv e\pmod S,
   \qquad
   \boxed{\gcd(e-1,S)=S_-},
   \qquad
   \boxed{\gcd(e,S)=S_+};
   \]
6. the observed radius lies in the single residue class
   \[
   r\equiv M(2e-1)\pmod S.
   \]

Thus the full prime-power cores, not merely their squarefree supports, are exactly recoverable from the idempotent.

## 3. Proof

Anchor survival means no prime `p<=k` dividing `M` divides either mirror state. Hence every prime appearing in `S_-S_+` is transverse to `M`, so `gcd(S,M)=1`. Because `2|M`, the same condition makes `S` odd.

The two mirror states satisfy

\[
M-r\equiv0\pmod{S_-},
\qquad
M+r\equiv0\pmod{S_+}.
\]

Since `M` is invertible modulo both cores,

\[
rM^{-1}\equiv1\pmod{S_-},
\qquad
rM^{-1}\equiv-1\pmod{S_+}.
\]

Moreover `gcd(n_-,n_+)=1` after anchor survival on the transverse small-prime support, so the full small-prime powers on the two sides are coprime. The Chinese remainder theorem combines the two signs into one class `w mod S`, and immediately gives `w^2=1 mod S`.

Because `S` is odd, `2` is invertible modulo `S`; hence `e=(1+w)/2` is idempotent. On the lower core `e=1`, and on the upper core `e=0`. Coprimeness of the two factors therefore gives the exact gcd recovery formulas above. Multiplying `w` back by `M` yields the radius residue class modulo `S`.

## 4. Capacity refinement over the squarefree CRT cell

Let

\[
D=\operatorname{rad}(S)
\]

be the squarefree transverse-support modulus used by canonical L046–L048. Since `D|S`, every solution of the full-core radius congruence modulo `S` also solves the corresponding squarefree sign-pattern congruence modulo `D`.

Therefore, inside the bounded radius window `1<=r<k`,

\[
\boxed{
\mathcal R_{\rm full}(k;S,e)
\subseteq
\mathcal R_{\rm sf}(k;D,e_D)
}
\]

and hence

\[
\boxed{
\operatorname{cap}_{\rm full}
\le
\operatorname{cap}_{\rm sf}.
}
\]

In particular,

\[
\boxed{S\ge k\quad\Longrightarrow\quad
\operatorname{cap}_{\rm full}\le1.}
\]

The prime-power multiplicities can therefore collapse a squarefree CRT cell from several bounded radii to one without any new sieve representation.

## 5. Strict witness

Take

\[
k=31,
\qquad M=31\cdot32=992,
\qquad r=7.
\]

Then

\[
n_-=985=5\cdot197,
\qquad
n_+=999=3^3\cdot37.
\]

Thus

\[
S_-=5,
\qquad
S_+=27,
\qquad
S=135,
\qquad
D=15.
\]

The canonical squarefree sign-pattern progression has bounded radii

\[
\mathcal R_{\rm sf}=\{7,22\},
\]

whereas the full-core progression has

\[
\boxed{\mathcal R_{\rm full}=\{7\}}.
\]

So the refinement can be strict.

## 6. Supporting bounded-core corollary from L020

When the L020 residual tail is nontrivial, `Q_k(n)>k`. Since `n<(k+1)^2`,

\[
S_k(n)=\frac{n}{Q_k(n)}<\frac{(k+1)^2}{k+1}=k+1.
\]

Therefore

\[
\boxed{Q_k(n)>1\quad\Longrightarrow\quad S_k(n)\le k.}
\]

This is recorded only as a supporting corollary of canonical L020, not as a new smooth-tail classification theorem.

## 7. Structural consequence for the parity hard core

The earlier squarefree mirror CRT records only which small primes choose the `+` or `-` side. L053 records the full exponents already present in the state. The hard branch is therefore narrower than “two composite mirror states with the same squarefree support pattern”:

\[
\boxed{
\text{surviving hard core}
\subseteq
\{S_-S_+<k\}
}
\]

unless the full-core congruence has already collapsed the bounded radius cell to at most one candidate.

This does not by itself remove the remaining singleton-small-core plus large-prime-tail obstruction, but it gives that obstruction a strictly smaller multiplicity-sensitive state space.

## 8. Executable validation

`observed_mirror_full_core_idempotent(k,r)` implements L053 using canonical `square_basin_smooth_tail` from L020. Regression tests verify:

- exact recovery of full prime-power cores;
- divisibility `D|S`;
- inclusion of full-core lifts in squarefree sign-pattern lifts;
- `cap_full<=cap_sf`;
- uniqueness whenever `S>=k`;
- the strict `k=31,r=7` witness.

Finite tests audit the implementation only. The theorem is the CRT argument above.

## 9. Next target

Combine L052 root-channel disjointness, L053 multiplicity-preserving CRT capacity, T113 exact quotient-branch thresholds, and the exact first-factor cofactor windows. The remaining pressure should be isolated in the region

\[
S_-S_+<k
\]

with one or both mirror states carrying a large prime tail. That is the right place to test whether the lower-band recursion yields a genuinely smaller capacity than ordinary Buchstab bookkeeping.
