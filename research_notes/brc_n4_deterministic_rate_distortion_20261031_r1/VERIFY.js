"use strict";
// Exact integer arithmetic. Each single K-leaf has mass n/240.
// Conditional stage-three public probabilities use scale 160.
// Total variation between two scale-160 vectors equals L1/320.
const DATA={
  AU:{Q:[10,10],P:[9,11]},
  AV:{Q:[20,20],P:[5,5]},
  BU:{Q:[15,15],P:[3,27]},
  BV:{Q:[15,15],P:[30,30]}
};
const X=["AU_Q","AU_P","AV_Q","BU_Q","BU_P","BV_Q"];
const H=["AU","AV","BU","BV","AU1","BU1"];
const EXPECT={3:320,4:128,5:16,6:0}; // TV error units 1/640
const GROUPS={
  3:[[0,1],[3,4],[2,5]],
  4:[[0,1],[3,4],[2],[5]],
  5:[[0,1],[3],[4],[2],[5]],
  6:[[0],[1],[2],[3],[4],[5]]
};
function assert(c,msg){if(!c)throw Error(msg);}
function state(x){const a=x.split("_");return {s:a[0],b:a[1]};}
function j1scaled(x){
  const {s,b}=state(x),v=DATA[s][b], n=160*v[1], d=v[0]+v[1];
  assert(n%d===0,"fraction scale");return n/d;
}
function law(x,h,epsNum){
  const {s}=state(x), j1=j1scaled(x),out=[0,0,0,0,0,0];
  for(let j=0;j<2;j++){
    const mass=j===1?j1:160-j1;
    const decision=(h===s)||(h===s+"1"&&j===1);
    if(s!=="BU")out[decision?1:0]+=mass;
    else for(let z=0;z<2;z++){
      const wn=z===j?8-epsNum:epsNum;
      assert((mass*wn)%8===0,"nonintegral BU sensor mass");
      const idx=2+2*z+(decision?1:0);
      out[idx]+=(mass*wn)/8;
    }
  }
  assert(out.reduce((a,b)=>a+b,0)===160,"output not normalized");
  return out;
}
function l1(a,b){return a.reduce((s,x,i)=>s+Math.abs(x-b[i]),0);}
function* parts(a=[0]){
  if(a.length===X.length){yield a.slice();return;}
  for(let k=0;k<=Math.max(...a)+1;k++)yield* parts(a.concat(k));
}
function upper(epsNum,k){
  const groups=GROUPS[k];
  let worst=0;
  for(const h of H){
    for(const grp of groups){
      const avg=Array(6).fill(0);
      for(const i of grp){
        const p=law(X[i],h,epsNum);
        for(let j=0;j<6;j++)avg[j]+=p[j]*(2/grp.length);
      }
      for(const i of grp){
        const actual=law(X[i],h,epsNum).map(v=>2*v);
        worst=Math.max(worst,l1(actual,avg)); // TV with scale-320 distributions: L1/640
      }
    }
  }
  return worst;
}
function run(){
  for(const b of ["P","Q"]){
    let total=0;
    for(const s of ["AU","AV","BU","BV"]){
      const v=DATA[s][b];
      assert(v.every(t=>Number.isInteger(t)&&t>0),"not strictly positive");
      total+=2*(v[0]+v[1]);
    }
    assert(total===240,"P/Q law not normalized");
  }
  const lines=[];
  for(const e of [0,1,2,4]){
    const dist=X.map((x,i)=>X.map((y,j)=>Math.max(...H.map(h=>l1(law(x,h,e),law(y,h,e))))));
    assert(dist[0][1]===16,"AU TV not 1/20");
    assert(dist[3][4]===128,"BU TV not 2/5");
    for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){
      const s1=state(X[i]).s,s2=state(X[j]).s;
      if(s1!==s2)assert(dist[i][j]===320,"cross source not TV=1");
    }
    let count=0;
    const minLower={3:Infinity,4:Infinity,5:Infinity,6:Infinity};
    for(const p of parts()){
      count++;
      const used=Math.max(...p)+1;
      let maxdist=0;
      for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){
        if(p[i]===p[j])maxdist=Math.max(maxdist,dist[i][j]);
      }
      for(let k=used;k<=6;k++)minLower[k]=Math.min(minLower[k],maxdist);
    }
    assert(count===203,"wrong partition enumeration: "+count);
    for(const k of [3,4,5,6]){
      assert(minLower[k]===EXPECT[k],"lower mismatch K"+k+" got "+minLower[k]);
      assert(upper(e,k)===EXPECT[k],"upper mismatch K"+k+" got "+upper(e,k));
    }
    lines.push("epsilon="+e+"/8; partitions=203; exact minimax deterministic [K=3,4,5,6]=[1/2,1/5,1/40,0]; PASS");
  }
  return ["PASS_BRC_N4_DETERMINISTIC_RATE_DISTORTION_20261031",
    "Model: original 16 positive K-leaves per law; 6 distinct prepared rows; 6 lawful S23 policies.",
    ...lines,
    "Scope: exhaustive six-row deterministic collision bounds and explicit-code upper checks for six witnesses; analytic data processing extends upper to all legal S23/S2 policies and all real epsilon in [0,1/2].",
    "Class-preserving stochastic-code result is proved analytically; not inferred from finite enumeration."
  ].join("\n");
}
run();
