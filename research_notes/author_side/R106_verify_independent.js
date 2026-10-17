#!/usr/bin/env node
"use strict";
const result=(function verifyR106() {
  const S=[-4,0,1,2,4], S3=[0,1,2,4], D=[-8,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,8];
  const T=new Set([-8,-4,-3,-2,0,2,3,4,8]);
  const slot=new Map([[0,1],[1,3],[4,4],[2,7],[-4,8]]);
  const rep=new Map();
  function check(x,msg) { if(!x)throw new Error(msg); }
  for(const d of D) {
    let pair=null;
    for(const a of S)for(const b of S) {
      if(a-b===d&&(!T.has(d)||(a===4||b===4))&&pair===null)pair=[a,b];
    }
    check(!!pair,"missing pair "+d);
    rep.set(d,pair);
  }
  function prefix(d2,s3,s4,d5,d6) {
    const b=Array.from({length:9},()=>[]);
    b[slot.get(s3)].push(3);
    b[slot.get(s4)].push(4);
    for(const [j,d] of [[2,d2],[5,d5],[6,d6]]) {
      const [a,c]=rep.get(d);
      if(a===c) {check(a===4,"equal stages");b[4].push(j);b[5].push(-j);}
      else {b[slot.get(a)].push(j);b[slot.get(c)].push(-j);}
    }
    check(b[4].length>0,"bridge missing");
    check(s3!==-4||s4===-4,"bad end");
    let p=[];
    const h=[1,1,1,1,-1,-1,-1,-1];
    for(let k=1;k<=8;k++) {
      p.push(h[k-1]);
      p.push(...b[k].sort((x,y)=>Math.abs(x)-Math.abs(y)));
    }
    check(p.length===16&&p[0]===1&&p[15]!==3,"prefix boundary");
    for(let k=0;k<15;k++)check(p[k]!==-p[k+1],"prefix reduction");
    return p;
  }
  const suffix={2:[-3,2,2,-4,-2,-2],3:[3,3,-4,-3,-3,-3],4:[4,4,-3,-4,-4,-4],5:[-3,5,5,-4,-5,-5],6:[-3,6,6,-4,-6,-6]};
  function directCount(w,pat) {
    const dp=[1,0,0,0,0];
    for(const x of w)for(let i=4;i>=1;i--)if(x===pat[i-1])dp[i]+=dp[i-1];
    return dp[4];
  }
  function independent(w,l) {
    return directCount(w,[1,1,1,l])-directCount(w,[1,1,1,-l])
      -2*directCount(w,[-1,-1,-1,l])+2*directCount(w,[-1,-1,-1,-l]);
  }
  function c3(x){return x>=3?x*(x-1)*(x-2)/6:0;}
  function streaming(w,l) {
    let p=0,m=0,z=0;
    for(const x of w){
      const f=c3(p)-2*c3(m);
      if(x===l)z+=f;
      else if(x===-l)z-=f;
      if(x===1)p++;
      else if(x===-1)m++;
    }
    return z;
  }
  function admissible(w,l) {
    if(w.length!==22)return false;
    const pos=Array(7).fill(0),neg=Array(7).fill(0);
    for(let i=0;i<22;i++) {
      if(w[i]===-w[(i+1)%22])return false;
      if(w[i]>0)pos[w[i]]++;
      else neg[-w[i]]++;
    }
    if(pos[1]!==4||neg[1]!==4||pos[l]!==3||neg[l]!==3)return false;
    for(let i=2;i<=6;i++) {
      if(i===l)continue;
      if(pos[i]!==1||neg[i]!==1)return false;
    }
    return true;
  }
  const seen=new Set(),counts={A:0,B:0};
  let completions=0;
  let example=null;
  function one(cls,d2,s3,s4,d5,d6) {
    const p=prefix(d2,s3,s4,d5,d6);
    const want=[d2,s3+4,s4+4,d5,d6],got=[];
    const key=want.join(",");
    check(!seen.has(key),"duplicate response signature");
    seen.add(key);
    for(let l=2;l<=6;l++) {
      const w=p.concat(suffix[l]);
      check(admissible(w,l),"not CYCL "+key+"/"+l);
      const a=streaming(w,l),b=independent(w,l);
      check(a===b&&a===want[l-2],"source disagreement "+key+"/"+l);
      got.push(a);
      completions++;
    }
    counts[cls]++;
    if(example===null)example={prefix:p,responses:got,full_l2:p.concat(suffix[2])};
  }
  for(const d2 of D)for(const d5 of D)for(const d6 of D) {
    const bridge=T.has(d2)||T.has(d5)||T.has(d6);
    for(const s3 of S3)for(const s4 of S) {
      if(bridge||s3===4||s4===4)one("A",d2,s3,s4,d5,d6);
    }
    if(bridge)one("B",d2,-4,-4,d5,d6);
  }
  check(counts.A===64908&&counts.B===3159,"class counts");
  check(seen.size===68067&&completions===340335,"total counts");
  return {schema:"EM_R106_INDEPENDENT_JS_EXHAUSTION_V1",
          verdict:"R106_ONLINE_17BIT_INDEPENDENT_JS_PASS",
          domain:"CYCL subset of signed X6 C22 (4,3,1,1,1,1)",
          cut:16,suffix_size:6,classes:counts,
          distinguishable_prefixes:seen.size,legal_completions:completions,
          lower_bound_bits:17,source_algorithms:["ordered fourth-level DP","prefix combinatorial f-score"],
          example,author_side_unreviewed:true};
})();
console.log(JSON.stringify(result,null,2));
