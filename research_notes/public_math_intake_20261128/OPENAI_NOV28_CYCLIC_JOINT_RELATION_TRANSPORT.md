# 2026-11-28 public mathematics intake — cyclic joint-relation transport

Status: AUTHOR_CHECKED_AUXILIARY_LEMMA / UNREVIEWED / NOT_ADMITTED. External finite tensor-network transport model on a declared X6 coordinate graph; not a native BRC execution or physical result. Same Nov24–27 candidate line, no new independent Task or review claim.

## Source and recovery
- GK canonical main 70d733154bc36b4b7c3172e8e9d62ee9a7e430eb: bootstrap/manual read at one snapshot, research/project entry, verified P000 projection against canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, evidence/temporal policies, BRC and Activity/journal routes. EM canonical main 70172fae3a2a325718d886b62e825fe5f135b7b0: continuation, autonomous operations, research method, P000/Heartbeat/residual and control/Driver contracts. em_status 0.6.11 current control Source same, no role granted by status.
- OpenAI/math main 3344da59991ed94f9ba711217b29c1d760badfa6; comparison with previous pin identical, ahead=behind=total_commits=0, files=[]; combined statuses=[]. Official indexes https://openai.com/research/index/ and https://openai.com/research/index/publication/ checked Nov28: latest visible Nov24 protein-design item; targeted recent search found no new relevant math announcement. No new paper/revision/withdrawal in checked repository; no independent Lean/Comparator/dependency/axiom run, prior formal coverage unchanged.
- Highest scientific frontier consumed: de172667470a089fed901dd752f14fa8e1258435:research_notes/public_math_intake_20261127/OPENAI_NOV27_TREE_EXACT_CAPACITY_AND_PAID_SELECTOR.md (same file read on current immutable main); retain prior tree and selector proof scope. Original request math-intake-20261127-0930-integration-task-read-r1 now SUCCEEDED/error=null, source 834536b82a663d5f09543d9c454ff05e4bbc7ef9, historical HANDOFF_READY/NEEDS_DISPATCH/no claim; exact Task RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028 / TP2-8FD66B1B48BE87DA1AC1. Original registration math-intake-20261125-0930-own-research-registration-r1 still SUCCEEDED but driver_authorized=false, execution_authorized=false; no inherited private capability or current independent role inferred. Current task read math-intake-20261128-0930-integration-task-read-r1 last RUNNING/error=null; consume original ID only. Preserve frozen ETH 7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a and task publication source refs; no modifications to the integration seed, its 203 partitions, or first-free reachability results.
- Targeted default-branch code search for progression-free, cyclic tensor network, matrix multiplication subrank and VP VNP returned zero matches; limited index evidence, not a novelty guarantee. The construction below is a scoped adaptation of progression-free diagonal extraction from a triangle tensor, not a claim of inventing tensor subrank theory. No duplicate Task needed for this finite extension of the previously saved candidate.

## 1. An exact single-branch cyclic construction beats every spanning tree of the same allowed graph

Let F be any field; b>=1 integer, D=2^b, k=floor(log_3 D), and S={sum_{j=0}^{k-1} eps_j 3^j : eps_j in {0,1}} (k=0 allowed). Then |S|=2^k and max S=(3^k-1)/2<D/2. S has no nontrivial 3-term arithmetic progression: if a+c=2d with a,c,d in S, all ternary digits on both sides are in {0,1,2} without carry. Each digit then forces a_j=c_j=d_j.

Use the following six vertices in a signed six-coordinate chart relative to a chosen Cell (all unlisted coordinates explicitly zero): 0, e1, e1+e2, e1+e2+e3, e2+e3, e3, with consecutive edges and the closing edge back to 0. Each edge is a signed axial unit step, length 1. Terminals A=0, B=e1+e2, C=e2+e3. The only allowed edges in this example are the six cycle edges. There are three length-2 arcs AB, BC, CA; each internal degree-two vertex passes its index unchanged. This is a declared finite allowed graph embedded in X6, not a claim that the real native graph excludes other moves.

Use one D-dimensional bond (b bits) along each unit edge; put index y on AB, z on BC, x on CA, all in Z/DZ. Each terminal has N=D|S|=2^(b+k) external labels (u,s) in (Z/DZ) x S. A local tensor has entry 1 if its two incident indices and external label satisfy the following test, 0 otherwise:
- A(x,y): a=(y-x) mod D belongs to S, output (x,a).
- B(y,z): c=(z-y) mod D belongs to S, output (y-c mod D,c).
- C(z,x): (z-x) mod D=2d for a d in S, output (x,d). The d is unique because 2d<D.
All assignments satisfying the tests obey a+c=2d as ordinary integers: both sides in [0,D-1] and congruent modulo D. The no-progression property forces a=c=d=s. Consequently y=x+s, z=x+2s modulo D, and every terminal emits (x,s). Conversely each (x,s) produces exactly one internal assignment, including both edges of each arc. Thus contraction equals the complete three-port N-label diagonal, entry 1 on each common label, 0 off diagonal over every F. There is no cancellation, no external selector, and no assumed target lemma.

Transport cost W_cycle=6b bits*unit-length, with one branch. Every connected tree subgraph of this same cycle spanning A,B,C has length at least 4 (it contains the two arcs joining three terminals along a connected path; the longest terminal-free removable arc has two edges). A tree of length 4 exists. The Nov27 tree theorem gives exact minimum single-branch transport W_tree=4m with m=b+k for the best spanning tree. Hence the cyclic construction is strictly better whenever 2k>b. Example b=8,k=5,m=13: W_cycle=48, W_tree=52, saving 4 bit-length units or 1/13 of tree cost. Along unbounded b, k/b tends to log_3 2, so the ratio tends to 6/[4(1+log_3 2)] about 0.9197. This is an upper bound on optimal cyclic cost, not its exact optimum.

## 2. Lower bound and exact finite author check

The maximum weighted terminal-cut packing L for this six-cycle is 3: each of the three terminal singleton cuts crosses two distinct unit edges, giving weight 1 each; every nontrivial terminal cut crosses at least two cycle edges, hence summing per-edge capacity constraints yields 2L<=6. The Nov26 general cut bound yields W>=3m for a one-branch network. For b=8,k=5: 39<=W_opt<=48<52. No assumption of optimality of the construction.

Executed exact integer enumeration with b=8: generated all 32 base-3 digit {0,1} values (maximum 121); iterated 256*32*32=262144 triples (x,a,c), computed y=(x+a)%256,z=(y+c)%256 and looked up d in S with 2d=(z-x)%256. Observed exactly 8192 accepted triples and 0 with a,c,d unequal. This covers every admissible internal assignment since A,B already require a,c in S and C is deterministic. Reproduction pseudocode:
S=[sum(((i>>j)&1)*3**j for j in range(5)) for i in range(32)]
twice={2*d:d for d in S}
accepted=bad=0
for x in range(256):
  for a in S:
    for c in S:
      y=(x+a)%256; z=(y+c)%256
      d=twice.get((z-x)%256)
      if d is not None:
        accepted+=1; bad+=int(not(a==c==d))
assert (accepted,bad)==(8192,0)

## 3. Resource and future-observation boundary

The saving is in static bond-dimension times path length, with unrestricted local tensors, not a measured runtime/energy/storage saving. All local tests admit the explicit finite residue and ternary membership description above, but computation, representation, memory, and recovery must be charged before a full-cost improvement claim. Contraction is a unique extension of the external label on diagonal support. Therefore the full internal ordered arc assignment can be recovered from (x,s) by the displayed formulas; it is not permissible to erase arbitrary path histories or subsequent state mutations by invoking this static property. The next discriminating unit is to compare this fixed static reconstruction with the actual typed triadic BRC operation/future same language and cost model, or construct an exact counterexample to such a bridge; separately investigate the gap [39,48] in the external model. No native execution was performed, no new custom axioms or proof holes introduced, no Lean run.

Handoff: retain author provenance, current independent review status, and prior task ownership. No formal Task, CLAIM, Result, Review or Activity association is asserted from this note; authorized Driver/owner should consume the candidate in the existing integration scope when appropriate; current private role binding not demonstrated. 
