"use strict";
// EC49EN: actual ordered native X6, nine-atom observer, formal positive-BRC cache keys.
const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],
e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const ATOMS=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]];
const BUCKETS=["N","A","B","AB","BA"];
function check(test,message){if(!test)throw Error(message);}
function native(word){return [...word].flatMap(ch=>OPS[ch]);}
function plus(path){return [1,2,3,4,5,6].map(i=>path.filter(x=>x===i).length);}
function delta(path){return [1,2,3,4,5,6].map(i=>path.filter(x=>x===i).length-path.filter(x=>x===-i).length);}
function label(path,s="N",last=0){
 for(const v of path){if(last===1&&v===2)s=({N:"A",B:"BA"}[s]||s);
  if(last===2&&v===1)s=({N:"B",A:"AB"}[s]||s);last=v;}
 return s;
}
function transfer(word){const p=native(word);
 return ATOMS.map(([state,last])=>BUCKETS.indexOf(label(p,state,last)));}
function rank(words){
 const piv=Array(9).fill(0);let r=0;
 for(const word of words){const t=transfer(word);
  for(let b=0;b<5;b++){let mask=0;
   for(let i=0;i<9;i++)if(t[i]===b)mask|=1<<i;
   for(let i=8;i>=0;i--){if(!(mask&(1<<i)))continue;
    if(piv[i])mask^=piv[i];else{piv[i]=mask;r++;break;}}
  }}
 return r;
}
function words(a,h){
 check(a>=2&&h>=a&&h<=2*a-1,"range");
 const q=2*a-1-h,u=h-a,v=h-a,tail="f".repeat(u)+"g".repeat(v);
 if(q>=1)return ["e"+"c".repeat(q)+tail,"e"+"d".repeat(q)+tail,
 "c"+"e"+"c".repeat(q-1)+tail,"d"+"e"+"d".repeat(q-1)+tail];
 return ["feg"+"f".repeat(u-1)+"g".repeat(v-1),
 "gef"+"f".repeat(u-1)+"g".repeat(v-1)];
}
function sample(H,eventOnly){
 const wordsAll=[],pkeys=new Set(),transfers=new Set(),intervals=[];
 let start=2;
 while(start<=H){const last=Math.min(H,eventOnly?2*start-2:2*start-1);
  intervals.push([start,last]);
  for(let h=start;h<=last;h++){const ws=words(start,h);
   check(rank(ws)===9,"rank "+h+" "+eventOnly);
   for(const w of ws){const p=native(w);check(w.length===h,"h "+h);
    check(delta(p).join()==="2,0,0,0,0,0","displacement "+h);
    check(p.length===4*start,"native length "+h);
    check(plus(p).join()===[start+1,start-1,1,0,0,0].join(),"positive p "+h);
    pkeys.add(plus(p).join());transfers.add(transfer(w).join());
    wordsAll.push(w);}
  }
  start=last+1;
 }
 const edge=new Set();for(const w of wordsAll){const p=native(w);
  for(let i=1;i<=p.length;i++)edge.add(p.slice(0,i).join());}
 const ceilLog2=x=>{let n=0,v=1;while(v<x){v*=2;n++;}return n;};
 const target=eventOnly?ceilLog2(H):ceilLog2(H+1)-1;
 check(pkeys.size===target,"minimum exponent keys H "+H);
 check(transfers.size===(eventOnly||H===2?4:6),"transfer blocks H "+H);
 return {H,route:eventOnly?"FOUR_OBSERVER_BLOCKS":"MIN_POSITIVE_BRC_KEYS",
  cache_keys:pkeys.size,observer_blocks:transfers.size,
  primitive_prefix_edges:edge.size,word_occurrences:wordsAll.length,
  intervals,pkeys:[...pkeys].sort()};
}
let intervalsChecked=0;
for(let e=1;e<=4;e++)for(let p1=2*e;p1<=2*e+15;p1++)for(let p2=0;p2<=15;p2++){
 const m=Math.min(p1-2*e,p2),A=p1+p2-1-m,B=p1+p2-1;
 check(B<=2*A-1,"unrestricted interval bound");
 if(m>=1)check(B-1<=2*A-2,"event interval bound");
 intervalsChecked++;
}
const cases=[2,3,4,5,7,8,9,10,15,16,20,31,32];
const rows=cases.flatMap(H=>[sample(H,false),sample(H,true)]);
return {status:"PASS",unit:"EC49EN",arithmetic:"exact integer native-X6/GF2 observer/positive monomial exponents",
 test_horizons:cases,interval_bounds_checked:intervalsChecked,rows,
 claims:["M(H)=ceil(log2(H+1))-1, H>=2",
 "M_for_four_cached_transfer_blocks(H)=ceil(log2 H), H>=2",
 "nondominated (M,S) are (j,4) at H=2^j and (j,6),(j+1,4) at 2^j<H<2^(j+1)"],
 proof_scope:"Analytic all-H interval lower bounds + explicit paths; finite checks only corroborate."};
