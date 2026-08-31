# Prime Fusion Phase/Fusion Extension — Targeted Independent Verification Return

Status: `FROZEN / STATEMENT-EXPOSED INDEPENDENT VERIFICATION / FIREWALL INTACT`

Frozen at: `2026-08-23T19:25:14.2028524+08:00`

Researcher-ID: `EM-PFVEXT-B47C27`

Task-ID: `RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION`

Hard target:

`PRIME_FUSION_PHASE_EXTENSION_T3_T6_T10_T11_INDEPENDENTLY_VERIFIED_OR_NARROWED_OR_REFUTED`

Final classification:

`PHASE_EXTENSION_VERIFIED_WITH_SCOPE_NARROWING`

The only target-level narrowing is V10: the four powers are exactly the **channel-oriented mixed locus**, not necessarily the full root set of `F` modulo `pq`. V3 and V6 survive; V11 survives exactly under the stated dual-prime hypotheses. The composite-channel continuation of V11 has an exact parity correction.

## 1. Evidence status and exact read boundary

### 1.1 Mathematical evidence type

This is statement-exposed independent verification. The four statements were visible, but their source proofs, source checker, source research narrative, and later comparison/reconciliation notes were not read.

The mathematical proof used only:

1. `research_inputs/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_PACKET_20260823.md@1054ebbf56ae0f9e3cce1e60d743875946d25e18`, blob `7386138e6df6af0d424a9d6933ad35d8c2f35ecc`;
2. ordinary exact polynomial algebra, elementary number theory, CRT, and finite-ring reasoning;
3. the independently authored checker named below.

The optional primitive carrier definition was not needed and was not read. The completed R1–R6 core route was not re-derived.

### 1.2 Execution/router reads

- Global knowledge `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, and `CODEX_SYNC_PROTOCOL.md` at `506eb72c7d409dafda4763403a0bba7c5cc28287`;
- Enterprise Math TASK router at the same global-knowledge SHA;
- repository `AGENTS.md@94f6222675abb38acf8ccfe15c9bc6df83b1f9da`, blob `bb0c06d83f0527762e3d30175661aa84c2430e47`;
- controlling taskbook `research_tasks/PRIME_FUSION_PHASE_EXTENSION_TARGETED_INDEPENDENT_VERIFICATION_20260823.md@94f6222675abb38acf8ccfe15c9bc6df83b1f9da`, blob `bdbf8a56a783f92b378259b91f3fc82c53e155b0`.

The account memory registry was used only to locate the already mandated global-knowledge synchronization path. It supplied no Prime Fusion mathematical statement, proof, checker, or narrative.

### 1.3 Node-reuse disclosure

The execution node was reused after an unrelated high-dimensional task had completed. That prior lane contained no Prime Fusion source proof, checker, or narrative. No prior-lane mathematics, code, output, or artifact was referenced or copied. The machine-readable disclosure is:

`research_output/evidence/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_MANIFEST_20260823.json`

SHA-256: `7073e282f9638701a2faafb60e5efcf83919af94d07a7c2dbfba526c72d2e75e`.

## 2. V3/V6/V10/V11 verdict table

| Cluster | Verdict | Exact retained scope | Repair or counterexample |
|---|---|---|---|
| V3 — product algebra/discriminant | `VERIFIED_EXACTLY_WITH_CONVENTION` | CRT product over `Z`; `omega=[X]` satisfies `omega^2+omega+1=0`; standard monic-polynomial/order discriminant | State the `omega` convention explicitly. |
| V6 — reciprocal-trace idempotent | `VERIFIED_AND_STRENGTHENED` | Every modular root of `F` is automatically a unit; the idempotent splits all prime-power factors of `H`; the pointed primitive root recovers `N,C` | The assumed unit hypothesis is redundant. No primality or oddness is required for pointed recovery. |
| V10 — four phases/order 12 | `VERIFIED_WITH_SCOPE_NARROWING` | Exactly four roots in `M_{p,q}:={x:f(x)=0 mod p, g(x)=0 mod q}`; these are the `U(12)` orbit and split into the shared pair and the other conjugation pair | They need not be all roots of `F mod pq`. At `(a,b)=(2,3)`, `H=91` has eight `F`-roots but only four oriented mixed roots. |
| V11 — sixth-power readout | `VERIFIED_EXACTLY_UNDER_V10` | Every element of `M_{p,q}` has sixth power `(-1,+1)` and gives the exact two gcds for odd `p,q` | For coprime composite channels `A,B`, the exact formulas acquire factors `gcd(B,2)` and `gcd(A,2)`. |

All four clusters are classified. There is no `OPEN` item.

## 3. Independent proofs, hypotheses, and counterexamples

Put

`f=X^2+1`, `g=X^2+X+1`, `F=fg=X^4+X^3+2X^2+X+1`.

For a pointed primitive positive cell, retain the packet notation

`N=a^2+b^2`, `C=a^2-ab+b^2`, `H=NC`, `r=-a*b^{-1} mod H`.

### 3.1 V3 — product fusion algebra and discriminant

There is an integral Bezout identity

`(X+1)f-Xg=1`.

Therefore `(f)+(g)=Z[X]`. The integral CRT, with no field extension or localization, gives

`Z[X]/(fg) -> Z[X]/(f) x Z[X]/(g)`,

`[h] -> ([h] mod f,[h] mod g)`,

as an isomorphism. With `i=[X]` in the first quotient and with

`omega=[X]`, `omega^2+omega+1=0`,

in the second, this is

`Z[X]/(F) ~= Z[i] x Z[omega]`.

The convention matters: `omega` is the primitive **cube** root `(-1+sqrt(-3))/2`, not a primitive sixth root. Consequently

`Norm_Z[i]/Z(a+bi)=a^2+b^2=N`,

`Norm_Z[omega]/Z(a+b*omega)=(a+b*omega)(a+b*omega^2)=a^2-ab+b^2=C`.

Also `Res(f,g)=1`. Hence the standard product formula gives

`Disc(F)=Disc(f) Disc(g) Res(f,g)^2=(-4)(-3)(1)^2=12`.

This is also the trace discriminant of the displayed product order. V3 uses no positivity, primitivity, coprimality, primality, or modular unit hypothesis; those enter only when a cell is interpreted inside the product.

### 3.2 V6 — reciprocal trace and the universal idempotent split

First, the unit hypothesis follows from the root equation. In any commutative quotient ring, if `F(r)=0`, then

`r[-(r^3+r^2+2r+1)]=1`.

Thus `r` is automatically a unit.

In `Z[X,X^{-1}]`, the reciprocal shape of `F` gives the exact identity

`X^-2 F(X)=X^2+X+2+X^-1+X^-2`

`=(X+X^-1)^2+(X+X^-1)`.

For `T=r+r^-1`, a modular root therefore satisfies `T^2+T=0`. With `e=-T`,

`e^2-e=T^2+T=0 mod H`.

There are also useful exact congruences

`e=(r+1)f(r) mod H`,

`e-1=r g(r) mod H`,

coming from the same inverse formula and the Bezout identity.

This yields a stronger theorem for arbitrary `H>=2`: for every root `r` of `F mod H`, put

`A=gcd(e,H)`, `B=gcd(e-1,H)`.

Since `H | e(e-1)` and `gcd(e,e-1)=1`, every prime power dividing `H` divides exactly one of `e,e-1`. Therefore

`gcd(A,B)=1`, `AB=H`.

For the pointed primitive root, the supplied local equations are

`f(r)=0 mod N`, `g(r)=0 mod C`, with `gcd(N,C)=1`.

They give `e=0 mod N` and `e=1 mod C`. Hence

`gcd(e,H)=N`, `gcd(e-1,H)=C`.

No primality, oddness, positivity beyond the pointed-cell setup, or squarefreeness is used. The degenerate cell `(1,1)` has `(N,C,H,r)=(2,1,2,1)` and still returns `(2,1)` exactly.

### 3.3 V10 — exact oriented mixed locus, orbit, and the required repair

Assume now `p=N>3` and `q=C>3` are primes. Primitivity supplies `p!=q` and the CRT modulus `H=pq`.

The pointed residue satisfies `r^2=-1 mod p`. Because `p` is odd, `r^2!=1`, so

`ord_p(r)=4`.

It also satisfies `r^2+r+1=0 mod q`, hence `r^3=1 mod q`. If `r=1 mod q`, then `q|3`, excluded by `q>3`. Therefore

`ord_q(r)=3`,

and CRT gives `ord_H(r)=lcm(4,3)=12`.

Define the channel-oriented mixed locus, rather than the full fused root set, by

`M_{p,q}={x mod pq : f(x)=0 mod p and g(x)=0 mod q}`.

Over the two prime fields, the relevant roots are exactly

`Z_p(f)={r_p,r_p^-1}` and `Z_q(g)={r_q,r_q^-1}`.

There are therefore exactly `2*2=4` CRT combinations. Reducing exponents modulo `4` and modulo `3` shows that they are

`M_{p,q}={r,r^5,r^7,r^11}`.

Each has order `12`. Exponentiation by

`U(12)=(Z/12Z)^x={1,5,7,11}`

acts freely and transitively on this set, so it is exactly the `U(12)` orbit of the pointed `r`.

#### Full `F`-roots are a different set

An arbitrary root of `F mod pq` may select either factor independently at each prime. For primes greater than `3`, `g` also has two roots modulo `p` exactly when `p=1 mod 3`; `f` also has two roots modulo `q` exactly when `q=1 mod 4`. Since the pointed equations already ensure two `f`-roots at `p` and two `g`-roots at `q`, the complete cardinality is

`#Z_{pq}(F)=(2+2*1_{p=1 mod 3})(2+2*1_{q=1 mod 4})`.

Thus `Z_{pq}(F)=M_{p,q}` only when `p=2 mod 3` and `q=3 mod 4`.

The smallest allowed dual-prime cell by coordinate bound, up to swap, already pressures the overbroad reading:

`(a,b)=(2,3)`, `(p,q,H,r)=(13,7,91,60)`.

Here

`M_{13,7}={18,44,60,86}`,

but

`Z_91(F)={9,16,18,44,60,74,81,86}`.

The extra roots `{9,16,74,81}` select `g` at both local primes. Hence the word “exactly” is retained only for `M_{p,q}`, not for all roots of the fused polynomial.

#### Shared coefficients and coordinate swap

Suppose another positive ordered pair `(u,v)` has the same two channel values `N,C`. Then

`uv=N-C=ab`,

`(u+v)^2=N+2uv=3N-2C=(a+b)^2`.

Positivity gives `u+v=a+b`. Thus `{u,v}={a,b}` as roots of the same monic quadratic. The only positive ordered pairs with the same channels are `(a,b)` and `(b,a)`.

Under the fixed marked-residue sign,

`r(b,a)=-b*a^-1=r(a,b)^-1=r^11 mod H`.

Therefore the shared-coefficient pair is exactly `{r,r^11}`. The remaining inversion pair is `{r^5,r^7}`; it is algebraically valid in `M_{p,q}` but cannot arise from a third positive shared-coefficient pair.

Relative to the pointed base phase, the two pairs are precisely the cosets

`{1,11}` and `{5,7}`

of `{+/-1}` in `U(12)`. This coset bit is relative to the marked residue and the channel orientation; it is not an unpointed canonical label.

#### Sign convention

The minus sign is structural for the displayed `g`. If `s=+a*b^-1=-r` is used instead, then the `C`-channel equation becomes

`s^2-s+1=0 mod C`.

For `q>3`, the local `q`-order becomes `6`, while the `p`-order remains `4`; the combined order is still `12`, coordinate swap still sends `s` to `s^-1`, and the sixth power below is unchanged. The four-phase theorem must, however, be stated using `X^2-X+1`, not the original `g`.

#### Composite channel roots

Primality is not required merely for the pointed order. If coprime channels `A>2`, `B>3` satisfy `f(r)=0 mod A`, `g(r)=0 mod B`, then the same argument gives local orders `4,3` and global order `12`. The four powers remain a subset of

`M_{A,B}:={x:f(x)=0 mod A, g(x)=0 mod B}`.

They exhaust `M_{A,B}` if and only if each local root set is exactly its inversion pair. Composite CRT factors can create independently conjugated local roots, so this condition need not hold. For example

`(a,b)=(4,7)`, `(N,C,H,r)=(65,37,2405,343)`

has four roots of `f mod 65` and two roots of `g mod 37`. Its power orbit is

`{47,343,1802,2098}`,

while its oriented mixed locus has eight roots

`{47,343,528,1617,1802,2098,2267,2283}`.

This is why composite channel roots cannot be folded into the dual-prime completeness statement.

### 3.4 V11 — phase-blind sixth power and parity-exact recovery

The full V10 orbit theorem is unnecessary. Let `A,B` be any coprime positive channel moduli and let `x` be any element of the oriented mixed locus:

`x^2=-1 mod A`, `x^2+x+1=0 mod B`.

Then directly

`x^6=(x^2)^3=-1 mod A`,

and `x^3=1 mod B`, so

`x^6=1 mod B`.

Consequently every element of `M_{A,B}`, including mixed roots outside a single four-power orbit, has the same sixth power. Exact CRT arithmetic gives the general formulas

`gcd(AB,x^6+1)=A*gcd(B,2)`,

`gcd(AB,x^6-1)=B*gcd(A,2)`.

Under V10, `A=p>3` and `B=q>3` are odd primes. Hence the claimed formulas hold with no further qualification:

`p=gcd(H,x^6+1)`, `q=gcd(H,x^6-1)`.

For primitive positive composite channels, `C` is always odd, while `N` is even exactly when `a,b` are both odd. Thus

`N=gcd(H,x^6+1)` always,

but

`gcd(H,x^6-1)=C` if `N` is odd and `=2C` if `N` is even.

The nondegenerate cell `(a,b)=(1,3)` gives

`(N,C,H,r,r^6)=(10,7,70,23,29)`

and

`gcd(70,29+1)=10`, `gcd(70,29-1)=14`,

so an unqualified composite-channel formula returning `C=7` is false. The smaller degeneration `(1,1)` similarly returns `gcd(2,r^6-1)=2`, not `C=1`.

The readout retains the oriented factor split—`-1` labels the `f` channel and `+1` labels the `g` channel—but loses:

- the exponent among `1,5,7,11`;
- the coordinate-swap/inversion choice;
- the shared-versus-algebraically-mixed coset bit;
- all additional composite local-conjugation choices.

For an oriented mixed root, the V6 idempotent and the V11 readout satisfy the stronger congruence

`x^6=2e-1 mod H`.

When `H` is odd, the two readouts are equivalent because `2` is invertible. When `H` is even, the displayed forward identity still holds, but recovering `e` by division by `2` is not valid.

### 3.5 Complete hypothesis ledger

| Hypothesis | Where used | What fails without it |
|---|---|---|
| `r` is a unit | Needed to write `r^-1` in V6 | It is automatic from `F(r)=0`; no extra assumption is needed. |
| `a,b>0` | Exact shared-coefficient-pair proof | It fixes `u+v` rather than only its sign and limits interpretation to the one-sector carrier. |
| `gcd(a,b)=1` | Pointed channel premise and `gcd(N,C)=1` | Without the supplied primitive channel coprimality, CRT factor recovery is not licensed. |
| `gcd(A,B)=1` | CRT, global order, and exact gcd products | Without it, local congruences do not combine into an independent two-channel split. |
| `p,q` prime | Exactly two relevant local roots and four-element completeness | Orders and V11 survive more generally, but composite local root sets may contain more conjugation choices. |
| `p>3`, `q>3` | Excludes `-1=1 mod p` and `r=1 mod q`; ensures odd gcd recovery | `p=2` collapses order `4`; `q=3` ramifies `g` and collapses order `3`; even channels create the V11 parity factor. |
| Squarefree `H` | Nowhere in V3 or V6; automatic under dual distinct primes | V6 survives nonsquarefree `H`; composite orbit cardinality depends on local root sets, not a blanket squarefree slogan. |
| Fixed sign `r=-a/b` | Identifies `g=X^2+X+1` and the order-3 local phase | The opposite sign uses `X^2-X+1` and local order `6`. |

## 4. Corrected theorem statements

### Theorem A — integral product fusion

With `omega^2+omega+1=0`,

`Z[X]/((X^2+1)(X^2+X+1)) ~= Z[i] x Z[omega]`,

the discriminant is `12`, and the norms of `a+b(i,omega)` are `N,C`.

### Theorem B — universal reciprocal-trace splitter

For every `H>=2` and every root `r` of `F mod H`, `r` is a unit and `e=-(r+r^-1)` is idempotent. The coprime factors

`A=gcd(e,H)`, `B=gcd(e-1,H)`

satisfy `AB=H`. For the pointed primitive cell they are exactly `N,C`.

### Theorem C — dual-prime oriented four-phase theorem

For the stated dual-prime pointed cell, the channel-oriented locus

`M_{p,q}={x:f(x)=0 mod p, g(x)=0 mod q}`

is exactly `{r,r^5,r^7,r^11}`, the free `U(12)` orbit of `r`. Its inversion pairs are `{r,r^11}` and `{r^5,r^7}`; positivity makes only the first pair the shared-coefficient coordinate-swap pair. No claim that `M_{p,q}` equals every root of `F mod pq` is made without the additional conditions `p=2 mod 3`, `q=3 mod 4`.

### Theorem D — local-equation sixth-power theorem

For coprime `A,B` and every `x` satisfying `f(x)=0 mod A`, `g(x)=0 mod B`,

`x^6=(-1,+1) mod A x B`,

and the two gcds are exactly

`A*gcd(B,2)` and `B*gcd(A,2)`.

The dual-prime V11 formulas follow because both channels are odd.

## 5. Dependency DAG

```text
V3 Bezout identity
  +--> integral CRT product --> Z[i] x Z[omega] --> component norms
  +--> resultant 1 ---------> discriminant product = 12

pointed core local equations f(r)=0 mod N, g(r)=0 mod C
  +--> F(r)=0 --> automatic unit --> Laurent identity --> V6 idempotent
  |                                                +--> pointed N/C recovery
  |                                                +--> universal factor split
  |
  +--> local orders (N>2,C>3) --> global order 12
  |        + primality ----------> two roots per oriented local channel
  |        + coprime CRT --------> V10 four-element oriented mixed locus/orbit
  |        + positivity + fixed N,C --> exact shared coefficient/swap pair
  |
  +--> local sixth powers (-1,+1) -----------------> V11 phase-blind readout
           + coprimality --------------------------> parity-exact gcd formulas

V6 idempotent + oriented local equations --> x^6 = 2e-1 mod H
```

Consequences for the requested audit:

- V6 does not require the V3 product-ring theorem; the Laurent identity and the modular root equation suffice.
- V10 does not require V3; local orders plus CRT prove it.
- V11 does not require V10 orbit completeness or even primality; the two local polynomial equations suffice.
- Product algebra, phase orbit, and sixth-power readout are therefore presentation-compatible but not a single linear dependency chain.

## 6. Executable evidence

Checker:

`experiments/prime_fusion_phase_extension_targeted_verification_checker.py`

SHA-256: `f1dc858eaf76f1ee215562e242172b1d6a88095238c08c8182395bceb45a9d70`.

Evidence JSON:

`research_output/evidence/PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_CHECK_20260823.json`

SHA-256: `38174f0de641c6337bb544a78132ab3f47b6bd6756319b086088555ecefe9c84`.

Exact command:

```powershell
python .\experiments\prime_fusion_phase_extension_targeted_verification_checker.py --cell-bound 80 --root-modulus-cap 5000 --universal-modulus 400 --output .\research_output\evidence\PRIME_FUSION_PHASE_EXTENSION_TARGETED_VERIFICATION_CHECK_20260823.json
```

Actual result: exit `0`, `final_status=PASS`.

Finite ranges and cardinalities:

- symbolic Bezout, resultant, discriminant, and Laurent identities: `PASS`;
- every root of `F mod H` for `2<=H<=400`: 621 roots across 193 moduli; automatic-unit and universal-idempotent factorization checks all `PASS`;
- ordered primitive cells `1<=a,b<=80`: 3,931;
- ordered dual-prime cells in that range: 318;
- ordered composite cells with the retained local order-12 hypotheses: 3,610;
- exhaustive full-root enumeration for 21 unordered primitive cells with `H<=5000`;
- explicit swap, `(1,1)` degeneration, `(3,4)` nonsquarefree, `(2,3)` dual-prime extra-root, `(4,7)` composite-orbit, and `(1,3)` parity controls: all behaved exactly as the corrected theorems state.

The checker enumerates all residues in each declared full-root case; it does not infer completeness from sampled powers. Computation is audit evidence only; Sections 3–5 are the proofs.

## 7. Stronger independent consequences

1. `F(r)=0` makes `r` a unit automatically over every commutative quotient ring.
2. The reciprocal trace gives a universal full prime-power allocation `H=A B`, not merely the pointed cell recovery.
3. Local orders `4` and `3`, and hence pointed order `12`, extend to coprime composite channels with only `A>2,B>3`; primality is used for four-root completeness.
4. The exact dual-prime full fused-root cardinality is controlled by the two cross-splitting indicators `p=1 mod 3` and `q=1 mod 4`.
5. V11 is a local-equation theorem for every oriented mixed root, including composite roots outside the four-power orbit.
6. On the oriented locus, the V6 and V11 readouts satisfy `x^6=2e-1`; for odd `H` they contain the same channel-split information.

## 8. Final classification, nonclaims, and stop boundary

Final classification:

`PHASE_EXTENSION_VERIFIED_WITH_SCOPE_NARROWING`.

The hard target is met: V3, V6, V10, and V11 each have an exact verdict, proof, scope ledger, dependency position, and executable pressure evidence. V10's four-element statement is retained only for the explicitly defined oriented mixed locus. V11's dual-prime statement is exact; its composite continuation uses the parity-corrected gcd theorem.

Nonclaims:

- no root outside `M_{p,q}` is assigned a shared positive coefficient pair;
- no globalization beyond the supplied one-sector positive carrier is made;
- no composite four-phase completeness is claimed without an exact local-root cardinality hypothesis;
- no source-package agreement or disagreement is claimed before Driver reconciliation;
- no source proof, source checker, source narrative, or later comparison note was read.

`RETURN_FREEZE=2026-08-23T19:25:14.2028524+08:00`

`SOURCE_RECONCILIATION=NOT_STARTED`

`REMOTE_PUBLICATION=NOT_STARTED`

Researcher-ID: `EM-PFVEXT-B47C27 / RS-PRIME-FUSION-PHASE-EXTENSION-TARGETED-INDEPENDENT-VERIFICATION`

Global-Knowledge-Sync: `main@506eb72 / GLOBAL_KNOWLEDGE_V1`
