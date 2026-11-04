/* PREFIX-487 exact BRC/KMP/source support certificate; Node.js >=18; all counts in exact safe integer range. */
"use strict";
function certificate() {
 const L="aAbBcCdDeE", V=[0,1,0,2,1], W=[0,0,1,0,1];
 const gateList=["aab","aba"], lines=["PREFIX-487: N-only, NB-only, triple-source exact reachability"];
 function ok(cond,msg){if(!cond)throw Error(msg)}
 function choose(n,k){if(n<k||n<0)return 0;let x=1;for(let i=1;i<=k;i++)x=x*(n-k+i)/i;return Math.round(x)}
 function kmp(q,c,w){const s=w.slice(0,q)+c;for(let j=w.length;j>=0;j--)if(s.endsWith(w.slice(0,j)))return j;throw Error("KMP")}
 function move(o,i){
  const a=o.slice();if(i===10){a[0]++;return a}
  const axis=Math.floor(i/2),dir=i%2===0?1:-1,y=a[axis+1],inc=Number(y*dir<0);
  a[axis+1]+=dir;a[6]+=inc*V[axis];a[7]+=inc*W[axis];return a;
 }
 function source(t,c){return t||(c==="b"||c==="B"?1:(c==="c"||c==="C"?2:0))}
 function decode(x){return x.split(",").map(Number)}
 function key(o,q,t){return o.concat([q,t]).join(",")}
 function Nformula(w,n) {
  let ans=0;
  for(let s=0;s<=1;s++){
   const m=n-s;if(m<0)continue;
   ans+=choose(m+5,5)-Number(m>=1);
   ans+=choose(m+4,5)-Number(w==="aab"&&m>=2);
   if(w==="aab")ans+=choose(m+3,5);
  }
  return ans;
 }
 function NBformula(w,n){
  let ans=0,qs=w==="aab"?[0,1,2]:[0,1];
  for(let s=0;s<=1;s++)for(const q of qs){const m=n-s;ans+=choose(m-q,4)+choose(m-q-1,4)}
  return ans;
 }
 function Tformula(w,n){
  let ans=0,qs=w==="aab"?[0,1,2]:[0,1];
  for(let s=0;s<=1;s++)for(const q of qs)ans+=choose(n+1-s-q,5);
  return ans;
 }
 function brute(w,n){
  const mask=new Map();let count=0;
  function visit(o,q,t,len){
   if(len===n){const k=o.concat([q]).join(",");mask.set(k,(mask.get(k)||0)|(1<<t));count++;return}
   for(let i=0;i<10;i++)visit(move(o,i),kmp(q,L[i],w),source(t,L[i]),len+1);
   if(len===0||q===w.length)visit(move(o,10),0,t,len+1);
  }
  visit(Array(8).fill(0),0,0,0);return {mask,count};
 }
 for(const w of gateList){
  let cur=new Set([key(Array(8).fill(0),0,0)]);
  lines.push("GATE="+w);
  for(let n=0;n<=9;n++){
   const fibers=new Map();
   for(const k of cur){const a=decode(k),b=a.slice(0,9).join(",");fibers.set(b,(fibers.get(b)||0)|(1<<a[9]))}
   let nTotal=0,nOnly=0,nb=0,t=0;
   for(const mask of fibers.values()){
    if(mask&1){nTotal++;if(mask===1)nOnly++;else if(mask===3)nb++;else if(mask===7)t++;else throw Error("Unexpected N support mask="+mask)}
    ok(mask!==5,"Found forbidden NC-only fiber");
   }
   ok(nTotal===Nformula(w,n),w+" n="+n+" N error "+nTotal);
   ok(nb===NBformula(w,n),w+" n="+n+" NB error "+nb);
   ok(t===Tformula(w,n),w+" n="+n+" T error "+t);
   ok(nOnly===nTotal-nb-t,"N decomposition failed");
   if(n<=4){const b=brute(w,n);ok(b.mask.size===fibers.size,"Brute size mismatch");for(const [k,v] of b.mask)ok(fibers.get(k)===v,"Brute mask mismatch");}
   lines.push("n="+n+" base="+fibers.size+" N="+nTotal+" N_only="+nOnly+" NB_only="+nb+" NBC="+t+" check=PASS");
   if(n===9)break;
   const next=new Set();
   for(const k of cur){
    const a=decode(k),o=a.slice(0,8),q=a[8],t=a[9];
    for(let i=0;i<10;i++)next.add(key(move(o,i),kmp(q,L[i],w),source(t,L[i])));
    if(n===0||q===w.length)next.add(key(move(o,10),0,t));
   }
   cur=next;
  }
 }
 lines.push("CHECK_DOMAIN=n:0..9;brute:n:0..4;source_masks:ALL");
 lines.push("ALL_CHECKS_PASS");
 return lines.join("\n")+"\n";
}
console.log(certificate());
