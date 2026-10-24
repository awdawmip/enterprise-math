// R260 independent C++17 model verifier, not an import of native EM modules.
#include <array>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using namespace std;
using Quad=tuple<int,int,int,int>; // q,r,eps,k
struct Edge {int q,eta,b;};
const Edge E[3][2]={{{2,-1,-1},{2,1,-1}},{{0,-1,-1},{0,1,-1}},{{1,1,1},{2,1,-1}}};
const int D[3][2]={{1,0},{2,0},{2,2}};
const vector<int> MODES[3]={{0,2},{1,2},{0,1,2}};
struct Base {int q,j;vector<pair<int,string>> words;};
const vector<Base> BASE={
 {0,6,{{0,"101101"},{2,"000000"}}},
 {0,7,{{0,"0101101"},{2,"0011101"}}},
 {0,8,{{0,"01011101"},{2,"00111101"}}},
 {1,5,{{1,"10110"},{2,"00010"}}},
 {1,6,{{1,"010110"},{2,"001110"}}},
 {1,7,{{1,"0101110"},{2,"0011110"}}},
 {2,7,{{0,"1110101"},{1,"1011010"},{2,"0000000"}}},
 {2,8,{{0,"11110101"},{1,"10111010"},{2,"00011010"}}},
 {2,9,{{0,"101101011"},{1,"010101010"},{2,"000000011"}}},
};
Quad walk(const string &w){int q=0,r=0,e=1,k=0;for(char c:w){int a=c-'0'; if(a!=0 && a!=1) throw runtime_error("selector");Edge x=E[q][a];r=D[r][a];q=x.q;e=x.eta*e;k=x.eta*k+x.b;}return {q,r,e,k};}
const Base& choose(int q,int m){for(const auto& b:BASE)if(b.q==q && b.j<=m && (m-b.j)%3==0)return b;throw runtime_error("missing base");}
string construct(int q,int m,int mode,const string& bits=""){
  const auto& b=choose(q,m);int h=(m-b.j)/3,K=h/7,rem=h%7;
  string prefix=""; if(bits.empty()) {for(int i=0;i<3*K;i++)prefix+="1011101";}
  else {if((int)bits.size()!=3*K)throw runtime_error("bits");for(char v:bits)prefix+=(v=='0'?"1011101":"1101101");}
  for(int i=0;i<rem;i++)prefix+="101";
  for(const auto& [r,w]:b.words)if(r==mode){string path=prefix+w;if((int)path.size()!=m)throw runtime_error("length");auto [qq,rr,e,k]=walk(path);auto [bq,br,be,bk]=walk(w);if(qq!=q||rr!=mode||e!=be||k!=bk-be*(9*K+rem))throw runtime_error("constructed effect");return path;}
  throw runtime_error("missing mode");
}
int main(){
  if(walk("101")!=Quad(0,0,1,-1))throw runtime_error("3-loop");
  if(walk("1011101")!=Quad(0,0,1,-3)||walk("1101101")!=Quad(0,0,1,-3))throw runtime_error("7-loops");
  for(const auto& b:BASE){set<pair<int,int>> eff;set<int> modes;for(auto [r,w]:b.words){auto [q,dr,e,k]=walk(w);if(q!=b.q||dr!=r||w.size()!=size_t(b.j))throw runtime_error("base word");eff.insert({e,k});modes.insert(dr);}if(eff.size()!=1||modes!=set<int>(MODES[b.q].begin(),MODES[b.q].end()))throw runtime_error("base collision");}
  map<Quad,cpp_int> cur;cur[{0,0,1,0}]=1;int first=-1;
  for(int m=0;m<=128;m++){
    cpp_int total=0;map<tuple<int,int,int>,set<int>> f;
    for(auto const& [x,n]:cur){total+=n;auto [q,r,e,k]=x;f[{q,e,k}].insert(r);}
    cpp_int expected=1; expected <<= m; if(total!=expected)throw runtime_error("mass");
    bool ok=true;
    for(int q=0;q<3;q++){
      bool found=false;for(auto const& [key,s]:f)if(get<0>(key)==q && includes(s.begin(),s.end(),MODES[q].begin(),MODES[q].end()))found=true;
      ok&=found;
    }
    if(ok && first<0)first=m;
    if(m>=7 && !ok)throw runtime_error("all-q fiber absent");
    if(m==128)break;
    map<Quad,cpp_int> nd;
    for(const auto& [x,n]:cur){auto [q,r,e,k]=x;for(int a=0;a<2;a++){auto z=E[q][a];nd[{z.q,D[r][a],z.eta*e,z.eta*k+z.b}]+=n;}}
    cur.swap(nd);
  }
  if(first!=7)throw runtime_error("threshold");
  int checks=0;
  for(int m=7;m<=511;m++)for(int q=0;q<3;q++)for(int r:MODES[q]){(void)walk(construct(q,m,r));checks++;}
  set<string> words;set<tuple<int,int,int>> effects;set<int> modes;
  for(int b=0;b<8;b++){string bits="";for(int k=2;k>=0;k--)bits.push_back('0'+((b>>k)&1));for(int r:MODES[2]){string w=construct(2,28,r,bits);auto [q,mode,e,k]=walk(w);words.insert(w);effects.insert({q,e,k});modes.insert(mode);}}
  if(words.size()!=24 || effects.size()!=1 || modes!=set<int>({0,1,2}))throw runtime_error("exp collision");
  cout << "{\"result\":\"PASS\",\"model\":\"R260_independent_cpp17\",\"dp_depth\":128,\"first_simultaneous_all_q\":"<<first<<",\"construction_depth\":511,\"word_checks\":"<<checks<<",\"depth28_distinct\":"<<words.size()<<"}\n";
}
