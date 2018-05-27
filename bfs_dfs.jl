function bfs(start_node::Any,
			 next_nodes::Function,
	         at_node::Function)
	to_process = Array(Any, 0)
	depths = Array(Int, 0)
 
	push!(to_process, start_node)
	push!(depths, 0)
 
	while !isempty(to_process)
		current_node = shift!(to_process)
		depth = shift!(depths)
 
		at_node(current_node, depth)
 
		for child_node in next_nodes(current_node)
			push!(to_process, child_node)
			push!(depths, depth + 1)
		end
	end
end
 
function dfs(current_node::Any,
			 next_nodes::Function,
	         at_node::Function,
	         pre::Bool = true,
	         depth::Integer = 0)
	if pre
		at_node(current_node, depth)
	end
 
	for child_node in next_nodes(current_node)
		dfs(child_node, next_nodes, at_node, pre, depth + 1)
	end
 
	if !pre
		at_node(current_node, depth)
	end
end
