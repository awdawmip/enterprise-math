"use strict";
(function () {
  const acts=[
    {id:"alpha",m:7n,d:10n,w:[1n,1n,1n,7n]},
    {id:"beta",m:8n,d:11n,w:[1n,1n,1n,8n]}
  ];
  const edges=[[0,1],[0,2],[0,3],[1,2]], goodMasks=[3,5,9,6];
  function req(b,why){if(!b) throw new Error(why)}
  function p(a,k){return a**BigInt(k)}
  function N(x,y){
    req(x+y>=1,"nonempty history required");
    return p(8n,x)*p(9n,y)+3n*p(2n,x+y)-p(7n,x)*p(8n,y)-7n;
  }
  function inc(x,y,a){
    return 7n*(a.m+2n)+3n*p(7n,x)*p(8n,y)
      -3n*(a.m+1n)*p(2n,x+y)-2n*p(8n,x)*p(9n,y);
  }
  function allowed(i,e){
    return acts.every(a=>a.w[i]<=a.w[edges[e][0]]+a.w[edges[e][1]]);
  }
  function step(dp,a){
    const nx=Array(16).fill(0n);
    for(let mask=0;mask<16;mask++)for(let i=0;i<4;i++)
      nx[mask|(1<<i)]+=dp[mask]*a.w[i];
    return nx;
  }
  function occ(dp){return goodMasks.reduce((s,m)=>s+dp[m],0n)}
  const table=[],flows=[],failedCuts=[];
  for(let n=1;n<=4;n++)for(let x=0;x<=n;x++){
    const y=n-x;
    if(n<=3){
      const cut=3n*p(7n,x)*p(8n,y)-2n*p(8n,x)*p(9n,y);
      req(cut>0n,"expected forced heavy cut before length 4");
      failedCuts.push({x,y,strict_shortage:String(cut)});
    }
    const nv=acts.map(a=>inc(x,y,a));
    if(n===1)req(nv.every(v=>v>0n),"two samples strictly increase from one sample");
    if(n===2||n===3)req(nv.every(v=>v<0n),"length 2/3 strict decrease");
    if(n<=3)table.push({x,y,alpha:String(nv[0]),beta:String(nv[1])});
    if(n===4){
      const perAction={};
      for(const a of acts){
        const d=[3n*(a.m+2n),2n*(a.m+2n),2n*(a.m+2n),
          3n*p(7n,x)*p(8n,y)];
        const small=(a.m+1n)*p(2n,n);
        const cap=[small,small,2n*p(8n,x)*p(9n,y),small];
        const route=[0,3,1,2],used=[0n,0n,0n,0n];
        for(let i=0;i<4;i++){
          req(allowed(i,route[i]),"cross-action spectral transport order");
          used[route[i]]+=d[i];
        }
        const slack=cap.map((c,e)=>c-used[e]);
        req(slack.every(v=>v>0n),"all 4 edge slacks must be strictly positive");
        req(d.reduce((s,v)=>s+v,0n)-cap.reduce((s,v)=>s+v,0n)===inc(x,y,a),"signed spectrum identity");
        perAction[a.id]=slack.map(String);
      }
      flows.push({x,y,edge_order:["01","02","03","12"],strict_slack:perAction});
    }
  }
  req(acts.every(a=>[0,1,3].every(e=>!allowed(3,e))&&allowed(3,2)),"heavy can only use 03");
  let countWords=0,countNext=0,nodes=[{x:0,y:0,dp:[1n,...Array(15).fill(0n)]}];
  for(let n=1;n<=6;n++){
    const fresh=[];
    for(const parent of nodes)for(const a of acts){
      const dp=step(parent.dp,a);
      const x=parent.x+(a.id==="alpha"?1:0),y=parent.y+(a.id==="beta"?1:0);
      req(occ(dp)===N(x,y),"independent 16-mask DP versus closed form");
      countWords++;
      for(const b of acts){
        const after=step(dp,b);
        req(occ(after)-b.d*occ(dp)===inc(x,y,b),"independent next-step increment");
        countNext++;
      }
      fresh.push({x,y,dp});
    }
    nodes=fresh;
  }
  req(countWords===126&&countNext===252,"exhaustive word counts");
  function belongs(n,r){return n>=Math.max(2,4-r)}
  let recursiveChecks=0;
  for(let r=1;r<=3;r++)for(let n=1;n<=6;n++)for(let x=0;x<=n;x++){
    const y=n-x;
    const v=belongs(n,r-1)||acts.every(a=>inc(x,y,a)<=0n)
      &&acts.every(()=>belongs(n+1,r-1));
    req(v===belongs(n,r),"recursive predecessor classification");
    recursiveChecks++;
  }
  return {
    scope:"four-label two-action positive BRC auxiliary occupancy, not native P000",
    q_alpha:"(1,1,1,7)/10",q_beta:"(1,1,1,8)/11",
    good_edges:["01","02","03","12"],
    universal_claims_proved_analytically:[
      "cross-action transport K0 is upward closed",
      "each Kr is upward closed and sound",
      "finite-action predecessor chain stabilizes at some finite r for every fixed positive BRC model",
      "in this model K0={|c|>=4}, K1={|c|>=3}, K2=K3=...={|c|>=2}=S"
    ],
    finite_exact_checks:{
      heavy_cut_failures_count:failedCuts.length,
      negative_next_action_states_count:7,
      all_positive_strict_flow_certificates:flows.length*2,
      history_words_length_1_to_6:countWords,
      independent_support_mask_increment_checks:countNext,
      recurrence_membership_checks:recursiveChecks
    },
    increment_numerators_by_counts_length_1_to_3:table,
    short_length_heavy_cut_strict_shortages:failedCuts,
    length_4_positive_flow_slacks:flows,
    assumptions:"empty history has delta=0; N closed form used only for |c|>=1",
    status:"AUTHOR_EXACT_VERIFIED_UNREVIEWED_NOT_ADMITTED"
  };
})()