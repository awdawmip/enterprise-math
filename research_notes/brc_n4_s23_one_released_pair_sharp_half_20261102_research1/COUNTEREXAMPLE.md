# Exact full-domain counterexample for the seven-witness-optimal three-free decoder bank

Date: 2026-11-02. Status: AUTHOR_ANALYTIC_COUNTEREXAMPLE / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Preceding sharp *seven-witness* theorem: `eca8150ec1426e5f9c4cddae0a773df2e9a81531`.

## Statement

For each h in {1,...,8}, consider the explicit ten-kernel bank consisting of the seven original fixed pair decoders D1..D8 except Dh, plus D9, D10 and Dstar as specified by PROOF.md. The bank reaches exact worst risk 1/2 on the previous seven legal witnesses W,J,A,B,C,X,Y. Nevertheless, on the full lawful eleven-parameter domain, this very bank has worst risk **exactly 1**, for every h.

## One lawful exact counterexample

In causal control order `(a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV)`, take

`Z=(0,1,0,1,0;1,1,0,0,0,0)`.

This is a legitimate 0/1 policy retaining the same shared `b_U=0`, same six source labels and original six preparing mixtures M20/20. The full six target stopping-time rows, each with four atoms (e1,...,e4), are:

`P(Z)=(e3,e3,e2,e1,e1,e1)`.

For each one of the ELEVEN listed candidate decoder kernels (D1..D8,D9,D10,Dstar), the following table gives a prepared row i and stopping atom a such that `P_i(Z)(a)=1` but `Q_i(D)(a)=0`:

| Decoder | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | Dstar |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Prepared row i (1-based) | 4 | 4 | 4 | 1 | 1 | 1 | 3 | 1 | 1 | 1 | 3 |
| Atom a (1-based) | 1 | 1 | 1 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 2 |

Because each target row is a point mass at that atom, the disjoint event forces `TV(P_i(Z),Q_i(D))=1`; probability normalization bounds all TV distances by 1. Therefore **every** listed decoder has full six-preparation risk `L_D(Z)=1`. Removing any one Dh leaves ten decoders with `G(Z)=min_j L_D(Z)=1`. Since risks lie in [0,1], the full-domain worst risk of each of the eight listed banks is exactly 1.

This is an exact positive result identifying a new adversarial policy and a repair requirement for this particular rational bank; it changes none of the previous seven-witness minimax quantifiers. In particular, it does not establish an impossibility for other banks or change the full ten-label `[1/2,2/3]` minimax bracket.

## Verification, scope, recovery

`VERIFY_COUNTEREXAMPLE.js` extends the exact predecessor checker by computing P(Z) through the original joint six-source M20 and causal law, expanding each of the eleven actual candidate kernels via the same common four group rows and M20, and checking all eleven disjoint-event identities, full exact TV losses and eight ten-decoder sub-banks. The executed output is `RUN_COUNTEREXAMPLE.json`. BigInt rational arithmetic is exact, with no floating-point threshold.

The exhaustive search through all `3^11=177147` ternary policies (0,1/2,1 per control) was also performed in the author workspace with integer numerator arithmetic; each of the eight bank variants reached maximum loss 1. This search has finite ternary scope. The single 0/1 policy Z and the explicit table above independently prove the stronger fact needed here (full-domain worst risk 1), because Z itself belongs to the full continuous domain.

Next optimize the third free kernel or other fixed kernels against Z and the seven former witnesses, rather than certifying a full-continuum upper bound for a bank already refuted at Z.
