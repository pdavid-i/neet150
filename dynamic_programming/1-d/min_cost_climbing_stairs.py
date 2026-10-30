class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_to_climb = {}
        cost.append(0)

        def solvit(i, current_cost):
            if i >= len(cost):
                return
            if i in cost_to_climb:
                if cost_to_climb[i] <= current_cost:
                    return
                cost_to_climb[i] = current_cost
            else: 
                cost_to_climb[i] = current_cost
            new_cost = current_cost+cost[i]
            solvit(i+1, new_cost)
            solvit(i+2, new_cost)        

        solvit(0, 0)
        solvit(1, 0)
        return cost_to_climb[len(cost)-1]
