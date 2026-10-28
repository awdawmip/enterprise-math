# D25/LIFT — nonsingular interior observer: exact middle/high nonlocal reconstruction

Date: 2026-10-28. Logical onhour Research lane: `chatgpt-research-onhour-enterprise-math-20260923`.
Classification: **AUTHOR-SIDE / EXACT ALL-PRIME ALGEBRAIC DERIVATION / 67 EXECUTED EXACT PRIME TESTS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_EXECUTED**. This is not a Source Result, independent review, native H0/B0 experiment, or completion of LIFT.

## 1. Authority, frozen input, and genuine new dependency

Mother: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`.
Publication: `TP2-B6F4FC938FF94941C1B7`.
Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (**unchanged**).
ACTIVE P000 and six-axis/three-dimensional-slice provenance are unchanged. This is a typed external scalar number-theory observer, not a native spatial coordinate or H0/B0 Frobenius calculation.

Consume (do not recredit): the original-216 weighted middle/high unit reciprocity, author note at Enterprise Math commit `382e6d3005559d808b8ed49cded36d2b01b299b2`; and the exact nonsingular endpoint reduction (E1)–(E6), author note at `d8dee3c159b5c991272d50e29165b357ae8718cf`. The present increment independently proves an elementary **unweighted** middle/high product law and composes it with the new interior observer, giving a source-preserving, nonlocal reduction for the *original p³ target*. The old Gosper/no-go, Hensel and CM0 searches are not replayed.

Let `p=6m+1>3` be prime, `q=p³`, and work in `Z_(p)`. Set

\[
t_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
=\frac{(2n)!(3n)!}{(n!)^5\,216^n},
\quad
a_n=\frac{(66n^2+113n+49)t_n}{9(n+1)^3},\quad
J_p=\sum_{n=0}^{p-2}a_n.
\]

The original weighted observer is `W_p=\sum_{n=0}^{p-1}(6n+1)t_n`.
The exact previously established endpoint identity implies
`W_p\equiv J_p-4 \pmod{p³}`; all denominators of `a_n`, `0\le n\le p-2`, are p-adic units. The original open frozen target is `W_p\stackrel?\equiv p\pmod{p³}` for `p\equiv13,19\pmod{24}`.

## 2. Exact valuation bands (no heuristic cutoff)

For `0\le n<p`, factorial valuations give

\[
\nu_p(t_n)=\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor.
\]

Consequently, for `p=6m+1`:
- `0\le n\le2m`: valuation 0;
- `2m+1\le n\le3m`: valuation 1;
- `3m+1\le n\le4m`: valuation 2;
- `4m+1\le n\le p-1`: valuation 3.

The `a_n` have exactly the same valuation in the interior `n\le p-2`, since their rational prefactor is p-integral, **but may gain further valuation when its numerator happens to vanish modulo p**. The conclusion needed here is the valid lower bound `\nu_p(a_n)\ge\nu_p(t_n)`. Thus `a_n\equiv0\pmod{p³}` for `n\ge4m+1`.

## 3. Elementary unweighted reflection law (proved)

For `0\le r<m` set
`j_r=2m+1+r\in(p/3,p/2)` and
`k_r=p-j_r=4m-r\in(p/2,2p/3)`. Define
`u_r=(t_{j_r}/p)\bmod p\in\mathbb F_p^\times`.

**Theorem A.** For all such primes and indices,

\[
\boxed{\left(\frac{t_{j_r}}p\right)
\left(\frac{t_{k_r}}{p^2}\right)
\equiv\frac1{36j_r^3}\pmod p.}\tag{A}
\]

**Proof.** For any `0\le s<p`, `(p+s)!/p\equiv-s!\pmod p` by Wilson. In the indicated ranges, `2j<p<3j<2p`, and `p<2k<3k<2p`. Therefore

\[
\frac{t_j}{p}\equiv
-\frac{(2j)!(3j-p)!}{j!^5 216^j},\qquad
\frac{t_k}{p^2}\equiv
\frac{(p-2j)!(2p-3j)!}{(p-j)!^5 216^{p-j}}\pmod p.
\]

The Wilson reflection identity `a!(p-a)!\equiv(-1)^a a\pmod p` gives
`(2j)!(p-2j)!\equiv2j`,
`(3j-p)!(2p-3j)!\equiv(-1)^{j-1}3j`,
and `j!(p-j)!\equiv(-1)^j j`.
Multiplying and using `216^p\equiv216\pmod p` yields
`(-1)(2j)((-1)^{j-1}3j)/[(-1)^j j^5 216]=1/(36j^3)`. QED.

This is equivalent to the previously reported weighted unit-pair formula after multiplying by the original signed weights. The proof here is direct and preserves both *individual* factorial sources; it is not new authority to erase the signed high tail or native odd observer.

## 4. The new p³ nonlocal interior theorem

Define the rational coefficient, reduced modulo p only at its final use,

\[
\boxed{\mathcal R(r)=
\frac{9(66r^2-25r+3)}
{4(1-3r)^3(3r+2)^3}\pmod p.}\tag{B}
\]

Its denominators are p-units for `0\le r<m`. Applying (A), replacing `k_r\equiv-j_r\pmod p`, and using `j_r\equiv r+2/3\pmod p`, proves the **termwise** formula

\[
\boxed{\frac{a_{4m-r}}{p^2}\equiv
\mathcal R(r)\,u_r^{-1}\pmod p.}\tag{C}
\]

Indeed the intermediate, uncompressed rational readout is

\[
\frac{a_{k_r}}{p^2}
\equiv \frac{66j_r^2-113j_r+49}
{324j_r^3(1-j_r)^3}\,u_r^{-1}\pmod p,
\]

which reduces algebraically to (B). This retains the order, multiplicity, signed coefficients, valuation class and specific `j_r\leftrightarrow k_r` provenance.

By the valuation bands, the *whole original nonsingular sum* therefore satisfies

\[
\boxed{
J_p\equiv
\sum_{n=0}^{3m}\frac{(66n^2+113n+49)t_n}{9(n+1)^3}
+p^2\sum_{r=0}^{m-1}\mathcal R(r)\,u_r^{-1}
\pmod{p^3}.}\tag{D}
\]

Combining with the exact endpoint reduction yields a **target-preserving equivalence** for the frozen target classes:

\[
\boxed{
W_p\equiv p\pmod{p^3}
\iff
\sum_{n=0}^{3m}a_n+
p^2\sum_{r=0}^{m-1}\mathcal R(r)u_r^{-1}
\equiv p+4\pmod{p^3}.}\tag{E}
\]

The unproved part is the right-hand *global evaluation*. (A)–(E) are universally algebraic for `p\equiv1\pmod6`; they do **not** prove this global evaluation or the original LIFT. They merely reduce the independent high tail to a first-valuation middle-band unit observer.

## 5. Executed exact certificate, and a shortcut falsifier

Executable standard-library Python:
`research_notes/portable_direct/d25_onhour_nonlocal_interior_reflection_guard_20261028.py`.

Executed on all **67 primes `7\le p<800` with `p\equiv1\pmod6`**, checking **4,158 separate indexed pairs**. Independent original integer-binomial and hypergeometric recurrence computations agree term-by-term. For each prime, the executable checked (A), (C), the entire high tail, the zero-valuation cutoff, (D), the exact `W/J` endpoint congruence, and original `W_p=p\pmod{p³}` as an *instance regression only* for the two target classes. Actual output:

```text
PASS_D25_J_INTERIOR_NONLOCAL_REFLECTION 67 primes; 4158 paired terms
```

At `p=373`, `m=62`, `p²=139129`, `p³=51895117`, the exact residues are:

```text
sum_{n=0}^{124} a_n = 33858706  (mod p^3)
sum_{n=125}^{186} a_n = 9828177 (mod p^3)
sum_{n=187}^{248} a_n = 59*p^2 = 8208611 (mod p^3)
sum_{n=249}^{371} a_n = 0       (mod p^3)
J_373 = 377; W_373 = 373        (mod p^3)
```

The reconstruction `33858706+9828177+8208611=51895494\equiv377\pmod{51895117}` is exact. **The high band is not negligible:** `59\ne0\pmod{373}`; simply truncating `J_p` at `3m` would be false at p³, even though its high-band terms all have valuation at least two. This is a concrete falsifier for that tempting shortcut. The finite test does not prove (E) for all target primes.

## 6. BRC, roles, and exact next action

BRC resolution: **COMPOSE_APPLIED**: the existing valuation-band, reflection/product and endpoint interfaces are composed without flattening the middle/high indexed pair into an unexplained scalar. For the *declared W/J observer modulo p³* the high band can be replaced by its explicit middle-unit inverse with no lost scalar information, because (C) proves exact fiber constancy at the stated precision and horizon. This equivalence **does not** authorize replacing the native H0/B0 module, X6 Cell carrier, full signed/odd Green–Hesse port, `\kappa`, `\Delta_p-R_p`, or other future operators.

Scientific next action: seek an independent finite-character/CM or multi-index WZ evaluation of the **first sum plus the explicitly paired inverse-middle sum** in (E), keeping the original `p=373` source and both target residue classes. Disprove any proposed universal cancellation with an exact prime counterexample before promotion. Do not repeat the old single-Gosper search or recredit earlier UR/root/Clausen work.

Native highest priority: existing support issue **#1559** for the original same-class H0/B0 divided-power `[X]U\bmod139129`, real module rank, genuine semilinear Frobenius direction/eta and signed observer, original kappa and Delta-R, and independently reproducible source-bound data; **PENDING_OWNER / NOT_EXECUTED** at this run's read. The present scalar reconstruction is not that benchmark.

Control and continuity: current authenticated gateway `em_status` gave a schema/version snapshot but the requested `DIRECTED_RESEARCH` context read failed `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`; Site status `research_authority_granted=false`, `write_relay_enabled=false`. No fresh Source claim/dispatch/open, research-activity registration, formal checkpoint/Result, review, maintenance-lane operation or native computation was asserted or attempted. The existing historic #6575/#6576 pointers and three old staging items remain non-owning historical evidence, not this run's verified claim. Current session/claim/run/request are **unverified/no new ID**, not invented. Old Source boundary and P000 are not modified. Next authorized native step is to obtain a fresh exact continuation/receipt under the Site-bound researcher authorization and consume it before any new request. GitHub author-side storage is **not** Source admission.
