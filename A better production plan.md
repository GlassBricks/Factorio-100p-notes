# Motivation
All our guts are telling us the current meta production order is far from optimal.
The target time should be... as low as possible.

Here are some questions to answer:
- Is it worth it to build the GC mall (or some mall of that scale) first before science? This requires a bigger science, but maybe it works out.
- How big of a mall before/after science? 
- We likely want asm3s, beacons, and prod3s, early. Should purple be done early?
- How big or expensive should GC outposts be, therefore dictating the mall size? 
	- How much mining? How many speed modules? 
	- Prod 1s, 2s, or 3s? 
	- How many bots?
	- See also [[Possible new strats#Late game]]
- How big is the base actually gonna be? See [[Possible new strats#Outposts that connect to main base]]
# How much modulage?
### Earlier modules?
In the old meta, modules are also produced kinda slowly and take a while to actually exist, so you don't get their benefits for quite a while.

It's probably worth it to make more modules early, so they actually become useful earlier. The close we hug to the exponential curve the more this becomes relavent.

### More modules everywhere?
Prod modules generate free resources! However, its not always used, as its theoretically better to put resources instead to more mining and smelting. 
However, if player outposting rate starts becoming a bottleneck (we value miners a lot more), then modules start becoming worth it everywhere:
- In more recipes
- Speed modules in outposts??

By the time we get to GC outposts, it definitely becomes worth it to use more modules. Is it worth it to do it earlier?

When/where is it worth it to put more modules everywhere?

 https://github.com/GlassBricks/factorio-recipe-analysis

# Some TODOs for analysis
https://github.com/GlassBricks/factorio-recipe-analysis
- [ ] See at what point modules in other places becomes worth it.
	- Taking into account bot times and space costs
	- Including beacons and asm3s and stuff
	- Somehow including internal buffer/startup times?
- [ ] Get a rough estimate of cost to build different sizes of mall, using realistic strats
	- Malls for everything, with varying amounts of tech available (e.g. assembler 3s) and module usage
	- The various sciences, at varying tech levels and module usage
	- Startup times
- Use the above to estimate/compare alternative production plans


# Some data
This will be useful in comparing production strategies.

Estimated optimistic patch connection time, using 2-way rails.
Based on experiment in [[old stuff/Patch connection times|Patch connection times]].
- 1:30 -- 2:00 per outpost, no legs
- 1:00 -- 1:30 per outpost, 3 legs

This is quite fast, hence the focus on massive scaling and optimizing bots a ton.
If the above numbers can be made a reality depends on a lot of factors.