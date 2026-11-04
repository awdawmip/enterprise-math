"use strict";
// EC49FAF: pure integer audit of five-fiber pairwise prefix-capacity graphs.
// Input tables are immutable Git blobs of the frozen Enterprise Math model.
function audit(tsvText, capText) {
  function insist(test, message) { if (!test) throw Error(message); }
  const lines = tsvText.trim().split(/\r?\n/);
  insist(lines[0].startsWith("# exy_lb exs_lb pair1a"), "unexpected TSV header");
  const schedules = lines.slice(1).map((s, i) => {
    const a = s.trim().split(/\s+/).map(Number);
    insist(a.length === 21 && a.every(Number.isInteger), "invalid schedule " + i);
    return a;
  });
  insist(schedules.length === 12356, "candidate census mismatch");
  const capLines = capText.trim().split(/\r?\n/).filter(s => !s.startsWith("#"));
  insist(Number(capLines[0]) === 164, "family census mismatch");
  const families = capLines.slice(1).map((s, i) => {
    const a = s.trim().split(/\s+/).map(Number);
    insist(a.length === 169 && a.every(Number.isInteger), "invalid cap row " + i);
    return a;
  });
  insist(families.length === 164, "capacity rows mismatch");
  const familyId = new Map(families.map((a, i) => [a.slice(0,4).join(","), i]));
  insist(familyId.size === 164, "family key not unique");
  const cap = families.map(a => a.slice(5));
  for(let i=0;i<164;i++) for(let j=0;j<i;j++)
    insist(cap[i][j] === cap[j][i], "asymmetric cross-fiber capacity");
  const pair = (a,b) => [Math.min(a,b),Math.max(a,b)].join(",");
  const allPairs=[];
  for(let i=0;i<5;i++) for(let j=i+1;j<5;j++) allPairs.push([i,j]);
  function permutations(a) {
    if(a.length === 0) return [[]];
    const result=[];
    for(let i=0;i<a.length;i++)
      for(const p of permutations(a.filter((_,j)=>i!==j))) result.push([a[i],...p]);
    return result;
  }
  const cycles=[];
  for(const p of permutations([1,2,3,4])) {
    if(p[0] > p[3]) continue; // reversal of same Hamiltonian cycle
    const q=[0,...p], e=new Set();
    for(let i=0;i<5;i++) e.add(pair(q[i],q[(i+1)%5]));
    cycles.push(e);
  }
  insist(cycles.length === 12, "cycle enumeration mismatch");
  const twoK2=[];
  for(let omit=0;omit<5;omit++) {
    const v=[0,1,2,3,4].filter(x=>x!==omit);
    twoK2.push([[v[0],v[1]],[v[2],v[3]]],
                [[v[0],v[2]],[v[1],v[3]]],
                [[v[0],v[3]],[v[1],v[2]]]);
  }
  insist(twoK2.length === 15, "matching enumeration mismatch");
  let c5Thresholds=0,k2Thresholds=0,c5Depths=0,k2Depths=0,
      c4Depths=0,p4Depths=0,depths=0,maxC5Gap=-999,maxK2Gap=-999;
  const distinct=new Set(), gapHistogram={};
  for(let rank=0;rank<schedules.length;rank++) {
    const a=schedules[rank], doublePair=[[a[2],a[3]],[a[4],a[5]]];
    const used=new Set(doublePair.flat());
    insist(used.size===4, "invalid double-pair skeleton " + rank);
    const rem=[2,3,4,5,6,7,8].filter(x=>!used.has(x));
    const hs=[...doublePair,...rem.map(h=>[h])];
    const keys=Array.from({length:5},(_,i)=>a.slice(6+3*i,9+3*i));
    const ids=hs.map((g,i)=>g.map(h=>familyId.get([h,...keys[i]].join(","))));
    insist(ids.every(g=>g.every(x=>x!==undefined)), "missing family " + rank);
    const cc=Array.from({length:5},()=>Array(5).fill(0));
    for(const [i,j] of allPairs) {
      for(const x of ids[i]) for(const y of ids[j])
        cc[i][j]=Math.max(cc[i][j], cap[x][y]);
      cc[j][i]=cc[i][j];
    }
    const lens=keys.map(k=>2*(k[0]+k[1]+k[2]-1));
    let bestC5Gap=-999;
    // Independent threshold-interval test: G_d is C5 iff
    // max(C_ij on its five edges) < d <= min(C_ij on its five nonedges).
    for(const cycle of cycles) {
      let emax=-999,nmin=999;
      for(const [i,j] of allPairs) {
        if(cycle.has(pair(i,j))) emax=Math.max(emax,cc[i][j]);
        else nmin=Math.min(nmin,cc[i][j]);
      }
      const gap=nmin-emax;
      bestC5Gap=Math.max(bestC5Gap,gap);
      maxC5Gap=Math.max(maxC5Gap,gap);
      if(gap>0) c5Thresholds++;
    }
    gapHistogram[bestC5Gap]=(gapHistogram[bestC5Gap]||0)+1;
    for(const match of twoK2) {
      const edgeNames=new Set(match.map(z=>pair(z[0],z[1])));
      const vertices=match.flat();
      let emax=-999,nmin=999;
      for(let i=0;i<4;i++) for(let j=i+1;j<4;j++) {
        const x=vertices[i],y=vertices[j];
        if(edgeNames.has(pair(x,y))) emax=Math.max(emax,cc[x][y]);
        else nmin=Math.min(nmin,cc[x][y]);
      }
      maxK2Gap=Math.max(maxK2Gap,nmin-emax);
      if(emax<nmin) k2Thresholds++;
    }
    for(let d=1;d<=Math.max(...lens);d++) {
      const active=lens.map(L=>L>=d), adj=Array(5).fill(0);
      for(const [i,j] of allPairs) if(active[i]&&active[j]&&cc[i][j]<d) {
        adj[i]|=1<<j; adj[j]|=1<<i;
      }
      depths++;
      const activeMask=active.reduce((m,x,i)=>m|(x?1<<i:0),0);
      distinct.add(activeMask+":"+adj.join(","));
      if(active.every(Boolean)) {
        const degree=adj.map(x=>{
          let t=0;for(let j=0;j<5;j++) if(x&(1<<j))t++;return t;
        });
        if(degree.every(x=>x===2)) c5Depths++;
      }
      let has2K2=false,hasC4=false,hasP4=false;
      for(let omit=0;omit<5;omit++) {
        const v=[0,1,2,3,4].filter(i=>i!==omit&&active[i]);
        if(v.length!==4) continue;
        const degree=v.map(i=>v.reduce((s,j)=>s+Number(Boolean(adj[i]&(1<<j))),0));
        const edges=degree.reduce((s,x)=>s+x,0)/2;
        if(edges===2 && degree.every(x=>x===1)) has2K2=true;
        if(edges===4 && degree.every(x=>x===2)) hasC4=true;
        if(edges===3 && degree.slice().sort((x,y)=>x-y).join(",")==="1,1,2,2")
          hasP4=true;
      }
      if(has2K2) k2Depths++;
      if(hasC4) c4Depths++;
      if(hasP4) p4Depths++;
    }
  }
  const result={
    schema:"EC49FAF_PAIRWISE_RELAXATION_AUDIT_V1",status:"PASS",
    source_candidate_blob:"61ffbcdba1679479fade3cfd052c2d9d6bbf30ce",
    source_cap_family_count:164,source_candidate_count:schedules.length,
    horizon_domain:"h=2..8; five BRC cache fibers; frozen 12,356 double-collision schedule rows",
    thresholds_tested_per_schedule: "All integer depths d>=1, including every active depth",
    cycle_edge_patterns:cycles.length,disjoint_pair_patterns:twoK2.length,
    c5_threshold_instances:c5Thresholds,disjoint2k2_threshold_instances:k2Thresholds,
    c5_active_depth_instances:c5Depths,disjoint2k2_active_depth_instances:k2Depths,
    induced_c4_active_depth_instances:c4Depths,induced_p4_active_depth_instances:p4Depths,
    active_depth_graph_instances:depths,distinct_labeled_active_graphs:distinct.size,
    maximum_hamiltonian_threshold_gap:maxC5Gap,
    maximum_disjoint_pair_threshold_gap:maxK2Gap,
    max_cycle_gap_by_schedule_histogram:gapHistogram,
    theorem:"Every declared depth-wise five-fiber pairwise incompatibility graph is co-chordal (and perfect); hence B_EXY already attains the exact weighted-coloring lower bound based solely on the five per-fiber depth demands and pairwise shared-prefix capacities."
  };
  if(c5Thresholds!==0||k2Thresholds!==0||c5Depths!==0||k2Depths!==0 ||
     c4Depths!==1220||p4Depths!==792||depths!==236896||distinct.size!==127 ||
     maxC5Gap!==0||maxK2Gap!==0) throw Error("audit counts changed: "+JSON.stringify(result));
  return result;
}

// Usage: node VERIFY_EC49FAF.js EC49EXY_DOUBLE_CANDIDATES.tsv EC49EXY_CAPS_TABLE.txt
if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) {
  const fs=require("fs");
  if(process.argv.length!==4) throw Error("expected exactly two table filenames");
  process.stdout.write(JSON.stringify(audit(fs.readFileSync(process.argv[2],"utf8"),
     fs.readFileSync(process.argv[3],"utf8")),null,2)+"\n");
}
if (typeof module !== "undefined") module.exports={audit};
