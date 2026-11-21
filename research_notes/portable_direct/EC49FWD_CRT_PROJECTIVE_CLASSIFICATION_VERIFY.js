#!/usr/bin/env node
'use strict';
// Standalone exact BRC16943 P10 CRT projective verifier, Node.js.
function verify(){
 const mod=(x,n)=>((x%n)+n)%n, inv=(a,p)=>{for(let i=1;i<p;i++)if(mod(a*i,p)===1)return i;throw Error("modular inverse")};
 const pow=(a,e,p)=>{let v=1;for(let k=0;k<e;k++)v=mod(v*a,p);return v};
 const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
 const U=mod(4822040484*inv(mod(8132285009,11),11),11),gamma=mod(141024*inv(mod(1653649,11),11),11),I=inv(mod(637,11),11);
 const rows=Array.from({length:11},(_,z)=>{let l=mod((637-3*z)*I,11),r=mod(U*(1+gamma*z),11);return {z,l,r,A:mod(1-(1-z)*l,11),B:mod(1-(1-z)*r,11)}});
 const c=mod(-3*I,11),d=mod(U*gamma,11),P=new Set();
 for(let h=0;h<10;h++)for(let n=0;n<10;n++){
  let good=rows.filter(z=>z.z!==3).every(x=>mod(pow(x.A,h,11)*pow(x.l,n,11)-pow(x.B,h,11)*pow(x.r,n,11),11)!==0);
  if(good&&mod(pow(c,h+n,11)-pow(d,h+n,11),11)!==0)P.add(10*h+n);
 }
 if(P.size!==44||U!==4||gamma!==6||c!==3||d!==2)throw Error("P10 frozen input mismatch");
 const units=[1,3,7,9];for(const u of units)for(let h=0;h<10;h++)for(let n=0;n<10;n++)
   if(P.has(10*h+n)!==P.has(10*mod(u*h,10)+mod(u*n,10)))throw Error("unit covariance");
 const crt=(q2,q5)=>{for(let k=0;k<10;k++)if(k%2===q2&&k%5===q5)return k;throw Error("CRT")};
 const mask=(a,b)=>{let h0=-1,n0=-1;outer:for(let h=0;h<10;h++)for(let n=0;n<10;n++)if(mod((b-a)*h-a*n+1,10)===0){h0=h;n0=n;break outer}if(h0<0)throw Error("affine anchor");let S=[];for(let t=0;t<10;t++)if(P.has(10*mod(h0+a*t,10)+mod(n0+(b-a)*t,10)))S.push(t);return S};
 const optimum=(S)=>{let best=11,centers=[];for(let k=0;k<10;k++){let sum=0;for(const x of S)if(S.includes(mod(k-x,10)))sum++;let delta=2*(S.length-sum);if(delta<best){best=delta;centers=[k]}else if(delta===best)centers.push(k)}return {delta:best,centers}};
 const expected=(q,s)=>q==="11"?[2,2]:q==="10"?[[2,"inf"].includes(s)?0:2,[1,3].includes(s)?4:1]:[2,[0,"inf"].includes(s)?4:1];
 const E=[[1,0],[0,1],[1,1]],L=[0,1,2,3,4,"inf"],classes=[],seen=new Set();
 for(const [q2a,q2b] of E)for(const lam of L){
  let a5=lam==="inf"?0:1,b5=lam==="inf"?1:lam,a=crt(q2a,a5),b=crt(q2b,b5),S=mask(a,b),got=optimum(S),exp=expected(String(q2a)+String(q2b),lam);
  if(got.delta!==exp[0]||got.centers.length!==exp[1])throw Error("wrong class "+q2a+q2b+"/"+lam);
  for(const u of units){const x=mod(u*a,10),y=mod(u*b,10),tag=x+","+y;if(seen.has(tag))throw Error("orbit overlap");seen.add(tag);const z=optimum(mask(x,y));if(z.delta!==got.delta||z.centers.length!==got.centers.length)throw Error("orbit mismatch")}
  classes.push({epsilon:String(q2a)+String(q2b),lambda:String(lam),direction:[a,b],mask:S.reduce((v,x)=>v|(1<<x),0),weight:S.length,minimum_defect:got.delta,optimal_centers:got.centers.length,centers:got.centers});
 }
 if(classes.length!==18||seen.size!==72)throw Error("projective completeness");
 let hist={};for(const r of classes){let k="delta"+r.minimum_defect+"_N"+r.optimal_centers;hist[k]=(hist[k]||0)+1}
 if(JSON.stringify([hist.delta0_N1,hist.delta2_N1,hist.delta2_N2,hist.delta2_N4])!==JSON.stringify([2,6,6,4]))throw Error("18-class histogram");
 let all=0,per={};for(let a=0;a<10;a++)for(let b=0;b<10;b++)if(gcd(gcd(a,b),10)===1){all++;let o=optimum(mask(a,b)),k="delta"+o.delta+"_N"+o.centers.length;per[k]=(per[k]||0)+1}
 if(all!==72||JSON.stringify([per.delta0_N1,per.delta2_N1,per.delta2_N2,per.delta2_N4])!==JSON.stringify([8,24,24,16]))throw Error("72-direction independent histogram");
 return {status:"ALL PASS",scientific_pin:"BRC16943",scope:"auxiliary mod-10 P10 factor only",arithmetic:"exact modular integers, no floats",P10_cells:44,primitive_directions:72,CRT_projective_classes:18,unit_orbit_size:4,representative_histogram:hist,all_direction_histogram:per,table:classes,limits:"Confluent mod-11 factor and Bernoulli-to-projective bridge inherited; formal Review not performed."};
}
console.log(JSON.stringify(verify(),null,2));
