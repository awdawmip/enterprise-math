# R284GT — Sublinear-omission flexibility transition and exact one-edge injection

2026-11-24. Author proof, NOT_REVIEWED. Informed independent continuation of the frozen auxiliary four-phase binary fixed-tag model. P000 / ACTIVE worldview unchanged; the lattice of attempted counts is an auxiliary discrete carrier, not native spatial geometry or physical attribution. Original registration r1-20261124-0256-r284gd-session-v1 read back SUCCEEDED (EM-DIRECT-0C386E, RA-B82240E8488EF5A1DA5186C4). Previous owner request r1-20261124-1600-owner-read now SUCCEEDED, snapshot as of 2026-11-24T08:02:10.170649Z returned no LEASED entries. Fresh r1-20261124-1700-owner-read queued; no shared CLAIM or formal task mutation. Initial em_status reported BACKEND_IDENTITY_CHECK_UNAVAILABLE, operation_sent=false; subsequent receipt reads and new read-only owner query worked.

Frozen inputs (read at exact commits):
- GS 66a518fef06384f130ecd16912ef5a2231ebc960:research_notes/portable_direct/R284GS_LOW_OMISSION_ASYMMETRIC_PATH_COUNTS_20261124.md (counts, observers, corridor).
- GL 5f74ba8a545788cc3fdb080f9953bbe5a0926531:research_notes/portable_direct/R284GL_ASYMMETRIC_THREE_PATTERN_SHARP_CAPACITY_20261124.md (exact prefix distances).
- GQ 9f74833b63383390e436542669d7601834a0b2ea:research_notes/portable_direct/R284GQ_ALL_PARAMETER_MINIMIZER_RIGIDITY_20261124.md (minimizers).
- GR e72cd4e1806d52fdc27923852e7e8fa49720b0ab:research_notes/portable_direct/R284GR_EXACT_OPTIMAL_MODE_WORD_COUNTS_20261124.md (cycle observer).
Current normative snapshots: global 7a3e5434c3a83601bba58309f895c4952235414f, EM a768f4b48f5e3df99fc7f9f79e2a30e1a5ca43fc. No changes to scientific pins.

## 1. Main asymptotic theorem

For 0<=q<u define H=2q+u+1, J=q+3u and let S,P,Q count one-edge safe mode words for (A,B,C)=(H,J,H),(H-1,J+1,H),(H,J+1,H-1), respectively. Use the GS cycle convention: symmetric mode count S^4, asymmetric (PQ)^2. Define K=PQ(J+1)^2/(S^2 H), whose square is the ratio of physically labeled cycle order counts, asymmetric/symmetric.

For every integer sequence u->infinity, q>=0, q/u->0:
    PQ/S^2 ~ 36/(16+3q)^2,
    K ~ 324u/(16+3q)^2.
Here ~ is relative asymptotic equivalence along the stated sequence, including fixed q. In particular if q/sqrt(u)->c in (0,infinity), K->36/c^2. For c<6 asymmetry eventually strictly wins labeled counts; c>6 symmetry eventually wins. If q/sqrt(u)->0, K->infinity; if q/sqrt(u)->infinity but q/u->0, K->0. At c=6 the limiting ratio is 1; no sign claim on that critical scale without higher-order analysis. The full-cycle labeled ratio tends (36/c^2)^2. This is a sublinear-scale transition theorem, not an assertion of a unique finite-u boundary or of behavior in the remaining linear regime.

For each fixed q, the safe fractions S/binom(H+J,H), P/binom(H+J,H-1), Q/binom(H+J+1,H) tend respectively to
    (3/4)^q * (16/27)*(4/3+q/4),
    (3/4)^q * 4/9,
    (3/4)^q * 4/9.
Thus absolute mode-count and normalized mode-fraction ordering favor symmetry eventually throughout the sublinear regime, although the physical-labeled preference switches.

## 2. Exact corridor and retained boundary events

Use GS notation r=2u+1,e=A-2q,d=C-2q,s=r-d,t=e-s,h=B-q-s.
For S, (t,h)=(1,2u); for P, (0,2u+1); for Q, (0,2u). Exact safety throughout a word is
    [e-a]_+ + [b-q]_+ >= s,
    b <= h+[a-q]_+.
The lower bound is vacuous for a<=t, is b>=q+a-t for t<a<e, and is b>=q+s for a>=e. Uniform word means each of the binom(A+B,A) words with fixed inventories equally likely; this is an auxiliary normalized count, not a physical stochastic omission model.

Let N=A+B, and mark the first step reaching a=t+1, at b=q+l. Any safe word has l>=1 since e>t+1 for sufficiently large u (the proof of the limit ignores finitely many small u). Every prefix ending at this marked step has t earlier A steps, q+l B steps, and the final A. There are binom(q+l+t,t) such prefixes. Lower safety before the cut is automatic; upper safety before it holds for every fixed l eventually since q=o(u), h~2u. After it the lower residual height b-a-q+t starts at l-1. The terminal upper residual in reversed counts a'=A-a,b'=B-b is t+b'-a': the exact upper rule becomes b'>=a'-t for a>=q; an upper violation anywhere implies this reversed height negative because h+[a-q]_+ >= h+a-q and B-h+q=A-t. A lower violation after the cut always implies b-a-q+t<0, including the capped region a>=e.

Let p=1/4,beta=3/4,rho=p/beta=1/3. For fixed l>=1, conditional on any specified prefix at the cut, the remaining word is uniformly shuffled with A-(t+1),B-(q+l) counts. Their proportion tends p,beta even when q grows sublinearly. For any fixed m the first and last m steps of this remaining word converge jointly to two independent iid Bernoulli step sequences with these probabilities, by the finite falling-factorial sampling law. In those first m steps, the lower rule is exactly the residual nonnegative walk rule (a<e); upper safety automatic. In the last m steps, the upper rule is exactly the reverse residual rule (a>=q); lower safety automatic.

To justify replacing finite windows by whole paths, not just assume independence, take any remaining prefix or reversed suffix of length k. Its number X of A steps is hypergeometric with population fraction p_u<=0.3 eventually. E[2^X] <= (1+p_u)^k: expand product of (1+indicator_A) and use Pr(all j prescribed positions are A)=(A_remaining)_j/(N_remaining)_j<=p_u^j. Thus Pr(2X>=k-c)<=2^(c/2)(1.3/sqrt(2))^k, with c any fixed real. A failure of the lower height after the marked cut implies 2X>k+l-1, while a failure of the reverse upper height implies 2X>k+t. Both are bounded by the geometric tail (even c=0 suffices). Summing for k>=m bounds the probability of any failure beyond the respective windows uniformly for large u. The exact lower and upper conditions may be weaker away from the windows, so this union bound suffices. First let u->infinity with fixed m,l, then m->infinity. This proves that the conditional probability of completing a safe word tends
    G_t(l)=(1-rho^l)(1-rho^(t+1)).
For an upward biased +/-1 walk starting at height x>=0, the probability of never becoming negative is 1-rho^(x+1): solve the two-boundary difference equation for hitting -1 before a finite upper level, then let that level go to infinity. The stopping events increase to ever hitting -1. This gives both factors. This limiting multiplication is justified for the two retained end ports and the uniform fixed-inventory observer only. It does not assume independence of actual source omissions or identify full word histories.

## 3. Sum over marked prefixes; common rare-event factor

Write (x)_k=x(x-1)...(x-k+1), F=(B)_q/(N)_q. The probability mass of all prefixes ending at the cut with b=q+l, before enforcing the remaining conditions, is exactly
    binom(q+l+t,t) * F * (A)_(t+1) (B-q)_l / (N-q)_(t+1+l).
Let g_u(l) be the conditional probability that the whole word is safe, including the cut-prefix safety (averaged over those prefixes if needed). For each fixed l, all prefixes are valid and the suffix condition has the same count, so g_u(l)->G_t(l). For invalid l set the term zero. To control the sum, the falling-factorial ratio is bounded above by ((B-q)/(N-q))^l<=0.8^l eventually (discard the condition on the A positions, keep l specified B positions after conditioning q B positions). For t=0 the binomial factor is 1; for t=1 it is q+l+1. If q tends to infinity, divide by q^t to obtain a common summable bound (l+2)0.8^l. If q is fixed, use (q+l+1)0.8^l. Hence dominated convergence is valid even when F itself is exponentially small.

For fixed q, F->beta^q. With t=0, the sum after dividing by F tends
    p(1-rho) sum_{l>=1}(beta^l-p^l)=4/9.
For t=1 it tends
    p^2(1-rho^2) sum_{l>=1}(q+l+1)(beta^l-p^l)
      = (16/27)(4/3+q/4).
These evaluations use sum(beta^l-p^l)=8/3 and sum l(beta^l-p^l)=104/9. For q->infinity with q=o(u), the same divided-by-q^t limit is 4/9 for t=0 and 4/27 for t=1. Thus for the two asymmetric orientations the fractions are asymptotic to (4/9)F_P and (4/9)F_Q; for symmetric, asymptotic to (4/27)q F_S in the growing-q case.

The common factors F_P/F_S and F_Q/F_S tend to 1: the individual B,N inventories differ by at most one, each of the q product factors has relative deviation 1+O(1/u) uniformly since q=o(u); product log bound O(q/u) tends zero. This cancels the shared small prefix probability without replacing it by beta^q in the growing regime. In particular, simply plugging a growing q into the fixed-q survival formula would not justify the result.

The two unrestricted word ratios are exactly H/(J+1) and (H+J+1)/(J+1), respectively; their product tends 4/9. Combining the survival fractions gives PQ/S^2 -> 36/(16+3q)^2 for fixed q, and PQ/S^2 ~ 4/q^2 for growing sublinear q. These together yield the claimed relative asymptotic for all q=o(u): any violating sequence has a subsequence with either fixed q or q->infinity. Finally (J+1)^2/H ~ 9u. This proves the transition. The cycle-normalized safe fraction comparison is the square of the product of the two asymmetric fractions divided by the square of the symmetric fraction; it is eventually <1 since that product ratio is asymptotic to (9/(16+3q))^2. The proof uses positive branch multiplicity with exact cut inventory and two conditional residual end ports before taking the limit; no untyped spatial quotient or physical interpretation.

## 4. Exact strict one-edge injection (all low-omission integers)

For Q, t=0 and the first step must be B (at a=1,b=0 the lower rule fails). Delete the first B. All remaining prefixes have b reduced by one, the upper bound is preserved since Q and S have the same h=2u, and the lower bound is preserved since S has the same e=u+1 and s one less than Q. The initial empty prefix is safe. This yields an injective map to S-words, with unique candidate inverse inserting B at the start. The S word B^(2u) A^H B^(J-2u) is safe: its first segment satisfies the upper bound, second has b=2u>=q+s, and the last remains within the terminal upper bound. Its inverse violates Q's upper bound at a=0,b=2u+1. Therefore Q<S strictly for every 0<=q<u. This does not yet prove P<S everywhere, nor universal full-cycle symmetry for arbitrary q/u.

## 5. Executed finite integer evidence

The following DP used original GL distances (not the asymptotic reduction). All 465 pairs u=1..30,0<=q<u satisfied both P<S,Q<S; no exception. Additional 25 fixed-q samples q in {0,1,2,4,8}, u in {16,32,64,128,256}, plus eight valid moving-q cases u in {64,256,1024}, q=c sqrt(u), c in {4,6,8}, q<u, were executed. Integer counts exact; reported ratios below truncated at 8 decimal places. The moving-q evidence demonstrates finite-size displacement of the transition (at c=6 the theorem only gives a limit of 1).
Moving-q (u,q,q^2*PQ/S^2,K):
64,32,1.89707146,0.72704126
64,48,1.74215673,0.27278027
256,64,2.60407808,1.14583828
256,96,2.47033960,0.44668366
256,128,2.32596776,0.22266464
1024,128,3.15354242,1.53957537
1024,192,3.02911018,0.62168156
1024,256,2.89293515,0.31828230
At u=256 fixed q=0,1,2,4,8, PQ/S^2 respectively .14099042,.09991584,.07436747,.04560818,.02196151; the exact limiting formula gives 36/(16+3q)^2. Finite evidence supports but does not replace the proof.

```javascript
function dp(q,u,A,B,C){const r=2*u+1,p=x=>Math.max(0,x),M=p(C-q),v=Array(B+1).fill(0n);for(let a=0;a<=A;a++)for(let b=0;b<=B;b++){const D2=p(A-a-2*q)+p(p(b-q)+M-q),D3=Math.max(0,C-2*q,p(a-q)-q,B-b+p(a-q)-2*q+M);v[b]=D2<r||D3<r?0n:a===0&&b===0?1n:v[b]+(b?v[b-1]:0n)}return v[B]}
function comb(n,k){let z=1n;for(let i=1;i<=Math.min(k,n-k);i++)z=z*BigInt(n-i+1)/BigInt(i);return z}
const scaled=(a,b)=>String(a*100000000n/b);
let checks=0,exceptions=[],samples=[],lastSym={};for(let u=1;u<=30;u++)for(let q=0;q<u;q++){let H=2*q+u+1,J=q+3*u,S=dp(q,u,H,J,H),P=dp(q,u,H-1,J+1,H),Q=dp(q,u,H,J+1,H-1);checks++;if(Q>=S||P>=S)exceptions.push([q,u,String(P),String(Q),String(S)]);if(P*Q*BigInt((J+1)**2)<=S*S*BigInt(H))lastSym[q]=u;}
for(let q of [0,1,2,4,8])for(let u of [16,32,64,128,256]){let H=2*q+u+1,J=q+3*u,S=dp(q,u,H,J,H),P=dp(q,u,H-1,J+1,H),Q=dp(q,u,H,J+1,H-1);samples.push({q,u,modeRatio:scaled(P*Q,S*S),fractionS:scaled(S,comb(H+J,H)),fractionP:scaled(P,comb(H+J,H-1)),fractionQ:scaled(Q,comb(H+J+1,H)),labeledPerU:scaled(P*Q*BigInt((J+1)**2),S*S*BigInt(H*u))})}
console.log({checks,exceptions,lastSym,samples,scale:100000000});
let out=[];for(let u of [64,256,1024])for(let c of [4,6,8]){let q=Math.floor(c*Math.sqrt(u));if(q>=u)continue;let H=2*q+u+1,J=q+3*u,S=dp(q,u,H,J,H),P=dp(q,u,H-1,J+1,H),Q=dp(q,u,H,J+1,H-1);let scale=100000000n;out.push({q,u,c,modeRatioTimesQ2:String(P*Q*BigInt(q*q)*scale/(S*S)),labeledRatio:String(P*Q*BigInt((J+1)**2)*scale/(S*S*BigInt(H)))})}
console.log({scale:100000000,out});
```

## 6. Next
Obtain first finite-size correction to K in the q~6 sqrt(u) regime and prove or disprove a unique finite-u transition. Investigate linear q/u regime separately (conditioned prefix may occupy macroscopic part of the word). Prove or refute P<S and universal normalized ordering. GR middle-regime optimizer and independent GP/GQ rational certificates remain open. No repeated capacity enumeration.
