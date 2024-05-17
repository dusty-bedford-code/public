import pygame as pg
import time
clock=pg.time.Clock()

start_time = time.time_ns()

while(True):
    clock.tick(32)
    cur_time = time.time_ns()
    print(cur_time - start_time)
    start_time = cur_time