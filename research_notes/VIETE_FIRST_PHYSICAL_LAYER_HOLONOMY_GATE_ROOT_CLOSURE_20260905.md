# Viète first physical layer closure: ordered-neighbor holonomy and Cell-gate principal root

Status: `FREE_RESEARCH / EXACT RESTRICTED FIRST-LAYER CLOSURE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent: `#1158`
Depends on:
- merged `#1170` Cell-radius Euler bisector package;
- open `#1169` Cell-gate phase refinement;
- `research_notes/VIETE_PIVOT_LOCAL_TRANSLATION_QUOTIENT_C12_20260905.md`;
- accepted finite `C3/C2` holonomy benchmark from PR `#908`.

## 1. Revision of the earlier native frontier

Earlier #1158 work isolated two missing clauses inside a cycle-cover architecture:

1. an effective nontrivial `C2` holonomy selecting connected `C3 -> C6`;
2. a forward/shortest root section selecting the Viète root inside a connected binary cover.

Those no-go results remain correct **if the input is only the already-compressed `C3` ray-label state plus unspecified local fiber data**.

The merged Cell/gate work now provides a richer local source before that compression: ordered nearest-neighbor Cell germs and actual triple gates. At this richer source, both clauses are realized at the first physical layers.

## 2. Ordered-neighbor C6 realizes the nontrivial C3/C2 transport class

Let the six oriented nearest-neighbor classes around a pivot be

\[
C_6=\{[k]_6:k=0,\ldots,5\}
\]

with positive successor

\[
R[k]=[k+1].
\]

The exact Chinese-remainder coordinate is

\[
\Psi:C_6\to C_3\times C_2,
\qquad
\Psi(k)=(2k\bmod3,\;k\bmod2).
\]

It is a bijection. In these coordinates,

\[
\boxed{
R(a,\eta)=(a+2,\eta\oplus1).
}
\]

After three fine direction steps,

\[
R^3(a,\eta)=(a,\eta\oplus1).
\]

Hence one full circuit of the coarse three-ray label flips the endpoint-orientation sheet:

\[
\boxed{H=1.}
\]

This is exactly the nontrivial gauge class of the accepted `C3/C2` transport classifier.

The sheet bit here is **ordered endpoint orientation parity**, not sweep chirality and not a primitive native negative axis.

## 3. Effectivity is no longer an external contract at this restricted layer

The accepted bare-slice theorem warns that an abstract `H=1` transport packet does not by itself prove existence of a global object; an effectivity contract is separate data.

Here the six states are already constructed as actual common-translation orbits of ordered nearest-neighbor Cell germs, and the successor is a well-defined permutation of those orbits.

Therefore the nontrivial class is realized, not merely proposed:

\[
\boxed{
H=1\text{ IS EFFECTIVE ON THE PIVOT-LOCAL ORDERED-NEIGHBOR QUOTIENT.}
}
\]

Equivalently, at this restricted interface the abstract requirement `1 in E_rot` has a concrete witness: the existing connected six-state successor shell itself.

This does not promote an effectivity law for arbitrary native covers.

## 4. Endpoint parity is distinct from sweep chirality

Let reflection/sweep reversal act on the cyclic direction label by

\[
S(k)=-k\pmod6.
\]

Then

\[
SRS=R^{-1}.
\]

The endpoint half-turn is

\[
H=R^3:k\mapsto k+3.
\]

Since `-k` has the same parity as `k`, `S` preserves the endpoint parity coordinate, while `H` flips it. Thus

\[
\boxed{H\ne S}
\]

as operations, although special quarter-turn states can make their actions coincide on isolated points.

Moreover `H` is central and commutes with `S`, giving the expected local `V4=<H,S>` sign structure at the character layer.

## 5. Actual gates realize the first binary phase residual

The six pivot-incident triple gates interleave the six ordered-neighbor classes:

\[
E_0,G_0,E_1,G_1,\ldots,E_5,G_5.
\]

Therefore the typed phase successor `Q` is a genuine `C12` cycle with

\[
Q(E_k)=G_k,
\qquad
Q(G_k)=E_{k+1},
\qquad
Q^2|_{E}=R.
\]

In residue coordinates every phase is uniquely

\[
j=2k+\varepsilon,
\qquad \varepsilon\in\{0,1\},
\]

where `epsilon=0` is an ordered-neighbor Cell-direction state and `epsilon=1` is its outgoing pivot-gate transition phase.

The first residual bit is therefore physically supplied by existing Cell/gate incidence.

## 6. Directed incidence selects the forward root

The square-root fiber of one coarse direction step contains two opposite roots. The unoriented `C12` incidence cycle alone cannot choose between them; reflection exchanges the two choices.

Once a sweep chirality / directed cyclic order is given, however, each ordered-neighbor state has a unique outgoing physical gate `G_k` before the next ordered-neighbor state `E_{k+1}`.

Hence the first directed refinement is not an arbitrary near-root convention:

\[
\boxed{
\text{FORWARD PHYSICAL GATE INCIDENCE SELECTS THE FIRST ROOT.}
}
\]

Reversing sweep selects the inverse root tower.

## 7. Cell radius identifies the same root with the normalized bisector

In the merged #1170 character representation let `G` be the six-direction rotor and let the current Cell radius satisfy

\[
r^2=1/3,
\qquad r>0.
\]

The adjacent-state sum has norm dilation exactly three. Therefore the unique positive scalar normalizing it is

\[
r=1/\sqrt3.
\]

The physical gate rotor

\[
K=r(I+G)
\]

satisfies

\[
\boxed{K^2=G},
\qquad
K^{12}=I.
\]

Thus the same first root is characterized in two independent finite ways:

1. combinatorially: the unique outgoing physical triple gate on the chosen directed incidence cycle;
2. algebraically: the unique positive normalized adjacent-state bisector.

This closes the former shortest-root/positive-longitudinal ambiguity at the first Cell-gate layer.

## 8. BRC observer audit

Population: translated pivot-local ordered-neighbor germs plus their pivot triple-gate events.

Retained observer:

\[
(\text{direction class }k,\text{ Cell/gate residual }\varepsilon,\text{ sweep chirality}).
\]

Future operations: directed successor/predecessor, coarse two-step successor, reversal, gate incidence, and first normalized-bisector character readout.

The common-translation quotient is safe for those operations because they are translation-equivariant. Erasing endpoint parity destroys the `C3 -> C6` holonomy; erasing Cell/gate parity destroys the one-step `C12` successor; erasing sweep chirality destroys root-sign selection.

Thus the three binary notions are typed separately:

- endpoint/deck parity;
- Cell/gate phase residual;
- sweep chirality.

Weighted positive-branch statistics are not used because this local dynamics is deterministic.

## 9. Updated #1158 frontier

At restricted pivot-local carrier/character strength, the first physical chain is now closed:

\[
\boxed{
C_3
\xleftarrow{\text{forget endpoint orientation}}
C_6
\xrightarrow{\text{actual triple gates}}
C_{12}.
}
\]

More explicitly:

- `C3 -> C6` nontrivial holonomy is realized by ordered endpoint parity;
- its effectivity is witnessed by the actual six-state quotient;
- `C6 -> C12` is realized by actual pivot triple gates;
- directed sweep selects the forward gate/root;
- Cell radius is the unique positive normalized-bisector scale.

Therefore the old two-clause native gap has moved strictly upward. It no longer blocks the first physical Cell/gate layer.

The remaining hard frontier is:

\[
\boxed{
C_{12}\to C_{24}\to C_{48}\to\cdots
}
\]

where the newly inserted states are currently transition/history tokens rather than independently realized one-step Cell/gate objects.

## 10. Boundary

This theorem does **not** prove that every fixed-radius native rotating single-Cell trajectory factors through the pivot-local phase quotient. It does not identify carrier direction with native directed line gauge, and it does not identify endpoint reversal with equality of canonical reverse trace and groupoid inverse.

The exact remaining question is now sharper:

> Can the canonical higher transition/history refinement required beyond `C12` be justified as a native process-state precision extension compatible with the one-Cell rotation law, or must a new physical carrier be found?

That is the smallest unresolved native unit for the cycle-cover route.
