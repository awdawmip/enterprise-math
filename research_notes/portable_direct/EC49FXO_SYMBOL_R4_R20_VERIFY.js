'use strict';
const assert=require('node:assert/strict');
const MOD=(a,n)=>((a%n)+n)%n, clamp=x=>Math.min(5,Math.max(0,x));
const value=(r,k)=>5*r+clamp(k-55+5*Math.ceil(r/2))+clamp(k-55+5*(r-10));
function perColor(r,k,i){
 const safe=[],unsafe=[];
 for(let x=i;x<55;x+=5) ((2*x)%55>=k?safe:unsafe).push(x);
 const s=safe.length;
 let sites;
 if(2*s>=r)sites=safe.flatMap(x=>[x,x+55]).slice(0,r);
 else if(11+s>=r+1)sites=[...safe.flatMap(x=>[x,x+55]),...unsafe].slice(0,r+1);
 else sites=[...safe,...unsafe].flatMap(x=>[x,x+55]).slice(0,r+2);
 assert.equal(new Set(sites).size,sites.length);
 assert.equal(sites.length,r+(s<Math.ceil(r/2)?1:0)+(s<r-10?1:0));
 return sites;
}
function construct(r,k){
 const sites=Array.from({length:5},(_,i)=>perColor(r,k,i)).flat().sort((a,b)=>a-b);
 assert.equal(new Set(sites).size,sites.length);
 assert.equal(sites.length,value(r,k));
 return sites;
}
function distance(sites,k){
 let min=Infinity,rows=0;
 for(let d=0;d<k;d++)for(let i=0;i<5;i++)for(let j=0;j<11;j++){
  let count=0;
  for(const t of sites){
   if((t%5===i&&t%11!==j)||(MOD(d-t,5)===i&&MOD(d-t,11)!==j))count++;
  }
  min=Math.min(min,count);rows++;
 }
 return {min,rows};
}
function states(s){
 let dp=new Map([['0:0',[0,0]]]);
 for(let x=0;x<11;x++){
  const next=new Map();
  for(const [m,e] of dp.values())for(let n=0;n<=2;n++){
   const M=m+n,E=x<s?e:Math.max(e,n);
   next.set(M+':'+E,[M,E]);
  }
  dp=next;
 }
 return [...dp.values()];
}
const lookup=Array.from({length:11},(_,s)=>states(s));
let occupancyChecks=0,crtRows=0,layouts=0;
for(let r=4;r<=20;r++)for(let s=0;s<=10;s++){
 const best=Math.min(...lookup[s].filter(([m,e])=>m-e>=r).map(([m])=>m));
 assert.equal(best,r+(s<Math.ceil(r/2)?1:0)+(s<r-10?1:0));
 occupancyChecks++;
}
for(let s=0;s<=10;s++)assert.equal(Math.max(...lookup[s].map(([m,e])=>m-e)),20);
const profiles=[];
for(let r=4;r<=20;r++){
 const values=[];
 for(let k=5;k<=55;k++){
  const sites=construct(r,k),check=distance(sites,k);
  assert.ok(check.min>=r,'distance shortfall: '+r+','+k);
  crtRows+=check.rows;layouts++;
  values.push({k,N:sites.length,minimum_observed_distance:check.min});
 }
 profiles.push({r,values});
}
assert.equal(occupancyChecks,187);
assert.equal(layouts,867);
assert.equal(crtRows,1430550);
console.log(JSON.stringify({schema:'EC49FXO_EXACT_INTEGER_V1',frozen_science:'BRC16943',scope:'r=4..20 k=5..55; auxiliary whole-activation symbol distance',occupancyChecks,layouts,crtRows,r21:'NO_FEASIBLE_LAYOUT_WHEN_k>=5',result:'PASS',profiles},null,2));
