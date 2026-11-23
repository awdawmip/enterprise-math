# X6 R142 — unique global lower first contact and exact local two-facet entry cusp

Date: 2026-11-23 (Asia/Shanghai). Status: **author exact integer/rational certificate PASS; independent mathematical review pending**.

## Frozen observer and source

Continue exact R141 after R140. Original immutable scientific inputs: R121 at 8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122 at 0687aa24f5402da3b35f914dd6907967a9805b94 in awdawmip/enterprise-math, with the original paths stated in R140/R141. R140 proof at f9b7ce6ac8523c515c350064c90f0baf5cd032b5 and R141 at 32d116d425dcc7fe23563aafa7a1eb9278a47428 under research_notes/portable_direct. P000 V5 and the ACTIVE Heartbeat X6 worldview, full six gap observations and integer Port 10 remain unchanged.

Recall w=(136,B,176,D) with B,D>0, heights h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z), gap vector g of all six i<j differences, capacities s=(136+B,312,136+D,B+176,B+D,176+D), q(a)=max(sum positive coordinates,sum absolute negative coordinates), F=max(g/s), eta=min F over all 1,935 integer directions modulo ±, strict near means 2F<3eta. The R138–R141 four-direction core is C={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}/±.

## Theorem A: the global first lower-boundary equality is unique

For **all real B>0 at D=448**, the complete near set is C (R141). Among the 1,931 outsider directions, exactly one equality with the strict threshold is possible:
- B=20,
- a=(6,-1,0) modulo ±,
- 2F_448(a)=3eta_448(20).

For all other B>0 and directions a outside C the inequality is strict: 2F_448(a)>3eta_448(B). For the four insiders it remains 2F_448(a)<3eta_448(B).

Proof: R141's complete nonnegative polynomial certificate gives, for each outsider and each of eight rational B cells, a fixed gap pair j with polynomial

P(B)=2g_j(a)(L0+L1 B)(448+m(B))-3K s_j(B,500)(500+m(B)) >=0, m(B)=min(B,136),

where eta_500(B)=K/(L0+L1 B) on that cell. Equality of the *actual* score ratio at D=448 forces equality in this selected polynomial. For B<=136 this is degree at most two; above 136 affine. A polynomial nonnegative on a closed interval may vanish only at an endpoint, an exact interior vertex of an upward parabola, or identically; on the final unbounded ray use the same endpoint/vertex criterion. All 8 x 1,931 = 15,448 selected polynomials were inspected: none are identically zero; the only positive B at which any can vanish is **B=20**. This leaves 64 direction/pair candidate zeros at B=20; an exact full-population evaluation of 2F=3eta at (B,D)=(20,448) finds only (6,-1,0). The four insiders retain R141's stronger 125/88 ratio bound. This proves global uniqueness without interpolation from samples.

## Theorem B: exact local two-facet entry region

For every real pair in the **closed rectangle**

19 <= B <= 21, 447 <= D <= 449,

the exact Port-10 optimum and full near set are

eta(B,D)=6/(B+D),

N(B,D)= C union {(6,-1,0)} if D<min(408+2B,468-B),

N(B,D)= C otherwise (including equality on either line).

The entry region therefore has a sharp two-facet roof meeting at (B,D)=(20,448), with left slope +2 and right slope -1 when plotted as D against B. It is locally a cusp-like V-shaped upper boundary for an entering direction, and the global lower uniform first contact is its apex.

Proof: every score comparison with eta=6/(B+D) becomes affine after multiplication by positive denominators. The four vertices (19,447),(19,449),(21,447),(21,449) suffice to certify:
- all 1,935 Port-10 integer directions have F>=6/(B+D), each using one fixed observation pair throughout the rectangle;
- the witness (1,0,0) has F<=6/(B+D) and its B+D gap is identically tight, establishing the exact optimum;
- all six gap comparisons of each of four C directions are strictly less than 3eta/2, establishing four persistent insiders;
- each of the remaining 1,930 outsider directions, except b=(6,-1,0), has at least one fixed observation pair satisfying F>=3eta/2 across the rectangle.

For b=(6,-1,0), its six integer gaps are (3,6,3,3,0,3); throughout the rectangle all other pair scores are at most 1/52 and the two active ratios give

F(b)=max(3/(136+B),1/52).

The strict criterion F(b)<9/(B+D) becomes D<408+2B when B<=20, and D<468-B when B>=20. Equality is excluded by the strict 3/2 condition. All comparisons are exact affine inequalities over the continuous rectangle, not inferences from numerical samples.

## Reproducibility and continuation

Companion executable: research_notes/portable_direct/x6_r142_first_contact_cusp_verify.py, using standard-library Fraction and importing only the already published R140/R141 certificate helpers. An independent local execution of the same checker logic returned:

    R142 UNIQUE FIRST CONTACT AND AFFINE LOCAL CUSP EXACT CERTIFICATE PASS
    optimizer_lower 1935 permanent_insiders 4 permanent_outsiders 1930
    global_boundary_outsider_polynomials 15448 possible_equal_B [Fraction(20, 1)]
    actual_equality_B20_D448 [(6, -1, 0)] raw_zero_candidates 64
    full_fraction_replays 45 local_box 19<=B<=21, 447<=D<=449
    new_entrant (6, -1, 0) iff D<min(408+2B,468-B)

The finite certificate and vertex proof cover their stated infinite real parameter domains. These are author results, not independently reviewed/admitted shared Results or a statement about native X6 physical time dynamics.

Next: extend this lower contact cusp beyond the local rectangle and find the entire first outsider-entry wall; independently analyze the upper near-loss limit B->0,D=528, including strict equality on positive-B slices and possible replacement directions.
