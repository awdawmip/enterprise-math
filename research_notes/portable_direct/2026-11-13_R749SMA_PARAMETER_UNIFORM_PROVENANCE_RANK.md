# R749SMA — Parameter-uniform delayed provenance rank and support-only parameter blindness

Date 2026-11-13 (Asia/Shanghai). Direct continuation of R749SM at `awdawmip/enterprise-math@9415de46856d44d72988953f636287d3643f2df3:research_notes/portable_direct/2026-11-13_R749SM_PREDICTIVE_HANKEL_MEMORY_HORIZON.md`, in research PR #2193. Original scientific pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Source Activity `RA-48A0B2230CE380089F80A83F`; researcher `EM-DIRECT-09A4C7`. This is the abstract positive-rational signed-Port conditional observer/controller kernel with no V29/V39 native event authorization.

## Exact theorem

R749SM exhibited four private histories Z=(Z0,Z1) with identical current eight-lift distribution after observing two legal nonforced unsigned transitions `({0,1},{1,2})->{2,3}->{3,4}` at p=1/2. In fact, **the entire construction is valid for every real parameter `0<=p<1`** in the original R749SF mixed source-preservation family `P_p=pR+(1-p)A`, provided the signed support transition is conditioned on the actually selected next unsigned support and the controller controls future support selection as explicitly stated by R749SM.

Let `q=(1+15p)/16`, `r=(1-p)/16`. The probability of each individual nonforced unsigned continuation under the uncontrolled homogeneous kernel is `2r=(1-p)/8>0`. Its conditional signed transition copies the two current shared signs and draws the new sign as a fresh independent fair ±1 coin for **all** p<1. The two consecutive nonforced transitions therefore erase first Z0, then Z1, leaving uniform current signed lifts independent of the private historical pair for all p<1.

For a forced conditional support transition, the old-only sign traverses a binary symmetric channel with correlation `theta=(q-r)/(q+r)=8p/(1+7p)` and the other two signs copy. Every such three-sign update is doubly stochastic (a permutation of axes with one BSC), hence maps the uniform current sign law to uniform for all p. The nonforced reset is likewise uniformity-preserving. Consequently R749SM's future two-stage controlled public-support law is identical across the entire interval `0<=p<1`:

[
  \Pr_p(A=a,B=b\mid\mu,\mathrm{nonforced\ prelude})
   =\frac14\left(1+\frac a2 m_{01}+\frac b2 m_0+\frac{ab}{4}m_1\right),
  \qquad a,b\in\{\pm1\}.
]

Here the controller's conditional action probabilities `(2+Z0 Z1)/4` and `(2+Z0)/4` are held fixed with p, and its two Bernoulli choices are conditionally independent given Z. The resulting public two-step likelihood matrix has `det=1/16`, rank 4 and **the same entries for every p<1**. The sharp affine predictive memory counts at H=0,1,2 are 0,1,3; deterministic private-history classes are 1,2,4.

## Distinguish provenance identifiability from parameter identifiability

At fixed initial private-history prior \mu, the conditional public two-stage support distribution after the **observed nonforced prelude** is constant in p. Its derivative with respect to p is exactly zero for 0<p<1, so the Fisher information on p in those two public choice letters is exactly zero. This coexists with full rank 4 with respect to the four private-history likelihood columns: **all four historical-source classes are identifiable from their two-step predictive probability laws, even though these same public observations carry no information about the numerical noise parameter p.**

The data scope matters: if one also includes the probability of observing the preceding two nonforced supports under the *uncontrolled* original homogeneous kernel, that prefix contributes a factor `((1-p)/8)^2` and does depend on p. An augmented adaptive controller may instead prescribe that prefix; the present zero-Fisher statement is explicitly conditional on the realized prefix and uses only the two later public support-choice letters. It does not cover p-sensitive signed emissions.

At p=1 the original homogeneous kernel assigns probability zero to every nonforced support. Therefore the two-step nonforced prelude is **outside the positive-probability conditioning domain** at that endpoint; no rank collapse is inferred there. The formulas for the future controlled support-choice law remain algebraically meaningful in a separately defined intervention model, but they are not an observation conditional of the p=1 original homogeneous chain.

## Exact evidence

Companion script `R749SMA_PARAMETER_STRATA_EXACT_CHECK.py` imports and reuses the exact R749SM signed-Port verifier, replaces only its rational BSC correlation according to p, and checks the legal conditional nonforced prelude, uniform sign posterior for all four private histories, four subsequent two-choice words, and the p-independent exact public law at `p in {0,1/8,1/2,7/8,15/16,63/64}`. Actual exact Fraction output is `PASS`: 96 full conditional signed-path tests, all six 4×4 word kernels equal, rank 4 and determinant 1/16, Fisher information 0 in the declared conditional support-only experiment. The algebraic proof establishes all real p in [0,1), not just six test points. No numerical approximation.

## Next

The parameter-invariant predictive memory is a useful stress test for typed source-safe quotient construction. For a genuinely native-authorized V29/V39 event, identify its conditional public symbol matrices, retain its exact branch/source histories, and test whether the event's predictive equivalence has a similar p-independent stratum or a truly parameter-sensitive residual. Additionally quantify minimal state coordinates when both historical-source laws and the parameter p are unknown and the observer also records prefix-event frequencies.
