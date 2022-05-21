from cmath import inf
import time

# I think this is O(n^4)?
def generate_map(blocks: list, reqs: list):
    map = {}
    for i, block in enumerate(blocks):
        for req in reqs:
            if block[req] == True:
                if req in map:
                    map[req].append(i)
                else:
                    map[req] = [i]
    return map

def apartment_hunting(blocks: list, reqs: list) -> int:
    map = generate_map(blocks, reqs)
    # print(map)
    best = float(inf)
    best_address = None
    
    for i in range(len(blocks)):
        score = 0
        for req, addresses in map.items():
            closest = float(inf)
            for address in addresses:
                closest = min(closest, abs(address - i))
                # print(f"closest {req} from block {i} is now {closest}")
            score += closest
            # print(f"req {req} final closest score for block {i} is {closest}")
        # print(score)
        if score == 0: # if this is ever true it means we've found a block with all requirements on it
            return i
        if score < best:
            best = score
            best_address = i
    return best_address

def main():
    town = [{'school': True, 'gym': True, 'cafe': False},
            {'school': False, 'gym': False, 'cafe': False},
            {'school': False, 'gym': False, 'cafe': False},
            {'school': False, 'gym': False, 'cafe': False},
            {'school': False, 'gym': True, 'cafe': False},
            {'school': False, 'gym': False, 'cafe': False},
            {'school': False, 'gym': False, 'cafe': False},
            {'school': False, 'gym': False, 'cafe': False},
            {'school': False, 'gym': False, 'cafe': True}]
    
    requirements = ['gym', 'school', 'cafe']
    
    print(f"Best address is: {apartment_hunting(town, requirements)}")

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))