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
  function H2Keys(h){const s=new Set();for(let z=1;z<=Math.floor((h+1)/2);z++){let rem=h-(2*z-1);for(let r=1;r<=rem;r++)for(let f=0;f<=rem-r;f++){let g=rem-r-f;s.add([2*z+r+f,r+g,z].join(","));}}return s;}
  function H2Words(h,K){let [x,y,z]=K.split(",").map(Number),r=x+y-h-1,f=h+1-y-2*z,g=h+1-x;const words=[];if(z<1||r<1||f<0||g<0)return words;
    for(let root of B2){let allowed=(root==="de"||root==="ed")?"d":"c", counts={a:z-1,e:z-1,f,g};counts[allowed]=r-1;const chars=Object.keys(counts).filter(k=>counts[k]>0);
      function go(prefix,left){if(left===0){words.push(root+prefix);return;}for(let ch of chars)if(counts[ch]>0){counts[ch]--;go(prefix+ch,left-1);counts[ch]++;}}
      go("",h-2);
    }return words;}
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
  const H2_8=H2Keys(8),H2_9=H2Keys(9);
  if(H2_8.size!==50||H2_9.size!==70)throw Error("wrong H2 key counts");
  let cases=[];
  for(const [cid,src] of Object.entries(CASES)){
    stepCache=new Map();obsCache=new Map();
    const byH={2:B2,3:B3,...src}, base=[];for(let h=2;h<=7;h++)base.push(...byH[h]);
    const P0=prefixes(base);if(P0.size!==72)throw Error("base prefix mismatch");
    let oldKeys=new Set(base.map(key));if(oldKeys.size!==4)throw Error("old keys mismatch");
    let groups={8:new Map(),9:new Map()};
    for(const h of [8,9])for(const h0 of [3,4,5,6])for(const root of byH[h0])for(const suf of ZERO[h-h0]){
      let w=root+suf, m=S.get(observer(w));if(m===undefined)continue;let k=key(w);
      if(!groups[h].has(k))groups[h].set(k,new Map());groups[h].get(k).set(w,m);
    }
    function capable(g){const s=new Set();for(const [k,vs] of g){let m=0;for(const v of vs.values())m|=v;if(rank9(m))s.add(k);}return s;}
    const cap8=capable(groups[8]),cap9=capable(groups[9]);
    let poss8=new Set([...cap8,...H2_8]),poss9=new Set([...cap9,...H2_9]);
    if([...oldKeys].some(k=>poss8.has(k)||poss9.has(k)))throw Error("old key still rank9 possible");
    let common=[...poss8].filter(k=>poss9.has(k)).sort((a,b)=>{
      const x=a.split(",").map(Number),y=b.split(",").map(Number);
      for(let i=0;i<3;i++)if(x[i]!==y[i])return x[i]-y[i];return 0;});
    if(common.length!==50)throw Error("unexpected joint key count: "+common.length);
    let rec=[],h2sum8=0,h2sum9=0;
    for(const K of common){
      let pools={8:new Map(groups[8].get(K)||[]),9:new Map(groups[9].get(K)||[])};
      for(const h of [8,9]){let h2=H2Words(h,K);for(const w of h2){
        const m=S.get(observer(w));if(m===undefined||m!==S.get(observer(w.slice(0,2)))||key(w)!==K||net(w)!=="2,0,0,0,0,0")throw Error("invalid H2 word "+w);
        pools[h].set(w,m);
      }if(h===8)h2sum8+=h2.length;else h2sum9+=h2.length;
      }
      const [d8,n8]=exactMin(pools[8],P0);
      const free9=new Set([...P0,...prefixes(pools[8].keys())]);
      const [d9,n9]=exactMin(pools[9],free9);
      rec.push({key:K.split(",").map(Number),d8,d9,lower_bound:72+d8+d9,words8:pools[8].size,words9:pools[9].size,nodes8:n8,nodes9:n9});
    }
    if(h2sum8!==15956||h2sum9!==48048)throw Error("wrong H2 shared-key totals");
    const mn=Math.min(...rec.map(r=>r.lower_bound)), winners=rec.filter(r=>r.lower_bound===mn);
    if(mn!==94||winners.length!==1||Math.min(...rec.map(r=>r.d8))!==16||Math.min(...rec.map(r=>r.d9))!==6)throw Error("bound discrepancy");
    const w8=byH[7].flatMap(w=>[w+"c",w+"d"]),w9=byH[7].map(w=>w+"fg");
    if(prefixes([...base,...w8,...w9]).size!==94)throw Error("witness cost mismatch");
    for(const hwords of [w8,w9]){let m=0;for(const w of hwords)m|=S.get(observer(w));if(!rank9(m))throw Error("witness rank");}
    cases.push({case:Number(cid),base_edges:72,full_common_keys:50,H2_h8_in_common:h2sum8,H2_h9_in_common:h2sum9,min_lower_bound:mn,attaining_key:winners[0].key,attaining_d8:winners[0].d8,attaining_d9:winners[0].d9,classes_below_94:rec.filter(r=>r.lower_bound<94).length,exact_key_certificates:rec});
  }
  return {status:"PASS_AUTHOR_SIDE_EXACT_INTEGER",date:"2026-11-05",frozen_science_pin:"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",model:"signed native X6 7-operation BRC, nine histories, six original signatures",scope:"Four fixed H2..H7 schedules; H8,H9 independently extend selected H2..H6 roots",rank_criterion:"(E|F)&(C|F)&(D|G)&(J|G)",zero_suffix_counts:{2:18,3:88,4:454,5:2424,6:13236},H2_h8_all_keys:50,H2_h9_all_keys:70,case_count:cases.length,key_cases:cases.reduce((n,c)=>n+c.full_common_keys,0),cases};
};
const result=run();
console.log(JSON.stringify(result,null,2));
