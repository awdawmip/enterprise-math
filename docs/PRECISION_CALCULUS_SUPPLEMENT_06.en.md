# P018 — Finite-Precision Proof Calculus, Supplement 06

Status: `ACTIVE RESEARCH NOTE`  
Scope: proof-relevant compression of P017 factor precision and the minimal survivor-prime horizon of a square basin  
Depends on: P017 Root-Factor Horizon and P018 Stages 4–6  
Discipline: prime sieving, least prime factors, and semiprime factorization are classical. This note does not prove Legendre's conjecture.

## 1. Full factor information is more than primality needs

Stage 4 used the factor-precision state

\[
D_y(n)=\{p\le y:p\text{ prime},\ p\mid n\}.
\]

This is a valid compatible precision system: increasing `y` adds factor witnesses and projection to a lower cutoff forgets witnesses above that cutoff.

But for the Boolean predicate “is `n` prime?”, the identity of every visible factor is unnecessary once compositeness has been witnessed.

The first question of Stage 7 is therefore:

> how far can factor precision be compressed without losing primality proof power, and which compressions still remain valid precision systems across cutoffs?

## 2. P018-T55 — Least-witness factor precision is projectively compatible

Status: `PROVED`

Define

\[
\ell_y(n)=
\begin{cases}
0,&D_y(n)=\varnothing,\\
\min D_y(n),&D_y(n)\ne\varnothing.
\end{cases}
\]

Thus `ell_y(n)` records only the least visible tested factor.

For `a<=b`, define the projection

\[
q_{b\to a}(s)=
\begin{cases}
s,&0<s\le a,\\
0,&s=0\text{ or }s>a.
\end{cases}
\]

Then

\[
\boxed{
\ell_a(n)=q_{b\to a}(\ell_b(n)).
}
\]

Proof: if the least prime factor of `n` is at most `a`, both levels see the same least factor. If it lies in `(a,b]`, the fine level records it and projection erases it. If no factor at most `b` is visible, both values are zero. ∎

Therefore the least-witness states themselves form a compatible finite precision chain.

## 3. P018-T56 — Least-witness compression loses no primality proof power

Status: `PROVED`

Fix a square basin `I_k` and cutoff `y<=k`.

The full observation `D_y` refines the least-witness observation `ell_y`, because `ell_y` is a deterministic function of `D_y`.

Nevertheless, for the primality predicate, the two observations have exactly the same conflict multiplicity at every state:

\[
\boxed{
C_{D_y,\mathrm{prime}}(n)
=
C_{\ell_y,\mathrm{prime}}(n).
}
\]

Proof has two cases.

- If no factor at most `y` is visible, `D_y(n)=empty` and `ell_y(n)=0`. Their fibers are identical: the factor-survivor set `S_y(k)`.
- If a factor is visible, both the full-factor fiber and the least-witness fiber consist entirely of composite states, so both primality-conflict multiplicities are zero.

Thus exact identities of additional visible factors can reduce **state ambiguity** without reducing **primality conflict**.

The least visible witness is a proof-sufficient compression of full factor precision for primality.

## 4. P018-T57 — One-bit factor compression is proof-sufficient per level but need not be a precision chain

Status: `PROVED + COUNTEREXAMPLE`.

Define the single bit

\[
b_y(n)=\mathbf1_{D_y(n)\ne\varnothing}.
\]

At one fixed cutoff, this bit has the same primality conflict multiplicity as both `D_y` and `ell_y`:

- `b_y=1` is a composite-only fiber;
- `b_y=0` is exactly the survivor fiber `S_y(k)`.

So the bit is **single-level proof sufficient** for primality.

However, the bit observations do not generally form a compatible precision chain.

Take terminal states `2` and `3`, with cutoffs `2<3`.

At cutoff `3`, both states have bit `1`. At cutoff `2`, the bits are respectively `1` and `0`.

Therefore no deterministic projection from the high-cutoff bit to the low-cutoff bit can exist.

Hence

\[
\boxed{
\text{proof-sufficient compression at every level}
\not\Rightarrow
\text{precision-system-compatible compression across levels}.
}
\]

This is an important P018 design constraint: a usable precision coordinate must preserve both target proof information **and** its forgetting maps.

## 5. Minimal survivor-prime horizon

For the open square basin

\[
I_k=\{k^2+1,\ldots,(k+1)^2-1\},
\]

define

\[
\boxed{
H(k)=
\max\{\operatorname{spf}(n):n\in I_k,\ n\text{ composite}\},
}
\]

with `H(k)=0` if the basin contains no composite state.

This is not the same object as the universal Root-Factor Horizon `k`.

The value `k` is a theorem-known universal cutoff. `H(k)` is the exact smallest cutoff that removes every composite state in this particular basin.

## 6. P018-T58 — Exact minimality of the survivor-prime horizon

Status: `PROVED`

Let `S_y(k)` denote the states in `I_k` with no prime factor at most `y`.

Then

\[
\boxed{
S_y(k)\subseteq\{\text{primes}\}
\iff
y\ge H(k).
}
\]

Proof:

- if `y>=H(k)`, every composite state's least prime factor is at most `H(k)<=y`, so every composite has been removed;
- if `y<H(k)`, choose a composite state whose least prime factor is `H(k)`; it survives cutoff `y`, so the survivor set is not prime-only. ∎

Thus `H(k)` is the exact minimal factor precision at which **absence of a visible factor becomes a sound prime certificate for every remaining basin state**.

## 7. P018-T59 — Root horizon bound and last-shell characterization

Status: `PROVED`

P017 Root-Factor Horizon gives every composite `n in I_k` a prime factor at most `k`. Hence

\[
\boxed{H(k)\le k.}
\]

Let `L_p(k)` be the Stage-4 first-factor shell: basin states whose least prime factor is `p`.

Then

\[
\boxed{
H(k)=\max\{p\le k:L_p(k)\ne\varnothing\},
}
\]

again with value zero if no composite shell is present.

So the minimal primality-certifying factor horizon is exactly the index of the last nonempty composite first-decision shell.

Define the **factor proof slack**

\[
\boxed{
\sigma(k)=k-H(k)\ge0.
}
\]

The universal root horizon may contain `sigma(k)` units of factor precision that are not needed for this particular basin.

## 8. P018-T60 — Prime survivors at the minimal horizon

Status: `PROVED`

At `y=H(k)`, all composites have exited and every prime remains, because primes have no factor at any cutoff at most `k`.

Therefore

\[
\boxed{
S_{H(k)}(k)
=
\{n\in I_k:n\text{ prime}\}.
}
\]

Consequently

\[
\boxed{
\Pi(k)=|S_{H(k)}(k)|.
}
\]

More generally, any cutoff `B>=H(k)` has the same prime-only survivor set until the universal terminal cutoff `k`.

### Non-circularity boundary

`H(k)` is defined using which basin states are composite. Therefore the identity above is a structural theorem, **not by itself a proof shortcut for Legendre's conjecture**.

To obtain genuine proof leverage, one must independently prove an explicit bound

\[
H(k)\le B(k)
\]

without already classifying the basin's primes/composites. Then Legendre at `k` reduces to proving

\[
S_{B(k)}(k)\ne\varnothing.
\]

The existing universal choice is `B(k)=k`. A genuinely smaller independently proved `B(k)` would be new factor-precision leverage.

## 9. P018-T61 — The square-root observation itself is primality-inert inside one basin

Status: `PROVED`.

For every `n in I_k`,

\[
R_2(n)=k.
\]

Therefore the observation

\[
n\mapsto R_2(n)
\]

is constant on the whole P017 terminal set `I_k`.

Its induced precision partition is the one-block partition, exactly the same as a completely uninformative observation.

Hence, by itself, the square-root coordinate has

\[
\boxed{
\text{zero ambiguity gain and zero primality-conflict gain within a fixed basin}.
}
\]

The value of the root coordinate in P017 is not that it distinguishes basin states. Its value is **structural**: it supplies the finite factor-completeness horizon `p<=k` and organizes the relations between other precision axes.

This cleanly separates “coordinate information” from “theorems enabled by the coordinate.”

## 10. P018-T62 — High first-factor shells are semiprime shells

Status: `PROVED`.

Let

\[
U=(k+1)^2-1
\]

be the largest state in the open basin, and let `p<=k` be prime with

\[
\boxed{p>R_3(U).}
\]

Equivalently, `p^3>U`.

If `n in L_p(k)`, then `spf(n)=p`. If `n` had at least three prime factors counted with multiplicity, every one would be at least `p`, so

\[
n\ge p^3>U,
\]

contradiction.

Thus `n` has exactly two prime factors counted with multiplicity. Since `p<=k` gives `p^2<=k^2<n`, the second factor cannot equal `p`.

Therefore every state in the shell has the form

\[
\boxed{
n=pq,
\qquad q\text{ prime},
\qquad q>p.
}
\]

So above the cube-root threshold the factor-precision shells cease to be arbitrary rough-composite shells and become exact semiprime-pair shells.

In particular, if the horizon itself satisfies

\[
H(k)>R_3(U),
\]

then the last nonempty composite precision shell consists entirely of semiprimes `H(k)q` with prime `q>H(k)`.

This connects the proof-horizon question to a narrow prime-pair geometry near the square boundary.

## 11. What Stage 7 changes conceptually

The factor axis now has three different state representations:

1. full witness set `D_y` — most state information;
2. least witness `ell_y` — less state information, same primality proof power, compatible projections;
3. one-bit witness `b_y` — same single-level primality proof power, but generally incompatible across precision levels.

This yields a general P018 lesson:

> The best precision representation is not necessarily the richest representation or the smallest per-level certificate. It must preserve exactly the proof-relevant information **and** the inter-level transition structure needed by the calculus.

The horizon `H(k)` gives a second lesson:

> a universal precision bound and the minimal precision actually needed by one finite problem are different mathematical objects.

That distinction is the direct foundation for Stage 6 adaptive precision selection.

## 12. Prior-art and novelty boundary

Trial division, smallest-prime-factor sieves, rough numbers, and semiprime factorization are classical mathematics. Compressing a divisibility record to a least witness is not claimed as a historical invention.

The project-specific research package under test is the integration of these elementary facts into the P018 proof calculus:

\[
\boxed{
\text{proof-sufficient factor compression}
+
\text{projection compatibility}
+
\text{minimal survivor-prime horizon}
+
\text{first-decision shells}
+
\text{adaptive proof precision}.
}
\]

Historical novelty remains `NOVELTY_UNVERIFIED`.

This note does not prove that `S_(H(k))(k)` is nonempty for every `k`; that is exactly the remaining Legendre existence issue written at the minimal semantic factor horizon.

## 13. Stage-7 status

- P018-T55 least-witness projective compatibility: `PROVED`
- P018-T56 least-witness primality-proof equivalence to full factor state: `PROVED`
- P018-T57 one-bit proof sufficiency / projective incompatibility: `PROVED + COUNTEREXAMPLE`
- P018-T58 minimal survivor-prime horizon criterion: `PROVED`
- P018-T59 `H(k)<=k` and last-shell characterization: `PROVED`
- P018-T60 prime survivor identity at `H(k)` plus non-circularity boundary: `PROVED`
- P018-T61 square-root observation is state/proof inert inside one fixed basin: `PROVED`
- P018-T62 high factor shells are semiprime shells: `PROVED`
- independent nontrivial upper bound `H(k)<=B(k)<k`: `OPEN / HIGH PRIORITY`
- proof that `S_(H(k))(k)` is always nonempty: `OPEN / EQUIVALENT EXISTENCE TARGET`
- adaptive multi-axis P017 proof cost beyond factor precision: `OPEN`

Executable checks live in `src/enterprise_math/p017_precision_horizon.py` and `tests/test_p017_precision_horizon.py`.
