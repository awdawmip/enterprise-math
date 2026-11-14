#!/usr/bin/env node
"use strict";
// EC49EI exact native-six-axis signed-step, BRC count-fiber nine-atom observer verification.
// Full exhaustive domains: h=2,...,7. Transfer ranks GF(2); certificates BigInt Bareiss.
const OP={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const ATOMS=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]];
const BUCKETS=["N","A","B","AB","BA"];
const REPS=["ce","ec","de","ed","cged","gedc","gecd","egdc"];
const OREPS=["e","fe","ge"];
function ok(v,msg){if(!v)throw Error(msg);}
function native(w){return [...w].flatMap(c=>OP[c]);}
function transition(p,state="N",last=0){
 for(const v of p){
  const a=last===1&&v===2,b=last===2&&v===1;
  if(state==="N"){if(a)state="A";else if(b)state="B";}
  else if(state==="A"&&b)state="AB";
  else if(state==="B"&&a)state="BA";
  last=v;
 }
 return [state,last];
}
function transfer(w){const p=native(w);return ATOMS.map(([s,l])=>BUCKETS.indexOf(transition(p,s,l)[0]));}
function cols(t){return BUCKETS.map((_,b)=>t.reduce((v,c,i)=>v|(c===b?1<<i:0),0));}
function rank(cs){
 const piv=Array(9).fill(0);let d=0;
 for(let v of cs){for(let j=8;j>=0;j--){if(!(v&(1<<j)))continue;if(piv[j])v^=piv[j];else{piv[j]=v;d++;break;}}}
 return d;
}
function det9(words){
 const all=words.flatMap(w=>cols(transfer(w)));let sel=[],basis=[];
 for(let j=0;j<all.length;j++){if(rank(basis.concat([all[j]]))>basis.length){sel.push(j);basis.push(all[j]);if(sel.length===9)break;}}
 ok(sel.length===9,"nonfull determinant");
 let a=Array.from({length:9},(_,i)=>sel.map(j=>BigInt((all[j]>>i)&1)));
 let prev=1n,sgn=1n;
 for(let k=0;k<8;k++){
  if(a[k][k]===0n){const p=a.findIndex((row,i)=>i>k&&row[k]!==0n);ok(p>=0,"singular");[a[p],a[k]]=[a[k],a[p]];sgn=-sgn;}
  const pv=a[k][k];
  for(let i=k+1;i<9;i++){
   for(let j=k+1;j<9;j++){const n=a[i][j]*pv-a[i][k]*a[k][j];ok(n%prev===0n,"nonexact Bareiss");a[i][j]=n/prev;}
   a[i][k]=0n;
  }
  prev=pv;
 }
 return String(sgn*a[8][8]);
}
function fiberSet(h){
 const map=new Map(),chars="acdefg";let words=0;
 function walk(w,ns){
  if(w.length===h){
   const [a,c,d,e,f,g]=ns;
   if(e-a!==1)return;
   const p1=2*e+f+c+d,p2=g+c+d,p3=e;
   const key=[p1,p2,p3].join(",");
   if(!map.has(key))map.set(key,new Set());
   map.get(key).add(transfer(w).join(","));
   words++;return;
  }
  for(let i=0;i<6;i++){ns[i]++;walk(w+chars[i],ns);ns[i]--;}
 }
 walk("",[0,0,0,0,0,0]);return {map,words};
}
function bweight(p,w){
 const count=Array(6).fill(0);for(const v of p)if(v>0)count[v-1]++;
 return count.reduce((z,n,i)=>z*BigInt(w[i])**BigInt(n),1n);
}
function run(){
 const signatures=REPS.map(w=>transfer(w)),ranks=signatures.map(x=>rank(cols(x)));
 ok(new Set(signatures.map(x=>x.join(","))).size===8,"event type count");
 ok(JSON.stringify(ranks)==="[3,3,3,3,2,2,2,2]","event ranks");
 const missingPairs=[[3,4],[4,7],[5,6],[6,8]];
 for(let i=0;i<4;i++)for(let j=0;j<8;j++)if(i!==j)
  ok(signatures[j][missingPairs[i][0]]===signatures[j][missingPairs[i][1]],"event omission pair");
 const evDet=det9(REPS.slice(0,4)),noDet=det9(["feg","gef"]);
 ok(evDet==="-1"&&noDet==="-1","unimodular certificates");
 const noTypes=OREPS.map(transfer);
 ok(rank(cols(noTypes[0]))===5,"O rank");
 for(let j=1;j<=2;j++)ok(rank([...cols(noTypes[0]),...cols(noTypes[j])])===7,"partial rank");
 ok(rank(noTypes.flatMap(cols))===9,"zero event rank");
 const hist=[-2,-2,-1,-1,1,1,-1,2,2,-1];
 const weights=[[2,3,5,7,11,13],[3,4,7,11,13,17]];
 for(const w of REPS.slice(0,4).concat(["feg","gef"]))
  for(const x of weights){
   const p=native(w);
   ok(bweight(hist.concat(p),x)===bweight(hist,x)*bweight(p,x),"positive-BRC multiplication");
  }
 const rows=[];
 for(let h=2;h<=7;h++){
  const {map,words}=fiberSet(h);const ct={5:0,7:0,9:0};let events=0,zero=0;
  for(const [key,set] of map){
   const [p1,p2,e]=key.split(",").map(Number);
   const k=p1+p2-h-1,f=p1-2*e-k,g=p2-k;
   ok(k>=0&&f>=0&&g>=0&&e>=1&&h===2*e-1+k+f+g,"fiber algebra");
   const actual=rank([...set].flatMap(s=>cols(s.split(",").map(Number))));
   const expected=k>0?9:5+2*(f>0)+2*(g>0);
   ok(actual===expected,"fiber rank "+h+" "+key+" "+actual+" != "+expected);
   if(k>0){
    events++;
    for(let j=0;j<4;j++)ok(set.has(signatures[j].join(",")),"missing necessary four types");
    for(const s of set)ok(signatures.some(t=>t.join(",")===s),"unlisted event type");
   }else{
    zero++;
    for(const s of set)ok(noTypes.some(t=>t.join(",")===s),"unlisted no-event type");
   }
   ct[actual]++;
  }
  rows.push({h,returning_words:words,positive_fibers:map.size,event_fibers:events,zero_event_fibers:zero,rank_distribution:ct});
 }
 return {status:"PASS",checker:"independent JS GF2 transfer; exact integer Bareiss; full h2..h7 enumeration",event_type_ranks:ranks,unimodular_determinants:{four_event_words:evDet,two_zero_event_words:noDet},enumeration:rows,scope:"native six-axis signed paths; fixed future count p; positive BRC X/Y; nine exact history atoms"};
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module)
 console.log(JSON.stringify(run(),null,2));
