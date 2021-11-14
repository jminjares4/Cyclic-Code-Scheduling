# Author: Jesus Minjares
#         Master of Science in Computer Engineering
# Cyclic code: The purpose of this code is to automate the
#              conditions for the cyclic code scheduling for RTOS

from math import gcd
## Documentation for a function
# @param e exectuion list 
# @param p period list
# @return utlization factor
def utlization_factor(e, p):
    cpu_factor = 0.0
    for i in range(len(e)):
        cpu_factor = cpu_factor + e[i]/p[i]
    return cpu_factor

## Documentation for a function
# @param period period list 
# @return phyper, the lcm common multiple of period
def phyper(period):
    lcm = period[0]
    for i in range(1,len(period)):
        lcm = lcm*period[i]//gcd(lcm, period[i])
    return lcm

## Documentation for a function
# @param e execution list
# @return minimum frame bound, f >= max(ei)
def C1(e):
    return max(e)

## Documentation for a function
# @param phyper lcm(pi)
# @param frame  f >= max(ei)
# @return frame list
def C2(phyper, frame):
    frame_list = []
    current_frame = frame
    while current_frame <= phyper:
        if (phyper // current_frame) - (phyper / current_frame) == 0:
                frame_list.append(current_frame ) # add to the list
        current_frame = current_frame + 1
    return frame_list

## Documentation for a function
# @param period     task period
# @param frames     frame list 
# @param deadline   task deadline
# @return frame list          
def C3(period, frames, deadline):
    count  = 0
    frame_size  = 0
    for i in range(len(frames)):
        for j in range(len(period)):
            if 2 * frames[i] - gcd(period[j], frames[i]) <= deadline[j]:
                count = count + 1
            else:
                break
        if count == len(period):
            frame_size = frames[i]
            break
    return frame_size

def print_cyclic_code(p,e,d):
    cpu = utlization_factor(e, p)
    p_hyper = phyper(p)
    c1 = C1(e)
    c2 = C2(p_hyper, c1)
    c3 = C3(p, c2,d)
    print(f'Utlization factor: {cpu}')
    print(f'Phyper: {p_hyper}', end='\n')
    print(f'C1: {c1}', end='\n')
    print(f'C2: {c2}', end='\n')
    print(f'C3: {c3}', end='\n')


