vertex_num=int(input("Vertex number: "))
vertex_map={v:[] for v in range(vertex_num)}
current_verex=0

def min_arrive_to_vertex(map):
    for v in map:
        print(len(map[v]))

min_arrive_to_vertex(vertex_map)
#for p in range(int(vertex_num*(vertex_num-1))/2):
    #pass
