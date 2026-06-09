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
    # 变异规则 1 - RSR
    if (speed != 58) != (not (speed != 58)):
        triggered.add(1)
    # 变异规则 2 - SCR
    if (speed != 58) != (not (speed != 58)):
        triggered.add(2)
    # 变异规则 3 - CSR
    if (speed != 58) != (speed != -58):
        triggered.add(3)
    # 变异规则 4 - SVR
    if (speed != 58) != (altitude != 58):
        triggered.add(4)
    # 变异规则 5 - ABS
    if (speed != 58) != (abs(speed) != 58):
        t=1
    # 变异规则 6 - SAR
    if (speed != 58) != (58 != speed):
        t=1
    # 变异规则 7 - ROR
    if (speed != 58) != (voltage_mv != 58):
        triggered.add(5)
    # 变异规则 8 - SRC
    if (speed != 58) != (58 != speed):
        t=1
    # 变异规则 9 - CAR
    if (speed != 58) != (speed != 56):
        triggered.add(6)
    # 变异规则 10 - UOI
    if (speed != 58) != (not (speed != 58)):
        triggered.add(7)
    # 原语句
    if speed != 58:
        health_score -= 21
        speed = min(speed + 3, 100)
    # 原语句2
    # 变异规则 11 - SRC
    if (33 <= altitude <= 664) != (33 <= -altitude <= 664):
        triggered.add(8)
    # 变异规则 12 - CSR
    if (33 <= altitude <= 664) != (-33 <= altitude <= 664):
        triggered.add(9)
    # 变异规则 13 - RSR
    if (33 <= altitude <= 664) != (not (33 <= altitude <= 664)):
        triggered.add(10)
    # 变异规则 14 - AOR
    if (33 <= altitude <= 664) != (33 <= altitude <= 674):
        triggered.add(11)
    # 变异规则 15 - ABS
    if (33 <= altitude <= 664) != (33 <= abs(altitude) <= 664):
        t=1
    # 变异规则 16 - SAR
    if (33 <= altitude <= 664) != (altitude >= 33 <= 664):
        triggered.add(12)
    # 变异规则 17 - CAR
    if (33 <= altitude <= 664) != (31 <= altitude <= 664):
        triggered.add(13)
    # 变异规则 18 - UOI
    if (33 <= altitude <= 664) != (33 <= -altitude <= 664):
        triggered.add(14)
    # 变异规则 19 - SVR
    if (33 <= altitude <= 664) != (33 <= speed <= 664):
        triggered.add(15)
    # 变异规则 20 - ROR
    if (33 <= altitude <= 664) != (-33 <= altitude <= 664):
        triggered.add(16)
    # 原语句
    if 33 <= altitude <= 664:
        health_score -= 6
    # 原语句3
    # 变异规则 21 - SCR
    if (259 <= altitude <= 690) != (not (259) <= altitude <= 690):
        triggered.add(17)
    # 变异规则 22 - AOR
    if (259 <= altitude <= 690) != (259 <= voltage_mv <= 690):
        triggered.add(18)
    # 变异规则 23 - UOI
    if (259 <= altitude <= 690) != (259 <= -altitude <= 690):
        triggered.add(19)
    # 变异规则 24 - LCR
    if (259 <= altitude <= 690) != (259 <= altitude <= -690):
        triggered.add(20)
    # 变异规则 25 - RSR
    if (259 <= altitude <= 690) != (not (259 <= altitude <= 690)):
        triggered.add(21)
    # 变异规则 26 - CRP
    if (259 <= altitude <= 690) != (261 <= altitude <= 690):
        triggered.add(22)
    # 变异规则 27 - SRC
    if (259 <= altitude <= 690) != (259 <= -altitude <= 690):
        triggered.add(23)
    # 变异规则 28 - ROR
    if (259 <= altitude <= 690) != (-259 <= altitude <= 690):
        triggered.add(24)
    # 变异规则 29 - CSR
    if (259 <= altitude <= 690) != (259 <= altitude <= -690):
        triggered.add(25)
    # 变异规则 30 - CAR
    if (259 <= altitude <= 690) != (249 <= altitude <= 690):
        triggered.add(26)
    # 原语句
    if 259 <= altitude <= 690:
        health_score -= 5
        voltage_mv = max(voltage_mv - 4, 2)
    # 原语句4
    # 变异规则 31 - SAR
    if (speed * 100 == voltage_mv) != (speed * voltage_mv == 100):
        triggered.add(27)
    # 变异规则 32 - LCR
    if (speed * 100 == voltage_mv) != (voltage_mv * 100 == voltage_mv):
        t=1
    # 变异规则 33 - AOR
    if (speed * 100 == voltage_mv) != (not (speed * 100 == voltage_mv)):
        triggered.add(28)
    # 变异规则 34 - ABS
    if (speed * 100 == voltage_mv) != (abs(speed) * 100 == voltage_mv):
        t=1
    # 变异规则 35 - RSR
    if (speed * 100 == voltage_mv) != (not (speed * 100 == voltage_mv)):
        triggered.add(29)
    # 变异规则 36 - CRP
    if (speed * 100 == voltage_mv) != (speed * 104 == voltage_mv):
        t=1
    # 变异规则 37 - CSR
    if (speed * 100 == voltage_mv) != (speed * -100 == voltage_mv):
        t=1
    # 变异规则 38 - CAR
    if (speed * 100 == voltage_mv) != (speed * 105 == voltage_mv):
        t=1
    # 变异规则 39 - SVR
    if (speed * 100 == voltage_mv) != (altitude * 100 == voltage_mv):
        t=1
    # 变异规则 40 - ROR
    if (speed * 100 == voltage_mv) != (altitude * 100 == voltage_mv):
        t=1
    # 原语句
    if speed * 100 == voltage_mv:
        health_score -= 22
        speed = max(speed - 4, 2)
    # 原语句5
    # 变异规则 41 - AOR
    if (speed // altitude < 95) != (speed // altitude < 105):
        t=1
    # 变异规则 42 - SRC
    if (speed // altitude < 95) != (altitude // altitude < 95):
        t=1
    # 变异规则 43 - ROR
    if (speed // altitude < 95) != (not (speed // altitude < 95)):
        triggered.add(30)
    # 变异规则 44 - CRP
    if (speed // altitude < 95) != (speed // altitude < 190):
        t=1
    # 变异规则 45 - LCR
    if (speed // altitude < 95) != (speed // -altitude < 95):
        t=1
    # 变异规则 46 - CAR
    if (speed // altitude < 95) != (speed // altitude < 94):
        t=1
    # 变异规则 47 - CSR
    if (speed // altitude < 95) != (speed // altitude < -95):
        triggered.add(31)
    # 变异规则 48 - ABS
    if (speed // altitude < 95) != (speed // abs(altitude) < 95):
        t=1
    # 变异规则 49 - UOI
    if (speed // altitude < 95) != (speed // -altitude < 95):
        t=1
    # 变异规则 50 - SAR
    if (speed // altitude < 95) != (speed // 95 > altitude):
        triggered.add(32)
    # 原语句
    if speed // altitude < 95:
        health_score -= 8
        speed = max(speed - 8, 2)
    # 原语句6
    # 变异规则 51 - ROR
    if (voltage_mv * 50 == altitude) != (voltage_mv * -50 == altitude):
        triggered.add(33)
    # 变异规则 52 - AOR
    if (voltage_mv * 50 == altitude) != (not (voltage_mv * 50 == altitude)):
        triggered.add(34)
    # 变异规则 53 - LCR
    if (voltage_mv * 50 == altitude) != (voltage_mv * 51 == altitude):
        triggered.add(35)
    # 变异规则 54 - SCR
    if (voltage_mv * 50 == altitude) != (not (voltage_mv * 50 == altitude)):
        triggered.add(36)
    # 变异规则 55 - SVR
    if (voltage_mv * 50 == altitude) != (altitude * 50 == altitude):
        triggered.add(37)
    # 变异规则 56 - CAR
    if (voltage_mv * 50 == altitude) != (voltage_mv * 52 == altitude):
        triggered.add(38)
    # 变异规则 57 - CRP
    if (voltage_mv * 50 == altitude) != (voltage_mv * 25 == altitude):
        triggered.add(39)
    # 变异规则 58 - SAR
    if (voltage_mv * 50 == altitude) != (voltage_mv * altitude == 50):
        triggered.add(40)
    # 变异规则 59 - CSR
    if (voltage_mv * 50 == altitude) != (voltage_mv * -50 == altitude):
        triggered.add(41)
    # 变异规则 60 - SRC
    if (voltage_mv * 50 == altitude) != (voltage_mv * -50 == altitude):
        triggered.add(42)
    # 原语句
    if voltage_mv * 50 == altitude:
        health_score += 7
        altitude = min(altitude + 7, 1000)
        voltage_mv = min(voltage_mv + 4, 100)
    # 原语句7
    # 变异规则 61 - AOR
    if (altitude >= 355 or altitude > 1000) != (altitude >= 355 or 1000 < altitude):
        t=1
    # 变异规则 62 - CRP
    if (altitude >= 355 or altitude > 1000) != (altitude >= 355 or altitude > 1007):
        t=1
    # 变异规则 63 - CSR
    if (altitude >= 355 or altitude > 1000) != (altitude >= 355 or altitude > -1000):
        triggered.add(43)
    # 变异规则 64 - SVR
    if (altitude >= 355 or altitude > 1000) != (voltage_mv >= 355 or altitude > 1000):
        triggered.add(44)
    # 变异规则 65 - UOI
    if (altitude >= 355 or altitude > 1000) != (altitude >= 355 or -altitude > 1000):
        t=1
    # 变异规则 66 - ROR
    if (altitude >= 355 or altitude > 1000) != (altitude >= -355 or altitude > 1000):
        triggered.add(45)
    # 变异规则 67 - SRC
    if (altitude >= 355 or altitude > 1000) != (altitude > 1000 or altitude >= 355):
        t=1
    # 变异规则 68 - SAR
    if (altitude >= 355 or altitude > 1000) != (altitude >= 355 or 1000 < altitude):
        t=1
    # 变异规则 69 - LCR
    if (altitude >= 355 or altitude > 1000) != (altitude >= 355 and altitude > 1000):
        triggered.add(46)
    # 变异规则 70 - SCR
    if (altitude >= 355 or altitude > 1000) != (abs(altitude) >= 355 or altitude > 1000):
        t=1
    # 原语句
    if altitude >= 355 or altitude > 1000:
        health_score -= 1
    # 原语句8
    # 变异规则 71 - ABS
    if (speed <= 97 and speed == 2) != (abs(speed) <= 97 and speed == 2):
        t=1
    # 变异规则 72 - LCR
    if (speed <= 97 and speed == 2) != (speed <= 97 or speed == 2):
        triggered.add(47)
    # 变异规则 73 - AOR
    if (speed <= 97 and speed == 2) != (speed <= 97 and speed == -2):
        triggered.add(48)
    # 变异规则 74 - SRC
    if (speed <= 97 and speed == 2) != (speed == 2 and speed <= 97):
        t=1
    # 变异规则 75 - SAR
    if (speed <= 97 and speed == 2) != (97 >= speed and speed == 2):
        t=1
    # 变异规则 76 - RSR
    if (speed <= 97 and speed == 2) != (not (speed <= 97 and speed == 2)):
        triggered.add(49)
    # 变异规则 77 - CRP
    if (speed <= 97 and speed == 2) != (speed <= 97 and speed == 1):
        triggered.add(50)
    # 变异规则 78 - SCR
    if (speed <= 97 and speed == 2) != (speed <= 97 and speed == -2):
        triggered.add(51)
    # 变异规则 79 - SVR
    if (speed <= 97 and speed == 2) != (altitude <= 97 and speed == 2):
        triggered.add(52)
    # 变异规则 80 - CSR
    if (speed <= 97 and speed == 2) != (speed <= 97 and speed == -2):
        triggered.add(53)
    # 原语句
    if speed <= 97 and speed == 2:
        health_score += 13
        altitude = min(altitude + 99, 1000)
        altitude, speed = speed, altitude
    # 原语句9
    # 变异规则 81 - ABS
    if (speed >= 65 and voltage_mv > 40) != (abs(speed) >= 65 and voltage_mv > 40):
        t=1
    # 变异规则 82 - CRP
    if (speed >= 65 and voltage_mv > 40) != (speed >= 65 and voltage_mv > 32):
        triggered.add(54)
    # 变异规则 83 - UOI
    if (speed >= 65 and voltage_mv > 40) != (speed >= 65 and -voltage_mv > 40):
        triggered.add(55)
    # 变异规则 84 - SVR
    if (speed >= 65 and voltage_mv > 40) != (voltage_mv >= 65 and voltage_mv > 40):
        triggered.add(56)
    # 变异规则 85 - SRC
    if (speed >= 65 and voltage_mv > 40) != (voltage_mv > 40 and speed >= 65):
        t=1
    # 变异规则 86 - SCR
    if (speed >= 65 and voltage_mv > 40) != (speed >= 65 and 40 < voltage_mv):
        t=1
    # 变异规则 87 - CAR
    if (speed >= 65 and voltage_mv > 40) != (speed >= 65 and voltage_mv > 42):
        triggered.add(57)
    # 变异规则 88 - CSR
    if (speed >= 65 and voltage_mv > 40) != (speed >= -65 and voltage_mv > 40):
        triggered.add(58)
    # 变异规则 89 - ROR
    if (speed >= 65 and voltage_mv > 40) != (speed >= 65 or voltage_mv > 40):
        triggered.add(59)
    # 变异规则 90 - AOR
    if (speed >= 65 and voltage_mv > 40) != (not (speed >= 65 and voltage_mv > 40)):
        triggered.add(60)
    # 原语句
    if speed >= 65 and voltage_mv > 40:
        health_score -= 30
    # 原语句10
    # 变异规则 91 - CSR
    if (altitude != 1000) != (altitude != -1000):
        triggered.add(61)
    # 变异规则 92 - LCR
    if (altitude != 1000) != (altitude != -1000):
        triggered.add(62)
    # 变异规则 93 - ROR
    if (altitude != 1000) != (altitude != -1000):
        triggered.add(63)
    # 变异规则 94 - SAR
    if (altitude != 1000) != (1000 != altitude):
        t=1
    # 变异规则 95 - RSR
    if (altitude != 1000) != (not (altitude != 1000)):
        triggered.add(64)
    # 变异规则 96 - UOI
    if (altitude != 1000) != (abs(altitude) != 1000):
        t=1
    # 变异规则 97 - SVR
    if (altitude != 1000) != (voltage_mv != 1000):
        triggered.add(65)
    # 变异规则 98 - CRP
    if (altitude != 1000) != (altitude != 500):
        triggered.add(66)
    # 变异规则 99 - SRC
    if (altitude != 1000) != (speed != 1000):
        triggered.add(67)
    # 变异规则 100 - ABS
    if (altitude != 1000) != (abs(altitude) != 1000):
        t=1
    # 原语句
    if altitude != 1000:
        health_score += 17
    # 原语句11
    # 变异规则 101 - AOR
    if (altitude != 842 or speed > 30) != (not (altitude != 842 or speed > 30)):
        triggered.add(68)
    # 变异规则 102 - SVR
    if (altitude != 842 or speed > 30) != (speed != 842 or speed > 30):
        triggered.add(69)
    # 变异规则 103 - ABS
    if (altitude != 842 or speed > 30) != (abs(altitude) != 842 or speed > 30):
        t=1
    # 变异规则 104 - CAR
    if (altitude != 842 or speed > 30) != (altitude != 842 or speed > 29):
        triggered.add(70)
    # 变异规则 105 - SAR
    if (altitude != 842 or speed > 30) != (altitude != 842 or 30 < speed):
        t=1
    # 变异规则 106 - CRP
    if (altitude != 842 or speed > 30) != (altitude != 852 or speed > 30):
        triggered.add(71)
    # 变异规则 107 - SRC
    if (altitude != 842 or speed > 30) != (speed > 30 or altitude != 842):
        t=1
    # 变异规则 108 - LCR
    if (altitude != 842 or speed > 30) != (altitude != 842 and speed > 30):
        triggered.add(72)
    # 变异规则 109 - CSR
    if (altitude != 842 or speed > 30) != (altitude != 842 or speed > -30):
        triggered.add(73)
    # 变异规则 110 - ROR
    if (altitude != 842 or speed > 30) != (not (altitude != 842 or speed > 30)):
        triggered.add(74)
    # 原语句
    if altitude != 842 or speed > 30:
        health_score -= 23
        voltage_mv = min(voltage_mv + 3, 100)
    # 原语句12
    # 变异规则 111 - CAR
    if (22 <= speed <= 88) != (22 <= speed <= 93):
        triggered.add(75)
    # 变异规则 112 - UOI
    if (22 <= speed <= 88) != (22 <= -speed <= 88):
        triggered.add(76)
    # 变异规则 113 - CSR
    if (22 <= speed <= 88) != (-22 <= speed <= 88):
        triggered.add(77)
    # 变异规则 114 - ROR
    if (22 <= speed <= 88) != (22 <= abs(speed) <= 88):
        t=1
    # 变异规则 115 - SVR
    if (22 <= speed <= 88) != (22 <= altitude <= 88):
        triggered.add(78)
    # 变异规则 116 - CRP
    if (22 <= speed <= 88) != (44 <= speed <= 88):
        triggered.add(79)
    # 变异规则 117 - SRC
    if (22 <= speed <= 88) != (22 <= -speed <= 88):
        triggered.add(80)
    # 变异规则 118 - SCR
    if (22 <= speed <= 88) != (22 <= speed <= 83):
        triggered.add(81)
    # 变异规则 119 - RSR
    if (22 <= speed <= 88) != (not (22 <= speed <= 88)):
        triggered.add(82)
    # 变异规则 120 - LCR
    if (22 <= speed <= 88) != (22 <= speed <= 44):
        triggered.add(83)
    # 原语句
    if 22 <= speed <= 88:
        health_score -= 22
    # 原语句13
    # 变异规则 121 - ROR
    if (voltage_mv // speed != 95) != (voltage_mv // speed != 100):
        t=1
    # 变异规则 122 - RSR
    if (voltage_mv // speed != 95) != (not (voltage_mv // speed != 95)):
        triggered.add(84)
    # 变异规则 123 - CAR
    if (voltage_mv // speed != 95) != (voltage_mv // speed != 100):
        t=1
    # 变异规则 124 - SAR
    if (voltage_mv // speed != 95) != (voltage_mv // 95 != speed):
        t=1
    # 变异规则 125 - AOR
    if (voltage_mv // speed != 95) != (not (voltage_mv // speed != 95)):
        triggered.add(85)
    # 变异规则 126 - CSR
    if (voltage_mv // speed != 95) != (voltage_mv // speed != -95):
        t=1
    # 变异规则 127 - SVR
    if (voltage_mv // speed != 95) != (altitude // speed != 95):
        triggered.add(86)
    # 变异规则 128 - UOI
    if (voltage_mv // speed != 95) != (voltage_mv // -speed != 95):
        t=1
    # 变异规则 129 - SCR
    if (voltage_mv // speed != 95) != (voltage_mv // 95 != speed):
        t=1
    # 变异规则 130 - LCR
    if (voltage_mv // speed != 95) != (not (voltage_mv // speed != 95)):
        triggered.add(87)
    # 原语句
    if voltage_mv // speed != 95:
        health_score -= 11
        speed = min(speed + 1, 100)
        speed, voltage_mv = voltage_mv, speed
    # 原语句14
    # 变异规则 131 - LCR
    if (voltage_mv <= 5) != (voltage_mv <= -5):
        triggered.add(88)
    # 变异规则 132 - CRP
    if (voltage_mv <= 5) != (voltage_mv <= 10):
        triggered.add(89)
    # 变异规则 133 - SVR
    if (voltage_mv <= 5) != (altitude <= 5):
        triggered.add(90)
    # 变异规则 134 - ABS
    if (voltage_mv <= 5) != (abs(voltage_mv) <= 5):
        t=1
    # 变异规则 135 - CSR
    if (voltage_mv <= 5) != (voltage_mv <= -5):
        triggered.add(91)
    # 变异规则 136 - SAR
    if (voltage_mv <= 5) != (5 >= voltage_mv):
        t=1
    # 变异规则 137 - SCR
    if (voltage_mv <= 5) != (5 >= voltage_mv):
        t=1
    # 变异规则 138 - UOI
    if (voltage_mv <= 5) != (abs(voltage_mv) <= 5):
        t=1
    # 变异规则 139 - AOR
    if (voltage_mv <= 5) != (5 >= voltage_mv):
        t=1
    # 变异规则 140 - ROR
    if (voltage_mv <= 5) != (voltage_mv <= 10):
        triggered.add(92)
    # 原语句
    if voltage_mv <= 5:
        health_score += 6
    # 原语句15
    # 变异规则 141 - CAR
    if (altitude > 953 and altitude <= 1000) != (altitude > 963 and altitude <= 1000):
        triggered.add(93)
    # 变异规则 142 - SVR
    if (altitude > 953 and altitude <= 1000) != (voltage_mv > 953 and altitude <= 1000):
        triggered.add(94)
    # 变异规则 143 - SAR
    if (altitude > 953 and altitude <= 1000) != (953 < altitude and altitude <= 1000):
        t=1
    # 变异规则 144 - SCR
    if (altitude > 953 and altitude <= 1000) != (altitude > 953 and altitude <= 1002):
        t=1
    # 变异规则 145 - AOR
    if (altitude > 953 and altitude <= 1000) != (953 < altitude and altitude <= 1000):
        t=1
    # 变异规则 146 - ROR
    if (altitude > 953 and altitude <= 1000) != (altitude > 953 and -altitude <= 1000):
        t=1
    # 变异规则 147 - SRC
    if (altitude > 953 and altitude <= 1000) != (altitude <= 1000 and altitude > 953):
        t=1
    # 变异规则 148 - LCR
    if (altitude > 953 and altitude <= 1000) != (altitude > 953 or altitude <= 1000):
        triggered.add(95)
    # 变异规则 149 - CRP
    if (altitude > 953 and altitude <= 1000) != (altitude > 953 and altitude <= 998):
        triggered.add(96)
    # 变异规则 150 - UOI
    if (altitude > 953 and altitude <= 1000) != (altitude > 953 and -altitude <= 1000):
        t=1
    # 原语句
    if altitude > 953 and altitude <= 1000:
        health_score -= 13
        speed = min(speed + 4, 100)
    # 原语句16
    # 变异规则 151 - CRP
    if (speed - voltage_mv == 20) != (speed - voltage_mv == 24):
        triggered.add(97)
    # 变异规则 152 - AOR
    if (speed - voltage_mv == 20) != (speed - 20 == voltage_mv):
        t=1
    # 变异规则 153 - CSR
    if (speed - voltage_mv == 20) != (speed - voltage_mv == -20):
        triggered.add(98)
    # 变异规则 154 - RSR
    if (speed - voltage_mv == 20) != (not (speed - voltage_mv == 20)):
        triggered.add(99)
    # 变异规则 155 - ROR
    if (speed - voltage_mv == 20) != (not (speed - voltage_mv == 20)):
        triggered.add(100)
    # 变异规则 156 - LCR
    if (speed - voltage_mv == 20) != (altitude - voltage_mv == 20):
        triggered.add(101)
    # 变异规则 157 - SVR
    if (speed - voltage_mv == 20) != (altitude - voltage_mv == 20):
        triggered.add(102)
    # 变异规则 158 - CAR
    if (speed - voltage_mv == 20) != (speed - voltage_mv == 21):
        triggered.add(103)
    # 变异规则 159 - SAR
    if (speed - voltage_mv == 20) != (speed - 20 == voltage_mv):
        t=1
    # 变异规则 160 - SRC
    if (speed - voltage_mv == 20) != (speed - voltage_mv == -20):
        triggered.add(104)
    # 原语句
    if speed - voltage_mv == 20:
        health_score += 9
        altitude = max(altitude - 30, 2)
        speed = max(speed - 10, 2)
    # 原语句17
    # 变异规则 161 - SAR
    if (voltage_mv >= 36) != (36 <= voltage_mv):
        t=1
    # 变异规则 162 - ABS
    if (voltage_mv >= 36) != (abs(voltage_mv) >= 36):
        t=1
    # 变异规则 163 - UOI
    if (voltage_mv >= 36) != (36 <= voltage_mv):
        t=1
    # 变异规则 164 - LCR
    if (voltage_mv >= 36) != (speed >= 36):
        triggered.add(105)
    # 变异规则 165 - SVR
    if (voltage_mv >= 36) != (speed >= 36):
        triggered.add(106)
    # 变异规则 166 - CRP
    if (voltage_mv >= 36) != (voltage_mv >= 72):
        triggered.add(107)
    # 变异规则 167 - SRC
    if (voltage_mv >= 36) != (not (voltage_mv >= 36)):
        triggered.add(108)
    # 变异规则 168 - SCR
    if (voltage_mv >= 36) != (voltage_mv >= -36):
        triggered.add(109)
    # 变异规则 169 - RSR
    if (voltage_mv >= 36) != (not (voltage_mv >= 36)):
        triggered.add(110)
    # 变异规则 170 - AOR
    if (voltage_mv >= 36) != (not (voltage_mv >= 36)):
        triggered.add(111)
    # 原语句
    if voltage_mv >= 36:
        health_score += 12
        altitude = min(altitude + 92, 1000)
    # 原语句18
    # 变异规则 171 - SCR
    if (speed <= 26) != (altitude <= 26):
        triggered.add(112)
    # 变异规则 172 - CAR
    if (speed <= 26) != (speed <= 27):
        triggered.add(113)
    # 变异规则 173 - RSR
    if (speed <= 26) != (not (speed <= 26)):
        triggered.add(114)
    # 变异规则 174 - SRC
    if (speed <= 26) != (speed <= 21):
        triggered.add(115)
    # 变异规则 175 - CRP
    if (speed <= 26) != (speed <= 52):
        triggered.add(116)
    # 变异规则 176 - UOI
    if (speed <= 26) != (speed <= -26):
        triggered.add(117)
    # 变异规则 177 - ROR
    if (speed <= 26) != (altitude <= 26):
        triggered.add(118)
    # 变异规则 178 - LCR
    if (speed <= 26) != (abs(speed) <= 26):
        t=1
    # 变异规则 179 - SAR
    if (speed <= 26) != (26 >= speed):
        t=1
    # 变异规则 180 - CSR
    if (speed <= 26) != (speed <= -26):
        triggered.add(119)
    # 原语句
    if speed <= 26:
        health_score -= 25
        altitude = min(altitude + 20, 1000)
    # 原语句19
    # 变异规则 181 - SVR
    if (245 <= altitude <= 786) != (245 <= speed <= 786):
        triggered.add(120)
    # 变异规则 182 - SAR
    if (245 <= altitude <= 786) != (altitude >= 245 <= 786):
        triggered.add(121)
    # 变异规则 183 - CRP
    if (245 <= altitude <= 786) != (245 <= altitude <= 780):
        triggered.add(122)
    # 变异规则 184 - SCR
    if (245 <= altitude <= 786) != (245 <= abs(altitude) <= 786):
        t=1
    # 变异规则 185 - RSR
    if (245 <= altitude <= 786) != (not (245 <= altitude <= 786)):
        triggered.add(123)
    # 变异规则 186 - CSR
    if (245 <= altitude <= 786) != (-245 <= altitude <= 786):
        triggered.add(124)
    # 变异规则 187 - SRC
    if (245 <= altitude <= 786) != (245 <= voltage_mv <= 786):
        triggered.add(125)
    # 变异规则 188 - CAR
    if (245 <= altitude <= 786) != (245 <= altitude <= 796):
        triggered.add(126)
    # 变异规则 189 - ABS
    if (245 <= altitude <= 786) != (245 <= abs(altitude) <= 786):
        t=1
    # 变异规则 190 - LCR
    if (245 <= altitude <= 786) != (247 <= altitude <= 786):
        triggered.add(127)
    # 原语句
    if 245 <= altitude <= 786:
        health_score -= 2
        speed = min(speed + 10, 100)
    # 原语句20
    # 变异规则 191 - SAR
    if (voltage_mv != 20 or speed != 5) != (20 != voltage_mv or speed != 5):
        t=1
    # 变异规则 192 - AOR
    if (voltage_mv != 20 or speed != 5) != (not (voltage_mv != 20 or speed != 5)):
        triggered.add(128)
    # 变异规则 193 - LCR
    if (voltage_mv != 20 or speed != 5) != (voltage_mv != 20 and speed != 5):
        triggered.add(129)
    # 变异规则 194 - ROR
    if (voltage_mv != 20 or speed != 5) != (20 != voltage_mv or speed != 5):
        t=1
    # 变异规则 195 - SRC
    if (voltage_mv != 20 or speed != 5) != (speed != 5 or voltage_mv != 20):
        t=1
    # 变异规则 196 - CRP
    if (voltage_mv != 20 or speed != 5) != (voltage_mv != 20 or speed != 12):
        triggered.add(130)
    # 变异规则 197 - RSR
    if (voltage_mv != 20 or speed != 5) != (not (voltage_mv != 20 or speed != 5)):
        triggered.add(131)
    # 变异规则 198 - CAR
    if (voltage_mv != 20 or speed != 5) != (voltage_mv != 15 or speed != 5):
        triggered.add(132)
    # 变异规则 199 - ABS
    if (voltage_mv != 20 or speed != 5) != (voltage_mv != 20 or abs(speed) != 5):
        t=1
    # 变异规则 200 - UOI
    if (voltage_mv != 20 or speed != 5) != (voltage_mv != 20 or -speed != 5):
        triggered.add(133)
    # 原语句
    if voltage_mv != 20 or speed != 5:
        health_score -= 1
        altitude = max(altitude - 28, 2)
        speed = max(speed - 5, 2)
        voltage_mv, speed = speed, voltage_mv
    # 原语句21
    # 变异规则 201 - RSR
    if (altitude < 200 and altitude != 50) != (not (altitude < 200 and altitude != 50)):
        triggered.add(134)
    # 变异规则 202 - ROR
    if (altitude < 200 and altitude != 50) != (altitude < 200 and -altitude != 50):
        triggered.add(135)
    # 变异规则 203 - SAR
    if (altitude < 200 and altitude != 50) != (200 > altitude and altitude != 50):
        t=1
    # 变异规则 204 - LCR
    if (altitude < 200 and altitude != 50) != (altitude < 200 or altitude != 50):
        triggered.add(136)
    # 变异规则 205 - UOI
    if (altitude < 200 and altitude != 50) != (altitude < 200 and -altitude != 50):
        triggered.add(137)
    # 变异规则 206 - SCR
    if (altitude < 200 and altitude != 50) != (altitude != 50 and altitude < 200):
        t=1
    # 变异规则 207 - SVR
    if (altitude < 200 and altitude != 50) != (voltage_mv < 200 and altitude != 50):
        triggered.add(138)
    # 变异规则 208 - ABS
    if (altitude < 200 and altitude != 50) != (abs(altitude) < 200 and altitude != 50):
        t=1
    # 变异规则 209 - CRP
    if (altitude < 200 and altitude != 50) != (altitude < 200 and altitude != 25):
        triggered.add(139)
    # 变异规则 210 - CAR
    if (altitude < 200 and altitude != 50) != (altitude < 200 and altitude != 49):
        triggered.add(140)
    # 原语句
    if altitude < 200 and altitude != 50:
        health_score -= 20
    # 原语句22
    # 变异规则 211 - SCR
    if (speed >= 5 and speed <= 28) != (speed >= 5 and speed <= 36):
        triggered.add(141)
    # 变异规则 212 - SVR
    if (speed >= 5 and speed <= 28) != (altitude >= 5 and speed <= 28):
        triggered.add(142)
    # 变异规则 213 - RSR
    if (speed >= 5 and speed <= 28) != (not (speed >= 5 and speed <= 28)):
        triggered.add(143)
    # 变异规则 214 - AOR
    if (speed >= 5 and speed <= 28) != (abs(speed) >= 5 and speed <= 28):
        t=1
    # 变异规则 215 - CAR
    if (speed >= 5 and speed <= 28) != (speed >= 15 and speed <= 28):
        triggered.add(144)
    # 变异规则 216 - LCR
    if (speed >= 5 and speed <= 28) != (speed >= 5 or speed <= 28):
        triggered.add(145)
    # 变异规则 217 - SAR
    if (speed >= 5 and speed <= 28) != (speed >= 5 and 28 >= speed):
        t=1
    # 变异规则 218 - ROR
    if (speed >= 5 and speed <= 28) != (speed >= 5 and -speed <= 28):
        triggered.add(146)
    # 变异规则 219 - CSR
    if (speed >= 5 and speed <= 28) != (speed >= 5 and speed <= -28):
        triggered.add(147)
    # 变异规则 220 - SRC
    if (speed >= 5 and speed <= 28) != (speed <= 28 and speed >= 5):
        t=1
    # 原语句
    if speed >= 5 and speed <= 28:
        health_score -= 18
    # 原语句23
    # 变异规则 221 - SVR
    if (22 <= voltage_mv <= 61) != (22 <= altitude <= 61):
        triggered.add(148)
    # 变异规则 222 - AOR
    if (22 <= voltage_mv <= 61) != (29 <= voltage_mv <= 61):
        triggered.add(149)
    # 变异规则 223 - LCR
    if (22 <= voltage_mv <= 61) != (-22 <= voltage_mv <= 61):
        triggered.add(150)
    # 变异规则 224 - UOI
    if (22 <= voltage_mv <= 61) != (22 <= -voltage_mv <= 61):
        triggered.add(151)
    # 变异规则 225 - SAR
    if (22 <= voltage_mv <= 61) != (voltage_mv >= 22 <= 61):
        triggered.add(152)
    # 变异规则 226 - SRC
    if (22 <= voltage_mv <= 61) != (22 <= voltage_mv <= -61):
        triggered.add(153)
    # 变异规则 227 - ROR
    if (22 <= voltage_mv <= 61) != (voltage_mv >= 22 <= 61):
        triggered.add(154)
    # 变异规则 228 - RSR
    if (22 <= voltage_mv <= 61) != (not (22 <= voltage_mv <= 61)):
        triggered.add(155)
    # 变异规则 229 - CRP
    if (22 <= voltage_mv <= 61) != (11 <= voltage_mv <= 61):
        triggered.add(156)
    # 变异规则 230 - CSR
    if (22 <= voltage_mv <= 61) != (22 <= voltage_mv <= -61):
        triggered.add(157)
    # 原语句
    if 22 <= voltage_mv <= 61:
        health_score += 8
    # 原语句24
    # 变异规则 231 - SAR
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 变异规则 232 - ABS
    if (altitude >= 1000) != (abs(altitude) >= 1000):
        t=1
    # 变异规则 233 - SVR
    if (altitude >= 1000) != (speed >= 1000):
        t=1
    # 变异规则 234 - CSR
    if (altitude >= 1000) != (altitude >= -1000):
        triggered.add(158)
    # 变异规则 235 - ROR
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 变异规则 236 - UOI
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 变异规则 237 - AOR
    if (altitude >= 1000) != (altitude >= 1001):
        t=1
    # 变异规则 238 - SCR
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 变异规则 239 - RSR
    if (altitude >= 1000) != (not (altitude >= 1000)):
        triggered.add(159)
    # 变异规则 240 - SRC
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 原语句
    if altitude >= 1000:
        health_score -= 21
    # 原语句25
    # 变异规则 241 - CSR
    if (altitude % 328 < voltage_mv) != (altitude % -328 < voltage_mv):
        triggered.add(160)
    # 变异规则 242 - SAR
    if (altitude % 328 < voltage_mv) != (altitude % voltage_mv > 328):
        triggered.add(161)
    # 变异规则 243 - UOI
    if (altitude % 328 < voltage_mv) != (altitude % 328 < -voltage_mv):
        triggered.add(162)
    # 变异规则 244 - SRC
    if (altitude % 328 < voltage_mv) != (altitude % -328 < voltage_mv):
        triggered.add(163)
    # 变异规则 245 - CRP
    if (altitude % 328 < voltage_mv) != (altitude % 338 < voltage_mv):
        triggered.add(164)
    # 变异规则 246 - AOR
    if (altitude % 328 < voltage_mv) != (speed % 328 < voltage_mv):
        triggered.add(165)
    # 变异规则 247 - SCR
    if (altitude % 328 < voltage_mv) != (altitude % 338 < voltage_mv):
        triggered.add(166)
    # 变异规则 248 - ABS
    if (altitude % 328 < voltage_mv) != (abs(altitude) % 328 < voltage_mv):
        t=1
    # 变异规则 249 - CAR
    if (altitude % 328 < voltage_mv) != (altitude % 318 < voltage_mv):
        triggered.add(167)
    # 变异规则 250 - RSR
    if (altitude % 328 < voltage_mv) != (not (altitude % 328 < voltage_mv)):
        triggered.add(168)
    # 原语句
    if altitude % 328 < voltage_mv:
        health_score += 14
        altitude = max(altitude - 13, 2)
        speed = min(speed + 5, 100)
    # 原语句26
    # 变异规则 251 - SRC
    if (altitude < 50 or speed >= 50) != (speed >= 50 or altitude < 50):
        t=1
    # 变异规则 252 - SAR
    if (altitude < 50 or speed >= 50) != (50 > altitude or speed >= 50):
        t=1
    # 变异规则 253 - AOR
    if (altitude < 50 or speed >= 50) != (speed < 50 or speed >= 50):
        triggered.add(169)
    # 变异规则 254 - CSR
    if (altitude < 50 or speed >= 50) != (altitude < 50 or speed >= -50):
        triggered.add(170)
    # 变异规则 255 - LCR
    if (altitude < 50 or speed >= 50) != (altitude < 50 and speed >= 50):
        triggered.add(171)
    # 变异规则 256 - CRP
    if (altitude < 50 or speed >= 50) != (altitude < 50 or speed >= 25):
        triggered.add(172)
    # 变异规则 257 - RSR
    if (altitude < 50 or speed >= 50) != (not (altitude < 50 or speed >= 50)):
        triggered.add(173)
    # 变异规则 258 - ABS
    if (altitude < 50 or speed >= 50) != (abs(altitude) < 50 or speed >= 50):
        t=1
    # 变异规则 259 - ROR
    if (altitude < 50 or speed >= 50) != (altitude < -50 or speed >= 50):
        triggered.add(174)
    # 变异规则 260 - SCR
    if (altitude < 50 or speed >= 50) != (altitude < 50 or speed >= 25):
        triggered.add(175)
    # 原语句
    if altitude < 50 or speed >= 50:
        health_score -= 7
        altitude = min(altitude + 91, 1000)
        speed, voltage_mv = voltage_mv, speed
    # 原语句27
    # 变异规则 261 - RSR
    if (285 <= altitude <= 921) != (not (285 <= altitude <= 921)):
        triggered.add(176)
    # 变异规则 262 - SCR
    if (285 <= altitude <= 921) != (287 <= altitude <= 921):
        triggered.add(177)
    # 变异规则 263 - ROR
    if (285 <= altitude <= 921) != (285 <= abs(altitude) <= 921):
        t=1
    # 变异规则 264 - AOR
    if (285 <= altitude <= 921) != (285 <= -altitude <= 921):
        triggered.add(178)
    # 变异规则 265 - CRP
    if (285 <= altitude <= 921) != (570 <= altitude <= 921):
        triggered.add(179)
    # 变异规则 266 - UOI
    if (285 <= altitude <= 921) != (285 <= -altitude <= 921):
        triggered.add(180)
    # 变异规则 267 - CSR
    if (285 <= altitude <= 921) != (-285 <= altitude <= 921):
        triggered.add(181)
    # 变异规则 268 - SRC
    if (285 <= altitude <= 921) != (285 <= abs(altitude) <= 921):
        t=1
    # 变异规则 269 - LCR
    if (285 <= altitude <= 921) != (not (285 <= altitude <= 921)):
        triggered.add(182)
    # 变异规则 270 - SAR
    if (285 <= altitude <= 921) != (altitude >= 285 <= 921):
        triggered.add(183)
    # 原语句
    if 285 <= altitude <= 921:
        health_score += 5
        altitude = max(altitude - 15, 2)
        voltage_mv = min(voltage_mv + 6, 100)
    # 原语句28
    # 变异规则 271 - SVR
    if (49 <= altitude <= 490) != (49 <= voltage_mv <= 490):
        triggered.add(184)
    # 变异规则 272 - ROR
    if (49 <= altitude <= 490) != (49 <= speed <= 490):
        triggered.add(185)
    # 变异规则 273 - CAR
    if (49 <= altitude <= 490) != (50 <= altitude <= 490):
        t=1
    # 变异规则 274 - AOR
    if (49 <= altitude <= 490) != (49 <= abs(altitude) <= 490):
        t=1
    # 变异规则 275 - SAR
    if (49 <= altitude <= 490) != (altitude >= 49 <= 490):
        triggered.add(186)
    # 变异规则 276 - CSR
    if (49 <= altitude <= 490) != (-49 <= altitude <= 490):
        t=1
    # 变异规则 277 - RSR
    if (49 <= altitude <= 490) != (not (49 <= altitude <= 490)):
        triggered.add(187)
    # 变异规则 278 - UOI
    if (49 <= altitude <= 490) != (49 <= -altitude <= 490):
        triggered.add(188)
    # 变异规则 279 - CRP
    if (49 <= altitude <= 490) != (49 <= altitude <= 980):
        triggered.add(189)
    # 变异规则 280 - SRC
    if (49 <= altitude <= 490) != (49 <= altitude <= 487):
        triggered.add(190)
    # 原语句
    if 49 <= altitude <= 490:
        health_score += 20
        altitude = max(altitude - 37, 2)
    # 原语句29
    # 变异规则 281 - AOR
    if (voltage_mv <= 100) != (not (voltage_mv <= 100)):
        triggered.add(191)
    # 变异规则 282 - ABS
    if (voltage_mv <= 100) != (abs(voltage_mv) <= 100):
        t=1
    # 变异规则 283 - LCR
    if (voltage_mv <= 100) != (speed <= 100):
        t=1
    # 变异规则 284 - SRC
    if (voltage_mv <= 100) != (not (voltage_mv <= 100)):
        triggered.add(192)
    # 变异规则 285 - CRP
    if (voltage_mv <= 100) != (voltage_mv <= 200):
        t=1
    # 变异规则 286 - SVR
    if (voltage_mv <= 100) != (speed <= 100):
        t=1
    # 变异规则 287 - ROR
    if (voltage_mv <= 100) != (speed <= 100):
        t=1
    # 变异规则 288 - CAR
    if (voltage_mv <= 100) != (voltage_mv <= 102):
        t=1
    # 变异规则 289 - UOI
    if (voltage_mv <= 100) != (100 >= voltage_mv):
        t=1
    # 变异规则 290 - SAR
    if (voltage_mv <= 100) != (100 >= voltage_mv):
        t=1
    # 原语句
    if voltage_mv <= 100:
        health_score += 2
        speed = min(speed + 10, 100)
        voltage_mv = min(voltage_mv + 10, 100)
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句30
    # 变异规则 291 - SRC
    if (speed <= 10 or voltage_mv < 100) != (voltage_mv < 100 or speed <= 10):
        t=1
    # 变异规则 292 - ROR
    if (speed <= 10 or voltage_mv < 100) != (speed <= 10 or voltage_mv < 90):
        triggered.add(193)
    # 变异规则 293 - ABS
    if (speed <= 10 or voltage_mv < 100) != (abs(speed) <= 10 or voltage_mv < 100):
        t=1
    # 变异规则 294 - LCR
    if (speed <= 10 or voltage_mv < 100) != (speed <= 10 and voltage_mv < 100):
        triggered.add(194)
    # 变异规则 295 - CRP
    if (speed <= 10 or voltage_mv < 100) != (speed <= 10 or voltage_mv < 108):
        triggered.add(195)
    # 变异规则 296 - SCR
    if (speed <= 10 or voltage_mv < 100) != (speed <= 10 or 100 > voltage_mv):
        t=1
    # 变异规则 297 - RSR
    if (speed <= 10 or voltage_mv < 100) != (not (speed <= 10 or voltage_mv < 100)):
        triggered.add(196)
    # 变异规则 298 - CAR
    if (speed <= 10 or voltage_mv < 100) != (speed <= 15 or voltage_mv < 100):
        triggered.add(197)
    # 变异规则 299 - SAR
    if (speed <= 10 or voltage_mv < 100) != (speed <= 10 or 100 > voltage_mv):
        t=1
    # 变异规则 300 - AOR
    if (speed <= 10 or voltage_mv < 100) != (speed <= 10 and voltage_mv < 100):
        triggered.add(198)
    # 原语句
    if speed <= 10 or voltage_mv < 100:
        health_score -= 30
        speed = max(speed - 4, 2)
    return triggered

targetPaths = [
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 134, 143, 145, 146, 150, 155, 156, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 115, 117, 123, 124, 128, 134, 143, 145, 146, 150, 155, 156, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 27, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 115, 117, 123, 124, 128, 134, 143, 145, 146, 150, 155, 156, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 113, 114, 116, 123, 124, 128, 134, 143, 145, 146, 148, 149, 151, 153, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 40, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 114, 116, 123, 124, 128, 134, 143, 145, 146, 148, 149, 151, 153, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 54, 59, 60, 64, 68, 82, 84, 90, 95, 99, 108, 114, 116, 123, 124, 128, 134, 143, 145, 146, 148, 151, 153, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 55, 56, 57, 60, 64, 68, 82, 84, 90, 95, 99, 108, 114, 116, 123, 124, 128, 134, 143, 145, 146, 148, 151, 153, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 5, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 55, 56, 60, 64, 68, 82, 84, 90, 95, 99, 108, 114, 123, 124, 128, 134, 143, 145, 146, 148, 151, 153, 155, 158, 159, 160, 168, 171, 173, 176, 181, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 55, 56, 60, 64, 68, 82, 84, 90, 95, 99, 108, 114, 123, 124, 128, 134, 143, 145, 146, 152, 155, 158, 159, 160, 168, 171, 173, 176, 181, 187, 188, 191, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 55, 60, 64, 68, 82, 84, 90, 95, 99, 108, 114, 123, 124, 128, 134, 143, 145, 146, 152, 155, 158, 159, 161, 162, 165, 168, 171, 173, 176, 181, 187, 188, 191, 195, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 55, 60, 64, 68, 82, 84, 90, 95, 98, 99, 108, 114, 123, 124, 128, 134, 143, 145, 146, 152, 155, 158, 159, 161, 162, 165, 168, 171, 173, 176, 181, 187, 188, 191, 195, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 88, 95, 99, 108, 109, 114, 117, 123, 124, 128, 129, 134, 143, 145, 150, 155, 158, 159, 160, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 88, 95, 97, 98, 99, 101, 103, 108, 109, 114, 117, 123, 124, 128, 134, 143, 145, 150, 155, 158, 159, 161, 162, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 58, 59, 60, 64, 68, 72, 77, 82, 84, 88, 95, 99, 105, 108, 109, 112, 114, 116, 123, 124, 128, 134, 143, 145, 148, 151, 153, 155, 158, 159, 161, 162, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 88, 95, 99, 108, 109, 114, 117, 123, 124, 128, 129, 134, 142, 143, 144, 147, 150, 155, 158, 159, 160, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 89, 90, 95, 99, 108, 109, 114, 117, 123, 124, 128, 129, 134, 142, 143, 144, 147, 150, 155, 158, 159, 160, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 90, 95, 99, 108, 109, 114, 117, 123, 124, 128, 129, 132, 134, 142, 143, 147, 150, 155, 158, 159, 160, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 90, 95, 99, 108, 109, 114, 117, 123, 124, 128, 130, 132, 133, 134, 143, 144, 147, 148, 150, 155, 156, 158, 159, 160, 165, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 76, 78, 79, 82, 84, 90, 95, 99, 108, 109, 114, 117, 123, 124, 128, 129, 134, 142, 143, 147, 150, 155, 158, 159, 160, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 76, 78, 79, 82, 84, 90, 95, 99, 108, 109, 114, 117, 123, 124, 128, 129, 134, 142, 143, 147, 150, 155, 158, 159, 160, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 76, 78, 79, 82, 84, 90, 95, 99, 108, 109, 114, 117, 123, 124, 128, 129, 134, 141, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 79, 82, 84, 90, 95, 99, 105, 107, 108, 112, 114, 117, 123, 124, 128, 129, 134, 141, 143, 145, 146, 150, 155, 158, 159, 160, 168, 169, 170, 172, 173, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 82, 83, 84, 90, 95, 99, 105, 107, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 169, 170, 172, 173, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 6, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 82, 83, 84, 90, 95, 99, 105, 107, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 3, 4, 5, 6, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 82, 83, 84, 90, 95, 99, 105, 107, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 59, 60, 64, 68, 76, 78, 81, 82, 83, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 9, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 59, 60, 64, 68, 75, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 90, 95, 99, 108, 109, 114, 117, 123, 124, 128, 130, 132, 133, 134, 139, 143, 144, 147, 148, 150, 155, 156, 158, 159, 160, 165, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 95, 99, 108, 109, 114, 117, 123, 124, 128, 130, 132, 133, 134, 143, 144, 147, 148, 150, 155, 156, 158, 159, 160, 165, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 193, 194, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 78, 82, 84, 95, 99, 108, 109, 112, 114, 117, 123, 124, 128, 130, 132, 133, 134, 140, 143, 144, 147, 148, 150, 155, 156, 158, 159, 160, 165, 168, 171, 173, 174, 176, 181, 184, 185, 187, 188, 191, 195, 196},
    {1, 9, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 78, 82, 84, 95, 99, 108, 109, 112, 114, 117, 123, 124, 128, 130, 132, 133, 134, 135, 136, 139, 140, 143, 144, 147, 148, 150, 155, 156, 158, 159, 160, 165, 168, 169, 170, 173, 176, 181, 184, 185, 187, 188, 191, 194, 196},
    {1, 9, 10, 13, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 39, 43, 45, 48, 49, 50, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 15, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 52, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 15, 17, 21, 24, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 43, 45, 48, 49, 50, 52, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 82, 83, 84, 95, 99, 105, 107, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 177, 178, 179, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 79, 82, 84, 95, 99, 105, 107, 108, 112, 114, 117, 123, 124, 128, 129, 134, 136, 138, 141, 143, 145, 146, 150, 155, 158, 159, 160, 168, 169, 170, 172, 173, 176, 181, 184, 185, 187, 188, 191, 196},
    {1, 8, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 79, 82, 84, 95, 99, 105, 107, 108, 112, 114, 117, 120, 123, 125, 127, 128, 134, 136, 138, 141, 143, 145, 146, 150, 155, 158, 159, 160, 168, 169, 170, 172, 173, 176, 181, 184, 185, 187, 188, 191, 196},
    {1, 8, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 79, 82, 84, 95, 99, 105, 107, 108, 112, 114, 117, 120, 123, 125, 128, 134, 136, 138, 141, 143, 145, 146, 150, 155, 158, 159, 160, 167, 168, 169, 170, 172, 173, 176, 178, 179, 184, 185, 187, 188, 191, 196},
    {1, 8, 10, 17, 21, 24, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 79, 82, 84, 95, 99, 105, 107, 108, 112, 114, 117, 120, 123, 125, 128, 134, 136, 138, 141, 143, 145, 146, 150, 155, 158, 159, 161, 162, 164, 165, 167, 168, 169, 170, 172, 173, 176, 178, 179, 184, 185, 187, 188, 191, 196},
    {1, 8, 10, 15, 17, 21, 24, 26, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 52, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 15, 17, 18, 19, 20, 21, 22, 28, 30, 31, 32, 34, 43, 45, 48, 49, 50, 52, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 15, 17, 18, 19, 20, 21, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 72, 77, 82, 84, 86, 88, 90, 95, 99, 108, 109, 112, 114, 117, 120, 123, 125, 128, 134, 136, 138, 142, 143, 145, 150, 155, 158, 159, 160, 165, 168, 169, 170, 173, 176, 181, 184, 185, 187, 188, 191, 196, 197},
    {1, 8, 10, 17, 18, 19, 20, 21, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 82, 83, 84, 95, 99, 105, 107, 108, 112, 114, 117, 120, 123, 125, 128, 134, 136, 138, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 178, 179, 185, 187, 188, 190, 191, 196},
    {1, 8, 10, 17, 18, 19, 20, 21, 28, 30, 31, 32, 34, 43, 45, 47, 49, 60, 64, 68, 76, 78, 82, 83, 84, 95, 99, 105, 107, 108, 112, 114, 117, 120, 123, 125, 128, 134, 136, 138, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 178, 179, 184, 186, 187, 189, 191, 196},
    {1, 8, 10, 15, 17, 18, 19, 20, 21, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 44, 46, 48, 49, 50, 52, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 8, 10, 15, 17, 18, 19, 20, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 64, 66, 68, 72, 77, 82, 84, 88, 90, 95, 99, 108, 109, 112, 114, 117, 120, 123, 125, 128, 134, 136, 138, 142, 143, 145, 150, 155, 158, 159, 160, 165, 168, 169, 170, 173, 176, 178, 179, 184, 185, 187, 188, 191, 196, 197},
    {1, 10, 11, 12, 17, 18, 19, 20, 21, 28, 30, 31, 32, 34, 44, 46, 48, 49, 50, 52, 59, 60, 64, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 117, 123, 124, 128, 129, 134, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196, 197},
    {1, 10, 11, 12, 15, 17, 18, 19, 20, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 64, 68, 76, 78, 79, 82, 84, 95, 99, 105, 107, 108, 112, 114, 117, 120, 122, 123, 125, 128, 134, 136, 138, 141, 143, 145, 146, 150, 155, 158, 159, 160, 168, 169, 170, 172, 173, 176, 178, 186, 187, 189, 191, 196},
    {1, 10, 12, 15, 17, 18, 19, 20, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 64, 68, 76, 78, 79, 82, 84, 95, 99, 105, 107, 108, 112, 114, 117, 121, 123, 126, 128, 129, 134, 136, 138, 141, 143, 145, 146, 150, 155, 158, 159, 160, 168, 169, 170, 172, 173, 176, 178, 186, 187, 189, 191, 196},
    {1, 10, 12, 15, 17, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 64, 68, 76, 78, 82, 83, 84, 95, 99, 105, 107, 108, 112, 114, 117, 121, 123, 128, 129, 134, 136, 138, 143, 145, 146, 150, 155, 158, 159, 160, 168, 171, 173, 176, 183, 184, 186, 187, 189, 191, 196, 197},
    {1, 10, 12, 17, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 64, 68, 69, 71, 73, 77, 82, 84, 88, 90, 95, 99, 108, 109, 112, 114, 117, 121, 123, 128, 134, 136, 138, 142, 143, 145, 150, 155, 158, 159, 160, 168, 169, 170, 173, 176, 178, 186, 187, 189, 191, 196, 197},
    {1, 10, 12, 15, 17, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 64, 68, 69, 70, 71, 73, 76, 78, 79, 82, 84, 95, 99, 108, 109, 112, 114, 117, 121, 123, 128, 134, 136, 138, 141, 143, 145, 146, 150, 155, 158, 159, 160, 168, 169, 170, 172, 173, 176, 178, 186, 187, 189, 191, 196},
    {1, 10, 12, 17, 21, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 44, 46, 48, 49, 50, 52, 59, 60, 64, 67, 68, 82, 84, 90, 95, 99, 105, 108, 112, 114, 115, 117, 123, 124, 128, 134, 143, 145, 146, 150, 155, 156, 158, 159, 160, 168, 171, 173, 176, 181, 185, 187, 188, 191, 196},
    {1, 10, 12, 17, 21, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 44, 46, 47, 49, 60, 64, 68, 72, 77, 82, 84, 88, 90, 93, 94, 99, 108, 109, 114, 116, 121, 123, 128, 134, 136, 138, 142, 143, 145, 148, 149, 151, 153, 155, 158, 159, 160, 165, 168, 169, 170, 173, 176, 183, 186, 187, 189, 191, 196, 197},
    {1, 10, 12, 17, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 64, 68, 72, 77, 82, 84, 88, 90, 94, 96, 99, 108, 109, 112, 114, 117, 121, 123, 128, 134, 136, 138, 142, 143, 145, 150, 155, 158, 159, 160, 168, 169, 170, 173, 176, 183, 186, 187, 189, 191, 196, 197},
    {1, 10, 12, 17, 21, 28, 30, 31, 32, 34, 44, 46, 47, 49, 60, 61, 64, 65, 66, 67, 68, 72, 77, 82, 84, 88, 90, 94, 96, 99, 108, 109, 112, 114, 117, 121, 123, 128, 134, 136, 138, 142, 143, 145, 150, 155, 158, 159, 160, 168, 169, 170, 173, 176, 183, 186, 187, 189, 191, 196, 197}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 3:3, 4:4, 7:5, 9:6, 10:7, 11:8, 12:9, 13:10, 14:11, 16:12, 17:13, 18:14, 19:15, 20:16, 21:17, 22:18, 23:19, 24:20, 25:21, 26:22, 27:23, 28:24, 29:25, 30:26, 31:27, 33:28, 35:29, 43:30, 47:31, 50:32, 51:33, 52:34, 53:35, 54:36, 55:37, 56:38, 57:39, 58:40, 59:41, 60:42, 63:43, 64:44, 66:45, 69:46, 72:47, 73:48, 76:49, 77:50, 78:51, 79:52, 80:53, 82:54, 83:55, 84:56, 87:57, 88:58, 89:59, 90:60, 91:61, 92:62, 93:63, 95:64, 97:65, 98:66, 99:67, 101:68, 102:69, 104:70, 106:71, 108:72, 109:73, 110:74, 111:75, 112:76, 113:77, 115:78, 116:79, 117:80, 118:81, 119:82, 120:83, 122:84, 125:85, 127:86, 130:87, 131:88, 132:89, 133:90, 135:91, 140:92, 141:93, 142:94, 148:95, 149:96, 151:97, 153:98, 154:99, 155:100, 156:101, 157:102, 158:103, 160:104, 164:105, 165:106, 166:107, 167:108, 168:109, 169:110, 170:111, 171:112, 172:113, 173:114, 174:115, 175:116, 176:117, 177:118, 180:119, 181:120, 182:121, 183:122, 185:123, 186:124, 187:125, 188:126, 190:127, 192:128, 193:129, 196:130, 197:131, 198:132, 200:133, 201:134, 202:135, 204:136, 205:137, 207:138, 209:139, 210:140, 211:141, 212:142, 213:143, 215:144, 216:145, 218:146, 219:147, 221:148, 222:149, 223:150, 224:151, 225:152, 226:153, 227:154, 228:155, 229:156, 230:157, 234:158, 239:159, 241:160, 242:161, 243:162, 244:163, 245:164, 246:165, 247:166, 249:167, 250:168, 253:169, 254:170, 255:171, 256:172, 257:173, 259:174, 260:175, 261:176, 262:177, 264:178, 265:179, 266:180, 267:181, 269:182, 270:183, 271:184, 272:185, 275:186, 277:187, 278:188, 279:189, 280:190, 281:191, 284:192, 292:193, 294:194, 295:195, 297:196, 298:197, 300:198}

    rule_expressions[1] = "(speed != 58) != (not (speed != 58))"
    rule_expressions[2] = "(speed != 58) != (not (speed != 58))"
    rule_expressions[3] = "(speed != 58) != (speed != -58)"
    rule_expressions[4] = "(speed != 58) != (altitude != 58)"
    rule_expressions[5] = "(speed != 58) != (voltage_mv != 58)"
    rule_expressions[6] = "(speed != 58) != (speed != 56)"
    rule_expressions[7] = "(speed != 58) != (not (speed != 58))"
    rule_expressions[8] = "(33 <= altitude <= 664) != (33 <= -altitude <= 664)"
    rule_expressions[9] = "(33 <= altitude <= 664) != (-33 <= altitude <= 664)"
    rule_expressions[10] = "(33 <= altitude <= 664) != (not (33 <= altitude <= 664))"
    rule_expressions[11] = "(33 <= altitude <= 664) != (33 <= altitude <= 674)"
    rule_expressions[12] = "(33 <= altitude <= 664) != (altitude >= 33 <= 664)"
    rule_expressions[13] = "(33 <= altitude <= 664) != (31 <= altitude <= 664)"
    rule_expressions[14] = "(33 <= altitude <= 664) != (33 <= -altitude <= 664)"
    rule_expressions[15] = "(33 <= altitude <= 664) != (33 <= speed <= 664)"
    rule_expressions[16] = "(33 <= altitude <= 664) != (-33 <= altitude <= 664)"
    rule_expressions[17] = "(259 <= altitude <= 690) != (not (259) <= altitude <= 690)"
    rule_expressions[18] = "(259 <= altitude <= 690) != (259 <= voltage_mv <= 690)"
    rule_expressions[19] = "(259 <= altitude <= 690) != (259 <= -altitude <= 690)"
    rule_expressions[20] = "(259 <= altitude <= 690) != (259 <= altitude <= -690)"
    rule_expressions[21] = "(259 <= altitude <= 690) != (not (259 <= altitude <= 690))"
    rule_expressions[22] = "(259 <= altitude <= 690) != (261 <= altitude <= 690)"
    rule_expressions[23] = "(259 <= altitude <= 690) != (259 <= -altitude <= 690)"
    rule_expressions[24] = "(259 <= altitude <= 690) != (-259 <= altitude <= 690)"
    rule_expressions[25] = "(259 <= altitude <= 690) != (259 <= altitude <= -690)"
    rule_expressions[26] = "(259 <= altitude <= 690) != (249 <= altitude <= 690)"
    rule_expressions[27] = "(speed * 100 == voltage_mv) != (speed * voltage_mv == 100)"
    rule_expressions[28] = "(speed * 100 == voltage_mv) != (not (speed * 100 == voltage_mv))"
    rule_expressions[29] = "(speed * 100 == voltage_mv) != (not (speed * 100 == voltage_mv))"
    rule_expressions[30] = "(speed // altitude < 95) != (not (speed // altitude < 95))"
    rule_expressions[31] = "(speed // altitude < 95) != (speed // altitude < -95)"
    rule_expressions[32] = "(speed // altitude < 95) != (speed // 95 > altitude)"
    rule_expressions[33] = "(voltage_mv * 50 == altitude) != (voltage_mv * -50 == altitude)"
    rule_expressions[34] = "(voltage_mv * 50 == altitude) != (not (voltage_mv * 50 == altitude))"
    rule_expressions[35] = "(voltage_mv * 50 == altitude) != (voltage_mv * 51 == altitude)"
    rule_expressions[36] = "(voltage_mv * 50 == altitude) != (not (voltage_mv * 50 == altitude))"
    rule_expressions[37] = "(voltage_mv * 50 == altitude) != (altitude * 50 == altitude)"
    rule_expressions[38] = "(voltage_mv * 50 == altitude) != (voltage_mv * 52 == altitude)"
    rule_expressions[39] = "(voltage_mv * 50 == altitude) != (voltage_mv * 25 == altitude)"
    rule_expressions[40] = "(voltage_mv * 50 == altitude) != (voltage_mv * altitude == 50)"
    rule_expressions[41] = "(voltage_mv * 50 == altitude) != (voltage_mv * -50 == altitude)"
    rule_expressions[42] = "(voltage_mv * 50 == altitude) != (voltage_mv * -50 == altitude)"
    rule_expressions[43] = "(altitude >= 355 or altitude > 1000) != (altitude >= 355 or altitude > -1000)"
    rule_expressions[44] = "(altitude >= 355 or altitude > 1000) != (voltage_mv >= 355 or altitude > 1000)"
    rule_expressions[45] = "(altitude >= 355 or altitude > 1000) != (altitude >= -355 or altitude > 1000)"
    rule_expressions[46] = "(altitude >= 355 or altitude > 1000) != (altitude >= 355 and altitude > 1000)"
    rule_expressions[47] = "(speed <= 97 and speed == 2) != (speed <= 97 or speed == 2)"
    rule_expressions[48] = "(speed <= 97 and speed == 2) != (speed <= 97 and speed == -2)"
    rule_expressions[49] = "(speed <= 97 and speed == 2) != (not (speed <= 97 and speed == 2))"
    rule_expressions[50] = "(speed <= 97 and speed == 2) != (speed <= 97 and speed == 1)"
    rule_expressions[51] = "(speed <= 97 and speed == 2) != (speed <= 97 and speed == -2)"
    rule_expressions[52] = "(speed <= 97 and speed == 2) != (altitude <= 97 and speed == 2)"
    rule_expressions[53] = "(speed <= 97 and speed == 2) != (speed <= 97 and speed == -2)"
    rule_expressions[54] = "(speed >= 65 and voltage_mv > 40) != (speed >= 65 and voltage_mv > 32)"
    rule_expressions[55] = "(speed >= 65 and voltage_mv > 40) != (speed >= 65 and -voltage_mv > 40)"
    rule_expressions[56] = "(speed >= 65 and voltage_mv > 40) != (voltage_mv >= 65 and voltage_mv > 40)"
    rule_expressions[57] = "(speed >= 65 and voltage_mv > 40) != (speed >= 65 and voltage_mv > 42)"
    rule_expressions[58] = "(speed >= 65 and voltage_mv > 40) != (speed >= -65 and voltage_mv > 40)"
    rule_expressions[59] = "(speed >= 65 and voltage_mv > 40) != (speed >= 65 or voltage_mv > 40)"
    rule_expressions[60] = "(speed >= 65 and voltage_mv > 40) != (not (speed >= 65 and voltage_mv > 40))"
    rule_expressions[61] = "(altitude != 1000) != (altitude != -1000)"
    rule_expressions[62] = "(altitude != 1000) != (altitude != -1000)"
    rule_expressions[63] = "(altitude != 1000) != (altitude != -1000)"
    rule_expressions[64] = "(altitude != 1000) != (not (altitude != 1000))"
    rule_expressions[65] = "(altitude != 1000) != (voltage_mv != 1000)"
    rule_expressions[66] = "(altitude != 1000) != (altitude != 500)"
    rule_expressions[67] = "(altitude != 1000) != (speed != 1000)"
    rule_expressions[68] = "(altitude != 842 or speed > 30) != (not (altitude != 842 or speed > 30))"
    rule_expressions[69] = "(altitude != 842 or speed > 30) != (speed != 842 or speed > 30)"
    rule_expressions[70] = "(altitude != 842 or speed > 30) != (altitude != 842 or speed > 29)"
    rule_expressions[71] = "(altitude != 842 or speed > 30) != (altitude != 852 or speed > 30)"
    rule_expressions[72] = "(altitude != 842 or speed > 30) != (altitude != 842 and speed > 30)"
    rule_expressions[73] = "(altitude != 842 or speed > 30) != (altitude != 842 or speed > -30)"
    rule_expressions[74] = "(altitude != 842 or speed > 30) != (not (altitude != 842 or speed > 30))"
    rule_expressions[75] = "(22 <= speed <= 88) != (22 <= speed <= 93)"
    rule_expressions[76] = "(22 <= speed <= 88) != (22 <= -speed <= 88)"
    rule_expressions[77] = "(22 <= speed <= 88) != (-22 <= speed <= 88)"
    rule_expressions[78] = "(22 <= speed <= 88) != (22 <= altitude <= 88)"
    rule_expressions[79] = "(22 <= speed <= 88) != (44 <= speed <= 88)"
    rule_expressions[80] = "(22 <= speed <= 88) != (22 <= -speed <= 88)"
    rule_expressions[81] = "(22 <= speed <= 88) != (22 <= speed <= 83)"
    rule_expressions[82] = "(22 <= speed <= 88) != (not (22 <= speed <= 88))"
    rule_expressions[83] = "(22 <= speed <= 88) != (22 <= speed <= 44)"
    rule_expressions[84] = "(voltage_mv // speed != 95) != (not (voltage_mv // speed != 95))"
    rule_expressions[85] = "(voltage_mv // speed != 95) != (not (voltage_mv // speed != 95))"
    rule_expressions[86] = "(voltage_mv // speed != 95) != (altitude // speed != 95)"
    rule_expressions[87] = "(voltage_mv // speed != 95) != (not (voltage_mv // speed != 95))"
    rule_expressions[88] = "(voltage_mv <= 5) != (voltage_mv <= -5)"
    rule_expressions[89] = "(voltage_mv <= 5) != (voltage_mv <= 10)"
    rule_expressions[90] = "(voltage_mv <= 5) != (altitude <= 5)"
    rule_expressions[91] = "(voltage_mv <= 5) != (voltage_mv <= -5)"
    rule_expressions[92] = "(voltage_mv <= 5) != (voltage_mv <= 10)"
    rule_expressions[93] = "(altitude > 953 and altitude <= 1000) != (altitude > 963 and altitude <= 1000)"
    rule_expressions[94] = "(altitude > 953 and altitude <= 1000) != (voltage_mv > 953 and altitude <= 1000)"
    rule_expressions[95] = "(altitude > 953 and altitude <= 1000) != (altitude > 953 or altitude <= 1000)"
    rule_expressions[96] = "(altitude > 953 and altitude <= 1000) != (altitude > 953 and altitude <= 998)"
    rule_expressions[97] = "(speed - voltage_mv == 20) != (speed - voltage_mv == 24)"
    rule_expressions[98] = "(speed - voltage_mv == 20) != (speed - voltage_mv == -20)"
    rule_expressions[99] = "(speed - voltage_mv == 20) != (not (speed - voltage_mv == 20))"
    rule_expressions[100] = "(speed - voltage_mv == 20) != (not (speed - voltage_mv == 20))"
    rule_expressions[101] = "(speed - voltage_mv == 20) != (altitude - voltage_mv == 20)"
    rule_expressions[102] = "(speed - voltage_mv == 20) != (altitude - voltage_mv == 20)"
    rule_expressions[103] = "(speed - voltage_mv == 20) != (speed - voltage_mv == 21)"
    rule_expressions[104] = "(speed - voltage_mv == 20) != (speed - voltage_mv == -20)"
    rule_expressions[105] = "(voltage_mv >= 36) != (speed >= 36)"
    rule_expressions[106] = "(voltage_mv >= 36) != (speed >= 36)"
    rule_expressions[107] = "(voltage_mv >= 36) != (voltage_mv >= 72)"
    rule_expressions[108] = "(voltage_mv >= 36) != (not (voltage_mv >= 36))"
    rule_expressions[109] = "(voltage_mv >= 36) != (voltage_mv >= -36)"
    rule_expressions[110] = "(voltage_mv >= 36) != (not (voltage_mv >= 36))"
    rule_expressions[111] = "(voltage_mv >= 36) != (not (voltage_mv >= 36))"
    rule_expressions[112] = "(speed <= 26) != (altitude <= 26)"
    rule_expressions[113] = "(speed <= 26) != (speed <= 27)"
    rule_expressions[114] = "(speed <= 26) != (not (speed <= 26))"
    rule_expressions[115] = "(speed <= 26) != (speed <= 21)"
    rule_expressions[116] = "(speed <= 26) != (speed <= 52)"
    rule_expressions[117] = "(speed <= 26) != (speed <= -26)"
    rule_expressions[118] = "(speed <= 26) != (altitude <= 26)"
    rule_expressions[119] = "(speed <= 26) != (speed <= -26)"
    rule_expressions[120] = "(245 <= altitude <= 786) != (245 <= speed <= 786)"
    rule_expressions[121] = "(245 <= altitude <= 786) != (altitude >= 245 <= 786)"
    rule_expressions[122] = "(245 <= altitude <= 786) != (245 <= altitude <= 780)"
    rule_expressions[123] = "(245 <= altitude <= 786) != (not (245 <= altitude <= 786))"
    rule_expressions[124] = "(245 <= altitude <= 786) != (-245 <= altitude <= 786)"
    rule_expressions[125] = "(245 <= altitude <= 786) != (245 <= voltage_mv <= 786)"
    rule_expressions[126] = "(245 <= altitude <= 786) != (245 <= altitude <= 796)"
    rule_expressions[127] = "(245 <= altitude <= 786) != (247 <= altitude <= 786)"
    rule_expressions[128] = "(voltage_mv != 20 or speed != 5) != (not (voltage_mv != 20 or speed != 5))"
    rule_expressions[129] = "(voltage_mv != 20 or speed != 5) != (voltage_mv != 20 and speed != 5)"
    rule_expressions[130] = "(voltage_mv != 20 or speed != 5) != (voltage_mv != 20 or speed != 12)"
    rule_expressions[131] = "(voltage_mv != 20 or speed != 5) != (not (voltage_mv != 20 or speed != 5))"
    rule_expressions[132] = "(voltage_mv != 20 or speed != 5) != (voltage_mv != 15 or speed != 5)"
    rule_expressions[133] = "(voltage_mv != 20 or speed != 5) != (voltage_mv != 20 or -speed != 5)"
    rule_expressions[134] = "(altitude < 200 and altitude != 50) != (not (altitude < 200 and altitude != 50))"
    rule_expressions[135] = "(altitude < 200 and altitude != 50) != (altitude < 200 and -altitude != 50)"
    rule_expressions[136] = "(altitude < 200 and altitude != 50) != (altitude < 200 or altitude != 50)"
    rule_expressions[137] = "(altitude < 200 and altitude != 50) != (altitude < 200 and -altitude != 50)"
    rule_expressions[138] = "(altitude < 200 and altitude != 50) != (voltage_mv < 200 and altitude != 50)"
    rule_expressions[139] = "(altitude < 200 and altitude != 50) != (altitude < 200 and altitude != 25)"
    rule_expressions[140] = "(altitude < 200 and altitude != 50) != (altitude < 200 and altitude != 49)"
    rule_expressions[141] = "(speed >= 5 and speed <= 28) != (speed >= 5 and speed <= 36)"
    rule_expressions[142] = "(speed >= 5 and speed <= 28) != (altitude >= 5 and speed <= 28)"
    rule_expressions[143] = "(speed >= 5 and speed <= 28) != (not (speed >= 5 and speed <= 28))"
    rule_expressions[144] = "(speed >= 5 and speed <= 28) != (speed >= 15 and speed <= 28)"
    rule_expressions[145] = "(speed >= 5 and speed <= 28) != (speed >= 5 or speed <= 28)"
    rule_expressions[146] = "(speed >= 5 and speed <= 28) != (speed >= 5 and -speed <= 28)"
    rule_expressions[147] = "(speed >= 5 and speed <= 28) != (speed >= 5 and speed <= -28)"
    rule_expressions[148] = "(22 <= voltage_mv <= 61) != (22 <= altitude <= 61)"
    rule_expressions[149] = "(22 <= voltage_mv <= 61) != (29 <= voltage_mv <= 61)"
    rule_expressions[150] = "(22 <= voltage_mv <= 61) != (-22 <= voltage_mv <= 61)"
    rule_expressions[151] = "(22 <= voltage_mv <= 61) != (22 <= -voltage_mv <= 61)"
    rule_expressions[152] = "(22 <= voltage_mv <= 61) != (voltage_mv >= 22 <= 61)"
    rule_expressions[153] = "(22 <= voltage_mv <= 61) != (22 <= voltage_mv <= -61)"
    rule_expressions[154] = "(22 <= voltage_mv <= 61) != (voltage_mv >= 22 <= 61)"
    rule_expressions[155] = "(22 <= voltage_mv <= 61) != (not (22 <= voltage_mv <= 61))"
    rule_expressions[156] = "(22 <= voltage_mv <= 61) != (11 <= voltage_mv <= 61)"
    rule_expressions[157] = "(22 <= voltage_mv <= 61) != (22 <= voltage_mv <= -61)"
    rule_expressions[158] = "(altitude >= 1000) != (altitude >= -1000)"
    rule_expressions[159] = "(altitude >= 1000) != (not (altitude >= 1000))"
    rule_expressions[160] = "(altitude % 328 < voltage_mv) != (altitude % -328 < voltage_mv)"
    rule_expressions[161] = "(altitude % 328 < voltage_mv) != (altitude % voltage_mv > 328)"
    rule_expressions[162] = "(altitude % 328 < voltage_mv) != (altitude % 328 < -voltage_mv)"
    rule_expressions[163] = "(altitude % 328 < voltage_mv) != (altitude % -328 < voltage_mv)"
    rule_expressions[164] = "(altitude % 328 < voltage_mv) != (altitude % 338 < voltage_mv)"
    rule_expressions[165] = "(altitude % 328 < voltage_mv) != (speed % 328 < voltage_mv)"
    rule_expressions[166] = "(altitude % 328 < voltage_mv) != (altitude % 338 < voltage_mv)"
    rule_expressions[167] = "(altitude % 328 < voltage_mv) != (altitude % 318 < voltage_mv)"
    rule_expressions[168] = "(altitude % 328 < voltage_mv) != (not (altitude % 328 < voltage_mv))"
    rule_expressions[169] = "(altitude < 50 or speed >= 50) != (speed < 50 or speed >= 50)"
    rule_expressions[170] = "(altitude < 50 or speed >= 50) != (altitude < 50 or speed >= -50)"
    rule_expressions[171] = "(altitude < 50 or speed >= 50) != (altitude < 50 and speed >= 50)"
    rule_expressions[172] = "(altitude < 50 or speed >= 50) != (altitude < 50 or speed >= 25)"
    rule_expressions[173] = "(altitude < 50 or speed >= 50) != (not (altitude < 50 or speed >= 50))"
    rule_expressions[174] = "(altitude < 50 or speed >= 50) != (altitude < -50 or speed >= 50)"
    rule_expressions[175] = "(altitude < 50 or speed >= 50) != (altitude < 50 or speed >= 25)"
    rule_expressions[176] = "(285 <= altitude <= 921) != (not (285 <= altitude <= 921))"
    rule_expressions[177] = "(285 <= altitude <= 921) != (287 <= altitude <= 921)"
    rule_expressions[178] = "(285 <= altitude <= 921) != (285 <= -altitude <= 921)"
    rule_expressions[179] = "(285 <= altitude <= 921) != (570 <= altitude <= 921)"
    rule_expressions[180] = "(285 <= altitude <= 921) != (285 <= -altitude <= 921)"
    rule_expressions[181] = "(285 <= altitude <= 921) != (-285 <= altitude <= 921)"
    rule_expressions[182] = "(285 <= altitude <= 921) != (not (285 <= altitude <= 921))"
    rule_expressions[183] = "(285 <= altitude <= 921) != (altitude >= 285 <= 921)"
    rule_expressions[184] = "(49 <= altitude <= 490) != (49 <= voltage_mv <= 490)"
    rule_expressions[185] = "(49 <= altitude <= 490) != (49 <= speed <= 490)"
    rule_expressions[186] = "(49 <= altitude <= 490) != (altitude >= 49 <= 490)"
    rule_expressions[187] = "(49 <= altitude <= 490) != (not (49 <= altitude <= 490))"
    rule_expressions[188] = "(49 <= altitude <= 490) != (49 <= -altitude <= 490)"
    rule_expressions[189] = "(49 <= altitude <= 490) != (49 <= altitude <= 980)"
    rule_expressions[190] = "(49 <= altitude <= 490) != (49 <= altitude <= 487)"
    rule_expressions[191] = "(voltage_mv <= 100) != (not (voltage_mv <= 100))"
    rule_expressions[192] = "(voltage_mv <= 100) != (not (voltage_mv <= 100))"
    rule_expressions[193] = "(speed <= 10 or voltage_mv < 100) != (speed <= 10 or voltage_mv < 90)"
    rule_expressions[194] = "(speed <= 10 or voltage_mv < 100) != (speed <= 10 and voltage_mv < 100)"
    rule_expressions[195] = "(speed <= 10 or voltage_mv < 100) != (speed <= 10 or voltage_mv < 108)"
    rule_expressions[196] = "(speed <= 10 or voltage_mv < 100) != (not (speed <= 10 or voltage_mv < 100))"
    rule_expressions[197] = "(speed <= 10 or voltage_mv < 100) != (speed <= 15 or voltage_mv < 100)"
    rule_expressions[198] = "(speed <= 10 or voltage_mv < 100) != (speed <= 10 and voltage_mv < 100)"

    return rule_expressions