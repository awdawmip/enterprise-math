#!/usr/bin/env node
'use strict';
// EC49FWB exact checker: rebuild frozen P10, verify universal 10-cycle lemma and signed swaps.
const mod=(x,n)=>((x%n)+n)%n;
const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
const inv=(a,n)=>{for(let x=1;x<n;x++)if(mod(a*x,n)===1)return x;throw Error('inverse')};
const pow=(a,e,p)=>{let z=1;for(let j=0;j<e;j++)z=mod(z*a,p);return z};
function maskDefect(mask,n,c){let d=0;for(let i=0;i<n;i++)if(((mask>>i)&1)!==((mask>>mod(c-i,n))&1))d++;return d}
function minDefect(mask,n){let best=n+1,centers=[];for(let c=0;c<n;c++){const d=maskDefect(mask,n,c);if(d<best){best=d;centers=[c]}else if(d===best)centers.push(c)}return{best,centers}}
function verify(){
 const all10={};
 for(let mask=0;mask<1024;mask++){const d=minDefect(mask,10).best;all10[d]=(all10[d]||0)+1;if(d>2)throw Error('universal ten-cycle lemma false')}
 if(all10[0]!==424||all10[2]!==600)throw Error('ten-cycle full histogram');
 let elevenMask=0;for(const i of [0,1,2,4,7])elevenMask|=1<<i;
 const eleven=minDefect(elevenMask,11);
 if(eleven.best!==4)throw Error('eleven-cycle counterexample');
 const p=11,U=mod(4822040484,p)*inv(mod(8132285009,p),p)%p;
 const gamma=mod(141024,p)*inv(mod(1653649,p),p)%p,i637=inv(mod(637,p),p),rows=[];
 for(let z=0;z<p;z++){let la=mod((637-3*z)*i637,p),lb=mod(U*(1+gamma*z),p);rows.push({z,la,lb,aa:mod(1-(1-z)*la,p),bb:mod(1-(1-z)*lb,p)})}
 const c=mod(-3*i637,p),d=mod(U*gamma,p),P10=new Set();
 for(let h=0;h<10;h++)for(let n=0;n<10;n++){
  let good=rows.filter(r=>r.z!==3).every(r=>mod((pow(r.aa,h,p)*pow(r.la,n,p)-pow(r.bb,h,p)*pow(r.lb,n,p))*inv(mod(r.la-r.lb,p),p),p)!==0);
  good=good&&mod((pow(c,h+n,p)-pow(d,h+n,p))*inv(mod(c-d,p),p),p)!==0;
  if(good)P10.add(10*h+n)
 }
 if(P10.size!==44)throw Error('frozen P10 size');
 const C=(h,n)=>P10.has(10*mod(h,10)+mod(n,10))&&mod(9*h+10*n,11)!==0;
 for(let h=1;h<=110;h++)for(let n=1;n<=110;n++){
  let good=true;
  for(const r of rows){let v;if(r.z===3)v=mod(pow(r.la,n-1,p)*pow(r.aa,h-1,p)*(n*r.aa-h*(1-r.z)*r.la),p);
  else v=mod((pow(r.aa,h,p)*pow(r.la,n,p)-pow(r.bb,h,p)*pow(r.lb,n,p))*inv(mod(r.la-r.lb,p),p),p);
  if(!v){good=false;break}}
  good=good&&mod((pow(c,h+n,p)-pow(d,h+n,p))*inv(mod(c-d,p),p),p)!==0;
  if(good!==C(h,n))throw Error('projective '+h+' '+n)
 }
 const signed={},undirected={},optMultiplicity={},rowCount={0:0,2:0};
 for(let b=0;b<10;b++)for(let a=0;a<10;a++){
  if(gcd(gcd(a,b),10)!==1)continue;
  let anchor=null;
  for(let h=0;h<10&&anchor===null;h++)for(let n=0;n<10;n++)if(mod((b-a)*h-a*n+1,10)===0){anchor=[h,n];break}
  if(!anchor)throw Error('affine line');
  let mask=0;
  for(let t=0;t<10;t++){const h=mod(anchor[0]+a*t,10),n=mod(anchor[1]+(b-a)*t,10);if(P10.has(10*h+n))mask|=1<<t}
  const {best,centers}=minDefect(mask,10),yes=b%2===0&&(a%5===0||mod(2*a-b,5)===0);
  if(best!==(yes?0:2))throw Error('direction '+a+'/'+b);
  rowCount[best]++; const key=best+'|'+centers.length;optMultiplicity[key]=(optMultiplicity[key]||0)+1;
  for(const shift of centers){if(best===0)continue;
   const mismatch=[];for(let t=0;t<10;t++)if(((mask>>t)&1)!==((mask>>mod(shift-t,10))&1))mismatch.push(t);
   if(mismatch.length!==2)throw Error('not a swapped pair');
   const src=mismatch.find(t=>mask>>t&1),dst=mismatch.find(t=>!(mask>>t&1));
   const sign=mod(dst-src,10),delta=Math.min(sign,10-sign);
   signed[sign]=(signed[sign]||0)+1;undirected[delta]=(undirected[delta]||0)+1;
  }
 }
 const eq=(a,b)=>JSON.stringify(Object.keys(a).sort().map(k=>[k,a[k]]))===JSON.stringify(Object.keys(b).sort().map(k=>[k,b[k]]));
 if(rowCount[0]!==8||rowCount[2]!==64||!eq(optMultiplicity,{'0|1':8,'2|1':24,'2|2':24,'2|4':16}))throw Error('direction counts');
 if(!eq(signed,{'1':12,'2':24,'3':12,'4':20,'6':20,'7':12,'8':24,'9':12}))throw Error('signed histogram');
 if(!eq(undirected,{'1':24,'2':48,'3':24,'4':40}))throw Error('distance histogram');
 return {status:'ALL PASS',scope:'exact integer finite certificate; theorem proof in accompanying MD',frozen_input:'BRC16943',ten_bit_masks:1024,all_ten_bit_defects:all10,eleven_cycle_counterexample:{support:[0,1,2,4,7],minimal_defect:eleven.best},original_projective_checks:12100,projective_P10_cells:P10.size,primitive_mod10_directions:72,primitive_direction_defect_histogram:rowCount,optimal_center_multiplicity:optMultiplicity,nonperfect_optimal_swap_centers:136,swap_signed_difference_mod10:signed,swap_unsigned_circular_distance:undirected};
}
console.log(JSON.stringify(verify(),null,2));
