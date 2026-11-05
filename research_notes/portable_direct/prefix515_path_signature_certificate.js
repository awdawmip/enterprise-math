"use strict";
// PREFIX-515 executable exact integer signed-path BRC/KMP/source certificate.
const ALPH = "aAbBcCdDeE";
const COLOR = [0,4,1,2,3,3,4,4,4,4];
const GATES = {aab:[0,0,1], aba:[0,1,0]};
const STEP = Object.fromEntries([...ALPH].map((c,i)=>[c,{axis:Math.floor(i/2),sign:i%2?-1:1,color:COLOR[i]}]));
function kmp(g,q,c) {
  const p=GATES[g],s=p.slice(0,q).concat([STEP[c].color]);
  for(let k=3;k>=1;k--)if(s.length>=k&&s.slice(-k).every((x,i)=>x===p[i]))return k;
  return 0;
}
function transition(w,g) {
  let a=[0,1,2,3];
  for(const c of w)a=a.map(q=>kmp(g,q,c));
  return a;
}
function signature(w,g) {
  const y=[0,0,0,0,0],vweights=[0,1,0,2,1],wweights=[0,0,1,0,1];
  let V=0,W=0,first="N",last="N";
  for(const c of w) {
    const {axis:i,sign:d}=STEP[c];
    if(y[i]*d<0){V+=vweights[i];W+=wweights[i];}
    y[i]+=d;
    if(i===1||i===2){const s=i===1?"B":"C";if(first==="N")first=s;last=s;}
  }
  return {n:w.length,y,V,W,T:transition(w,g),R:transition([...w].reverse().join(""),g),first,last};
}
function merge(a,b) {
  const k=a.y.map((x,i)=>(Math.abs(x)+Math.abs(b.y[i])-Math.abs(x+b.y[i]))/2);
  if(k.some(x=>!Number.isInteger(x)||x<0))throw Error("bad cancellation cocycle");
  return {n:a.n+b.n,y:a.y.map((x,i)=>x+b.y[i]),
    V:a.V+b.V+k[1]+2*k[3]+k[4],W:a.W+b.W+k[2]+k[4],
    T:a.T.map(q=>b.T[q]),R:b.R.map(q=>a.R[q]),
    first:a.first!=="N"?a.first:b.first,last:b.last!=="N"?b.last:a.last};
}
function rev(s){return {n:s.n,y:s.y,V:s.V,W:s.W,T:s.R,R:s.T,first:s.last,last:s.first};}
function cref(s){const y=s.y.slice();y[2]=-y[2];return {...s,y};}
function swapc(w){return [...w].map(c=>c==="c"?"C":c==="C"?"c":c).join("");}
function obs(s){return {n:s.n,y:s.y,V:s.V,W:s.W,q:s.T[0],t:s.first};}
function equal(a,b){return JSON.stringify(a)===JSON.stringify(b);}
function check(ok,tag){if(!ok)throw Error(tag);}
function run(){
  let out={status:"ALL_CHECKS_PASS",scientific_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    alphabet:ALPH,gates:{},minimal_witnesses:{}};
  const ws=[[""]];
  for(let n=1;n<=4;n++)ws.push(ws[n-1].flatMap(w=>[...ALPH].map(c=>w+c)));
  for(const gate of Object.keys(GATES)){
    const cache=new Map(ws.flat().map(w=>[w,signature(w,gate)]));
    let revs=0,refs=0,comps=0,pairs=0;
    for(const [w,s] of cache) {
      check(equal(rev(s),signature([...w].reverse().join(""),gate)),gate+":reverse:"+w);revs++;
      check(equal(cref(s),signature(swapc(w),gate)),gate+":reflect:"+w);
      check(equal(cref(rev(s)),rev(cref(s))),gate+":involution:"+w);refs++;
    }
    for(let n=0;n<=4;n++)for(let j=0;j<=n;j++)
      for(const u of ws[j])for(const v of ws[n-j]){
        check(equal(merge(cache.get(u),cache.get(v)),cache.get(u+v)),gate+":merge:"+u+"/"+v);comps++;
      }
    for(let n=0;n<=2;n++){
      const seen=new Map();
      for(const w of ws[n]){
        const o=JSON.stringify(obs(cache.get(w))),rr=obs(rev(cache.get(w)));
        if(seen.has(o)){check(equal(seen.get(o),rr),gate+":short obstruction:"+w);pairs++;}
        else seen.set(o,rr);
      }
    }
    const o1=obs(cache.get("bbc")),o2=obs(cache.get("bcb"));
    const r1=obs(rev(cache.get("bbc"))),r2=obs(rev(cache.get("bcb")));
    check(equal(o1,o2)&&!equal(r1,r2),gate+":witness");
    out.minimal_witnesses[gate]={words:["bbc","bcb"],same_observer:o1,
      reversed_words:["cbb","bcb"],reversed_observers:[r1,r2],minimal_length:3};
    out.gates[gate]={words_tested:cache.size,reverse_tests:revs,c_reflection_tests:refs,
      exhaustive_concat_splits:comps,short_fiber_pairs:pairs};
  }
  return out;
}
if(typeof module!=="undefined" && require.main===module)console.log(JSON.stringify(run(),null,2));
