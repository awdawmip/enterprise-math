# HODGE H0A0 — GAGA boundary matrix

Date: `2026-08-17`  
Researcher-ID: `EM-HODGE-H0-2F8C71`  
Task: `RS-HODGE-H0A0-REALIZATION-COMPARISON-CRITERION-REPAIR`  
Status: `FROZEN / PRIMARY-SOURCE-BOUNDARY-AUDIT`

## Primary source

Jean-Pierre Serre, **“Géométrie algébrique et géométrie analytique”**, *Annales de l'Institut Fourier* 6 (1956), 1–42, DOI `10.5802/aif.59`.

Primary archive:
- Centre Mersenne / Annales de l'Institut Fourier: `https://aif.centre-mersenne.org/articles/10.5802/aif.59/`
- Digitized article PDF: `https://aif.centre-mersenne.org/item/10.5802/aif.59.pdf`

Current Hodge-status checker:
- Clay Mathematics Institute, Hodge Conjecture: `https://www.claymath.org/millennium/hodge-conjecture/`

## Exact projective-complex boundary

| Item | Exact scope used by H0A0 | Source location | H0A0 consequence |
|---|---|---|---|
| Canonical analytification | A complex algebraic variety has an associated analytic space; H0A0 uses the full analytic locally ringed-space meaning only when declared as `C_full^an(X)`. | Serre, Introduction and §2 | Analytification is not a mere point-set readout. |
| Algebraic coherent sheaf → analytic coherent sheaf | Analytification is exact on algebraic sheaves in Serre's setup; an algebraic coherent sheaf gives an analytic coherent sheaf. | Serre §9, Proposition 10 | Coherent-sheaf structure can be compared without pretending it is singular/Hodge cohomology. |
| Coherent cohomology comparison | For projective complex `X`, and coherent algebraic `F`, the canonical map `H^q(X,F) -> H^q(X^an,F^an)` is bijective for every `q >= 0`. | Serre §12, Theorem 1 | Full recoverability in this language is compatible with different algebraic/analytic proof forms. |
| Full faithfulness on coherent sheaf morphisms | For coherent algebraic sheaves `F,G` on projective `X`, every analytic morphism `F^an -> G^an` comes from a unique algebraic morphism. | Serre §12, Theorem 2 | Analytic morphism data in the coherent category is not automatically extra information. |
| Algebraization of coherent analytic sheaves | Every coherent analytic sheaf on `X^an` for projective `X` is analytification of a coherent algebraic sheaf, unique up to isomorphism. | Serre §12, Theorem 3 | In the declared coherent-sheaf language, the projective algebraic and analytic categories are essentially equivalent. |
| Projectivity limitation | Serre explicitly notes that the three §12 theorems depend on projectivity and are false even for an affine variety in general. | Serre §12, Remark 1 | H0A0 does not promote GAGA to an unrestricted all-varieties equivalence. |
| Chow algebraization | Every closed analytic subset of projective space is algebraic; Serre derives this from Theorem 3. He also records that a compact analytic subset of an algebraic variety is algebraic. | Serre §19, Propositions 13–14 | If an appropriate analytic subvariety already exists, algebraization is available; existence is a separate question. |
| Holomorphic map algebraization | A holomorphic map from a compact algebraic variety `X` to an algebraic variety `Y` is regular. | Serre §19, Proposition 15 | In the projective/compact source setting, analytic presentation changes cannot be treated as automatically beyond algebraic control. |

## What this does **not** prove

`GAGA_DOES_NOT_SOLVE_RATIONAL_HODGE_CONJECTURE = true`.

The following inferences are rejected:

1. `rational Hodge class -> analytic subvariety` is **not** supplied by GAGA.
2. `H^{2p}(X,Q) ∩ H^{p,p}(X) -> algebraic cycle` is **not** a GAGA theorem.
3. Algebraization of an already existing coherent analytic sheaf or analytic subvariety does not create the subvariety/cycle required to represent an arbitrary rational Hodge class.
4. Coherent-sheaf cohomology comparison is not identical to saying that every singular/rational cohomology class has an analytic-subvariety representative.
5. Full recoverability in a declared algebraic/analytic comparison language does not imply equality of proof form, proof locality, normal form, obstruction basis, or operational complexity.

Clay Mathematics Institute continues to state the Hodge conjecture as an open Millennium problem and describes Hodge cycles as conjecturally rational linear combinations of algebraic cycles. That current status is a direct guard against misusing GAGA as a Hodge shortcut.

## Criterion consequence

The valid boundary is narrower than “analytic and algebraic geometry are identical”:

> For projective complex varieties, Serre's GAGA gives a strong algebraic/analytic equivalence on declared categories such as coherent sheaves, their morphisms and coherent cohomology, and strong algebraization consequences for analytic subvarieties/maps under the stated hypotheses. Therefore “an Enterprise realization must contain theorem-relevant information unrecoverable from a full analytification” is not an appropriate universal *necessary* qualification rule.

This statement concerns the **qualification criterion only**. It does not assert the existence of any Enterprise Hodge realization, Hodge class lifting, or algebraic cycle.
