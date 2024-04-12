###########
# user variables
###########
############
from traincalc2 import calcTime

front = 1
cargo = 4
fluid = 0
rear = 0
time = calcTime(front=front,
                cargo=cargo,
                fluid=fluid,
                rear=rear,
                R=0.0075,
                fuelPower=1.8,
                fuelSpeed=1.15,
                clear=5)
if fluid == 0:
    print('{}-{}-{}'.format(front, cargo, rear))
elif cargo == 0:
    print('{}-{}f-{}'.format(front, fluid, rear))
else:
    print('{}-{}-{}f-{}'.format(front, cargo, fluid, rear))
if time == 0:
    print('train cannot acelerate')
else:
    print('\ttook {} ticks ({:.2f} seconds) to clear junction, for {:.3f}tpm or {:.2f}wpm'.format(time, time / 60,
                                                                                                  3600 / time,
                                                                                                  (3600 / time) * (
                                                                                                          cargo + fluid)))
    maxSpeed = min(A / B, 1.2 * fuelSpeed)
    print('\thas a maximim speed of {:.2f}tpt ({:.2f}km/h)'.format(maxSpeed, maxSpeed * 216))
