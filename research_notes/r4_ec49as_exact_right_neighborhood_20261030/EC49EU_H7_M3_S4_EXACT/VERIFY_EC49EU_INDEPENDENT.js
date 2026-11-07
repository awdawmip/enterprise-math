#!/usr/bin/env node
// Independent seven-letter native signed-X6 and 9-history enumeration.
// No import of the Python fiber/trie generator. Exact integer mod-p arithmetic.
const fs=require('fs');
const OP={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
const HIST=[['N',0],['N',1],['N',2],['A',0],['A',2],['B',0],['B',1],['AB',0],['BA',0]];
const BUCKETS=['N','A','B','AB','BA'];const BASE=['ce','de','ec','ed'];
const MOD=1000003;
const assert=(ok,msg)=>{if(!ok)throw Error(msg)};
const steps=w=>Array.from(w).flatMap(t=>OP[t]);
function pc(w){const p=Array(6).fill(0);for(const s of steps(w))if(s>0)p[s-1]++;return p;}
function dis(w){const p=Array(6).fill(0);for(const s of steps(w))p[Math.abs(s)-1]+=Math.sign(s);return p;}
function sig(w){const seq=steps(w);return HIST.map(([start,old])=>{
 let state=start,last=old;
 for(const s of seq){
   if(last===1&&s===2){if(state==='N')state='A';else if(state==='B')state='BA';}
   else if(last===2&&s===1){if(state==='N')state='B';else if(state==='A')state='AB';}
   last=s;
 }
 return BUCKETS.indexOf(state);
});}
const key=a=>a.join(',');
const sigKey=w=>key(sig(w));
const T4=BASE.map(sigKey),T4SET=new Set(T4);
assert(T4SET.size===4,'T4 not distinct');
function pow(a,n){let b=1;while(n){if(n%2)b=b*a%MOD;a=a*a%MOD;n=Math.floor(n/2);}return b;}
function rank(words){const rows=Array.from({length:9},()=>[]);
 for(const w of words){const sg=sig(w);for(let i=0;i<9;i++)for(let b=0;b<5;b++)rows[i].push(+(sg[i]===b));}
 let r=0;for(let j=0;j<rows[0].length&&r<9;j++){
  let k=r;while(k<9&&!rows[k][j])k++;if(k===9)continue;
  [rows[r],rows[k]]=[rows[k],rows[r]];const inv=pow(rows[r][j],MOD-2);
  for(let l=j;l<rows[r].length;l++)rows[r][l]=rows[r][l]*inv%MOD;
  for(let i=r+1;i<9;i++)if(rows[i][j]){
   const mul=rows[i][j];for(let l=j;l<rows[i].length;l++)rows[i][l]=(rows[i][l]-mul*rows[r][l]+MOD*MOD)%MOD;
  }
  r++;
 }
 return r;
}
assert(rank(BASE)===9,'base rank9');
for(let j=0;j<4;j++)assert(rank(BASE.filter((_,i)=>i!==j))<9,'T4 not inclusion-minimal');

// Exhaust 7^h operation words, *without* using the Python inverse-count formula.
let byH={}, totals={};
for(let h=2;h<=7;h++){
 const fibers=new Map();let legal=0;
 const walk=(word,displ,p)=>{
   if(word.length===h){
     if(displ[0]===2&&displ.slice(1).every(x=>x===0)){
       legal++;const k=key(p);if(!fibers.has(k))fibers.set(k,new Set());
       fibers.get(k).add(sigKey(word));
     }
     return;
   }
   for(const [t,seq] of Object.entries(OP)){
     const q=displ.slice(),pp=p.slice();
     for(const s of seq){q[Math.abs(s)-1]+=Math.sign(s);if(s>0)pp[s-1]++;}
     walk(word+t,q,pp);
   }
 };
 walk('',Array(6).fill(0),Array(6).fill(0));
 const t4=Array.from(fibers).filter(([p,signatures])=>T4.every(t=>signatures.has(t))).map(([p])=>p).sort();
 byH[h]=t4;totals[h]={all_return_words:legal,full_T4_fibers:t4.length};
}
assert(key(Object.values(totals).map(x=>x.all_return_words))==='8,51,304,1770,10224,58947','legal population counts mismatch');
assert(key(Object.values(totals).map(x=>x.full_T4_fibers))==='1,3,7,13,22,34','T4 population counts mismatch');
const p0=key(pc('ce'));
const combos=[];
for(const p3 of byH[3])for(const p4 of byH[4])for(const p5 of byH[5])for(const p6 of byH[6])for(const p7 of byH[7]){
  const arr=[p3,p4,p5,p6,p7];if(new Set([p0,...arr]).size===3)combos.push(arr);
}
assert(combos.length===3,'M3-S4 assignment count mismatch');
const j=JSON.parse(fs.readFileSync('EC49EU_M3S4_EXECUTED.json','utf8'));
const EXPECTED=[116,116,128];let cases=[];
for(const [i,c] of j.cases.entries()){
 const stored=c.p3_to_p7.map(p=>key(p));assert(combos.some(a=>key(a)===key(stored)),'missing exact p assignment');
 const W={2:BASE};for(const [h,ww] of Object.entries(c.attaining_words))W[+h]=ww;
 const prefix=new Set(),pkeys=new Set(),signs=new Set(),ranks={};
 for(let h=2;h<=7;h++){
   const ww=W[h];assert(ww&&ww.length>=4,'required four transfer types');
   assert(ww.every(w=>w.length===h&&key(dis(w))==='2,0,0,0,0,0'),'native displacement/length');
   assert(new Set(ww.map(w=>key(pc(w)))).size===1,'same positive p within horizon');
   if(h>=3)assert(key(pc(ww[0]))===stored[h-3],'frozen selected p assignment');
   ranks[h]=rank(ww);assert(ranks[h]===9,'exact rank failure');
   for(const w of ww){const seq=steps(w);pkeys.add(key(pc(w)));signs.add(sigKey(w));for(let k=1;k<=seq.length;k++)prefix.add(key(seq.slice(0,k)));}
 }
 assert(prefix.size===EXPECTED[i]&&pkeys.size===3&&signs.size===4,'E/M/S mismatch');
 cases.push({p7:c.p3_to_p7[4].slice(0,3),E:prefix.size,M:pkeys.size,S:signs.size,ranks,selected_words:Object.values(W).reduce((n,x)=>n+x.length,0)});
}
const report={unit:'EC49EU',verification:'independent JS native seven-letter complete enumeration and exact modular 9-rank',status:'PASS',native_operation_words:totals,M3_S4_assignments:combos,independent_witnesses:cases,modulus:MOD,modular_rank_nonzero_implies_rational_rank:true};
fs.writeFileSync('EC49EU_INDEPENDENT_EXECUTED.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'PASS',native_operation_words:totals,M3_S4_assignments:combos.length,resource_points:cases.map(x=>[x.E,x.M,x.S])}));
