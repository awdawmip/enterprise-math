# Precision Type Is Not Precision Placement

Status: `RESEARCH BRIDGE / NONCANONICAL`

Smith/determinantal data provides a powerful integer precision **type**, but it does not by itself determine where unresolved directions lie in a fixed world coordinate system.

For example, on `Z^2` compare

`O_1=(2,0)`

and

`O_2=(0,2)`.

Both have exactly the same abstract integer profile:

- rational rank `1`;
- hidden free rank `1`;
- Smith factor `(2)`;
- maximal determinantal divisor `2`.

Yet their hidden state directions are different:

- `O_1` sees the first coordinate and hides the second;
- `O_2` sees the second coordinate and hides the first.

Thus

`(hidden rank ; Smith factors)`

classifies the observation map only up to suitable unimodular changes of state/observation coordinates.  It is not a replacement for the actual row lattice / kernel embedding when world-coordinate identity matters.

## Why the horizon plateau criterion is still exact

Future observation lattices form a nested chain

`L_h subseteq L_(h+1)`.

If adjacent horizons have equal rational rank, their rational spans are the same.  Inside that fixed rational span, if the nested lattices also have the same saturation index, they have equal finite index in the same saturated lattice; therefore

`L_h=L_(h+1)`.

That equality makes `L_h` action-invariant, so no later future word can enlarge it.

Hence along one declared future-language refinement chain:

`same adjacent rank + same adjacent saturation index`

is an exact permanent-stop certificate.

The same numerical pair is **not** a valid equality test for arbitrary non-nested observation maps.

## Architecture rule

Keep two levels distinct:

1. **precision type / abstract arithmetic complexity** — hidden rank, Smith factors, determinantal divisors;
2. **precision placement / semantic embedding** — the actual kernel, row lattice, named state coordinates, and future operations that act on them.

The first is useful for comparison, bounds, and topology/arithmetic phase summaries.  The second is required to run the world or decide which concrete state distinctions may be collapsed.

Smith normal form and lattice index arguments are standard prior mathematics.  The project value is the explicit guard against replacing semantic state placement with an abstract invariant tuple.
