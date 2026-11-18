# Stage204 — exact full-real optimum in the external ternary IID N14 problem

**PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.** Executed 2026-10-27. Scientific parent: Stage203 at immutable commit d70598906ed8ffac8fba281107b581ccc0517cf3, in the existing Draft PR #1571.

## Domain, claim and proof obligations

Take IID law P=(3,1,20)/24, Q=(2,2,20)/24 and horizon N=14. Allow **arbitrary randomized stopping and reporting policies depending on all complete ordered histories**. Put eP=P(report Q), eQ=Q(report P), tP=E_P T and tQ=E_Q T; define V14(alpha)=inf_(eP,eQ<=alpha) max(tP,tQ).

Let alpha203=1237525705766008115/3505953353861431296, V203=2226587197356332573/219122084616339456. Let K204=L204=6550632/53665 and H204=56640586903640112316369/587959333546792845312. Set Delta204=6875828125/427972821516288 and alpha204=1237582032550008115/3505953353861431296, V204=2225727754437932573/219122084616339456.

**Theorem.** For **every real** 0<=delta<=Delta204, including irrational delta,

  V14(alpha203+delta) = V203 - (13101264/53665)*delta.

For each feasible alpha>alpha204, the **fixed Stage204 supporting affine line** H204-(13101264/53665)*alpha lies strictly below V14(alpha). This does not claim that V14 is strictly above all supporting lines.

## Bellman dual, including uncompressed full-history strategies

At s=(n,a,b), a and b count symbols 0 and 1, with likelihood ratio Q/P=2^(a+b)/3^a. Under P and K=6550632/53665, the rational Bellman recurrence is

  h(s) = min { K*(Q/P)(s) [report P], K [report Q],
               1 + (3*h(child0)+h(child1)+20*h(child2))/24 [continue, n<14] }.

Exact Fraction backward induction enumerated 680 states, root h(0,0,0)=H204, exactly 1238 strictly positive alternative action gaps, minimum 43804/1448955 and no negative gap. The only ties are U=(9,2,2), report Q/continue, and Z=(14,0,0), report P/report Q. Every other action is uniquely fixed. All conditional suffix laws and the likelihood ratio depend only on counts under these IID inputs. Thus this Bellman calculation lower-bounds **every ordered prefix** even for full-history-dependent randomized policies. Summing gives tP+K*(eP+eQ)>=H204 and hence V14(alpha)>=H204-2*K*alpha.

## Exact primal attainment

Let u be the probability of report Q instead of continue at U; let z be the probability of report P instead of report Q at Z. Otherwise take the unique Bellman action. Four deterministic corner policies were independently evaluated by a rational conditional-suffix DP and by a second **unmerged integer-weight ordered-history DFS**, with separate P and Q positive masses (3,1,20) and (2,2,20); an early leaf with length n is padded by 24^(14-n). Both algorithms return identical four-dimensional observer vectors in the coordinate order O=(eP,eQ,tP,tQ).

For exact data, certificate204.json contains O00, O10, O01 and O11. Their exact affine coefficients are:

  O00 = (637527965338350899/1752976676930715648, 4068995092961/11888133931008, 2226587197356332573/219122084616339456, 259209256153735/26748301344768)
  DU = O10-O00 = (321978125/2641807540224, -150034375/1671768834048, -1295215625/330225942528, -858053125/139314069504)
  DZ = O01-O00 = (-6103515625/78364164096, 6103515625/78364164096, 0, 0)
  M = O11-O10-O01+O00 = (0,0,0,0).

The zero mixed term is also proved structurally: U has observed two 0-symbols and two 1-symbols, while Z has zero of both; count monotonicity forbids U→Z, and Z is terminal so forbids Z→U. No history can be touched by both coins. Accordingly for **all real** (u,z) in [0,1]^2,

  O(u,z)=O00+u*DU+z*DZ.

Exact error equalization eP=eQ gives

  z(u)=112590674732081049/819200000000000000
       +(43473243/32000000000)*u.

The endpoint z(1)=113703589752881049/819200000000000000; both endpoints lie strictly between 0 and 1, so all real u in [0,1] are legal. Along this segment the common error increases strictly and affinely from alpha203 to alpha204 by Delta204. The P−Q time differences at u=0 and u=1 are 34381656981645151/73040694872113152 and 11515014321881717/24346898290704384, both positive, so max(tP,tQ)=tP throughout. Chosen actions all attain Bellman equality. For arbitrary real delta in the stated interval set u=delta/Delta204 and z=z(u), attaining the universal lower bound exactly.

## Strict-right property for this fixed support

The set of N14 full-history behavioral policies is a finite product of compact simplices. Its observer map is continuous, so each feasible constrained optimum is attained. Equality for alpha>alpha204 in max(tP,tQ)>=tP>=H204-K*(eP+eQ)>=H204-2*K*alpha requires eP=eQ=alpha and zero Bellman slack at every reached positive-P history. Uniquely optimal non-tie actions are then forced. Multiple ordered prefixes at U have identical conditional suffix laws and LR, so averaging their U-coins with positive P-prefix masses gives one effective u in [0,1] with identical observer vector. Z has only the all-symbol2 history. Their tie cones do not intersect. Every such zero-slack policy therefore has O(u,z) as above; equal errors force z(u), and its maximum common error is alpha204. This contradicts alpha>alpha204 and proves strict separation from the fixed support.

## Execution, BRC and native transfer boundary

Executed primary verify_stage204.py (full original available in the companion portable evidence archive): exact Fraction Bellman+suffix observer DP and unmerged positive integer-mass DFS. Counts per corner (u,z): 00=92974, 01=92974, 10=84856, 11=84856, total **355660** DFS nodes. 246 U-first-arrival ordered histories, one Z history, zero intersection. Actual stdout: STAGE204_AUTHOR_EXACT_FULL_REAL_PASS. A separately run compact and directly reproducible reference is REPRO_STAGE204.py, stdout STAGE204_REFERENCE_EXACT_PASS 355660. The exact dual scan for Stage205 is recorded in scan_stage205.py and certificate205_dual.json; it is not Stage205 primal proof.

**BRC resolution: REUSE_APPLIED.** The carrier is a positive weighted branch tree preserving ordered path labels, multiplicity and separate exact P/Q masses until the stated observer projection. Count-state compression is justified only by the proven conditional IID suffix factorization; it does **not** establish phase or signed cancellation, native X6 operations, P000 rotations or native three-dimensional-slice dynamics. ACTIVE P000 six-axis/one-time-dimension, three-dimensional research slice and 120-degree native orthogonality are not altered. A native transfer still requires a slice embedding, third-coordinate semantics, readout and preserved relations/updates. GitHub persistence is not a Source CLAIM, frozen Result or independent Driver mathematical admission.

Sources: GLOBAL_KNOWLEDGE_V1 main@138a017a98649b4a7d16ddbff1cc0dfa13028cfb; Enterprise Math control main@a7d98c76f02e09d6131f16b04a97dede4026b2eb; P000 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc.
