# Same Execution Monoid, Different Minimum Capability Design

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The design/execution separation can be sharpened beyond NP-hardness: even the **complete generated semantic operation monoid**, together with the number of named generators and the exact composition law, does not determine the minimum precision-preserving generator count.

## 1. Two catalogues with identical execution semantics

Fix universe size `m>=2`.

Both catalogues contain all m singleton actions `{0},...,{m-1}` and one extra named action, so both have exactly `m+1` generators.

### Catalogue A — duplicate singleton

Extra action duplicates `{0}`.

### Catalogue B — full action

Extra action is the full universe `{0,...,m-1}`.

Because both catalogues already contain every singleton, arbitrary unions generate **every** universe subset.

Thus both generated semantic effect monoids are exactly

`2^[m]`

under bitwise OR, with `2^m` effects.

They have the same monoid carrier, same OR multiplication law, same identity and same named-generator count.

## 2. Minimum preserving basis sizes differ maximally

The semantic target is full-universe coverage, equivalently full precision preservation in the parent Set-Cover action compiler.

In Catalogue A, the duplicate contributes no missing direction. Every universe element needs its singleton representative, so the minimum preserving subset has size

`m`.

In Catalogue B, the full-universe action alone preserves the target precision, so the minimum size is

`1`.

Hence the minimum-basis gap is

`m-1`.

The executable report verifies this for a growing bounded family of universe sizes.

## 3. What the monoid forgets

The generated operation monoid records **which exact effects can eventually be produced and how effects compose**.

Minimum design additionally depends on the presented generator catalogue: which named primitive actions are available as atomic selectable resources.

Two catalogues can generate the same closure of effects while placing very different primitive generators inside that closure.

Therefore basis design is a property of

`(semantic target, generator presentation, cost model)`,

not of the abstract generated monoid alone.

## 4. Same action count is not enough either

The witness keeps named action count fixed at `m+1` on both sides.

So adding generator-count metadata to the abstract monoid still does not recover minimum basis size.

One must know the actual generator placement / presentation.

## 5. Stage131 consequence

The same semantic operation algebra can have different upstream design costs before runtime representation optimization even begins.

Thus at least three objects must remain distinct:

1. **generated semantic algebra** — all exact effects and their composition;
2. **generator presentation/catalogue** — atomic capabilities available to select;
3. **execution representation** — tables, caches, formulas or circuits used after selection.

Collapsing these into one “law complexity” loses essential resource information.

## 6. Relation to classical generating-set questions

This witness does not claim a novel general theorem about minimum generating sets of monoids. The preserving target is a project-specific semantic requirement inherited from the Set-Cover precision compiler, not merely “generate the whole monoid”.

The result is narrower and more relevant here: **even identical exact execution monoids do not determine minimum subsets satisfying a declared precision target.**

## Owner-local assets

- `src/enterprise_math/same_monoid_design_gap.py`;
- `tests/test_same_monoid_design_gap.py`;
- this bilingual note.

## Prior art / status

Semilattice generation and Set Cover are standard prior mathematics/CS. This note owns only the Enterprise Math same-monoid design-separation pressure test.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
