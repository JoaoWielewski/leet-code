from typing import List


gain = [-5,1,5,0,-7]


def largest_altitude(gain: List[int]) -> int:
    altitude = 0
    max_altitude = 0

    for altitude_dif in gain:
        altitude += altitude_dif
        max_altitude = max(max_altitude, altitude)

    return max_altitude


print(largest_altitude(gain))