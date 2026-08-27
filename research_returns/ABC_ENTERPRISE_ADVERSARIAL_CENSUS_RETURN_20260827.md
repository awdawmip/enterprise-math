# ABC Enterprise Adversarial Census — Research Return

Status: `RESEARCH_RETURN_FROZEN / EXACT_INFINITE_OBSTRUCTION_FAMILY / AWAITING_DRIVER_REVIEW`

Date: `2026-08-27`

Task: `RS-ABC-ENTERPRISE-ADVERSARIAL-CENSUS`

Publication: `TP2-3132361FDFD8E30AD1F9`

Researcher-ID: `EM-ABC4-7DA30C`

Execution: `ER-B6E4F8165904ABEBD107`

Primary task-native verdict: `EXACT_INFINITE_OBSTRUCTION_FAMILY`.

Hard target: `ABC_ADVERSARIAL_CENSUS_AND_NOGO_CERTIFICATES_FROZEN`.

## 1. Scope and source boundary

The immutable task asks for an exact primitive-abc census stressing capped-core, boundary, and carry heuristics. I used the frozen typed Enterprise source refs

- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5`;
- `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md@c7a5a1c148f48f3c9d57cafe79536030541ed2d5`.

Those sources keep native line/path semantics separate from derived arithmetic readouts. This return preserves that separation: no radical, valuation, beta, carry, or census statistic is promoted to primitive native point ontology.

The taskbook names `q,R,H,beta,I_cap` but does not durably restate formulas for `beta/I_cap/D_sup`. Repository search and the available parent record did not expose a canonical formula. Therefore this return makes one explicit operational audit choice rather than silently asserting provenance:

\[
r=\operatorname{rad}(abc),\quad R=\log r,\quad
H=\log\frac{abc}{r},\quad
\beta=\log\frac{c^2}{4ab},
\]
\[
I_{\rm cap}^{(R)}=
\sum_{p\mid abc}\min\bigl((v_p(abc)-1)\log p,R\bigr),
\qquad
D_{\rm sup}^{(R)}=H-I_{\rm cap}^{(R)}.
\]

`I_cap^(R)` and `D_sup^(R)` are therefore **operational audit readouts** until Driver maps them to, or rejects them against, the parent conversation definition. The carry theorem below is independent of this choice.

For the standard quality readout,

\[
q=\frac{\log c}{R},
\]

the definitions give the exact identity

\[
\boxed{3\log c=R+H+\beta+\log4}
\]

because `ab=c^2/(4e^beta)` and `abc=r e^H`.

## 2. Exact census

The checker enumerates unordered primitive triples

\[
1\le a\le b,\qquad a+b=c\le5000,\qquad \gcd(a,b)=1.
\]

All counterexample decisions use integer cross-products; floating logarithms are used only to rank readouts.

Exact corpus size:

\[
\boxed{3,800,228}
\]

and this independently matches

\[
\sum_{c=3}^{5000}\frac{\varphi(c)}2=3,800,228.
\]

Exactly `80` enumerated triples satisfy `q>1`.

Top quality rows:

| a | b | c | rad | q | β | Icap/R |
|---|---|---|---|---|---|---|
| 1 | 4374 | 4375 | 210 | 1.567887 | 6.997596 | 1.902977 |
| 1 | 2400 | 2401 | 210 | 1.455673 | 6.397763 | 1.819513 |
| 3 | 125 | 128 | 30 | 1.426565 | 2.390840 | 1.946395 |
| 625 | 2048 | 2673 | 330 | 1.360723 | 0.333248 | 2.590380 |
| 1 | 512 | 513 | 114 | 1.317571 | 4.855933 | 1.463922 |
| 1 | 242 | 243 | 66 | 1.311101 | 4.110891 | 1.572337 |
| 5 | 1024 | 1029 | 210 | 1.297214 | 3.945481 | 1.727837 |
| 1 | 80 | 81 | 30 | 1.292030 | 3.020577 | 1.580408 |
| 10 | 2187 | 2197 | 390 | 1.289752 | 4.010531 | 1.859834 |
| 13 | 243 | 256 | 78 | 1.272790 | 1.646050 | 2.000000 |

The low-boundary slice `beta <= 0.1` is not empty of high-quality examples:

| a | b | c | q | β | Icap/R |
|---|---|---|---|---|---|
| 1024 | 1377 | 2401 | 1.184565 | 0.021853 | 2.339395 |
| 32 | 49 | 81 | 1.175719 | 0.045048 | 2.144207 |
| 2048 | 2187 | 4235 | 1.078262 | 0.001078 | 2.055653 |
| 343 | 625 | 968 | 1.034431 | 0.088688 | 1.881371 |
| 640 | 729 | 1369 | 1.029908 | 0.004235 | 1.891421 |

In particular, `1024+1377=2401` has `q≈1.184565` with `beta≈0.021853`, and `32+49=81` has `q≈1.175719` with `beta≈0.045048`. Thus a boundary-only explanation is already stress-tested by explicit interior examples.

## 3. Minimal capped-core no-go certificate under the operational R-cap

Test the coefficient-2 family

\[
(C_k):\qquad I_{\rm cap}^{(R)}\le2R+k\beta
\]

for `k in {0,1,2,4,8}`.

The same triple is the **minimal counterexample by c** for every tested coefficient:

\[
\boxed{32+49=81},\qquad
32=2^5,\ 49=7^2,\ 81=3^4.
\]

Here

\[
r=\operatorname{rad}(32\cdot49\cdot81)=42,
\]

and every repeated tower is below the cap `R=log42` because

\[
2^4=16<42,\qquad 7<42,\qquad 3^3=27<42.
\]

Hence

\[
I_{\rm cap}^{(R)}=H=\log(16\cdot7\cdot27)=\log3024.
\]

Already at `k=0`,

\[
I_{\rm cap}^{(R)}-2R
=\log\frac{3024}{42^2}
=\boxed{\log\frac{12}7}>0.
\]

Also

\[
\beta=\log\frac{81^2}{4\cdot32\cdot49}
=\log\frac{6561}{6272}.
\]

The checker verifies by exact integer cross-products that `(C_k)` fails for each tested `k=0,1,2,4,8`; no floating comparison is used for the certificate. In fact this same witness also kills every integer `0<=k<=11`, since

\[
\frac{12}7>\left(\frac{6561}{6272}\right)^{11},
\]

while the inequality reverses at `k=12` for this particular witness. The finite census contains still more severe near-balanced overloads; for example `2048+2187=4235` has `beta≈0.001078` and `I_cap^(R)/R≈2.055653`.

This kills a universal coefficient-2 capped-core claim with a modest boundary correction under the operational cap. It does **not** by itself refute a differently defined parent `I_cap`.

## 4. Exact infinite carry-activation obstruction

Use the taskbook's carry statistic

\[
h_p(n)=v_p\left(\frac1c\binom{nc}{na}\right)
      =v_p\binom{nc}{na}-v_p(c),
\]
and

\[
\tau_p=\min\{n\ge1:h_p(n)>0\}.
\]

### Theorem

For every prime `p`, the primitive family

\[
\boxed{(a,b,c)=(1,p-1,p)}
\]

satisfies

\[
\boxed{h_p(n)=0\quad(1\le n\le p),\qquad h_p(p+1)=1},
\]

and therefore

\[
\boxed{\tau_p=p+1}.
\]

### Proof

Since

\[
\binom{np}n=p\binom{np-1}{n-1},
\]

and `v_p(c)=v_p(p)=1`,

\[
h_p(n)=v_p\binom{np-1}{n-1}.
\]

For `1<=n<=p`,

\[
np-1=(n-1)p+(p-1),
\]

while `n-1<p`. Lucas' theorem gives

\[
\binom{np-1}{n-1}
\equiv
\binom{p-1}{n-1}\binom{n-1}0
\not\equiv0\pmod p,
\]

so `h_p(n)=0`.

At `n=p+1`, Legendre's formula gives

\[
v_p((p^2+p-1)!)=p+1,\quad
v_p(p!)=1,\quad
v_p((p^2-1)!)=p-1,
\]

hence

\[
v_p\binom{p^2+p-1}p=1.
\]

Thus `h_p(p+1)=1` and `tau_p=p+1`. QED.

### Consequences

This is an exact infinite obstruction, not finite evidence:

1. no universal rule `tau_p<=p` can hold;
2. no fixed scale window can force every radical prime to contribute positive carry energy;
3. for every fixed `W`, choosing a prime `p>W` gives a primitive abc triple whose `p`-channel is silent for every `1<=n<=W`;
4. any ABC2 energy theorem must either allow a window growing beyond `p`, aggregate information not requiring each radical prime to activate, or use additional arithmetic structure.

The checker directly replays this theorem for all `168` primes `p<=997`, with zero regression failures. That replay is corroboration only; the theorem is the proof above.

## 5. Boundary-payment stress result

Under the operational `R`-cap, the parent-shaped inequality

\[
D_{\rm sup}^{(R)}\le2\beta+\log16
\]

is equivalent to the exact rational comparison

\[
\frac{e^H}{e^{I_{\rm cap}^{(R)}}}
\le\frac{c^4}{a^2b^2}.
\]

The checker finds **no counterexample** among all `3,800,228` triples with `c<=5000`.

Freeze this only as

`BOUNDARY_PAYMENT_OPERATIONAL_NO_COUNTEREXAMPLE_IN_RANGE`.

It is not reported as a global theorem here, both because finite enumeration cannot prove it and because the parent `D_sup` formula is not durably present in the taskbook.

## 6. Reproducibility

Artifacts:

- `scripts/check_abc_enterprise_adversarial_census.py`
- `research_artifacts/ABC_ENTERPRISE_ADVERSARIAL_CENSUS/census_summary.json`

Default replay:

```text
python scripts/check_abc_enterprise_adversarial_census.py \
  --c-max 5000 \
  --carry-prime-max 997 \
  --json-out research_artifacts/ABC_ENTERPRISE_ADVERSARIAL_CENSUS/census_summary.json
```

Frozen summary canonical-payload SHA-256:

`6d3e4346f8e5150f61e2be7bde415ab3649a4b9e9405c3b177803d4ee420f347`.

The checker also verifies the corpus cardinality independently via the totient formula.

## 7. Task disposition

Primary verdict:

\[
\boxed{\texttt{EXACT_INFINITE_OBSTRUCTION_FAMILY}}
\]

because the carry family is an exact all-prime theorem and directly kills a natural universal activation/payment heuristic.

Secondary no-go:

`CAPPED_CORE_COEFFICIENT_2_OPERATIONAL_NO_GO`

via the minimal exact witness `32+49=81` for every tested `k in {0,1,2,4,8}`.

Surviving item:

`BOUNDARY_PAYMENT_OPERATIONAL_NO_COUNTEREXAMPLE_IN_RANGE` only.

Unresolved residue:

1. map the operational `I_cap^(R),D_sup^(R)` symbols to the parent analysis before any downstream theorem cites these names without the superscript;
2. ABC1 must not rely on `I_cap<=2R+k beta` for the tested small coefficients under this operational cap;
3. ABC2 must accommodate `tau_p=p+1` and therefore cannot demand every radical prime activate by scale `p`;
4. no new generic Enterprise tool was created: the work is a task-specific exact enumeration/valuation certificate, composing the existing scale-enumeration/valuation and precision/carry tool families.

Recommended control-plane routing: Driver review this result; if the operational cap matches the parent definition, feed `32+49=81` directly into the active ABC1 lane. Feed the exact `(1,p-1,p)` carry theorem directly into ABC2 regardless of that mapping. Do not create duplicate successors while those sibling lanes are already leased.
