// Verbatim functions from multiplicative_browser.py::SCRIPT at f7f2ecbf.
// Test-only module wrapper; only exact readout functions execute here.
const MulExactReadouts = (() => {
  function safeInt(s) {
    const n=BigInt(s);if(n< -9007199254740991n||n>9007199254740991n)throw Error('格点超出网页安全整数载体');
    return Number(n); // Checked integer transport; never a numerical decision.
  }
  const exact=f=>f?.cell_engine==='CERTIFIED_INTEGER_RESIDUAL';
  function stats(f) {
    if(!exact(f))return MulMath.stats(f);
    const total=f.records.length,p=total-1,grid=Array.from({length:8},()=>Array(32).fill(0)),fibers=new Map();
    for(const r of f.records){
      if(r.coord!==null){const k=r.coord.join(',');if(!fibers.has(k))fibers.set(k,[]);fibers.get(k).push(r.n);}
      if(r.n){const band=Number(NollmAngularExact.evaluateDivision(BigInt(r.n-1)*8n,BigInt(p)).quotient);grid[band][NollmAngularExact.phaseBin(r.phase,MulMath.M,32)]++;}
    }
    const pop=f.cell_membership_exact,n=x=>x===null?null:safeInt(x);
    return {population:total,positive_population:p,prime_count:Object.keys(f.prime_phase).length,
      rings:8,sectors:32,grid,distinct_phases:new Set(f.records.slice(1).map(r=>r.phase)).size,
      angular_cv:null,area_sector_cv:null,iid_cv_scale:null,
      angular_cv_squared_exact:NollmAngularExact.fromCounts(Array.from({length:32},(_,j)=>grid.reduce((s,r)=>s+r[j],0)),'1000000'),
      area_sector_cv_squared_exact:NollmAngularExact.fromCounts(grid.flat(),'1000000'),
      approximate_metrics_role:'OMITTED_FROM_EXACT_OBSERVER',
      occupied_hex_centers:n(pop.occupied_cells),occupied_hex_centers_bounds:pop.occupied_cells_bounds.map(safeInt),
      collision_groups:n(pop.collision_groups),extra_identities_at_shared_centers:n(pop.excess_identities_if_collapsed),largest_fiber:n(pop.max_cell_load),
      unresolved_cell_identities:pop.unresolved_identities.slice(),max_display_quantization_error:null,fibers};
  }
  function multiply(f,a,b) {
    if(!exact(f))return MulMath.multiply(f,a,b);
    if(![a,b].every(x=>Number.isSafeInteger(x)&&x>=0&&x<f.records.length))throw Error('因子须为范围内整数');
    const n=a*b;if(n>=f.records.length)return {a,b,product:n,in_range:false};
    const [A,B,Z]=[f.records[a],f.records[b],f.records[n]];
    return {a,b,product:n,in_range:true,phase_defect:n?((Z.phase-A.phase-B.phase)%MulMath.M+MulMath.M)%MulMath.M:null,
      omega_defect:n?Z.omega-A.omega-B.omega:null,ideal_relative_error:null,rounded_relative_error:null,
      approximate_metrics_role:'OMITTED_FROM_EXACT_OBSERVER',zero_phase:n?null:'undefined; multiplication by zero is handled separately'};
  }
  return {stats,multiply};
})();
