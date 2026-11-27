# R846 — Exponential exact two-anchor pendant Pareto frontier

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_AUXILIARY_INTEGER_CHECKED / NOT_REVIEWED.

Continuation of R845 (7473e8488b5c789621b6d39a156dd7f61a5161ca:research_notes/portable_direct/R845_MULTIANCHOR_PENDANT_RESIDUAL_FRONTIER.md). Frozen science a72226e2430ffa4786321ac86e7f0c599d5f0389 retained. P000 V5 and joint observer read at that pin; generated startup and two companion paths returned 404; global P000 V4 and ACTIVE worldview read at 6ffa7f77421a80f5230211808387c0800a34107f. Current normative and portable protocols read. Auxiliary positive certificate model, not a native BRC calculation. Existing lane activity RA-708BCC309CE076D8BB599B91; public own-session metadata verified, private execution authority not established. Current owner request r3-20261127-r846-running-read was QUEUED at the last observation before this calculation; no shared task mutation. No external priority/novelty assertion.

## 1. Theorem

For every integer m>=1 there exists an R845 conditional private Kraft scope with two anchor groups, 2m private labels and three fixed boundary labels, rational R=2, positive dyadic weights of O(m) bits each, and cap C=2m+2 (the R839 scope bound), whose exact Pareto frontier in the two residual coordinates contains at least 2^m distinct points. All these points obey P_h<3/2 at both anchors (safety eta=1/2) when the private labels are singleton pendant bundles with no other anchor loads. This is an output-size obstruction to explicit exact-frontier enumeration, not a lower bound on implicit representations or on every scalar optimization algorithm.

## 2. Construction

Index the paired labels by i=2,...,m+1; each group has one label from every pair. Fix boundary lengths (2,m+1,m+2). Put a_i=2^(-i-1), lambda=2^(-C-4), b_i=lambda*2^(-2i-3), identical in both groups. For length L, activity c_i(L)=b_i*2^(L+2)=lambda*2^(L-2i-1). At L=i and i+1 the activities are lambda*a_i and 2lambda*a_i. Define P_h=product of (1+c_i(L)) in group h and v_h=P_h-1. The private Kraft budget is B=1-2^(-2)-2^(-m-1)-2^(-m-2)=3 sum_i a_i. For each binary word choose one length i and one length i+1 in every pair, independently assigning the shorter length to either group. These assignments saturate Kraft exactly, have the same combined product P*=product_i (1+lambda*a_i)(1+2lambda*a_i), and common linear activity sum S*=3lambda sum_i a_i<3lambda/4.

## 3. Global optimality of every binary word, not merely within a subclass

Write S(L)=sum of all private activities and K(L)=sum of private Kraft terms. The scalar surrogate S+lambda K is separable. For each label, successive difference of c_i(L)+lambda*2^(-L) at L+1 minus L is
lambda*[2^(L-2i-1)-2^(-L-1)].
It is negative for L<i, zero for L=i, and positive for L>i. Hence its only minima are i,i+1. The nearest nonminimizing lengths i-1 and i+2 both have surplus (3/2)lambda*a_i; all other lengths have at least that surplus. For any feasible capped assignment,
S(L)-S* = [S(L)+lambda K(L)-(S*+lambda B)] + lambda(B-K(L)).
Both terms nonnegative. If any length is outside its two minimizers, the first term is at least (3/2)lambda*2^(-m-2)>=lambda*2^(-C). If K(L)<B, dyadic lattice gives B-K>=2^(-C). If neither holds, let n_i be the number of shorter lengths in pair i. Saturation implies sum_i(n_i-1)a_i=0, where coefficients are -1,0,1. The largest nonzero power of two exceeds the sum of all smaller powers in this finite range; thus every n_i=1. Consequently every assignment outside the binary family has S(L)>=S*+lambda*2^(-C).

For nonnegative x_j with sum S<=1/2, 1+S<=prod(1+x_j)<=1+S+S^2: elementary symmetric degree k is at most S^k/k!, hence remainder <=S^2/[2(1-S)]<=S^2. For the binary family S*<lambda and (S*)^2<lambda*2^(-C). Therefore P*<=1+S*+(S*)^2<1+S*+lambda*2^(-C)<=prod(1+c_j(L)) for every other feasible assignment (lower bound does not require a small S for those assignments). The 2^m words are exactly the minimizers of the combined product.

## 4. Distinctness and Pareto claim

In group 1 the linear sum is lambda times sum_i a_i plus lambda times a subset sum of the a_i. Different words give distinct subset sums separated by at least lambda*2^(-m-2). Every group sum is less than lambda/2; its product differs from 1+that sum by at most lambda^2, strictly less than the separation. Thus group-1 products are distinct. The group-2 product equals P*/P_1, so their strict orders are opposite. More generally, a feasible point weakly dominating any binary witness and strictly improving one coordinate would strictly decrease the combined positive product, contradicting global optimality. Subtracting one preserves all comparisons. Both group products are below 1+lambda+lambda^2<3/2. Boundary labels are fixed inputs to this conditional frontier; their other anchor costs are outside the claimed isolated two-group safety check. The input is O(m^2) bits including all weights; the lower bound is exponential in private-label count (at least 2^Omega(sqrt(input bits)) for this explicit encoding). Fixed two-group count alone does not make exact explicit output polynomial. R845 approximate frontier remains useful and is not contradicted.

## 5. Exact computation

Common denominator D=2^(C+4+2(m+1)+3) makes all activity factors integral numerators. Compare products with common denominators and Kraft sums on denominator 2^C. Exhaustive labeled feasible assignments for m=1..3, checking all global minima, and all binary witnesses for m=1..14, checking saturation, common product, distinctness, and safety. General theorem is analytical; no large m exhaustive search, end-to-end multi-anchor solver, native realization or independent review.

Actual output:
```json
{
  "exhaustiveInstances": 3,
  "feasibleAssignments": 117969,
  "minimizers": 14,
  "candidateInstances": 14,
  "candidateWitnesses": 32766,
  "distinctGroupProducts": 32766,
  "assertionFailures": 0
}
```

Reproduction (JavaScript BigInt):
```javascript
function replay(){
 const stats={exhaustiveInstances:0,feasibleAssignments:0,minimizers:0,candidateInstances:0,candidateWitnesses:0,distinctGroupProducts:0,assertionFailures:0};
 for(let m=1;m<=14;m++){
  const C=2*m+2,D=1n<<BigInt(C+4+2*(m+1)+3),cap=1n<<BigInt(C);
  const boundary=[2,m+1,m+2],budget=cap-boundary.reduce((s,l)=>s+(cap>>BigInt(l)),0n);
  const factors=Array.from({length:m},(_,j)=>Array.from({length:C+1},(_,l)=>D+(D>>BigInt(C+4+2*(j+2)+1-l))));
  let target=1n;for(let j=0;j<m;j++)target*=factors[j][j+2]*factors[j][j+3];
  const seen=new Set();for(let mask=0;mask<(1<<m);mask++){
   let p=1n,q=1n,k=0n;
   for(let j=0;j<m;j++){let l=j+2+((mask>>j)&1),r=2*(j+2)+1-l;p*=factors[j][l];q*=factors[j][r];k+=(cap>>BigInt(l))+(cap>>BigInt(r))}
   if(k!==budget||p*q!==target||2n*p>=3n*D**BigInt(m)||2n*q>=3n*D**BigInt(m))throw Error("candidate");
   seen.add(p.toString());stats.candidateWitnesses++;
  }
  if(seen.size!==(1<<m))throw Error("distinct");stats.distinctGroupProducts+=seen.size;stats.candidateInstances++;
  if(m<=3){
   let minima=0;const ls=[];function visit(j,k,p){
    if(j===2*m){stats.feasibleAssignments++;if(p<target)throw Error("smaller product");if(p===target){minima++;for(let i=0;i<m;i++)if(!((ls[i]===i+2&&ls[i+m]===i+3)||(ls[i]===i+3&&ls[i+m]===i+2)))throw Error("unexpected minimizer")}return}
    for(let l=0;l<=C;l++){let z=k+(cap>>BigInt(l));if(z+BigInt(2*m-j-1)>budget)continue;ls[j]=l;visit(j+1,z,p*factors[j%m][l]);}
   }visit(0,0n,1n);if(minima!==(1<<m))throw Error("minima");stats.minimizers+=minima;stats.exhaustiveInstances++;
  }
 }
 return stats;
}
console.log(JSON.stringify(replay(),null,2));
```

Original signed joint moments, road matrix, branch identities, ordered steps, multiplicities, provenance and common depth remain unchanged. The lower bound concerns the auxiliary certificate Pareto readout only. Next: integrate R845 approximate frontier with retained payment constraints in the end-to-end solver; investigate adaptive scalarizations/implicit Pareto representation under fixed reduced width, separating explicit enumeration from decision complexity. Full Port observer and native realization remain open.
