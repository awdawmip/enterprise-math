// PREFIX-815 exact named-source hub-release verifier.
// Pure integer JS, no dependencies; run: node research_notes/portable_direct/PREFIX815_R6_HUB_RELEASE_CHECK.js
"use strict";
const result=(function exactCheck() {
  "use strict";
  function insist(ok, msg) { if (!ok) throw new Error(msg); }
  function pop(x) { let n=0; while(x){n+=x&1; x>>=1;} return n; }
  function enumerate(n,q,pinMask,pinHub) {
    const edges=[];
    for(let i=1;i<=n;i++){
      edges.push({r:i,c:0,cap:1,tag:"a"+i});
      edges.push({r:i,c:i,cap:(pinMask&(1<<(i-1)))?0:1,tag:"b"+i});
      edges.push({r:0,c:i,cap:1,tag:"c"+i});
    }
    edges.push({r:0,c:0,cap:pinHub?0:q,tag:"h"});
    const m=edges.length, suffixR=Array.from({length:m+1},()=>Array(n+1).fill(0)),suffixC=Array.from({length:m+1},()=>Array(n+1).fill(0));
    for(let k=m-1;k>=0;k--){
      suffixR[k]=suffixR[k+1].slice(); suffixC[k]=suffixC[k+1].slice();
      suffixR[k][edges[k].r]+=edges[k].cap;
      suffixC[k][edges[k].c]+=edges[k].cap;
    }
    const rr=[n,...Array(n).fill(1)],cc=[n,...Array(n).fill(1)],x=Array(m).fill(0), states=new Map();
    let nodes=0;
    function dfs(k){
      nodes++;
      if(k===m){
        insist(rr.every(v=>v===0)&&cc.every(v=>v===0),"bad leaf");
        const t=Array.from({length:n},(_,i)=>x[3*i+1]);
        const key=t.join("");
        insist(!states.has(key),"duplicate source table "+key);
        states.set(key,{t,hub:x[m-1]});
        return;
      }
      const e=edges[k];
      for(let v=0;v<=e.cap && v<=rr[e.r] && v<=cc[e.c];v++){
        rr[e.r]-=v;cc[e.c]-=v;x[k]=v;
        let good=true;
        for(let j=0;j<=n;j++){
          if(rr[j]<0||cc[j]<0||rr[j]>suffixR[k+1][j]||cc[j]>suffixC[k+1][j]){good=false;break;}
        }
        if(good)dfs(k+1);
        rr[e.r]+=v;cc[e.c]+=v;
      }
    }
    dfs(0); return {states,nodes};
  }
  function sccCount(n,q,pinHub){
    const N=2*(n+1),reach=Array.from({length:N},(_,i)=>Array.from({length:N},(_,j)=>i===j));
    function arc(r,c,cap,x,move){if(!move)return;if(x<cap)reach[r][n+1+c]=true;if(x>0)reach[n+1+c][r]=true;}
    for(let i=1;i<=n;i++){arc(i,0,1,1,true);arc(i,i,1,0,true);arc(0,i,1,1,true);}
    arc(0,0,q,0,!pinHub);
    for(let k=0;k<N;k++)for(let i=0;i<N;i++)if(reach[i][k])for(let j=0;j<N;j++)if(reach[k][j])reach[i][j]=true;
    let count=0;
    for(let i=0;i<N;i++)if(!Array.from({length:i},(_,j)=>reach[i][j]&&reach[j][i]).some(Boolean))count++;
    return count;
  }
  const stats={schema:"PREFIX815_R6_HUB_RELEASE_REGRESSION_V1",frozen_science_pin:"f42f2906d77f24085c123f3ccfe9667d41caa96d",integer_arithmetic:"exact JS safe integers; n<=8; 0<=q<=n",families:0,unpin_cases:0,pinned_cases:0,source_tables_checked:0,search_nodes:0,hub_scc_checks:0,one_other_pin_cases:0,restricted_pin_cases:0,subset_support_assertions:0,rank_witness_checks:0,parity_observer_checks:0,max_family_n:8,max_eligible_count:0,verdict:""};
  for(let n=1;n<=8;n++)for(let q=0;q<=n;q++){
    const cases=[0];
    if(n<=6)for(let mask=1;mask<(1<<n);mask++)cases.push(mask);
    for(const mask of cases){
      const actual=enumerate(n,q,mask,false);
      const pinned=enumerate(n,q,mask,true);
      const allowed=[];
      for(let bits=0;bits<(1<<n);bits++)if(!(bits&mask)&&pop(bits)<=q)allowed.push(bits);
      insist(actual.states.size===allowed.length,`count n${n} q${q} m${mask}`);
      for(const bits of allowed){
        const key=Array.from({length:n},(_,i)=>(bits>>i)&1).join("");
        const s=actual.states.get(key);
        insist(!!s,`missing ${n}/${q}/${mask}/${key}`);
        insist(s.hub===pop(bits),`hub conservation ${key}`);
        stats.subset_support_assertions++;
      }
      insist(pinned.states.size===1&&pinned.states.has("0".repeat(n)),`pin not singleton ${n}/${q}/${mask}`);
      stats.source_tables_checked+=actual.states.size;
      stats.search_nodes+=actual.nodes+pinned.nodes;
      stats.families++;stats.unpin_cases++;stats.pinned_cases++;
      if(mask)stats.restricted_pin_cases++;
      if(pop(mask)===1)stats.one_other_pin_cases++;
      stats.max_eligible_count=Math.max(stats.max_eligible_count,allowed.length);
      const permitted=n-pop(mask);
      if(q===0)insist(actual.states.size===1,"zero q rank");
      else {
        for(let i=0;i<n;i++)if(!(mask&(1<<i))){
          const singleton="0".repeat(i)+"1"+"0".repeat(n-i-1);
          insist(actual.states.has(singleton),"standard basis missing");
          stats.rank_witness_checks++;
        }
      }
      if(mask===0){
        const before=sccCount(n,q,true),after=sccCount(n,q,false);
        insist(before===2*n+2,"pinned SCC count");
        insist(after===(q===0?2*n+2:1),"unpinned SCC count");
        stats.hub_scc_checks++;
      }
    }
  }
  const p=enumerate(2,1,0,false).states, seen=new Set();
  for(const state of p.values()){
    const [a,b]=state.t, u=a+b, v=a-b;
    insist(((u-v)%2)===0,"parity");
    seen.add(u+","+v);
    stats.parity_observer_checks++;
  }
  insist(seen.size===3&&seen.has("0,0")&&seen.has("1,1")&&seen.has("1,-1"),"parity witness");
  insist(Math.abs(1*(-1)-1*1)===2,"index 2");
  stats.verdict="ALL_EXACT_ASSERTIONS_PASSED";
  return stats;
})();
console.log(JSON.stringify(result,null,2));
