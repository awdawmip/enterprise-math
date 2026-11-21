#!/usr/bin/env node
'use strict';
// EC49FWC exact verifier: rebuild the frozen BRC16943 P10 factor, enumerate the 18 homothety orbits,
// and verify the antipodal correction criterion on the complete 1024-word universe.
const mod=(x,n)=>((x%n)+n)%n;
const gcd=(a,b)=>{while(b){[a,b]=[b,a%b]}return a};
const inv=(a,n)=>{for(let x=1;x<n;x++)if(mod(a*x,n)===1)return x;throw Error('inverse')};
const power=(a,e,p)=>{let z=1;for(let i=0;i<e;i++)z=mod(z*a,p);return z};
function makeP10(){
 const p=11, U=mod(4822040484,p)*inv(mod(8132285009,p),p)%p, gam=mod(141024,p)*inv(mod(1653649,p),p), I=inv(mod(637,p),p);
 const rows=[];for(let z=0;z<11;z++){const l=mod((637-3*z)*I,p),r=mod(U*(1+gam*z),p);rows.push({z,l,r,A:mod(1-(1-z)*l,p),B:mod(1-(1-z)*r,p)})}
 const c=mod(-3*I,p),d=mod(U*gam,p),P=new Set();
 for(let h=0;h<10;h++)for(let n=0;n<10;n++){
  let good=rows.filter(x=>x.z!==3).every(x=>mod((power(x.A,h,p)*power(x.l,n,p)-power(x.B,h,p)*power(x.r,n,p))*inv(mod(x.l-x.r,p),p),p)!==0);
  good=good&&mod((power(c,h+n,p)-power(d,h+n,p))*inv(mod(c-d,p),p),p)!==0;
  if(good)P.add(10*h+n);
 }
 return P;
}
function calc(P){
 const units=[1,3,7,9], directions=new Map(),counts={},reps=[],seen=new Set(),allUnsigned={},allSigned={},allWeight={};
 const bitcount=m=>{let n=0;for(let t=0;t<10;t++)n+=(m>>t)&1;return n};
 const maskAt=(a,b)=>{let h0=-1,n0=-1;outer:for(let h=0;h<10;h++)for(let n=0;n<10;n++)if(mod((b-a)*h-a*n+1,10)===0){h0=h;n0=n;break outer}if(h0<0)throw Error('no anchor');
 let m=0;for(let t=0;t<10;t++)if(P.has(10*mod(h0+a*t,10)+mod(n0+(b-a)*t,10)))m|=1<<t;return m;};
 const optimum=(m)=>{let best=11,centers=[];for(let c=0;c<10;c++){let dif=[];for(let t=0;t<10;t++)if(((m>>t)&1)!==((m>>mod(c-t,10))&1))dif.push(t);if(dif.length<best){best=dif.length;centers=[{c,dif}]}else if(dif.length===best)centers.push({c,dif});}return {best,centers};};
 const shifts=m=>{const out=new Set();for(let k=0;k<10;k++)for(let sign of [1,-1]){let mm=0;for(let t=0;t<10;t++)if((m>>mod(sign*t+k,10))&1)mm|=1<<t;out.add(mm)}return out};
 if(P.size!==44)throw Error('P10 cell count');
 for(let u of units)for(let h=0;h<10;h++)for(let n=0;n<10;n++)if(P.has(10*h+n)!==P.has(10*mod(u*h,10)+mod(u*n,10)))throw Error('unit covariance');
 for(let b=0;b<10;b++)for(let a=0;a<10;a++)if(gcd(gcd(a,b),10)===1)directions.set(`${a},${b}`,maskAt(a,b));
 if(directions.size!==72)throw Error('primitive count');
 let totalCorrections=0,p10Antipodal=0;
 for(let [key,m] of directions){
  const [a,b]=key.split(',').map(Number),{best,centers}=optimum(m);
  counts[`${best}|${centers.length}`]=(counts[`${best}|${centers.length}`]||0)+1;
  allWeight[bitcount(m)]=(allWeight[bitcount(m)]||0)+1;
  if(best!==0)for(let {dif} of centers){if(dif.length!==2)throw Error('bad defect');const from=dif.find(t=>(m>>t)&1),to=dif.find(t=>!((m>>t)&1)),s=mod(to-from,10),d=Math.min(s,10-s);
   allSigned[s]=(allSigned[s]||0)+1;allUnsigned[d]=(allUnsigned[d]||0)+1;
   totalCorrections++;if(d===5)p10Antipodal++;
  }
  for(let u of units){const vv=`${mod(u*a,10)},${mod(u*b,10)}`;if(!shifts(m).has(directions.get(vv)))throw Error('unit orbit word mismatch '+key+' '+u);}
  if(seen.has(key))continue;
  const orbit=units.map(u=>`${mod(u*a,10)},${mod(u*b,10)}`);
  if(new Set(orbit).size!==4)throw Error('orbit not free');
  for(let z of orbit)seen.add(z);
  const distances=best===2?centers.map(({dif})=>{const from=dif.find(t=>(m>>t)&1),to=dif.find(t=>!((m>>t)&1));return Math.min(mod(to-from,10),mod(from-to,10))}).sort((x,y)=>x-y):[];
  reps.push({a,b,defect:best,optimal_centers:centers.length,distances});
 }
 if(reps.length!==18||totalCorrections!==136||p10Antipodal!==0)throw Error('frozen spectrum');
 let allWordsAntipodal=0,wordStats={},tripleCount=0;
 for(let m=0;m<1024;m++){const {best,centers}=optimum(m),weight=bitcount(m);
  if(weight===3){const pts=[];for(let t=0;t<10;t++)if((m>>t)&1)pts.push(t);const good=pts.some(z=>{const other=pts.filter(x=>x!==z);return mod(other[0]+other[1]-2*z,10)===5});if(good)tripleCount++;}
  if(best===2)for(const {dif} of centers){if(Math.abs(dif[0]-dif[1])!==5)continue;allWordsAntipodal++;wordStats[weight]=(wordStats[weight]||0)+1;if(weight!==3&&weight!==7)throw Error('unexpected antipodal weight');}
 }
 if(allWordsAntipodal!==80||tripleCount!==40||wordStats[3]!==40||wordStats[7]!==40)throw Error('universal antipodal census');
 const T=new Set([0,2,7]);
 for(let m of directions.values()){if(bitcount(m)!==7)continue;const zeros=[];for(let t=0;t<10;t++)if(!((m>>t)&1))zeros.push(t);let ok=false;
  for(let sign of [1,-1])for(let shift=0;shift<10;shift++)if(zeros.every(t=>T.has(mod(sign*t+shift,10))))ok=true;
  if(!ok)throw Error('weight7 complement not in triple orbit');
 }
 return {status:'ALL PASS',frozen_science:'BRC16943',scope:'P10 auxiliary mod-10 certificate factor; finite exact checks',P10_cells:P.size,unit_covariance:units,primitive_directions:directions.size,unit_direction_orbits:reps.length,orbit_size:4,representatives:reps,all_direction_optimal_center_histogram:counts,all_direction_weight_histogram:allWeight,optimal_signed_displacement:allSigned,optimal_unsigned_distance:allUnsigned,optimal_corrections:totalCorrections,antipodal_corrections_in_frozen_P10:p10Antipodal,universal_optimal_antipodal_word_events:allWordsAntipodal,universal_antipodal_triples:tripleCount,universal_antipodal_event_weight_histogram:wordStats};
}
console.log(JSON.stringify(calc(makeP10()),null,2));
