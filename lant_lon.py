#!/usr/bin/evn python3
# -*- encoding : utf-8 -*-

import math
EARTH_RADIUS = 6378137 #赤道半径(单位m)  
#转换为弧度（rad）
def rad(d):
    return d * math.pi / 180

'''
'''
def lantitudeLongitudeDist(lon1,lat1,lon2,lat2):
    radLon1 = rad(lon1)
    radLon2 = rad(lon2)
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)

    if(radLat1 < 0):
        radLat1 = math.pi / 2 + math.fabs(radLat1) # south
    if(radLat1 > 0):
        radLat1 = math.pi /2 - math.fabs(radLat1) # north
    if(radLat2 < 0):
        radLat2 = math.pi / 2 + math.fabs(radLat2)  # south
    if(radLat2 > 0):
        radLat2 = math.pi /2 - math.fabs(radLat2) # north
    
    if(radLon1 < 0):
        radLon1 = math.pi / 2 - math.fabs(radLon1)  #west
    if(radLon2 < 0):
        radLon2 = math.pi / 2 - math.fabs(radLon2) #west
    
    x1 = EARTH_RADIUS * math.cos(radLon1) * math.sin(radLat1)
    y1 = EARTH_RADIUS * math.sin(radLon1) * math.sin(radLat1)
    z1 = EARTH_RADIUS * math.cos(radLat1)

    x2 = EARTH_RADIUS * math.cos(radLon2) * math.sin(radLat2)
    y2 = EARTH_RADIUS * math.sin(radLon2) * math.sin(radLat2)
    z2 = EARTH_RADIUS * math.cos(radLat2)

    d = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) + (z1-z2)*(z1-z2))

    theta = math.acos((EARTH_RADIUS*EARTH_RADIUS + EARTH_RADIUS*EARTH_RADIUS - d*d) / (2 * EARTH_RADIUS * EARTH_RADIUS))

    dist = theta * EARTH_RADIUS

    return dist

if __name__ == "__main__":
    dist = lantitudeLongitudeDist(121.4078568,31.1684894,121.0888802,31.2924345)
    print(dist)