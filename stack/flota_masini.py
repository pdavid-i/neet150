class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tempos = {}
        batches = 0
        for index, value in enumerate(position):
            tempos[value] = (target - position[index]) / speed[index]
        position.sort(reverse=True)
        current_tempo = 0
        for car_position in position:
            if tempos[car_position] > current_tempo:
                batches += 1
                current_tempo = tempos[car_position]
        return batches
