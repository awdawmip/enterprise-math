/** R729 reproducible exact BRC named-S3 holonomy certificate.
 * Run: node R729_NAMED_S3_FIBER_VERIFY.js > R729_NAMED_S3_FIBER_RESULTS.json
 * No external dependencies; uses BigInt throughout.
 * R728 frozen source and R725 sharp 15-arc representatives.
 */
const computeR729 = function computeR729(){
  const T=["012","013","014","023","024","034","123","124","134","234"];
  const arcsAll=[];
  for(const u of T) for(const v of T) if([...u].filter(x=>v.includes(x)).length===2) arcsAll.push([u,v]);
  if(arcsAll.length!==60)throw Error("arc inventory");
  const masks={A:"211733226574",B:"5363347296468"};
  const Ds={
    A:{D0:[1,0,0,-3,-7,-8,-4],Ds:[1,0,0,1,1,-2],D2:[1,0,0,-2,0,2,2,-1,-3,-1,3,2]},
    B:{D0:[1,0,0,-3,-7,-8,-5,-1],Ds:[1,0,0,1,1,-2,-1,1],D2:[1,0,0,-2,0,2,3,-1,-3,-2,2,4,2,-1,-1]}
  };
  const ps=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
  const names=ps.map(p=>p.map(j=>"012"[j]).join(""));
  const pindex=new Map(ps.map((p,i)=>[p.join(""),i]));
  const check=(ok,s)=>{if(!ok)throw Error(s)};
  const step=(fr,tar)=>{const leave=[...fr].find(c=>!tar.includes(c));const ent=[...tar].find(c=>!fr.includes(c));return fr.replace(leave,ent)};
  const ep=(e)=>[...step(e[0],e[1])].map(c=>e[1].indexOf(c));
  const mul=(a,b)=>{const o=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)o[i+j]+=a[i]*b[j];return o};
  const eq=(a,b)=>{const n=Math.max(a.length,b.length);return Array.from({length:n},(_,i)=>(a[i]||0n)===(b[i]||0n)).every(Boolean)};
  const diff=(a,b)=>Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)-(b[i]||0n));
  const det=(M)=>{let a=M.map(row=>row.slice()),sign=1n,old=1n,n=a.length;for(let k=0;k<n-1;k++){if(a[k][k]===0n){const z=a.findIndex((r,i)=>i>k&&r[k]!==0n);if(z<0)return 0n;[a[k],a[z]]=[a[z],a[k]];sign=-sign}const pivot=a[k][k];for(let i=k+1;i<n;i++){for(let j=k+1;j<n;j++){const v=a[i][j]*pivot-a[i][k]*a[k][j];check(v%old===0n,"nonintegral Bareiss");a[i][j]=v/old}a[i][k]=0n}old=pivot}return sign*a[n-1][n-1]};
  const res={schema:"R729_NAMED_BRC_HOLONOMY_INTEGER_CERTIFICATE_V1",status:"PASS",arithmetic:"BigInt exact integers; full 90x90 polynomial operator certificate and independent string-frame brute force",science_pin:"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",predecessor:"R728@69579fbe3fa934b25554bafb80e16545013c9964",classes:{}};
  for(const label of ["A","B"]){
    const mask=BigInt(masks[label]);const E=arcsAll.filter((e,i)=>((mask>>BigInt(i))&1n)!==0n);check(E.length===15,"mask size");
    const eid=new Map(E.map((e,i)=>[e.join(">"),i]));
    const roots=E.filter(e=>e[0]==="012");
    const J=Array.from({length:90},()=>[]);
    for(let i=0;i<15;i++) for(let j=0;j<15;j++){
      if(E[i][1]!==E[j][0]||E[i][0]===E[j][1])continue;
      const p=ep(E[j]);
      for(let k=0;k<6;k++){
        const q=ps[k],upd=p.map((v,z)=>0);for(let z=0;z<3;z++)upd[z]=p[q[z]];
        const kk=pindex.get(upd.join(""));check(kk!==undefined,"frame permutation");
        J[6*i+k].push(6*j+kk);
      }
    }
    const vmove=(v)=>{const w=Array(90).fill(0n);for(let i=0;i<90;i++)if(v[i])for(const j of J[i])w[j]+=v[i];return w};
    const d=Object.fromEntries(Object.entries(Ds[label]).map(([key,arr])=>[key,arr.map(BigInt)]));
    const Q=mul(mul(d.D0,d.Ds),mul(d.D2,d.D2));
    const degree=Q.length-1;const tail=label==="A"?5:3;check(degree===(label==="A"?33:42),"degree");
    let before=0;
    for(let basis=0;basis<90;basis++){
      let w=Array(90).fill(0n);w[basis]=1n;
      const powers=[w];for(let k=0;k<degree;k++)powers.push(vmove(powers.at(-1)));
      w=Array(90).fill(0n);
      for(let j=0;j<=degree;j++)for(let i=0;i<90;i++)w[i]+=Q[j]*powers[degree-j][i];
      for(let j=0;j<tail;j++){if(j===tail-1)before+=w.filter(v=>v!==0n).length;w=vmove(w)}
      check(w.every(x=>x===0n),"matrix polynomial not annihilated "+basis)
    }
    check(before===(label==="A"?144:120),"minimal tail witness");
    const maxM=82;const H=Object.fromEntries(names.map(h=>[h,Array(maxM+1).fill(0n)]));
    for(const first of roots){
      let v=Array(90).fill(0n);
      const firstIndex=eid.get(first.join(">"));
      v[6*firstIndex+pindex.get(ep(first).join(""))]=1n;
      for(let m=1;m<=maxM;m++){
        for(let e=0;e<15;e++){
          if(E[e][1]==="012"&&E[e][0]!==first[1])for(let k=0;k<6;k++)H[names[k]][m]+=v[6*e+k]
        }
        v=vmove(v);
      }
    }
    const Brute=Object.fromEntries(Array.from({length:5},(_,j)=>[j+3,Object.fromEntries(names.map(h=>[h,0n]))]));
    const nbr=Object.fromEntries(T.map(t=>[t,E.filter(e=>e[0]===t).map(e=>e[1])]));
    function walk(prev,cur,frame,first,m){
      if(m>=3&&cur==="012"&&prev!==first)Brute[m][frame]++;
      if(m===7)return;
      for(const tar of nbr[cur])if(tar!==prev)walk(cur,tar,step(frame,tar),first,m+1);
    }
    for(const f of nbr["012"])walk("012",f,step("012",f),f,1);
    for(let m=3;m<=7;m++)for(const h of names)check(Brute[m][h]===H[h][m],"brute mismatch "+label+" "+m+" "+h);
    const Numer={};
    for(const h of names){
      const N=Array(maxM+1).fill(0n);
      for(let m=1;m<=maxM;m++)for(let j=0;j<=Math.min(degree,m);j++)N[m]+=Q[j]*H[h][m-j];
      for(let m=degree+1;m<=maxM;m++)check(N[m]===0n,"bad numerator tail "+h+" "+m);
      Numer[h]=N.slice(0,degree+1);
    }
    const shift=(a,n)=>Array(n).fill(0n).concat(a);
    const target=mul(mul(d.D0,d.Ds),d.D2);
    if(label==="A"){
      check(eq(Numer["120"],Numer["201"]),"A cycles unequal");
      check(eq(diff(Numer["102"],Numer["210"]),shift(target,3)),"A transposition identity");
    }else{
      check(eq(diff(Numer["201"],Numer["120"]),mul([0n,0n,0n,0n,0n,2n,1n],target)),"B cycle identity");
    }
    const rows=label==="A"?["012","021","102","120","210"]:names;
    const lengths=label==="A"?[3,4,5,6,7]:[3,4,5,6,7,8];
    const minor=det(rows.map(h=>lengths.map(m=>H[h][m])));
    check(minor===(label==="A"?-2n:-7n),"rank minor");
    const asNums=a=>a.map(x=>x.toString());
    res.classes[label]={
      arc_mask:masks[label],selected_directed_arcs:E.map(e=>e.join(">")),
      root_departure_options:roots.length,frame_names:names,operator_states:90,
      denominator_factors:Object.fromEntries(Object.entries(d).map(([key,a])=>[key,asNums(a)])),
      common_denominator:asNums(Q),
      rational_numerators:Object.fromEntries(names.map(h=>[h,asNums(Numer[h])])),
      operator_certificate:{verified_entries:8100,polynomial_annihilation_shift:tail,immediately_previous_shift_nonzero_entries:before},
      all_length_linear_named_count_rank:rows.length,rank_minor:{row_names:rows,column_lengths:lengths,determinant:minor.toString()},
      named_counts_3_to_16:Object.fromEntries(Array.from({length:14},(_,j)=>j+3).map(m=>[String(m),Object.fromEntries(names.map(h=>[h,H[h][m].toString()]))])),
      independent_brute_force_lengths:"3..7",
      computed_exact_dp_lengths:"1..82",
      model:"positive source-distinct rooted cyclic nonbacktracking, derived V17 slot transfer in 5 accessible axes of native X6"
    }
  }
  return res;
};
const output=computeR729();
process.stdout.write(JSON.stringify(output,null,2)+"\n");
