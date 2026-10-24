"use strict";
// Exact BRC finite-label verifier. Node.js: node verify_two_step.js
// Mathematics is auxiliary probability; not a P000 native six-axis simulation.
const A=[{id:"alpha",m:7n,d:10n,w:[1n,1n,1n,7n]},
         {id:"beta",m:8n,d:11n,w:[1n,1n,1n,8n]}];
const E=[[0,1],[0,2],[0,3],[1,2]];
const GOOD=[3,5,9,6];
function assert(c,m){if(!c)throw Error(m)}
function pw(a,n){return a**BigInt(n)}
function den(x,y){return pw(10n,x)*pw(11n,y)}
function N(x,y){assert(x+y>=1,"closed form needs nonempty history");
  return pw(8n,x)*pw(9n,y)+3n*pw(2n,x+y)-pw(7n,x)*pw(8n,y)-7n;}
function inc(x,y,a){const m=a.m;
  return 7n*(m+2n)+3n*pw(7n,x)*pw(8n,y)
    -3n*(m+1n)*pw(2n,x+y)-2n*pw(8n,x)*pw(9n,y);}
function spectra(x,y,a){
  const m=a.m,small=(m+1n)*pw(2n,x+y);
  const D=[3n*(m+2n),2n*(m+2n),2n*(m+2n),
           3n*pw(7n,x)*pw(8n,y)];
  const C=[small,small,2n*pw(8n,x)*pw(9n,y),small];
  assert(D.reduce((u,v)=>u+v,0n)-C.reduce((u,v)=>u+v,0n)===inc(x,y,a),"spectrum equation");
  return {D,C};
}
function admissible(i,e){const [j,k]=E[e];
  return A.every(a=>a.w[i]<=a.w[j]+a.w[k]);}
function K0flow(x,y,a){
  assert(x+y===4,"expected level 4");
  const {D,C}=spectra(x,y,a);
  // Flow: 0 -> 01, 1 -> 12, 2 -> 02, 3 -> 03
  const edges=[0,3,1,2],usage=[0n,0n,0n,0n];
  for(let i=0;i<4;i++){assert(admissible(i,edges[i]),"spectral order");usage[edges[i]]+=D[i];}
  const L=C.map((c,i)=>c-usage[i]);
  assert(L.every(z=>z>0n),"strict flow slack");
  return {D:D.map(String),C:C.map(String),L:L.map(String),
    common_denominator:String(den(x,y)*a.d)};
}
function impossibleK0(x,y,a){
  assert(x+y===3,"expected level 3");
  assert(admissible(3,2)&&[0,1,3].every(e=>!admissible(3,e)),"only high edge allowed");
  const {D,C}=spectra(x,y,a);
  const gap=D[3]-C[2];assert(gap>0n,"strict cut");
  return {heavy_demand:String(D[3]),only_reachable_capacity:String(C[2]),gap:String(gap)};
}
function step(dp,a){
  const result=Array(16).fill(0n);
  for(let mask=0;mask<16;mask++)for(let i=0;i<4;i++)
    result[mask|(1<<i)]+=dp[mask]*a.w[i];
  return result;
}
function good(dp){return GOOD.reduce((s,m)=>s+dp[m],0n);}
function verify(){
  assert(N(2,0)===20n&&den(2,0)===100n,"base occupancy");
  const base=Object.fromEntries(A.map(a=>[a.id,String(inc(2,0,a))]));
  assert(base.alpha==="-14"&&base.beta==="-19","base signed increments");
  const level3={}; const cuts={};
  for(const [x,y] of [[3,0],[2,1]]){
    const key=x+","+y;
    level3[key]=Object.fromEntries(A.map(a=>[a.id,String(inc(x,y,a))]));
    cuts[key]=Object.fromEntries(A.map(a=>[a.id,impossibleK0(x,y,a)]));
    assert(A.every(a=>inc(x,y,a)<0n),"level 3 strict negativity");
  }
  const k0={};
  for(const [x,y] of [[4,0],[3,1],[2,2]])
    k0[x+","+y]=Object.fromEntries(A.map(a=>[a.id,K0flow(x,y,a)]));
  let dp=Array(16).fill(0n);dp[0]=1n;dp=step(step(dp,A[0]),A[0]);
  let nodes=[{x:2,y:0,dp}],words=0,next=0;
  for(let length=0;length<=10;length++){
    const grow=[];
    for(const node of nodes){
      const {x,y,dp}=node;
      assert(good(dp)===N(x,y),"support DP vs inclusion-exclusion");
      words++;
      for(const a of A){
        const np=step(dp,a),xx=x+(a.id==="alpha"?1:0), yy=y+(a.id==="beta"?1:0);
        assert(good(np)-a.d*good(dp)===inc(x,y,a),"independent increment identity");
        assert(inc(x,y,a)<0n,"strict negative at enumerated suffix");
        next++;
        if(length<10)grow.push({x:xx,y:yy,dp:np});
      }
    }
    nodes=grow;
  }
  assert(words===2047&&next===4094,"full word count");
  let grid=0;
  for(let x=2;x<=21;x++)for(let y=0;y<=20;y++)for(const a of A){
    assert(inc(x,y,a)<0n,"grid count sign");grid++;
  }
  assert(grid===840,"grid coverage");
  return {scope:"STRICTLY_POSITIVE_AUXILIARY_BRC_NOT_P000_NATIVE",q_alpha:"(1,1,1,7)/10",
    q_beta:"(1,1,1,8)/11",good_edges:E,base_history:"alpha alpha",base_occupancy:"1/5",
    base_increment_numerators:base,level3_increment_numerators:level3,
    strict_K0_cut_failures_at_level3:cuts,strict_K0_flows_at_level4:k0,
    all_suffix_words_length_0_through_10:words,independent_support_mask_next_actions:next,
    exact_count_grid_sign_checks:grid,proof:"K2\\K1 witness and all-future strict decrease use analytic induction and strict flows",
    status:"AUTHOR_VERIFIED_UNREVIEWED_NOT_ADMITTED"};
}
if(typeof process!=="undefined"&&process.stdout)
  process.stdout.write(JSON.stringify(verify(),null,2)+"\n");
