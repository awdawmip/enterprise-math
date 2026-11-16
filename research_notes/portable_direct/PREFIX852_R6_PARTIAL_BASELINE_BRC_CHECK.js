/* PREFIX852_R6_PARTIAL_BASELINE_BRC_CHECK.js
Exact-integer exhaustive checker. Node.js: node PREFIX852_R6_PARTIAL_BASELINE_BRC_CHECK.js */
(function(){
"use strict";
const cases=[];let signedAssignments=0,divisorChecks=0,directCases=0;
function pop(x){let v=0;while(x){v+=x&1;x>>=1;}return v;}
function choose(n,k){let x=1;for(let i=1;i<=k;i++)x=x*(n-i+1)/i;return Math.round(x);}
function differenceSet(p,J,r){
 const N=1<<p,mark=new Uint8Array(N),K=((1<<p)-1)^J;
 function visit(i,v,h,used){
  if(h>2*r)return;
  if(i===p){signedAssignments++;if(used&&v!==0)mark[Math.abs(v)]=1;return;}
  visit(i+1,v,h,used);
  const a=(K>>i)&1;
  if(h+a<=2*r){visit(i+1,v+(1<<i),h+a,true);visit(i+1,v-(1<<i),h+a,true);}
 }
 visit(0,0,0,false);return mark;
}
function calc(p,J,r){
 const N=1<<p,D=differenceSet(p,J,r),bad={};let qstar=null;
 for(let q=3;q<=N+1;q+=2){
  let d=0;for(let k=q;k<N;k+=q){divisorChecks++;if(D[k]){d=k;break;}}
  if(!d){qstar=q;break;}bad[q]=d;
 }
 if(qstar===null)throw Error("N+1 guarantee");
 let s=pop(J),n=p-s,v=0;
 for(let j=0;j<=Math.min(r,n);j++)v+=choose(n,j);
 v*=1<<s;
 if(qstar<v)throw Error("volume bound");
 if(2*r>=n&&qstar!==N+1)throw Error("saturation");
 if(r===0&&J>0&&(J&(J+1))===0&&qstar!==J+2)throw Error("contiguous");
 return {p,J,r,unknown_indices:Array.from({length:p},(_,i)=>i).filter(i=>(J>>i)&1),q_star:qstar,bits:Math.ceil(Math.log2(qstar)),volume:v,differences:D.reduce((s,x)=>s+x,0),excluded_odd_witnesses:bad};
}
function direct(p,J,r,q){
 const K=Array.from({length:p},(_,i)=>i).filter(i=>!((J>>i)&1));
 for(let z=0;z<(1<<K.length);z++){
  let a=0;K.forEach((i,j)=>{if((z>>j)&1)a|=1<<i;});
  const seen=new Set();
  for(let x=0;x<(1<<p);x++){
   if(pop((x^a)&~J&((1<<p)-1))>r)continue;
   if(seen.has(x%q))return false;
   seen.add(x%q);
  }
 }
 return true;
}
const schemes=[["known",p=>0],["low",p=>1],["middle",p=>1<<Math.floor(p/2)],["high",p=>1<<(p-1)],["low2",p=>3],["high2",p=>3<<(p-2)]];
for(let p=2;p<=9;p++){
 const used=new Set();
 for(const [name,fn]of schemes)for(const r of [0,1,2]){
  const J=fn(p);if(J===0&&r===0)continue;
  const key=[p,J,r].join("/");if(used.has(key))continue;used.add(key);
  const t=calc(p,J,r);t.scheme=name;
  if(p<=6){if(!direct(p,J,r,t.q_star))throw Error("direct optimal "+key);
   for(let q=3;q<t.q_star;q+=2)if(direct(p,J,r,q))throw Error("direct lower "+key+" q="+q);
   directCases++;}
  cases.push(t);
 }
}
const lookup=(p,J,r)=>cases.find(t=>t.p===p&&t.J===J&&t.r===r)?.q_star;
if(lookup(6,1,1)!==43||lookup(6,8,1)!==27||lookup(6,32,1)!==43)throw Error("illustration mismatch");
const result={schema:"ENTERPRISE_MATH_PREFIX852_EXACT_CHECK_V1",scientific_input:"f42f2906d77f24085c123f3ccfe9667d41caa96d",model:"named binary BRC Q-only modular observer; c_t powers of 2; uniform old outside-J bits; <=r lost one-bit updates; odd q>=3",status:"ALL_EXACT_ASSERTIONS_PASSED",parameter_cases:cases.length,signed_ternary_leaves:signedAssignments,divisor_checks:divisorChecks,direct_oracle_cases:directCases,results:cases};
if(typeof process!=="undefined"&&process.stdout)process.stdout.write(JSON.stringify(result,null,2)+"\n");
return result;
})()
