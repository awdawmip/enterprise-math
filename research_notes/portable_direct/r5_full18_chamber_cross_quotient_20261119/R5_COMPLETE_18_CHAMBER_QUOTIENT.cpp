#include <bits/stdc++.h>
using namespace std;
constexpr int NK=101, NH=256, NS=9, ST=18;
const int H[7]={18,24,82,34,17,144,208};
vector<unsigned char> onset, rankidx, slotorder;
struct Pair{int x,y; array<int,9> states;};
vector<Pair> pairs;
inline size_t indexOnset(int k,int i,int j){return (size_t(k)*NH+i)*NH+j;}
string fam(const Pair& p,int k,int st,const uint8_t* os){
 uint16_t masks[9];
 for(int i=0;i<9;i++){
  uint16_t m=0;int a=p.states[os[i]];
  for(int j=i;j<9;j++){
   int b=p.states[os[j]];
   if(onset[indexOnset(k,a,b)]>st)break;
   m|=uint16_t(1u<<os[j]);
  }
  masks[i]=m;
 }
 vector<uint16_t> maximal;
 for(int i=0;i<9;i++){
  bool ok=true;
  for(int j=0;j<9;j++)if(i!=j&&masks[i]!=masks[j]&&(masks[i]&masks[j])==masks[i]){ok=false;break;}
  if(ok)maximal.push_back(masks[i]);
 }
 sort(maximal.begin(),maximal.end());
 maximal.erase(unique(maximal.begin(),maximal.end()),maximal.end());
 string s; s.reserve(19);s.push_back(char(maximal.size()));
 for(auto m:maximal){s.push_back(char(m&255));s.push_back(char(m>>8));}
 return s;
}
string profile(int pi,int st){
 string key;key.reserve(1600);
 for(int k=0;k<NK;k++)key+=fam(pairs[pi],k,st,slotorder.data()+(size_t(pi)*NK+k)*NS);
 return key;
}
string prefix(int old,string&& sig){
 string key; key.reserve(4+sig.size());for(int j=0;j<4;j++)key.push_back(char((unsigned(old)>>(j*8))&255));key+=sig;return key;
}
string masksFor(int pi,int k,int st){
 const string s=fam(pairs[pi],k,st,slotorder.data()+(size_t(pi)*NK+k)*NS);ostringstream os;
 os<<"[";for(int i=0;i<(unsigned char)s[0];i++){int v=(unsigned char)s[1+2*i]|((unsigned char)s[2+2*i]<<8);if(i)os<<",";os<<v;}os<<"]";return os.str();
}
int main(int argc,char**argv){
 string root=argc>1?argv[1]:".";
 auto read=[&](string name,size_t expect){ifstream f(root+"/"+name,ios::binary);if(!f){cerr<<"MISSING "<<name<<"\n";exit(3);}vector<unsigned char> v((istreambuf_iterator<char>(f)),{});if(v.size()!=expect){cerr<<"SIZE_FAIL "<<name<<" "<<v.size()<<" != "<<expect<<"\n";exit(4);}return v;};
 onset=read("onset_18.bin",NK*NH*NH);rankidx=read("ranks_18.bin",NK*NH);
 vector<int> candidates;for(int x=0;x<NH;x++)if(find(begin(H),end(H),x)==end(H))candidates.push_back(x);
 for(int i=0;i<(int)candidates.size();i++)for(int j=i+1;j<(int)candidates.size();j++){
  int x=candidates[i],y=candidates[j];pairs.push_back({x,y,{18,24,82,34,17,x,144,208,y}});
 }
 if(pairs.size()!=30876){cerr<<"PAIR_COUNT_BAD\n";return 5;}
 slotorder.resize(size_t(pairs.size())*NK*NS);
 for(int pi=0;pi<(int)pairs.size();pi++)for(int k=0;k<NK;k++){
  auto* o=slotorder.data()+(size_t(pi)*NK+k)*NS;
  for(int i=0;i<NS;i++)o[i]=i;
  sort(o,o+NS,[&](unsigned a,unsigned b){
   int ra=rankidx[k*NH+pairs[pi].states[a]];
   int rb=rankidx[k*NH+pairs[pi].states[b]];
   return ra==rb?a<b:ra<rb;
  });
 }
 vector<int> grp(pairs.size(),0),endpointGroup;
 int stages[ST]={0,17,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
 int firstWitnessA=-1,firstWitnessB=-1,firstWitnessStage=-1;
 for(int step=0;step<ST;step++){
  int st=stages[step];int prevN=*max_element(grp.begin(),grp.end())+1;
  unordered_map<string,int> map;map.reserve(pairs.size()*2);
  vector<int> next(pairs.size());vector<int> firstNew(prevN,-1);
  vector<int> firstRep;firstRep.reserve(pairs.size());
  int splits=0;
  for(int i=0;i<(int)pairs.size();i++){
    int old=grp[i];auto key=prefix(old,profile(i,st));
    auto [it,inserted]=map.emplace(move(key),map.size());
    int gid=it->second;
    if(inserted){
      // insert count before updating representative vector
      firstRep.push_back(i);
      if(firstNew[old]!=-1){
       if(firstWitnessA<0&&step>=2){firstWitnessA=firstRep[firstNew[old]];firstWitnessB=i;firstWitnessStage=st;}
      }else firstNew[old]=gid;
    }
    next[i]=gid;
  }
  int newN=map.size();
  for(int v:firstNew)if(v<0){cerr<<"GROUP_DELETION\n";return 6;}
  // Group-parent split counts.
  vector<int> newPerParent(prevN,0),parentForNew(newN,-1);
  for(int i=0;i<(int)pairs.size();i++){
   if(parentForNew[next[i]]==-1){parentForNew[next[i]]=grp[i];newPerParent[grp[i]]++;}
   else if(parentForNew[next[i]]!=grp[i]){cerr<<"PARENT_MERGE_FAIL\n";return 7;}
  }
  for(int n:newPerParent)splits+=(n>1);
  grp.swap(next);
  if(step==1) endpointGroup=grp;
  vector<int> counts(newN,0);for(int v:grp)counts[v]++;
  long long equal_pair_instances=0;for(int c:counts)equal_pair_instances+=1LL*c*(c-1)/2;
  cout<<"STAGE "<<st<<" GROUPS "<<newN<<" SPLIT_PREVIOUS "<<splits<<" EXTRA "<<(newN-prevN)<<" EQUIV_INSTANCE_PAIRS "<<equal_pair_instances<<"\n"<<flush;
  if(step==0&&newN!=1460){cerr<<"ENDPOINT_L_BAD "<<newN<<"\n";return 8;}
  if(step==1&&newN!=2563){cerr<<"ENDPOINT_CROSS_BAD "<<newN<<"\n";return 9;}
 }
 if(firstWitnessA>=0){
   const auto&a=pairs[firstWitnessA],&b=pairs[firstWitnessB];
   cout<<"FIRST_SPLIT A "<<a.x<<" "<<a.y<<" B "<<b.x<<" "<<b.y<<" STAGE "<<firstWitnessStage<<"\n";
   for(int k=0;k<NK;k++){
    auto sa=masksFor(firstWitnessA,k,firstWitnessStage),sb=masksFor(firstWitnessB,k,firstWitnessStage);
    if(sa!=sb){cout<<"WITNESS_BUDGET "<<(k+214)<<" A "<<sa<<" B "<<sb<<"\n";break;}
   }
   // Pointwise endpoint equality verified by direct full signatures.
   cout<<"ENDPOINTS_EQUAL "<<(profile(firstWitnessA,0)==profile(firstWitnessB,0))<<" "<<(profile(firstWitnessA,17)==profile(firstWitnessB,17))<<"\n";
 }else cout<<"NO_INTERIOR_SPLIT\n";
 int finalN=*max_element(grp.begin(),grp.end())+1;
 unordered_map<int,int> mult;for(int g:grp)mult[g]++;
 int singleton=0,largest=0;for(auto [k,v]:mult){singleton+=(v==1);largest=max(largest,v);}
 map<int,set<int>> e_to_f;for(int i=0;i<(int)grp.size();i++)e_to_f[endpointGroup[i]].insert(grp[i]);
 int endpoint_split=0,max_daughters=0;map<int,int> daughters_hist;
 for(auto &[e,gs]:e_to_f){endpoint_split+=gs.size()>1;max_daughters=max(max_daughters,(int)gs.size());daughters_hist[gs.size()]++;}
 cout<<"ENDPOINT_SPLIT_CLASSES "<<endpoint_split<<" MAX_DAUGHTERS "<<max_daughters<<" DAUGHTERS_HIST ";for(auto [k,v]:daughters_hist)cout<<k<<":"<<v<<" ";cout<<"\n";
 cout<<"FINAL_CLASSES "<<finalN<<" SINGLETONS "<<singleton<<" MAX_CLASS_SIZE "<<largest<<" PAIRS "<<pairs.size()<<"\n";
 return 0;
}
