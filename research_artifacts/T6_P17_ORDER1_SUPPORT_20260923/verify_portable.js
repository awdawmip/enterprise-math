/* Standalone BigInt consumer: Node or browser, no Python/FLINT/SDK.
 * Mathematical values are decimal strings. Number is used only for indices
 * and counts below 2^17. This is an author cross-check, not independent review.
 */
"use strict";
(function (global) {
  function verifyR1(input, cert) {
    let brcCalls = 0;
    const check = (p, message) => { if (!p) throw new Error(message); };
    const big = x => { check(typeof x === "string" && /^-?(0|[1-9][0-9]*)$/.test(x), "decimal integer string required"); return BigInt(x); };
    const abs = x => x < 0n ? -x : x;
    // Language port of the existing BRC division facade: primitive division
    // occurs only here, and its quotient/remainder/collapse trace is checked.
    function brc(n, d) {
      check(d > 0n, "positive divisor"); brcCalls++;
      const a = abs(n), q0 = a / d, r0 = a - d * q0, collapsed = d * q0;
      check(a === collapsed + r0 && r0 >= 0n && r0 < d, "BRC reconstruction");
      const q = n >= 0n ? q0 : r0 === 0n ? -q0 : -q0 - 1n;
      const r = n >= 0n ? r0 : r0 === 0n ? 0n : d - r0;
      check(n === d * q + r && r >= 0n && r < d, "signed BRC transport");
      return {q, r, numerator:a, denominator:d, collapsed_numerator:collapsed, evaluation_kind:"BRC_DIVISION_EVALUATION"};
    }
    function gcd(a,b) { a=abs(a);b=abs(b); while(b){const r=brc(a,b).r;a=b;b=r;} return a; }
    function divExact(n,d) { const s=d<0n?-1n:1n;const t=brc(n*s,d*s);check(t.r===0n,"exact divisibility");return t.q; }
    class Q {
      constructor(n,d=1n) { check(d!==0n,"zero denominator");if(d<0n){n=-n;d=-d;}const g=gcd(n,d);this.n=divExact(n,g);this.d=divExact(d,g); }
      add(x){return new Q(this.n*x.d+x.n*this.d,this.d*x.d);}
      mul(x){return new Q(this.n*x.n,this.d*x.d);}
      eq(x){return this.n*x.d===x.n*this.d;}
      gt(x){return this.n*x.d>x.n*this.d;}
    }
    const q = pair => {check(Array.isArray(pair)&&pair.length===2,"rational pair");return new Q(big(pair[0]),big(pair[1]));};
    function inv(a,m){let r0=m,r1=brc(a,m).r,t0=0n,t1=1n;while(r1){const z=brc(r0,r1);[r0,r1,t0,t1]=[r1,z.r,t1,t0-z.q*t1];}check(r0===1n,"unit inverse");return brc(t0,m).r;}
    function det(matrix){const a=matrix.map(r=>r.slice());let previous=1n,sign=1n;for(let k=0;k<a.length-1;k++){if(a[k][k]===0n){let j=k+1;while(j<a.length&&a[j][k]===0n)j++;check(j<a.length,"singular basis");[a[k],a[j]]=[a[j],a[k]];sign=-sign;}const pivot=a[k][k];for(let i=k+1;i<a.length;i++){for(let j=k+1;j<a.length;j++)a[i][j]=divExact(a[i][j]*pivot-a[i][k]*a[k][j],previous);a[i][k]=0n;}previous=pivot;}return sign*a.at(-1).at(-1);}
    const dot=(x,y)=>x.reduce((s,a,i)=>s+a*y[i],0n);
    check(input.dimension===16&&input.degree===6&&input.prime==="17"&&input.residue==="1","fixed problem identity");
    check(input.positive_vertical_denominator==="306"&&input.positive_vertical_mass==="305","vertical atom");
    check(input.q0_positive_budget==="2026"&&input.q0_negative_budget==="2331","side budgets");
    const radius=2026n**2n+2331n**2n;check(big(input.radius_squared)===radius,"radius bound");
    const weights=input.weights.map(big),B=input.weighted_basis.map(r=>r.map(big));
    check(B.length===16&&B.every(r=>r.length===16),"basis shape");
    weights.forEach((w,i)=>check(w===17n*BigInt(i+1)-1n,"weight"));
    const U=B.map(row=>row.map((x,i)=>divExact(x,weights[i])));
    const declared=input.unweighted_basis.map(r=>r.map(big));
    check(U.every((row,i)=>row.every((v,j)=>v===declared[i][j])),"unweighted basis");
    check(abs(det(U))===17n**21n,"full kernel index");
    const x0=input.weighted_particular.map(big),u0=input.particular_q0.map(big);
    check(x0.length===16&&u0.length===16&&x0.every((x,i)=>x===u0[i]*weights[i]),"particular weights");
    for(let k=1;k<=6;k++){const m=17n**BigInt(k),a=Array.from({length:16},(_,j)=>inv(BigInt(j+1)**BigInt(k),m));check(U.every(row=>brc(dot(row,a),m).r===0n),"homogeneous congruence");check(brc(dot(u0,a)+inv(18n**BigInt(k),m),m).r===0n,"affine congruence");}
    const minor=Array.from({length:6},(_,k)=>Array.from({length:6},(_,j)=>inv(BigInt(j+1)**BigInt(k+1),17n)));
    check(brc(det(minor),17n).r!==0n,"mixed-modulus surjectivity");
    const D=input.gram_schmidt_squared.map(q),M=input.mu.map(row=>row.map(q)),C=input.centers.map(q);
    check(D.length===16&&M.length===16&&M.every(row=>row.length===16)&&C.length===16,"orthogonal shape");
    D.forEach(d=>check(d.gt(new Q(radius)),"two-candidate strict bound"));
    for(let i=0;i<16;i++)for(let j=0;j<16;j++)if(j>=i)check(M[i][j].eq(new Q(BigInt(i===j))),"unit lower triangular");
    for(let i=0;i<16;i++)for(let j=0;j<=i;j++){let total=new Q(0n);for(let k=0;k<16;k++)total=total.add(M[i][k].mul(D[k]).mul(M[j][k]));check(total.eq(new Q(dot(B[i],B[j]))),"exact Gram factorization");}
    for(let j=0;j<16;j++){let total=new Q(0n);for(let k=0;k<16;k++)total=total.add(C[k].mul(M[j][k]).mul(D[k]));check(total.eq(new Q(dot(x0,B[j]))),"exact affine coordinates");}
    check(cert.status==="R1_AFFINE_CLASS_EMPTY"&&cert.kernel===null,"complete empty certificate only");
    const seen=new Set(),chosen=Array(16).fill(0n);let branches=0,leaves=0;
    function walk(id,level,partial){
      check(Number.isInteger(id)&&id>=0&&id<cert.nodes.length&&!seen.has(id),"unique proof node");seen.add(id);
      const node=cert.nodes[id];check(node.id===id&&node.level===level,"node identity");
      let center=C[level];for(let j=level+1;j<16;j++)center=center.add(new Q(chosen[j]).mul(M[j][level]));
      check(q(node.center).eq(center)&&q(node.partial_before).eq(partial),"node state");
      const floor=brc(center.n,center.d),w=node.floor_witness;
      check(big(w.numerator)===center.n&&big(w.denominator)===center.d&&big(w.quotient)===floor.q&&big(w.remainder)===floor.r,"floor trace");
      check(node.options.length===2,"both branches mandatory");
      const candidates=[-floor.q-1n,-floor.q];
      node.options.forEach((option,index)=>{
        branches++;const n=big(option.coefficient);check(n===candidates[index],"complete adjacent candidates");chosen[level]=n;
        const error=center.add(new Q(n)),term=error.mul(error).mul(D[level]),total=partial.add(term);
        check(q(option.squared_component).eq(term)&&q(option.partial_after).eq(total),"exact norm increment");
        if(total.gt(new Q(radius))){check(option.decision==="PRUNE_EXACT_SQUARED_NORM"&&option.child===undefined,"sound norm rejection");}
        else if(level>0){check(option.decision==="DESCEND","missing feasible child");walk(option.child,level-1,total);}
        else {leaves++;const v=x0.map((x,t)=>x+chosen.reduce((s,n,i)=>s+n*B[i][t],0n));check(total.eq(new Q(dot(v,v))),"leaf norm");const pos=v.reduce((s,x)=>s+(x>0n?x:0n),0n),neg=v.reduce((s,x)=>s+(x<0n?-x:0n),0n);check(big(option.positive_q0_mass)===pos&&big(option.negative_q0_mass)===neg,"leaf side accounting");check(pos>2026n||neg>2331n,"hidden feasible modular kernel");check(option.decision==="PRUNE_EXACT_SIDE_BUDGET","side rejection marker");}
      });
    }
    walk(cert.root,15,new Q(0n));
    check(seen.size===cert.nodes.length&&seen.size===cert.node_count&&leaves===cert.full_leaves,"complete proof coverage");
    check(seen.size<=131071,"proved finite bound");
    return {status:"PORTABLE_BIGINT_CERTIFICATE_PASS",nodes:seen.size,branches,full_leaves:leaves,brc_evaluations:brcCalls,scope:"Fixed r1 class only; author cross-check, not independent Driver acceptance"};
  }
  global.verifyR1=verifyR1;
  if(typeof module!=="undefined"){
    module.exports={verifyR1};
    if(require.main===module){const fs=require("fs"),crypto=require("crypto");const text=fs.readFileSync(process.argv[2],"utf8"),cert=JSON.parse(fs.readFileSync(process.argv[3],"utf8"));if(crypto.createHash("sha256").update(text).digest("hex")!==cert.portable_input_sha256)throw new Error("input digest mismatch");console.log(JSON.stringify(verifyR1(JSON.parse(text),cert)));}
  }
})(typeof globalThis!=="undefined"?globalThis:this);
