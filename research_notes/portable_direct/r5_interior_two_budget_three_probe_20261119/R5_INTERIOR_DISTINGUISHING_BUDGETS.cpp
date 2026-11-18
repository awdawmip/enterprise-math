// Research extension of the pinned complete 18-chamber enumerator.
// Frozen science: exact onset matrix generated from EXACT_R5_ALL_101_BUDGETS.json.
#include <bits/stdc++.h>
using namespace std;
constexpr int NK=101, NH=256, NS=9, ST=18;
const int H[7]={18,24,82,34,17,144,208};
vector<unsigned char> onset,rankidx,slotorder;
struct Pair {int x,y;array<int,9> states;}; vector<Pair> pairs;
inline size_t indexOnset(int k,int i,int j){return (size_t(k)*NH+i)*NH+j;}
string fam(const Pair& p,int k,int st,const uint8_t* os){
 uint16_t masks[9];for(int i=0;i<9;i++){uint16_t m=0;int a=p.states[os[i]];for(int j=i;j<9;j++){int b=p.states[os[j]];if(onset[indexOnset(k,a,b)]>st)break;m|=uint16_t(1u<<os[j]);}masks[i]=m;}
 vector<uint16_t> maximal;for(int i=0;i<9;i++){bool ok=true;for(int j=0;j<9;j++)if(i!=j&&masks[i]!=masks[j]&&(masks[i]&masks[j])==masks[i]){ok=false;break;}if(ok)maximal.push_back(masks[i]);}
 sort(maximal.begin(),maximal.end());maximal.erase(unique(maximal.begin(),maximal.end()),maximal.end());string s;s.push_back(char(maximal.size()));for(auto m:maximal){s.push_back(char(m&255));s.push_back(char(m>>8));}return s;
}
string profile(int pi,int st){string key;key.reserve(1600);for(int k=0;k<NK;k++)key+=fam(pairs[pi],k,st,slotorder.data()+(size_t(pi)*NK+k)*NS);return key;}
string prefix(int old,string&& sig){string key;key.reserve(4+sig.size());for(int j=0;j<4;j++)key.push_back(char((unsigned(old)>>(j*8))&255));key+=sig;return key;}
int main(int argc,char**argv){
 string root=argc>1?argv[1]:".";auto read=[&](string name,size_t expect){ifstream f(root+"/"+name,ios::binary);if(!f){cerr<<"MISSING "<<name<<"\n";exit(3);}vector<unsigned char> v((istreambuf_iterator<char>(f)),{});if(v.size()!=expect){cerr<<"SIZE_FAIL "<<name<<"\n";exit(4);}return v;};
 onset=read("onset_18.bin",NK*NH*NH);rankidx=read("ranks_18.bin",NK*NH);
 vector<int> candidates;for(int x=0;x<NH;x++)if(find(begin(H),end(H),x)==end(H))candidates.push_back(x);
 for(int i=0;i<(int)candidates.size();i++)for(int j=i+1;j<(int)candidates.size();j++){int x=candidates[i],y=candidates[j];pairs.push_back({x,y,{18,24,82,34,17,x,144,208,y}});}if(pairs.size()!=30876)return 5;
 slotorder.resize(size_t(pairs.size())*NK*NS);
 for(int pi=0;pi<(int)pairs.size();pi++)for(int k=0;k<NK;k++){auto*o=slotorder.data()+(size_t(pi)*NK+k)*NS;for(int i=0;i<NS;i++)o[i]=i;sort(o,o+NS,[&](unsigned a,unsigned b){int ra=rankidx[k*NH+pairs[pi].states[a]],rb=rankidx[k*NH+pairs[pi].states[b]];return ra==rb?a<b:ra<rb;});}
 int stages[ST]={0,17,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
 vector<int> grp(pairs.size(),0),endpoint;
 for(int step=0;step<ST;step++){unordered_map<string,int> mp;mp.reserve(pairs.size()*2);vector<int> nx(pairs.size());for(int i=0;i<(int)pairs.size();i++){auto key=prefix(grp[i],profile(i,stages[step]));auto it=mp.find(key);if(it==mp.end()){int g=mp.size();mp.emplace(move(key),g);nx[i]=g;}else nx[i]=it->second;}grp.swap(nx);if(step==1)endpoint=grp;cout<<"REFINE_STAGE "<<stages[step]<<" CLASSES "<<mp.size()<<"\n";}
 map<int,map<int,vector<int>>> buckets;for(int i=0;i<(int)pairs.size();i++)buckets[endpoint[i]][grp[i]].push_back(i);
 struct Witness{int a,b,stage;bitset<NK> budgets;};vector<Witness> witnesses;
 long long parentEqPairs=0;
 for(auto &[eg,groups]:buckets){long long n=0;for(auto &[f,vec]:groups)n+=vec.size();parentEqPairs+=n*(n-1)/2;vector<pair<int,const vector<int>*>> v;for(auto &[f,vec]:groups)v.push_back({f,&vec});for(int i=0;i<(int)v.size();i++)for(int j=i+1;j<(int)v.size();j++)for(int a:*v[i].second)for(int b:*v[j].second){Witness w={a,b,99,{}};for(int st=1;st<=16;st++){for(int k=0;k<NK;k++)if(fam(pairs[a],k,st,slotorder.data()+(size_t(a)*NK+k)*NS)!=fam(pairs[b],k,st,slotorder.data()+(size_t(b)*NK+k)*NS)){w.budgets.set(k);w.stage=min(w.stage,st);}}if(w.budgets.none()||w.stage==99){cerr<<"INCONSISTENT_PARTITION";return 6;}witnesses.push_back(move(w));}}
 cout<<"ENDPOINT_INDISTINGUISHABLE_PAIR_INSTANCES "<<parentEqPairs<<"\n";
 cout<<"INTERIOR_SPLIT_INSTANCE_PAIRS "<<witnesses.size()<<"\n";
 vector<int> coverage(NK,0),byFirstStage(ST,0);map<int,int> countSizes;
 for(auto&w:witnesses){byFirstStage[w.stage]++;countSizes[w.budgets.count()]++;for(int k=0;k<NK;k++)if(w.budgets[k])coverage[k]++;}
 for(int st=0;st<ST;st++)if(byFirstStage[st])cout<<"FIRST_SPLIT_STAGE "<<st<<" COUNT "<<byFirstStage[st]<<"\n";
 for(int k=0;k<NK;k++)if(coverage[k])cout<<"BUDGET "<<k+214<<" SEPARATED_PAIRS "<<coverage[k]<<"\n";
 for(auto [n,c]:countSizes)cout<<"PAIR_WITNESS_BUDGET_COUNT "<<n<<" INSTANCES "<<c<<"\n";
 ofstream csv(root+"/interior_distinguishing_budget_witnesses.csv");csv<<"xA,yA,xB,yB,first_split_stage,witness_budget_count,witness_budget_list\n";
 for(auto&w:witnesses){auto A=pairs[w.a],B=pairs[w.b];csv<<A.x<<","<<A.y<<","<<B.x<<","<<B.y<<","<<w.stage<<","<<w.budgets.count()<<",\"";bool first=true;for(int k=0;k<NK;k++)if(w.budgets[k]){if(!first)csv<<";";first=false;csv<<k+214;}csv<<"\"\n";}
 for(int k=0;k<NK;k++)if(coverage[k]==(int)witnesses.size())cout<<"UNIVERSAL_BUDGET "<<k+214<<"\n";
 for(int k=0;k<NK;k++)for(int j=k+1;j<NK;j++){int c=0;for(auto&w:witnesses)if(w.budgets[k]||w.budgets[j])c++;if(c==(int)witnesses.size())cout<<"UNIVERSAL_PAIR "<<k+214<<" "<<j+214<<"\n";}
 for(int k=0;k<NK;k++)for(int j=k+1;j<NK;j++)for(int h=j+1;h<NK;h++){int c=0;for(auto&w:witnesses)if(w.budgets[k]||w.budgets[j]||w.budgets[h])c++;if(c==(int)witnesses.size()){cout<<"FIRST_TRIPLE_COVER "<<k+214<<" "<<j+214<<" "<<h+214<<"\n";goto done;}}
 done:cout<<"DONE\n";return 0;
}
