def execute_Tr(a):
    """
    飞行机器人健康监测模块 (自动生成)
    :param a: 包含三个参数的列表 [altitude, speed, voltage_mv]
    :return: 触发的变异分支集合
    """
    health_score = 100
    triggered = set()
    altitude, speed, voltage_mv = int(a[0]), int(a[1]), int(a[2])

    # 修正变量范围
    altitude = max(altitude, 2)
    altitude = min(altitude, 10000)
    speed = max(speed, 2)
    speed = min(speed, 1000)
    voltage_mv = max(voltage_mv, 2)
    voltage_mv = min(voltage_mv, 100)

    # 原语句1
    # 变异规则 1 - CRP
    if (altitude <= voltage_mv + 279) != (altitude <= voltage_mv + 139):
        triggered.add(1)
    # 变异规则 2 - SVR
    if (altitude <= voltage_mv + 279) != (speed <= voltage_mv + 279):
        triggered.add(2)
    # 变异规则 3 - SRC
    if (altitude <= voltage_mv + 279) != (abs(altitude) <= voltage_mv + 279):
        t=1
    # 变异规则 4 - LCR
    if (altitude <= voltage_mv + 279) != (altitude <= -voltage_mv + 279):
        triggered.add(3)
    # 变异规则 5 - UOI
    if (altitude <= voltage_mv + 279) != (altitude <= -voltage_mv + 279):
        triggered.add(4)
    # 变异规则 6 - ROR
    if (altitude <= voltage_mv + 279) != (voltage_mv <= voltage_mv + 279):
        triggered.add(5)
    # 变异规则 7 - CSR
    if (altitude <= voltage_mv + 279) != (altitude <= voltage_mv + -279):
        triggered.add(6)
    # 变异规则 8 - RSR
    if (altitude <= voltage_mv + 279) != (not (altitude <= voltage_mv + 279)):
        triggered.add(7)
    # 变异规则 9 - CAR
    if (altitude <= voltage_mv + 279) != (altitude <= voltage_mv + 274):
        triggered.add(8)
    # 变异规则 10 - SAR
    if (altitude <= voltage_mv + 279) != (voltage_mv >= altitude + 279):
        triggered.add(9)
    # 原语句
    if altitude <= voltage_mv + 279:
        health_score += 11
    # 原语句2
    # 变异规则 11 - SAR
    if (voltage_mv <= 100 or speed > 20) != (voltage_mv <= 100 or 20 < speed):
        t=1
    # 变异规则 12 - LCR
    if (voltage_mv <= 100 or speed > 20) != (voltage_mv <= 100 and speed > 20):
        triggered.add(10)
    # 变异规则 13 - ABS
    if (voltage_mv <= 100 or speed > 20) != (voltage_mv <= 100 or abs(speed) > 20):
        t=1
    # 变异规则 14 - AOR
    if (voltage_mv <= 100 or speed > 20) != (voltage_mv <= 100 or -speed > 20):
        t=1
    # 变异规则 15 - UOI
    if (voltage_mv <= 100 or speed > 20) != (voltage_mv <= 100 or -speed > 20):
        t=1
    # 变异规则 16 - RSR
    if (voltage_mv <= 100 or speed > 20) != (not (voltage_mv <= 100 or speed > 20)):
        triggered.add(11)
    # 变异规则 17 - SCR
    if (voltage_mv <= 100 or speed > 20) != (speed > 20 or voltage_mv <= 100):
        t=1
    # 变异规则 18 - CAR
    if (voltage_mv <= 100 or speed > 20) != (voltage_mv <= 102 or speed > 20):
        t=1
    # 变异规则 19 - SVR
    if (voltage_mv <= 100 or speed > 20) != (speed <= 100 or speed > 20):
        t=1
    # 变异规则 20 - CRP
    if (voltage_mv <= 100 or speed > 20) != (voltage_mv <= 200 or speed > 20):
        t=1
    # 原语句
    if voltage_mv <= 100 or speed > 20:
        health_score -= 30
        altitude = max(altitude - 13, 2)
        speed, voltage_mv = voltage_mv, speed
    # 原语句3
    # 变异规则 21 - ROR
    if (voltage_mv * altitude < 10) != (voltage_mv * -altitude < 10):
        triggered.add(12)
    # 变异规则 22 - AOR
    if (voltage_mv * altitude < 10) != (voltage_mv * abs(altitude) < 10):
        t=1
    # 变异规则 23 - SCR
    if (voltage_mv * altitude < 10) != (voltage_mv * -altitude < 10):
        triggered.add(13)
    # 变异规则 24 - CSR
    if (voltage_mv * altitude < 10) != (voltage_mv * altitude < -10):
        triggered.add(14)
    # 变异规则 25 - ABS
    if (voltage_mv * altitude < 10) != (voltage_mv * abs(altitude) < 10):
        t=1
    # 变异规则 26 - SRC
    if (voltage_mv * altitude < 10) != (not (voltage_mv * altitude < 10)):
        triggered.add(15)
    # 变异规则 27 - CRP
    if (voltage_mv * altitude < 10) != (voltage_mv * altitude < 5):
        triggered.add(16)
    # 变异规则 28 - CAR
    if (voltage_mv * altitude < 10) != (voltage_mv * altitude < 15):
        triggered.add(17)
    # 变异规则 29 - UOI
    if (voltage_mv * altitude < 10) != (voltage_mv * -altitude < 10):
        triggered.add(18)
    # 变异规则 30 - SVR
    if (voltage_mv * altitude < 10) != (speed * altitude < 10):
        triggered.add(19)
    # 原语句
    if voltage_mv * altitude < 10:
        health_score -= 17
        altitude = min(altitude + 67, 1000)
    # 原语句4
    # 变异规则 31 - UOI
    if (altitude > 613) != (613 < altitude):
        t=1
    # 变异规则 32 - LCR
    if (altitude > 613) != (altitude > -613):
        triggered.add(20)
    # 变异规则 33 - ROR
    if (altitude > 613) != (altitude > 619):
        triggered.add(21)
    # 变异规则 34 - SCR
    if (altitude > 613) != (altitude > -613):
        triggered.add(22)
    # 变异规则 35 - CAR
    if (altitude > 613) != (altitude > 608):
        triggered.add(23)
    # 变异规则 36 - AOR
    if (altitude > 613) != (abs(altitude) > 613):
        t=1
    # 变异规则 37 - CRP
    if (altitude > 613) != (altitude > 1226):
        triggered.add(24)
    # 变异规则 38 - SRC
    if (altitude > 613) != (613 < altitude):
        t=1
    # 变异规则 39 - CSR
    if (altitude > 613) != (altitude > -613):
        triggered.add(25)
    # 变异规则 40 - ABS
    if (altitude > 613) != (abs(altitude) > 613):
        t=1
    # 原语句
    if altitude > 613:
        health_score -= 14
        speed = min(speed + 4, 100)
    # 原语句5
    # 变异规则 41 - ABS
    if (altitude > 100 or voltage_mv > 30) != (abs(altitude) > 100 or voltage_mv > 30):
        t=1
    # 变异规则 42 - SAR
    if (altitude > 100 or voltage_mv > 30) != (100 < altitude or voltage_mv > 30):
        t=1
    # 变异规则 43 - LCR
    if (altitude > 100 or voltage_mv > 30) != (altitude > 100 and voltage_mv > 30):
        triggered.add(26)
    # 变异规则 44 - UOI
    if (altitude > 100 or voltage_mv > 30) != (altitude > 100 or -voltage_mv > 30):
        triggered.add(27)
    # 变异规则 45 - ROR
    if (altitude > 100 or voltage_mv > 30) != (voltage_mv > 30 or altitude > 100):
        t=1
    # 变异规则 46 - CSR
    if (altitude > 100 or voltage_mv > 30) != (altitude > 100 or voltage_mv > -30):
        triggered.add(28)
    # 变异规则 47 - AOR
    if (altitude > 100 or voltage_mv > 30) != (100 < altitude or voltage_mv > 30):
        t=1
    # 变异规则 48 - CRP
    if (altitude > 100 or voltage_mv > 30) != (altitude > 100 or voltage_mv > 39):
        triggered.add(29)
    # 变异规则 49 - SVR
    if (altitude > 100 or voltage_mv > 30) != (speed > 100 or voltage_mv > 30):
        triggered.add(30)
    # 变异规则 50 - RSR
    if (altitude > 100 or voltage_mv > 30) != (not (altitude > 100 or voltage_mv > 30)):
        triggered.add(31)
    # 原语句
    if altitude > 100 or voltage_mv > 30:
        health_score -= 24
    # 原语句6
    # 变异规则 51 - ABS
    if (altitude - speed == 500) != (abs(altitude) - speed == 500):
        t=1
    # 变异规则 52 - SVR
    if (altitude - speed == 500) != (speed - speed == 500):
        triggered.add(32)
    # 变异规则 53 - SAR
    if (altitude - speed == 500) != (altitude - 500 == speed):
        t=1
    # 变异规则 54 - CRP
    if (altitude - speed == 500) != (altitude - speed == 496):
        triggered.add(33)
    # 变异规则 55 - LCR
    if (altitude - speed == 500) != (altitude - 500 == speed):
        t=1
    # 变异规则 56 - CAR
    if (altitude - speed == 500) != (altitude - speed == 502):
        triggered.add(34)
    # 变异规则 57 - SCR
    if (altitude - speed == 500) != (not (altitude - speed == 500)):
        triggered.add(35)
    # 变异规则 58 - UOI
    if (altitude - speed == 500) != (altitude - 500 == speed):
        t=1
    # 变异规则 59 - RSR
    if (altitude - speed == 500) != (not (altitude - speed == 500)):
        triggered.add(36)
    # 变异规则 60 - ROR
    if (altitude - speed == 500) != (altitude - speed == 250):
        triggered.add(37)
    # 原语句
    if altitude - speed == 500:
        health_score -= 10
        altitude = min(altitude + 60, 1000)
        speed = max(speed - 3, 2)
        voltage_mv = min(voltage_mv + 1, 100)
    # 原语句7
    # 变异规则 61 - SCR
    if (speed <= 30 or altitude < 200) != (speed <= 15 or altitude < 200):
        triggered.add(38)
    # 变异规则 62 - SAR
    if (speed <= 30 or altitude < 200) != (speed <= 30 or 200 > altitude):
        t=1
    # 变异规则 63 - AOR
    if (speed <= 30 or altitude < 200) != (not (speed <= 30 or altitude < 200)):
        triggered.add(39)
    # 变异规则 64 - UOI
    if (speed <= 30 or altitude < 200) != (speed <= 30 or -altitude < 200):
        triggered.add(40)
    # 变异规则 65 - CRP
    if (speed <= 30 or altitude < 200) != (speed <= 20 or altitude < 200):
        triggered.add(41)
    # 变异规则 66 - ROR
    if (speed <= 30 or altitude < 200) != (speed <= 30 or abs(altitude) < 200):
        t=1
    # 变异规则 67 - CSR
    if (speed <= 30 or altitude < 200) != (speed <= -30 or altitude < 200):
        triggered.add(42)
    # 变异规则 68 - LCR
    if (speed <= 30 or altitude < 200) != (speed <= 30 and altitude < 200):
        triggered.add(43)
    # 变异规则 69 - CAR
    if (speed <= 30 or altitude < 200) != (speed <= 25 or altitude < 200):
        triggered.add(44)
    # 变异规则 70 - ABS
    if (speed <= 30 or altitude < 200) != (speed <= 30 or abs(altitude) < 200):
        t=1
    # 原语句
    if speed <= 30 or altitude < 200:
        health_score += 6
    # 原语句8
    # 变异规则 71 - SVR
    if (altitude // voltage_mv < 100) != (voltage_mv // voltage_mv < 100):
        triggered.add(45)
    # 变异规则 72 - CAR
    if (altitude // voltage_mv < 100) != (altitude // voltage_mv < 102):
        triggered.add(46)
    # 变异规则 73 - RSR
    if (altitude // voltage_mv < 100) != (not (altitude // voltage_mv < 100)):
        triggered.add(47)
    # 变异规则 74 - ABS
    if (altitude // voltage_mv < 100) != (abs(altitude) // voltage_mv < 100):
        t=1
    # 变异规则 75 - SRC
    if (altitude // voltage_mv < 100) != (altitude // voltage_mv < 99):
        triggered.add(48)
    # 变异规则 76 - SCR
    if (altitude // voltage_mv < 100) != (altitude // voltage_mv < -100):
        triggered.add(49)
    # 变异规则 77 - LCR
    if (altitude // voltage_mv < 100) != (abs(altitude) // voltage_mv < 100):
        t=1
    # 变异规则 78 - CSR
    if (altitude // voltage_mv < 100) != (altitude // voltage_mv < -100):
        triggered.add(50)
    # 变异规则 79 - SAR
    if (altitude // voltage_mv < 100) != (altitude // 100 > voltage_mv):
        triggered.add(51)
    # 变异规则 80 - UOI
    if (altitude // voltage_mv < 100) != (altitude // -voltage_mv < 100):
        triggered.add(52)
    # 原语句
    if altitude // voltage_mv < 100:
        health_score -= 14
    # 原语句9
    # 变异规则 81 - CSR
    if (5 <= voltage_mv <= 62) != (5 <= voltage_mv <= -62):
        triggered.add(53)
    # 变异规则 82 - CAR
    if (5 <= voltage_mv <= 62) != (7 <= voltage_mv <= 62):
        triggered.add(54)
    # 变异规则 83 - RSR
    if (5 <= voltage_mv <= 62) != (not (5 <= voltage_mv <= 62)):
        triggered.add(55)
    # 变异规则 84 - AOR
    if (5 <= voltage_mv <= 62) != (5 <= -voltage_mv <= 62):
        triggered.add(56)
    # 变异规则 85 - SCR
    if (5 <= voltage_mv <= 62) != (voltage_mv >= 5 <= 62):
        triggered.add(57)
    # 变异规则 86 - UOI
    if (5 <= voltage_mv <= 62) != (5 <= -voltage_mv <= 62):
        triggered.add(58)
    # 变异规则 87 - SVR
    if (5 <= voltage_mv <= 62) != (5 <= altitude <= 62):
        triggered.add(59)
    # 变异规则 88 - LCR
    if (5 <= voltage_mv <= 62) != (5 <= voltage_mv <= 57):
        triggered.add(60)
    # 变异规则 89 - SRC
    if (5 <= voltage_mv <= 62) != (5 <= voltage_mv <= -62):
        triggered.add(61)
    # 变异规则 90 - ROR
    if (5 <= voltage_mv <= 62) != (-5 <= voltage_mv <= 62):
        triggered.add(62)
    # 原语句
    if 5 <= voltage_mv <= 62:
        health_score -= 10
    # 原语句10
    # 变异规则 91 - UOI
    if (speed >= 5) != (speed >= 7):
        triggered.add(63)
    # 变异规则 92 - SCR
    if (speed >= 5) != (speed >= 15):
        triggered.add(64)
    # 变异规则 93 - ABS
    if (speed >= 5) != (abs(speed) >= 5):
        t=1
    # 变异规则 94 - CSR
    if (speed >= 5) != (speed >= -5):
        triggered.add(65)
    # 变异规则 95 - LCR
    if (speed >= 5) != (speed >= -5):
        triggered.add(66)
    # 变异规则 96 - SAR
    if (speed >= 5) != (5 <= speed):
        t=1
    # 变异规则 97 - AOR
    if (speed >= 5) != (speed >= 10):
        triggered.add(67)
    # 变异规则 98 - CAR
    if (speed >= 5) != (speed >= 1):
        triggered.add(68)
    # 变异规则 99 - RSR
    if (speed >= 5) != (not (speed >= 5)):
        triggered.add(69)
    # 变异规则 100 - SRC
    if (speed >= 5) != (5 <= speed):
        t=1
    # 原语句
    if speed >= 5:
        health_score -= 1
        speed = min(speed + 2, 100)
        voltage_mv = min(voltage_mv + 9, 100)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句11
    # 变异规则 101 - SAR
    if (236 <= altitude <= 722) != (altitude >= 236 <= 722):
        t=1
    # 变异规则 102 - RSR
    if (236 <= altitude <= 722) != (not (236 <= altitude <= 722)):
        triggered.add(70)
    # 变异规则 103 - AOR
    if (236 <= altitude <= 722) != (not (236 <= altitude <= 722)):
        triggered.add(71)
    # 变异规则 104 - CRP
    if (236 <= altitude <= 722) != (236 <= altitude <= 712):
        t=1
    # 变异规则 105 - CSR
    if (236 <= altitude <= 722) != (-236 <= altitude <= 722):
        triggered.add(72)
    # 变异规则 106 - SVR
    if (236 <= altitude <= 722) != (236 <= speed <= 722):
        triggered.add(73)
    # 变异规则 107 - UOI
    if (236 <= altitude <= 722) != (236 <= -altitude <= 722):
        triggered.add(74)
    # 变异规则 108 - ABS
    if (236 <= altitude <= 722) != (236 <= abs(altitude) <= 722):
        t=1
    # 变异规则 109 - SRC
    if (236 <= altitude <= 722) != (altitude >= 236 <= 722):
        t=1
    # 变异规则 110 - LCR
    if (236 <= altitude <= 722) != (236 <= abs(altitude) <= 722):
        t=1
    # 原语句
    if 236 <= altitude <= 722:
        health_score += 17
    # 原语句12
    # 变异规则 111 - UOI
    if (altitude <= 50) != (abs(altitude) <= 50):
        t=1
    # 变异规则 112 - SRC
    if (altitude <= 50) != (voltage_mv <= 50):
        triggered.add(75)
    # 变异规则 113 - ROR
    if (altitude <= 50) != (not (altitude <= 50)):
        triggered.add(76)
    # 变异规则 114 - SVR
    if (altitude <= 50) != (voltage_mv <= 50):
        triggered.add(77)
    # 变异规则 115 - CRP
    if (altitude <= 50) != (altitude <= 51):
        triggered.add(78)
    # 变异规则 116 - CSR
    if (altitude <= 50) != (altitude <= -50):
        triggered.add(79)
    # 变异规则 117 - ABS
    if (altitude <= 50) != (abs(altitude) <= 50):
        t=1
    # 变异规则 118 - LCR
    if (altitude <= 50) != (50 >= altitude):
        t=1
    # 变异规则 119 - SAR
    if (altitude <= 50) != (50 >= altitude):
        t=1
    # 变异规则 120 - SCR
    if (altitude <= 50) != (altitude <= 48):
        triggered.add(80)
    # 原语句
    if altitude <= 50:
        health_score += 7
        speed = min(speed + 8, 100)
        voltage_mv = max(voltage_mv - 7, 2)
    # 原语句13
    # 变异规则 121 - SVR
    if (speed != voltage_mv + 20) != (altitude != voltage_mv + 20):
        triggered.add(81)
    # 变异规则 122 - SAR
    if (speed != voltage_mv + 20) != (voltage_mv != speed + 20):
        triggered.add(82)
    # 变异规则 123 - ROR
    if (speed != voltage_mv + 20) != (voltage_mv != speed + 20):
        triggered.add(83)
    # 变异规则 124 - CAR
    if (speed != voltage_mv + 20) != (speed != voltage_mv + 21):
        triggered.add(84)
    # 变异规则 125 - SRC
    if (speed != voltage_mv + 20) != (abs(speed) != voltage_mv + 20):
        t=1
    # 变异规则 126 - RSR
    if (speed != voltage_mv + 20) != (not (speed != voltage_mv + 20)):
        triggered.add(85)
    # 变异规则 127 - CSR
    if (speed != voltage_mv + 20) != (speed != voltage_mv + -20):
        triggered.add(86)
    # 变异规则 128 - SCR
    if (speed != voltage_mv + 20) != (speed != voltage_mv + -20):
        triggered.add(87)
    # 变异规则 129 - CRP
    if (speed != voltage_mv + 20) != (speed != voltage_mv + 10):
        triggered.add(88)
    # 变异规则 130 - LCR
    if (speed != voltage_mv + 20) != (speed != voltage_mv + -20):
        triggered.add(89)
    # 原语句
    if speed != voltage_mv + 20:
        health_score -= 10
        altitude = min(altitude + 20, 1000)
        speed = min(speed + 10, 100)
        voltage_mv = max(voltage_mv - 6, 2)
    # 原语句14
    # 变异规则 131 - CRP
    if (3 <= voltage_mv <= 49) != (3 <= voltage_mv <= 47):
        triggered.add(90)
    # 变异规则 132 - AOR
    if (3 <= voltage_mv <= 49) != (-3 <= voltage_mv <= 49):
        triggered.add(91)
    # 变异规则 133 - SAR
    if (3 <= voltage_mv <= 49) != (voltage_mv >= 3 <= 49):
        triggered.add(92)
    # 变异规则 134 - CSR
    if (3 <= voltage_mv <= 49) != (3 <= voltage_mv <= -49):
        triggered.add(93)
    # 变异规则 135 - RSR
    if (3 <= voltage_mv <= 49) != (not (3 <= voltage_mv <= 49)):
        triggered.add(94)
    # 变异规则 136 - LCR
    if (3 <= voltage_mv <= 49) != (3 <= voltage_mv <= 47):
        triggered.add(95)
    # 变异规则 137 - SVR
    if (3 <= voltage_mv <= 49) != (3 <= altitude <= 49):
        triggered.add(96)
    # 变异规则 138 - CAR
    if (3 <= voltage_mv <= 49) != (3 <= voltage_mv <= 59):
        triggered.add(97)
    # 变异规则 139 - ROR
    if (3 <= voltage_mv <= 49) != (3 <= -voltage_mv <= 49):
        triggered.add(98)
    # 变异规则 140 - ABS
    if (3 <= voltage_mv <= 49) != (3 <= abs(voltage_mv) <= 49):
        t=1
    # 原语句
    if 3 <= voltage_mv <= 49:
        health_score -= 25
        altitude = max(altitude - 49, 2)
        speed = min(speed + 2, 100)
    # 原语句15
    # 变异规则 141 - SAR
    if (altitude > 10) != (10 < altitude):
        t=1
    # 变异规则 142 - SVR
    if (altitude > 10) != (speed > 10):
        triggered.add(99)
    # 变异规则 143 - AOR
    if (altitude > 10) != (voltage_mv > 10):
        triggered.add(100)
    # 变异规则 144 - ROR
    if (altitude > 10) != (altitude > -10):
        triggered.add(101)
    # 变异规则 145 - CAR
    if (altitude > 10) != (altitude > 5):
        triggered.add(102)
    # 变异规则 146 - CSR
    if (altitude > 10) != (altitude > -10):
        triggered.add(103)
    # 变异规则 147 - UOI
    if (altitude > 10) != (altitude > 5):
        triggered.add(104)
    # 变异规则 148 - ABS
    if (altitude > 10) != (abs(altitude) > 10):
        t=1
    # 变异规则 149 - SRC
    if (altitude > 10) != (altitude > 5):
        triggered.add(105)
    # 变异规则 150 - RSR
    if (altitude > 10) != (not (altitude > 10)):
        triggered.add(106)
    # 原语句
    if altitude > 10:
        health_score += 8
        voltage_mv, speed = speed, voltage_mv
    # 原语句16
    # 变异规则 151 - SVR
    if (altitude + 716 != voltage_mv) != (speed + 716 != voltage_mv):
        t=1
    # 变异规则 152 - SRC
    if (altitude + 716 != voltage_mv) != (not (altitude + 716 != voltage_mv)):
        triggered.add(107)
    # 变异规则 153 - CAR
    if (altitude + 716 != voltage_mv) != (altitude + 711 != voltage_mv):
        t=1
    # 变异规则 154 - ROR
    if (altitude + 716 != voltage_mv) != (voltage_mv + 716 != voltage_mv):
        t=1
    # 变异规则 155 - SAR
    if (altitude + 716 != voltage_mv) != (altitude + voltage_mv != 716):
        t=1
    # 变异规则 156 - CSR
    if (altitude + 716 != voltage_mv) != (altitude + -716 != voltage_mv):
        t=1
    # 变异规则 157 - ABS
    if (altitude + 716 != voltage_mv) != (abs(altitude) + 716 != voltage_mv):
        t=1
    # 变异规则 158 - SCR
    if (altitude + 716 != voltage_mv) != (altitude + -716 != voltage_mv):
        t=1
    # 变异规则 159 - RSR
    if (altitude + 716 != voltage_mv) != (not (altitude + 716 != voltage_mv)):
        triggered.add(108)
    # 变异规则 160 - AOR
    if (altitude + 716 != voltage_mv) != (altitude + 358 != voltage_mv):
        t=1
    # 原语句
    if altitude + 716 != voltage_mv:
        health_score += 5
        altitude = min(altitude + 76, 1000)
        voltage_mv = min(voltage_mv + 10, 100)
    # 原语句17
    # 变异规则 161 - UOI
    if (voltage_mv > 2) != (not (voltage_mv > 2)):
        triggered.add(109)
    # 变异规则 162 - AOR
    if (voltage_mv > 2) != (2 < voltage_mv):
        t=1
    # 变异规则 163 - CSR
    if (voltage_mv > 2) != (voltage_mv > -2):
        t=1
    # 变异规则 164 - CAR
    if (voltage_mv > 2) != (voltage_mv > 1):
        t=1
    # 变异规则 165 - SAR
    if (voltage_mv > 2) != (2 < voltage_mv):
        t=1
    # 变异规则 166 - SVR
    if (voltage_mv > 2) != (altitude > 2):
        t=1
    # 变异规则 167 - SRC
    if (voltage_mv > 2) != (voltage_mv > 8):
        t=1
    # 变异规则 168 - ROR
    if (voltage_mv > 2) != (2 < voltage_mv):
        t=1
    # 变异规则 169 - CRP
    if (voltage_mv > 2) != (voltage_mv > 8):
        t=1
    # 变异规则 170 - ABS
    if (voltage_mv > 2) != (abs(voltage_mv) > 2):
        t=1
    # 原语句
    if voltage_mv > 2:
        health_score -= 8
        voltage_mv = max(voltage_mv - 2, 2)
    # 原语句18
    # 变异规则 171 - SRC
    if (voltage_mv < 10) != (speed < 10):
        triggered.add(110)
    # 变异规则 172 - RSR
    if (voltage_mv < 10) != (not (voltage_mv < 10)):
        triggered.add(111)
    # 变异规则 173 - LCR
    if (voltage_mv < 10) != (altitude < 10):
        t=1
    # 变异规则 174 - CRP
    if (voltage_mv < 10) != (voltage_mv < 12):
        triggered.add(112)
    # 变异规则 175 - SCR
    if (voltage_mv < 10) != (abs(voltage_mv) < 10):
        t=1
    # 变异规则 176 - ROR
    if (voltage_mv < 10) != (altitude < 10):
        t=1
    # 变异规则 177 - SAR
    if (voltage_mv < 10) != (10 > voltage_mv):
        t=1
    # 变异规则 178 - UOI
    if (voltage_mv < 10) != (voltage_mv < 20):
        triggered.add(113)
    # 变异规则 179 - CAR
    if (voltage_mv < 10) != (voltage_mv < 8):
        t=1
    # 变异规则 180 - CSR
    if (voltage_mv < 10) != (voltage_mv < -10):
        t=1
    # 原语句
    if voltage_mv < 10:
        health_score -= 5
    # 原语句19
    # 变异规则 181 - LCR
    if (speed < 100) != (speed < 200):
        triggered.add(114)
    # 变异规则 182 - ABS
    if (speed < 100) != (abs(speed) < 100):
        t=1
    # 变异规则 183 - ROR
    if (speed < 100) != (abs(speed) < 100):
        t=1
    # 变异规则 184 - SCR
    if (speed < 100) != (not (speed < 100)):
        triggered.add(115)
    # 变异规则 185 - AOR
    if (speed < 100) != (not (speed < 100)):
        triggered.add(116)
    # 变异规则 186 - SRC
    if (speed < 100) != (100 > speed):
        t=1
    # 变异规则 187 - CAR
    if (speed < 100) != (speed < 98):
        triggered.add(117)
    # 变异规则 188 - UOI
    if (speed < 100) != (speed < 102):
        triggered.add(118)
    # 变异规则 189 - SVR
    if (speed < 100) != (altitude < 100):
        triggered.add(119)
    # 变异规则 190 - RSR
    if (speed < 100) != (not (speed < 100)):
        triggered.add(120)
    # 原语句
    if speed < 100:
        health_score += 5
        speed, voltage_mv = voltage_mv, speed
    # 原语句20
    # 变异规则 191 - CAR
    if (voltage_mv // 20 == speed) != (voltage_mv // 30 == speed):
        t=1
    # 变异规则 192 - SRC
    if (voltage_mv // 20 == speed) != (voltage_mv // 17 == speed):
        t=1
    # 变异规则 193 - ABS
    if (voltage_mv // 20 == speed) != (voltage_mv // 20 == abs(speed)):
        t=1
    # 变异规则 194 - AOR
    if (voltage_mv // 20 == speed) != (voltage_mv // 20 == -speed):
        t=1
    # 变异规则 195 - CRP
    if (voltage_mv // 20 == speed) != (voltage_mv // 10 == speed):
        t=1
    # 变异规则 196 - LCR
    if (voltage_mv // 20 == speed) != (voltage_mv // 40 == speed):
        t=1
    # 变异规则 197 - ROR
    if (voltage_mv // 20 == speed) != (voltage_mv // 20 == -speed):
        t=1
    # 变异规则 198 - SVR
    if (voltage_mv // 20 == speed) != (altitude // 20 == speed):
        triggered.add(121)
    # 变异规则 199 - SAR
    if (voltage_mv // 20 == speed) != (voltage_mv // speed == 20):
        t=1
    # 变异规则 200 - RSR
    if (voltage_mv // 20 == speed) != (not (voltage_mv // 20 == speed)):
        triggered.add(122)
    # 原语句
    if voltage_mv // 20 == speed:
        health_score -= 22
        speed = min(speed + 8, 100)
    # 原语句21
    # 变异规则 201 - RSR
    if (26 <= speed <= 91) != (not (26 <= speed <= 91)):
        triggered.add(123)
    # 变异规则 202 - CAR
    if (26 <= speed <= 91) != (26 <= speed <= 81):
        triggered.add(124)
    # 变异规则 203 - LCR
    if (26 <= speed <= 91) != (26 <= speed <= 93):
        triggered.add(125)
    # 变异规则 204 - ABS
    if (26 <= speed <= 91) != (26 <= abs(speed) <= 91):
        t=1
    # 变异规则 205 - CSR
    if (26 <= speed <= 91) != (-26 <= speed <= 91):
        triggered.add(126)
    # 变异规则 206 - AOR
    if (26 <= speed <= 91) != (26 <= -speed <= 91):
        triggered.add(127)
    # 变异规则 207 - UOI
    if (26 <= speed <= 91) != (26 <= -speed <= 91):
        triggered.add(128)
    # 变异规则 208 - SRC
    if (26 <= speed <= 91) != (26 <= abs(speed) <= 91):
        t=1
    # 变异规则 209 - ROR
    if (26 <= speed <= 91) != (34 <= speed <= 91):
        triggered.add(129)
    # 变异规则 210 - SCR
    if (26 <= speed <= 91) != (not (26) <= speed <= 91):
        triggered.add(130)
    # 原语句
    if 26 <= speed <= 91:
        speed = min(speed + 6, 100)
    # 原语句22
    # 变异规则 211 - ROR
    if (voltage_mv == 5 and altitude <= 50) != (altitude <= 50 and voltage_mv == 5):
        t=1
    # 变异规则 212 - CSR
    if (voltage_mv == 5 and altitude <= 50) != (voltage_mv == -5 and altitude <= 50):
        t=1
    # 变异规则 213 - SCR
    if (voltage_mv == 5 and altitude <= 50) != (speed == 5 and altitude <= 50):
        t=1
    # 变异规则 214 - CAR
    if (voltage_mv == 5 and altitude <= 50) != (voltage_mv == 4 and altitude <= 50):
        t=1
    # 变异规则 215 - ABS
    if (voltage_mv == 5 and altitude <= 50) != (voltage_mv == 5 and abs(altitude) <= 50):
        t=1
    # 变异规则 216 - AOR
    if (voltage_mv == 5 and altitude <= 50) != (voltage_mv == 3 and altitude <= 50):
        t=1
    # 变异规则 217 - SVR
    if (voltage_mv == 5 and altitude <= 50) != (speed == 5 and altitude <= 50):
        t=1
    # 变异规则 218 - CRP
    if (voltage_mv == 5 and altitude <= 50) != (voltage_mv == 5 and altitude <= 100):
        triggered.add(131)
    # 变异规则 219 - SRC
    if (voltage_mv == 5 and altitude <= 50) != (altitude <= 50 and voltage_mv == 5):
        t=1
    # 变异规则 220 - UOI
    if (voltage_mv == 5 and altitude <= 50) != (voltage_mv == 5 and -altitude <= 50):
        triggered.add(132)
    # 原语句
    if voltage_mv == 5 and altitude <= 50:
        health_score -= 17
    # 原语句23
    # 变异规则 221 - ROR
    if (speed <= 50) != (50 >= speed):
        t=1
    # 变异规则 222 - UOI
    if (speed <= 50) != (speed <= 45):
        triggered.add(133)
    # 变异规则 223 - CRP
    if (speed <= 50) != (speed <= 25):
        triggered.add(134)
    # 变异规则 224 - CAR
    if (speed <= 50) != (speed <= 60):
        triggered.add(135)
    # 变异规则 225 - SAR
    if (speed <= 50) != (50 >= speed):
        t=1
    # 变异规则 226 - CSR
    if (speed <= 50) != (speed <= -50):
        triggered.add(136)
    # 变异规则 227 - RSR
    if (speed <= 50) != (not (speed <= 50)):
        triggered.add(137)
    # 变异规则 228 - SCR
    if (speed <= 50) != (speed <= 49):
        triggered.add(138)
    # 变异规则 229 - SVR
    if (speed <= 50) != (voltage_mv <= 50):
        triggered.add(139)
    # 变异规则 230 - SRC
    if (speed <= 50) != (speed <= 25):
        triggered.add(140)
    # 原语句
    if speed <= 50:
        health_score += 14
        voltage_mv = max(voltage_mv - 10, 2)
    # 原语句24
    # 变异规则 231 - ABS
    if (speed == 54 or altitude != 135) != (speed == 54 or abs(altitude) != 135):
        t=1
    # 变异规则 232 - UOI
    if (speed == 54 or altitude != 135) != (speed == 54 or -altitude != 135):
        triggered.add(141)
    # 变异规则 233 - SVR
    if (speed == 54 or altitude != 135) != (voltage_mv == 54 or altitude != 135):
        triggered.add(142)
    # 变异规则 234 - LCR
    if (speed == 54 or altitude != 135) != (speed == 54 and altitude != 135):
        triggered.add(143)
    # 变异规则 235 - SAR
    if (speed == 54 or altitude != 135) != (54 == speed or altitude != 135):
        t=1
    # 变异规则 236 - CSR
    if (speed == 54 or altitude != 135) != (speed == 54 or altitude != -135):
        triggered.add(144)
    # 变异规则 237 - CRP
    if (speed == 54 or altitude != 135) != (speed == 54 or altitude != 141):
        triggered.add(145)
    # 变异规则 238 - AOR
    if (speed == 54 or altitude != 135) != (not (speed == 54 or altitude != 135)):
        triggered.add(146)
    # 变异规则 239 - SCR
    if (speed == 54 or altitude != 135) != (54 == speed or altitude != 135):
        t=1
    # 变异规则 240 - CAR
    if (speed == 54 or altitude != 135) != (speed == 54 or altitude != 134):
        triggered.add(147)
    # 原语句
    if speed == 54 or altitude != 135:
        health_score += 13
        altitude = min(altitude + 29, 1000)
        voltage_mv = max(voltage_mv - 1, 2)
    # 原语句25
    # 变异规则 241 - CRP
    if (voltage_mv != 5 and altitude != 500) != (voltage_mv != 10 and altitude != 500):
        triggered.add(148)
    # 变异规则 242 - ABS
    if (voltage_mv != 5 and altitude != 500) != (voltage_mv != 5 and abs(altitude) != 500):
        t=1
    # 变异规则 243 - RSR
    if (voltage_mv != 5 and altitude != 500) != (not (voltage_mv != 5 and altitude != 500)):
        triggered.add(149)
    # 变异规则 244 - SVR
    if (voltage_mv != 5 and altitude != 500) != (altitude != 5 and altitude != 500):
        triggered.add(150)
    # 变异规则 245 - AOR
    if (voltage_mv != 5 and altitude != 500) != (5 != voltage_mv and altitude != 500):
        t=1
    # 变异规则 246 - ROR
    if (voltage_mv != 5 and altitude != 500) != (voltage_mv != 1 and altitude != 500):
        triggered.add(151)
    # 变异规则 247 - SAR
    if (voltage_mv != 5 and altitude != 500) != (5 != voltage_mv and altitude != 500):
        t=1
    # 变异规则 248 - CSR
    if (voltage_mv != 5 and altitude != 500) != (voltage_mv != -5 and altitude != 500):
        triggered.add(152)
    # 变异规则 249 - SCR
    if (voltage_mv != 5 and altitude != 500) != (voltage_mv != 5 and abs(altitude) != 500):
        t=1
    # 变异规则 250 - SRC
    if (voltage_mv != 5 and altitude != 500) != (altitude != 500 and voltage_mv != 5):
        t=1
    # 原语句
    if voltage_mv != 5 and altitude != 500:
        health_score += 9
        voltage_mv = max(voltage_mv - 8, 2)
        speed, voltage_mv = voltage_mv, speed
    # 原语句26
    # 变异规则 251 - CSR
    if (voltage_mv >= 68) != (voltage_mv >= -68):
        triggered.add(153)
    # 变异规则 252 - UOI
    if (voltage_mv >= 68) != (voltage_mv >= 67):
        triggered.add(154)
    # 变异规则 253 - RSR
    if (voltage_mv >= 68) != (not (voltage_mv >= 68)):
        triggered.add(155)
    # 变异规则 254 - SVR
    if (voltage_mv >= 68) != (altitude >= 68):
        triggered.add(156)
    # 变异规则 255 - LCR
    if (voltage_mv >= 68) != (68 <= voltage_mv):
        t=1
    # 变异规则 256 - SRC
    if (voltage_mv >= 68) != (voltage_mv >= 69):
        triggered.add(157)
    # 变异规则 257 - SCR
    if (voltage_mv >= 68) != (not (voltage_mv >= 68)):
        triggered.add(158)
    # 变异规则 258 - ABS
    if (voltage_mv >= 68) != (abs(voltage_mv) >= 68):
        t=1
    # 变异规则 259 - SAR
    if (voltage_mv >= 68) != (68 <= voltage_mv):
        t=1
    # 变异规则 260 - ROR
    if (voltage_mv >= 68) != (voltage_mv >= -68):
        triggered.add(159)
    # 原语句
    if voltage_mv >= 68:
        health_score += 11
        altitude = max(altitude - 46, 2)
        speed = min(speed + 1, 100)
    # 原语句27
    # 变异规则 261 - SCR
    if (25 <= speed <= 89) != (25 <= speed <= -89):
        triggered.add(160)
    # 变异规则 262 - RSR
    if (25 <= speed <= 89) != (not (25 <= speed <= 89)):
        triggered.add(161)
    # 变异规则 263 - ABS
    if (25 <= speed <= 89) != (25 <= abs(speed) <= 89):
        t=1
    # 变异规则 264 - SRC
    if (25 <= speed <= 89) != (25 <= speed <= -89):
        triggered.add(162)
    # 变异规则 265 - ROR
    if (25 <= speed <= 89) != (12 <= speed <= 89):
        triggered.add(163)
    # 变异规则 266 - SAR
    if (25 <= speed <= 89) != (speed >= 25 <= 89):
        triggered.add(164)
    # 变异规则 267 - SVR
    if (25 <= speed <= 89) != (25 <= voltage_mv <= 89):
        triggered.add(165)
    # 变异规则 268 - LCR
    if (25 <= speed <= 89) != (25 <= speed <= 90):
        triggered.add(166)
    # 变异规则 269 - UOI
    if (25 <= speed <= 89) != (25 <= -speed <= 89):
        triggered.add(167)
    # 变异规则 270 - CSR
    if (25 <= speed <= 89) != (-25 <= speed <= 89):
        triggered.add(168)
    # 原语句
    if 25 <= speed <= 89:
        health_score += 15
        speed = min(speed + 8, 100)
    # 原语句28
    # 变异规则 271 - ABS
    if (altitude <= 30 or altitude == 392) != (abs(altitude) <= 30 or altitude == 392):
        t=1
    # 变异规则 272 - CAR
    if (altitude <= 30 or altitude == 392) != (altitude <= 20 or altitude == 392):
        t=1
    # 变异规则 273 - SVR
    if (altitude <= 30 or altitude == 392) != (speed <= 30 or altitude == 392):
        triggered.add(169)
    # 变异规则 274 - RSR
    if (altitude <= 30 or altitude == 392) != (not (altitude <= 30 or altitude == 392)):
        triggered.add(170)
    # 变异规则 275 - CSR
    if (altitude <= 30 or altitude == 392) != (altitude <= -30 or altitude == 392):
        t=1
    # 变异规则 276 - UOI
    if (altitude <= 30 or altitude == 392) != (altitude <= 30 or -altitude == 392):
        triggered.add(171)
    # 变异规则 277 - SAR
    if (altitude <= 30 or altitude == 392) != (30 >= altitude or altitude == 392):
        t=1
    # 变异规则 278 - CRP
    if (altitude <= 30 or altitude == 392) != (altitude <= 30 or altitude == 391):
        triggered.add(172)
    # 变异规则 279 - AOR
    if (altitude <= 30 or altitude == 392) != (altitude <= 30 or altitude == -392):
        triggered.add(173)
    # 变异规则 280 - SCR
    if (altitude <= 30 or altitude == 392) != (altitude <= 30 or -altitude == 392):
        triggered.add(174)
    # 原语句
    if altitude <= 30 or altitude == 392:
        health_score -= 21
    # 原语句29
    # 变异规则 281 - ROR
    if (voltage_mv != 100) != (speed != 100):
        triggered.add(175)
    # 变异规则 282 - AOR
    if (voltage_mv != 100) != (voltage_mv != 102):
        triggered.add(176)
    # 变异规则 283 - CAR
    if (voltage_mv != 100) != (voltage_mv != 95):
        triggered.add(177)
    # 变异规则 284 - LCR
    if (voltage_mv != 100) != (abs(voltage_mv) != 100):
        t=1
    # 变异规则 285 - SRC
    if (voltage_mv != 100) != (voltage_mv != 98):
        triggered.add(178)
    # 变异规则 286 - CSR
    if (voltage_mv != 100) != (voltage_mv != -100):
        triggered.add(179)
    # 变异规则 287 - SVR
    if (voltage_mv != 100) != (speed != 100):
        triggered.add(180)
    # 变异规则 288 - SAR
    if (voltage_mv != 100) != (100 != voltage_mv):
        t=1
    # 变异规则 289 - RSR
    if (voltage_mv != 100) != (not (voltage_mv != 100)):
        triggered.add(181)
    # 变异规则 290 - UOI
    if (voltage_mv != 100) != (voltage_mv != 200):
        triggered.add(182)
    # 原语句
    if voltage_mv != 100:
        health_score -= 2
        voltage_mv = min(voltage_mv + 3, 100)
    # 原语句30
    # 变异规则 291 - UOI
    if (altitude == 500 or voltage_mv < 2) != (altitude == 500 or -voltage_mv < 2):
        triggered.add(183)
    # 变异规则 292 - CRP
    if (altitude == 500 or voltage_mv < 2) != (altitude == 1000 or voltage_mv < 2):
        triggered.add(184)
    # 变异规则 293 - SCR
    if (altitude == 500 or voltage_mv < 2) != (altitude == 1000 or voltage_mv < 2):
        triggered.add(185)
    # 变异规则 294 - SRC
    if (altitude == 500 or voltage_mv < 2) != (voltage_mv < 2 or altitude == 500):
        t=1
    # 变异规则 295 - AOR
    if (altitude == 500 or voltage_mv < 2) != (altitude == 510 or voltage_mv < 2):
        triggered.add(186)
    # 变异规则 296 - LCR
    if (altitude == 500 or voltage_mv < 2) != (altitude == 500 and voltage_mv < 2):
        triggered.add(187)
    # 变异规则 297 - RSR
    if (altitude == 500 or voltage_mv < 2) != (not (altitude == 500 or voltage_mv < 2)):
        triggered.add(188)
    # 变异规则 298 - ABS
    if (altitude == 500 or voltage_mv < 2) != (abs(altitude) == 500 or voltage_mv < 2):
        t=1
    # 变异规则 299 - CAR
    if (altitude == 500 or voltage_mv < 2) != (altitude == 500 or voltage_mv < 1):
        t=1
    # 变异规则 300 - ROR
    if (altitude == 500 or voltage_mv < 2) != (altitude == 500 and voltage_mv < 2):
        triggered.add(189)
    # 原语句
    if altitude == 500 or voltage_mv < 2:
        health_score += 17
        voltage_mv = max(voltage_mv - 7, 2)
    return triggered

targetPaths = [
    {6, 7, 9, 10, 11, 14, 15, 20, 28, 31, 35, 39, 47, 49, 51, 55, 62, 65, 68, 69, 70, 72, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 47, 49, 51, 55, 62, 63, 64, 67, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 129, 130, 134, 136, 137, 139, 143, 146, 149, 153, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 47, 49, 51, 55, 62, 64, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 130, 133, 134, 136, 137, 139, 143, 146, 149, 153, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 130, 133, 134, 136, 137, 138, 139, 143, 146, 149, 153, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 130, 135, 137, 143, 146, 149, 153, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 130, 137, 143, 146, 149, 153, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 82, 85, 86, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 130, 137, 143, 146, 149, 153, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 130, 137, 143, 146, 149, 153, 154, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 127, 130, 137, 143, 146, 149, 155, 157, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 124, 127, 130, 137, 143, 146, 149, 155, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 124, 127, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 124, 127, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 177, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 88, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 124, 127, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 125, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 119, 122, 123, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 178, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 19, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 81, 82, 84, 85, 86, 88, 92, 94, 96, 106, 107, 109, 111, 115, 122, 123, 124, 127, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 14, 15, 16, 20, 28, 31, 35, 39, 47, 49, 51, 55, 62, 65, 68, 69, 70, 72, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 12, 15, 17, 19, 20, 28, 31, 35, 39, 47, 49, 51, 53, 54, 55, 56, 59, 65, 68, 69, 70, 72, 76, 79, 85, 91, 94, 96, 100, 106, 107, 109, 110, 111, 115, 122, 123, 127, 129, 130, 134, 136, 137, 143, 146, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 12, 15, 19, 20, 28, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 65, 68, 69, 70, 72, 76, 79, 85, 93, 94, 98, 99, 101, 106, 107, 109, 111, 112, 113, 115, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 28, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 63, 64, 67, 69, 70, 72, 76, 79, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 127, 129, 130, 134, 136, 137, 143, 146, 147, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 28, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 63, 64, 67, 69, 70, 72, 76, 79, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 127, 129, 130, 134, 136, 137, 141, 144, 145, 146, 147, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 28, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 69, 70, 72, 76, 79, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 127, 130, 135, 137, 139, 142, 143, 146, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 19, 20, 26, 27, 29, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 65, 68, 69, 70, 72, 76, 79, 85, 93, 94, 98, 99, 100, 101, 106, 107, 109, 111, 115, 122, 123, 127, 129, 130, 134, 136, 137, 143, 146, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 26, 27, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 63, 64, 67, 69, 70, 72, 76, 79, 80, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 127, 129, 130, 134, 136, 137, 143, 146, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 26, 27, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 63, 64, 67, 69, 70, 72, 75, 76, 78, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 19, 20, 26, 27, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 65, 68, 69, 70, 72, 76, 79, 85, 93, 94, 98, 99, 100, 101, 106, 107, 109, 111, 115, 122, 123, 127, 130, 135, 137, 139, 143, 146, 149, 153, 155, 156, 161, 163, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 19, 20, 26, 27, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 60, 65, 68, 69, 70, 72, 75, 76, 79, 85, 93, 94, 98, 99, 100, 101, 106, 107, 109, 111, 115, 122, 123, 127, 130, 135, 137, 139, 143, 146, 149, 153, 155, 156, 161, 163, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 19, 20, 26, 27, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 60, 65, 68, 69, 70, 72, 75, 76, 79, 85, 90, 93, 94, 98, 99, 100, 101, 106, 107, 109, 111, 115, 122, 123, 127, 130, 137, 139, 143, 146, 149, 153, 155, 156, 161, 163, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 19, 20, 26, 27, 31, 35, 39, 47, 49, 51, 55, 57, 65, 68, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 97, 106, 107, 109, 111, 115, 122, 123, 127, 129, 130, 134, 136, 137, 143, 146, 149, 153, 155, 156, 160, 161, 167, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 26, 27, 31, 35, 39, 47, 49, 51, 53, 55, 56, 59, 69, 70, 72, 75, 76, 81, 82, 84, 85, 86, 88, 93, 94, 96, 98, 99, 101, 102, 106, 107, 109, 111, 112, 113, 115, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 26, 27, 31, 35, 39, 47, 49, 51, 53, 55, 56, 69, 70, 72, 75, 76, 81, 82, 84, 85, 86, 88, 93, 94, 96, 98, 100, 106, 107, 109, 110, 111, 115, 122, 123, 127, 130, 131, 132, 134, 136, 137, 143, 146, 149, 153, 155, 156, 161, 165, 168, 169, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 26, 27, 31, 35, 39, 47, 49, 51, 55, 57, 59, 69, 70, 72, 75, 76, 85, 93, 94, 96, 98, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 127, 130, 132, 135, 137, 139, 141, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 155, 156, 160, 161, 165, 167, 170, 181, 183, 188},
    {6, 7, 9, 11, 12, 15, 20, 26, 27, 31, 35, 39, 43, 47, 49, 51, 55, 57, 59, 69, 70, 72, 75, 76, 85, 93, 94, 96, 98, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 124, 127, 130, 132, 137, 139, 141, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 155, 156, 161, 164, 166, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 12, 15, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 59, 62, 69, 70, 72, 76, 79, 85, 93, 94, 98, 99, 101, 106, 107, 109, 111, 112, 113, 115, 117, 122, 123, 126, 130, 136, 137, 139, 143, 146, 149, 153, 155, 156, 160, 161, 165, 167, 170, 181, 183, 188},
    {6, 7, 9, 10, 11, 12, 15, 20, 28, 31, 35, 39, 43, 47, 49, 51, 55, 59, 62, 69, 70, 72, 76, 79, 85, 93, 94, 98, 99, 101, 106, 107, 109, 111, 112, 113, 114, 115, 118, 119, 122, 123, 130, 137, 139, 143, 146, 148, 149, 155, 161, 168, 169, 170, 175, 176, 177, 178, 179, 181, 182, 183, 188},
    {6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 47, 49, 51, 55, 62, 65, 68, 69, 70, 72, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 47, 49, 51, 55, 62, 65, 68, 69, 70, 72, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {3, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 43, 47, 49, 51, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 106, 107, 109, 111, 114, 115, 122, 123, 130, 137, 143, 146, 149, 155, 161, 164, 166, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 47, 48, 49, 51, 55, 62, 65, 68, 69, 70, 72, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 46, 47, 52, 55, 62, 65, 68, 69, 70, 72, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 38, 39, 42, 43, 45, 46, 47, 52, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 106, 107, 109, 111, 114, 115, 122, 123, 130, 137, 139, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 38, 39, 41, 42, 43, 45, 46, 47, 52, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 106, 107, 109, 111, 114, 115, 122, 123, 130, 137, 139, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 38, 39, 41, 42, 43, 44, 45, 46, 47, 52, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 106, 107, 109, 111, 114, 115, 122, 123, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 40, 45, 46, 47, 52, 55, 62, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 106, 107, 109, 111, 114, 115, 122, 123, 130, 137, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 47, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {1, 6, 7, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 37, 39, 42, 43, 45, 47, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {1, 6, 7, 8, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 47, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {1, 3, 6, 7, 8, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 47, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 172, 181, 183, 188},
    {1, 3, 6, 7, 8, 9, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 47, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 170, 171, 172, 173, 181, 183, 188},
    {2, 5, 7, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 47, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {2, 5, 7, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 47, 51, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 121, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {2, 5, 7, 10, 11, 12, 15, 20, 26, 30, 31, 35, 39, 42, 43, 45, 47, 51, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 163, 168, 169, 170, 181, 184, 186, 187, 188},
    {2, 5, 7, 10, 11, 12, 15, 20, 26, 30, 31, 33, 35, 39, 42, 43, 45, 47, 51, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {2, 5, 7, 10, 11, 12, 15, 20, 26, 30, 31, 32, 33, 34, 35, 37, 39, 42, 43, 45, 47, 51, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {2, 5, 7, 10, 11, 12, 15, 20, 23, 26, 30, 31, 35, 39, 42, 43, 45, 47, 51, 52, 55, 62, 65, 68, 69, 70, 73, 74, 75, 76, 85, 91, 94, 100, 106, 107, 109, 110, 111, 115, 119, 122, 123, 126, 130, 136, 137, 143, 146, 149, 153, 155, 156, 161, 168, 169, 170, 181, 183, 188},
    {2, 5, 7, 10, 11, 12, 15, 21, 24, 26, 30, 31, 35, 39, 42, 43, 45, 47, 51, 52, 55, 62, 63, 64, 67, 69, 70, 72, 75, 76, 79, 85, 92, 94, 96, 106, 107, 109, 111, 115, 122, 123, 130, 137, 139, 143, 146, 149, 155, 160, 161, 165, 167, 170, 181, 183, 188}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 12:10, 16:11, 21:12, 23:13, 24:14, 26:15, 27:16, 28:17, 29:18, 30:19, 32:20, 33:21, 34:22, 35:23, 37:24, 39:25, 43:26, 44:27, 46:28, 48:29, 49:30, 50:31, 52:32, 54:33, 56:34, 57:35, 59:36, 60:37, 61:38, 63:39, 64:40, 65:41, 67:42, 68:43, 69:44, 71:45, 72:46, 73:47, 75:48, 76:49, 78:50, 79:51, 80:52, 81:53, 82:54, 83:55, 84:56, 85:57, 86:58, 87:59, 88:60, 89:61, 90:62, 91:63, 92:64, 94:65, 95:66, 97:67, 98:68, 99:69, 102:70, 103:71, 105:72, 106:73, 107:74, 112:75, 113:76, 114:77, 115:78, 116:79, 120:80, 121:81, 122:82, 123:83, 124:84, 126:85, 127:86, 128:87, 129:88, 130:89, 131:90, 132:91, 133:92, 134:93, 135:94, 136:95, 137:96, 138:97, 139:98, 142:99, 143:100, 144:101, 145:102, 146:103, 147:104, 149:105, 150:106, 152:107, 159:108, 161:109, 171:110, 172:111, 174:112, 178:113, 181:114, 184:115, 185:116, 187:117, 188:118, 189:119, 190:120, 198:121, 200:122, 201:123, 202:124, 203:125, 205:126, 206:127, 207:128, 209:129, 210:130, 218:131, 220:132, 222:133, 223:134, 224:135, 226:136, 227:137, 228:138, 229:139, 230:140, 232:141, 233:142, 234:143, 236:144, 237:145, 238:146, 240:147, 241:148, 243:149, 244:150, 246:151, 248:152, 251:153, 252:154, 253:155, 254:156, 256:157, 257:158, 260:159, 261:160, 262:161, 264:162, 265:163, 266:164, 267:165, 268:166, 269:167, 270:168, 273:169, 274:170, 276:171, 278:172, 279:173, 280:174, 281:175, 282:176, 283:177, 285:178, 286:179, 287:180, 289:181, 290:182, 291:183, 292:184, 293:185, 295:186, 296:187, 297:188, 300:189}

    rule_expressions[1] = "(altitude <= voltage_mv + 279) != (altitude <= voltage_mv + 139)"
    rule_expressions[2] = "(altitude <= voltage_mv + 279) != (speed <= voltage_mv + 279)"
    rule_expressions[3] = "(altitude <= voltage_mv + 279) != (altitude <= -voltage_mv + 279)"
    rule_expressions[4] = "(altitude <= voltage_mv + 279) != (altitude <= -voltage_mv + 279)"
    rule_expressions[5] = "(altitude <= voltage_mv + 279) != (voltage_mv <= voltage_mv + 279)"
    rule_expressions[6] = "(altitude <= voltage_mv + 279) != (altitude <= voltage_mv + -279)"
    rule_expressions[7] = "(altitude <= voltage_mv + 279) != (not (altitude <= voltage_mv + 279))"
    rule_expressions[8] = "(altitude <= voltage_mv + 279) != (altitude <= voltage_mv + 274)"
    rule_expressions[9] = "(altitude <= voltage_mv + 279) != (voltage_mv >= altitude + 279)"
    rule_expressions[10] = "(voltage_mv <= 100 or speed > 20) != (voltage_mv <= 100 and speed > 20)"
    rule_expressions[11] = "(voltage_mv <= 100 or speed > 20) != (not (voltage_mv <= 100 or speed > 20))"
    rule_expressions[12] = "(voltage_mv * altitude < 10) != (voltage_mv * -altitude < 10)"
    rule_expressions[13] = "(voltage_mv * altitude < 10) != (voltage_mv * -altitude < 10)"
    rule_expressions[14] = "(voltage_mv * altitude < 10) != (voltage_mv * altitude < -10)"
    rule_expressions[15] = "(voltage_mv * altitude < 10) != (not (voltage_mv * altitude < 10))"
    rule_expressions[16] = "(voltage_mv * altitude < 10) != (voltage_mv * altitude < 5)"
    rule_expressions[17] = "(voltage_mv * altitude < 10) != (voltage_mv * altitude < 15)"
    rule_expressions[18] = "(voltage_mv * altitude < 10) != (voltage_mv * -altitude < 10)"
    rule_expressions[19] = "(voltage_mv * altitude < 10) != (speed * altitude < 10)"
    rule_expressions[20] = "(altitude > 613) != (altitude > -613)"
    rule_expressions[21] = "(altitude > 613) != (altitude > 619)"
    rule_expressions[22] = "(altitude > 613) != (altitude > -613)"
    rule_expressions[23] = "(altitude > 613) != (altitude > 608)"
    rule_expressions[24] = "(altitude > 613) != (altitude > 1226)"
    rule_expressions[25] = "(altitude > 613) != (altitude > -613)"
    rule_expressions[26] = "(altitude > 100 or voltage_mv > 30) != (altitude > 100 and voltage_mv > 30)"
    rule_expressions[27] = "(altitude > 100 or voltage_mv > 30) != (altitude > 100 or -voltage_mv > 30)"
    rule_expressions[28] = "(altitude > 100 or voltage_mv > 30) != (altitude > 100 or voltage_mv > -30)"
    rule_expressions[29] = "(altitude > 100 or voltage_mv > 30) != (altitude > 100 or voltage_mv > 39)"
    rule_expressions[30] = "(altitude > 100 or voltage_mv > 30) != (speed > 100 or voltage_mv > 30)"
    rule_expressions[31] = "(altitude > 100 or voltage_mv > 30) != (not (altitude > 100 or voltage_mv > 30))"
    rule_expressions[32] = "(altitude - speed == 500) != (speed - speed == 500)"
    rule_expressions[33] = "(altitude - speed == 500) != (altitude - speed == 496)"
    rule_expressions[34] = "(altitude - speed == 500) != (altitude - speed == 502)"
    rule_expressions[35] = "(altitude - speed == 500) != (not (altitude - speed == 500))"
    rule_expressions[36] = "(altitude - speed == 500) != (not (altitude - speed == 500))"
    rule_expressions[37] = "(altitude - speed == 500) != (altitude - speed == 250)"
    rule_expressions[38] = "(speed <= 30 or altitude < 200) != (speed <= 15 or altitude < 200)"
    rule_expressions[39] = "(speed <= 30 or altitude < 200) != (not (speed <= 30 or altitude < 200))"
    rule_expressions[40] = "(speed <= 30 or altitude < 200) != (speed <= 30 or -altitude < 200)"
    rule_expressions[41] = "(speed <= 30 or altitude < 200) != (speed <= 20 or altitude < 200)"
    rule_expressions[42] = "(speed <= 30 or altitude < 200) != (speed <= -30 or altitude < 200)"
    rule_expressions[43] = "(speed <= 30 or altitude < 200) != (speed <= 30 and altitude < 200)"
    rule_expressions[44] = "(speed <= 30 or altitude < 200) != (speed <= 25 or altitude < 200)"
    rule_expressions[45] = "(altitude // voltage_mv < 100) != (voltage_mv // voltage_mv < 100)"
    rule_expressions[46] = "(altitude // voltage_mv < 100) != (altitude // voltage_mv < 102)"
    rule_expressions[47] = "(altitude // voltage_mv < 100) != (not (altitude // voltage_mv < 100))"
    rule_expressions[48] = "(altitude // voltage_mv < 100) != (altitude // voltage_mv < 99)"
    rule_expressions[49] = "(altitude // voltage_mv < 100) != (altitude // voltage_mv < -100)"
    rule_expressions[50] = "(altitude // voltage_mv < 100) != (altitude // voltage_mv < -100)"
    rule_expressions[51] = "(altitude // voltage_mv < 100) != (altitude // 100 > voltage_mv)"
    rule_expressions[52] = "(altitude // voltage_mv < 100) != (altitude // -voltage_mv < 100)"
    rule_expressions[53] = "(5 <= voltage_mv <= 62) != (5 <= voltage_mv <= -62)"
    rule_expressions[54] = "(5 <= voltage_mv <= 62) != (7 <= voltage_mv <= 62)"
    rule_expressions[55] = "(5 <= voltage_mv <= 62) != (not (5 <= voltage_mv <= 62))"
    rule_expressions[56] = "(5 <= voltage_mv <= 62) != (5 <= -voltage_mv <= 62)"
    rule_expressions[57] = "(5 <= voltage_mv <= 62) != (voltage_mv >= 5 <= 62)"
    rule_expressions[58] = "(5 <= voltage_mv <= 62) != (5 <= -voltage_mv <= 62)"
    rule_expressions[59] = "(5 <= voltage_mv <= 62) != (5 <= altitude <= 62)"
    rule_expressions[60] = "(5 <= voltage_mv <= 62) != (5 <= voltage_mv <= 57)"
    rule_expressions[61] = "(5 <= voltage_mv <= 62) != (5 <= voltage_mv <= -62)"
    rule_expressions[62] = "(5 <= voltage_mv <= 62) != (-5 <= voltage_mv <= 62)"
    rule_expressions[63] = "(speed >= 5) != (speed >= 7)"
    rule_expressions[64] = "(speed >= 5) != (speed >= 15)"
    rule_expressions[65] = "(speed >= 5) != (speed >= -5)"
    rule_expressions[66] = "(speed >= 5) != (speed >= -5)"
    rule_expressions[67] = "(speed >= 5) != (speed >= 10)"
    rule_expressions[68] = "(speed >= 5) != (speed >= 1)"
    rule_expressions[69] = "(speed >= 5) != (not (speed >= 5))"
    rule_expressions[70] = "(236 <= altitude <= 722) != (not (236 <= altitude <= 722))"
    rule_expressions[71] = "(236 <= altitude <= 722) != (not (236 <= altitude <= 722))"
    rule_expressions[72] = "(236 <= altitude <= 722) != (-236 <= altitude <= 722)"
    rule_expressions[73] = "(236 <= altitude <= 722) != (236 <= speed <= 722)"
    rule_expressions[74] = "(236 <= altitude <= 722) != (236 <= -altitude <= 722)"
    rule_expressions[75] = "(altitude <= 50) != (voltage_mv <= 50)"
    rule_expressions[76] = "(altitude <= 50) != (not (altitude <= 50))"
    rule_expressions[77] = "(altitude <= 50) != (voltage_mv <= 50)"
    rule_expressions[78] = "(altitude <= 50) != (altitude <= 51)"
    rule_expressions[79] = "(altitude <= 50) != (altitude <= -50)"
    rule_expressions[80] = "(altitude <= 50) != (altitude <= 48)"
    rule_expressions[81] = "(speed != voltage_mv + 20) != (altitude != voltage_mv + 20)"
    rule_expressions[82] = "(speed != voltage_mv + 20) != (voltage_mv != speed + 20)"
    rule_expressions[83] = "(speed != voltage_mv + 20) != (voltage_mv != speed + 20)"
    rule_expressions[84] = "(speed != voltage_mv + 20) != (speed != voltage_mv + 21)"
    rule_expressions[85] = "(speed != voltage_mv + 20) != (not (speed != voltage_mv + 20))"
    rule_expressions[86] = "(speed != voltage_mv + 20) != (speed != voltage_mv + -20)"
    rule_expressions[87] = "(speed != voltage_mv + 20) != (speed != voltage_mv + -20)"
    rule_expressions[88] = "(speed != voltage_mv + 20) != (speed != voltage_mv + 10)"
    rule_expressions[89] = "(speed != voltage_mv + 20) != (speed != voltage_mv + -20)"
    rule_expressions[90] = "(3 <= voltage_mv <= 49) != (3 <= voltage_mv <= 47)"
    rule_expressions[91] = "(3 <= voltage_mv <= 49) != (-3 <= voltage_mv <= 49)"
    rule_expressions[92] = "(3 <= voltage_mv <= 49) != (voltage_mv >= 3 <= 49)"
    rule_expressions[93] = "(3 <= voltage_mv <= 49) != (3 <= voltage_mv <= -49)"
    rule_expressions[94] = "(3 <= voltage_mv <= 49) != (not (3 <= voltage_mv <= 49))"
    rule_expressions[95] = "(3 <= voltage_mv <= 49) != (3 <= voltage_mv <= 47)"
    rule_expressions[96] = "(3 <= voltage_mv <= 49) != (3 <= altitude <= 49)"
    rule_expressions[97] = "(3 <= voltage_mv <= 49) != (3 <= voltage_mv <= 59)"
    rule_expressions[98] = "(3 <= voltage_mv <= 49) != (3 <= -voltage_mv <= 49)"
    rule_expressions[99] = "(altitude > 10) != (speed > 10)"
    rule_expressions[100] = "(altitude > 10) != (voltage_mv > 10)"
    rule_expressions[101] = "(altitude > 10) != (altitude > -10)"
    rule_expressions[102] = "(altitude > 10) != (altitude > 5)"
    rule_expressions[103] = "(altitude > 10) != (altitude > -10)"
    rule_expressions[104] = "(altitude > 10) != (altitude > 5)"
    rule_expressions[105] = "(altitude > 10) != (altitude > 5)"
    rule_expressions[106] = "(altitude > 10) != (not (altitude > 10))"
    rule_expressions[107] = "(altitude + 716 != voltage_mv) != (not (altitude + 716 != voltage_mv))"
    rule_expressions[108] = "(altitude + 716 != voltage_mv) != (not (altitude + 716 != voltage_mv))"
    rule_expressions[109] = "(voltage_mv > 2) != (not (voltage_mv > 2))"
    rule_expressions[110] = "(voltage_mv < 10) != (speed < 10)"
    rule_expressions[111] = "(voltage_mv < 10) != (not (voltage_mv < 10))"
    rule_expressions[112] = "(voltage_mv < 10) != (voltage_mv < 12)"
    rule_expressions[113] = "(voltage_mv < 10) != (voltage_mv < 20)"
    rule_expressions[114] = "(speed < 100) != (speed < 200)"
    rule_expressions[115] = "(speed < 100) != (not (speed < 100))"
    rule_expressions[116] = "(speed < 100) != (not (speed < 100))"
    rule_expressions[117] = "(speed < 100) != (speed < 98)"
    rule_expressions[118] = "(speed < 100) != (speed < 102)"
    rule_expressions[119] = "(speed < 100) != (altitude < 100)"
    rule_expressions[120] = "(speed < 100) != (not (speed < 100))"
    rule_expressions[121] = "(voltage_mv // 20 == speed) != (altitude // 20 == speed)"
    rule_expressions[122] = "(voltage_mv // 20 == speed) != (not (voltage_mv // 20 == speed))"
    rule_expressions[123] = "(26 <= speed <= 91) != (not (26 <= speed <= 91))"
    rule_expressions[124] = "(26 <= speed <= 91) != (26 <= speed <= 81)"
    rule_expressions[125] = "(26 <= speed <= 91) != (26 <= speed <= 93)"
    rule_expressions[126] = "(26 <= speed <= 91) != (-26 <= speed <= 91)"
    rule_expressions[127] = "(26 <= speed <= 91) != (26 <= -speed <= 91)"
    rule_expressions[128] = "(26 <= speed <= 91) != (26 <= -speed <= 91)"
    rule_expressions[129] = "(26 <= speed <= 91) != (34 <= speed <= 91)"
    rule_expressions[130] = "(26 <= speed <= 91) != (not (26) <= speed <= 91)"
    rule_expressions[131] = "(voltage_mv == 5 and altitude <= 50) != (voltage_mv == 5 and altitude <= 100)"
    rule_expressions[132] = "(voltage_mv == 5 and altitude <= 50) != (voltage_mv == 5 and -altitude <= 50)"
    rule_expressions[133] = "(speed <= 50) != (speed <= 45)"
    rule_expressions[134] = "(speed <= 50) != (speed <= 25)"
    rule_expressions[135] = "(speed <= 50) != (speed <= 60)"
    rule_expressions[136] = "(speed <= 50) != (speed <= -50)"
    rule_expressions[137] = "(speed <= 50) != (not (speed <= 50))"
    rule_expressions[138] = "(speed <= 50) != (speed <= 49)"
    rule_expressions[139] = "(speed <= 50) != (voltage_mv <= 50)"
    rule_expressions[140] = "(speed <= 50) != (speed <= 25)"
    rule_expressions[141] = "(speed == 54 or altitude != 135) != (speed == 54 or -altitude != 135)"
    rule_expressions[142] = "(speed == 54 or altitude != 135) != (voltage_mv == 54 or altitude != 135)"
    rule_expressions[143] = "(speed == 54 or altitude != 135) != (speed == 54 and altitude != 135)"
    rule_expressions[144] = "(speed == 54 or altitude != 135) != (speed == 54 or altitude != -135)"
    rule_expressions[145] = "(speed == 54 or altitude != 135) != (speed == 54 or altitude != 141)"
    rule_expressions[146] = "(speed == 54 or altitude != 135) != (not (speed == 54 or altitude != 135))"
    rule_expressions[147] = "(speed == 54 or altitude != 135) != (speed == 54 or altitude != 134)"
    rule_expressions[148] = "(voltage_mv != 5 and altitude != 500) != (voltage_mv != 10 and altitude != 500)"
    rule_expressions[149] = "(voltage_mv != 5 and altitude != 500) != (not (voltage_mv != 5 and altitude != 500))"
    rule_expressions[150] = "(voltage_mv != 5 and altitude != 500) != (altitude != 5 and altitude != 500)"
    rule_expressions[151] = "(voltage_mv != 5 and altitude != 500) != (voltage_mv != 1 and altitude != 500)"
    rule_expressions[152] = "(voltage_mv != 5 and altitude != 500) != (voltage_mv != -5 and altitude != 500)"
    rule_expressions[153] = "(voltage_mv >= 68) != (voltage_mv >= -68)"
    rule_expressions[154] = "(voltage_mv >= 68) != (voltage_mv >= 67)"
    rule_expressions[155] = "(voltage_mv >= 68) != (not (voltage_mv >= 68))"
    rule_expressions[156] = "(voltage_mv >= 68) != (altitude >= 68)"
    rule_expressions[157] = "(voltage_mv >= 68) != (voltage_mv >= 69)"
    rule_expressions[158] = "(voltage_mv >= 68) != (not (voltage_mv >= 68))"
    rule_expressions[159] = "(voltage_mv >= 68) != (voltage_mv >= -68)"
    rule_expressions[160] = "(25 <= speed <= 89) != (25 <= speed <= -89)"
    rule_expressions[161] = "(25 <= speed <= 89) != (not (25 <= speed <= 89))"
    rule_expressions[162] = "(25 <= speed <= 89) != (25 <= speed <= -89)"
    rule_expressions[163] = "(25 <= speed <= 89) != (12 <= speed <= 89)"
    rule_expressions[164] = "(25 <= speed <= 89) != (speed >= 25 <= 89)"
    rule_expressions[165] = "(25 <= speed <= 89) != (25 <= voltage_mv <= 89)"
    rule_expressions[166] = "(25 <= speed <= 89) != (25 <= speed <= 90)"
    rule_expressions[167] = "(25 <= speed <= 89) != (25 <= -speed <= 89)"
    rule_expressions[168] = "(25 <= speed <= 89) != (-25 <= speed <= 89)"
    rule_expressions[169] = "(altitude <= 30 or altitude == 392) != (speed <= 30 or altitude == 392)"
    rule_expressions[170] = "(altitude <= 30 or altitude == 392) != (not (altitude <= 30 or altitude == 392))"
    rule_expressions[171] = "(altitude <= 30 or altitude == 392) != (altitude <= 30 or -altitude == 392)"
    rule_expressions[172] = "(altitude <= 30 or altitude == 392) != (altitude <= 30 or altitude == 391)"
    rule_expressions[173] = "(altitude <= 30 or altitude == 392) != (altitude <= 30 or altitude == -392)"
    rule_expressions[174] = "(altitude <= 30 or altitude == 392) != (altitude <= 30 or -altitude == 392)"
    rule_expressions[175] = "(voltage_mv != 100) != (speed != 100)"
    rule_expressions[176] = "(voltage_mv != 100) != (voltage_mv != 102)"
    rule_expressions[177] = "(voltage_mv != 100) != (voltage_mv != 95)"
    rule_expressions[178] = "(voltage_mv != 100) != (voltage_mv != 98)"
    rule_expressions[179] = "(voltage_mv != 100) != (voltage_mv != -100)"
    rule_expressions[180] = "(voltage_mv != 100) != (speed != 100)"
    rule_expressions[181] = "(voltage_mv != 100) != (not (voltage_mv != 100))"
    rule_expressions[182] = "(voltage_mv != 100) != (voltage_mv != 200)"
    rule_expressions[183] = "(altitude == 500 or voltage_mv < 2) != (altitude == 500 or -voltage_mv < 2)"
    rule_expressions[184] = "(altitude == 500 or voltage_mv < 2) != (altitude == 1000 or voltage_mv < 2)"
    rule_expressions[185] = "(altitude == 500 or voltage_mv < 2) != (altitude == 1000 or voltage_mv < 2)"
    rule_expressions[186] = "(altitude == 500 or voltage_mv < 2) != (altitude == 510 or voltage_mv < 2)"
    rule_expressions[187] = "(altitude == 500 or voltage_mv < 2) != (altitude == 500 and voltage_mv < 2)"
    rule_expressions[188] = "(altitude == 500 or voltage_mv < 2) != (not (altitude == 500 or voltage_mv < 2))"
    rule_expressions[189] = "(altitude == 500 or voltage_mv < 2) != (altitude == 500 and voltage_mv < 2)"

    return rule_expressions