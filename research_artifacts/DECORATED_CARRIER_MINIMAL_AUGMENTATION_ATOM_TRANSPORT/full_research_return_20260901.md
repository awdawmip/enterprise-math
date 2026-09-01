# Decorated Carrier Minimal Augmentation: C2 Pairing Frame -> S3 Pairing State -> S4 Atom Transport

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

- Task-ID: `RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT`
- Publication-ID: `TP2-DCE2A9D900EF145F0E77`
- Researcher-ID: `EM-DCTRMIN-7BC444`
- Claim-ID: `chatgpt-dctrmin-20260901-1045`
- Execution record: `ER-DEB4D6566F79BCBC451B`
- Execution branch: `research/decorated-carrier-minimal-augmentation-atom-transport-em-dctrmin-7bc444`
- Execution base: `f87f026d13485309d2c353ecf81322e2501c6512`
- Hard target: `MINIMAL_TRANSPORT_AUGMENTATION_HIERARCHY_CLASSIFIED`
- Terminal verdict: `SUCCESS`
- Terminal class: `C2_TO_S3_C3_TWISTED_LIFT_AND_S3_TO_S4_V4_TWISTED_LIFT_HIERARCHY_CLASSIFIED`

## 1. Executive result

The frozen decorated-carrier hierarchy admits a sharper and smaller augmentation atlas than “choose an `S3` section, then choose an `S4` section”.

The exact two lift layers are the standard split extensions

\[
1\longrightarrow A_3\cong C_3
\longrightarrow S_3
\overset{\operatorname{sgn}}{\longrightarrow} C_2
\longrightarrow 1,
\]

and

\[
1\longrightarrow V_4
\longrightarrow S_4
\overset{\Phi}{\longrightarrow} S_3
\longrightarrow 1.
\]

The marked carrier state makes the first split **typed and canonical**: its stabilizer inside `S3` is exactly the accepted opposite-frame `C2`. Therefore an `L1` connection is precisely the sign quotient of an `L2` connection, without globally numbering the three pairing states.

Fix an `L1` holonomy

\[
h:\pi_1(X)\to C_2.
\]

Then the residual `L1 -> L2` lift freedom, modulo the kernel vertex gauge, is

\[
\boxed{H^1(X;C_{3,h})},
\]

where the nontrivial element of `C2` acts on `C3` by inversion. Relative to the canonical marked split, an `S3` lift has the unique form

\[
\rho(\gamma)=a(\gamma)s(h(\gamma)),
\qquad a(\gamma)\in C_3,
\]

and flatness is exactly the twisted cocycle law

\[
a(\gamma\delta)=a(\gamma)+(-1)^{h(\gamma)}a(\delta)\pmod 3.
\]

Thus an `S3` **section is not the missing L2 structural datum**. The zero class gives the canonical split lift, while a genuinely carrier-mixing augmentation is a nonzero class in `H^1(X;C_{3,h})`.

Next fix an `L2` holonomy

\[
\rho:\pi_1(X)\to S_3.
\]

Relative to any temporary homomorphic section `s:S3->S4`, every `S4` lift is

\[
\widetilde\rho(\gamma)=v(\gamma)s(\rho(\gamma)),
\qquad v(\gamma)\in V_4,
\]

with twisted law

\[
v(\gamma\delta)=v(\gamma)+\rho(\gamma)\cdot v(\delta).
\]

Modulo vertex atom-frame gauge, the residual `L2 -> L3` freedom is

\[
\boxed{H^1(X;V_{4,\rho})}.
\]

All four homomorphic sections `S3->S4` are conjugate by `V4`; more strongly, changing section by `w in V4` changes the coordinate cocycle by the twisted coboundary

\[
\delta_\rho w(\gamma)=w-\rho(\gamma)\cdot w.
\]

Therefore the four sections represent the **same unframed zero lift class**. A section is a coordinate/gauge choice, not independent L3 structure. A genuinely new atom-kernel augmentation is a nonzero class in `H^1(X;V_{4,\rho})`.

For the accepted parent homotopy type

\[
X\simeq K_R\vee\bigvee^m S^1,
\]

write

\[
\beta=\dim_{\mathbf F_2}H^1(X;\mathbf F_2)
      =\frac{(k-1)(k-2)}2+m
\]

for `a != b`; the equality stratum has the same formula with `m=0`.

Then the exact lift dimensions are:

### L1 -> L2

\[
\dim_{\mathbf F_3}H^1(X;C_{3,h})=
\begin{cases}
0,&\beta=0,\\
\beta,& h=0,\\
\beta-1,& h\ne0.
\end{cases}
\]

Hence the relative lift fibre has `3^d2` classes. If temporary L1 framing is also quotiented, the residual constant `C2` acts by inversion; therefore the full-gauge orbit count is

\[
1\quad(d_2=0),
\qquad
1+\frac{3^{d_2}-1}{2}\quad(d_2>0).
\]

### L2 -> L3

Let

\[
f(\rho)=\dim_{\mathbf F_2}V_4^{\operatorname{im}\rho}.
\]

For `beta>=1`,

\[
\boxed{
\dim_{\mathbf F_2}H^1(X;V_{4,\rho})
=2\beta-2+f(\rho).
}
\]

For `beta=0`, the dimension is `0`. Concretely:

- trivial `rho`: `f=2`, so `d3=2 beta`;
- nontrivial image contained in one transposition subgroup: `f=1`, so `d3=2 beta-1`;
- image containing a 3-cycle or two distinct transpositions: `f=0`, so `d3=2 beta-2`.

On one loop the three exact cases are

\[
\rho=1:\ d_3=2,
\qquad
\rho=\text{transposition}:\ d_3=1,
\qquad
\rho=\text{3-cycle}:\ d_3=0.
\]

The decisive naturality boundary is therefore also sharper than the parent statement: **zero split lifts are canonical as gauge classes; what the lower reduct does not supply is any preferred nonzero kernel-cohomology class.** Any rule selecting a nonzero `C3` or `V4` class is genuinely exogenous unless additional typed structure is declared.

## 2. Frozen input and exact level semantics

The task freezes the accepted decorated carrier/resonance typed CW complex and the parent C2 result. No arithmetic/support theorem is changed here.

The four levels are:

### `L0_ARITHMETIC_REDUCT`

Objects are frozen decorated carrier/resonance states. Morphisms are the accepted support-typed carrier/resonance groupoid morphisms. There is no cross-support opposite-frame connection.

### `L1_PAIRING_FRAME_C2`

At each marked pairing cell `x`, let `F_x` be the three perfect matchings/pairing states and let `c_x in F_x` be the distinguished carrier matching. Put

\[
O_x=F_x\setminus\{c_x\},\quad |O_x|=2,
\]

and let

\[
P_x=\operatorname{Bij}(\mathbf F_2,O_x).
\]

The accepted new connection is a flat `C2` torsor connection on the family `P_x`. Framed representatives form `Z^1(X;F2)` and unframed classes form `H^1(X;F2)`.

### `L2_PAIRING_STATE_S3`

Let

\[
Q_x=\operatorname{Bij}(\{0,1,2\},F_x),
\]

with the natural right `S3` action. This is the full pairing-state frame torsor.

The alternating subgroup `A3` is normal and the quotient `Q_x/A3` is the two-element orientation torsor of the three-element set `F_x`. Because `c_x` is already distinguished, orientation of `F_x` is canonically equivalent to ordering the opposite pair `O_x`: the ordered pair `(o_0,o_1)` is sent to the orientation class of `(c_x,o_0,o_1)`.

Thus there is a canonical typed torsor isomorphism

\[
\boxed{Q_x/A_3\cong P_x.}
\]

This is the intrinsic meaning of the sign map `S3->C2` in the present interface. It uses the marked carrier state but introduces no global names for the other two states.

An `L2` object over an `L1` object is a flat `S3` connection on `Q_x` whose quotient under this canonical map is the prescribed flat `C2` connection.

### `L3_ATOM_TRANSPORT_S4`

The atom frame is a four-element frame whose induced action on the three perfect matchings is the standard quotient

\[
\Phi:S_4\to S_3,
\qquad \ker\Phi=V_4.
\]

An `L3` object over an `L2` object is a flat `S4` connection projecting to the prescribed `S3` connection. Temporary atom-frame changes are vertex `S4` gauge; when the L2 representative is held fixed, relative kernel gauge is vertex `V4` gauge.

## 3. L0 -> L1: inherited minimal exogenous layer

The parent result already proved the exact first augmentation boundary:

\[
\operatorname{Conn}^{\rm flat}_{C_2}(X)/\operatorname{Gauge}
\cong H^1(X;\mathbf F_2).
\]

The arithmetic reduct does not choose a class. `0` is the canonical zero-holonomy class only **after** the new C2 connection primitive has been admitted into the interface; it is not a derivation of an opposite-frame transport from L0.

Necessity is the accepted same-reduct/different-connection family: whenever `beta>0`, the same L0 carrier supports `2^beta` different unframed C2 connections. Even when `beta=0`, the connection primitive still changes the type of the interface, although its global gauge class is unique.

Sufficiency is the parent cocycle construction.

Tool disposition:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`;
- `T9_HOLONOMY_COCOYCLE_GLUING`: `REUSE_APPLIED`;
- parent exact finite symmetry/cohomology checker: `REUSE_APPLIED`;
- new general-purpose tool family: `NONE`.

## 4. L1 -> L2: exact C3 twisted-lift theorem

### 4.1 Canonical typed split

Fix a vertex `x` and write the marked state as `c`. The stabilizer

\[
H_c=\operatorname{Stab}_{S_3}(c)
\]

has order two. Its nontrivial element swaps the two states in `O_x`. Therefore

\[
H_c\cong C_2
\]

canonically as an action on the accepted opposite-frame torsor.

The restriction of the sign map to `H_c` is an isomorphism

\[
\operatorname{sgn}|_{H_c}:H_c\overset{\sim}{\to}C_2.
\]

Its inverse gives a typed splitting

\[
s_c:C_2\to S_3
\]

without numbering all three pairing states. This is exactly why the first lift problem is cleaner than an arbitrary `C2` quotient of an unmarked three-set.

Every `sigma in S3` has a unique decomposition

\[
\sigma=a\,s_c(\epsilon),
\qquad a\in A_3,\quad \epsilon=\operatorname{sgn}(\sigma).
\]

Conjugation by the nontrivial `s_c(C2)` element sends every 3-cycle to its inverse. Identifying `A3` with additive `C3`, the action is

\[
\epsilon\cdot a=(-1)^\epsilon a.
\]

### 4.2 Necessity and sufficiency

Let the L1 holonomy be

\[
h:\pi_1(X)\to C_2.
\]

Every lift `rho:pi1(X)->S3` with `sgn rho=h` has a unique expression

\[
\rho(\gamma)=a(\gamma)s_c(h(\gamma)).
\]

Then

\[
\rho(\gamma\delta)=\rho(\gamma)\rho(\delta)
\]

holds if and only if

\[
a(\gamma\delta)
=a(\gamma)+(-1)^{h(\gamma)}a(\delta).
\]

So lifts are crossed homomorphisms/cocycles in `Z^1(X;C3_h)`. If local full-pairing frames are changed by a kernel element `b_x in C3`, the cocycle changes by the twisted coboundary. Therefore

\[
\boxed{
\{S3\text{ lifts of }h\}/A3\text{-vertex gauge}
\cong H^1(X;C_{3,h}).
}
\]

This is both necessity and sufficiency: every lift produces such a class, and every twisted class reconstructs a flat lift.

### 4.3 Exact free-rank formula

For the accepted parent normal form, `pi1(X)` is free of rank `beta`. Use a bouquet presentation with generators `g_1,...,g_beta` and write `h_i=h(g_i)`.

The local-system cellular complex has

\[
C^0=C_3,
\qquad C^1=C_3^\beta,
\]

and

\[
\delta b=((1-(-1)^{h_i})b)_i.
\]

There are no 2-cells after homotopy reduction, so every 1-cochain is closed. Over `F3`, `1-(-1)=2` is invertible. Hence

- if `h=0`, `rank delta=0`;
- if `h!=0`, `rank delta=1`.

Thus

\[
d_2=\dim_{F3}H^1(X;C_{3,h})
=\begin{cases}
0,&\beta=0,\\
\beta,&h=0,\\
\beta-1,&h\ne0.
\end{cases}
\]

### 4.4 Full-gauge audit

The relative classification above fixes the marked L1 object. A global opposite-frame flip, representing the residual constant L1 gauge on connected `X`, conjugates `A3` by inversion. Therefore the full-gauge residual action on `H^1(X;C3_h)` is

\[
[a]\mapsto[-a].
\]

The zero class is fixed. Every nonzero class has a two-element orbit because `3` is odd. Thus

\[
N_{L2/L1}^{\rm full}=
\begin{cases}
1,&d_2=0,\\
1+(3^{d_2}-1)/2,&d_2>0.
\end{cases}
\]

This is the correct finite count; it is not a bit count.

### 4.5 Minimal same-L1/different-L2 witness

Take `X=S1` and trivial L1 holonomy `h=0`. Then

\[
H^1(S^1;C_3)=C_3.
\]

Two lifts are

\[
\rho_0(g)=1,
\qquad
\rho_1(g)=(012).
\]

Both have sign zero and hence the same L1 reduct. They are not related by A3 kernel gauge on one loop because `A3` is abelian and the action is trivial. Under the remaining C2 full gauge, `(012)` and `(021)` become equivalent, but neither becomes the zero class. Thus the same L1 reduct supports at least two inequivalent L2 classes: split and genuinely carrier-mixing.

This proves necessity of the C3 twisted class for any nontrivial L2 augmentation.

## 5. L2 -> L3: exact V4 twisted-lift theorem

### 5.1 Standard extension and section audit

Let `Phi:S4->S3` be the action of `S4` on the three perfect matchings of four atoms. The kernel is

\[
V_4=\{1,(01)(23),(02)(13),(03)(12)\}
\cong F_2^2.
\]

The extension splits. There are exactly four `S3` complements in `S4`, hence exactly four homomorphic sections. The parent checker established that `V4` conjugation acts transitively on them. The new audit strengthens the structural interpretation.

Choose one section `s`. For `w in V4`, define

\[
s^w(\sigma)=w\,s(\sigma)\,w^{-1}.
\]

Every section is of this form. Relative to `s`, the new section has kernel coordinate

\[
d_w(\sigma)
=w-\sigma\cdot w.
\]

This is exactly the group-cohomology coboundary of the zero-cochain `w` for the natural `S3` action on `V4`.

Therefore all four sections determine the same element in the unframed lift set. “Choose one of four sections” is presentation data, not four structural atom transports.

### 5.2 Necessity and sufficiency

Fix an L2 representation

\[
\rho:\pi_1(X)\to S_3.
\]

Relative to a temporary section, every `S4` lift is uniquely

\[
\widetilde\rho(\gamma)=v(\gamma)s(\rho(\gamma)),
\qquad v(\gamma)\in V_4.
\]

Multiplication gives

\[
v(\gamma\delta)
=v(\gamma)+\rho(\gamma)\cdot v(\delta).
\]

A vertex atom-frame change by `w_x in V4` changes `v` by the local twisted coboundary. Thus

\[
\boxed{
\{S4\text{ lifts of }\rho\}/V4\text{-vertex gauge}
\cong H^1(X;V_{4,\rho}).
}
\]

Again, every lift yields such a class and every class reconstructs a flat lift. This is exact necessity and sufficiency.

### 5.3 Exact free-rank dimension

View `V4` as the natural two-dimensional `F2` representation of

\[
S_3\cong GL(2,2).
\]

For the free rank-beta normal form, a cocycle may choose one arbitrary vector in `V4` on each free generator, so

\[
\dim Z^1=2\beta.
\]

Coboundaries are the image of

\[
\delta:V_4\to V_4^\beta,
\qquad
w\mapsto((1-\rho(g_i))w)_i.
\]

Its kernel is the common fixed subspace

\[
V_4^{\operatorname{im}\rho}.
\]

Writing

\[
f(\rho)=\dim V_4^{\operatorname{im}\rho},
\]

rank-nullity gives, for `beta>=1`,

\[
\dim B^1=2-f(\rho)
\]

and therefore

\[
\boxed{
d_3=2\beta-2+f(\rho).
}
\]

The image types give:

- trivial: `f=2`;
- a single transposition subgroup: `f=1`, because a transvection in `GL(2,2)` fixes one nonzero line;
- a 3-cycle subgroup, full `S3`, or any image containing two distinct transpositions: `f=0`.

### 5.4 One-loop calibration

For `X=S1`, beta=1:

1. `rho(g)=1`: `H^1(S1;V4)=V4`, dimension 2, four relative classes;
2. `rho(g)=tau` a transposition: dimension 1, two relative classes;
3. `rho(g)=c` a 3-cycle: `1-c` is invertible on `V4`, dimension 0, one relative class.

This explicitly shows why no uniform “two atom bits” law is correct. The lift freedom depends on the actual S3 holonomy action.

### 5.5 Minimal same-L2/different-L3 witness

Take `X=S1` with trivial L2 holonomy `rho(g)=1`. Then

\[
H^1(S^1;V_4)=V_4.
\]

The two S4 holonomies

\[
\widetilde\rho_0(g)=1,
\qquad
\widetilde\rho_1(g)=(01)(23)
\]

have the same S3 quotient. They are distinct relative kernel classes. Full constant S3 gauge is transitive on the three nonzero V4 vectors, so the unframed fibre still has two qualitative orbits, zero and nonzero. Hence the same L2 reduct does not determine a nontrivial L3 atom transport.

## 6. Gauge atlas: what is and is not structural

The exact classification is:

| Datum | Layer | Gauge / structural status |
|---|---|---|
| local ordering of the opposite pair | L1 presentation | vertex C2 frame / gauge |
| C2 holonomy class `[h]` | L1 | structural only after C2 primitive is added |
| marked-state stabilizer split `C2->S3` | L1->L2 | canonical typed split, no extra datum |
| local full pairing-state frame | L2 presentation | vertex S3 frame / gauge |
| C3 crossed cocycle representative `a` | L2 presentation | changes by twisted C3 coboundary |
| `[a] in H1(X;C3_h)` | L2 | genuine relative augmentation class |
| choice among three abstract sign splittings without mark | abstract group presentation | irrelevant; marked carrier state selects the typed stabilizer split |
| choice among four `S3->S4` sections | L3 presentation | V4 gauge/coboundary; **not structural** |
| local atom frame | L3 presentation | vertex S4 frame; relative V4 gauge when L2 fixed |
| V4 cocycle representative `v` | L3 presentation | changes by twisted V4 coboundary |
| `[v] in H1(X;V4_rho)` | L3 | genuine relative atom-kernel augmentation class |

This directly repairs the too-coarse phrase “a selected atom-frame/section is needed” from the parent boundary. A selected **representative** needs a frame and a section for coordinates, but the unframed split lift class is canonical and independent of which section is used.

## 7. Natural-compression and selector boundary

### 7.1 What is canonical

At both split extensions there is a distinguished **zero cohomology class** after the lower-level object is fixed:

- L1 -> L2: the marked-state stabilizer split gives `[a]=0`;
- L2 -> L3: any homomorphic section gives `[v]=0`, and the four section choices differ by coboundaries.

Thus the lower level always determines a canonical split-lift gauge class.

### 7.2 What is not forced

The lower level does **not** force any nonzero kernel-cohomology class.

When the relevant H1 group is nonzero, the same lower reduct admits zero and nonzero lifts. No equation in the frozen support/resonance interface distinguishes a nonzero class. Requiring “the augmentation must be nonzero” is already a new axiom.

In the L1 -> L2 case, the residual full C2 gauge sends `[a]` to `[-a]`. If `d2=1`, all nonzero vectors collapse to one full-gauge orbit, but the dichotomy zero versus nonzero remains and the lower reduct does not choose the nonzero orbit. For `d2>=2`, there are multiple nonzero full-gauge orbits.

In the L2 -> L3 trivial-holonomy one-loop witness, full S3 gauge is transitive on nonzero V4, yet again zero versus nonzero remains. For larger beta/other rho, the kernel-cohomology orbit structure can be richer.

Hence the exact no-go is not “there is no canonical lift”. The correct statement is

\[
\boxed{
\text{LOWER REDUCT DOES NOT NATURALLY SELECT A NONZERO KERNEL-COHOMOLOGY CLASS.}
}
\]

This is the minimum naturality boundary compatible with the split extensions.

### 7.3 No support-faithful bit compression

The L2 relative kernel is C3-valued and therefore cannot be represented faithfully by a fixed bit count at the object level. The L3 kernel is V4-valued but its twisted H1 dimension depends on `rho`. Any fixed “one atom bit per loop” law is false; the one-loop dimensions `2,1,0` already refute it.

## 8. Exact finite witnesses and required strata

The deterministic checker freezes the following cases.

### 8.1 H1 dimensions 0, 1, 2+

Using the accepted formula:

- `beta=0`: equality stratum `k=2`, no cycle freedom;
- `beta=1`: clean `k=3,m=0`, single-pinch `k=2,m=1`, equality `k=3`;
- `beta=2`: for example `k=3,m=1`;
- `beta=3`: multi-pinch `k=3,m=2`.

### 8.2 Clean backbone

`k=3,m=0` gives beta=1.

- L1 has two C2 classes.
- For h=0, L2 has d2=1; for h!=0, d2=0.
- L3 depends on rho by the one-loop 2/1/0 law.

### 8.3 Single pinch

`k=2,m=1` gives beta=1 with the new L1 bit produced by loss of one gauge degree, as accepted by the parent. The L2/L3 lift classification depends only on the resulting typed holonomy and therefore applies unchanged.

### 8.4 Multiple pinches

`k=3,m=2` gives beta=3.

- L2: d2=3 when h=0 and d2=2 when h!=0.
- L3: d3=6,5,4 according as the S3 image has fixed dimension f=2,1,0.

Thus pinch count affects lift freedom through beta but does not create a separate section datum.

### 8.5 Equality stratum

For `a=b`, the parent normalizes to `K_R`, with

\[
\beta=(k-1)(k-2)/2.
\]

There is no carrier-height class, but the C2->S3 and S3->S4 lift theorems remain valid because they depend only on the pairing/atom transport local systems over `X`. For `k=2`, beta=0 and all relative lift cohomology vanishes. For `k=3`, beta=1 and the one-loop calibration applies.

## 9. Four S4 sections: exact gauge collapse

The checker reconstructs `Phi:S4->S3` from the action on the three perfect matchings and verifies:

1. `ker Phi=V4`, order 4;
2. every S3 element has exactly four S4 lifts;
3. exactly four subgroups of S4 map isomorphically onto S3;
4. each yields a homomorphic section;
5. V4 conjugation acts freely and transitively on those four sections;
6. for every section obtained by w-conjugation, the coordinate difference from a base section is the twisted coboundary `w-rho(.)w`;
7. hence section choice does not survive the V4 gauge quotient.

This directly satisfies the task's “all four complements/sections” obligation while avoiding the kill-rule error of treating a complement choice as intrinsic atom data.

## 10. Deterministic checker and machine-readable atlas

Checker:

`research_checks/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT_CHECK_20260901.py`

Machine-readable atlas:

`research_artifacts/DECORATED_CARRIER_MINIMAL_AUGMENTATION_ATOM_TRANSPORT/augmentation_atlas_20260901.json`

Observed exact execution:

`PASS checks=8384; L1_to_L2=C3_twisted_H1; S3_sign_kernel=3; marked_split=canonical; L2_to_L3=V4_twisted_H1; S4_kernel=4; sections=4_all_V4_gauge; L3_one_loop_dims=id:2,transposition:1,3cycle:0; clean_single_multi_equality=PASS`

The checker uses only exact finite group tables, finite-field linear orbit enumeration, and the accepted parent beta formula. It checks:

- `A3` is the normal C3 kernel of `sgn:S3->C2`;
- the marked stabilizer is the typed split and conjugation acts by inversion;
- unique semidirect decomposition of every S3 element;
- all C3 twisted gauge quotients for beta through 5 and every C2 holonomy vector;
- residual inversion full-gauge orbit counts;
- the minimal same-L1/different-L2 witness;
- `Phi:S4->S3`, V4 kernel, all four sections, and their exact coboundary equivalence;
- the faithful S3 action on V4 as `GL(2,2)`;
- all V4 twisted gauge quotients for beta through 3 and every S3 generator tuple;
- the formula `d3=2 beta-2+f(rho)`;
- one-loop dimensions `2,1,0`;
- the minimal same-L2/different-L3 witness;
- clean, single-pinch, multi-pinch, and equality regressions.

The finite census is regression evidence. The classification follows symbolically from the two split extensions and the free-group/local-system cochain complexes.

## 11. Necessity/sufficiency atlas

### L0 -> L1

- necessity: accepted parent same-carrier/different-C2 classes and canonical-selection obstruction;
- sufficiency: explicit C2 torsor connection;
- gauge: vertex C2 frame;
- structural class: H1(X;F2).

### L1 -> L2

- necessity: same L1 sign quotient supports distinct C3 twisted H1 classes;
- sufficiency: canonical marked split plus any C3 twisted cocycle;
- gauge: vertex C3 kernel gauge plus inherited C2 frame action;
- structural class: H1(X;C3_h), modulo inherited automorphisms when full gauge is taken;
- section datum: none beyond the canonical marked-state stabilizer split.

### L2 -> L3

- necessity: same L2 quotient supports distinct V4 twisted H1 classes whenever d3>0;
- sufficiency: any temporary section plus a V4 twisted cocycle;
- gauge: vertex V4 atom-frame gauge; changing among the four sections is such a gauge change;
- structural class: H1(X;V4_rho);
- independent section datum: none.

## 12. Prior-art and novelty boundary

The group extensions

`1->C3->S3->C2->1`,

`1->V4->S4->S3->1`,

semidirect products, crossed homomorphisms, local-system H1, group cohomology, and `S3 ~= GL(2,2)` are standard mathematics. No historical novelty is claimed for them.

The project-local contribution of this Result is only the exact application to the **frozen typed decorated-carrier interface**:

- the marked carrier state canonically identifies the accepted C2 connection with the sign quotient of full S3 pairing transport;
- the missing genuine L2 augmentation is exactly the C3 twisted H1 class, not an arbitrary S3 section;
- all four S4 sections collapse under V4 gauge, so the genuine L3 augmentation is exactly the V4 twisted H1 class;
- the parent free-rank geometry yields closed formulas for both lift spaces;
- zero split lifts are canonical, but no nonzero augmentation class is supplied by the lower reduct.

No Working Truth, Foundation status, L4, canonical theorem promotion, or broad physical interpretation follows.

## 13. Boundary and disposition

Hard target disposition:

`MINIMAL_TRANSPORT_AUGMENTATION_HIERARCHY_CLASSIFIED = SATISFIED`.

Recommended Driver freeze strength:

`L0_TO_L1_EXOGENOUS_C2_H1 + L1_TO_L2_SIGN_KERNEL_C3_TWISTED_H1_WITH_D2_BETA_OR_BETA_MINUS_1 + L2_TO_L3_V4_TWISTED_H1_WITH_D3_2BETA_MINUS_2_PLUS_FIXED_DIM + ALL_S4_SECTIONS_GAUGE_EQUIVALENT + ZERO_SPLIT_LIFTS_CANONICAL_BUT_NO_NONZERO_CLASS_FORCED`.

Unresolved residue is intentionally narrow:

- an application may independently impose a nonzero C3 or V4 kernel class, a relation among classes, or another symmetry-breaking datum;
- such a condition is external new structure and is not derivable from the closed Seed-6 arithmetic reduct by this Result;
- the present task does not decide which future physical/application semantics, if any, should motivate such a constraint.

Recommended next control-plane action:

`DRIVER_REVIEW`. If accepted, close `OBJ-DECORATED-CARRIER-TRANSPORT-AUGMENTATION-MINIMALITY` at this atlas. Do not publish another task merely to “pick an S3/S4 section” or “choose an atom frame”: those have been classified as gauge/presentation. Reopen only if an independently motivated nonzero C3/V4 constraint or a new typed relation is supplied.
