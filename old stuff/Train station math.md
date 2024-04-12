

Let $C$ be train cycle time: time to got to outpost and back.
Let $T$ be the time from outpost to base, or vice versa. T determines how far the outpost can be

Let `$W$` be wagon capacity (of all wagons).
Let $r_u$ be the unload rate, and $t_u$ be the unload time. `$t_u=W/r_u$`
Let $n$ be total number of trains.

# no/little train traffic

`$1/2C=T+t_u+k$`
where $k$ is some constant accounting for time to "get up to speed" and train traffic. $k$ is roughly constant probably, with little train traffic.

Solving for T (max travel time, roughly linear to outpost distance):
see [[train station math.ipynb]]
```am
T = W( n/(2r) - 1/u_r ) - k
```

Observations:
- Increasing wagon capacity (e.g. on site smelting) almost directly increases max distance.
- Making unloading faster has quickly diminishing returns (the 1/u_r term).

# 3 trains, shared 2-way rail

Throughput wise, this is functionally equivalent to 1 train with 0 unload time:
```am
T = W/(2r) - k
```
However, the unload time must be faster than the time before the next train, which is 2T:
```am
t_u &< 2T

    &= W/r - 2k
    
r_u &= W/t_u 

    &> W/(W/r - 2k)
    
    &> 1/(1/r - 2k/W)
```
As 2k/W is small, this is only needs to be slightly greater than r.
Some example numbers:
```am
k = 8
W = 50*40
r = 30

```

# In practice

- for P2P trains, the max distance is about 900 tiles.
