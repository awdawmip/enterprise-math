// Stage440-B: exact positive-unit X6 two-source implicit quotient ranking.
// Node.js: node REPRO_STAGE440B.js (uses no dependencies).
"use strict";
function stage440() {
  const check=(v,msg)=>{if(!v)throw Error("CHECK_FAIL "+msg);};
  const cases=[[6,1,1],[7,2,1],[8,2,2],[8,3,1]];
  function parameters(L,a,b) {
    check(Number.isInteger(L)&&Number.isInteger(a)&&Number.isInteger(b)&&1<=b&&b<=a&&L>=a+4,"bounds");
    const s=Math.max(b,a-1),d=a-s,h=L-a-2;
    return {L,a,b,s,d,h,q:(d+1)*(s+1)+s*s,N:L-2};
  }
  function classes(x,y,t) {
    const i=x<t.L-t.a?0:x-(t.L-t.a)+1;
    const j=y<t.L-t.s?0:y-(t.L-t.s)+1;
    return [i,j];
  }
  function rank(i,j,t) {
    const {a,s,d}=t;
    check(i>=0&&i<=a&&j>=0&&j<=s&&!(i>d&&j===i-d),"invalid class");
    const base=i<=d?i*(s+1):(d+1)*(s+1)+(i-d-1)*s;
    const local=i<=d?j:j-(j>i-d?1:0);
    return base+local;
  }
  function unrank(r,t) {
    const {s,d}=t;check(Number.isInteger(r)&&r>=0&&r<t.q,"rank bounds");
    const first=(d+1)*(s+1);
    if(r<first)return [Math.floor(r/(s+1)),r%(s+1)];
    const i=d+1+Math.floor((r-first)/s),local=(r-first)%s;
    return [i,local+(local>=i-d?1:0)];
  }
  function mass(i,j,t) {
    const {h,d}=t;
    if(i===0&&j===0)return h*(h+d-1);
    if(i===0)return h;
    if(j===0)return h+d-(i<=d?1:0);
    return 1;
  }
  function unrankHistory(r,z,t) {
    const [i,j]=unrank(r,t),m=mass(i,j,t),{L,a,s,d,h}=t;
    check(Number.isInteger(z)&&z>=0&&z<m,"within-class index");
    const xv=i===0?null:L-a+i-1,yv=j===0?null:L-s+j-1;
    if(i===0&&j===0) {
      const w=h+d-1,xi=Math.floor(z/w);
      let yi=z%w;
      if(yi>=xi)yi++;
      return [2+xi,2+yi];
    }
    if(i===0)return [2+z,yv];
    if(j===0) {
      let yi=z;
      const excluded=xv-2;
      if(i<=d&&yi>=excluded)yi++;
      return [xv,2+yi];
    }
    return [xv,yv];
  }
  function word(L,j){const x=Array(L).fill(0);x[j-1]=1;return x;}
  function v(word){const q=Array(6).fill(0);for(const z of word)q[Math.floor(z/2)]+=z%2?-1:1;return q;}
  function J(word){const h=Array(144).fill(0);for(let i=1;i<word.length;i++)h[12*word[i-1]+word[i]]++;return h;}
  function K(P,Q){let k=0;for(let i=0;i<Math.min(P.length,Q.length);i++)k+=P[i]===Q[i]?1:0;return k;}
  function obs(P,Q){return JSON.stringify([P.length,Q.length,v(P),v(Q),J(P),J(Q),K(P,Q)]);}
  let observationChecks=0,equalFullFutures=0,separatingFutures=0;
  let shortestWitness=null;
  function compareFuture(X,Y,t) {
    const [x,y]=X,[u,z]=Y;
    function walk(P,Q,R,S,pP,pQ,rP,rQ,path) {
      observationChecks++;
      if(obs(P,Q)!==obs(R,S))return {path:path.slice(),K_left:K(P,Q),K_right:K(R,S)};
      if(pP<t.a&&P.length>1){const r=walk(P.slice(0,-1),Q,R.slice(0,-1),S,pP+1,pQ,rP,rQ,path.concat("P:POP"));if(r)return r;}
      if(pQ<t.b&&Q.length>1){const r=walk(P,Q.slice(0,-1),R,S.slice(0,-1),pP,pQ+1,rP,rQ,path.concat("Q:POP"));if(r)return r;}
      if(rP<1){for(let dir=0;dir<12;dir++){const r=walk(P.concat(dir),Q,R.concat(dir),S,pP,pQ,rP+1,rQ,path.concat("P:APPEND("+dir+")"));if(r)return r;}}
      if(rQ<1){for(let dir=0;dir<12;dir++){const r=walk(P,Q.concat(dir),R,S.concat(dir),pP,pQ,rP,rQ+1,path.concat("Q:APPEND("+dir+")"));if(r)return r;}}
      return null;
    }
    return walk(word(t.L,x),word(t.L,y),word(t.L,u),word(t.L,z),0,0,0,0,[]);
  }
  const summaries=[];
  for(const [L,a,b] of cases) {
    const t=parameters(L,a,b),groups=Array.from({length:t.q},()=>[]);
    for(let x=2;x<L;x++)for(let y=2;y<L;y++)if(x!==y){
      const [i,j]=classes(x,y,t),r=rank(i,j,t);
      const c=unrank(r,t);check(c[0]===i&&c[1]===j,"rank roundtrip");
      groups[r].push([x,y]);
      check(K(word(L,x),word(L,y))===L-2,"K fiber");
    }
    check(groups.every(g=>g.length>0),"all classes realized");
    let sum=0,eq=0,sep=0;
    for(let r=0;r<t.q;r++){
      const [i,j]=unrank(r,t),arr=groups[r],M=mass(i,j,t);
      check(arr.length===M,"mass count "+[L,a,b,r,M,arr.length]);
      const rebuilt=new Set();
      for(let z=0;z<M;z++)rebuilt.add(unrankHistory(r,z,t).join(":"));
      check(rebuilt.size===M&&arr.every(p=>rebuilt.has(p.join(":"))),"lossless unrank");
      sum+=M;
      for(let j2=1;j2<arr.length;j2++){
        const fail=compareFuture(arr[0],arr[j2],t);
        check(fail===null,"same class distinguishable "+[L,a,b,r]);
        eq++;equalFullFutures++;
      }
    }
    check(sum===t.N*(t.N-1),"population total");
    for(let r=0;r<t.q;r++)for(let r2=r+1;r2<t.q;r2++){
      const witness=compareFuture(groups[r][0],groups[r2][0],t);
      check(witness!==null,"distinct class future equivalent "+[L,a,b,r,r2]);
      sep++;separatingFutures++;
      if(!shortestWitness||witness.path.length<shortestWitness.path.length)shortestWitness={L,a,b,left:groups[r][0],right:groups[r2][0],...witness};
    }
    summaries.push({L,a,b,q:t.q,history_pairs:t.N*(t.N-1),population_sum:sum,within_class_future_checks:eq,between_class_future_witnesses:sep,largest_class:Math.max(...groups.map(g=>g.length))});
  }
  let algebraicParameterCases=0;
  for(let L=6;L<=16;L++)for(let a=1;a<=L-4;a++)for(let b=1;b<=a;b++) {
    const t=parameters(L,a,b),groups=Array.from({length:t.q},()=>0);
    for(let x=2;x<L;x++)for(let y=2;y<L;y++)if(x!==y){const [i,j]=classes(x,y,t);groups[rank(i,j,t)]++;}
    for(let r=0;r<t.q;r++){const [i,j]=unrank(r,t);check(groups[r]===mass(i,j,t),"longer grid count");}
    check(groups.reduce((u,z)=>u+z,0)===(L-2)*(L-3),"longer grid sum");
    algebraicParameterCases++;
  }
  return {marker:"STAGE440B_TWO_SOURCE_IMPLICIT_RANK_EXACT_PASS",cases:summaries,algebraic_parameter_cases:algebraicParameterCases,verified_full_future_equal_pairs:equalFullFutures,verified_full_future_distinct_class_witnesses:separatingFutures,full_observation_prefix_comparisons:observationChecks,append_direction_count:12,smallest_witness:shortestWitness,arithmetic:"exact safe JS integers on tested L<=16"};
}
const executed=stage440();
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(executed)+"\n");
executed;
