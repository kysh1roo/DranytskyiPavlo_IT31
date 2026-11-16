import math
import sys

NAME = "Pavlo Dranytskyi"
GROUP = "IT-31"

LENGTH, WIDTH, HEIGHT = 5.0, 3.0, 2.5
DOOR_W, DOOR_H = 0.9, 2.0
WINDOW_W, WINDOW_H = 1.0, 1.0
TILE_W_CM, TILE_H_CM = 70, 60
TILE_PRICE = 42.30

SPARE = 0.10            
PAINT_PER_M2 = 0.1      
COATS = 2
CAN_VOLUME = 2.5        

def main():
    print(f"{NAME}, {GROUP}")

    floor_area = LENGTH * WIDTH
    walls_full = 2 * (LENGTH + WIDTH) * HEIGHT
    wall_area = walls_full - DOOR_W * DOOR_H - WINDOW_W * WINDOW_H
    if wall_area <= 0:
        print("error: wall area is not positive, check door and window sizes",
              file=sys.stderr)
        sys.exit(1)

    floor_diag = math.hypot(LENGTH, WIDTH)
    room_diag = math.dist((0, 0, 0), (LENGTH, WIDTH, HEIGHT))

    tile_area = (TILE_W_CM / 100) * (TILE_H_CM / 100)
    tiles_exact = floor_area / tile_area
    tiles_to_buy = math.ceil(tiles_exact * (1 + SPARE))

    paint_l = wall_area * PAINT_PER_M2 * COATS
    cans = math.ceil(paint_l / CAN_VOLUME)

    cost_mul = tiles_to_buy * TILE_PRICE
    cost_sum = 0.0
    for _ in range(tiles_to_buy):
        cost_sum += TILE_PRICE

    print(f"room:          {LENGTH} x {WIDTH} x {HEIGHT} m")
    print(f"floor area:    {floor_area:.2f} m2")
    print(f"wall area:     {wall_area:.2f} m2 (without door and window)")
    print(f"floor diag:    {floor_diag:.2f} m")
    print(f"room diag:     {room_diag:.2f} m")
    print()
    print(f"tiles exact:   {tiles_exact:.2f}")
    print(f"  round:       {round(tiles_exact)}")
    print(f"  floor:       {math.floor(tiles_exact)}")
    print(f"  ceil:        {math.ceil(tiles_exact)}")
    print(f"tiles to buy:  {tiles_to_buy} (+{SPARE:.0%} spare)")
    print(f"paint:         {paint_l:.2f} l -> {cans} cans of {CAN_VOLUME} l")
    print()
    print(f"tiles cost:    {cost_mul:.2f} UAH")
    print(f"sum == mul:    {cost_sum == cost_mul}")
    print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
    print(f"difference:    {abs(cost_sum - cost_mul)}")


if __name__ == "__main__":
    main()
