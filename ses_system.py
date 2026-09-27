
from dataclasses import dataclass
 
 
@dataclass

class Carrier:

    id: int

    satellite_id: str
 
 
def group_by_satellite(carriers: list[Carrier]) -> dict[str, list[Carrier]]:

    """Group carriers by their satellite_id."""
    dic = {}

    for carrier in carriers:
        if carrier.satellite_id not in dic:
            dic[carrier.satellite_id] = []

        dic[carrier.satellite_id].append(carrier)

    return dic
 
 
# ---------------- Sample input data ----------------

carriers = [

    Carrier(1, "SAT-A"),

    Carrier(2, "SAT-B"),

    Carrier(3, "SAT-A"),

    Carrier(4, "SAT-C"),

    Carrier(5, "SAT-B"),

    Carrier(6, "SAT-A"),

]
 
# ---------------- Run and print result ----------------

if __name__ == "__main__":

    grouped = group_by_satellite(carriers)

    for sat_id, sat_carriers in grouped.items():

        ids = [c.id for c in sat_carriers]

        print(f"{sat_id}: carriers {ids}")
 
 
# o/p:
# SAT-A: carriers [1, 3, 6]

# SAT-B: carriers [2, 5]

# SAT-C: carriers [4]
 

from copy import deepcopy

from dataclasses import dataclass

from functools import reduce
 
 
def r(f: float) -> float:

    return round(f, 7)
 
 
@dataclass

class Carrier:

    id: int

    satellite_id: str

    min_freq: float

    max_freq: float

    start: float

    end: float
 
 
def _overlaps(a: Carrier, b: Carrier) -> bool:

    freq_overlap = r(a.min_freq) <= r(b.max_freq) and r(b.min_freq) <= r(a.max_freq)

    time_overlap = a.start <= b.end and b.start <= a.end

    return freq_overlap and time_overlap
 
 
def find_conflicts(carriers: list[Carrier]) -> list[tuple[int, int]]:

    """Return all conflicting (id_a, id_b) pairs on the same satellite."""

    conflicts = []

    working = deepcopy(carriers)                      

    for a in working:

        for b in working:                             

            if a.id == b.id:

                continue

            if a.satellite_id != b.satellite_id:      

                continue

            if _overlaps(a, b):

                pair = tuple(sorted([a.id, b.id]))    

                if pair not in conflicts:             

                    conflicts.append(pair)

    total = reduce(lambda acc, _: acc + 1, conflicts, 0)  

    print(f"Found {total} conflicts")

    return conflicts
 