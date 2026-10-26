'use strict';
// EC41 exact positive labelled BRC counts. Node >= 16: node EC41_verify.js.
// For experiment [p,q] with denominator M, branch 0 counts under P,Q are p,q;
// branch 1 counts are M-p,M-q. Full ordered provenance h,z is retained at terminal.
function gcd(a,b){while(b){const t=a%b;a=b;b=t;}return Math.abs(a);}
function reduced(n,d){if(d<=0||n<0)throw Error('bad ratio');const g=gcd(n,d);return [n/g,d/g];}
function breaks(a,b,M){const s=new Map();
  for(const [n,d] of [[0,1],[1,1],...([a,b].flatMap(([p,q])=>[[p,q],[M-p,M-q]]))]){
    const r=reduced(n,d);s.set(r.join('/'),r);}
  return [...s.values()].sort((u,v)=>u[0]*v[1]-v[0]*u[1]);}
function gain([p,q],M,alpha,beta){return M*Math.min(alpha,beta)
  -Math.min(alpha*p,beta*q)-Math.min(alpha*(M-p),beta*(M-q));}
function sameProfile(a,b,M){return breaks(a,b,M).every(([n,d])=>gain(a,M,d,n)===gain(b,M,d,n));}
// Exhaustively enumerate all deterministic stage-one decisions for histories a,b
// and all 4 terminal decisions per history. Every behavioral policy is contained
// in the resulting convex occupation polytope, so linear minima occur here.
// Objective alpha*eP + beta*eQ + theta*C; theta=(Ga+Gb)/(2M);
// all totals below are scaled by 4M, hence exact integers.
function exhaustive(a,b,M,alpha,beta){
  const Ga=gain(a,M,alpha,beta),Gb=gain(b,M,alpha,beta),S=Ga+Gb;
  function contribution([p,q],action,mask){
    if(action===0)return 2*M*beta; // decide P; Q wrong
    if(action===1)return 2*M*alpha; // decide Q; P wrong
    let r=S;
    for(let z=0;z<2;z++){
      const P=z===0?p:M-p,Q=z===0?q:M-q;
      const decideQ=Boolean((mask>>z)&1);
      r+=2*(decideQ?alpha*P:beta*Q);}
    return r;}
  let full=Infinity,stat=Infinity,fullPolicies=0,statPolicies=0;
  for(let i=0;i<3;i++)for(let j=0;j<3;j++)
    for(let x=0;x<4;x++)for(let y=0;y<4;y++){
      const value=contribution(a,i,x)+contribution(b,j,y);
      full=Math.min(full,value);fullPolicies++;
      if(i===j){stat=Math.min(stat,value);statPolicies++;}}
  const delta=stat-full;
  if(delta!==Math.abs(Ga-Gb)||fullPolicies!==144||statPolicies!==48)
    throw Error('policy enumeration contradicts exact gain gap');
  const base=2*M*Math.min(alpha,beta);
  const Ca=M*Math.min(alpha,beta)-Ga,Cb=M*Math.min(alpha,beta)-Gb;
  if(full!==Math.min(base,2*Ca+S)+Math.min(base,2*Cb+S)||
    stat!==Math.min(2*base,2*Ca+2*Cb+2*S))
    throw Error('direct-primal and analytic certificate disagree');
  return {gapNumerator:delta,denominator:4*M,fullPolicies,statPolicies};}
function verify(){
  const M=4,experiments=[];
  for(let p=1;p<M;p++)for(let q=1;q<M;q++)experiments.push([p,q]);
  let pairs=0,safe=0,unsafe=0,breakpointChecks=0,deterministicPolicies=0,statPolicies=0;
  for(const a of experiments)for(const b of experiments){
    const eq=sameProfile(a,b,M);let mismatch=false;
    for(const [n,d] of breaks(a,b,M)){
      const G1=gain(a,M,d,n),G2=gain(b,M,d,n);
      if(G1<0||G2<0)throw Error('positive-branch Bayes gain negative');
      const v=exhaustive(a,b,M,d,n);
      mismatch ||= v.gapNumerator>0;
      deterministicPolicies+=v.fullPolicies;statPolicies+=v.statPolicies;breakpointChecks++;}
    if(eq===mismatch)throw Error('profile characterization failed');
    if(eq)safe++;else unsafe++;pairs++;}
  const examples={
    label_permutation_safe:{M:4,a:[3,1],b:[1,3],same_profile:sameProfile([3,1],[1,3],4),
       gap:exhaustive([3,1],[1,3],4,1,1)},
    ec40_gap:{M:4,a:[3,1],b:[2,2],gain_a:[2,4],gain_b:[0,4],
       theta:[2,8],gap:exhaustive([3,1],[2,2],4,1,1),
       fixed_C:'1/2',full_error_sum:'3/4',stat_error_sum:'7/8'},
    equal_TV_insufficient:{M:20,a:[15,5],b:[12,2],TV_a:'1/2',TV_b:'1/2',
       normal:[1,2],gain_a:[5,20],gain_b:[8,20],theta:[13,40],
       gap:exhaustive([15,5],[12,2],20,1,2)}
  };
  if(pairs!==81||safe!==21||unsafe!==60||breakpointChecks!==354||
    examples.label_permutation_safe.gap.gapNumerator!==0||
    examples.ec40_gap.gap.gapNumerator!==2||
    examples.equal_TV_insufficient.gap.gapNumerator!==3)
    throw Error('exhaustive family or witness failed');
  return {schema:'EM_R4_EC41_EXACT_BRC_BAYES_PROFILE_REPORT_V1',status:'PASS',
    model:'finite positive rational ordered-label BRC two-hypothesis decision tree',
    enumeration_scope:{denominator:M,strictly_positive_binary_experiments:experiments.length,
      ordered_pairs:pairs,same_Bayes_profile_pairs:safe,different_profile_pairs:unsafe,
      distinct_ratio_breakpoint_tests:breakpointChecks,
      deterministic_full_policy_evaluations:deterministicPolicies,
      deterministic_stat_policy_evaluations:statPolicies},
    examples,computation:'integer only; all first-stage deterministic actions and all terminal decision masks',
    scope_limits:['The universal proposition relies on the proof, not finite enumeration',
      'No native X6 heartbeat dynamics or physical residual attribution',
      'No formal task claim, independent review, or mathematical admission']};}
if(typeof module!=='undefined' && typeof require!=='undefined' && require.main===module)
  console.log(JSON.stringify(verify(),null,2));
