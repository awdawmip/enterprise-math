"use strict";
// PREFIX-285 author-side exact C4, ordered-source-pair BRC verifier.
// Source labels are provenance/history indices, not native X6 spatial axes.
const G=(r,i=0)=>({r:BigInt(r),i:BigInt(i)});
const add=(a,b)=>G(a.r+b.r,a.i+b.i);
const mul=(a,b)=>G(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r);
const bar=a=>G(a.r,-a.i);
const n2=a=>a.r*a.r+a.i*a.i;
const CZ=[G(1),G(0,1),G(-1),G(0,-1)];
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b!==0n){const t=a%b;a=b;b=t}return a;}
function frac(n,d){if(d<=0n)throw Error("bad denominator");const g=gcd(n,d);return String(n/g)+"/"+String(d/g);}
function eq(a,b){return a.r===b.r&&a.i===b.i;}
function assert(cond,msg){if(!cond)throw Error(msg);}
function sumSquared(a){let z=0n;for(const v of a)z+=n2(v);return z;}
// Correlation is the exact ordered path-pair sum, preserving history offset.
function rawCorrelation(a,offset){
 let v=G(0);
 for(let j=0;j+offset<a.length;j++){
   const left={source:j,amp:a[j]},right={source:j+offset,amp:a[j+offset]};
   v=add(v,mul(left.amp,bar(right.amp)));
 }
 return v;
}
function signature(a){
 const z=sumSquared(a);
 assert(z>0n,"zero packet");
 const components=[];
 for(let k=1;k<a.length;k++){
  const c=rawCorrelation(a,k);
  components.push(frac(c.r,z),frac(c.i,z));
 }
 components.push(frac(n2(a[0]),z));
 return components.join("|");
}
function relative(a){
 assert(a[0].i===0n&&a[0].r>0n,"first source gauge");
 return a.map(v=>frac(v.r,a[0].r)+","+frac(v.i,a[0].r)).join("|");
}
// A common source convolution creates branches (input-source, filter-tap),
// and collects only the branches at the same resulting source index.
function typedConvolution(a,h){
 const buckets=Array.from({length:a.length+h.length-1},()=>[]);
 for(let j=0;j<a.length;j++)for(let k=0;k<h.length;k++)
  buckets[j+k].push({input_source:j,filter_tap:k,amplitude:mul(a[j],h[k])});
 return buckets;
}
// Diagonal source probability is computed from *all ordered branch pairs*.
function bucketMass(branches){
 let total=G(0);
 for(const x of branches)for(const y of branches)
  total=add(total,mul(x.amplitude,bar(y.amplitude)));
 assert(total.i===0n&&total.r>=0n,"nonreal/negative BRC mass");
 return total.r;
}
function convolveEvidence(a,h){
 const branches=typedConvolution(a,h);
 const out=branches.map(b=>b.reduce((v,x)=>add(v,x.amplitude),G(0)));
 const masses=branches.map(bucketMass);
 for(let i=0;i<out.length;i++)assert(masses[i]===n2(out[i]),"pair/direct mismatch");
 const z=masses.reduce((x,y)=>x+y,0n);
 assert(z===sumSquared(out)&&z>0n,"inconsistent BRC norm");
 return {out,masses,z,branches};
}
function normalizedMass(ev,k){return frac(ev.masses[k],ev.z);}
function complexString(g){return String(g.r)+(g.i>=0n?"+":"")+String(g.i)+"i";}
function allPackets(){
 const a=[];
 for(let m0=1;m0<=3;m0++)
 for(let m1=1;m1<=3;m1++)
 for(let m2=1;m2<=3;m2++)
 for(let p1=0;p1<4;p1++)
 for(let p2=0;p2<4;p2++){
  a.push([G(m0),mul(G(m1),CZ[p1]),mul(G(m2),CZ[p2])]);
 }
 return a;
}
function verifyPrefix285(){
 const f=[G(1),G(0,1),G(1)];
 const g=[G(1),G(0,-1),G(1)];
 assert(signature(f)===signature(g),"base signatures differ");
 const h=[G(1),G(0,1)];
 const F=convolveEvidence(f,h),H=convolveEvidence(g,h);
 assert(F.masses.map(String).join(",")==="1,4,0,1","f masses");
 assert(H.masses.map(String).join(",")==="1,0,4,1","g masses");
 assert(normalizedMass(F,1)==="2/3"&&normalizedMass(H,1)==="0/1","interior contrast");
 assert(signature(F.out)===signature(H.out),"filtered signatures");
 const filters=[];
 for(let u=0;u<4;u++)filters.push([G(1),CZ[u]]);
 for(let u=0;u<4;u++)for(let v=0;v<4;v++)filters.push([G(1),CZ[u],CZ[v]]);
 const map=new Map();
 for(const p of allPackets()){
   const s=signature(p);
   if(!map.has(s))map.set(s,new Map());
   map.get(s).set(relative(p),p);
 }
 let twinSignatures=0,pairs=0,filterComparisons=0,twoProbeComparisons=0;
 const filterCases=[];
 for(const [sig,canonical] of map){
   assert(canonical.size<=2,"unexpected >2 class");
   if(canonical.size!==2)continue;
   twinSignatures++;
   const [a,b]=[...canonical.values()];
   pairs++;
   let distinguished=false;
   const probes=[G(1),G(0,1)];
   for(const u of probes){
      const A=convolveEvidence(a,[G(1),u]),B=convolveEvidence(b,[G(1),u]);
      if(normalizedMass(A,1)!==normalizedMass(B,1))distinguished=true;
      twoProbeComparisons++;
   }
   assert(distinguished,"two C4 filters fail to resolve distinct twin");
   for(const q of filters){
      const A=convolveEvidence(a,q),B=convolveEvidence(b,q);
      assert(signature(A.out)===signature(B.out),"common-filter autocorrelation violated");
      assert(normalizedMass(A,0)===normalizedMass(B,0),"left endpoint violated");
      assert(normalizedMass(A,A.masses.length-1)===normalizedMass(B,B.masses.length-1),"right endpoint violated");
      filterComparisons++;
   }
 }
 const sampleCorr=[];
 for(let r=0;r<F.out.length;r++){
  const v=rawCorrelation(F.out,r);
  assert(eq(v,rawCorrelation(H.out,r)),"sample correlation equality");
  sampleCorr.push(complexString(v));
 }
 return {
  schema:"PREFIX285_EXACT_TYPED_C4_BRC_V1",
  input_packet_count:432,
  distinct_initial_observation_signatures:map.size,
  double_class_signatures:twinSignatures,
  distinct_partner_pairs:pairs,
  common_C4_filters_tested:filters.length,
  pair_filter_comparisons:filterComparisons,
  two_probe_pair_comparisons:twoProbeComparisons,
  sample:{
    f:["1","i","1"],g:["1","-i","1"],common_filter:["1","i"],
    f_filtered_masses:F.masses.map(String),
    g_filtered_masses:H.masses.map(String),
    total_mass:String(F.z),
    interior_source_1_f:normalizedMass(F,1),
    interior_source_1_g:normalizedMass(H,1),
    left_endpoint:normalizedMass(F,0),
    right_endpoint:normalizedMass(F,3),
    filtered_Cr:sampleCorr
  },
  assertions:["direct ordered branch-pair mass equals regrouped amplitude mass",
    "all tested common filters preserve normalized autocorrelation and both endpoints for twin pairs",
    "at least one of h=(1,1),h=(1,i) distinguishes every enumerated distinct Z2 partner using interior mass",
    "special C4 counterexample has exact interior separation 2/3"],
  result:"PASS",
  native_status:"FORMAL_SOURCE_ALGEBRA_ONLY",
  physical_detector_status:"UNVERIFIED"
 };
}
if(typeof process!=="undefined"&&typeof require!=="undefined"&&require.main===module)
 process.stdout.write(JSON.stringify(verifyPrefix285(),null,2)+"\n");
