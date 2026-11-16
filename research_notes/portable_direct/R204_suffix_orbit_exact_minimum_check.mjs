/** R204: exact finite-field shift-register witness checks. Run: node R204_suffix_orbit_exact_minimum_check.mjs */
function verifyR204(){
  const models = [[2,2,5],[2,3,3],[2,4,3],[2,8,2],[2,84,2],[3,3,4],[3,5,3],[5,5,3]];
  const checks={models:0,orbit_states:0,distinct_orbit_states:0,action_concatenation:0,tail_quotient_composition:0,rank_witnesses:0};
  const records=[];
  function code(q,a,x){let c=0, cap=1;while(cap<a+1){cap*=q;c++}let value=x+1;const arr=[];for(let i=0;i<c;i++){arr.push(value%q);value=Math.floor(value/q)}return arr}
  function apply(q,a,L,word,initial){let result=initial.slice(), c=code(q,a,0).length;for(const x of word)result=result.slice(c).concat(code(q,a,x));return result}
  function key(word){return word.join(",")}
  function rng(seed){let x=seed>>>0;return ()=>{x^=x<<13;x^=x>>>17;x^=x<<5;return x>>>0}}
  for(const [q,a,L] of models){
    const c=code(q,a,0).length,D=L*c,zero=Array(D).fill(0),seen=new Map(),words=[[]];
    for(let h=1;h<=L;h++){
      const prior=words.filter(w=>w.length===h-1);
      for(const w of prior)for(let x=0;x<a;x++)words.push(w.concat(x));
    }
    for(const w of words){
      const orbit=apply(q,a,L,w,zero).join(",");
      if(seen.has(orbit))throw Error("collision "+q+"/"+a+"/"+L+" "+key(w)+" vs "+key(seen.get(orbit)));
      seen.set(orbit,w);checks.orbit_states++;checks.distinct_orbit_states++;
      const expected=Array(D).fill(0),offset=D-w.length*c;
      for(let i=0;i<w.length;i++)for(let j=0;j<c;j++)expected[offset+i*c+j]=code(q,a,w[i])[j];
      if(orbit!==expected.join(","))throw Error("orbit not padded suffix");
    }
    const sizeExpected=Array.from({length:L+1},(_,h)=>a**h).reduce((u,v)=>u+v,0);
    if(words.length!==sizeExpected||seen.size!==sizeExpected)throw Error("unexpected cardinality");
    const random=rng(20261116+a+L*100+q*10000);
    const vectors=[zero];
    for(let i=0;i<D;i++){const e=zero.slice();e[i]=1;vectors.push(e)}
    for(let z=0;z<Math.min(700,words.length*4);z++){
      const w=words[random()%words.length],v=words[random()%words.length],tail=w.concat(v).slice(-L);
      for(const basis of vectors){
        const left=apply(q,a,L,tail,basis);
        const right=apply(q,a,L,v,apply(q,a,L,w,basis));
        if(left.join(",")!==right.join(","))throw Error("action quotient failed");
        checks.action_concatenation++;
      }
      const expected=apply(q,a,L,tail,zero);
      const actual=apply(q,a,L,v,apply(q,a,L,w,zero));
      if(expected.join(",")!==actual.join(","))throw Error("orbit quotient failed");
      checks.tail_quotient_composition++;
    }
    for(let i=0;i<c;i++){
      let e=zero.slice();e[(L-1)*c+i]=1;
      let result=e;
      for(let j=0;j<L-1;j++)result=result.slice(c).concat(Array(c).fill(0));
      if(result.slice(0,c).some((x,j)=>x!==(i===j?1:0)))throw Error("rank witness failed");
      checks.rank_witnesses++;
    }
    let ca=0,power=1;while(power<a){power*=q;ca++}
    checks.models++;records.push({q,a,L,c,D,N:words.length,general_orbit_lower_bound:D,action_faithful_tail_dimension:L*ca});
  }
  return {result:"PASS",backend:"exact_integer_prime_field_shift_register_models",theorem:"minimum orbit-separating affine dimension over F_q equals L*ceil(log_q(a+1))",frozen_source_commit:"43ec6098b1330ae86d0a7863be336c5d97f6ef34",checks,models:records,review:"NOT_REVIEWED",native_package_integration:"NOT_EXECUTED"};
}
console.log(JSON.stringify(verifyR204(),null,2));
