def get_next_min(lst,ind):
    min_index=lst.index(sorted(lst)[0])
    if min_index == ind:
        if ind == 0:
            min_index = house_cost.index(min(house_cost[1],house_cost[2]))
        elif ind == 1:
            min_index = house_cost.index(min(house_cost[0],house_cost[2]))
        else:
            min_index = house_cost.index(min(house_cost[0],house_cost[1]))

    return min_index


tc_count=int(raw_input())
house_count=int(raw_input())
cost_list=[]
for i in range(0,house_count):
    cost_list.append([int(i) for i in raw_input().split()])
    
start_color=0
for tc in range(0,tc_count):
    prev_color=0
    total_cost=cost_list[0][start_color]
    for house in range(1,house_count):
        house_cost=cost_list[house]
        min_cost_color = get_next_min(house_cost,prev_color)
        """
        min_cost_color=house_cost.index(sorted(house_cost)[0])
        if min_cost_color == prev_color:
            if prev_color == 0:
                min_cost_color=house_cost.index(min(house_cost[1],house_cost[2]))
            elif prev_color == 1:
                min_cost_color=house_cost.index(min(house_cost[0],house_cost[2]))
            else:
                min_cost_color=house_cost.index(min(house_cost[0],house_cost[1]))
        """
        min_cost=house_cost[min_cost_color]
        total_cost += min_cost

    print(total_cost)
    start_color = get_next_min(cost_list[0],start_color)
 

