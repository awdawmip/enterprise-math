// PREFIX-522 exact certificate. Node.js, no dependencies; signed integers only.
"use strict";
function runCertificate() {
  const check=(ok,why)=>{if(!ok)throw Error(why)};
  const E=[[0,1],[2,3],[0,2],[1,3],[1,2],[0,3]];
  const S=[[0,2,5],[0,3,4],[1,2,4],[1,3,5]];
  function perms(a) {
    if(!a.length)return [[]];
    return a.flatMap((v,i)=>perms(a.filter((_,j)=>i!==j)).map(p=>[v,...p]));
  }
  const MAPS=perms([0,1,2,3]).map(g=>E.map(pair=>{
    const p=pair.map(v=>g[v]).sort((a,b)=>a-b);
    return E.findIndex(e=>e[0]===p[0]&&e[1]===p[1]);
  }));
  const neigh=(star,phase)=>S[star].filter(a=>a!==Math.abs(phase)-1)
    .map(a=>(phase>0?-1:1)*(a+1));
  function successors(s) {
    const keep=neigh(s[0],s[2]).filter(z=>z!==s[1]).map(z=>[s[0],s[2],z]);
    const j=S.findIndex((axes,i)=>i!==s[0]&&axes.includes(Math.abs(s[2])-1));
    const sw=neigh(j,s[2]).map(z=>[j,s[2],z]);
    check(keep.length===1&&sw.length===2,"three phase exits");
    return keep.concat(sw);
  }
  const STATES=[];
  for(let star=0;star<4;star++)
    for(const a of S[star])for(const sign of [-1,1]) {
      const now=sign*(a+1);
      for(const prev of neigh(star,now))STATES.push([star,prev,now]);
    }
  const key=s=>s.join(",");
  check(STATES.length===48&&new Set(STATES.map(key)).size===48,"48 states");
  const indeg=new Map(STATES.map(s=>[key(s),0]));
  for(const s of STATES)for(const t of successors(s))
    indeg.set(key(t),indeg.get(key(t))+1);
  check([...indeg.values()].every(n=>n===3),"3 incoming phase exits each");
  const micro=(old,nxt,b)=>b===0?[-old,nxt]:[nxt,-old];
  function letter(x,map) {
    const a=map[Math.abs(x)-1];
    if(a===0)return x>0?"a":"A";
    if(a===1)return x>0?"b":"B";
    if(a===2)return "c";
    return "_";
  }
  function q(word) {
    const pat="aAc";
    for(let k=3;k>0;k--)if(word.endsWith(pat.slice(0,k)))return k;
    return 0;
  }
  function target(map) {
    const a=map.indexOf(0)+1,c=map.indexOf(2)+1;
    const st=S.findIndex(axes=>axes.includes(a-1)&&axes.includes(c-1));
    check(st>=0,"unique common STAR");
    return [st,a,-c];
  }
  function quotient(st,bprev,bnow,last,map) {
    if(last>0&&map[last-1]===0)return 1;
    return bprev===0&&bnow===0&&key(st)===key(target(map))?3:0;
  }
  const localHits=[],q1local=[];
  let localChecks=0;
  for(const map of MAPS) {
    let hit=0,q1count=0;
    for(const s of STATES)for(const t of successors(s))for(let b=0;b<2;b++) {
      const first=micro(s[2],t[2],b);
      const word=first.map(x=>letter(x,map)).join("");
      const qfirst=q(word);
      if(qfirst===1)q1count++;
      check(qfirst===quotient(t,-1,b,first[1],map),"first block");
      for(const u of successors(t))for(let c=0;c<2;c++) {
        const second=micro(t[2],u[2],c);
        const w=word+second.map(x=>letter(x,map)).join("");
        const actual=q(w),pred=quotient(u,b,c,second[1],map);
        check(actual===pred&&actual!==2,"two-macro KMP descent");
        localChecks++;
        if(actual===3) {
          check(b===0&&c===0&&key(u)===key(target(map)),"inner-inner suffix");
          hit++;
        }
      }
    }
    check(hit===9&&q1count===24,"9/24 exact local counts");
    localHits.push(hit);q1local.push(q1count);
  }
  const hist=[],occTotals=[];
  let fullChecks=0;
  for(const map of MAPS) {
    const cnt=Array.from({length:4},()=>[0,0,0,0]);
    const occ=[0,0,0,0];
    function walk(st,path,branches,d) {
      const w=path.map(x=>letter(x,map)).join(""),actual=q(w);
      cnt[d][actual]++;
      for(let i=0;i+3<=w.length;i++)if(w.slice(i,i+3)==="aAc")occ[d]++;
      if(d) {
        const bprev=d<2?-1:branches[d-2],bnow=branches[d-1];
        check(actual===quotient(st,bprev,bnow,path[path.length-1],map),"long suffix descent");
      }
      fullChecks++;
      if(d===3)return;
      for(const t of successors(st))for(let b=0;b<2;b++)
        walk(t,path.concat(micro(st[2],t[2],b)),branches.concat(b),d+1);
    }
    for(const s of STATES)walk(s,[],[],0);
    for(let d=0;d<=3;d++) {
      const all=48*6**d,one=d?24*6**(d-1):0;
      const three=d>=2?9*6**(d-2):0;
      const occurrences=d>=2?(d-1)*9*6**(d-2):0;
      check(cnt[d].reduce((x,y)=>x+y,0)===all,"all histories");
      check(cnt[d][1]===one&&cnt[d][2]===0&&cnt[d][3]===three,"closed-form KMP histogram");
      check(occ[d]===occurrences,"closed-form occurrence count");
    }
    hist.push(cnt);occTotals.push(occ);
  }
  const s0=[0,3,-6],s1=[0,-6,1],s2=[0,1,-3],map=MAPS[0];
  check(successors(s0).some(x=>key(x)===key(s1)),"witness edge 1");
  check(successors(s1).some(x=>key(x)===key(s2)),"witness edge 2");
  const good=micro(s0[2],s1[2],0).concat(micro(s1[2],s2[2],0));
  const bad=micro(s0[2],s1[2],1).concat(micro(s1[2],s2[2],0));
  check(q(good.map(x=>letter(x,map)).join(""))===3,"hit witness");
  check(q(bad.map(x=>letter(x,map)).join(""))===0,"non-hit with identical terminal macro");
  return {
    verdict:"ALL_CHECKS_PASS",
    model:"PREFIX-518 four-STAR symbolic candidate macrograph; gate aAc; KMP q0; all 24 S4 charts",
    states:48,charts:MAPS.length,exits_per_state:3,branches_per_state:6,
    indegrees_3:indeg.size,two_macro_histories_per_chart:1728,
    local_checks_all_frames:localChecks,gate_hits_per_chart:localHits,
    one_macro_q1_per_chart:q1local,
    total_histories_checked_all_frames_all_depths_0_to_3:fullChecks,
    depth_histogram_per_chart:hist[0],indexed_occurrences_per_chart:occTotals[0],
    all_charts_match:hist.every(h=>JSON.stringify(h)===JSON.stringify(hist[0]))
      &&occTotals.every(h=>JSON.stringify(h)===JSON.stringify(occTotals[0])),
    local_gate_event_fraction:"1/192",
    witness:{phases:[s0,s1,s2],good_signed:good,bad_signed:bad,
      good_color:good.map(x=>letter(x,map)).join(""),
      bad_color:bad.map(x=>letter(x,map)).join("")},
    arithmetic:"Exact bounded integer/combinatorial enumeration; no floating point"
  };
}
const result=runCertificate();
if(typeof console!=="undefined")console.log(JSON.stringify(result,null,2));
