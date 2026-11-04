function executedPrefix479Certificate(){
"use strict";
/* PREFIX-479 exact integer certificate: X6 word gates, weighted renewal and KMP factorization.
 * No external dependencies. BigInt for every count and mass. Return raw log string.
 */
const ORD=[..."aAbBcCdDeE"];
const POS={a:6n,A:1n,b:12n,B:1n,c:18n,C:1n,d:24n,D:1n,e:36n,E:1n,x:1n};
const ONE=Object.fromEntries([...ORD,"x"].map(c=>[c,1n]));
const WORDS=["aab","aba","aAa","ababa","abab","aa","aA","abbb"];
const check=(b,msg)=>{if(!b)throw Error(msg)};
const plus=(map,key,val)=>map.set(key,(map.get(key)||0n)+val);
function transition(w,q,c){
  const t=w.slice(0,q)+c;
  for(let j=w.length;j>=0;--j)if(t.endsWith(w.slice(0,j)))return j;
  throw Error("transition");
}
function choose(n,r){
  if(n<0||r<0||r>n)return 0n;
  let v=1n;
  for(let j=1;j<=r;j++)v=v*BigInt(n-r+j)/BigInt(j);
  return v;
}
function bi(n,s,k,A,Q){
  if(s===0)return A**BigInt(n);
  const d=n-(k+1)*s,e=n-1-(k+1)*(s-1);
  return (d>=0?Q**BigInt(s)*choose(d+s,s)*A**BigInt(d):0n)
    +(e>=0?Q**BigInt(s-1)*choose(e+s-1,s-1)*A**BigInt(e):0n);
}
function wordsDP(w,N,weights){
  let cur=new Map([["0,0",1n]]),out=[];
  for(let n=0;n<=N;n++){
    out.push(cur);
    if(n===N)break;
    let nxt=new Map();
    for(const [key,v] of cur){
      const [s,q]=key.split(",").map(Number);
      for(const c of ORD)plus(nxt,s+","+transition(w,q,c),v*weights[c]);
      if(n===0||q===w.length)plus(nxt,(s+1)+",0",v*weights.x);
    }
    cur=nxt;
  }
  return out;
}
function ordinaryDP(w,N,weights){
  let cur=new Map([[0,1n]]),out=[];
  for(let n=0;n<=N;n++){
    out.push(cur);
    if(n===N)break;
    const nxt=new Map();
    for(const [q,v] of cur)for(const c of ORD)plus(nxt,transition(w,q,c),v*weights[c]);
    cur=nxt;
  }
  return out;
}
function orderedBrute(w,n,weights){
  const result=new Map();
  function visit(word,s,mass){
    if(word.length===n){
      const tail=word.split("x").at(-1);
      let q=0;
      for(let j=w.length;j>=0;j--)if(tail.endsWith(w.slice(0,j))){q=j;break}
      plus(result,s+","+q,mass);
      return;
    }
    for(const c of ORD)visit(word+c,s,mass*weights[c]);
    if(word===""||word.endsWith(w))visit(word+"x",s+1,mass*weights.x);
  }
  visit("",0,1n);
  return result;
}
function totals(cur){
  let a=0n;for(const v of cur.values())a+=v;return a;
}
function profile(cur,k){
  let v=Array(k+1).fill(0n);
  for(const [key,mass] of cur){
    let q=+key.split(",")[1];v[q]+=mass;
  }
  return v;
}
const log=[];
for(const w of WORDS){
  const k=w.length;
  for(const [label,weights] of [["count",ONE],["positive",POS]]){
    const A=ORD.reduce((a,c)=>a+weights[c],0n);
    const Q=[...w].reduce((a,c)=>a*weights[c],1n);
    const N=16,raw=wordsDP(w,N,weights),r=ordinaryDP(w,N,weights);
    const L=[],H=[];
    for(let n=0;n<=N;n++){
      let v=(n===0?1n:0n)+(n===1?weights.x:0n);
      if(n>0)v+=A*L[n-1];
      if(n>=k+1)v+=weights.x*Q*L[n-k-1];
      L.push(v);H.push(v-(n>0?A*L[n-1]:0n));
    }
    for(let n=0;n<=N;n++){
      check(totals(raw[n])===L[n],"L "+w+" "+label+" "+n);
      for(let s=0;s<=n;s++){
        let actual=0n;
        for(const [key,v] of raw[n])if(+key.split(",")[0]===s)actual+=v;
        check(actual===bi(n,s,k,A,Q)*weights.x**BigInt(s),"M "+w+" "+label+" "+n+" "+s);
      }
      for(let q=0;q<=k;q++){
        let actual=0n,expected=0n;
        for(const [key,v] of raw[n])if(+key.split(",")[1]===q)actual+=v;
        for(let t=0;t<=n;t++)expected+=H[n-t]*(r[t].get(q)||0n);
        check(actual===expected,"R "+w+" "+label+" "+n+" "+q);
      }
      if(n<=4){
        const actual=orderedBrute(w,n,weights),expected=raw[n];
        check(actual.size===expected.size,"brute size "+w+" "+n);
        for(const [key,v] of actual)check(v===expected.get(key),"brute "+w+" "+n+" "+key);
      }
    }
    log.push("PASS word="+w+" "+label+" n=0..16 recurrence/bivariate/KMP; ordered brute n=0..4; L8="+L[8]);
    if(label==="count"&&["aab","aba"].includes(w))log.push("N8 "+w+" suffix_counts="+profile(raw[8],k).join(","));
    if(label==="positive"&&["aab","aba"].includes(w))log.push("N8 "+w+" suffix_positive="+profile(raw[8],k).join(","));
  }
}
for(const weights of [ONE,POS]){
  const a=wordsDP("aab",12,weights),b=wordsDP("aba",12,weights);
  for(let n=0;n<=12;n++)check(totals(a[n])===totals(b[n]),"anagram invariant");
  check(profile(a[8],3).some((v,j)=>v!==profile(b[8],3)[j]),"suffix witness");
}
log.push("ANAGRAM aab versus aba: totals identical for n=0..12, suffix distributions different at n=8.");
log.push("ALL_CHECKS_PASS");
return log.join("\n")+"\n";
}
if(typeof module !== "undefined" && require.main === module) console.log(executedPrefix479Certificate());
