"use strict";
// EC49FWN: exact blind inversion of three CRT holes; Node.js, no dependencies.
const check=(v,s)=>{if(!v)throw Error(s)};
function defect(u,n){let ans=[];for(let a=0;a<n;a++){let count=0;for(let x=0;x<n;x++)if(u[x]!==u[(a-x+n)%n])count++;ans.push(count)}return ans}
function kap(z,q){let a=Array(q).fill(0);for(let x of z)for(let y of z)a[(x+y)%q]++;return a}
function construct(d,w,n,q,k){let s=[];for(let b=0;b<q;b++)for(let a=0;a<n;a++)s.push((q-6+k[b])*d[a]+2*w*(3-k[b]));return s}
function invert(s,n,q){
 let r=[];for(let b=0;b<q;b++)r.push(s.slice(b*n,(b+1)*n).reduce((x,y)=>x+y,0));
 let levels=[...new Set(r)].sort((a,b)=>a-b);check(levels.length>=2&&levels.length<=4,"row levels");
 let w2=levels.length===2?(levels[1]-levels[0])/6:Math.min(...levels.slice(1).map((v,i)=>(v-levels[i])/2));
 let w=Math.sqrt(w2);check(Number.isInteger(w)&&w>0,"weight");
 let hi=Math.max(...r),kmin=q===5?1:0;
 let k=r.map(v=>kmin+(hi-v)/(2*w2));check(k.every(Number.isInteger),"kappa");
 let z=[];for(let b=0;b<q;b++)if(k[b]%2)z.push(b*((q+1)/2)%q);
 z.sort((a,b)=>a-b);check(z.length===3,"holes");
 let mx=Math.max(...k),b=k.indexOf(mx),den=q-6+mx;check(den>0,"divisor");
 let d=s.slice(b*n,(b+1)*n).map(v=>(v-2*w*(3-mx))/den);check(d.every(Number.isInteger),"short spectrum");
 return {z,w,d,k}
}
function triples(q){let o=[];for(let a=0;a<q;a++)for(let b=a+1;b<q;b++)for(let c=b+1;c<q;c++)o.push([a,b,c]);return o}
function typ(k,q){let h=[0,0,0,0];for(let v of k){check(v>=0&&v<=3,"range");h[v]++}
 if(h[3]===3){check(q%3===0&&h[0]===q-3&&h[1]===0&&h[2]===0,"equilateral");return "equilateral"}
 if(h[3]===1){check(h[0]===q-5&&h[1]===2&&h[2]===2,"one AP");return "one_ap"}
 check(h[3]===0&&h[0]===q-6&&h[1]===3&&h[2]===3,"generic");return "generic"
}
function runAll(){
 let cases=[];
 for(let [n,q,maxMask] of [...[5,7,9,11,13,15,21,27].map(q=>[4,q,15]),[10,11,1023]]){
  let tt=triples(q),counts={generic:0,one_ap:0,equilateral:0},num=0,dc=0;
  for(let z of tt){
   let k=kap(z,q);counts[typ(k,q)]++;
   let parity=[];for(let b=0;b<q;b++)if(k[b]%2)parity.push(b*((q+1)/2)%q);
   parity.sort((a,b)=>a-b);check(JSON.stringify(parity)===JSON.stringify(z),"parity recovery");
   for(let mask=1;mask<=maxMask;mask++){
    let u=Array.from({length:n},(_,a)=>Number(!!(mask&(1<<a))));
    let w=u.reduce((a,b)=>a+b,0),d=defect(u,n),s=construct(d,w,n,q,k),got=invert(s,n,q);
    check(got.w===w&&JSON.stringify(got.z)===JSON.stringify(z)&&
      JSON.stringify(got.d)===JSON.stringify(d)&&JSON.stringify(got.k)===JSON.stringify(k),"blind inverse");
    if(mask===3&&z[0]===0&&z[1]===1&&z[2]<=7){
     let holes=new Set(z),W=Array.from({length:n*q},(_,c)=>Number(Boolean(u[c%n]&&!holes.has(c%q))));
     let raw=defect(W,n*q);
     for(let c=0;c<n*q;c++)check(raw[c]===s[(c%q)*n+c%n],"direct cycle");
     dc++;
    }
    num++;
   }
  }
  let e=q%3===0?q/3:0,ap=q%3===0?q*(q-3)/2:q*(q-1)/2;
  check(counts.equilateral===e&&counts.one_ap===ap&&
    counts.generic===q*(q-1)*(q-2)/6-ap-e,"population count");
  cases.push({n,q,triples:tt.length,nonemptySupports:maxMask,instances:num,directChecks:dc,patterns:counts});
 }
 return {status:"ALL PASS",scientificPin:"BRC16943",result:"EC49FWN",
  cases,totalInstances:cases.reduce((v,c)=>v+c.instances,0),
  totalDirectChecks:cases.reduce((v,c)=>v+c.directChecks,0),
  mathematicalScope:"odd q>=5, gcd(n,q)=1, U nonempty, exactly three missing positions, full indexed reflection defect",
  nativeMovingFarey:"NOT_TESTED",independentReview:"NOT_REVIEWED"};
}
if(typeof module!=="undefined"&&require.main===module)console.log(JSON.stringify(runAll(),null,2));
