def calcTime(
        front=1,
        cargo=4,
        fluid=0,
        rear=0,
        R=0.0075,
        fuelPower=1.8,
        fuelSpeed=1.15,
        clear=5,
):
    P = front * 600 * fuelPower
    F = 0.5 * (front + cargo + fluid + rear)
    W = 1000 * (2 * front + cargo + 3 * fluid + 2 * rear)

    A = (P / 60 - F) / W
    B = (1000 * R) / W
    C = 7 * (front + cargo + fluid + rear) + clear

    if A <= 0:
        return 0
    D = 0.0
    V = 0.0
    t = 0
    while D < C:
        t = t + 1
        D = D + V
        V = A + (1 - B) * V
        if V > (1.2 * fuelSpeed):
            V = 1.2 * fuelSpeed
    t = t + 1  # ajustment due to signal delay
    return t
