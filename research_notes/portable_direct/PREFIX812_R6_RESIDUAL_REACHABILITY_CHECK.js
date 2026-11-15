// PREFIX-812: exact bounded-fiber residual reachability checker.
// Requires Node.js >= 18; no dependencies, deterministic exhaustive enumeration.
// Run: node PREFIX812_R6_RESIDUAL_REACHABILITY_CHECK.js
"use strict";
const verify = function run() {
  const suites = [
    {name:"K2x2_0_1_2",rows:2,cols:2,edges:[[0,0],[0,1],[1,0],[1,1]],maximum:2},
    {name:"K2x3_0_1",rows:2,cols:3,edges:[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]],maximum:1},
    {name:"K3x3_0_1",rows:3,cols:3,edges:Array.from({length:9},(_,i)=>[Math.floor(i/3),i%3]),maximum:1},
    {name:"K2x2_parallel_0_1",rows:2,cols:2,edges:[[0,0],[0,0],[0,1],[1,0],[1,1]],maximum:1}
  ];
  function residual(rows,cols,edges,K,x) {
    const n=rows+cols,arcs=Array.from({length:n},()=>[]);
    for(let e=0;e<edges.length;e++){
      const [u,v0]=edges[e],v=rows+v0;
      if(x[e]<K[e])arcs[u].push(v);
      if(x[e]>0)arcs[v].push(u);
    }
    const reach=Array.from({length:n},()=>Array(n).fill(0));
    for(let a=0;a<n;a++){
      const seen=reach[a],stack=[a];seen[a]=1;
      while(stack.length){const u=stack.pop();for(const v of arcs[u])if(!seen[v]){seen[v]=1;stack.push(v)}}
    }
    return reach;
  }
  function scc(reach){
    const n=reach.length,ids=Array(n).fill(-1);let next=0;
    for(let u=0;u<n;u++)if(ids[u]<0){for(let v=0;v<n;v++)if(reach[u][v]&&reach[v][u])ids[v]=next;next++}
    return ids;
  }
  const report={schema:"PREFIX812_EXACT_CHECK_V1",arithmetic:"integer-only",suites:[],totals:{capacity_patterns:0,margin_fibers:0,source_tables:0,nonfirst_table_comparisons:0,reachability_bit_equalities:0,cross_scc_frozen_edge_checks:0,multi_table_fibers:0},witness:{}};
  for(const suite of suites){
    const {rows,cols,edges,maximum}=suite,m=edges.length,K=Array(m).fill(0),x=Array(m).fill(0);
    const count={name:suite.name,capacity_patterns:0,margin_fibers:0,source_tables:0,nonfirst_table_comparisons:0,reachability_bit_equalities:0,cross_scc_frozen_edge_checks:0,multi_table_fibers:0};
    function tableSearch(idx,rr,cc,map){
      if(idx<m){
        const [u,v]=edges[idx];
        for(let t=0;t<=K[idx];t++){x[idx]=t;rr[u]+=t;cc[v]+=t;tableSearch(idx+1,rr,cc,map);rr[u]-=t;cc[v]-=t}
        return;
      }
      count.source_tables++;
      const key=rr.join(",")+"|"+cc.join(","),R=residual(rows,cols,edges,K,x),previous=map.get(key);
      if(!previous){map.set(key,{reach:R,classes:scc(R),base:x.slice(),size:1})}
      else{
        previous.size++;count.nonfirst_table_comparisons++;
        const n=rows+cols;
        for(let i=0;i<n;i++)for(let j=0;j<n;j++){
          count.reachability_bit_equalities++;
          if(R[i][j]!==previous.reach[i][j])throw Error("reachability mismatch "+suite.name+" "+key+" "+i+","+j+" "+JSON.stringify(K));
        }
        for(let i=0;i<m;i++){
          const [u,v0]=edges[i],v=rows+v0;
          if(previous.classes[u]!==previous.classes[v]){
            count.cross_scc_frozen_edge_checks++;
            if(x[i]!==previous.base[i])throw Error("cross SCC edge changed "+suite.name+" "+key+" "+i);
          }
        }
      }
    }
    function capacitySearch(idx){
      if(idx<m){for(let t=0;t<=maximum;t++){K[idx]=t;capacitySearch(idx+1)}return}
      count.capacity_patterns++;
      const map=new Map();
      tableSearch(0,Array(rows).fill(0),Array(cols).fill(0),map);
      count.margin_fibers+=map.size;
      for(const b of map.values())if(b.size>1)count.multi_table_fibers++;
    }
    capacitySearch(0);report.suites.push(count);
    for(const key of Object.keys(report.totals))report.totals[key]+=count[key];
  }
  const fullEdges=[[0,0],[0,1],[1,0],[1,1]],fullK=[1,1,1,1],x=[1,0,0,1],y=[0,1,1,0];
  const R1=residual(2,2,fullEdges,fullK,x),R2=residual(2,2,fullEdges,fullK,y);
  if(JSON.stringify(R1)!==JSON.stringify(R2))throw Error("2x2 cycle flip reachability");
  const before=scc(R1),after=scc(residual(2,2,fullEdges.slice(1),fullK.slice(1),x.slice(1)));
  if(new Set(before).size!==1||new Set(after).size!==4)throw Error("pin witness invalid");
  report.witness={initial_fiber_tables:[x,y],reachability_invariant_on_unit_4_cycle:true,original_scc_count:new Set(before).size,pin_edge_00_to_1_after_removal_scc_count:new Set(after).size,observer_diagonal_before:2,observer_diagonal_after:0};
  report.status="ALL_EXACT_ASSERTIONS_PASSED";
  return report;
};
if (typeof module !== "undefined" && require.main === module) console.log(JSON.stringify(verify(),null,2));
module.exports = { verify };
