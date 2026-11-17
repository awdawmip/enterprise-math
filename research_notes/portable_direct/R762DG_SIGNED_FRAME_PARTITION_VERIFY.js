'use strict';
const mod=(x,q)=>((x%q)+q)%q;
const gcd=(a,b)=>b===0?a:gcd(b,a%b);
function experiment(n,q,patterns){
 const total=q**(n-1); let invisible=0,checks=0;
 for(let a=0;a<total;a++){
  let z=a; const u=Array(n).fill(0);for(let i=1;i<n;i++){u[i]=z%q;z=Math.floor(z/q);}
  let safe=true;
  for(const s of patterns){
   for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)for(let k=j+1;k<n;k++){
    checks++;
    const v=s[i]*s[j]*(u[j]-u[i])+s[j]*s[k]*(u[k]-u[j])+s[k]*s[i]*(u[i]-u[k]);
    if(mod(v,q)!==0) safe=false;
   }
  }
  if(safe)invisible++;
 }
 const parents=Array.from({length:n},(_,i)=>i);
 function find(i){while(parents[i]!==i)i=parents[i];return i;}
 function link(i,j){const a=find(i),b=find(j);parents[a]=b;}
 for(const s of patterns){ if(s.every(x=>x===s[0]))continue; for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(s[i]===s[j])link(i,j); }
 const components=new Set(Array.from({length:n},(_,i)=>find(i))).size;
 const prediction=q**(components-1)*gcd(q,2)**(n-components);
 if(invisible!==prediction)throw Error(JSON.stringify({n,q,invisible,prediction,components}));
 return {n,q,pattern_count:patterns.length,components,invisible,prediction,checks};
}
function run(){
 const rows=[];
 for(const n of [4,5])for(const q of [2,3,4,5]){
  const id=Array(n).fill(1),flip0=Array(n).fill(1),flip1=Array(n).fill(1),complement=Array(n).fill(-1);
  flip0[0]=-1;flip1[1]=-1;complement[0]=1;
  for(const p of [[id],[id,flip0],[id,flip0,complement],[id,flip0,flip1]])rows.push(experiment(n,q,p));
 }
 return {status:'PASS',arithmetic:'exact_integer',q_domain:[2,3,4,5],n_domain:[4,5],scenarios_per_pair:4,rows,total_checks:rows.reduce((s,r)=>s+r.checks,0),status_of_universal_claim:'PROVED_IN_THEOREM_NOT_BY_FINITE_ENUMERATION'};
}
if(require.main===module) console.log(JSON.stringify(run(),null,2));
module.exports={experiment,run};
