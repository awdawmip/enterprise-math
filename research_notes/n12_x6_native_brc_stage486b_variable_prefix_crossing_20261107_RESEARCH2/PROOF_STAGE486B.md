# Stage486-B — Variable T and Q POP boundary crossing

Date 2026-11-07. Author-side exact theorem and executed checks; independent review pending. Parent: Stage485-B @ 874a2075bc18af8704a619118b888298a18fb45c, research2 draft PR #1736.
Frozen scientific inputs: GLOBAL main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419, P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current behavior rules read separately.

## Exact model

X6 is the native six-axis affine torsor with ordered primitive directions D={+E1,...,+E6,-E1,...,-E6}. These are 12 signed directions, not 12 spatial dimensions. Time, if used, is separately typed. Direction words are ordered native provenance, not final Cell addresses. Let A=+E1, k,u>=1, m=2k+2, T in D^m, W in D^k and H in D^u. Set P=T and Q=T W A H A. Work within one complete initial observer fiber: lengths, both signed X6 displacements, both entire 144-entry directed adjacency count vectors and positional equality K. Compare all common legal action words and every action prefix, with P_POP<=k, P_APPEND<=k, Q_POP<=h, Q_APPEND<=a, a any finite nonnegative integer; POP requires current length>1 and APPEND may take any of D.

## Theorem 486.1: exact future-equivalence key

For each integer 0<=h<=|Q|-1 define
```
r=min(h,u)
L=max(k+1,h-k-u-1)
R_h=(suffix_L(T), W, suffix_r(H)).
```
Then two histories in the same full initial observer fiber have equal observers for every common legal future operation prefix if and only if R_h agrees. In particular, for u<h<=u+2k+2 the old Stage485 variable-T key still suffices: it retains suffix_(k+1)(T), W and all H. Only from h=u+2k+3 can an older T symbol become necessary.

**Sufficiency.** P can remove at most k original edges, all determined by suffix_(k+1)(T). The original Q tail after T has k+u+2 letters (W,A,H,A). At most h original edges can be removed by h total Q POP operations, including those interleaved with known APPENDs. If h crosses that tail, put c=max(0,h-(k+u+2)); at most c original T edges are removed, all determined by suffix_(c+1)(T), which the key retains. Initial edge multiset, displacement and length plus known removed/appended edges recursively determine these three observers.

For positional K: whenever both histories retain original T at a position, P and Q match in each history. Original T at a position touched by P APPEND must lie in the last k+1 positions (P can POP at most k); those symbols are retained. Original T touched by Q APPEND requires Q first to POP through W,A,H,A and part of T; the replaced T positions lie in the retained suffix_(c+1)(T). W is known; unknown H prefix, for h<=u, remains beyond P's greatest possible length m+k, hence cannot enter K. All appended letters are fixed by the common action word. Therefore K also agrees after every action prefix.

**Necessity.** Different W is detected by appending the first history's W to P in k actions (the original T prefix always matches Q and the first history gets k new matches). Different retained H suffix is detected by consecutive Q POPs: the first different deleted directed edge changes Q's adjacency vector. Different suffix_(k+1)(T) is detected by at most k P POPs. If L>k+1, the additional retained T suffix is detected by consecutive Q POPs crossing the k+u+2-letter tail and then into T. In each case the distinguishing legal witness uses no Q APPEND, so it applies to every finite a. QED.

## Theorem 486.2: exact integer Euler–BRC raw population

Let E(X) be the directed edge-count multiset of X, ThetaP=E(P), ThetaQ=E(Q), and let the first native direction s be recovered uniquely from
v(s)=DeltaP-sum_(x,y)ThetaP(x,y)*v(y).
For a fixed valid key (sigma,W,S), L=|sigma|, r=|S|, compute
```
P_rem=ThetaP-E(sigma)
R=ThetaQ-ThetaP-[sigma_last->W_first]-E(W)-[W_last->A]
M(sigma,W,S)=N(m-L+1,s,sigma_first,P_rem)*G_r(R,S)
G_0(R,empty)=N(u+2,A,A,R)
G_r(R,S)=N(u-r+2,A,S_first,R-E(S A))  (r>=1).
```
A negative edge residual has population zero. N(l,s,t,e) counts original ordered native direction words with l letters, first s, last t and exact edge multiset e, with equal edge instances indistinguishable. The recursion N(1,s,t,0)=[s=t], N(l,s,t,e)=sum_(v:e(s,v)>0)N(l-1,v,t,e-[s->v]) computes an exact integer.

**Proof.** T is the overlap-concatenation of its prefix U (length m-L+1, ending sigma_first) and sigma; U has precisely P_rem edges. Independently, A H A is the overlap-concatenation of a path from A to S_first of length u-r+2 and the fixed suffix S A. The edge bags split as the formula requires. Choices of U and the hidden H prefix are independent; their original-word Euler counts multiply. Positive support sums give exact class numbers, and summing M gives the raw initial fiber population. QED.

The memoized Euler subroutine visits at most O(d(n+1)^s) integer transitions for d active letters and s active directed edge types, each integer of bit size O(n log d). This covers the Euler subroutine, not enumeration of possible repair keys or rank/unrank over support.

## Sharp boundary witness

Take k=u=2; T1=AABAAA, T2=ABAAAA, W=AB, H=AB, Q_i=T_i AB A AB A. Both initial complete observers coincide. With h=8, R8=(AAA,AB,AB) is the same and eight Q POPs leave Q=AABA and Q=ABAA, which have equal edge multisets. Nine Q POPs leave Q1=AAB with edges AA+AB and Q2=ABA with edges AB+BA, separating their observers. The repaired h9 suffix length is L=4, giving BAAA versus AAAA. The Euler class populations for this witness are M(h8)=2 and M(h9)=1.

## Executed exact evidence

The source alphabet {A=+E1,B=+E2,G=-E1} embeds in the full 12-direction X6 alphabet. Finite initial fibers are grouped by the full observer restricted to this source alphabet; all missing entries of the 144-edge vector are identically zero. Local Python standard-library integer checks exhaust all 3^(m+k+u) original histories:
* k=1,u=2: 2,187 raw histories, 1,350 initial fibers, h=0..8, exact M equality for every key.
* k=2,u=2: 59,049 raw histories, 17,940 fibers, h=0..11, exact M equality for every key. Future class totals: h=0 42,525; h=1..8 54,675; h=9..11 59,049.

A separate full-operation paired-state explorer on the strict witness, with all 12 signed APPEND directions available to both parties, P POP<=2, P APPEND<=1, Q APPEND<=1, inspected 4,563 paired states at h8 (all equal) and found a distinction at h9 (4,261 visited states). These finite observations verify the specified bounded experiments; arbitrary finite a is covered by the theorem's action-induction proof. The full executed local code and evidence are retained in the Stage486 handoff as well as the remotely executed-portable independent checker and its stdout.

**Source/authority:** GitHub push access checked; native service session and task query both rejected before dispatch with BACKEND_IDENTITY_CHECK_UNAVAILABLE and operation_sent=false. No native CLAIM or Result; author-side derivation remains UNREVIEWED / NOT_ADMITTED.

**Next Stage487-B:** nonenumerative exact Boolean class-support and rank/unrank for growing k,u using sparse remaining-edge DP, plus independent adversarial audit of the K preservation step.
