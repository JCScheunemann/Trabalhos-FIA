include("bfs_dfs.jl")

dag = {:a => [:b, :c, :d],
       :b => [:e, :f, :g],
       :c => [:h, :i, :j],
       :e => [:k, :l]}

function printwithdepth(sym, depth)
	@printf "%s%s\n" repeat(" ", depth) sym
end

bfs(:a, sym -> get(dag, sym, Symbol[]), printwithdepth)

dfs(:a, sym -> get(dag, sym, Symbol[]), printwithdepth, true)
