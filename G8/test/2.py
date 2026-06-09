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
    # 变异规则 1 - AOR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 33 or voltage_mv <= 30):
        triggered.add(1)
    # 变异规则 2 - CAR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 or voltage_mv <= 31):
        t = 1
    # 变异规则 3 - SCR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 or voltage_mv <= 40):
        t = 1
    # 变异规则 4 - RSR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (not (voltage_mv >= 30 or voltage_mv <= 30)):
        triggered.add(2)
    # 变异规则 5 - ROR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 and voltage_mv <= 30):
        triggered.add(3)
    # 变异规则 6 - SVR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (speed >= 30 or voltage_mv <= 30):
        triggered.add(4)
    # 变异规则 7 - UOI
    if (voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 or -voltage_mv <= 30):
        t = 1
    # 变异规则 8 - SAR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 or 30 >= voltage_mv):
        t = 1
    # 变异规则 9 - ABS
    if (voltage_mv >= 30 or voltage_mv <= 30) != (abs(voltage_mv) >= 30 or voltage_mv <= 30):
        t = 1
    # 变异规则 10 - LCR
    if (voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 and voltage_mv <= 30):
        triggered.add(5)
    # 原语句
    if voltage_mv >= 30 or voltage_mv <= 30:
        health_score -= 8
        altitude = max(altitude - 10, 2)
        speed = min(speed + 4, 100)
    # 原语句2
    # 变异规则 11 - ABS
    if (7 <= voltage_mv <= 71) != (7 <= abs(voltage_mv) <= 71):
        t = 1
    # 变异规则 12 - AOR
    if (7 <= voltage_mv <= 71) != (9 <= voltage_mv <= 71):
        triggered.add(6)
    # 变异规则 13 - CRP
    if (7 <= voltage_mv <= 71) != (14 <= voltage_mv <= 71):
        triggered.add(7)
    # 变异规则 14 - SVR
    if (7 <= voltage_mv <= 71) != (7 <= speed <= 71):
        triggered.add(8)
    # 变异规则 15 - ROR
    if (7 <= voltage_mv <= 71) != (7 <= -voltage_mv <= 71):
        triggered.add(9)
    # 变异规则 16 - SRC
    if (7 <= voltage_mv <= 71) != (7 <= voltage_mv <= 75):
        triggered.add(10)
    # 变异规则 17 - CSR
    if (7 <= voltage_mv <= 71) != (7 <= voltage_mv <= -71):
        triggered.add(11)
    # 变异规则 18 - CAR
    if (7 <= voltage_mv <= 71) != (7 <= voltage_mv <= 70):
        triggered.add(12)
    # 变异规则 19 - SCR
    if (7 <= voltage_mv <= 71) != (7 <= abs(voltage_mv) <= 71):
        t = 1
    # 变异规则 20 - UOI
    if (7 <= voltage_mv <= 71) != (7 <= -voltage_mv <= 71):
        triggered.add(13)
    # 原语句
    if 7 <= voltage_mv <= 71:
        health_score += 8
        altitude = max(altitude - 5, 2)
    # 原语句3
    # 变异规则 21 - AOR
    if (4 <= voltage_mv <= 48) != (not (4 <= voltage_mv <= 48)):
        triggered.add(14)
    # 变异规则 22 - SAR
    if (4 <= voltage_mv <= 48) != (voltage_mv >= 4 <= 48):
        triggered.add(15)
    # 变异规则 23 - ROR
    if (4 <= voltage_mv <= 48) != (voltage_mv >= 4 <= 48):
        triggered.add(16)
    # 变异规则 24 - SCR
    if (4 <= voltage_mv <= 48) != (not (4) <= voltage_mv <= 48):
        triggered.add(17)
    # 变异规则 25 - CRP
    if (4 <= voltage_mv <= 48) != (13 <= voltage_mv <= 48):
        triggered.add(18)
    # 变异规则 26 - SRC
    if (4 <= voltage_mv <= 48) != (4 <= voltage_mv <= 96):
        triggered.add(19)
    # 变异规则 27 - RSR
    if (4 <= voltage_mv <= 48) != (not (4 <= voltage_mv <= 48)):
        triggered.add(20)
    # 变异规则 28 - ABS
    if (4 <= voltage_mv <= 48) != (4 <= abs(voltage_mv) <= 48):
        t = 1
    # 变异规则 29 - LCR
    if (4 <= voltage_mv <= 48) != (-4 <= voltage_mv <= 48):
        triggered.add(21)
    # 变异规则 30 - SVR
    if (4 <= voltage_mv <= 48) != (4 <= speed <= 48):
        triggered.add(22)
    # 原语句
    if 4 <= voltage_mv <= 48:
        health_score += 2
    # 原语句4
    # 变异规则 31 - CSR
    if (speed % altitude < 97) != (speed % altitude < -97):
        triggered.add(23)
    # 变异规则 32 - ROR
    if (speed % altitude < 97) != (speed % altitude < 100):
        triggered.add(24)
    # 变异规则 33 - SVR
    if (speed % altitude < 97) != (voltage_mv % altitude < 97):
        triggered.add(25)
    # 变异规则 34 - CRP
    if (speed % altitude < 97) != (speed % altitude < 99):
        triggered.add(26)
    # 变异规则 35 - SCR
    if (speed % altitude < 97) != (not (speed % altitude < 97)):
        triggered.add(27)
    # 变异规则 36 - SRC
    if (speed % altitude < 97) != (not (speed % altitude < 97)):
        triggered.add(28)
    # 变异规则 37 - ABS
    if (speed % altitude < 97) != (speed % abs(altitude) < 97):
        t = 1
    # 变异规则 38 - SAR
    if (speed % altitude < 97) != (speed % 97 > altitude):
        triggered.add(29)
    # 变异规则 39 - CAR
    if (speed % altitude < 97) != (speed % altitude < 87):
        triggered.add(30)
    # 变异规则 40 - RSR
    if (speed % altitude < 97) != (not (speed % altitude < 97)):
        triggered.add(31)
    # 原语句
    if speed % altitude < 97:
        health_score += 17
        altitude = min(altitude + 31, 1000)
        speed = min(speed + 5, 100)
    # 原语句5
    # 变异规则 41 - SAR
    if (altitude >= 200) != (200 <= altitude):
        t = 1
    # 变异规则 42 - SVR
    if (altitude >= 200) != (voltage_mv >= 200):
        triggered.add(32)
    # 变异规则 43 - CAR
    if (altitude >= 200) != (altitude >= 199):
        triggered.add(33)
    # 变异规则 44 - CRP
    if (altitude >= 200) != (altitude >= 400):
        triggered.add(34)
    # 变异规则 45 - RSR
    if (altitude >= 200) != (not (altitude >= 200)):
        triggered.add(35)
    # 变异规则 46 - ABS
    if (altitude >= 200) != (abs(altitude) >= 200):
        t = 1
    # 变异规则 47 - CSR
    if (altitude >= 200) != (altitude >= -200):
        triggered.add(36)
    # 变异规则 48 - ROR
    if (altitude >= 200) != (altitude >= 199):
        triggered.add(37)
    # 变异规则 49 - AOR
    if (altitude >= 200) != (voltage_mv >= 200):
        triggered.add(38)
    # 变异规则 50 - LCR
    if (altitude >= 200) != (altitude >= -200):
        triggered.add(39)
    # 原语句
    if altitude >= 200:
        health_score += 19
        speed = max(speed - 7, 2)
    # 原语句6
    # 变异规则 51 - SRC
    if (34 <= voltage_mv <= 84) != (34 <= voltage_mv <= -84):
        triggered.add(40)
    # 变异规则 52 - AOR
    if (34 <= voltage_mv <= 84) != (34 <= -voltage_mv <= 84):
        triggered.add(41)
    # 变异规则 53 - LCR
    if (34 <= voltage_mv <= 84) != (25 <= voltage_mv <= 84):
        triggered.add(42)
    # 变异规则 54 - UOI
    if (34 <= voltage_mv <= 84) != (34 <= -voltage_mv <= 84):
        triggered.add(43)
    # 变异规则 55 - CSR
    if (34 <= voltage_mv <= 84) != (-34 <= voltage_mv <= 84):
        triggered.add(44)
    # 变异规则 56 - CRP
    if (34 <= voltage_mv <= 84) != (68 <= voltage_mv <= 84):
        triggered.add(45)
    # 变异规则 57 - SCR
    if (34 <= voltage_mv <= 84) != (not (34) <= voltage_mv <= 84):
        triggered.add(46)
    # 变异规则 58 - ROR
    if (34 <= voltage_mv <= 84) != (29 <= voltage_mv <= 84):
        triggered.add(47)
    # 变异规则 59 - ABS
    if (34 <= voltage_mv <= 84) != (34 <= abs(voltage_mv) <= 84):
        t = 1
    # 变异规则 60 - SAR
    if (34 <= voltage_mv <= 84) != (voltage_mv >= 34 <= 84):
        triggered.add(48)
    # 原语句
    if 34 <= voltage_mv <= 84:
        health_score += 9
        altitude = max(altitude - 24, 2)
    # 原语句7
    # 变异规则 61 - CRP
    if (altitude != 500 or speed > 2) != (altitude != 250 or speed > 2):
        t = 1
    # 变异规则 62 - UOI
    if (altitude != 500 or speed > 2) != (altitude != 500 or -speed > 2):
        triggered.add(49)
    # 变异规则 63 - SAR
    if (altitude != 500 or speed > 2) != (altitude != 500 or 2 < speed):
        t = 1
    # 变异规则 64 - SCR
    if (altitude != 500 or speed > 2) != (not (altitude != 500 or speed > 2)):
        triggered.add(50)
    # 变异规则 65 - AOR
    if (altitude != 500 or speed > 2) != (altitude != 500 or 2 < speed):
        t = 1
    # 变异规则 66 - LCR
    if (altitude != 500 or speed > 2) != (altitude != 500 and speed > 2):
        triggered.add(51)
    # 变异规则 67 - SVR
    if (altitude != 500 or speed > 2) != (speed != 500 or speed > 2):
        t = 1
    # 变异规则 68 - CSR
    if (altitude != 500 or speed > 2) != (altitude != 500 or speed > -2):
        t = 1
    # 变异规则 69 - CAR
    if (altitude != 500 or speed > 2) != (altitude != 500 or speed > 7):
        triggered.add(52)
    # 变异规则 70 - RSR
    if (altitude != 500 or speed > 2) != (not (altitude != 500 or speed > 2)):
        triggered.add(53)
    # 原语句
    if altitude != 500 or speed > 2:
        health_score += 20
        altitude = max(altitude - 1, 2)
    # 原语句8
    # 变异规则 71 - UOI
    if (speed == voltage_mv // 5) != (speed == -voltage_mv // 5):
        triggered.add(54)
    # 变异规则 72 - SRC
    if (speed == voltage_mv // 5) != (speed == voltage_mv // 3):
        triggered.add(55)
    # 变异规则 73 - AOR
    if (speed == voltage_mv // 5) != (speed == voltage_mv // 3):
        triggered.add(56)
    # 变异规则 74 - ROR
    if (speed == voltage_mv // 5) != (speed == voltage_mv // 15):
        triggered.add(57)
    # 变异规则 75 - CAR
    if (speed == voltage_mv // 5) != (speed == voltage_mv // 4):
        triggered.add(58)
    # 变异规则 76 - SAR
    if (speed == voltage_mv // 5) != (voltage_mv == speed // 5):
        triggered.add(59)
    # 变异规则 77 - RSR
    if (speed == voltage_mv // 5) != (not (speed == voltage_mv // 5)):
        triggered.add(60)
    # 变异规则 78 - LCR
    if (speed == voltage_mv // 5) != (speed == voltage_mv // 3):
        triggered.add(61)
    # 变异规则 79 - ABS
    if (speed == voltage_mv // 5) != (abs(speed) == voltage_mv // 5):
        t = 1
    # 变异规则 80 - CSR
    if (speed == voltage_mv // 5) != (speed == voltage_mv // -5):
        triggered.add(62)
    # 原语句
    if speed == voltage_mv // 5:
        health_score -= 11
    # 原语句9
    # 变异规则 81 - UOI
    if (speed < 100 or altitude <= 500) != (speed < 100 or -altitude <= 500):
        t = 1
    # 变异规则 82 - SCR
    if (speed < 100 or altitude <= 500) != (not (speed < 100 or altitude <= 500)):
        triggered.add(63)
    # 变异规则 83 - SVR
    if (speed < 100 or altitude <= 500) != (voltage_mv < 100 or altitude <= 500):
        t = 1
    # 变异规则 84 - AOR
    if (speed < 100 or altitude <= 500) != (speed < 100 or altitude <= -500):
        triggered.add(64)
    # 变异规则 85 - SRC
    if (speed < 100 or altitude <= 500) != (altitude <= 500 or speed < 100):
        t = 1
    # 变异规则 86 - ABS
    if (speed < 100 or altitude <= 500) != (speed < 100 or abs(altitude) <= 500):
        t = 1
    # 变异规则 87 - CSR
    if (speed < 100 or altitude <= 500) != (speed < 100 or altitude <= -500):
        triggered.add(65)
    # 变异规则 88 - SAR
    if (speed < 100 or altitude <= 500) != (100 > speed or altitude <= 500):
        t = 1
    # 变异规则 89 - LCR
    if (speed < 100 or altitude <= 500) != (speed < 100 and altitude <= 500):
        triggered.add(66)
    # 变异规则 90 - CAR
    if (speed < 100 or altitude <= 500) != (speed < 110 or altitude <= 500):
        t = 1
    # 原语句
    if speed < 100 or altitude <= 500:
        health_score += 18
        speed, voltage_mv = voltage_mv, speed
    # 原语句10
    # 变异规则 91 - CAR
    if (altitude <= 10 and altitude > 30) != (altitude <= 10 and altitude > 40):
        t = 1
    # 变异规则 92 - SRC
    if (altitude <= 10 and altitude > 30) != (altitude > 30 and altitude <= 10):
        t = 1
    # 变异规则 93 - SAR
    if (altitude <= 10 and altitude > 30) != (altitude <= 10 and 30 < altitude):
        t = 1
    # 变异规则 94 - UOI
    if (altitude <= 10 and altitude > 30) != (altitude <= 10 and -altitude > 30):
        t = 1
    # 变异规则 95 - ROR
    if (altitude <= 10 and altitude > 30) != (speed <= 10 and altitude > 30):
        triggered.add(67)
    # 变异规则 96 - RSR
    if (altitude <= 10 and altitude > 30) != (not (altitude <= 10 and altitude > 30)):
        triggered.add(68)
    # 变异规则 97 - CSR
    if (altitude <= 10 and altitude > 30) != (altitude <= -10 and altitude > 30):
        t = 1
    # 变异规则 98 - SCR
    if (altitude <= 10 and altitude > 30) != (not (altitude <= 10 and altitude > 30)):
        triggered.add(69)
    # 变异规则 99 - SVR
    if (altitude <= 10 and altitude > 30) != (voltage_mv <= 10 and altitude > 30):
        triggered.add(70)
    # 变异规则 100 - AOR
    if (altitude <= 10 and altitude > 30) != (altitude <= 20 and altitude > 30):
        t = 1
    # 原语句
    if altitude <= 10 and altitude > 30:
        health_score += 16
        speed = max(speed - 9, 2)
    # 原语句11
    # 变异规则 101 - CSR
    if (12 <= voltage_mv <= 70) != (-12 <= voltage_mv <= 70):
        triggered.add(71)
    # 变异规则 102 - UOI
    if (12 <= voltage_mv <= 70) != (12 <= -voltage_mv <= 70):
        triggered.add(72)
    # 变异规则 103 - SAR
    if (12 <= voltage_mv <= 70) != (voltage_mv >= 12 <= 70):
        triggered.add(73)
    # 变异规则 104 - CAR
    if (12 <= voltage_mv <= 70) != (12 <= voltage_mv <= 72):
        triggered.add(74)
    # 变异规则 105 - SRC
    if (12 <= voltage_mv <= 70) != (12 <= speed <= 70):
        triggered.add(75)
    # 变异规则 106 - CRP
    if (12 <= voltage_mv <= 70) != (19 <= voltage_mv <= 70):
        triggered.add(76)
    # 变异规则 107 - ABS
    if (12 <= voltage_mv <= 70) != (12 <= abs(voltage_mv) <= 70):
        t = 1
    # 变异规则 108 - AOR
    if (12 <= voltage_mv <= 70) != (12 <= voltage_mv <= -70):
        triggered.add(77)
    # 变异规则 109 - RSR
    if (12 <= voltage_mv <= 70) != (not (12 <= voltage_mv <= 70)):
        triggered.add(78)
    # 变异规则 110 - SCR
    if (12 <= voltage_mv <= 70) != (not (12) <= voltage_mv <= 70):
        triggered.add(79)
    # 原语句
    if 12 <= voltage_mv <= 70:
        health_score -= 8
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句12
    # 变异规则 111 - ROR
    if (12 <= speed <= 91) != (speed >= 12 <= 91):
        triggered.add(80)
    # 变异规则 112 - CSR
    if (12 <= speed <= 91) != (12 <= speed <= -91):
        triggered.add(81)
    # 变异规则 113 - UOI
    if (12 <= speed <= 91) != (12 <= -speed <= 91):
        triggered.add(82)
    # 变异规则 114 - RSR
    if (12 <= speed <= 91) != (not (12 <= speed <= 91)):
        triggered.add(83)
    # 变异规则 115 - CRP
    if (12 <= speed <= 91) != (12 <= speed <= 94):
        triggered.add(84)
    # 变异规则 116 - AOR
    if (12 <= speed <= 91) != (not (12 <= speed <= 91)):
        triggered.add(85)
    # 变异规则 117 - ABS
    if (12 <= speed <= 91) != (12 <= abs(speed) <= 91):
        t = 1
    # 变异规则 118 - CAR
    if (12 <= speed <= 91) != (12 <= speed <= 86):
        triggered.add(86)
    # 变异规则 119 - LCR
    if (12 <= speed <= 91) != (not (12 <= speed <= 91)):
        triggered.add(87)
    # 变异规则 120 - SCR
    if (12 <= speed <= 91) != (speed >= 12 <= 91):
        triggered.add(88)
    # 原语句
    if 12 <= speed <= 91:
        health_score -= 2
        speed = min(speed + 3, 100)
    # 原语句13
    # 变异规则 121 - AOR
    if (voltage_mv >= 10) != (voltage_mv >= 12):
        triggered.add(89)
    # 变异规则 122 - CAR
    if (voltage_mv >= 10) != (voltage_mv >= 11):
        triggered.add(90)
    # 变异规则 123 - SCR
    if (voltage_mv >= 10) != (not (voltage_mv >= 10)):
        triggered.add(91)
    # 变异规则 124 - CRP
    if (voltage_mv >= 10) != (voltage_mv >= 5):
        triggered.add(92)
    # 变异规则 125 - UOI
    if (voltage_mv >= 10) != (voltage_mv >= -10):
        triggered.add(93)
    # 变异规则 126 - SRC
    if (voltage_mv >= 10) != (not (voltage_mv >= 10)):
        triggered.add(94)
    # 变异规则 127 - ABS
    if (voltage_mv >= 10) != (abs(voltage_mv) >= 10):
        t = 1
    # 变异规则 128 - SAR
    if (voltage_mv >= 10) != (10 <= voltage_mv):
        t = 1
    # 变异规则 129 - LCR
    if (voltage_mv >= 10) != (not (voltage_mv >= 10)):
        triggered.add(95)
    # 变异规则 130 - RSR
    if (voltage_mv >= 10) != (not (voltage_mv >= 10)):
        triggered.add(96)
    # 原语句
    if voltage_mv >= 10:
        health_score += 2
        speed = min(speed + 6, 100)
        voltage_mv = min(voltage_mv + 7, 100)
    # 原语句14
    # 变异规则 131 - AOR
    if (88 <= altitude <= 590) != (88 <= -altitude <= 590):
        triggered.add(97)
    # 变异规则 132 - CAR
    if (88 <= altitude <= 590) != (93 <= altitude <= 590):
        triggered.add(98)
    # 变异规则 133 - SAR
    if (88 <= altitude <= 590) != (altitude >= 88 <= 590):
        triggered.add(99)
    # 变异规则 134 - RSR
    if (88 <= altitude <= 590) != (not (88 <= altitude <= 590)):
        triggered.add(100)
    # 变异规则 135 - CRP
    if (88 <= altitude <= 590) != (176 <= altitude <= 590):
        triggered.add(101)
    # 变异规则 136 - LCR
    if (88 <= altitude <= 590) != (not (88 <= altitude <= 590)):
        triggered.add(102)
    # 变异规则 137 - UOI
    if (88 <= altitude <= 590) != (88 <= -altitude <= 590):
        triggered.add(103)
    # 变异规则 138 - ABS
    if (88 <= altitude <= 590) != (88 <= abs(altitude) <= 590):
        t = 1
    # 变异规则 139 - SCR
    if (88 <= altitude <= 590) != (not (88) <= altitude <= 590):
        triggered.add(104)
    # 变异规则 140 - ROR
    if (88 <= altitude <= 590) != (88 <= altitude <= -590):
        triggered.add(105)
    # 原语句
    if 88 <= altitude <= 590:
        health_score -= 26
        speed = min(speed + 6, 100)
    # 原语句15
    # 变异规则 141 - SVR
    if (altitude < 200 or voltage_mv == 100) != (speed < 200 or voltage_mv == 100):
        triggered.add(106)
    # 变异规则 142 - ABS
    if (altitude < 200 or voltage_mv == 100) != (abs(altitude) < 200 or voltage_mv == 100):
        t = 1
    # 变异规则 143 - CSR
    if (altitude < 200 or voltage_mv == 100) != (altitude < -200 or voltage_mv == 100):
        triggered.add(107)
    # 变异规则 144 - CAR
    if (altitude < 200 or voltage_mv == 100) != (altitude < 205 or voltage_mv == 100):
        triggered.add(108)
    # 变异规则 145 - SAR
    if (altitude < 200 or voltage_mv == 100) != (200 > altitude or voltage_mv == 100):
        t = 1
    # 变异规则 146 - SRC
    if (altitude < 200 or voltage_mv == 100) != (voltage_mv == 100 or altitude < 200):
        t = 1
    # 变异规则 147 - AOR
    if (altitude < 200 or voltage_mv == 100) != (altitude < 200 or voltage_mv == 200):
        triggered.add(109)
    # 变异规则 148 - LCR
    if (altitude < 200 or voltage_mv == 100) != (altitude < 200 and voltage_mv == 100):
        triggered.add(110)
    # 变异规则 149 - ROR
    if (altitude < 200 or voltage_mv == 100) != (not (altitude < 200 or voltage_mv == 100)):
        triggered.add(111)
    # 变异规则 150 - CRP
    if (altitude < 200 or voltage_mv == 100) != (altitude < 200 or voltage_mv == 50):
        triggered.add(112)
    # 原语句
    if altitude < 200 or voltage_mv == 100:
        health_score -= 6
        speed = max(speed - 5, 2)
        voltage_mv, speed = speed, voltage_mv
    # 原语句16
    # 变异规则 151 - SVR
    if (voltage_mv <= 100 and speed > 30) != (altitude <= 100 and speed > 30):
        triggered.add(113)
    # 变异规则 152 - CRP
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= 200 and speed > 30):
        t = 1
    # 变异规则 153 - ABS
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and abs(speed) > 30):
        t = 1
    # 变异规则 154 - AOR
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and speed > 20):
        triggered.add(114)
    # 变异规则 155 - SAR
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and 30 < speed):
        t = 1
    # 变异规则 156 - ROR
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and speed > -30):
        triggered.add(115)
    # 变异规则 157 - UOI
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and -speed > 30):
        triggered.add(116)
    # 变异规则 158 - LCR
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 or speed > 30):
        triggered.add(117)
    # 变异规则 159 - SRC
    if (voltage_mv <= 100 and speed > 30) != (speed > 30 and voltage_mv <= 100):
        t = 1
    # 变异规则 160 - CSR
    if (voltage_mv <= 100 and speed > 30) != (voltage_mv <= -100 and speed > 30):
        triggered.add(118)
    # 原语句
    if voltage_mv <= 100 and speed > 30:
        health_score -= 4
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句17
    # 变异规则 161 - LCR
    if (18 <= voltage_mv <= 95) != (18 <= voltage_mv <= 96):
        triggered.add(119)
    # 变异规则 162 - SVR
    if (18 <= voltage_mv <= 95) != (18 <= speed <= 95):
        triggered.add(120)
    # 变异规则 163 - ABS
    if (18 <= voltage_mv <= 95) != (18 <= abs(voltage_mv) <= 95):
        t = 1
    # 变异规则 164 - SCR
    if (18 <= voltage_mv <= 95) != (18 <= abs(voltage_mv) <= 95):
        t = 1
    # 变异规则 165 - CRP
    if (18 <= voltage_mv <= 95) != (18 <= voltage_mv <= 101):
        triggered.add(121)
    # 变异规则 166 - CAR
    if (18 <= voltage_mv <= 95) != (8 <= voltage_mv <= 95):
        triggered.add(122)
    # 变异规则 167 - SAR
    if (18 <= voltage_mv <= 95) != (voltage_mv >= 18 <= 95):
        triggered.add(123)
    # 变异规则 168 - CSR
    if (18 <= voltage_mv <= 95) != (-18 <= voltage_mv <= 95):
        triggered.add(124)
    # 变异规则 169 - UOI
    if (18 <= voltage_mv <= 95) != (18 <= -voltage_mv <= 95):
        triggered.add(125)
    # 变异规则 170 - SRC
    if (18 <= voltage_mv <= 95) != (18 <= -voltage_mv <= 95):
        triggered.add(126)
    # 原语句
    if 18 <= voltage_mv <= 95:
        health_score += 5
        altitude = max(altitude - 34, 2)
        voltage_mv = min(voltage_mv + 2, 100)
        voltage_mv, speed = speed, voltage_mv
    # 原语句18
    # 变异规则 171 - SVR
    if (18 <= voltage_mv <= 71) != (18 <= altitude <= 71):
        triggered.add(127)
    # 变异规则 172 - SAR
    if (18 <= voltage_mv <= 71) != (voltage_mv >= 18 <= 71):
        triggered.add(128)
    # 变异规则 173 - UOI
    if (18 <= voltage_mv <= 71) != (18 <= -voltage_mv <= 71):
        triggered.add(129)
    # 变异规则 174 - CAR
    if (18 <= voltage_mv <= 71) != (18 <= voltage_mv <= 76):
        triggered.add(130)
    # 变异规则 175 - SRC
    if (18 <= voltage_mv <= 71) != (18 <= -voltage_mv <= 71):
        triggered.add(131)
    # 变异规则 176 - CSR
    if (18 <= voltage_mv <= 71) != (18 <= voltage_mv <= -71):
        triggered.add(132)
    # 变异规则 177 - RSR
    if (18 <= voltage_mv <= 71) != (not (18 <= voltage_mv <= 71)):
        triggered.add(133)
    # 变异规则 178 - ROR
    if (18 <= voltage_mv <= 71) != (36 <= voltage_mv <= 71):
        triggered.add(134)
    # 变异规则 179 - AOR
    if (18 <= voltage_mv <= 71) != (voltage_mv >= 18 <= 71):
        triggered.add(135)
    # 变异规则 180 - SCR
    if (18 <= voltage_mv <= 71) != (not (18) <= voltage_mv <= 71):
        triggered.add(136)
    # 原语句
    if 18 <= voltage_mv <= 71:
        health_score -= 18
        voltage_mv = min(voltage_mv + 7, 100)
    # 原语句19
    # 变异规则 181 - LCR
    if (speed != altitude - 50) != (speed != altitude - -50):
        triggered.add(137)
    # 变异规则 182 - RSR
    if (speed != altitude - 50) != (not (speed != altitude - 50)):
        triggered.add(138)
    # 变异规则 183 - CAR
    if (speed != altitude - 50) != (speed != altitude - 45):
        triggered.add(139)
    # 变异规则 184 - ABS
    if (speed != altitude - 50) != (speed != abs(altitude) - 50):
        t = 1
    # 变异规则 185 - SCR
    if (speed != altitude - 50) != (speed != altitude - 53):
        triggered.add(140)
    # 变异规则 186 - SVR
    if (speed != altitude - 50) != (altitude != altitude - 50):
        triggered.add(141)
    # 变异规则 187 - CSR
    if (speed != altitude - 50) != (speed != altitude - -50):
        triggered.add(142)
    # 变异规则 188 - SRC
    if (speed != altitude - 50) != (speed != altitude - -50):
        triggered.add(143)
    # 变异规则 189 - UOI
    if (speed != altitude - 50) != (speed != -altitude - 50):
        triggered.add(144)
    # 变异规则 190 - SAR
    if (speed != altitude - 50) != (altitude != speed - 50):
        triggered.add(145)
    # 原语句
    if speed != altitude - 50:
        health_score -= 1
    # 原语句20
    # 变异规则 191 - ABS
    if (altitude == speed * 1000) != (abs(altitude) == speed * 1000):
        t = 1
    # 变异规则 192 - SRC
    if (altitude == speed * 1000) != (speed == speed * 1000):
        t = 1
    # 变异规则 193 - SVR
    if (altitude == speed * 1000) != (voltage_mv == speed * 1000):
        t = 1
    # 变异规则 194 - AOR
    if (altitude == speed * 1000) != (altitude == speed * -1000):
        t = 1
    # 变异规则 195 - ROR
    if (altitude == speed * 1000) != (altitude == speed * 1005):
        t = 1
    # 变异规则 196 - CRP
    if (altitude == speed * 1000) != (altitude == speed * 2000):
        t = 1
    # 变异规则 197 - UOI
    if (altitude == speed * 1000) != (altitude == -speed * 1000):
        t = 1
    # 变异规则 198 - CAR
    if (altitude == speed * 1000) != (altitude == speed * 999):
        t = 1
    # 变异规则 199 - RSR
    if (altitude == speed * 1000) != (not (altitude == speed * 1000)):
        triggered.add(146)
    # 变异规则 200 - SCR
    if (altitude == speed * 1000) != (altitude == speed * -1000):
        t = 1
    # 原语句
    if altitude == speed * 1000:
        health_score += 2
    # 原语句21
    # 变异规则 201 - ROR
    if (altitude <= 20 or speed == 20) != (speed <= 20 or speed == 20):
        triggered.add(147)
    # 变异规则 202 - CSR
    if (altitude <= 20 or speed == 20) != (altitude <= -20 or speed == 20):
        triggered.add(148)
    # 变异规则 203 - RSR
    if (altitude <= 20 or speed == 20) != (not (altitude <= 20 or speed == 20)):
        triggered.add(149)
    # 变异规则 204 - SAR
    if (altitude <= 20 or speed == 20) != (20 >= altitude or speed == 20):
        t = 1
    # 变异规则 205 - CAR
    if (altitude <= 20 or speed == 20) != (altitude <= 20 or speed == 30):
        triggered.add(150)
    # 变异规则 206 - SRC
    if (altitude <= 20 or speed == 20) != (speed == 20 or altitude <= 20):
        t = 1
    # 变异规则 207 - ABS
    if (altitude <= 20 or speed == 20) != (abs(altitude) <= 20 or speed == 20):
        t = 1
    # 变异规则 208 - AOR
    if (altitude <= 20 or speed == 20) != (altitude <= 20 or speed == 19):
        triggered.add(151)
    # 变异规则 209 - LCR
    if (altitude <= 20 or speed == 20) != (altitude <= 20 and speed == 20):
        triggered.add(152)
    # 变异规则 210 - CRP
    if (altitude <= 20 or speed == 20) != (altitude <= 20 or speed == 19):
        triggered.add(153)
    # 原语句
    if altitude <= 20 or speed == 20:
        health_score += 10
    # 原语句22
    # 变异规则 211 - UOI
    if (voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == 85 and -voltage_mv <= 100):
        t = 1
    # 变异规则 212 - AOR
    if (voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == 95 and voltage_mv <= 100):
        triggered.add(154)
    # 变异规则 213 - RSR
    if (voltage_mv == 85 and voltage_mv <= 100) != (not (voltage_mv == 85 and voltage_mv <= 100)):
        triggered.add(155)
    # 变异规则 214 - CRP
    if (voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == 85 and voltage_mv <= 200):
        t = 1
    # 变异规则 215 - ABS
    if (voltage_mv == 85 and voltage_mv <= 100) != (abs(voltage_mv) == 85 and voltage_mv <= 100):
        t = 1
    # 变异规则 216 - SVR
    if (voltage_mv == 85 and voltage_mv <= 100) != (altitude == 85 and voltage_mv <= 100):
        triggered.add(156)
    # 变异规则 217 - SCR
    if (voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == 85 and voltage_mv <= 102):
        t = 1
    # 变异规则 218 - CAR
    if (voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == 86 and voltage_mv <= 100):
        triggered.add(157)
    # 变异规则 219 - SRC
    if (voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv <= 100 and voltage_mv == 85):
        t = 1
    # 变异规则 220 - CSR
    if (voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == -85 and voltage_mv <= 100):
        triggered.add(158)
    # 原语句
    if voltage_mv == 85 and voltage_mv <= 100:
        health_score -= 29
        altitude = max(altitude - 8, 2)
    # 原语句23
    # 变异规则 221 - LCR
    if (5 <= speed <= 48) != (speed >= 5 <= 48):
        triggered.add(159)
    # 变异规则 222 - CAR
    if (5 <= speed <= 48) != (7 <= speed <= 48):
        triggered.add(160)
    # 变异规则 223 - SAR
    if (5 <= speed <= 48) != (speed >= 5 <= 48):
        triggered.add(161)
    # 变异规则 224 - AOR
    if (5 <= speed <= 48) != (1 <= speed <= 48):
        triggered.add(162)
    # 变异规则 225 - CRP
    if (5 <= speed <= 48) != (10 <= speed <= 48):
        triggered.add(163)
    # 变异规则 226 - RSR
    if (5 <= speed <= 48) != (not (5 <= speed <= 48)):
        triggered.add(164)
    # 变异规则 227 - ABS
    if (5 <= speed <= 48) != (5 <= abs(speed) <= 48):
        t = 1
    # 变异规则 228 - UOI
    if (5 <= speed <= 48) != (5 <= -speed <= 48):
        triggered.add(165)
    # 变异规则 229 - ROR
    if (5 <= speed <= 48) != (5 <= -speed <= 48):
        triggered.add(166)
    # 变异规则 230 - CSR
    if (5 <= speed <= 48) != (5 <= speed <= -48):
        triggered.add(167)
    # 原语句
    if 5 <= speed <= 48:
        health_score += 15
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句24
    # 变异规则 231 - UOI
    if (voltage_mv > 30 or speed == 10) != (voltage_mv > 30 or -speed == 10):
        t = 1
    # 变异规则 232 - LCR
    if (voltage_mv > 30 or speed == 10) != (voltage_mv > 30 and speed == 10):
        triggered.add(168)
    # 变异规则 233 - AOR
    if (voltage_mv > 30 or speed == 10) != (voltage_mv > 30 or -speed == 10):
        t = 1
    # 变异规则 234 - CAR
    if (voltage_mv > 30 or speed == 10) != (voltage_mv > 25 or speed == 10):
        triggered.add(169)
    # 变异规则 235 - CRP
    if (voltage_mv > 30 or speed == 10) != (voltage_mv > 30 or speed == 5):
        t = 1
    # 变异规则 236 - SCR
    if (voltage_mv > 30 or speed == 10) != (voltage_mv > 30 or -speed == 10):
        t = 1
    # 变异规则 237 - SAR
    if (voltage_mv > 30 or speed == 10) != (30 < voltage_mv or speed == 10):
        t = 1
    # 变异规则 238 - RSR
    if (voltage_mv > 30 or speed == 10) != (not (voltage_mv > 30 or speed == 10)):
        triggered.add(170)
    # 变异规则 239 - SRC
    if (voltage_mv > 30 or speed == 10) != (speed == 10 or voltage_mv > 30):
        t = 1
    # 变异规则 240 - CSR
    if (voltage_mv > 30 or speed == 10) != (voltage_mv > -30 or speed == 10):
        triggered.add(171)
    # 原语句
    if voltage_mv > 30 or speed == 10:
        health_score -= 14
        voltage_mv = min(voltage_mv + 5, 100)
    # 原语句25
    # 变异规则 241 - LCR
    if (5 <= voltage_mv <= 88) != (5 <= abs(voltage_mv) <= 88):
        t = 1
    # 变异规则 242 - SCR
    if (5 <= voltage_mv <= 88) != (not (5) <= voltage_mv <= 88):
        triggered.add(172)
    # 变异规则 243 - SAR
    if (5 <= voltage_mv <= 88) != (voltage_mv >= 5 <= 88):
        triggered.add(173)
    # 变异规则 244 - SRC
    if (5 <= voltage_mv <= 88) != (-5 <= voltage_mv <= 88):
        triggered.add(174)
    # 变异规则 245 - CSR
    if (5 <= voltage_mv <= 88) != (5 <= voltage_mv <= -88):
        triggered.add(175)
    # 变异规则 246 - UOI
    if (5 <= voltage_mv <= 88) != (5 <= -voltage_mv <= 88):
        triggered.add(176)
    # 变异规则 247 - ABS
    if (5 <= voltage_mv <= 88) != (5 <= abs(voltage_mv) <= 88):
        t = 1
    # 变异规则 248 - AOR
    if (5 <= voltage_mv <= 88) != (5 <= voltage_mv <= -88):
        triggered.add(177)
    # 变异规则 249 - RSR
    if (5 <= voltage_mv <= 88) != (not (5 <= voltage_mv <= 88)):
        triggered.add(178)
    # 变异规则 250 - SVR
    if (5 <= voltage_mv <= 88) != (5 <= altitude <= 88):
        triggered.add(179)
    # 原语句
    if 5 <= voltage_mv <= 88:
        health_score += 5
        altitude = min(altitude + 43, 1000)
        speed = max(speed - 9, 2)
        speed, voltage_mv = voltage_mv, speed
    # 原语句26
    # 变异规则 251 - SVR
    if (speed == 30) != (voltage_mv == 30):
        triggered.add(180)
    # 变异规则 252 - CRP
    if (speed == 30) != (speed == 60):
        triggered.add(181)
    # 变异规则 253 - CSR
    if (speed == 30) != (speed == -30):
        triggered.add(182)
    # 变异规则 254 - ABS
    if (speed == 30) != (abs(speed) == 30):
        t = 1
    # 变异规则 255 - SCR
    if (speed == 30) != (30 == speed):
        t = 1
    # 变异规则 256 - ROR
    if (speed == 30) != (voltage_mv == 30):
        triggered.add(183)
    # 变异规则 257 - SRC
    if (speed == 30) != (altitude == 30):
        triggered.add(184)
    # 变异规则 258 - CAR
    if (speed == 30) != (speed == 40):
        triggered.add(185)
    # 变异规则 259 - LCR
    if (speed == 30) != (30 == speed):
        t = 1
    # 变异规则 260 - AOR
    if (speed == 30) != (altitude == 30):
        triggered.add(186)
    # 原语句
    if speed == 30:
        health_score += 12
        speed = max(speed - 8, 2)
        altitude, speed = speed, altitude
    # 原语句27
    # 变异规则 261 - SRC
    if (271 <= altitude <= 907) != (271 <= altitude <= 1814):
        triggered.add(187)
    # 变异规则 262 - CSR
    if (271 <= altitude <= 907) != (271 <= altitude <= -907):
        triggered.add(188)
    # 变异规则 263 - LCR
    if (271 <= altitude <= 907) != (-271 <= altitude <= 907):
        triggered.add(189)
    # 变异规则 264 - ABS
    if (271 <= altitude <= 907) != (271 <= abs(altitude) <= 907):
        t = 1
    # 变异规则 265 - RSR
    if (271 <= altitude <= 907) != (not (271 <= altitude <= 907)):
        triggered.add(190)
    # 变异规则 266 - CRP
    if (271 <= altitude <= 907) != (542 <= altitude <= 907):
        triggered.add(191)
    # 变异规则 267 - SVR
    if (271 <= altitude <= 907) != (271 <= speed <= 907):
        triggered.add(192)
    # 变异规则 268 - SCR
    if (271 <= altitude <= 907) != (271 <= altitude <= 1814):
        triggered.add(193)
    # 变异规则 269 - ROR
    if (271 <= altitude <= 907) != (271 <= voltage_mv <= 907):
        triggered.add(194)
    # 变异规则 270 - AOR
    if (271 <= altitude <= 907) != (271 <= -altitude <= 907):
        triggered.add(195)
    # 原语句
    if 271 <= altitude <= 907:
        health_score += 8
        speed = max(speed - 10, 2)
        voltage_mv = max(voltage_mv - 10, 2)
    # 原语句28
    # 变异规则 271 - CRP
    if (speed != 20) != (speed != 40):
        triggered.add(196)
    # 变异规则 272 - SRC
    if (speed != 20) != (not (speed != 20)):
        triggered.add(197)
    # 变异规则 273 - SCR
    if (speed != 20) != (speed != 23):
        triggered.add(198)
    # 变异规则 274 - CSR
    if (speed != 20) != (speed != -20):
        triggered.add(199)
    # 变异规则 275 - AOR
    if (speed != 20) != (speed != 19):
        triggered.add(200)
    # 变异规则 276 - UOI
    if (speed != 20) != (speed != -20):
        triggered.add(201)
    # 变异规则 277 - CAR
    if (speed != 20) != (speed != 22):
        triggered.add(202)
    # 变异规则 278 - ROR
    if (speed != 20) != (speed != -20):
        triggered.add(203)
    # 变异规则 279 - LCR
    if (speed != 20) != (not (speed != 20)):
        triggered.add(204)
    # 变异规则 280 - SVR
    if (speed != 20) != (voltage_mv != 20):
        triggered.add(205)
    # 原语句
    if speed != 20:
        health_score += 1
        altitude = min(altitude + 53, 1000)
        speed = min(speed + 10, 100)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句29
    # 变异规则 281 - CRP
    if (voltage_mv < 50) != (voltage_mv < 55):
        t = 1
    # 变异规则 282 - RSR
    if (voltage_mv < 50) != (not (voltage_mv < 50)):
        triggered.add(206)
    # 变异规则 283 - AOR
    if (voltage_mv < 50) != (voltage_mv < 55):
        t = 1
    # 变异规则 284 - ROR
    if (voltage_mv < 50) != (not (voltage_mv < 50)):
        triggered.add(207)
    # 变异规则 285 - SRC
    if (voltage_mv < 50) != (not (voltage_mv < 50)):
        triggered.add(208)
    # 变异规则 286 - ABS
    if (voltage_mv < 50) != (abs(voltage_mv) < 50):
        t = 1
    # 变异规则 287 - CSR
    if (voltage_mv < 50) != (voltage_mv < -50):
        triggered.add(209)
    # 变异规则 288 - SVR
    if (voltage_mv < 50) != (altitude < 50):
        triggered.add(210)
    # 变异规则 289 - LCR
    if (voltage_mv < 50) != (50 > voltage_mv):
        t = 1
    # 变异规则 290 - SAR
    if (voltage_mv < 50) != (50 > voltage_mv):
        t = 1
    # 原语句
    if voltage_mv < 50:
        health_score -= 28
    # 原语句30
    # 变异规则 291 - LCR
    if (voltage_mv < 100 or speed < 5) != (voltage_mv < 100 and speed < 5):
        triggered.add(211)
    # 变异规则 292 - RSR
    if (voltage_mv < 100 or speed < 5) != (not (voltage_mv < 100 or speed < 5)):
        triggered.add(212)
    # 变异规则 293 - SVR
    if (voltage_mv < 100 or speed < 5) != (altitude < 100 or speed < 5):
        triggered.add(213)
    # 变异规则 294 - CRP
    if (voltage_mv < 100 or speed < 5) != (voltage_mv < 50 or speed < 5):
        triggered.add(214)
    # 变异规则 295 - AOR
    if (voltage_mv < 100 or speed < 5) != (100 > voltage_mv or speed < 5):
        t = 1
    # 变异规则 296 - CAR
    if (voltage_mv < 100 or speed < 5) != (voltage_mv < 90 or speed < 5):
        triggered.add(215)
    # 变异规则 297 - ABS
    if (voltage_mv < 100 or speed < 5) != (voltage_mv < 100 or abs(speed) < 5):
        t = 1
    # 变异规则 298 - CSR
    if (voltage_mv < 100 or speed < 5) != (voltage_mv < -100 or speed < 5):
        triggered.add(216)
    # 变异规则 299 - UOI
    if (voltage_mv < 100 or speed < 5) != (voltage_mv < 100 or -speed < 5):
        triggered.add(217)
    # 变异规则 300 - SCR
    if (voltage_mv < 100 or speed < 5) != (not (voltage_mv < 100 or speed < 5)):
        triggered.add(218)
    # 原语句
    if voltage_mv < 100 or speed < 5:
        health_score -= 7
        speed = min(speed + 6, 100)
        voltage_mv = min(voltage_mv + 1, 100)
        altitude, speed = speed, altitude
    return triggered

targetPaths = [
    {2, 3, 14, 17, 21, 22, 23, 27, 35, 36, 44, 46, 50, 59, 60, 63, 67, 68, 71, 78, 79, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 120, 124, 127, 133, 136, 138, 146, 147, 149, 155, 164, 165, 167, 168, 170, 172, 175, 176, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 215, 216},
    {2, 3, 14, 17, 21, 22, 23, 27, 35, 36, 44, 46, 50, 60, 63, 67, 68, 71, 78, 79, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 120, 124, 127, 133, 136, 138, 146, 147, 149, 155, 164, 165, 167, 168, 170, 172, 175, 176, 178, 179, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 14, 17, 18, 23, 27, 35, 36, 44, 46, 50, 60, 63, 67, 68, 71, 78, 79, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 120, 124, 127, 133, 136, 138, 146, 147, 149, 155, 164, 165, 167, 168, 170, 172, 175, 176, 178, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 6, 7, 8, 9, 11, 14, 17, 18, 23, 27, 35, 36, 44, 46, 50, 60, 63, 67, 68, 71, 78, 79, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 120, 122, 124, 127, 133, 136, 138, 146, 147, 149, 155, 164, 165, 167, 168, 170, 172, 175, 176, 178, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 7, 8, 9, 11, 14, 17, 18, 23, 27, 35, 36, 44, 46, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 120, 122, 124, 127, 133, 136, 138, 146, 147, 149, 155, 164, 165, 167, 168, 170, 172, 175, 176, 178, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 8, 9, 11, 14, 17, 23, 27, 35, 36, 44, 46, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 149, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 196, 197, 198, 199, 200, 202, 205, 206, 209, 211, 212, 216},
    {2, 3, 8, 9, 11, 14, 17, 23, 27, 35, 36, 44, 46, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 8, 9, 11, 14, 17, 23, 27, 35, 36, 44, 46, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 180, 181, 182, 184, 185, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 8, 9, 11, 14, 17, 23, 27, 35, 36, 42, 44, 46, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 8, 9, 11, 14, 17, 23, 27, 35, 36, 42, 44, 46, 47, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {1, 2, 3, 4, 8, 9, 11, 14, 17, 23, 27, 35, 36, 42, 44, 46, 47, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 4, 8, 9, 11, 14, 17, 23, 27, 35, 36, 42, 44, 46, 47, 50, 55, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 4, 8, 9, 11, 14, 17, 23, 27, 35, 36, 40, 41, 45, 46, 50, 55, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 185, 189, 190, 196, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 4, 8, 9, 11, 14, 17, 23, 27, 35, 36, 40, 41, 45, 46, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 215, 216},
    {2, 3, 4, 8, 9, 11, 14, 17, 23, 27, 35, 36, 40, 41, 45, 46, 50, 58, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 215, 216},
    {2, 3, 4, 8, 9, 11, 14, 17, 23, 27, 35, 36, 40, 41, 45, 46, 50, 58, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 137, 138, 145, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 215, 216},
    {2, 3, 4, 8, 9, 11, 14, 15, 17, 19, 22, 23, 27, 35, 36, 40, 41, 45, 46, 50, 60, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 215, 216},
    {2, 3, 4, 8, 9, 11, 14, 15, 17, 19, 22, 23, 27, 35, 36, 40, 41, 45, 46, 50, 54, 55, 57, 58, 59, 60, 62, 63, 68, 71, 75, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 4, 8, 9, 11, 12, 14, 15, 17, 19, 22, 23, 27, 35, 36, 40, 41, 46, 50, 60, 63, 68, 71, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 4, 10, 14, 15, 17, 19, 22, 23, 27, 35, 36, 40, 41, 46, 50, 60, 63, 68, 71, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 4, 14, 15, 17, 19, 22, 23, 27, 35, 36, 46, 48, 50, 60, 63, 68, 71, 78, 79, 81, 82, 83, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 4, 14, 15, 17, 19, 22, 23, 27, 35, 36, 46, 48, 50, 60, 63, 68, 71, 78, 79, 81, 82, 83, 86, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 4, 14, 15, 17, 19, 22, 23, 27, 35, 36, 46, 48, 50, 60, 63, 68, 71, 78, 79, 80, 83, 84, 89, 91, 100, 104, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 8, 14, 17, 21, 22, 23, 27, 35, 36, 44, 46, 50, 59, 60, 63, 67, 68, 72, 75, 76, 77, 78, 79, 83, 91, 100, 104, 107, 110, 111, 116, 118, 120, 122, 124, 133, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 9, 11, 14, 17, 23, 27, 35, 36, 44, 46, 50, 60, 63, 68, 72, 76, 77, 78, 79, 81, 82, 83, 91, 100, 104, 107, 110, 111, 116, 118, 120, 122, 124, 127, 133, 136, 138, 146, 149, 155, 164, 165, 167, 169, 170, 171, 172, 175, 176, 178, 180, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 4, 9, 11, 14, 17, 23, 27, 35, 36, 40, 41, 45, 46, 50, 60, 63, 68, 72, 76, 77, 78, 79, 81, 82, 83, 91, 92, 93, 100, 104, 107, 110, 111, 115, 117, 120, 125, 133, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 211, 212, 214, 216},
    {2, 3, 4, 8, 14, 15, 17, 19, 22, 23, 27, 35, 36, 46, 48, 50, 60, 63, 68, 72, 75, 76, 77, 78, 79, 81, 82, 83, 91, 100, 104, 107, 110, 111, 116, 118, 120, 122, 124, 133, 136, 137, 138, 139, 140, 141, 144, 145, 146, 149, 155, 164, 165, 167, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 214, 216},
    {2, 3, 4, 8, 14, 15, 17, 19, 22, 23, 27, 35, 36, 46, 48, 50, 60, 63, 68, 72, 75, 76, 77, 78, 79, 81, 82, 83, 91, 100, 104, 107, 110, 111, 116, 118, 125, 129, 132, 133, 136, 138, 146, 149, 150, 151, 152, 155, 164, 165, 167, 168, 170, 172, 175, 176, 178, 181, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 8, 14, 17, 21, 23, 27, 35, 36, 44, 46, 50, 60, 63, 67, 68, 73, 74, 78, 79, 83, 91, 100, 104, 107, 110, 111, 116, 118, 125, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 8, 14, 15, 17, 19, 23, 27, 35, 36, 40, 41, 46, 50, 60, 63, 68, 73, 74, 78, 79, 81, 82, 83, 91, 100, 104, 107, 110, 111, 116, 118, 120, 122, 124, 133, 136, 138, 146, 149, 155, 156, 159, 164, 170, 171, 172, 175, 176, 178, 189, 190, 197, 206, 212, 213, 217},
    {2, 3, 14, 17, 21, 23, 27, 35, 36, 44, 46, 50, 60, 63, 67, 68, 73, 78, 79, 83, 91, 100, 104, 107, 110, 111, 116, 118, 125, 128, 133, 136, 138, 146, 147, 148, 149, 152, 154, 155, 156, 157, 158, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 14, 17, 21, 23, 27, 35, 36, 44, 46, 50, 60, 63, 64, 66, 67, 68, 73, 78, 79, 83, 91, 100, 104, 111, 116, 118, 120, 125, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 14, 17, 21, 23, 27, 29, 35, 36, 44, 46, 50, 60, 63, 64, 66, 67, 68, 73, 78, 79, 83, 91, 100, 104, 111, 116, 118, 120, 125, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 174, 178, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 4, 8, 10, 14, 15, 17, 19, 22, 23, 27, 35, 36, 40, 41, 46, 50, 60, 63, 68, 72, 75, 76, 77, 78, 79, 81, 82, 83, 89, 90, 91, 100, 104, 107, 110, 111, 115, 117, 120, 125, 133, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 4, 8, 10, 14, 15, 17, 19, 22, 23, 27, 29, 35, 36, 40, 41, 46, 50, 60, 63, 68, 72, 75, 76, 77, 78, 79, 81, 82, 83, 91, 100, 104, 107, 110, 111, 114, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 169, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 211, 212, 214, 215, 216},
    {2, 3, 8, 14, 17, 21, 22, 23, 27, 29, 35, 36, 44, 46, 50, 60, 63, 67, 68, 72, 75, 76, 77, 78, 79, 83, 91, 100, 104, 107, 110, 111, 116, 118, 125, 128, 130, 133, 136, 138, 146, 149, 155, 164, 165, 167, 170, 171, 172, 174, 178, 179, 189, 190, 196, 197, 198, 199, 200, 202, 205, 206, 209, 210, 211, 212, 216},
    {2, 3, 14, 17, 21, 22, 23, 27, 29, 35, 36, 44, 46, 50, 59, 60, 63, 67, 68, 71, 78, 79, 83, 89, 91, 97, 98, 100, 101, 104, 105, 107, 110, 111, 115, 117, 120, 122, 124, 133, 136, 138, 146, 147, 149, 155, 164, 165, 167, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 214, 216},
    {2, 3, 8, 14, 17, 21, 23, 27, 29, 35, 36, 44, 46, 50, 60, 63, 67, 68, 73, 74, 78, 79, 83, 91, 97, 100, 101, 104, 105, 107, 110, 111, 116, 118, 119, 120, 121, 123, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 8, 14, 17, 21, 23, 27, 29, 35, 36, 44, 46, 50, 60, 63, 67, 68, 73, 74, 78, 79, 83, 91, 97, 100, 101, 104, 105, 107, 110, 111, 113, 116, 118, 120, 121, 123, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 14, 17, 21, 23, 27, 29, 30, 35, 36, 44, 46, 50, 60, 63, 67, 68, 73, 78, 79, 83, 91, 97, 100, 101, 104, 105, 107, 110, 111, 113, 116, 118, 123, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 4, 14, 15, 17, 22, 23, 25, 27, 29, 35, 36, 46, 48, 50, 60, 63, 68, 71, 78, 79, 80, 83, 89, 91, 97, 100, 101, 104, 105, 107, 110, 111, 115, 117, 125, 127, 129, 132, 133, 134, 136, 138, 146, 149, 155, 159, 164, 170, 171, 172, 175, 176, 178, 179, 189, 190, 197, 206, 212, 213, 217},
    {2, 3, 14, 17, 21, 24, 25, 26, 27, 35, 36, 44, 46, 50, 60, 63, 67, 68, 73, 78, 79, 83, 91, 97, 100, 101, 104, 105, 111, 116, 118, 121, 123, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 14, 17, 21, 22, 23, 27, 29, 33, 35, 36, 44, 46, 50, 59, 60, 63, 67, 68, 71, 78, 79, 83, 89, 91, 97, 100, 104, 105, 107, 110, 111, 115, 117, 120, 122, 124, 133, 136, 138, 146, 147, 149, 155, 164, 165, 167, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 14, 17, 21, 22, 23, 27, 29, 32, 34, 35, 44, 46, 50, 60, 63, 67, 68, 70, 71, 78, 79, 83, 91, 93, 97, 100, 104, 105, 107, 110, 111, 115, 117, 124, 133, 136, 138, 146, 147, 149, 155, 162, 164, 170, 171, 172, 174, 178, 189, 190, 197, 206, 210, 212, 213, 217},
    {2, 3, 8, 14, 17, 21, 22, 23, 27, 29, 32, 34, 35, 44, 46, 50, 60, 63, 67, 68, 70, 71, 78, 79, 83, 91, 92, 93, 97, 100, 104, 105, 107, 110, 111, 115, 117, 124, 133, 136, 138, 146, 147, 149, 155, 160, 163, 164, 165, 167, 168, 170, 172, 173, 178, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 14, 17, 21, 22, 23, 27, 29, 32, 34, 35, 44, 46, 50, 60, 63, 67, 68, 70, 71, 78, 79, 83, 91, 93, 97, 100, 104, 105, 106, 108, 111, 115, 117, 124, 133, 136, 138, 146, 147, 149, 155, 163, 164, 165, 167, 168, 170, 172, 173, 178, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 14, 17, 21, 23, 27, 29, 30, 32, 34, 35, 44, 46, 50, 60, 63, 67, 68, 73, 78, 79, 83, 91, 97, 100, 104, 105, 109, 110, 111, 112, 113, 116, 118, 123, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 159, 164, 168, 170, 172, 173, 178, 179, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 9, 11, 14, 17, 23, 27, 29, 32, 34, 35, 44, 46, 50, 58, 60, 63, 68, 70, 71, 75, 78, 79, 81, 82, 83, 91, 92, 93, 97, 100, 104, 105, 106, 111, 113, 116, 118, 120, 123, 128, 133, 136, 138, 146, 147, 148, 149, 152, 155, 164, 165, 167, 170, 171, 172, 175, 176, 178, 179, 188, 190, 191, 192, 194, 195, 197, 206, 210, 212, 213, 217},
    {2, 3, 14, 17, 21, 22, 23, 27, 29, 32, 35, 44, 46, 49, 50, 51, 52, 60, 63, 67, 68, 70, 71, 78, 79, 83, 91, 93, 97, 100, 104, 105, 106, 111, 115, 117, 124, 133, 136, 138, 146, 147, 149, 155, 163, 164, 165, 167, 168, 170, 172, 173, 178, 189, 190, 197, 206, 211, 212, 213, 214, 216},
    {2, 3, 14, 17, 21, 22, 23, 27, 29, 32, 35, 44, 46, 50, 60, 63, 66, 67, 68, 70, 71, 78, 79, 83, 91, 93, 99, 100, 104, 106, 111, 115, 117, 124, 133, 136, 138, 146, 147, 149, 155, 162, 164, 170, 171, 172, 174, 178, 188, 190, 192, 194, 195, 197, 206, 210, 212, 213, 217},
    {2, 3, 8, 14, 17, 21, 22, 23, 27, 29, 32, 35, 44, 46, 50, 60, 63, 66, 67, 68, 70, 71, 78, 79, 83, 91, 92, 93, 99, 100, 104, 106, 111, 115, 117, 124, 133, 136, 138, 146, 147, 149, 155, 162, 164, 170, 171, 172, 175, 176, 178, 179, 187, 190, 197, 206, 210, 212, 213, 217}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 4:2, 5:3, 6:4, 10:5, 12:6, 13:7, 14:8, 15:9, 16:10, 17:11, 18:12, 20:13, 21:14, 22:15, 23:16, 24:17, 25:18, 26:19, 27:20, 29:21, 30:22, 31:23, 32:24, 33:25, 34:26, 35:27, 36:28, 38:29, 39:30, 40:31, 42:32, 43:33, 44:34, 45:35, 47:36, 48:37, 49:38, 50:39, 51:40, 52:41, 53:42, 54:43, 55:44, 56:45, 57:46, 58:47, 60:48, 62:49, 64:50, 66:51, 69:52, 70:53, 71:54, 72:55, 73:56, 74:57, 75:58, 76:59, 77:60, 78:61, 80:62, 82:63, 84:64, 87:65, 89:66, 95:67, 96:68, 98:69, 99:70, 101:71, 102:72, 103:73, 104:74, 105:75, 106:76, 108:77, 109:78, 110:79, 111:80, 112:81, 113:82, 114:83, 115:84, 116:85, 118:86, 119:87, 120:88, 121:89, 122:90, 123:91, 124:92, 125:93, 126:94, 129:95, 130:96, 131:97, 132:98, 133:99, 134:100, 135:101, 136:102, 137:103, 139:104, 140:105, 141:106, 143:107, 144:108, 147:109, 148:110, 149:111, 150:112, 151:113, 154:114, 156:115, 157:116, 158:117, 160:118, 161:119, 162:120, 165:121, 166:122, 167:123, 168:124, 169:125, 170:126, 171:127, 172:128, 173:129, 174:130, 175:131, 176:132, 177:133, 178:134, 179:135, 180:136, 181:137, 182:138, 183:139, 185:140, 186:141, 187:142, 188:143, 189:144, 190:145, 199:146, 201:147, 202:148, 203:149, 205:150, 208:151, 209:152, 210:153, 212:154, 213:155, 216:156, 218:157, 220:158, 221:159, 222:160, 223:161, 224:162, 225:163, 226:164, 228:165, 229:166, 230:167, 232:168, 234:169, 238:170, 240:171, 242:172, 243:173, 244:174, 245:175, 246:176, 248:177, 249:178, 250:179, 251:180, 252:181, 253:182, 256:183, 257:184, 258:185, 260:186, 261:187, 262:188, 263:189, 265:190, 266:191, 267:192, 268:193, 269:194, 270:195, 271:196, 272:197, 273:198, 274:199, 275:200, 276:201, 277:202, 278:203, 279:204, 280:205, 282:206, 284:207, 285:208, 287:209, 288:210, 291:211, 292:212, 293:213, 294:214, 296:215, 298:216, 299:217, 300:218}

    rule_expressions[1] = "(voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 33 or voltage_mv <= 30)"
    rule_expressions[2] = "(voltage_mv >= 30 or voltage_mv <= 30) != (not (voltage_mv >= 30 or voltage_mv <= 30))"
    rule_expressions[3] = "(voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 and voltage_mv <= 30)"
    rule_expressions[4] = "(voltage_mv >= 30 or voltage_mv <= 30) != (speed >= 30 or voltage_mv <= 30)"
    rule_expressions[5] = "(voltage_mv >= 30 or voltage_mv <= 30) != (voltage_mv >= 30 and voltage_mv <= 30)"
    rule_expressions[6] = "(7 <= voltage_mv <= 71) != (9 <= voltage_mv <= 71)"
    rule_expressions[7] = "(7 <= voltage_mv <= 71) != (14 <= voltage_mv <= 71)"
    rule_expressions[8] = "(7 <= voltage_mv <= 71) != (7 <= speed <= 71)"
    rule_expressions[9] = "(7 <= voltage_mv <= 71) != (7 <= -voltage_mv <= 71)"
    rule_expressions[10] = "(7 <= voltage_mv <= 71) != (7 <= voltage_mv <= 75)"
    rule_expressions[11] = "(7 <= voltage_mv <= 71) != (7 <= voltage_mv <= -71)"
    rule_expressions[12] = "(7 <= voltage_mv <= 71) != (7 <= voltage_mv <= 70)"
    rule_expressions[13] = "(7 <= voltage_mv <= 71) != (7 <= -voltage_mv <= 71)"
    rule_expressions[14] = "(4 <= voltage_mv <= 48) != (not (4 <= voltage_mv <= 48))"
    rule_expressions[15] = "(4 <= voltage_mv <= 48) != (voltage_mv >= 4 <= 48)"
    rule_expressions[16] = "(4 <= voltage_mv <= 48) != (voltage_mv >= 4 <= 48)"
    rule_expressions[17] = "(4 <= voltage_mv <= 48) != (not (4) <= voltage_mv <= 48)"
    rule_expressions[18] = "(4 <= voltage_mv <= 48) != (13 <= voltage_mv <= 48)"
    rule_expressions[19] = "(4 <= voltage_mv <= 48) != (4 <= voltage_mv <= 96)"
    rule_expressions[20] = "(4 <= voltage_mv <= 48) != (not (4 <= voltage_mv <= 48))"
    rule_expressions[21] = "(4 <= voltage_mv <= 48) != (-4 <= voltage_mv <= 48)"
    rule_expressions[22] = "(4 <= voltage_mv <= 48) != (4 <= speed <= 48)"
    rule_expressions[23] = "(speed % altitude < 97) != (speed % altitude < -97)"
    rule_expressions[24] = "(speed % altitude < 97) != (speed % altitude < 100)"
    rule_expressions[25] = "(speed % altitude < 97) != (voltage_mv % altitude < 97)"
    rule_expressions[26] = "(speed % altitude < 97) != (speed % altitude < 99)"
    rule_expressions[27] = "(speed % altitude < 97) != (not (speed % altitude < 97))"
    rule_expressions[28] = "(speed % altitude < 97) != (not (speed % altitude < 97))"
    rule_expressions[29] = "(speed % altitude < 97) != (speed % 97 > altitude)"
    rule_expressions[30] = "(speed % altitude < 97) != (speed % altitude < 87)"
    rule_expressions[31] = "(speed % altitude < 97) != (not (speed % altitude < 97))"
    rule_expressions[32] = "(altitude >= 200) != (voltage_mv >= 200)"
    rule_expressions[33] = "(altitude >= 200) != (altitude >= 199)"
    rule_expressions[34] = "(altitude >= 200) != (altitude >= 400)"
    rule_expressions[35] = "(altitude >= 200) != (not (altitude >= 200))"
    rule_expressions[36] = "(altitude >= 200) != (altitude >= -200)"
    rule_expressions[37] = "(altitude >= 200) != (altitude >= 199)"
    rule_expressions[38] = "(altitude >= 200) != (voltage_mv >= 200)"
    rule_expressions[39] = "(altitude >= 200) != (altitude >= -200)"
    rule_expressions[40] = "(34 <= voltage_mv <= 84) != (34 <= voltage_mv <= -84)"
    rule_expressions[41] = "(34 <= voltage_mv <= 84) != (34 <= -voltage_mv <= 84)"
    rule_expressions[42] = "(34 <= voltage_mv <= 84) != (25 <= voltage_mv <= 84)"
    rule_expressions[43] = "(34 <= voltage_mv <= 84) != (34 <= -voltage_mv <= 84)"
    rule_expressions[44] = "(34 <= voltage_mv <= 84) != (-34 <= voltage_mv <= 84)"
    rule_expressions[45] = "(34 <= voltage_mv <= 84) != (68 <= voltage_mv <= 84)"
    rule_expressions[46] = "(34 <= voltage_mv <= 84) != (not (34) <= voltage_mv <= 84)"
    rule_expressions[47] = "(34 <= voltage_mv <= 84) != (29 <= voltage_mv <= 84)"
    rule_expressions[48] = "(34 <= voltage_mv <= 84) != (voltage_mv >= 34 <= 84)"
    rule_expressions[49] = "(altitude != 500 or speed > 2) != (altitude != 500 or -speed > 2)"
    rule_expressions[50] = "(altitude != 500 or speed > 2) != (not (altitude != 500 or speed > 2))"
    rule_expressions[51] = "(altitude != 500 or speed > 2) != (altitude != 500 and speed > 2)"
    rule_expressions[52] = "(altitude != 500 or speed > 2) != (altitude != 500 or speed > 7)"
    rule_expressions[53] = "(altitude != 500 or speed > 2) != (not (altitude != 500 or speed > 2))"
    rule_expressions[54] = "(speed == voltage_mv // 5) != (speed == -voltage_mv // 5)"
    rule_expressions[55] = "(speed == voltage_mv // 5) != (speed == voltage_mv // 3)"
    rule_expressions[56] = "(speed == voltage_mv // 5) != (speed == voltage_mv // 3)"
    rule_expressions[57] = "(speed == voltage_mv // 5) != (speed == voltage_mv // 15)"
    rule_expressions[58] = "(speed == voltage_mv // 5) != (speed == voltage_mv // 4)"
    rule_expressions[59] = "(speed == voltage_mv // 5) != (voltage_mv == speed // 5)"
    rule_expressions[60] = "(speed == voltage_mv // 5) != (not (speed == voltage_mv // 5))"
    rule_expressions[61] = "(speed == voltage_mv // 5) != (speed == voltage_mv // 3)"
    rule_expressions[62] = "(speed == voltage_mv // 5) != (speed == voltage_mv // -5)"
    rule_expressions[63] = "(speed < 100 or altitude <= 500) != (not (speed < 100 or altitude <= 500))"
    rule_expressions[64] = "(speed < 100 or altitude <= 500) != (speed < 100 or altitude <= -500)"
    rule_expressions[65] = "(speed < 100 or altitude <= 500) != (speed < 100 or altitude <= -500)"
    rule_expressions[66] = "(speed < 100 or altitude <= 500) != (speed < 100 and altitude <= 500)"
    rule_expressions[67] = "(altitude <= 10 and altitude > 30) != (speed <= 10 and altitude > 30)"
    rule_expressions[68] = "(altitude <= 10 and altitude > 30) != (not (altitude <= 10 and altitude > 30))"
    rule_expressions[69] = "(altitude <= 10 and altitude > 30) != (not (altitude <= 10 and altitude > 30))"
    rule_expressions[70] = "(altitude <= 10 and altitude > 30) != (voltage_mv <= 10 and altitude > 30)"
    rule_expressions[71] = "(12 <= voltage_mv <= 70) != (-12 <= voltage_mv <= 70)"
    rule_expressions[72] = "(12 <= voltage_mv <= 70) != (12 <= -voltage_mv <= 70)"
    rule_expressions[73] = "(12 <= voltage_mv <= 70) != (voltage_mv >= 12 <= 70)"
    rule_expressions[74] = "(12 <= voltage_mv <= 70) != (12 <= voltage_mv <= 72)"
    rule_expressions[75] = "(12 <= voltage_mv <= 70) != (12 <= speed <= 70)"
    rule_expressions[76] = "(12 <= voltage_mv <= 70) != (19 <= voltage_mv <= 70)"
    rule_expressions[77] = "(12 <= voltage_mv <= 70) != (12 <= voltage_mv <= -70)"
    rule_expressions[78] = "(12 <= voltage_mv <= 70) != (not (12 <= voltage_mv <= 70))"
    rule_expressions[79] = "(12 <= voltage_mv <= 70) != (not (12) <= voltage_mv <= 70)"
    rule_expressions[80] = "(12 <= speed <= 91) != (speed >= 12 <= 91)"
    rule_expressions[81] = "(12 <= speed <= 91) != (12 <= speed <= -91)"
    rule_expressions[82] = "(12 <= speed <= 91) != (12 <= -speed <= 91)"
    rule_expressions[83] = "(12 <= speed <= 91) != (not (12 <= speed <= 91))"
    rule_expressions[84] = "(12 <= speed <= 91) != (12 <= speed <= 94)"
    rule_expressions[85] = "(12 <= speed <= 91) != (not (12 <= speed <= 91))"
    rule_expressions[86] = "(12 <= speed <= 91) != (12 <= speed <= 86)"
    rule_expressions[87] = "(12 <= speed <= 91) != (not (12 <= speed <= 91))"
    rule_expressions[88] = "(12 <= speed <= 91) != (speed >= 12 <= 91)"
    rule_expressions[89] = "(voltage_mv >= 10) != (voltage_mv >= 12)"
    rule_expressions[90] = "(voltage_mv >= 10) != (voltage_mv >= 11)"
    rule_expressions[91] = "(voltage_mv >= 10) != (not (voltage_mv >= 10))"
    rule_expressions[92] = "(voltage_mv >= 10) != (voltage_mv >= 5)"
    rule_expressions[93] = "(voltage_mv >= 10) != (voltage_mv >= -10)"
    rule_expressions[94] = "(voltage_mv >= 10) != (not (voltage_mv >= 10))"
    rule_expressions[95] = "(voltage_mv >= 10) != (not (voltage_mv >= 10))"
    rule_expressions[96] = "(voltage_mv >= 10) != (not (voltage_mv >= 10))"
    rule_expressions[97] = "(88 <= altitude <= 590) != (88 <= -altitude <= 590)"
    rule_expressions[98] = "(88 <= altitude <= 590) != (93 <= altitude <= 590)"
    rule_expressions[99] = "(88 <= altitude <= 590) != (altitude >= 88 <= 590)"
    rule_expressions[100] = "(88 <= altitude <= 590) != (not (88 <= altitude <= 590))"
    rule_expressions[101] = "(88 <= altitude <= 590) != (176 <= altitude <= 590)"
    rule_expressions[102] = "(88 <= altitude <= 590) != (not (88 <= altitude <= 590))"
    rule_expressions[103] = "(88 <= altitude <= 590) != (88 <= -altitude <= 590)"
    rule_expressions[104] = "(88 <= altitude <= 590) != (not (88) <= altitude <= 590)"
    rule_expressions[105] = "(88 <= altitude <= 590) != (88 <= altitude <= -590)"
    rule_expressions[106] = "(altitude < 200 or voltage_mv == 100) != (speed < 200 or voltage_mv == 100)"
    rule_expressions[107] = "(altitude < 200 or voltage_mv == 100) != (altitude < -200 or voltage_mv == 100)"
    rule_expressions[108] = "(altitude < 200 or voltage_mv == 100) != (altitude < 205 or voltage_mv == 100)"
    rule_expressions[109] = "(altitude < 200 or voltage_mv == 100) != (altitude < 200 or voltage_mv == 200)"
    rule_expressions[110] = "(altitude < 200 or voltage_mv == 100) != (altitude < 200 and voltage_mv == 100)"
    rule_expressions[111] = "(altitude < 200 or voltage_mv == 100) != (not (altitude < 200 or voltage_mv == 100))"
    rule_expressions[112] = "(altitude < 200 or voltage_mv == 100) != (altitude < 200 or voltage_mv == 50)"
    rule_expressions[113] = "(voltage_mv <= 100 and speed > 30) != (altitude <= 100 and speed > 30)"
    rule_expressions[114] = "(voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and speed > 20)"
    rule_expressions[115] = "(voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and speed > -30)"
    rule_expressions[116] = "(voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 and -speed > 30)"
    rule_expressions[117] = "(voltage_mv <= 100 and speed > 30) != (voltage_mv <= 100 or speed > 30)"
    rule_expressions[118] = "(voltage_mv <= 100 and speed > 30) != (voltage_mv <= -100 and speed > 30)"
    rule_expressions[119] = "(18 <= voltage_mv <= 95) != (18 <= voltage_mv <= 96)"
    rule_expressions[120] = "(18 <= voltage_mv <= 95) != (18 <= speed <= 95)"
    rule_expressions[121] = "(18 <= voltage_mv <= 95) != (18 <= voltage_mv <= 101)"
    rule_expressions[122] = "(18 <= voltage_mv <= 95) != (8 <= voltage_mv <= 95)"
    rule_expressions[123] = "(18 <= voltage_mv <= 95) != (voltage_mv >= 18 <= 95)"
    rule_expressions[124] = "(18 <= voltage_mv <= 95) != (-18 <= voltage_mv <= 95)"
    rule_expressions[125] = "(18 <= voltage_mv <= 95) != (18 <= -voltage_mv <= 95)"
    rule_expressions[126] = "(18 <= voltage_mv <= 95) != (18 <= -voltage_mv <= 95)"
    rule_expressions[127] = "(18 <= voltage_mv <= 71) != (18 <= altitude <= 71)"
    rule_expressions[128] = "(18 <= voltage_mv <= 71) != (voltage_mv >= 18 <= 71)"
    rule_expressions[129] = "(18 <= voltage_mv <= 71) != (18 <= -voltage_mv <= 71)"
    rule_expressions[130] = "(18 <= voltage_mv <= 71) != (18 <= voltage_mv <= 76)"
    rule_expressions[131] = "(18 <= voltage_mv <= 71) != (18 <= -voltage_mv <= 71)"
    rule_expressions[132] = "(18 <= voltage_mv <= 71) != (18 <= voltage_mv <= -71)"
    rule_expressions[133] = "(18 <= voltage_mv <= 71) != (not (18 <= voltage_mv <= 71))"
    rule_expressions[134] = "(18 <= voltage_mv <= 71) != (36 <= voltage_mv <= 71)"
    rule_expressions[135] = "(18 <= voltage_mv <= 71) != (voltage_mv >= 18 <= 71)"
    rule_expressions[136] = "(18 <= voltage_mv <= 71) != (not (18) <= voltage_mv <= 71)"
    rule_expressions[137] = "(speed != altitude - 50) != (speed != altitude - -50)"
    rule_expressions[138] = "(speed != altitude - 50) != (not (speed != altitude - 50))"
    rule_expressions[139] = "(speed != altitude - 50) != (speed != altitude - 45)"
    rule_expressions[140] = "(speed != altitude - 50) != (speed != altitude - 53)"
    rule_expressions[141] = "(speed != altitude - 50) != (altitude != altitude - 50)"
    rule_expressions[142] = "(speed != altitude - 50) != (speed != altitude - -50)"
    rule_expressions[143] = "(speed != altitude - 50) != (speed != altitude - -50)"
    rule_expressions[144] = "(speed != altitude - 50) != (speed != -altitude - 50)"
    rule_expressions[145] = "(speed != altitude - 50) != (altitude != speed - 50)"
    rule_expressions[146] = "(altitude == speed * 1000) != (not (altitude == speed * 1000))"
    rule_expressions[147] = "(altitude <= 20 or speed == 20) != (speed <= 20 or speed == 20)"
    rule_expressions[148] = "(altitude <= 20 or speed == 20) != (altitude <= -20 or speed == 20)"
    rule_expressions[149] = "(altitude <= 20 or speed == 20) != (not (altitude <= 20 or speed == 20))"
    rule_expressions[150] = "(altitude <= 20 or speed == 20) != (altitude <= 20 or speed == 30)"
    rule_expressions[151] = "(altitude <= 20 or speed == 20) != (altitude <= 20 or speed == 19)"
    rule_expressions[152] = "(altitude <= 20 or speed == 20) != (altitude <= 20 and speed == 20)"
    rule_expressions[153] = "(altitude <= 20 or speed == 20) != (altitude <= 20 or speed == 19)"
    rule_expressions[154] = "(voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == 95 and voltage_mv <= 100)"
    rule_expressions[155] = "(voltage_mv == 85 and voltage_mv <= 100) != (not (voltage_mv == 85 and voltage_mv <= 100))"
    rule_expressions[156] = "(voltage_mv == 85 and voltage_mv <= 100) != (altitude == 85 and voltage_mv <= 100)"
    rule_expressions[157] = "(voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == 86 and voltage_mv <= 100)"
    rule_expressions[158] = "(voltage_mv == 85 and voltage_mv <= 100) != (voltage_mv == -85 and voltage_mv <= 100)"
    rule_expressions[159] = "(5 <= speed <= 48) != (speed >= 5 <= 48)"
    rule_expressions[160] = "(5 <= speed <= 48) != (7 <= speed <= 48)"
    rule_expressions[161] = "(5 <= speed <= 48) != (speed >= 5 <= 48)"
    rule_expressions[162] = "(5 <= speed <= 48) != (1 <= speed <= 48)"
    rule_expressions[163] = "(5 <= speed <= 48) != (10 <= speed <= 48)"
    rule_expressions[164] = "(5 <= speed <= 48) != (not (5 <= speed <= 48))"
    rule_expressions[165] = "(5 <= speed <= 48) != (5 <= -speed <= 48)"
    rule_expressions[166] = "(5 <= speed <= 48) != (5 <= -speed <= 48)"
    rule_expressions[167] = "(5 <= speed <= 48) != (5 <= speed <= -48)"
    rule_expressions[168] = "(voltage_mv > 30 or speed == 10) != (voltage_mv > 30 and speed == 10)"
    rule_expressions[169] = "(voltage_mv > 30 or speed == 10) != (voltage_mv > 25 or speed == 10)"
    rule_expressions[170] = "(voltage_mv > 30 or speed == 10) != (not (voltage_mv > 30 or speed == 10))"
    rule_expressions[171] = "(voltage_mv > 30 or speed == 10) != (voltage_mv > -30 or speed == 10)"
    rule_expressions[172] = "(5 <= voltage_mv <= 88) != (not (5) <= voltage_mv <= 88)"
    rule_expressions[173] = "(5 <= voltage_mv <= 88) != (voltage_mv >= 5 <= 88)"
    rule_expressions[174] = "(5 <= voltage_mv <= 88) != (-5 <= voltage_mv <= 88)"
    rule_expressions[175] = "(5 <= voltage_mv <= 88) != (5 <= voltage_mv <= -88)"
    rule_expressions[176] = "(5 <= voltage_mv <= 88) != (5 <= -voltage_mv <= 88)"
    rule_expressions[177] = "(5 <= voltage_mv <= 88) != (5 <= voltage_mv <= -88)"
    rule_expressions[178] = "(5 <= voltage_mv <= 88) != (not (5 <= voltage_mv <= 88))"
    rule_expressions[179] = "(5 <= voltage_mv <= 88) != (5 <= altitude <= 88)"
    rule_expressions[180] = "(speed == 30) != (voltage_mv == 30)"
    rule_expressions[181] = "(speed == 30) != (speed == 60)"
    rule_expressions[182] = "(speed == 30) != (speed == -30)"
    rule_expressions[183] = "(speed == 30) != (voltage_mv == 30)"
    rule_expressions[184] = "(speed == 30) != (altitude == 30)"
    rule_expressions[185] = "(speed == 30) != (speed == 40)"
    rule_expressions[186] = "(speed == 30) != (altitude == 30)"
    rule_expressions[187] = "(271 <= altitude <= 907) != (271 <= altitude <= 1814)"
    rule_expressions[188] = "(271 <= altitude <= 907) != (271 <= altitude <= -907)"
    rule_expressions[189] = "(271 <= altitude <= 907) != (-271 <= altitude <= 907)"
    rule_expressions[190] = "(271 <= altitude <= 907) != (not (271 <= altitude <= 907))"
    rule_expressions[191] = "(271 <= altitude <= 907) != (542 <= altitude <= 907)"
    rule_expressions[192] = "(271 <= altitude <= 907) != (271 <= speed <= 907)"
    rule_expressions[193] = "(271 <= altitude <= 907) != (271 <= altitude <= 1814)"
    rule_expressions[194] = "(271 <= altitude <= 907) != (271 <= voltage_mv <= 907)"
    rule_expressions[195] = "(271 <= altitude <= 907) != (271 <= -altitude <= 907)"
    rule_expressions[196] = "(speed != 20) != (speed != 40)"
    rule_expressions[197] = "(speed != 20) != (not (speed != 20))"
    rule_expressions[198] = "(speed != 20) != (speed != 23)"
    rule_expressions[199] = "(speed != 20) != (speed != -20)"
    rule_expressions[200] = "(speed != 20) != (speed != 19)"
    rule_expressions[201] = "(speed != 20) != (speed != -20)"
    rule_expressions[202] = "(speed != 20) != (speed != 22)"
    rule_expressions[203] = "(speed != 20) != (speed != -20)"
    rule_expressions[204] = "(speed != 20) != (not (speed != 20))"
    rule_expressions[205] = "(speed != 20) != (voltage_mv != 20)"
    rule_expressions[206] = "(voltage_mv < 50) != (not (voltage_mv < 50))"
    rule_expressions[207] = "(voltage_mv < 50) != (not (voltage_mv < 50))"
    rule_expressions[208] = "(voltage_mv < 50) != (not (voltage_mv < 50))"
    rule_expressions[209] = "(voltage_mv < 50) != (voltage_mv < -50)"
    rule_expressions[210] = "(voltage_mv < 50) != (altitude < 50)"
    rule_expressions[211] = "(voltage_mv < 100 or speed < 5) != (voltage_mv < 100 and speed < 5)"
    rule_expressions[212] = "(voltage_mv < 100 or speed < 5) != (not (voltage_mv < 100 or speed < 5))"
    rule_expressions[213] = "(voltage_mv < 100 or speed < 5) != (altitude < 100 or speed < 5)"
    rule_expressions[214] = "(voltage_mv < 100 or speed < 5) != (voltage_mv < 50 or speed < 5)"
    rule_expressions[215] = "(voltage_mv < 100 or speed < 5) != (voltage_mv < 90 or speed < 5)"
    rule_expressions[216] = "(voltage_mv < 100 or speed < 5) != (voltage_mv < -100 or speed < 5)"
    rule_expressions[217] = "(voltage_mv < 100 or speed < 5) != (voltage_mv < 100 or -speed < 5)"
    rule_expressions[218] = "(voltage_mv < 100 or speed < 5) != (not (voltage_mv < 100 or speed < 5))"

    return rule_expressions