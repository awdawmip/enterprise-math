import Lake

open Lake DSL

package enterpriseMath

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @
    "87adeaebd370a3b6a41ac4f044fddd4bf81803ad"

@[default_target]
lean_lib EnterpriseMath
