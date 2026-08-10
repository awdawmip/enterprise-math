# Integer Observation Exact Sequence and Precision Profile

Status: `RESEARCH BRIDGE / NONCANONICAL`

For an integer future-observation map

`O : Z^n -> Z^m`

of rational rank `r`, Smith normal form gives nonzero invariant factors

`d_1 | d_2 | ... | d_r`.

The standard exact sequences imply

`ker O ~= Z^(n-r)`,

and

`coker O ~= Z^(m-r) direct_sum Z/d_1 direct_sum ... direct_sum Z/d_r`.

This decomposition contains three mathematically different pieces.  Only two of
them are direct predictive-precision coordinates.

## 1. State hidden directions

`n-r`

is the rank of the state fiber invisible to the declared linear future language.
It is the free kernel / unresolved-state dimension.

When this reaches zero, integer states are uniquely distinguishable by the full
future observation vector.

## 2. Integer coordinate torsion

The nonunit Smith factors `d_i>1` describe the non-unimodular embedding of the
observable state lattice in the declared integer observation coordinates.

Even with hidden rank zero, nonunit factors can remain.  The state is then unique
but integer-linear recovery from the observation coordinates still carries
congruence/denominator structure.

A full-rank observation map has an integer linear left decoder exactly when all
nonzero Smith factors are one.

This is the coordinate-purification axis developed in the A2/P023 integer future
observability bridge.

## 3. Free cokernel rank is observation-interface excess, not state precision

The free cokernel rank

`m-r`

belongs to the declared observation codomain, not to unresolved state.

Appending a duplicate or integer-linearly dependent future observation can
increase the raw number of observation coordinates `m` and therefore increase
`m-r`, while leaving

- the state kernel unchanged;
- all nonzero Smith factors unchanged;
- the future-equivalence partition unchanged;
- integer coordinate quality unchanged.

Therefore neither

`number of future words`,

nor

`length of the raw future-signature vector`,

nor the free cokernel rank by itself should be called predictive precision.

They can contain arbitrary redundant interface coordinates.

## 4. Compact integer linear precision profile

For a declared linear future language, a robust algebraic precision profile is

`(hidden_free_rank ; nonzero Smith factors)`

that is,

`(n-r ; d_1,...,d_r)`.

Interpretation:

- decreasing `n-r` removes genuinely hidden state directions;
- after `n-r=0`, future refinement can continue by driving nonunit Smith factors
  toward one;
- adding redundant observation rows can leave this profile unchanged.

The profile is invariant under unimodular changes of state and observation
integer coordinates.

## 5. Future row refinement

When a future language is extended by **adding rows** to the observation matrix:

- rank cannot decrease;
- the state kernel cannot grow;
- every already-nonzero determinantal divisor can only decrease by divisibility;
- after full rank, additional rows may still remove Smith torsion without changing
  state distinguishability.

Thus integer-linear precision refinement has two stages inside one Smith profile:

```text
kernel-removal stage
    zero higher determinantal divisors become nonzero

coordinate-purification stage
    existing nonzero determinantal divisors shrink by divisibility toward 1
```

Redundant rows may change neither stage.

## 6. Relation to the wider diagnostic

This exact sequence refines the Foundation-facing five-location diagnostic:

- FIBER corresponds here to `ker O`;
- IMAGE/COKERNEL coordinate obstruction is the torsion part of `coker O`;
- raw observation-interface excess is the free part of `coker O` and should not be
  mistaken for either hidden state or additional predictive precision.

DOMAIN, RELATION, and LEDGER layers may be compiled into such an integer linear
observation map only when their declared semantics genuinely factor through a
linear state.  The exact sequence is therefore a specialization, not a universal
replacement for P023 future signatures.

Smith normal form and finitely generated abelian-group exact sequences are
standard prior mathematics.  The project value is the precision interpretation
and the explicit warning against using signature length as a precision measure.
