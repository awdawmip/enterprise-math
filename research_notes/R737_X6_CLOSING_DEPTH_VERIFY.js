'use strict';
// R737: exhaustive signed X6 coordinate-loop N-BRC checker (integer arithmetic).
const assert=(ok,msg)=>{if(!ok)throw Error(msg);};
const moves=[[0,1],[0,-1],[1,1],[1,-1],[2,1],[2,-1]];
const edges=[[0,1],[0,2],[1,2]];
const key=x=>JSON.stringify(x);
const all=[];
function permutations(rest,word){if(!rest.length){all.push(word);return;}
 for(let i=0;i<rest.length;i++)permutations(rest.slice(0,i).concat(rest.slice(i+1)),word.concat([rest[i]]));}
permutations(moves,[]);
const nb=w=>w.every(([i,s],t)=>t===0||i!==w[t-1][0]);
function obs(w){
 const x=[0,0,0],seen=[0,0,0],Q=[0,0,0],J=[0,0,0],K=[null,null,null];
 for(const [i,s] of w){
  if(!seen[i])Q[i]=s;
  for(let z=0;z<3;z++)if(i===edges[z][1])J[z]+=x[edges[z][0]]*s;
  x[i]+=s;seen[i]++;
  if(seen[i]===2)K[i]=x.reduce((a,v,j)=>a+(i===j?0:v),0);
 }
 assert(x.every(a=>a===0),'nonclosed');
 return {Q,J,K};
}
function cubic(w){
 const T=Array(27).fill(0);
 for(let a=0;a<6;a++)for(let b=a+1;b<6;b++)for(let c=b+1;c<6;c++){
  const [i,s]=w[a],[j,t]=w[b],[k,u]=w[c];
  T[9*i+3*j+k]+=s*t*u;
 }
 return T;
}
const contraction=T=>[0,1,2].map(i=>[0,1,2].filter(j=>i!==j).reduce((v,j)=>v+T[9*i+3*i+j],0));
const omega=T=>T[5]-T[7]-T[11]+T[15]+T[19]-T[21];
function census(ws,fn){const d=new Map();for(const w of ws){const k=key(fn(w));d.set(k,(d.get(k)||0)+1);}
 const sizes={};for(const v of d.values())sizes[v]=(sizes[v]||0)+1;
 return {classes:d.size,max:Math.max(...d.values()),sizes};
}
const W=all.filter(nb);
assert(all.length===720&&W.length===240,'population');
for(const w of all){const T=cubic(w);assert(key(contraction(T))===key(obs(w).K),'tensor K identity');assert(omega(T)===0,'alternating cubic');}
const stats={
 QJ:census(W,w=>{const v=obs(w);return [v.Q,v.J];}),
 QJ_K0:census(W,w=>{const v=obs(w);return [v.Q,v.J,v.K[0]];}),
 QJ_K01:census(W,w=>{const v=obs(w);return [v.Q,v.J,v.K[0],v.K[1]];}),
 QJK:census(W,w=>{const v=obs(w);return [v.Q,v.J,v.K];}),
 JK:census(W,w=>{const v=obs(w);return [v.J,v.K];}),
 T3_NB:census(W,cubic),
 T3_ALL:census(all,cubic)
};
const expected={
 QJ:{classes:192,max:2,sizes:{1:144,2:48}},
 QJ_K0:{classes:224,max:2,sizes:{1:208,2:16}},
 QJ_K01:{classes:240,max:1,sizes:{1:240}},
 QJK:{classes:240,max:1,sizes:{1:240}},
 JK:{classes:228,max:2,sizes:{1:216,2:12}},
 T3_NB:{classes:240,max:1,sizes:{1:240}},
 T3_ALL:{classes:379,max:48,sizes:{1:240,2:96,4:24,8:18,48:1}}
};
assert(key(stats)===key(expected),'fiber census '+key(stats));
for(let i=0;i<3;i++){let d=census(W,w=>{const o=obs(w);return [o.Q,o.J,o.K[i]];});
 assert(d.classes===224&&d.max===2,'one K component');}
for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){let d=census(W,w=>{const o=obs(w);return [o.Q,o.J,o.K[i],o.K[j]];});
 assert(d.classes===240&&d.max===1,'two K components');}
function perms6(rest,word,out){if(!rest.length){out.push(word);return;}for(let i=0;i<rest.length;i++)perms6(rest.slice(0,i).concat(rest.slice(i+1)),word.concat(rest[i]),out);}
function obs6(w,active){
 const x=Array(6).fill(0),seen=Array(6).fill(0),q=Array(6).fill(0),k=Array(6).fill(null),J=Array.from({length:6},()=>Array(6).fill(0));
 for(const [a,s] of w){if(!seen[a])q[a]=s;
  for(let i=0;i<a;i++)J[i][a]+=x[i]*s;
  x[a]+=s;seen[a]++;if(seen[a]===2)k[a]=active.filter(j=>j!==a).reduce((v,j)=>v+x[j],0);}
 return {q,k,J};
}
const sym=[];perms6([0,1,2,3,4,5],[],sym);
let covariance=0;
for(const w of [W[0],W[10],W[55],W[120],W[239]])for(const p of sym){
 const active=[p[0],p[1],p[2]], mapped=w.map(([i,s])=>[p[i],s]), o=obs(w),f=obs6(mapped,active);
 for(let i=0;i<3;i++){assert(f.q[p[i]]===o.Q[i]&&f.k[p[i]]===o.K[i],'S6 Q,K transport');
 for(let j=i+1;j<3;j++){const z=o.J[edges.findIndex(([a,b])=>a===i&&b===j)];
 assert((p[i]<p[j]?f.J[p[i]][p[j]]:-f.J[p[j]][p[i]])===z,'S6 J transport');}}
 covariance++;
}
const a=[[0,1],[1,1],[2,1],[0,-1],[2,-1],[1,-1]];
const b=[[0,1],[2,1],[1,1],[0,-1],[1,-1],[2,-1]];
const A=obs(a),B=obs(b);
assert(key(A.Q)===key(B.Q)&&key(A.J)===key(B.J)&&key(A.K)!==key(B.K),'R735 repair witness');
console.log(JSON.stringify({schema:'ENTERPRISE_MATH_R737_X6_CLOSING_DEPTH_EXACT_V1',date:'2026-11-12',
 frozen_science:'a72226e2430ffa4786321ac86e7f0c599d5f0389',
 scope:'three native axes, six signed steps once, nonbacktracking 240 of 720',
 total_words:720,nb_words:240,observer_statistics:stats,covariance_checks:covariance,
 collision:{word_a:a,word_b:b,Q:A.Q,J:A.J,K_a:A.K,K_b:B.K},
 cubic_alternating_all_720_zero:true,
 check:'R737_X6_CLOSING_DEPTH_CUBIC_EXACT_PASS',native_event_verified:false},null,2));
