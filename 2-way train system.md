#mid-game 

This page is for listing ideas related to 2-way train system.

2-way rail outposts are simply cheaper, more flexible, and faster to setup than belts. They should be transitioned to _eventually_.
However, they do have some startup delay and initial cost. The question that remains is, when should you transition to fully trains?
# Why a 2-way train system rocks
- Cheaper than red belt most almost all the time
- Much faster to setup than belt
- Infinitely more flexible:
	- Patches can be anywhere on any side of base, not location dependent.
	- Everything can be done with outpost train
	- No need to ping-pong back and forth between base and patches again; can have any pathing
	- Allows uranium, stone/coal, maybe oil to work anywhere; these were previous pain points.
- Can take advantage of multiple sizes of patches, big and small, and have them add up and balance out
- There is still opportunity for base bots to build outposts (just not connected with belt).
- If you design the whole base around this strategy, allows for even more niceties
	- No worry of balancing cost of red belt vs steel for trains

# Some notes

We definitely want more than 1 outpost train if doing this strat. Need room for train parking.
# Issues to tackle
## Possibly longer startup time
This needs to be quantified first via test; bots also need to fly, so maybe the startup time isn't as bad.

Also, the train needs to fill, taking stuff away from bots, before train leaves.

Multiple or stages with tons of alarms can mitigate this. This would require multiple train trips.
The choices for this are:
- Use the same build train, delivering half/a fraction the materials
- Different trains deliver different materials, and one blueprint stage activates another train stop calling the other.
- Use the same build train, and use circuitry at the outpost to take a variable amount of resources out. Keep calling the train as needed.
	- This is essentially rain's train strategy
	- This enables easier building of outposts of varying size.
	- However, this does mean more stuff needs to buffer unused inside the train.
	- Todo: expand this item to its own notes.
## More bulky outposts

A station is kinda big, taking up space. Gathering patches next to each other becomes more difficult.
We want to avoid 2-headed train, as its both more costly and less efficient.
Possible ideas:
- Design several outposts with stations in multiple configurations. A bit difficult, especially with multiple outpost sizes.
- See: [[possible new ideas/Readme#"Flexible" train outposts by connecting belt]]
## Maybe lost opportunity with close outposts

If an outpost is super close (there's usually 1 or 2... out of a lot), belt and base bots are cheaper and faster.
Maybe the base can be designed to still allow this option (but not be the main goal).
This does mean some red belt production (not as much)... the overflow of which goes into more steel, ig.
## Getting trains to balance 
Without p2p connections, getting trains to go where you want becomes a challenge.
I still believe this is mostly possible with circuitry control logic magic. The general idea is: request trains to base stations if balanced, request trains at outposts only there's enough ore. Try to emulate LTS. 

If you want to apply the strategy of varying sized outposts, balacing trains gets even more tricky.
Based on past efforts (TODO: put some of that here), likely one of the following concessions must be made to get it to work (compared to p2p):
- more trains
- lots more redundant ore being buffered
	- Allows a higher margin of error for train control
- more inserters per wagon (Stack inserters, anyone)?
	- Increases the amount of time station can be empty and still function
- Insane combinator control theory distributed algorithm shenanigans
	- Which may be the best option here

# Train congestion/throughput

Test for how much throughput a single basic hand-built intersection can support, with various variables.
> Maybe a "buffered" intersection, built by bots, is feasible?

Existing tests with 2-way tracks, and simple circuitry for train balancing.

Base: train limit = 1 + (1 if another train already present, else 0)
Outpost: train limit = (4000+ore count)/8000, assuming ore perfectly balanced.

| Fuel/braking force            | Train wagon size | throughput per wagon (yellow belts) | load rate per wagon | unload rate per wagon | Result (max # of outposts) | Result (throughput in yellow belts) |
| ----------------------------- | ---------------- | ----------------------------------- | ------------------- | --------------------- | -------------------------- | ----------------------------------- |
| solid fuel, no braking forece | 4                | 2                                   | 8 fast inserters    | 10 fast inserters     | 12                         | 24                                  |
| rocket fuel, braking force 2  | 4                | 2                                   | 8 fast inserters    | 10 fast inserters     | 15                         | 30                                  |

## Todo
- Share testing setup
- Test if braking force really makes a difference
- Test with outposts with varying mining rates (variable size outposts)
- Test with 5, maybe 6 wagons?
- Try various other train balancing control mechanisms. See [[#Getting trains to balance]]