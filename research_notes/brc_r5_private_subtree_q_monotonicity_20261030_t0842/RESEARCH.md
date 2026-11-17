# R5: Private-subtree Q compensation monotonicity at double LR collision

Date: 2026-10-30, Asia/Shanghai. Author-side classification: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is an auxiliary finite two-law stopping experiment; not a native X6/Heartbeat/BRC-Shor transfer or an independently accepted result.

## Immutable input pins and exact mother problem

Global Knowledge canonical main@897a3dbe5e8fef321f0fb516a9a60a0eb11775af (bootstrap, operating manual, P000 projection, ACTIVE worldview, task researcher, mathematical and BRC rules); Enterprise Math main@2c6d55763581f0fe6a83fff707e40b65bcd07f81 (AGENTS, P000, Heartbeat/X6 and joint-observer contract, portable research protocol, current authority). Global original P000 projected blob is 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc. Scientific predecessor is immutable commit b4fea861b1241b139648197accac659682b3f83b, research_notes/brc_r5_two_sign_q_compensation_no_go_20261030_t0737/RESEARCH.md.

The target remains: compare FULL history-based and seedless likelihood-ratio (LR) real behavior strategies on original O=(eP,eQ,TP,TQ). Search for equal convex hulls but unequal actual real images; a strict support gap KILLS a candidate. All sources/P000 are preserved, not altered.

## Exact model

Every natural-history P and Q mass below is an integer divided by 360. The prefix structure defines the binary natural tree until t3; at t4 stopping is compulsory. Tuple = (name,t,360P,360Q,LR-key).

    A 1 120 240 0   B 1 240 120 1
    A0 2 60 180 2   A1 2 60 60 3
    B0 2 180 60 4  B1 2 60 60 3
    A00 3 30 108 5 A01 3 30 72 6
    A10 3 30 45 7  A11 3 30 15 8
    B00 3 90 36 9  B01 3 90 24 10
    B10 3 20 40 11 B11 3 40 20 8

All natural masses are positive, normalized and consistent under splitting. Genuine dynamic collisions are at (t2,L=1) A1/B1 and (t3,L=2) A11/B11. FULL controls all 14 history nodes independently. LR shares the stop probability at the same (t,L) key, 12 keys, without persistent random seed. Both allow every real behavioral probability in [0,1].

Terminal P Bernoulli error p(t,h) may be ANY strictly legal rate, independently of Q. Q error is q0(t,h)+eta*c(t,h), with q0=2/5-t/30+(t+2)*L(h)/200, L=P(h)/Q(h), eta>0. Preserve fixed Q corrections c(A11)=+1, c(B11)=-1 at t3; c(A1)=u, c(B1)=v at t2 for arbitrary real u,v. NEW: permit six more arbitrary real corrections z_h at the private side subtree nodes A0,A00,A01,B0,B00,B01. All other Q correction coefficients zero, including compulsory t4. The sole admissibility restriction on real coefficients is 0<q0+eta*c<1 at each relevant terminal stop and 0<p<1. Q/P natural masses and LR collisions do not change.

BRC use is specifically positive, labelled two-source path-mass accounting, keeping paths and joint observables distinct. It is not a native complex-amplitude or X6 embedding.

## NEW full-real theorem: private-subtree compensation cannot heal the support gap

Fix lambda=1/75 and sign s in {+1,-1}. Put

    S=eQ-41/100-TP/200+TQ/30
    D=8-TP-TQ
    Psi_s=s*S-lambda*eta*D.

For any optional stop node h define its exact normalized signed reward
    r_s(h)= s*Qmass(h)*c(h) -lambda*(4-t(h))*(Pmass(h)+Qmass(h)).
Define
    C_A=max(0, r(A0), max(0,r(A00))+max(0,r(A01)))
    C_B=max(0, r(B0), max(0,r(B00))+max(0,r(B01))).
Write a2=r(A1), b2=r(B1), a3=r(A11), b3=r(B11). Then for EVERY admissible real coefficient and EVERY real behavioral strategy:

    F_s := max_FULL Psi_s/eta
         = C_A+C_B+max(0,a2,a3)+max(0,b2,b3).
    L_s := max_LR Psi_s/eta
         = max_{x,y in {0,1}}(
              -3*lambda*(2-x-y)+x*C_A+y*C_B+
              max(0,x*a2+y*b2,x*a3+y*b3)).

In particular, FOR EACH sign separately,

    [F_s-L_s] with private corrections >= [F_s-L_s] with all six z_h=0.

Together with the exact predecessor two-sign lemma below, the entire eight-real-parameter family satisfies

    max(F_+-L_+,F_--L_-) >= 1/25.

Therefore FULL and seedless LR four-observer CONVEX HULLS are unequal for all admissible eight-real-parameter corrections, even if the terminal P error rates are modified arbitrarily. At least one signed support functional separates an actual FULL observation from the entire LR convex hull by eta/25. Because terminal Q positivity at B11 forces eta<7/20<3/8, the L1 norm of both four-dimensional normals equals 623/600. Thus some FULL observation has L-infinity distance at least 24*eta/623 from the LR convex hull.

The bound 1/25 is SHARP among these two fixed signed directions across the enlarged parameter family: u=v=0, all six z_h=0 gives BOTH normalized gaps equal 1/25. No claim of global optimality over all possible support normals.

### Proof, exact all-real coverage

1. At a stopped history h, sum Qmass(h)*q0(t,h). The mass and likelihood-ratio identities give eQ_baseline = 41/100+TP/200-TQ/30. Since t4 is compulsory, D=8-TP-TQ=sum_over_early_stops (4-t(h))*(Pstop(h)+Qstop(h)). Thus Psi_s/eta is exactly the expected stopped-path reward r_s. No terminal P Bernoulli error appears in this scalar support functional.
2. Each natural trajectory visits each LR decision key at most once. The signed objective is multi-affine in the finitely many independent behavior stop probabilities, even when one key governs different histories, so its exact extrema over real probabilities [0,1] occur at deterministic vertices. FULL can always improve upon a root t1 stop reward -3lambda by continuing and ultimately waiting to t4, total reward 0. Its disjoint private subtree optimizes to C_A/C_B, and its A1/B1 descendants optimize independently over t2 stop, t3 collision stop, or t4 wait. This yields the F formula.
3. For LR let x=1/y=1 when the A/B root respectively continues. Each stopped root costs -3lambda. Each continued root's private side subtree retains its own unique LR keys and contributes C_A/C_B. The shared t2 A1/B1 key either stops both surviving branches or continues both. If continuing, the shared t3 A11/B11 key either stops both surviving collisions or waits. This yields the exhaustive L formula.
4. For each deterministic (x,y), replacing C_A=C_B=0 by arbitrary nonnegative C_A,C_B increases the LR candidate objective by x*C_A+y*C_B <= C_A+C_B. Hence L(C_A,C_B)-L(0,0) <= C_A+C_B. But F(C_A,C_B)-F(0,0)=C_A+C_B exactly. So Gap_s(C_A,C_B)>=Gap_s(0,0) for each sign. This is an algebraic monotonicity proof, not numerical sampling.
5. Reprove the predecessor two-sign lemma for the remaining real u,v. Set c=1/25,k=4/225,d=4/75,a=u/6-2/225,b=v/6-2/225. Direct substitution gives:
    F+=max(c,a)+max(0,b);
    L+=max(0,a+b,a-c,b-c);
    F-=max(0,-a-k)+max(d,-b-k);
    L-=max(1/75,-a-b-2k,-a-k-c,-b-k-c).
   If a<=0 then F+-L+>=c. If a>0 and b<=-c, then F+-L+=c. Else a>0 and b>-c; in this entire third real-plane region F-=d and L-=1/75, so F--L-=c. The cases are exhaustive. All real u,v are covered without a bounded grid.
6. The two hyperplane coefficient normals on (eP,eQ,TP,TQ) are (0,s,-s/200+eta/75,s/30+eta/75). In the stated positive-eta range their L1 norm is 1+1/200+1/30=623/600. The support gap eta/25 yields L-infinity lower bound (eta/25)/(623/600)=24 eta/623 by Holder duality.

## Fully nonzero signed private-compensation example

Let eta=1/1000; (u,v)=(1/2,1/10); (z_A0,z_A00,z_A01,z_B0,z_B00,z_B01)=(1,-1,1,-1,1,-1), all six nonzero. Use legal p(t,h)=1/5+t/20+(t+1)/(100 L(h)). Exact supports: Gap_+=0, Gap_-=13/300. A legal FULL deterministic stop mask 8272 yields

    O*=(6901/18000,169093/540000,101/36,149/45).

Every real seedless LR policy and its convex hull obey

    4500000*eQ - 22560*TP + 149940*TQ >= 1842478.

At the FULL point the left-hand side is 1842283, exact integer violation 195. Thus L-infinity distance >=195/(4500000+22560+149940) = 13/311500. This strictly strengthens the uniform bound in a concrete case with both signs of private Q adjustments.

## Exact executable evidence and boundary

VERIFY.py performs full exact standard-library Fraction checks of 14 positive normalized P/Q path masses, both dynamic LR collisions, strict terminal probability constraints at every stop, and 16,384 FULL + 4,096 LR deterministic masks for each sign under six rational parameter choices: 245,760 exactly scored policies. It checks analytical supports, monotonicity, the witness observation and exact separation. Actual stdout is EXACT_OUTPUT.txt; final marker PASS_EXACT_R5_PRIVATE_SUBTREE_Q_COMPENSATION_MONOTONICITY. The all-real theorem is the proof above, not an inference from the six finite instances. No independent Driver review, native X6 correspondence, formal Lean verification, novelty-priority, or Source RESULT has been obtained.

NEXT: the private A0/A00/A01/B0/B00/B01 branch reward family is excluded as a remedy. Change Q error rates at collision-reachable but individually distinguishable t3 A10/B10 nodes, or alter the natural source-sensitive kernel under both exact collision constraints. First derive BOTH signed supports, then require all-signed four-observer hull equality via at-most-five rational LR convex combinations for every FULL deterministic vector or an exact rational Farkas separator. Only after hull equality can actual real image nonmembership be tested. Preserve immutable predecessors, P000, real owner/role bounds and author contribution provenance.
