# Uniform Semantic Shortcut Language versus Target-Specific Cache

Status: `RESEARCH BRIDGE / NONCANONICAL`

Researcher-ID: `R-8F3K`

The bounded-support shortcut table has a large binomial size because it buys a **uniform future-language guarantee**, not because one fixed target intrinsically needs that many effects.

## 1. Uniform one-round requirement

Fix k primitive directions and shortcut depth d.

Require:

> every nonzero semantic effect T with support size at most d must be executable from identity in one shortcut application.

One application from identity returns exactly the chosen primitive shortcut mask. Therefore every such T must itself appear in the primitive catalogue.

Hence the minimum possible catalogue size is exactly

`sum_(i=1)^d C(k,i)`.

So the canonical bounded-support shortcut family is **globally minimum for this uniform one-round requirement**.

## 2. Target-specific requirement is much cheaper

Now declare only one target effect T.

Partition its support into chunks of size at most d and store only those chunk masks.

Catalogue size and execution distance are both

`ceil(|T|/d)`.

This reaches T exactly but gives no one-round guarantee for unrelated semantic effects.

## 3. Sharp k=20,d=3 gap

For the full 20-bit target:

- uniform one-round language storage through support3: `1350` primitive effects;
- target-specific full-mask cache: `ceil(20/3)=7` primitive effects.

Both are exact relative to their declared tasks.

The 1350-entry table is not overprecision for the uniform language; the 7-entry table is not sufficient for that language.

## 4. Quantifier placement changes resource minimality

Compare:

`for every target T with |T|<=d, execute T in one round`

versus

`for this fixed target T, execute it using d-bounded shortcuts`.

The first quantifies over an entire future-effect language and forces all local effects into storage. The second permits a target-adapted basis.

Thus cache minimality is future-language relative in the same way that fixed-target and all-target reflection/certification were earlier separated.

## 5. Routing consequence

Before optimizing shortcut/cache storage, declare whether the representation must support:

- one fixed target;
- one target region;
- all targets up to a complexity bound;
- the complete semantic operation language.

A storage lower bound from one quantifier pattern must not be transferred to another.

## Owner-local assets

- `src/enterprise_math/semantic_shortcut_uniform_target.py`;
- `tests/test_semantic_shortcut_uniform_target.py`;
- this bilingual note.

## Prior art / status

Set systems, support masks and target-specific versus uniform data structures are standard prior mathematics/CS. This note owns only the Enterprise Math future-language quantifier interpretation.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. `CI_NOT_REQUIRED_FOR_RESEARCH`. Hard block: `NONE`.
