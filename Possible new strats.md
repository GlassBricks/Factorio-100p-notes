These are possible alternate strategies to 100% running and design. These still need to evaluated or tested.
# Opening
From joining map to on-patch

## (much) bigger on/near-patch
Idea: Get a good chunk of the mall close to the patch; saves on belt and walking distance.
Suggested by Ximoltus
### Pros:
- Cheaper, Faster; better early growth
- Possibly can chose a central location, reducing trip time to mall
### Cons
- Hard to find a good location, as on-patch uses a lot of space.
- Hard to know what should be produced
- Existing mall is already in good location for blue sci/bots; this limits removes resources
	- Earlier on-patch connection (bringing intermediates)?

# Early game
Building main base, until after starter patches

## More bot production (how much)?

### Pros
- can afford dumping bunch of bots at outposts
- player (maybe) doesn't need to to help bots as much
### Cons
- Roboport production also needs to scale up with bot production, else more bots becomes counterproductive due to charging queue issues.
	- Perhaps new mall designs can attempt to dynamically balance this?
- Early setup cost, but may be worth it.

## Super early train outpost(s)
Design base so train outpost can be up super early after bots (taking some products from starter mall).
### Pros
- Allows taking further patches as "starter" patches for mall
- Train delay might not be a problem (compared to an insane amount of belt delay)
### Cons
- Requires buffering up some (how many? bots).
	- Might be ok with insane amounts of belt production
- Requires lots of steel fast
	- If we do steel instead of red belt, this could be fine

# Mid game
Connecting tons of outposts

See also: [[2-way train system]]

## Absolutely monstrous mall FIRST
See also [[A better production plan]]

Scale up to a GC-outpost-scale-or-bigger mall FIRST. Get an insane number of production, bots, modules, etc. 
Delay purple/yellow science as much as possible, except for a few critical techs (Asm 3s, beacons, bot speed?)
Then, build a much, much larger science.
### Pros
- Mathematically, it should be better to build a big mall and huge science, rather than a huge science and same size mall.
- Absolutely _massive_ scaling, and maybe enables new expensive strats (that may or may not be worth it). Like prod modules in everything
- Maybe having more expensive, red-belty speed-moduley outposts can be worth it?
### Cons
- We're assuming that player time won't become a bottleneck soon without power armor
- Now you need bigger later science; fancy techs might get researched late(r)
	- Most of the important stuff only needs blue sci, though
- RIP UPS


## GC outposts/GC production first
See also [[A better production plan]]

Why science first? Build GCs first! Either in outposts, or in the base.
### Pros
- Early GC production is theoretically more valuable as they run for longer.
- With [[#2-way train system for (almost) everything]], you an also belt back the GCs to be used for something!
### Cons
- Is it really any better, especially early game with tight resources, than to just belt ore back to base and produce tons of GCs there?


## "Flexible" train outposts via connecting belt
Somewhat separate the mining from the train station, connected by belts the player build
And/or, design train station(s) that allow manually belting in "filler"/supplement lanes.
### Pros
- Especially good if going with strategy that allows patches to be any size (above train setup)
- Allows moving train station out of the way if it collides
- Allows still taking advantage of "small" patches without the full cost of a station
### Cons
- Now we need red belt or something again. Possibly in the outpost train as well
- It costs player time to do this. Is it worth it?

## Filler water for power plant

Design power plant to enable several "filler" pump lanes, to make up for pumps that didn't get placed.
### Pros
- Enables a ton more maps.
- We don't need a perfectly rectangular water portion anymore, or even a super big one.
### Cons
- Can be really, really, annoying to design. Especially with boiler pumps.

## Separate bot network for power
May tie into above idea (connecting by train)
### Pros
- Bots don't have to fly back and forth a ton between main base and power
- Resources can be belted to central location for power plant
- These combined can save a _ton_ of bot time
### Cons
- Separate bot network means either lots of bot queue issues, or lots of tiny stages, or excessive bot overproduction

# The base
Base design stuff (somewhat) independent of player actions
## Roboport leapfrogging
Build the base in a space-filling cu Ximoltus
​￼￼￼Pros:rve.
Deconstruct roboports in old stages, so you have extra in new stages.
Later stages may have an insane amount of roboports (that may need to be deconstructed again to make room for other stuff?u)
Space filling curve is better than straight line, to keep the mall somewhat central.
### Pros
- Allows roboports also scale up with bots, enabling a ton more bot time
	- This was previously not quite true as old roboports eventually get underutilized
### Cons
- Requires additional player actions.
- You still probably need _some_ connections to old parts of base. Puts burden on player to not deconstruct the wrong roboports.
## Put (almost) everything on a construction belt

Put almost the entire mall on a construction belt.

Possibly want this to be on red belts to minimize belt delay.
### Pros
- Having resources in a more central location can save an ton of bot time.
- Can adapt this to help with [[#Super early train outpost]] or [[Good strategies#Super early restock train]]
### Cons
- Will add additional belt delay. is it worth putting really expensive stuff on the belt?

## Dynamically balanced mall

Actually calculate how much resources you need for each stage.
Use circuit magic feedback to let all resources to control production amounts. Production possibly can be readjusted between stages, to produced as close to the edge of optimal as possible.

This can be done for later sciences and modules and stuff as well.
### Pros
- Hug the exponential growth curve super tightly
- Never have 3500 red belt and 0 tanks ever again. Or a useless purple sciece
- If designed correctly (e.g. constant combinator input), mall can adapt to base as it evolves.
- If we happen to be behind on some material (e.g. assembler placed late), mall can channel extra resources to that thing to catch up.
- No need for player to reassign any assemblers to anything
### Cons
- It is feasible and worth it to make such a system? (probably yes)
- May need to be more costly (belt, space) to do effectively
- Using a construction belt may complicate things

## Use Prod 2s before Prod 3s

Instead of upgrading directly from prod 1s to prod 3s, we could upgrade to prod 3s first
### Pros
- More production for free
- Prod 2s can get recycled later into prod 3s, so no production is really lost
### Cons
- More player actions, and possibly be finicky

# Late game
Basically just GC outposts

## Ascend into Factorio godhood
This is basically mmkay's ideas.
The player stops doing stuff, and you have a global bot network (or maybe better, a network of separate networks, being expanded in parallel), and they do everything (like connect rails, GC outposts, fight biters with artillery, etc).

### Pros
- True essence of Factorio
- Theoretically faster, **when parallelized**,  than anything the player can do by hand, even with tons of power armor
- Higher ceiling for exponential growth, can really push down the target time.
- Eventually reach theoretical maximum build rate of 10k entities per second.
### Cons
- Extreme infrastructure cost. Is it actually worth it in the end?
- Bots are slow, especially travelling long distance. This needs lots of parallelism to potentially be worth it.
- Lots of problems to solve (@mmkkkay)
2s first ()
## Don't rely on logistics bots _at all_
(except for end-game stuff like tanks and shields)
### Pros
- Can go outposting as soon as you please. Or even before rocket!
- Enables delaying rocket science
### Cons
- I sense sushi spaghetti in your near future.
	- Is this even a con?

## Outposts that connect to main base
If we end up realizing we ant a absolutely colossal base, then at some point it could be worth breaking parts of the base out to outposts (e.g. iron or copper)

This might also allow Warger's old strat of basic iron outposts first, to scale up production even more before getting to main GC outposts.
### Pros
- Allows for much larger maximum base size. Maybe we need it
	- Reduced train congestion
	- Base takes up smaller footprint
	- Better bot management, potentially
	- Possibly cheaper logistics costs (if can find spot with multiple nearby patches)
- We only (maybe) need it very late game, where there should be a ton of accumulated bots and roboports and stuff. So the costs of doing so are manageable.
### Cons
- Based on Warger's old strat, very tricky to get right.
- May take a bunch of player time to set up
- Is it really worth it over just connecting everything to the base still?

## Allow GC outpost skeleton to be partially built by outpost bots

Put a bunch of skeleton stuff in the outpost train.
Stage the skeleton so outpost bots build some stuff.
### Pros
- Avoids having to run around in a weird circle, orphaning bots
- Makes being low on roboports less urgent.
### Cons
- Slightly longer startup time
- Bots need to finish skeleton first; more finicky for when to stamp the next stage
	- MORE ALARMS

## Connect GC outpost iron by train

This can be done probably via a p2p connection.
Another idea is to somehow connect it with the main rail network in a way that doesn't have trains running away to other outposts.

Signals can be pre-blueprinted to deal with crossing the outpost train rail.
### Pros
- Possibly saves time per outpost; just ghost rails. connecting iron to outposts is the longest part of setting up an outpost
### Cons
- Possibly more costly/bulky.
- Requires player to also start a train.
- Rail crossings may be annoying.

## Bypass lane in each outpost, multiple build trains.
Put a stacker/bypass lane in every outpost, still allowing single-rail connections.
Use multiple build trains, each carrying different stuff
(e.g. modules last, like Warger once did).

The coordination of trains can be completely automated.
### Pros
- Enables the outpost to get started building even when not all (expensive) resources are ready.
- Allows restock train to go whenever.
- If putting modules as the last train, doesn't contribute to bot queue issues at all (modules in separate bot queue)
### Cons
- More space required for stacker.
- May need even more multi-stage outposts to use effectively

