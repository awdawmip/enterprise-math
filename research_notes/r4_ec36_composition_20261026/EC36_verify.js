/* EC36: exact source-mass verifier for EC33 auxiliary positive BRC.
   Run with: node EC36_verify.js
   No native X6 program and no floating-point dynamics.
*/
function verify() {
  const checks={word_formula:0,total_mass:0,tv_formula:0,one_step_projection:0,no_go:0};
  function assert(ok,msg){if(!ok)throw new Error(msg);}
  function words(n){let a=[''];for(let i=0;i<n;i++)a=a.flatMap(w=>[w+'R',w+'B']);return a;}
  function phase(a,n,Q){
    const mask=[];for(let i=0;i<n;i++){
      mask.push(a>0);a=Math.max(0,a-1);if(Q)a=Q[a];
    }return mask;
  }
  function count(a,n,Q){
    let m=new Map([['',[a,1]]]);
    for(let i=0;i<n;i++){
      const next=new Map();
      for(const [w,[c,v]] of m.entries()){
        for(const label of ['R','B']){
          if(c===0 && label==='B')continue;
          const mult=c===0?2:1;
          let nc=Math.max(c-1,0);if(Q)nc=Q[nc];
          next.set(w+label,[nc,v*mult]);
        }
      }m=next;
    }
    return new Map([...m].map(([w,[_c,v]])=>[w,v]));
  }
  function expected(mask,w) {
    for(let i=0;i<mask.length;i++)if(!mask[i]&&w[i]==='B')return 0;
    return 2**mask.filter(x=>!x).length;
  }
  function maps(H){let a=[[]];for(let i=0;i<=H;i++)a=a.flatMap(p=>Array.from({length:H+1},(_,j)=>[...p,j]));return a;}
  const exhaustedMaps={};
  for(let H=1;H<=3;H++){
    const qq=maps(H);exhaustedMaps[H]=qq.length;
    for(const Q of qq)for(let a=0;a<=H;a++)for(let n=0;n<=7;n++){
      const truth=count(a,n,null),approx=count(a,n,Q),it=phase(a,n,null),jt=phase(a,n,Q);
      let s1=0,s2=0,l1=0;
      for(const w of words(n)){
        const x=truth.get(w)||0,y=approx.get(w)||0;
        assert(x===expected(it,w)&&y===expected(jt,w),'microbranch word formula');
        checks.word_formula+=2;s1+=x;s2+=y;l1+=Math.abs(x-y);
      }
      assert(s1===2**n&&s2===2**n,'mass');
      checks.total_mass++;
      let p=0,q=0;
      for(let t=0;t<n;t++){if(it[t]&&!jt[t])p++;if(!it[t]&&jt[t])q++;}
      const d=Math.max(p,q);
      assert(l1*2**d===2*(2**n)*(2**d-1),'TV exact identity');
      checks.tv_formula++;
    }
  }
  const Q=[0,2,2]; // H=2, remaining capacity.
  for(let a=0;a<=2;a++){
    assert((a>0)===(Q[a]>0),'one-step quotient');
    checks.one_step_projection++;
  }
  const witness=[];
  for(let n=0;n<=12;n++){
    const I=phase(2,n),J=phase(2,n,Q);
    let p=0,q=0;for(let t=0;t<n;t++){if(I[t]&&!J[t])p++;if(!I[t]&&J[t])q++;}
    const d=Math.max(p,q),want=Math.max(0,n-2);
    assert(d===want,'witness exponent');
    witness.push({n,TV_numerator:2**d-1,TV_denominator:2**d});checks.no_go++;
  }
  return {schema:'EM_R4_EC36_COMPOSITION_GITHUB_VERIFY_V1',status:'PASS',
    source:'EC33 transitions_v as remaining-capacity ordered positive-source model',
    domain:{all_H:[1,2,3],all_Q_counts:exhaustedMaps,all_starting_capacities:'0..H',lengths:'0..7'},
    checks,witness,proof_source:'EC36_COMPOSITION.md',native_X6_verified:false,
    original_owner_verified:false,independent_review:false};
}
if(typeof process!=='undefined' && process.versions && process.versions.node){
  console.log(JSON.stringify(verify(),null,2));
}