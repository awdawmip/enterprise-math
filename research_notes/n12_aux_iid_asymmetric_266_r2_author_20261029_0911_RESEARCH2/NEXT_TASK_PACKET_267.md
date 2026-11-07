# Stage267 scientific continuation — beyond R266's J5–J6 edge

Date: 2026-10-29. Source: Stage266 AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED, under external ternary IID N=12, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), with arbitrary ordered-history randomized policies. Errors are (eP,eQ); objective min max(tP,tQ) at caps (a,b). No P000/native X6 theorem or formal native Source Result is implied.

## Immutable scientific frontier

Stage266's exact support is
lambdaP=12729920/136697,
lambdaQ=7907076/136697,
thetaP=0, thetaQ=1,
H=11494057433/199304226.

Its exact old target optimum is 282137639660138177/49593269164032000. The complete real equality region is R266=conv(I5,J5,J6,I6), exact area 45888275146484375/808683748406889283584, adjacent to Stage265 along I5–I6. Do not redo this completed unit: proof, code, and executed stdout are in the same research_notes Stage266 directory of Draft PR #1571.

The NEW unsolved frontier is the opposite J5–J6 edge. Its rational cap vertices are:

J5=(555154589/7739670528,3425906045/4353564672),
J6=(1253006053/15479341056,4425329935/5804752896).

## Guaranteed-feasible rational target strictly OUTSIDE R266

Choose the Stage267 caps

a267=3776724593681/49533891379200,
b267=1799211749497/2321901158400.

They are outside R266 on the J5–J6 side because the exact orientation of (J5,J6,(a267,b267)) is

-47704025643875/11501279977342425366528,

while the old-side vertex I5 has positive orientation
20858306884765625/404341874203444641792.

An exact full-history feasibility witness is a random mixture of three ACTUAL deterministic policies, with J5 and J6 each weighted 49/100 and a third policy K weighted 1/50. Policy K starts from the Stage266 J5 minimizing policy with tie bits (0,1); only the action at count state (1,2,0) changes from stop-Q to continue. All other actions remain exactly as in J5. Its precise observer tuple (eP,eQ,tP,tQ), computed by the same exact count/ordered-source laws, is

K =
(71046311473/990677827584,
 109630907431/139314069504,
 1722912951593/371504185344,
 63545971253/11609505792).

The mixture's four observers are

(3776724593681/49533891379200,
 1799211749497/2321901158400,
 3355004206763/687970713600,
 3336652788737/580475289600).

It obeys both caps exactly, and tQ>tP. Hence

V12(a267,b267) <= 3336652788737/580475289600,

an exact rational FEASIBLE UPPER BOUND, not yet an optimum. At the same witness the old Stage266 support slack is strictly positive:

lambdaP*a267+lambdaQ*b267+tQ(witness)-H
=2449655187043/317396922649804800 > 0.

The point is therefore a well-posed adjacent-face research target with a certified feasible strategy instead of an unverified numerical candidate.

## One precise next question

Compute the exact V12(a267,b267). Recover a new exact rational Bellman support, allowing a different pair of time weights if justified. Identify every tie and strict action gap over the 455 count states and 1274 legal actions. Construct a matching cap-saturating rational primal mixture, and prove the exact two-dimensional equality region (if it is full dimensional) over ALL real caps, its exact boundary and adjacency to J5–J6. Preserve full ordered paths and independent positive P/Q likelihood masses as BRC-style provenance; compare to the existing Stage266 proof without weakening its quantifiers.

Acceptance evidence: an actually executed exact certificate with all state/action checks, no negative gaps, dual root; rational primal with both error constraints and time max checked; independent DFS over ordered histories with two exact terminal normalizations; cap polygon vertices/area and full-real iff proof if claimed; executable source, original stdout, precise assumptions, uncertainty and provenance.

Persist into the existing Enterprise Math Draft PR #1571, preserving concurrent valid HEAD and immutable commits; read back the result. Stage266 remains portable author evidence pending a genuinely authorized native Owner/CLAIM/Source Result and independent Driver review. Source connection health and read-only status do not confer such authority.
