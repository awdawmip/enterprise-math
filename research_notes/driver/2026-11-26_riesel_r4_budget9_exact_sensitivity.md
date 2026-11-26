# Riesel R4 budget nine: minimal local phase quotient and exact coordinate sensitivity

2026-11-26. Informed Driver derivation on the complete classification by EM-DIRECT-970E1C (RA-D2EC212845B63844081F9A14). Not a new independent classification, native Review or Result. The prior author already computed the exact full budget-nine density; the new scope is the local quotient, coordinate influence and one-coordinate robustness/repair distributions, with exact recalculation of that density as a crosscheck.

Sources:
- awdawmip/enterprise-math@9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/r4/proof.md, §§2,4,6, especially complete G/RR/RRR/HHH classification, RRR subset RR, and exact root density.
- awdawmip/enterprise-math@cc61353041652eadc2e57e7c44d0ba65eec62684:research_notes/driver/2026-11-26_riesel_all_budget_pivotal_density_cylinders.md, finite phase masses and resampling influence lower bound.

## Theorem 1: exact local quotient

Retain the author's R4 progression, twenty-prime P, proper-prime covering cost delta_P and thirteen free essential primes. The accepted predicate f=1(delta_P<=9) is exactly the disjunction of three events on disjoint groups G,R,H: each of k=5,2,3 designated phase colors appears at least once among the group's 5,3,5 coordinates respectively. RRR is redundant for this root predicate. Each designated color is a pair of distinct residues at each prime p, by the author's phase formula; every other root residue is a single additional symbol *, including zero and any irrelevant active phases. CRT gives independent symbols with weights 2/p per color and (p-2k)/p for *. This is a Boolean observer of the cost threshold, not a quotient of the full integer or all exponent trajectories.

This quotient is minimal among separate deterministic coordinate encodings: for any prime p and a specific color c, prescribe every other required color to a distinct other prime in that group, set all remaining primes there to *, and make the other two groups inactive. This is possible because n-1>=k-1. Then the full predicate is true precisely when the symbol of p is c. CRT realizes the context. This distinguishes c from every other color and *, so every local encoder deciding f in all contexts must distinguish these k+1 classes (up to refinement). Conversely f depends only on these symbols, proving sufficiency. The product alphabet has 6^5*3^3*4^5 states, not the count of true states and not a global one-bit information lower bound. Arbitrary joint encoders or other budgets need not obey this coordinatewise minimality.

## Theorem 2: exact resampling influence

Let D_j=prod_{p in j} p, C_j=sum_{r=0}^{k_j}(-1)^r binom(k_j,r) prod_{p in j}(p-2r), the author's accepted group count. Put D=prod_j D_j, F=prod_j(D_j-C_j), N=D-F. Fix p in group j and define L_p=sum_{r=0}^{k_j-1}(-1)^r binom(k_j-1,r) prod_{q in j, q!=p}(q-2(r+1)). This counts assignments of the other coordinates of j in which a specified color is absent and all the other k_j-1 colors occur, by inclusion-exclusion. There are k_j disjoint choices of the absent color. O_p=prod_{i!=j}(D_i-C_i). The conditional f as a function of p is nonconstant exactly when the other two groups fail and the remaining coordinates in j miss exactly one color. If they miss two or more it is identically zero; if they miss none or another group succeeds it is identically one. In the nonconstant case f=1 precisely on the two residues for the missing color. Consequently the exact probability that replacing p with an independent uniformly sampled residue changes f is

I_p = 4(p-2) k_j L_p O_p/(p D).

Indeed, the two independent samples disagree with probability 2(2/p)(1-2/p), and the nonconstant-context probability is k_j L_p O_p/(D/p). This is an equality, not the earlier cylinder lower bound. For accepted roots, the probability that some change of coordinate p alone can destroy acceptance is 2 k_j L_p O_p/N. For rejected roots, the probability that a change of p alone can repair rejection is (p-2)k_j L_p O_p/F. These counts count residue assignments, not prime magnitudes or number of covering dictionaries. All quantities are exact rational relative frequencies on R4 (or joint CRT sampling for resampling).

## Theorem 3: robustness histograms

In a successful group count singleton colors s. If exactly one group succeeds, precisely the s coordinates carrying these singleton colors can individually destroy the full predicate; if two or three groups succeed no single-coordinate change can destroy it. A failed group can be repaired in one coordinate only if precisely one color is absent. In that case any coordinate except those carrying singleton colors can repair it, so there are n-s such coordinates. On a rejected root, repairable coordinate counts add over the three groups. The weight of each full group assignment is the product of its local integer weights, 2 for a color and p-2k for *. Thus finite enumeration or a DP retaining color occupancy capped at 2 gives the exact singleton histogram for accepted groups and the near-miss histogram for rejected groups. Combine accepted histograms weighted by the other groups' failure counts, placing multiple-success roots in bin zero; convolve the rejected histograms, placing the groups missing >=2 colors in bin zero. This proves the histogram construction. Conditional means also equal the sum over the thirteen respective marginal critical/repair probabilities (linearity of expectation).

## General finite dictionary extension

For an arbitrary finite exact cover dictionary expressed as a union of partial phase prescriptions, normalize each conjunction to at most one symbol per prime; contradictory conjunctions vanish; remove a term only when another term is a subset of its required literals. Conditioning on one prime symbol deletes incompatible terms and removes matched literals from surviving terms. With integer symbol weights w_p(s), total integer union mass obeys W(A,P)=sum_s w_p(s) W(A restricted to s,P without p), with empty union mass 0 and a surviving empty term mass prod of remaining denominators. Induction on |P| proves exact counting without overlap double-counting. Disjoint variable components factor via the product of complementary counts. Cofactor equality gives the exact local observer quotient: merge two symbols iff their conditioned Boolean functions agree on every remaining assignment. For general influence condition on the other variables; if a context accepts total local weight a of p then resampling flip probability is 2a(p-a)/p^2. Unlike the color model a need not be 2. This is an exact counting interface, not a tractability guarantee or a new higher-budget classification.

## Executed exact arithmetic

The following reproducible JS uses BigInt throughout the mathematical computation. Direct group and omitted-coordinate enumerations independently crosscheck the inclusion-exclusion counts, including all 13 exact cofactor counts; the two histogram moments match the sum of their marginal counts. Decimal strings are truncated displays, not used in the proof. The original full density is recovered. The exact numerators/denominators and histograms follow.

```js
const groups=[{"name":"G","k":5,"p":["92737","649657","40388473189","77158673929","118750098349"]},{"name":"R","k":2,"p":["209924353","4261383649","24929060818265360451708193"]},{"name":"H","k":3,"p":["8369281","394783681","4278255361","46908728641","750016890283777055704738227247474485366338380663681"]}];
function calc(groups){
 const prod=a=>a.reduce((x,y)=>x*y,1n),sum=a=>a.reduce((x,y)=>x+y,0n);
 function choose(n,k){let r=1n;for(let j=1;j<=k;j++)r=r*BigInt(n-j+1)/BigInt(j);return r}
 function gcd(a,b){while(b){[a,b]=[b,a%b]}return a}
 function frac(n,d){const g=gcd(n,d);return [String(n/g),String(d/g)]}
 function fmt(n,d){if(!n)return "0";let e=0,a=n;while(a<d){a*=10n;e--}while(a>=10n*d){d*=10n;e++}let z=(a*10n**14n/d).toString().padStart(15,"0");return z[0]+"."+z.slice(1)+"e"+e}
 function ie(p,k,miss=0){let z=0n;for(let j=0;j<=k;j++)z+=(j%2?-1n:1n)*choose(k,j)*prod(p.map(x=>x-2n*BigInt(j+miss)));return z}
 function enumeration(p,k){let good=Array(p.length+1).fill(0n),near=Array(p.length+1).fill(0n),count=0,missingOne=0n;
 const c=Array(k).fill(0);
 function rec(i,w){if(i===p.length){count++;let m=c.filter(x=>x===0).length,s=c.filter(x=>x===1).length;if(m===0)good[s]+=w;if(m===1){near[p.length-s]+=w;if(c[0]===0)missingOne+=w;}return}
 rec(i+1,w*(p[i]-2n*BigInt(k)));for(let j=0;j<k;j++){c[j]++;rec(i+1,w*2n);c[j]--}}
 rec(0,1n);return {good,near,count,missingOne};}
 const gs=groups.map(g=>{let p=g.p.map(BigInt),D=prod(p),a=enumeration(p,g.k),N=sum(a.good);if(N!==ie(p,g.k))throw Error("density mismatch");return {...g,p,D,N,a}});
 const D=prod(gs.map(g=>g.D)),F=prod(gs.map(g=>g.D-g.N)),N=D-F;
 const pos=Array(14).fill(0n);let totalExclusive=0n;const results=[];let checks=0;
 for(const g of gs){let other=prod(gs.filter(h=>h!==g).map(h=>h.D-h.N));totalExclusive+=g.N*other;g.a.good.forEach((v,i)=>{pos[i]+=v*other});let rows=[];
 for(const p of g.p){const rem=g.p.filter(q=>q!==p),a=enumeration(rem,g.k);checks+=a.count;let L=ie(rem,g.k-1,1);if(L!==a.missingOne||sum(a.near)!==BigInt(g.k)*L)throw Error("cofactor mismatch");
 // Weighted resampling over two independently drawn q residues. Denominator D*q.
 const flip=4n*(p-2n)*BigInt(g.k)*L*other;
 const den=D*p;
 // Accepted roots on which q has unique needed color.
 const critical=2n*BigInt(g.k)*L*other;
 const repair=BigInt(g.k)*L*(p-2n)*other;
 rows.push({p:String(p),missing_specific_color_count:String(L),influence_fraction:frac(flip,den),influence_approx:fmt(flip,den),critical_given_accepted:frac(critical,N),critical_given_accepted_approx:fmt(critical,N),repairable_given_rejected:frac(repair,F),repairable_given_rejected_approx:fmt(repair,F)});
 }
 results.push({name:g.name,k:g.k,enumerated:g.a.count,group_success_num:String(g.N),group_den:String(g.D),accepted_singleton_histogram:g.a.good.map(String),near_repair_coordinate_histogram:g.a.near.map(String),rows});}
 pos[0]+=N-totalExclusive;
 if(sum(pos)!==N)throw Error("positive histogram mismatch");
 // False roots: groups either deficient by one color, or deficient by >=2; number of coordinates that could repair adds over independent groups.
 let neg=[1n];
 for(const g of gs){let hist=g.a.near.slice();hist[0]+=g.D-g.N-sum(hist);let next=Array(neg.length+hist.length-1).fill(0n);neg.forEach((x,i)=>hist.forEach((y,j)=>next[i+j]+=x*y));neg=next}
 if(sum(neg)!==F)throw Error("negative histogram mismatch");
 const meanPos=sum(pos.map((x,i)=>x*BigInt(i))),meanNeg=sum(neg.map((x,i)=>x*BigInt(i)));
 const criticalSum=gs.reduce((acc,g)=>acc+g.p.reduce((a,p)=>a+2n*BigInt(g.k)*ie(g.p.filter(x=>x!==p),g.k-1,1)*prod(gs.filter(h=>h!==g).map(h=>h.D-h.N)),0n),0n);
 const repairSum=gs.reduce((acc,g)=>acc+g.p.reduce((a,p)=>a+(p-2n)*BigInt(g.k)*ie(g.p.filter(x=>x!==p),g.k-1,1)*prod(gs.filter(h=>h!==g).map(h=>h.D-h.N)),0n),0n);
 if(meanPos!==criticalSum||meanNeg!==repairSum)throw Error("moment mismatch");
 return {density_fraction:frac(N,D),density_approx:fmt(N,D),common_den:String(D),accepted_count:String(N),rejected_count:String(F),group_results:results,cofactor_enumeration_states:checks,coordinate_quotient_size:String(prod(gs.map(g=>BigInt(g.k+1)**BigInt(g.p.length)))),accepted_critical_histogram:pos.map((v,i)=>({i,count:String(v),conditional_approx:fmt(v,N)})).filter(x=>x.count!=="0"),rejected_repair_histogram:neg.map((v,i)=>({i,count:String(v),conditional_approx:fmt(v,F)})).filter(x=>x.count!=="0"),mean_critical_given_accepted:fmt(meanPos,N),mean_repairable_given_rejected:fmt(meanNeg,F)};
}
console.log(JSON.stringify(calc(groups),null,2));
```

```json
{
  "density_fraction": [
    "2211302568955076227028475395829150344215995637700156808334005629626786419054341235330460874675364524489144830199982955984179691775966772937902842658279809352",
    "247270018077905641740348367855071566450549192243989999101589485734933219228412229611981969933441922493279983634102020596544059341940051477989933276542437754205026713679687681"
  ],
  "density_approx": "8.94286572284059e-18",
  "common_den": "247270018077905641740348367855071566450549192243989999101589485734933219228412229611981969933441922493279983634102020596544059341940051477989933276542437754205026713679687681",
  "accepted_count": "2211302568955076227028475395829150344215995637700156808334005629626786419054341235330460874675364524489144830199982955984179691775966772937902842658279809352",
  "rejected_count": "247270018077905639529045798899995339422073796414839654885593848034776410894406599985195550879100687162819108958737496107399229141957095493810241500575664816302184055399878329",
  "group_results": [
    {
      "name": "G",
      "k": 5,
      "enumerated": 7776,
      "group_success_num": "3840",
      "group_den": "22295300680984327451620939107576479079198721",
      "accepted_singleton_histogram": [
        "0",
        "0",
        "0",
        "0",
        "0",
        "3840"
      ],
      "near_repair_coordinate_histogram": [
        "0",
        "453692136597120",
        "38400",
        "0",
        "0",
        "0"
      ],
      "rows": [
        {
          "p": "92737",
          "missing_specific_color_count": "384",
          "influence_fraction": [
            "7898834659869504420970727216606011796749976143427511056986324433500150581235724399669379890716984312027327160857307891754543118554229363200",
            "22931079666490735498074686589775771857924580441130900546684104138600501951585264937526371945717603566259305842275719084061706431193494553914352442266716050011711562346513196472897"
          ],
          "influence_approx": "3.44459780121565e-40",
          "critical_given_accepted": [
            "1774508604237321494260241372505439288642811987434515702671214669376033541191685178121659363310549844545238035094918291312733217985440",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "1.92593302696791e-23",
          "repairable_given_rejected": [
            "178051200",
            "22295300680984327451620939107576479079194881"
          ],
          "repairable_given_rejected_approx": "7.98604165728340e-36"
        },
        {
          "p": "649657",
          "missing_specific_color_count": "384",
          "influence_fraction": [
            "55335282589718260576974581225041015731035809041444974343305662369607379369738443250846077456232732444385757553100278842053137539055889113600",
            "160640698134437945496109499615622228645564436585653810846341320534099510404272603853031370641050079041216794327779816394689023959906748023036506082638730484083575039729004859775417"
          ],
          "influence_approx": "3.44466148568458e-40",
          "critical_given_accepted": [
            "1774508604237321494260241372505439288642811987434515702671214669376033541191685178121659363310549844545238035094918291312733217985440",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "1.92593302696791e-23",
          "repairable_given_rejected": [
            "1247337600",
            "22295300680984327451620939107576479079194881"
          ],
          "repairable_given_rejected_approx": "5.59462111701348e-35"
        },
        {
          "p": "40388473189",
          "missing_specific_color_count": "384",
          "influence_fraction": [
            "3440145272752312980270169587532032658608315147589493682032007261639120033543985768507773994512750429630833500270256275614728669101880140627069440",
            "9986858495583037324701899354634467399264237945271996825098681031889648285512186602723245665808223201108454651676288244954245526789170752364076243751533169856411093434480845437962084709"
          ],
          "influence_approx": "3.44467209010101e-40",
          "critical_given_accepted": [
            "1774508604237321494260241372505439288642811987434515702671214669376033541191685178121659363310549844545238035094918291312733217985440",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "1.92593302696791e-23",
          "repairable_given_rejected": [
            "77545868519040",
            "22295300680984327451620939107576479079194881"
          ],
          "repairable_given_rejected_approx": "3.47812615889853e-30"
        },
        {
          "p": "77158673929",
          "missing_specific_color_count": "384",
          "influence_fraction": [
            "6572099077200162225575729574790182389101707096519677681643337707043415258564369263791745399192566849328634935223375180837144599184638886093898240",
            "19079026697291056730273031798196812124717181027328360150616546075436509187035332197026795009521527130317880950926134251928785139046778746255699782029204539207484704813545465528837168649"
          ],
          "influence_approx": "3.44467209018230e-40",
          "critical_given_accepted": [
            "1774508604237321494260241372505439288642811987434515702671214669376033541191685178121659363310549844545238035094918291312733217985440",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "1.92593302696791e-23",
          "repairable_given_rejected": [
            "148144653939840",
            "22295300680984327451620939107576479079194881"
          ],
          "repairable_given_rejected_approx": "6.64465826496758e-30"
        },
        {
          "p": "118750098349",
          "missing_specific_color_count": "384",
          "influence_fraction": [
            "10114707420997422161820511631855000511301038895799004859897082524528947462781597943069244581950137482034843751586236059519180737718949882275248640",
            "29363338965510302900608328204311378694436205424036320397486173073247652328321130161537229038410989280156633348142725376139230696367073333473427385421362297984057610559635175802353738669"
          ],
          "influence_approx": "3.44467209021357e-40",
          "critical_given_accepted": [
            "1774508604237321494260241372505439288642811987434515702671214669376033541191685178121659363310549844545238035094918291312733217985440",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "1.92593302696791e-23",
          "repairable_given_rejected": [
            "228000188826240",
            "22295300680984327451620939107576479079194881"
          ],
          "repairable_given_rejected_approx": "1.02263787373229e-29"
        }
      ]
    },
    {
      "name": "R",
      "k": 2,
      "enumerated": 27,
      "group_success_num": "199432486546122919384129512",
      "group_den": "22300745198530623141530995906165491860766721",
      "accepted_singleton_histogram": [
        "0",
        "48",
        "199432486546122919384129464",
        "0"
      ],
      "near_repair_coordinate_histogram": [
        "0",
        "0",
        "445862035678488353182329855787339884",
        "199432486546122919384129480"
      ],
      "rows": [
        {
          "p": "209924353",
          "missing_specific_color_count": "49858121636530729426183672",
          "influence_fraction": [
            "928412125597300860021649175687632850515376801787587880203121512999433006512294090456061949307343047386172481228630350601577430829348088974477711549666252989631854656",
            "51907998561302645437392425116581896355828045676492218699871754064508585544731596518582756085943248642477947412239455409722185693350371071303730483591341322594263262216924685675995393"
          ],
          "influence_approx": "1.78857238061463e-17",
          "critical_given_accepted": [
            "276412705688590190050667697338633444946132286062059767962293686273988113494362455613850495275362030113580201454520142413581116308104034871613617478108296316",
            "276412821119384528378559424478643793026999454712519601041750703703348302381792654416307609334420565561143103774997869498022461471995846617237855332284976169"
          ],
          "critical_given_accepted_approx": "9.99999582397104e-1",
          "repairable_given_rejected": [
            "20932867653255542532696419502793744",
            "22300745198530622942098509360042572476637209"
          ],
          "repairable_given_rejected_approx": "9.38662249485492e-10"
        },
        {
          "p": "4261383649",
          "missing_specific_color_count": "49858121636530721323265080",
          "influence_fraction": [
            "18846409341510110702954973813592529097839606577369209801456735111383814211746927163284854226533296315013349504612778343537218359570938999576907775865727418270415228480",
            "1053712411925121509877172438341439174997187294898696600691038124421163168526888271500133581157179026803988634637349949367974080387829035306524585051258939500369581831282825707240127969"
          ],
          "influence_approx": "1.78857239681536e-17",
          "critical_given_accepted": [
            "276412705688590145128204145321237505705145306079402527117982800214535198884941641985257139453778689475581578407061138860909546141406987821379964100568099740",
            "276412821119384528378559424478643793026999454712519601041750703703348302381792654416307609334420565561143103774997869498022461471995846617237855332284976169"
          ],
          "critical_given_accepted_approx": "9.99999582397104e-1",
          "repairable_given_rejected": [
            "424929168424097787320152025116293520",
            "22300745198530622942098509360042572476637209"
          ],
          "repairable_given_rejected_approx": "1.90544829171043e-8"
        },
        {
          "p": "24929060818265360451708193",
          "missing_specific_color_count": "8942615992",
          "influence_fraction": [
            "19774821458262204663535458354489518396765214055685371444999771563893628256458481735658760837069710849200229571692436277625006493516856307441684988345674075861246587456",
            "6164209319197684888701509916906424787720427428138181483298154322659429039498847413752491972578999130576823844084771786610636858567120434305538137335397619676631780006645298426567193334010263188870433"
          ],
          "influence_approx": "3.20800615849885e-33",
          "critical_given_accepted": [
            "49577733800377774891071287528129308216136269200703201819475618520667066636652572392121862004921668927972182396287914614997355744880544861276",
            "276412821119384528378559424478643793026999454712519601041750703703348302381792654416307609334420565561143103774997869498022461471995846617237855332284976169"
          ],
          "critical_given_accepted_approx": "1.79361194605965e-16",
          "repairable_given_rejected": [
            "445862035877920836150180025107980944",
            "22300745198530622942098509360042572476637209"
          ],
          "repairable_given_rejected_approx": "1.99931451576469e-8"
        }
      ]
    },
    {
      "name": "H",
      "k": 3,
      "enumerated": 1024,
      "group_success_num": "1857286756130554389486853344912331521416416237258591210882009440",
      "group_den": "497323236409786642155276935855152282913758255070409245538768223328754854066770925322241",
      "accepted_singleton_histogram": [
        "0",
        "2880",
        "432009728803455584085929218894545303571040623181156160",
        "1857286755698544660683397760826402302521870933687550587700850400",
        "0",
        "0"
      ],
      "near_repair_coordinate_histogram": [
        "0",
        "0",
        "0",
        "3983975846949372582369373002870266011439946616568183865960652765409250000",
        "5571860267383640467919163671869826386828643003443345511889988320",
        "216004864401727792042964609447272651785520311590579040"
      ],
      "rows": [
        {
          "p": "8369281",
          "missing_specific_color_count": "309497575871549482781777859294013045805335812565355862388884944",
          "influence_fraction": [
            "15454652808710506231957825441822137771834975416569205444612386875318410814464802325691881655992880129655582196483363690205788809673037391844837511319298986048",
            "2069472264169072207210304528470461214734818794212972863670949952761147627957185133459198073306526746526480794709200993040264861513371375973763066762634369989950800179291850194527361"
          ],
          "influence_approx": "7.46791975727000e-24",
          "critical_given_accepted": [
            "38470689472151927682873044385061270341196096005226389684156153304141677990981467075628322881798022191376895081810919460639393214340400449082983311444",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "4.17535148872882e-7",
          "repairable_given_rejected": [
            "7770814686877997351119185061363014629953905312153506839854553785706128",
            "497323236409786642155275078568396152359368768217064333207246806912517595475560043312801"
          ],
          "repairable_given_rejected_approx": "1.56252797335111e-17"
        },
        {
          "p": "394783681",
          "missing_specific_color_count": "307179037258358510456066555300101873767110514925765188781985744",
          "influence_fraction": [
            "723543623111551753328926806193584815129840744195361696518411404584609951880487550190267916999217522552020128426185304023081551951279039620702161537805255952448",
            "97618167937732134016921974884167227521783914585659021972512190129333926576172559791635443795955527161613769702690552820641479625693531203810356339857814529318433674729800157635533761"
          ],
          "influence_approx": "7.41197707759768e-24",
          "critical_given_accepted": [
            "38182494067822549289546428106094570798788473144394355803144125407252986592800586948691754142864903963014183628934148095352743797154238466119471212244",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "4.14407268590460e-7",
          "repairable_given_rejected": [
            "363807811321598538776417767710693500401720434845933979352445582825616528",
            "497323236409786642155275078568396152359368768217064333207246806912517595475560043312801"
          ],
          "repairable_given_rejected_approx": "7.31531898545409e-16"
        },
        {
          "p": "4278255361",
          "missing_specific_color_count": "283877682434848787581961488521470101643567061103161140460042704",
          "influence_fraction": [
            "7246226575241817949115513769064741507012377913719447787344475513007334976597517252772327319249735802729754230987905740271500570238843894835355538081429464203328",
            "1057884280456366727427790774783560000205729823112069833686760400966711070140942904855424812703088718089021576456589232038097039952357157376326405544399979865936455830948335858043907841"
          ],
          "influence_approx": "6.84973461569523e-24",
          "critical_given_accepted": [
            "35286125063408401207881212447479991901084464120651810046154354976870875777422618646629694819728071906534805748197050585557686875786115149405829029204",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "3.82972015413511e-7",
          "repairable_given_rejected": [
            "3643503648532175981481538169995789346744596461121438803041188271270552208",
            "497323236409786642155275078568396152359368768217064333207246806912517595475560043312801"
          ],
          "repairable_given_rejected_approx": "7.32622846025635e-15"
        },
        {
          "p": "46908728641",
          "missing_specific_color_count": "28089082428518792456378171992925869676435408823780466339085264",
          "influence_fraction": [
            "7861495505206227230341648239250183035941250654333012137768300326055047888093901424373202071265724753980498737771836057517927702521214753338842695941752212281408",
            "11599122179071640146000964568520799326263611604395068730974294978118722835042152676154246949792447973370624898329012717873078222071666905270600764199025223332637054790156472021659571521"
          ],
          "influence_approx": "6.77766419202891e-25",
          "critical_given_accepted": [
            "3491485723667537731469242310489986217042768585445519366257086494035862465645487071410437829823471070260720843684199496607255735801566796922981431764",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "3.78942522585760e-8",
          "repairable_given_rejected": [
            "3952869436073673450144611744337088344884961975977232196827073225379027088",
            "497323236409786642155275078568396152359368768217064333207246806912517595475560043312801"
          ],
          "repairable_given_rejected_approx": "7.94829026009267e-15"
        },
        {
          "p": "750016890283777055704738227247474485366338380663681",
          "missing_specific_color_count": "1770616059510274145744",
          "influence_fraction": [
            "7923360172643475591953800705044105315060779407637635710822361500928210149968506359339509328242704683916429648033542212627860344413551057098209188991651401232448",
            "185456690019204124825755728147872071804383309602576377434884470937467427778517279587786567681687915727560635763337102819592528653110022454417086348169001984963607797603084367313849875787150322636074056111006243325145579813761"
          ],
          "influence_approx": "4.27235068835910e-65",
          "critical_given_accepted": [
            "220088381655355843908252847125705995015402729324244390820806197622506749766635649529853778497423635673372244",
            "92137607039794842792853141492881264342333151570839867013916901234449434127264218138769203111473521853714367924999289832674153823998615539079285110761658723"
          ],
          "critical_given_accepted_approx": "2.38869218255579e-48",
          "repairable_given_rejected": [
            "3983975852521232849969018335191157475352735666998728384522380268479696528",
            "497323236409786642155275078568396152359368768217064333207246806912517595475560043312801"
          ],
          "repairable_given_rejected_approx": "8.01083794371212e-15"
        }
      ]
    }
  ],
  "cofactor_enumeration_states": 7787,
  "coordinate_quotient_size": "214990848",
  "accepted_critical_histogram": [
    {
      "i": 0,
      "count": "8258253303549502423224704587937699142062252258300476507251644479065330571750142076445039459788343037029376392870317765927576489711360",
      "conditional_approx": "3.73456505658193e-24"
    },
    {
      "i": 1,
      "count": "532222612387029398180474123919019510633270033470553176718866125017047976620510329899773706486096619730085103321949741234908956772208",
      "conditional_approx": "2.40682853562877e-25"
    },
    {
      "i": 2,
      "count": "2211301645508721753822445556883389810134150983804947634110895522251538631092490451455902666320940340472571820972529072141974228631955683661520302955471173624",
      "conditional_approx": "9.99999582397105e-1"
    },
    {
      "i": 3,
      "count": "923446354473205978460263342901834161002923557186961529984365257588555302704211889101170887212919891744589568156206279617969672618969883871620130501600",
      "conditional_approx": "4.17602894980386e-7"
    },
    {
      "i": 5,
      "count": "42588206501695715862245792940130542927427487698428376864109152065024804988600444274919824719453196269085712842278038991505597231650560",
      "conditional_approx": "1.92593302696791e-23"
    }
  ],
  "rejected_repair_histogram": [
    {
      "i": 0,
      "count": "247270013134198294123491035688933193751339170807826325227513728155078182267012537119854309059517300596118757049006345183543402736200746433272422136118935690056957089269921845",
      "conditional_approx": "9.99999980006846e-1"
    },
    {
      "i": 1,
      "count": "5031753649814399170678922387524168813704856672141683932895601152773591226219087486658479281444467481908073875649551898546978362607926340298422400",
      "conditional_approx": "2.03492266831520e-29"
    },
    {
      "i": 2,
      "count": "4943705362354209956828428578822847733189142711471005016302173716597723045800990531215282892231824309448694549376967792091215074247753224961914178432166041840086416684",
      "conditional_approx": "1.99931451487039e-8"
    },
    {
      "i": 3,
      "count": "1983051302432816076535888131753005048549958521659469479127193855279025262715725793493704070663148437984037754365886787196006008976902140219976913639564532444760",
      "conditional_approx": "8.01978063433485e-15"
    },
    {
      "i": 4,
      "count": "2770339008175024250543981008886166861432994965808038695453725694692395882619445860012855288785257472973186566037208220463842550986696251484671022165600",
      "conditional_approx": "1.12036996224192e-23"
    },
    {
      "i": 5,
      "count": "39603222444000115552278410784354590572565365193250331176279963460412443286565116725377638996490980443916313522312107574821580364768625767873738157296800",
      "conditional_approx": "1.60161845547819e-22"
    },
    {
      "i": 6,
      "count": "73102170110995866407668939832936892158412882792390869792949585752531532805596517865904728480781902596616170032206631405914692989064188707047680",
      "conditional_approx": "2.95637015272769e-31"
    },
    {
      "i": 7,
      "count": "26921983941275698166558848402919003725603256702399539979038615703302649144726906602309375110372481243170246956008871712459621248396160",
      "conditional_approx": "1.08876863238605e-40"
    },
    {
      "i": 8,
      "count": "960445595781193620137907284260377513053341189505980385313316772705665386655374477660808495369573090461966287093298523718400",
      "conditional_approx": "3.88419753938220e-51"
    },
    {
      "i": 9,
      "count": "65913028884765433079707230845878371714918153074254681301399081143170444508944947037594144768000",
      "conditional_approx": "2.66562963828468e-79"
    },
    {
      "i": 10,
      "count": "1654210069005875842969499809771149490538891704756478890557042702556602606109409280000",
      "conditional_approx": "6.68989342850573e-90"
    }
  ],
  "mean_critical_given_accepted": "2.00000041760289e0",
  "mean_repairable_given_rejected": "3.99863143567505e-8"
}
```

## Remaining

Budget nine already had exact density in the original proof. This result gives an exact local observable and sensitivity profile; it does not identify a complete dictionary for budgets 10 and higher, calculate those full densities, or settle budget19 sharpness. The derived result uses the complete original budget-nine classification as a premise; no custom target axiom, no new proof-checker claim. Preserve the author's classification, original full density and minimum, and distinguish informed new derivation from independent review. No formal Task, Review, Result or mother-objective acceptance claimed.
