// EC49FAU: complete unrestricted native-X6 late-word exact optimizer. Reuses the pinned EC49FAT observer/trie algebra; changes candidate generator to ALL valid ordered operation words. Node.js >= 18, no dependencies.
const run = function run(){
  const OPS={a:[-1,-1],b:[-2,-2],c:[1,2,-1,-2],d:[2,1,-2,-1],e:[3,1,1,-3],f:[1,-1],g:[2,-2]};
  const B2=["de","ed","ce","ec"], B3=["feg","gef"];
  const CASES={
    1512:{4:["defg","edfg","fegc","gefc"],5:["fegfg","geffg"],6:["fegfgg","geffgg"],7:["fegfggg","geffggg"]},
    1513:{4:["defg","edfg","fegc","gefc"],5:["fegfg","geffg"],6:["fegfgf","geffgf"],7:["fegfgff","geffgff"]},
    2200:{4:["fegg","gefg"],5:["feggd","gefgd","feggc","gefgc"],6:["fegggf","gefggf"],7:["fegggfg","gefggfg"]},
    2203:{4:["fegf","geff"],5:["fegfd","geffd","fegfc","geffc"],6:["fegfgf","geffgf"],7:["fegfgff","geffgff"]}
  };
  const START=[["N",0],["N",1],["N",2],["A",0],["A",2],["B",0],["B",1],["AB",0],["BA",0]], BUCKET=["N","A","B","AB","BA"];
  const sigNames=["de","ed","ce","ec","feg","gef"], sigVals=[];
  let stepCache=new Map(), obsCache=new Map();
  function steps(w){let a=stepCache.get(w);if(a)return a;a=[];for(let i=0;i<w.length;i++)a.push(...OPS[w[i]]);stepCache.set(w,a);return a;}
  function observer(w){let got=obsCache.get(w);if(got)return got;const st=steps(w),out=[];for(const [state0,prev0] of START){let state=state0,prev=prev0;for(const s of st){if(prev===1 && s===2){if(state==="N")state="A";else if(state==="B")state="BA";}else if(prev===2 && s===1){if(state==="N")state="B";else if(state==="A")state="AB";}prev=s;}out.push(BUCKET.indexOf(state));}got=out.join(",");obsCache.set(w,got);return got;}
  sigNames.forEach(w=>sigVals.push(observer(w)));const S=new Map(sigVals.map((v,i)=>[v,1<<i]));
  if(S.size!==6)throw Error("signature collision");
  const D=1,E=2,C=4,J=8,F=16,G=32;
  function rank9(m){return Boolean((m&(E|F))&&(m&(C|F))&&(m&(D|G))&&(m&(J|G)));}
  function key(w){const k=[0,0,0];for(const s of steps(w))if(s>0)k[s-1]++;return k.join(",");}
  function net(w){const n=[0,0,0,0,0,0];for(const s of steps(w))n[Math.abs(s)-1]+=s>0?1:-1;return n.join(",");}
  function zeroSuffix(n){let result=[];function go(prefix,a,e){if(prefix.length===n){if(a===e)result.push(prefix);return;}for(const ch of "acdefg")go(prefix+ch,a+(ch==="a"),e+(ch==="e"));}go("",0,0);return result;}
  const ZERO={};for(let n=2;n<=6;n++)ZERO[n]=zeroSuffix(n);
  if([ZERO[2].length,ZERO[3].length,ZERO[4].length,ZERO[5].length,ZERO[6].length].join(",")!=="18,88,454,2424,13236")throw Error("bad suffix census");

  // Exhaust all complete seven-symbol BRC operation words of length h and full key K.
  // Net +2*E1 fixes #b=0, #e=#a+1. The other counts follow exactly from h and K.
  function allKeys(h){const out=[];for(let z=1;2*z-1<=h;z++){const t=h-(2*z-1);for(let r=0;r<=t;r++)for(let f=0;f<=t-r;f++){const g=t-r-f;out.push([2*z+r+f,r+g,z].join(","));}}return [...new Set(out)];}
  function allWords(h,K){const [x,y,z]=K.split(",").map(Number),r=x+y-h-1,f=h+1-y-2*z,g=h+1-x;
    const out=new Map();if(z<1||r<0||f<0||g<0)return out;
    const counts={a:z-1,e:z,f:f,g:g};
    function rec(w,m){if(w.length===h){if(m!==0)return;let sig=S.get(observer(w));if(sig!==undefined){if(key(w)!==K||net(w)!=="2,0,0,0,0,0")throw Error("candidate invalid "+w);out.set(w,sig);}return;}
      for(const ch of "acdefg"){if(ch==="c"||ch==="d"){if(m>0)rec(w+ch,m-1);}else if(counts[ch]>0){counts[ch]--;rec(w+ch,m);counts[ch]++;}}
    }rec("",r);return out;
  }
  function prefixes(words){const p=new Set();for(let w of words){let s="";for(const v of steps(w)){s+=v+",";p.add(s);}}return p;}
  function exactMin(pool,free){
    const root={ch:new Map(),end:0,free:true};let nodes=0;
    for(const [w,mask] of pool){let node=root,pre="";for(const s of steps(w)){pre+=s+",";if(!node.ch.has(s)){node.ch.set(s,{ch:new Map(),end:0,free:free.has(pre)});nodes++;}node=node.ch.get(s);}node.end|=mask;}
    function dp(node){let d=new Map([[0,0]]);if(node.end)d.set(node.end,0);
      for(const child of node.ch.values()){let x=dp(child),nd=new Map();for(const [a,ca] of d)for(const [b,cb] of x){const m=a|b, v=ca+cb;if(!nd.has(m)||v<nd.get(m))nd.set(m,v);}d=nd;}
      if(!node.free)for(const [m,v] of d)if(m)d.set(m,v+1);return d;
    }
    let ans=Infinity;for(const [m,v] of dp(root))if(rank9(m))ans=Math.min(ans,v);if(!Number.isFinite(ans))throw Error("rank9 unattainable");
    return [ans,nodes];
  }

  const k8=allKeys(8), k9=new Set(allKeys(9)), common=k8.filter(k=>k9.has(k)).sort((a,b)=>{
    const x=a.split(",").map(Number),y=b.split(",").map(Number);for(let i=0;i<3;i++)if(x[i]!==y[i])return x[i]-y[i];return 0;
  });
  if(k8.length!==70||k9.size!==95||common.length!==50)throw Error("complete key enumeration error");
  const cases=[];
  for(const [cid,src] of Object.entries(CASES)){
    const byH={2:B2,3:B3,...src},base=[];for(let h=2;h<=7;h++)base.push(...byH[h]);
    const P0=prefixes(base);if(P0.size!==72)throw Error("base prefix mismatch");
    const oldKeys=new Set(base.map(key));if(oldKeys.size!==4)throw Error("early key budget mismatch");
    const records=[];
    for(const K of common){
      stepCache=new Map();obsCache=new Map();
      const W8=allWords(8,K),W9=allWords(9,K);
      if(!W8.size||!W9.size)throw Error("unexpected empty common pool "+K);
      let mask8=0,mask9=0;for(const m of W8.values())mask8|=m;for(const m of W9.values())mask9|=m;
      if(!rank9(mask8)||!rank9(mask9)||oldKeys.has(K))throw Error("unqualified key "+K);
      const [d8,n8]=exactMin(W8,P0);
      const all8prefixes=prefixes(W8.keys());
      const [d9plus,n9]=exactMin(W9,new Set([...P0,...all8prefixes]));
      records.push({key:K.split(",").map(Number),d8,d9_plus:d9plus,lower_bound:72+d8+d9plus,words8:W8.size,words9:W9.size,nodes8:n8,nodes9:n9});
    }
    const min=Math.min(...records.map(r=>r.lower_bound));
    const winners=records.filter(r=>r.lower_bound===min);
    if(records.length!==50||min!==94||winners.length!==1||Math.min(...records.map(r=>r.d8))!==16||Math.min(...records.map(r=>r.d9_plus))!==6)throw Error("bound discrepancy "+cid);
    const w8=byH[7].flatMap(w=>[w+"c",w+"d"]),w9=byH[7].map(w=>w+"fg");
    const full=[...base,...w8,...w9],pref=prefixes(full),fullKeys=new Set(full.map(key)),fullS=new Set();
    if(pref.size!==94||fullKeys.size!==5)throw Error("witness wrong resources "+cid);
    for(const hwords of [...Array.from({length:6},(_,i)=>byH[i+2]),w8,w9]){
      let m=0;for(const w of hwords){if(net(w)!=="2,0,0,0,0,0")throw Error("witness net "+w);
        const v=S.get(observer(w));if(v===undefined)throw Error("witness signature "+w);m|=v;fullS.add(v);
      }if(!rank9(m))throw Error("witness rank");
    }
    if(fullS.size!==6)throw Error("witness six-signature mismatch");
    cases.push({case:Number(cid),baseline_prefix_edges:72,eligible_fifth_key_classes:50,min_lower_bound:min,attaining_key:winners[0].key,attaining_d8:winners[0].d8,attaining_d9_plus:winners[0].d9_plus,upper_witness_edges:pref.size,records});
  }
  return {status:"PASS_AUTHOR_SIDE_EXACT_INTEGER",date:"2026-11-05",frozen_science_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    predecessor:"e00990837957c7022e57b44e8c9fa8ab386b9b21",
    scope:"Four fixed H2..H7 schedules; H8 and H9 any complete native seven-operation words with the original net, full keys and six observer signatures",
    rank_criterion:"(E|F)&(C|F)&(D|G)&(J|G)",all_keys_h8:k8.length,raw_keys_h9:k9.size,
    common_eligible_fifth_keys:common.length,total_case_key_classes:cases.length*common.length,minimum_edges:94,cases};
};
const result=run();
console.log(JSON.stringify(result,null,2));
