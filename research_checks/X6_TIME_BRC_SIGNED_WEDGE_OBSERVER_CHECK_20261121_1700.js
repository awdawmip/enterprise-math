"use strict";
// X6 Unit238: exact native two-step signed bivector observer; original source-possible graph.
// Execute: node research_checks/X6_TIME_BRC_SIGNED_WEDGE_OBSERVER_CHECK_20261121_1700.js
function assert(x,m){if(!x)throw Error(m);}
const E=Array.from({length:3},(_,i)=>Array.from({length:6},(_,j)=>+(i===j)));
const a=[E[0],E[1],E[2],E[0].map(x=>-x),E[1].map(x=>-x),E[2].map(x=>-x)];
const mod6=x=>((x%6)+6)%6;
const neg=x=>x.map(y=>-y);
const add=(x,y)=>x.map((v,i)=>v+y[i]);
const eq=(x,y)=>x.length===y.length&&x.every((v,i)=>v===y[i]);
function wedge(u,v){const out=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)out.push(u[i]*v[j]-u[j]*v[i]);return out;}
function fact(n){let p=1;for(let i=2;i<=n;i++)p*=i;return p;}
function comb(n,k){return fact(n)/(fact(k)*fact(n-k));}
function perms(x){if(x.length===0)return [[]];let out=[];for(let i=0;i<x.length;i++)for(let t of perms(x.filter((_,j)=>i!==j)))out.push([x[i],...t]);return out;}
function permute(v,p){const z=Array(6).fill(0);for(let i=0;i<6;i++)z[p[i]]=v[i];return z;}
function main(){
 let assertions=0, native_edges=0, perm_checks=0, reverse_checks=0;
 const check=(x,m)=>{assertions++;assert(x,m)};
 // The basis bivectors are 01,12,02 (the latter two appear in slots 5 and 1).
 const indices=[0,5,1];
 for(const eps of [-1,1])for(let r=0;r<6;r++)for(const branch of [0,1]){
   const u=a[r],v=a[mod6(r+eps)];
   const s1=branch?v:neg(u),s2=branch?neg(u):v;
   const target=wedge(u,v).map(z=>z*(branch?1:-1));
   check(eq(wedge(s1,s2),target),"native order wedge");
   check(eq(wedge(neg(s2),neg(s1)),target.map(x=>-x)),"time reversal");
   reverse_checks++;
   for(let p of perms([0,1,2,3,4,5])){
     check(eq(wedge(permute(s1,p),permute(s2,p)),targetFromPermutation(target,p)),"S6 covariance");
     perm_checks++;
   }
 }
 function targetFromPermutation(w,p){
   const M=Array(6).fill(0).map(()=>Array(6).fill(0));let q=0;
   for(let i=0;i<6;i++)for(let j=i+1;j<6;j++){M[i][j]=w[q];M[j][i]=-w[q];q++;}
   const z=[];for(let i=0;i<6;i++)for(let j=i+1;j<6;j++)z.push(M[p.indexOf(i)][p.indexOf(j)]);
   return z;
 }
 const tables=[];
 for(let W=1;W<=3;W++){
   const L=6*W, M=1<<L, bins=new Map(), seen=W<=2?new Set():null;
   let paths=0, valid_root=0;
   for(let eps of [-1,1])for(let mask=0;mask<M;mask++){
     let omega=Array(15).fill(0), hist=Array(12).fill(0), trace=[],r=0;
     for(let t=0;t<L;t++){
       let u=a[r], next=mod6(r+eps),v=a[next],branch=(mask>>t)&1;
       let s1=branch?v:neg(u),s2=branch?neg(u):v;
       let mid=add(u,s1),end=add(mid,s2);
       check(eq(end,v),"correct endpoint");
       check(eq(mid,branch?add(u,v):Array(6).fill(0)),"correct gate");
       check(s1.reduce((s,x)=>s+Math.abs(x),0)===1 && s2.reduce((s,x)=>s+Math.abs(x),0)===1,"primitive steps");
       for(let s of [s1,s2]){let i=s.findIndex(x=>x!==0);hist[2*i+(s[i]<0?1:0)]++;}
       let z=wedge(s1,s2);
       for(let i=0;i<15;i++)omega[i]+=z[i];
       if(seen)trace.push(mid.join(","),v.join(","));
       r=next;native_edges+=2;
     }
     check(r===0,"closed shell circuit");
     for(let i=0;i<3;i++){check(hist[2*i]===2*W,"positive axis histogram");check(hist[2*i+1]===2*W,"negative axis histogram");}
     for(let i=6;i<12;i++)check(hist[i]===0,"omitted axis histogram");
     for(let i=0;i<15;i++)if(!indices.includes(i))check(omega[i]===0,"bivector support in three-axis slice");
     let c=indices.map(i=>omega[i]);
     for(let ci of c)check(ci%2===0 && Math.abs(ci)<=2*W,"bivector coordinate parity/range");
     const key=c.join(",");
     bins.set(key,(bins.get(key)||0)+1);
     if(seen){const id=trace.join(";");check(!seen.has(id),"unique chronological Cell history");seen.add(id);}
     paths++;if(mask===M-1)valid_root++;
   }
   check(paths===2**(L+1),"population size");
   check(bins.size===(2*W+1)**3,"wedge image cardinality");
   if(seen)check(seen.size===paths,"complete Cell trace multiplicity");
   let max=0, sum=0;
   for(let c0=-2*W;c0<=2*W;c0+=2)for(let c1=-2*W;c1<=2*W;c1+=2)for(let c2=-2*W;c2<=2*W;c2+=2){
     let k=[c0,c1,c2].map(c=>W+c/2);
     let expected=2*k.reduce((p,x)=>p*comb(2*W,x),1);
     let got=bins.get([c0,c1,c2].join(","))||0;
     check(got===expected,"exact fiber multiplicity");
     max=Math.max(max,got);sum+=got;
   }
   check(sum===paths,"total fiber census");
   check(max===2*(comb(2*W,W)**3),"maximum fiber bound");
   check(valid_root===2,"all-OUTER qualified count");
   tables.push({W,all_ordered_histories:paths,distinct_wedge_values:bins.size,max_fiber:max,sharp_uniform_repair_bits:Math.ceil(Math.log2(max)),all_outer_qualified:valid_root});
 }
 return {schema:"X6_NATIVE_SIGNED_WEDGE_OBSERVER_EXACT_CERT_V1",unit:"Unit238",frozen_source:"a72226e2430ffa4786321ac86e7f0c599d5f0389",status:"AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED",assertions,failed_assertions:0,native_primitive_events_checked:native_edges,reverse_local_cases:reverse_checks,S6_covariance_cases:perm_checks,tables,not_executed:"R063 six-file native benchmark is separate; no physical Link/Port precision transport law established."};
}
if(typeof process!=="undefined"&&process.versions&&process.versions.node){console.log(JSON.stringify(main(),null,2));}
