# R5 — exact seedless LR reconstruction of the five-observer separator after forgetting one BRC coordinate

Date: 2026-11-06, Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Frozen scientific inputs remain GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Parent five-observer gap: RESEARCH.md in this directory. This is the same strictly positive four-stage delta=1/4 P/Q/BRC auxiliary model.

## Exact projection-repair theorem

The FULL_HIST witness in RESEARCH.md has the original four observations

W=(eP,eQ,TP,TQ)=(161801/180000,6499/18000,267/80,137/40).

**This precise W is attainable by a valid seedless LR strategy.** Thus its five-observer separation is entirely lost when M_{3/2} is forgotten, even though the extra mass observer differs by 21/1040 in the explicit paired strategies.

## Constructive LR policy, all rational

Set the root continuation g=1, the two time-2 Q continuation flows u0=1 and u1=12/13. The time-3 LR-key pooled flow is

(X0,X1,X2)=(81/520,4/13,0).

The capacities are V0=13u0/40+u1/80=35/104, V1=u0/10+9u1/40=4/13, V2=3u0/40+21u1/80=33/104, and the **shared** time-3 conditional continue probabilities are

(z0,z1,z2)=(X0/V0,X1/V1,X2/V2)=(81/175,1,0).

They are in [0,1] and depend only on the current LR key, not the earlier history. The exact time equations yield TP=267/80, TQ=137/40.

Set alpha=47/180, beta=67/162, A=u0/10, B=9u1/40. The pooled terminal coefficient is J_LR=X1*(alpha A+beta B)/(A+B). The stopped masses relevant to declarations are

M_{1/10}=93649/468000,
M_{1/2}=47/260,
M_{3/2}=33/104.

Use shared-by-ratio declaration probabilities

p_{1/10}=92924/93649,
p_{1/2}=169/188,
p_r=0 at all other ratios.

Their exact stopped Q declaration masses are ell_{1/10}=1787/9000 and ell_{1/2}=13/80. Hence

eQ=ell_{1/10}+ell_{1/2}=6499/18000,
eP=1-(1/10)ell_{1/10}-(1/2)ell_{1/2}=161801/180000.

All distributions normalize, and the likelihood-ratio moment sum is one. Thus this policy has the same W as the preceding FULL_HIST policy, while its extra observer is M_{3/2}=33/104 instead of 27/80. The exact difference is 21/1040.

## Scientific consequence and status

This provides a concrete observer-fiber pair: identical original four readouts, distinct stopped-ratio histograms, with FULL_HIST and seedless LR realizations fully explicit. The scalar central history defect can be exactly repaired in the original observer space by changing the earlier branch occupancy and declaration probabilities. The additional BRC coordinate detects the distinction, and the original readout deliberately forgets it.

This is an **exact positive reconstruction for one rational W**, not a proof of equality of the complete four-observer images. It changes the NEXT_UNIT direction: seek a different interior rational W whose entire K(W) avoids the LR quadratic zero, or construct a general repair over an analytically specified family.

Companion VERIFY_PROJECTION.py uses only the Python standard-library Fraction class to check capacities, shared probabilities, all seven mass bins and moments, both times, declarations, exact four-output equality and the differing extra mass. Its complete actual run is PROJECTION_OUTPUT.txt, ending PASS_EXACT_R5_FOUR_OBSERVER_LR_RECONSTRUCTION.
