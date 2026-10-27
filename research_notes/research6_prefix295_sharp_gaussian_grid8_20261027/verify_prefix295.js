#!/usr/bin/env node

"use strict";

// Exact SOURCE-LABELLED BRC: every bin sums all nine ordered source pairs; no floating point.

// q in C4; numerator rows have common denominator 8.

// Run with: node verify_prefix295.js

function g(r=0,i=0){return[BigInt(r),BigInt(i)]}

function add(a,b){return[a[0]+b[0],a[1]+b[1]]}

function mul(a,b){return[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]]}

function conj(a){return[a[0],-a[1]]}

function norm(a){return a[0]*a[0]+a[1]*a[1]}

function scale(a,n){return[a[0]*BigInt(n),a[1]*BigInt(n)]}

function eq(a,b){return a[0]===b[0] && a[1]===b[1]}

function zero(){return g(0,0)}

function rows(q){
 const q2=mul(q,q);
 return [
 [g(4),scale(q,4),zero()],
 [zero(),g(-4),scale(q,4)],
 [g(2,2),mul(g(-4,-4),q),mul(g(-2,-2),q2)],
 [g(-5,-2),zero(),scale(q2,2)],
 [g(-3,1),zero(),mul(g(-5,3),q2)],
 [g(1),zero(),zero()],
 [zero(),zero(),mul(g(1,1),q2)]
 ];
}

function brc(row,a,b=a){
 let acc=zero();
 for(let j=0;j<3;j++)for(let k=0;k<3;k++){
   const u=mul(row[j],a[j]),v=mul(row[k],b[k]);
   acc=add(acc,mul(conj(u),v));
 }
 return acc;
}

function dot(a,b){
 let acc=zero();
 for(let j=0;j<3;j++)acc=add(acc,mul(conj(a[j]),b[j]));
 return acc;
}

function fail(x){throw new Error(x)}

function verify(){
 const qlist=[g(1),g(0,1),g(-1),g(0,-1)];
 const digits=[g(0),g(1),g(-1),g(0,1),g(0,-1),g(1,1)];
 let totalBins=0,sourcePairs=0,mass=0,leak=0,cross=0;
 let qi=0;
 for(const q of qlist){
   const R=rows(q);
   const basis=[[g(1),zero(),zero()],[zero(),g(1),zero()],[zero(),zero(),g(1)]];
   for(let j=0;j<3;j++)for(let k=0;k<3;k++){
     let t=zero();
     for(const row of R)t=add(t,brc(row,basis[j],basis[k]));
     if(!eq(t,scale(dot(basis[j],basis[k]),64)))fail("cross q="+qi+" j="+j+" k="+k);
     cross++;
   }
   for(const a0 of digits)for(const a1 of digits)for(const a2 of digits){
     const a=[a0,a1,a2];
     const rr=R.map(row=>brc(row,a));
     if(rr.some(x=>x[1]!==0n||x[0]<0n))fail("positive BRC");
     const total=rr.reduce((x,y)=>x+y[0],0n);
     const Z=norm(a0)+norm(a1)+norm(a2);
     if(total!==64n*Z)fail("mass");
     const tail=rr[5][0]+rr[6][0];
     if(tail!==norm(a0)+2n*norm(a2))fail("leak");
     if(tail>2n*Z)fail("leak bound");
     mass++;leak++;totalBins+=7;sourcePairs+=7*9;
   }
   qi++;
 }
 const i=g(0,1),qq=i;
 const a=[g(1),i,g(1)],b=[g(1),g(0,-1),g(1)];
 const A=rows(qq).slice(0,2).reduce((v,r)=>v+brc(r,a)[0],0n);
 const B=rows(qq).slice(0,2).reduce((v,r)=>v+brc(r,b)[0],0n);
 if(A!==0n||B!==128n)fail("witness");
 return {schema:"PREFIX295_EXACT_BRC_V1",source_carrier:"three provenance-labelled Q(i) amplitudes", phases:4, inputs_per_phase:216, inputs_total:mass, ordered_source_pair_terms:sourcePairs, direct_brc_bin_reads:totalBins, mass_checks:mass, leak_checks:leak, cross_input_gram_checks:cross, event_witness:{phase:"i",a_event_numerator:A.toString(),b_event_numerator:B.toString(),normalizer:"64*Z; Z=3", probabilities:["0","2/3"]}, leakage_operator_numerator_diag:[1,0,2], worst_leakage:"1/32", exact_arithmetic:"BigInt Gaussian integers",native_Hn_executed:false,verified:true};
}

console.log(JSON.stringify(verify(), null, 2));

