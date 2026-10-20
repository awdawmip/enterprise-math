# R042 Stage 3 — Exact Shell-Return Lorentz Chords and Growing Norm Divisibility

Status: `L2 CONTINUATION SEMANTIC CHECKPOINT / PROVED + EXECUTABLE_CHECKED / NOT CANONICAL`

Researcher-ID: `EM-R042-963283`

Official task: `RS-R042-POLYGONAL-NONSQUARE-BRANCH-LIMIT-PELL-RECURRENCE`

Accepted Stage-2 owner head: `b3ca1369c147e50d1a841d3f86c081f2cb152f68`

Consumed concurrent owner continuation head: `e65eaad4ce240213745797dc75ecb8f1be5b5999`
(`reverse shadow + ordered local-gate residual + superlacunary necessity`).

Primary return:

`HIT_ANCESTRY_ONTOLOGY_REPLACED / SMALLER_EXACT_RECURRENCE_OBJECT_FOUND / NOT_CANONICAL`

Refined classification:

`LOCAL_GATE_INPUT_STATE_COMPRESSED_TO_SHELL_CHORD / TWO_SOURCE_LORENTZ_CERTIFICATE_FOUND / GROWING_NORM_DIVISIBILITY_PROVED / INFINITE_RECURRENCE_OPEN / NOT_CANONICAL`

## 0. Frozen contract

This is the next continuation of the same R042 task. It consumes without reopening all Stage-1 and Stage-2 results, including:

- nonsquare full dimension;
- the zero-dimensional / zero-conditioned-mass infinite-hit exceptional subset;
- the discriminant/Pell-strip classification;
- the exact hit-ancestry reduction;
- finite correction alphabet and the cocycle `xi_{t+1}=sqrt(r) xi_t+q_t`;
- finite reduced Pell seeds;
- finiteness on every fixed Pell-unit diagonal;
- the Stage-2 acceleration `n>(3/2)m-C_*`.

Before publication this session observed and consumed the newer same-owner head `e65eaad4...`, which further proves a reverse-shadow shrinking target, isolates the ordered local-gate residual word, and proves that any hypothetical infinite ray is superlacunary via a Baker/Matveev lower bound. Those results are preserved; the present checkpoint does not replace them with the weaker elementary rank estimate derived below.

The only question here is whether an infinite dynamically legal correction-address/local-gate-survival ray can return to `N(xi)=-B` infinitely often.

No bounded no-witness computation is promoted to a theorem. No finite-height theorem and no infinite recurrent branch are claimed below.

## 1. Aggregate one complete return block

Keep

\[
\alpha=\sqrt r,\qquad B=(r-1)(s-4)^2,
\]

and suppose a dynamically legal branch hits the shell at `xi`, leaves it, and returns after exactly `d>=1` endpoint steps at `xi'`.

Stage 2 gives

\[
\xi'=\alpha^d\xi+P,
\]

where the whole correction word is aggregated into one algebraic integer

\[
\boxed{P=p+\alpha q\in\mathbf Z[\alpha].}
\]

If the block digits are `q_0,...,q_{d-1}`, then

\[
P=\sum_{j=0}^{d-1}\alpha^{d-1-j}q_j.
\]

The recurrence problem therefore has an arithmetic layer that depends only on `(d,P)` before one asks whether the underlying correction word is dynamically legal.

The shell endpoints satisfy

\[
N(\xi)=N(\xi')=-B.
\]

Write

\[
\xi=Y+\alpha Z,
\qquad
P=p+\alpha q.
\]

Define the Lorentz bilinear coordinates

\[
\boxed{S:=pY-rqZ,\qquad T:=pZ-qY.}
\]

They obey the exact identity

\[
\boxed{S^2-rT^2=-B\,N(P).}
\]

This is simply multiplicativity of the quadratic norm written in bilinear coordinates.

Claim status: `PROVED`.

## 2. Shell equality linearizes by parity

Expanding the target norm gives

\[
N(\alpha^d\xi+P)
=N(\alpha^d)N(\xi)+N(P)
+\operatorname{Tr}(\alpha^d\xi\overline P).
\]

Because both endpoint norms are `-B`, define

\[
\boxed{
C_d(P):=B\bigl((-r)^d-1\bigr)-N(P).
}
\]

Then

\[
\operatorname{Tr}(\alpha^d\xi\overline P)=C_d(P).
\]

### Even gap

For `d=2L`, `alpha^d=r^L`, so

\[
\boxed{2r^L S=C_d(P).}
\]

Thus `S` is forced by `(d,P)`. The Lorentz identity then forces

\[
\boxed{T^2=\frac{S^2+B N(P)}r.}
\]

### Odd gap

For `d=2L+1`, `alpha^d=r^L alpha`, so

\[
\boxed{2r^{L+1}T=C_d(P).}
\]

Thus `T` is forced by `(d,P)`, and

\[
\boxed{S^2=rT^2-BN(P).}
\]

Claim status: `PROVED`.

This already produces exact divisibility and perfect-square obstructions before any endpoint predecessor is evaluated.

## 3. A return block reconstructs at most two shell sources

The Lorentz coordinates are related to the source pair by

\[
\begin{pmatrix}S\\T\end{pmatrix}
=
\begin{pmatrix}p&-rq\\-q&p\end{pmatrix}
\begin{pmatrix}Y\\Z\end{pmatrix}.
\]

Since `r` is nonsquare, a nonzero `P=p+alpha q` has `N(P)!=0`. Inverting gives

\[
\boxed{
Y=\frac{pS+rqT}{N(P)},
\qquad
Z=\frac{qS+pT}{N(P)}.
}
\]

For fixed `(d,P)`, parity fixes one of `S,T`, and the Lorentz equation allows at most two signs for the other. Therefore:

> **Two-source shell theorem.** For every fixed nonsquare cell and every nonzero aggregate return block `(d,P)`, there are at most two integral source pairs `(Y,Z)` on `N=-B` whose scaled translate `alpha^d xi+P` also lies on `N=-B`.

After positivity and the affine-lattice residue are imposed, the surviving source is frequently unique.

Claim status: `PROVED`.

This removes the Pell-unit rank from the primitive shell-return state. Unit rank remains useful metadata for growth estimates, but it is not needed to reconstruct the arithmetic shell endpoints once `(d,P)` is known.

### Correction-word elimination by unique reverse ancestry

For each reconstructed source candidate, `(d,P)` also determines the target pair `xi'=alpha^d xi+P`. Convert the source and target discriminant coordinates back to endpoint indices.

In the frozen `r>=5` separated regime, every positive endpoint has at most one parent. Therefore dynamic accessibility of this shell chord is no longer a search over correction words: start from the target child and iterate the exact predecessor oracle `d+1` times. The chord is dynamically legal if and only if this unique reverse chain lands on the reconstructed source pair with the correct endpoint length.

If the check succeeds, every intermediate endpoint and hence every correction digit is recovered uniquely from the path. If it fails, no alternative correction word can rescue that candidate, because there is no second parent chain.

Thus:

\[
\boxed{
(d,P)+\text{shell-sign candidate}+\text{unique predecessor oracle}
\quad\text{is a complete exact edge certificate.}
}
\]

Claim status: `PROVED`, consuming the frozen no-distinct-parent-recoalescence theorem.

This removes the growing correction word/address itself from the minimum recurrence state. The correction alphabet remains useful for deriving bounds and for generating candidates, but it is not theorem-critical state for certifying a proposed return edge.

## 4. Growing norm divisibility

The parity formulas imply that `C_d(P)` is divisible by

\[
2r^{\lceil d/2\rceil}.
\]

Modulo `r^{ceil(d/2)}`, the term `B(-r)^d` vanishes. Hence

\[
C_d(P)\equiv-(N(P)+B)
\pmod{r^{\lceil d/2\rceil}}.
\]

Therefore every shell-to-shell correction block satisfies the exact necessary condition

\[
\boxed{
r^{\lceil d/2\rceil}\mid N(P)+B.
}
\]

Claim status: `PROVED`.

This is a genuinely growing-modulus obstruction. It is not a fixed-residue automaton.

For the frozen finite revisit witnesses, the exact quotients are:

- `(s,r)=(3,6)`, `d=1`, `P=-1`: `(N(P)+B)/6 = 1`;
- `(6,11)`, `d=3`, `P=24+12 sqrt(11)`: quotient by `11^2` is `-8`;
- `(6,15)`, `d=2`, `P=-28-12 sqrt(15)`: quotient by `15` is `-88`;
- `(7,7)`, `d=11`, `P=-41996+9678 sqrt(7)`: quotient by `7^6` is `9418`;
- `(8,14)`, `d=3`, `P=-108-20 sqrt(14)`: quotient by `14^2` is `32`.

These examples are only executable certificates of the theorem, not the proof.

## 5. The exceptional case `N(P)=-B` has only finitely many possible gap lengths

The divisibility theorem is strongest when `N(P)+B` is nonzero. We therefore isolate the only exceptional possibility:

\[
N(P)=-B.
\]

Assume source `xi`, correction `P`, and target `alpha^d xi+P` all have norm `-B`. Since `P` is nonzero, put

\[
\rho:=\frac{\xi}{P},
\qquad N(\rho)=1,
\qquad t:=\alpha^d\rho.
\]

Dividing the shell equality by `N(P)` yields

\[
\operatorname{Tr}(t)=-N(\alpha^d),
\qquad
N(t)=N(\alpha^d).
\]

Thus `t` is a root of

\[
X^2+N(\alpha^d)X+N(\alpha^d)=0.
\]

Its discriminant

\[
\boxed{
\Delta_d=N(\alpha^d)\bigl(N(\alpha^d)-4\bigr)
}
\]

must have a square root in `K=Q(sqrt(r))`.

Let `D` be the squarefree part of `r`. A positive rational number has a square root in `Q(sqrt(D))` only if it is a rational square or `D` times a rational square. Applying this to `Delta_d` gives a strong gap restriction.

### Even `d=2L`

Here `N(alpha^d)=r^d=M^2`, with `M=r^L`. Field-square compatibility requires either

\[
M^2-u^2=4
\]

or

\[
M^2-Du^2=4.
\]

The first is impossible for `M>=5` by `(M-u)(M+u)=4`. The second forces `D|4`; with squarefree `D>1`, only `D=2` remains, and the resulting congruence is impossible for the present `r>=5` nonsquare regime. Hence no even gap can support the shell-correction exception.

### Odd `d=2L+1`

Write `r^d=D M^2`. Field-square compatibility reduces to one of

\[
u^2-(DM)^2=4D
\]

or

\[
u^2-r^d=4.
\]

The first is impossible for all sufficiently large odd `d` by the fixed product factorization

\[
(u-DM)(u+DM)=4D.
\]

For the second,

\[
(u-2)(u+2)=r^d,
\qquad
\gcd(u-2,u+2)\mid4.
\]

For fixed `r`, odd prime divisors of `r` must be allocated wholly to one of the two factors, and the common 2-adic part is bounded by the gcd. There are only finitely many such prime allocations. For each allocation, the difference `4` becomes an equality between two fixed-base exponential sequences in `d`, which can hold for only finitely many `d`.

Consequently:

\[
\boxed{
N(P)=-B\text{ can occur only at finitely many return-gap lengths }d
\text{ for each fixed nonsquare cell.}
}
\]

Claim status: `PROVED`.

Moreover, the frozen Stage-2 gap lower bound bounds the source height whenever `d` is fixed. Because the exceptional set of gap lengths is finite, all dynamically reachable shell-correction edges are confined to a bounded source-height region. Hence no sufficiently high source edge lies in this exception. In particular, the exception can occur only finitely often on a hypothetical infinite recurrent ray.

## 6. Independent elementary rank-doubling corollary

For every sufficiently high source hit, Stage 2 proved

\[
|P|<C\alpha^d
\]

and

\[
|\overline P|
\le
\frac B\xi\left(\alpha^d+2\alpha^{-d}\right).
\]

Hence

\[
|N(P)|
<
\frac{CB}{\xi}\left(\alpha^{2d}+2\right).
\]

Outside the finite shell-correction exception,

\[
|N(P)+B|\ge r^{\lceil d/2\rceil}\ge\alpha^d.
\]

For all sufficiently large `d`, `alpha^d>2B`, so

\[
\frac12\alpha^d
<
|N(P)|
<
\frac{CB}{\xi}(\alpha^{2d}+2).
\]

Thus for a cell constant `D_1`,

\[
\boxed{
\xi<D_1\alpha^d.
}
\]

Equivalently,

\[
\boxed{
d>\frac{\log\xi-O_{s,r}(1)}{\log\alpha}.}
\]

This doubles the Stage-2 **elementary** logarithmic gap lower bound.

Now use the frozen finite Pell coordinate

\[
\xi=\eta^m\sigma_i,
\qquad
\xi'=\eta^n\sigma_j,
\qquad h=n-m.
\]

For high source, the Stage-2 correction bound also gives

\[
\alpha^d<2\frac{\xi'}\xi
=2\eta^h\frac{\sigma_j}{\sigma_i}.
\]

Combining with `xi<D_1 alpha^d` and the finiteness of the seed set yields one cell constant `C_{**}` such that every sufficiently high dynamically reachable shell return satisfies

\[
\boxed{
h>m-C_{**}}
\]

and therefore

\[
\boxed{
n>2m-C_{**}.}
\]

Claim status: `PROVED`.

Thus any hypothetical infinite recurrent ray has, after a finite prefix, Pell-unit ranks that at least nearly double at every hit.

This is strictly stronger than the frozen Stage-2 `n>(3/2)m-C_*`, but **quantitatively weaker than the already-consumed concurrent `e65eaad4...` superlacunarity theorem**. It is retained because its proof is purely elementary and exposes the growing `r^{ceil(d/2)}` norm divisibility that is invisible in the reverse-shadow estimate and may be useful in a later profinite attack.

## 7. Arithmetic shell compatibility is not dynamic accessibility

The Lorentz certificate is deliberately **not** promoted into a reachability criterion by itself.

There is an exact false positive already at `(s,r)=(7,7)`.

Take the outer correction word

\[
(-12,-32,-22,18).
\]

It aggregates to

\[
P=-206-106\sqrt7,
\qquad d=4.
\]

The Lorentz reconstruction gives the unique positive shell source

\[
(Y,Z)=(17,7),
\]

which is the exact hit `1->2`, and the arithmetic target is

\[
(627,237),
\]

which is the exact hit `24->63`.

The implied endpoint-index sequence is

\[
1\to2\to4\to9\to24\to63.
\]

But it is not a legal branch: the exact endpoint oracle gives

\[
E_7(7P_7(4))=\{10,11\},
\]

so `4->9` is illegal. In the concurrent local-gate notation, this failed edge has

\[
E=7\cdot37^2-87^2-54=1960,
\]

while the exact legal interval is

\[
-1640<E<1840.
\]

Thus the same witness passes the global Lorentz shell arithmetic and fails one specific ordered local gate.

Claim status: `EXECUTABLE_CHECKED`.

This witness freezes the exact layering:

\[
\boxed{
\text{shell-return Lorentz arithmetic}
\;\supsetneq\;
\text{dynamically reachable return blocks}.
}
\]

The endpoint oracle remains a theorem-critical final admissibility gate.

## 8. Ontology replacement

Stage 2 used

\[
\text{finite Pell seed}\times\text{unit rank}\times\text{growing correction address}.
\]

The present result shows that the **primitive return object** can be made smaller:

\[
\boxed{
(d,P=p+\sqrt r q)
\;\xrightarrow{\text{Lorentz shell certificate}}\;
\le2\text{ shell sources}
\;\xrightarrow{\text{affine residue + positivity}}\;
\text{candidate source/target}
\;\xrightarrow{\text{unique exact reverse chain}}\;
\text{dynamic edge or rejection}.
}
\]

No correction word is needed as input to the final certificate.

Pell seed/rank coordinates are auxiliary growth coordinates rather than part of the minimum shell-return certificate. Likewise, the ordered local-gate residual word from `e65eaad4...` remains theorem-critical **semantics**, but it need not be supplied as input state: unique reverse ancestry reconstructs that trace deterministically for every proposed chord.

The infinite recurrence question becomes:

> Does there exist an infinite composable sequence of shell-compatible Lorentz chords `(d_j,P_j)` whose reconstructed source/target pairs concatenate and whose correction realizations all pass the exact endpoint oracle?

Every such sequence must satisfy the stronger already-consumed `e65eaad4...` superlacunarity condition. Independently, the present growing-norm argument supplies the elementary corollary

\[
n_{j+1}>2n_j-C_{**}.
\]

## 9. Why this does not yet close the mother frontier

The growing divisibility condition does not by itself kill all correction aggregates. It only forces non-shell corrections to carry a norm discrepancy of size at least `r^{ceil(d/2)}`.

The two-source theorem does not make the arithmetic certificate sufficient: Section 7 supplies an explicit shell-compatible but dynamically illegal block.

The new chord certificate and growing norm divisibility still permit the superlacunary sequence left open by `e65eaad4...`.

Accordingly, neither permitted final closure has been reached:

- `INFINITE_HIT_ANCESTRY_RAY_KILLED`: **not proved**;
- `INFINITE_REACHABLE_HIT_RAY_CONSTRUCTED`: **not constructed**.

The correct return is another exact ontology compression, not a forced finite-height claim.

## 10. Next exact attack

The remaining obstruction is now isolated from ambient Pell arithmetic:

1. characterize or generate the shell chords `(d,P)` that survive the **deterministic unique reverse-gate oracle**, rather than replacing legality by the outer digit alphabet;
2. combine the exact `r^{ceil(d/2)} | N(P)+B` obstruction with the already-frozen superlacunary shrinking target;
3. express composability directly at the chord level, with the ordered `E_t` word treated as a reconstructed certificate trace;
4. seek either a growing-modulus/profinite incompatibility theorem for an infinite sequence of accepted chords, or an exact recursively composable chord generator.

A fixed modulus, a bounded no-witness scan, or ambient Pell-unit generation cannot decide this reduced frontier.

## 11. Executable artifact

New checker:

`tools/r042_shell_return_lorentz.py`

It implements only exact integer arithmetic for:

- correction-word aggregation `P=p+sqrt(r)q`;
- the shell-return Lorentz reconstruction;
- deterministic correction-word-free edge certification against a supplied exact predecessor oracle;
- `r^{ceil(d/2)} | N(P)+B` certification;
- the necessary quadratic-field discriminant test for the shell-correction exception.

Focused tests:

`tests/test_r042_shell_return_lorentz.py`

Local result:

`7 tests / PASS`.

The test suite reconstructs all five currently frozen finite return blocks and freezes the `(7,7)` shell-compatible / dynamically-illegal false positive.

No CI/workflow query is required for this L2 research checkpoint: `CI_NOT_REQUIRED_FOR_RESEARCH`.
