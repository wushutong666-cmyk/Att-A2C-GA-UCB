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
    # 变异规则 1 - SAR
    if (15 <= speed <= 97) != (speed >= 15 <= 97):
        triggered.add(1)
    # 变异规则 2 - SVR
    if (15 <= speed <= 97) != (15 <= voltage_mv <= 97):
        triggered.add(2)
    # 变异规则 3 - ABS
    if (15 <= speed <= 97) != (15 <= abs(speed) <= 97):
        t=1
    # 变异规则 4 - LCR
    if (15 <= speed <= 97) != (-15 <= speed <= 97):
        triggered.add(3)
    # 变异规则 5 - SRC
    if (15 <= speed <= 97) != (15 <= speed <= -97):
        triggered.add(4)
    # 变异规则 6 - CSR
    if (15 <= speed <= 97) != (-15 <= speed <= 97):
        triggered.add(5)
    # 变异规则 7 - AOR
    if (15 <= speed <= 97) != (speed >= 15 <= 97):
        triggered.add(6)
    # 变异规则 8 - CRP
    if (15 <= speed <= 97) != (21 <= speed <= 97):
        triggered.add(7)
    # 变异规则 9 - SCR
    if (15 <= speed <= 97) != (15 <= -speed <= 97):
        triggered.add(8)
    # 变异规则 10 - ROR
    if (15 <= speed <= 97) != (15 <= -speed <= 97):
        triggered.add(9)
    # 原语句
    if 15 <= speed <= 97:
        health_score -= 24
        speed = min(speed + 2, 100)
    # 原语句2
    # 变异规则 11 - SVR
    if (voltage_mv >= 30 or voltage_mv <= 9) != (altitude >= 30 or voltage_mv <= 9):
        triggered.add(10)
    # 变异规则 12 - CAR
    if (voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 or voltage_mv <= 4):
        triggered.add(11)
    # 变异规则 13 - RSR
    if (voltage_mv >= 30 or voltage_mv <= 9) != (not (voltage_mv >= 30 or voltage_mv <= 9)):
        triggered.add(12)
    # 变异规则 14 - UOI
    if (voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 or -voltage_mv <= 9):
        triggered.add(13)
    # 变异规则 15 - CRP
    if (voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 34 or voltage_mv <= 9):
        triggered.add(14)
    # 变异规则 16 - LCR
    if (voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 and voltage_mv <= 9):
        triggered.add(15)
    # 变异规则 17 - ABS
    if (voltage_mv >= 30 or voltage_mv <= 9) != (abs(voltage_mv) >= 30 or voltage_mv <= 9):
        t=1
    # 变异规则 18 - CSR
    if (voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= -30 or voltage_mv <= 9):
        triggered.add(16)
    # 变异规则 19 - AOR
    if (voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 or -voltage_mv <= 9):
        triggered.add(17)
    # 变异规则 20 - SRC
    if (voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv <= 9 or voltage_mv >= 30):
        t=1
    # 原语句
    if voltage_mv >= 30 or voltage_mv <= 9:
        health_score -= 4
        altitude = min(altitude + 57, 1000)
    # 原语句3
    # 变异规则 21 - SAR
    if (voltage_mv > 10) != (10 < voltage_mv):
        t=1
    # 变异规则 22 - SRC
    if (voltage_mv > 10) != (abs(voltage_mv) > 10):
        t=1
    # 变异规则 23 - ROR
    if (voltage_mv > 10) != (voltage_mv > 20):
        triggered.add(18)
    # 变异规则 24 - AOR
    if (voltage_mv > 10) != (10 < voltage_mv):
        t=1
    # 变异规则 25 - CRP
    if (voltage_mv > 10) != (voltage_mv > 5):
        triggered.add(19)
    # 变异规则 26 - CAR
    if (voltage_mv > 10) != (voltage_mv > 15):
        triggered.add(20)
    # 变异规则 27 - SVR
    if (voltage_mv > 10) != (altitude > 10):
        triggered.add(21)
    # 变异规则 28 - RSR
    if (voltage_mv > 10) != (not (voltage_mv > 10)):
        triggered.add(22)
    # 变异规则 29 - UOI
    if (voltage_mv > 10) != (altitude > 10):
        triggered.add(23)
    # 变异规则 30 - LCR
    if (voltage_mv > 10) != (not (voltage_mv > 10)):
        triggered.add(24)
    # 原语句
    if voltage_mv > 10:
        health_score += 19
        voltage_mv = min(voltage_mv + 2, 100)
    # 原语句4
    # 变异规则 31 - SVR
    if (speed != 2) != (altitude != 2):
        triggered.add(25)
    # 变异规则 32 - CSR
    if (speed != 2) != (speed != -2):
        triggered.add(26)
    # 变异规则 33 - CAR
    if (speed != 2) != (speed != 7):
        triggered.add(27)
    # 变异规则 34 - ROR
    if (speed != 2) != (abs(speed) != 2):
        t=1
    # 变异规则 35 - RSR
    if (speed != 2) != (not (speed != 2)):
        triggered.add(28)
    # 变异规则 36 - LCR
    if (speed != 2) != (not (speed != 2)):
        triggered.add(29)
    # 变异规则 37 - CRP
    if (speed != 2) != (speed != 1):
        triggered.add(30)
    # 变异规则 38 - UOI
    if (speed != 2) != (not (speed != 2)):
        triggered.add(31)
    # 变异规则 39 - SRC
    if (speed != 2) != (speed != 7):
        triggered.add(32)
    # 变异规则 40 - AOR
    if (speed != 2) != (not (speed != 2)):
        triggered.add(33)
    # 原语句
    if speed != 2:
        health_score -= 29
    # 原语句5
    # 变异规则 41 - RSR
    if (voltage_mv >= 100) != (not (voltage_mv >= 100)):
        triggered.add(34)
    # 变异规则 42 - CAR
    if (voltage_mv >= 100) != (voltage_mv >= 99):
        triggered.add(35)
    # 变异规则 43 - CSR
    if (voltage_mv >= 100) != (voltage_mv >= -100):
        triggered.add(36)
    # 变异规则 44 - ROR
    if (voltage_mv >= 100) != (speed >= 100):
        triggered.add(37)
    # 变异规则 45 - CRP
    if (voltage_mv >= 100) != (voltage_mv >= 95):
        triggered.add(38)
    # 变异规则 46 - ABS
    if (voltage_mv >= 100) != (abs(voltage_mv) >= 100):
        t=1
    # 变异规则 47 - AOR
    if (voltage_mv >= 100) != (voltage_mv >= 95):
        triggered.add(39)
    # 变异规则 48 - SCR
    if (voltage_mv >= 100) != (voltage_mv >= 93):
        triggered.add(40)
    # 变异规则 49 - SRC
    if (voltage_mv >= 100) != (voltage_mv >= 99):
        triggered.add(41)
    # 变异规则 50 - UOI
    if (voltage_mv >= 100) != (voltage_mv >= -100):
        triggered.add(42)
    # 原语句
    if voltage_mv >= 100:
        speed = min(speed + 9, 100)
        altitude, speed = speed, altitude
    # 原语句6
    # 变异规则 51 - LCR
    if (altitude <= 100) != (abs(altitude) <= 100):
        t=1
    # 变异规则 52 - AOR
    if (altitude <= 100) != (altitude <= -100):
        triggered.add(43)
    # 变异规则 53 - ABS
    if (altitude <= 100) != (abs(altitude) <= 100):
        t=1
    # 变异规则 54 - ROR
    if (altitude <= 100) != (100 >= altitude):
        t=1
    # 变异规则 55 - CSR
    if (altitude <= 100) != (altitude <= -100):
        triggered.add(44)
    # 变异规则 56 - SAR
    if (altitude <= 100) != (100 >= altitude):
        t=1
    # 变异规则 57 - RSR
    if (altitude <= 100) != (not (altitude <= 100)):
        triggered.add(45)
    # 变异规则 58 - UOI
    if (altitude <= 100) != (altitude <= 94):
        triggered.add(46)
    # 变异规则 59 - CAR
    if (altitude <= 100) != (altitude <= 98):
        triggered.add(47)
    # 变异规则 60 - SCR
    if (altitude <= 100) != (not (altitude <= 100)):
        triggered.add(48)
    # 原语句
    if altitude <= 100:
        health_score += 15
        altitude = max(altitude - 14, 2)
    # 原语句7
    # 变异规则 61 - SVR
    if (voltage_mv < speed + 99) != (altitude < speed + 99):
        triggered.add(49)
    # 变异规则 62 - CAR
    if (voltage_mv < speed + 99) != (voltage_mv < speed + 101):
        t=1
    # 变异规则 63 - SAR
    if (voltage_mv < speed + 99) != (speed > voltage_mv + 99):
        triggered.add(50)
    # 变异规则 64 - UOI
    if (voltage_mv < speed + 99) != (voltage_mv < -speed + 99):
        triggered.add(51)
    # 变异规则 65 - SCR
    if (voltage_mv < speed + 99) != (speed > voltage_mv + 99):
        triggered.add(52)
    # 变异规则 66 - CRP
    if (voltage_mv < speed + 99) != (voltage_mv < speed + 95):
        triggered.add(53)
    # 变异规则 67 - ABS
    if (voltage_mv < speed + 99) != (voltage_mv < abs(speed) + 99):
        t=1
    # 变异规则 68 - RSR
    if (voltage_mv < speed + 99) != (not (voltage_mv < speed + 99)):
        triggered.add(54)
    # 变异规则 69 - AOR
    if (voltage_mv < speed + 99) != (voltage_mv < -speed + 99):
        triggered.add(55)
    # 变异规则 70 - ROR
    if (voltage_mv < speed + 99) != (voltage_mv < speed + 92):
        triggered.add(56)
    # 原语句
    if voltage_mv < speed + 99:
        health_score -= 10
        voltage_mv = min(voltage_mv + 10, 100)
    # 原语句8
    # 变异规则 71 - ROR
    if (voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 4 or voltage_mv <= 30):
        t=1
    # 变异规则 72 - SRC
    if (voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv <= 30 or voltage_mv < 2):
        t=1
    # 变异规则 73 - CAR
    if (voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 7 or voltage_mv <= 30):
        t=1
    # 变异规则 74 - CSR
    if (voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < -2 or voltage_mv <= 30):
        t=1
    # 变异规则 75 - UOI
    if (voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 2 or -voltage_mv <= 30):
        triggered.add(57)
    # 变异规则 76 - LCR
    if (voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 2 and voltage_mv <= 30):
        triggered.add(58)
    # 变异规则 77 - SAR
    if (voltage_mv < 2 or voltage_mv <= 30) != (2 > voltage_mv or voltage_mv <= 30):
        t=1
    # 变异规则 78 - CRP
    if (voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 2 or voltage_mv <= 15):
        triggered.add(59)
    # 变异规则 79 - SVR
    if (voltage_mv < 2 or voltage_mv <= 30) != (altitude < 2 or voltage_mv <= 30):
        t=1
    # 变异规则 80 - ABS
    if (voltage_mv < 2 or voltage_mv <= 30) != (abs(voltage_mv) < 2 or voltage_mv <= 30):
        t=1
    # 原语句
    if voltage_mv < 2 or voltage_mv <= 30:
        health_score += 8
        altitude = min(altitude + 95, 1000)
        speed = max(speed - 6, 2)
    # 原语句9
    # 变异规则 81 - SCR
    if (25 <= voltage_mv <= 77) != (not (25) <= voltage_mv <= 77):
        triggered.add(60)
    # 变异规则 82 - CAR
    if (25 <= voltage_mv <= 77) != (25 <= voltage_mv <= 67):
        triggered.add(61)
    # 变异规则 83 - AOR
    if (25 <= voltage_mv <= 77) != (25 <= voltage_mv <= 76):
        triggered.add(62)
    # 变异规则 84 - SAR
    if (25 <= voltage_mv <= 77) != (voltage_mv >= 25 <= 77):
        triggered.add(63)
    # 变异规则 85 - RSR
    if (25 <= voltage_mv <= 77) != (not (25 <= voltage_mv <= 77)):
        triggered.add(64)
    # 变异规则 86 - ABS
    if (25 <= voltage_mv <= 77) != (25 <= abs(voltage_mv) <= 77):
        t=1
    # 变异规则 87 - CSR
    if (25 <= voltage_mv <= 77) != (25 <= voltage_mv <= -77):
        triggered.add(65)
    # 变异规则 88 - LCR
    if (25 <= voltage_mv <= 77) != (25 <= speed <= 77):
        triggered.add(66)
    # 变异规则 89 - SVR
    if (25 <= voltage_mv <= 77) != (25 <= altitude <= 77):
        triggered.add(67)
    # 变异规则 90 - CRP
    if (25 <= voltage_mv <= 77) != (33 <= voltage_mv <= 77):
        triggered.add(68)
    # 原语句
    if 25 <= voltage_mv <= 77:
        health_score -= 18
        altitude = max(altitude - 45, 2)
        speed = min(speed + 8, 100)
        voltage_mv = max(voltage_mv - 3, 2)
        voltage_mv, speed = speed, voltage_mv
    # 原语句10
    # 变异规则 91 - CSR
    if (speed >= 20 or voltage_mv > 5) != (speed >= -20 or voltage_mv > 5):
        t=1
    # 变异规则 92 - CAR
    if (speed >= 20 or voltage_mv > 5) != (speed >= 18 or voltage_mv > 5):
        t=1
    # 变异规则 93 - AOR
    if (speed >= 20 or voltage_mv > 5) != (speed >= 20 or -voltage_mv > 5):
        triggered.add(69)
    # 变异规则 94 - SAR
    if (speed >= 20 or voltage_mv > 5) != (speed >= 20 or 5 < voltage_mv):
        t=1
    # 变异规则 95 - RSR
    if (speed >= 20 or voltage_mv > 5) != (not (speed >= 20 or voltage_mv > 5)):
        triggered.add(70)
    # 变异规则 96 - UOI
    if (speed >= 20 or voltage_mv > 5) != (speed >= 20 or -voltage_mv > 5):
        triggered.add(71)
    # 变异规则 97 - SVR
    if (speed >= 20 or voltage_mv > 5) != (voltage_mv >= 20 or voltage_mv > 5):
        t=1
    # 变异规则 98 - SCR
    if (speed >= 20 or voltage_mv > 5) != (speed >= 20 or -voltage_mv > 5):
        triggered.add(72)
    # 变异规则 99 - ABS
    if (speed >= 20 or voltage_mv > 5) != (abs(speed) >= 20 or voltage_mv > 5):
        t=1
    # 变异规则 100 - CRP
    if (speed >= 20 or voltage_mv > 5) != (speed >= 11 or voltage_mv > 5):
        t=1
    # 原语句
    if speed >= 20 or voltage_mv > 5:
        health_score -= 13
    # 原语句11
    # 变异规则 101 - SRC
    if (30 <= voltage_mv <= 90) != (voltage_mv >= 30 <= 90):
        triggered.add(73)
    # 变异规则 102 - RSR
    if (30 <= voltage_mv <= 90) != (not (30 <= voltage_mv <= 90)):
        triggered.add(74)
    # 变异规则 103 - SVR
    if (30 <= voltage_mv <= 90) != (30 <= speed <= 90):
        triggered.add(75)
    # 变异规则 104 - CSR
    if (30 <= voltage_mv <= 90) != (-30 <= voltage_mv <= 90):
        triggered.add(76)
    # 变异规则 105 - SCR
    if (30 <= voltage_mv <= 90) != (30 <= altitude <= 90):
        triggered.add(77)
    # 变异规则 106 - CRP
    if (30 <= voltage_mv <= 90) != (25 <= voltage_mv <= 90):
        triggered.add(78)
    # 变异规则 107 - UOI
    if (30 <= voltage_mv <= 90) != (30 <= -voltage_mv <= 90):
        triggered.add(79)
    # 变异规则 108 - CAR
    if (30 <= voltage_mv <= 90) != (31 <= voltage_mv <= 90):
        triggered.add(80)
    # 变异规则 109 - ABS
    if (30 <= voltage_mv <= 90) != (30 <= abs(voltage_mv) <= 90):
        t=1
    # 变异规则 110 - AOR
    if (30 <= voltage_mv <= 90) != (not (30 <= voltage_mv <= 90)):
        triggered.add(81)
    # 原语句
    if 30 <= voltage_mv <= 90:
        health_score -= 14
    # 原语句12
    # 变异规则 111 - SAR
    if (voltage_mv >= 94 or altitude >= 1000) != (94 <= voltage_mv or altitude >= 1000):
        t=1
    # 变异规则 112 - CRP
    if (voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or altitude >= 2000):
        triggered.add(82)
    # 变异规则 113 - SRC
    if (voltage_mv >= 94 or altitude >= 1000) != (altitude >= 1000 or voltage_mv >= 94):
        t=1
    # 变异规则 114 - ROR
    if (voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or -altitude >= 1000):
        triggered.add(83)
    # 变异规则 115 - SVR
    if (voltage_mv >= 94 or altitude >= 1000) != (altitude >= 94 or altitude >= 1000):
        triggered.add(84)
    # 变异规则 116 - CSR
    if (voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= -94 or altitude >= 1000):
        triggered.add(85)
    # 变异规则 117 - SCR
    if (voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or altitude >= 998):
        triggered.add(86)
    # 变异规则 118 - UOI
    if (voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or -altitude >= 1000):
        triggered.add(87)
    # 变异规则 119 - ABS
    if (voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or abs(altitude) >= 1000):
        t=1
    # 变异规则 120 - LCR
    if (voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 and altitude >= 1000):
        triggered.add(88)
    # 原语句
    if voltage_mv >= 94 or altitude >= 1000:
        health_score -= 28
        voltage_mv = max(voltage_mv - 10, 2)
    # 原语句13
    # 变异规则 121 - UOI
    if (altitude - 205 > voltage_mv) != (altitude - 205 > -voltage_mv):
        triggered.add(89)
    # 变异规则 122 - ROR
    if (altitude - 205 > voltage_mv) != (altitude - 205 > -voltage_mv):
        triggered.add(90)
    # 变异规则 123 - CRP
    if (altitude - 205 > voltage_mv) != (altitude - 196 > voltage_mv):
        triggered.add(91)
    # 变异规则 124 - SVR
    if (altitude - 205 > voltage_mv) != (speed - 205 > voltage_mv):
        triggered.add(92)
    # 变异规则 125 - RSR
    if (altitude - 205 > voltage_mv) != (not (altitude - 205 > voltage_mv)):
        triggered.add(93)
    # 变异规则 126 - SCR
    if (altitude - 205 > voltage_mv) != (not (altitude - 205 > voltage_mv)):
        triggered.add(94)
    # 变异规则 127 - SRC
    if (altitude - 205 > voltage_mv) != (not (altitude - 205 > voltage_mv)):
        triggered.add(95)
    # 变异规则 128 - SAR
    if (altitude - 205 > voltage_mv) != (altitude - voltage_mv < 205):
        triggered.add(96)
    # 变异规则 129 - CSR
    if (altitude - 205 > voltage_mv) != (altitude - -205 > voltage_mv):
        triggered.add(97)
    # 变异规则 130 - LCR
    if (altitude - 205 > voltage_mv) != (altitude - voltage_mv < 205):
        triggered.add(98)
    # 原语句
    if altitude - 205 > voltage_mv:
        health_score -= 9
        voltage_mv = min(voltage_mv + 7, 100)
        speed, altitude = altitude, speed
    # 原语句14
    # 变异规则 131 - AOR
    if (voltage_mv < 5 or altitude >= 745) != (altitude < 5 or altitude >= 745):
        triggered.add(99)
    # 变异规则 132 - LCR
    if (voltage_mv < 5 or altitude >= 745) != (voltage_mv < 5 and altitude >= 745):
        t=1
    # 变异规则 133 - SRC
    if (voltage_mv < 5 or altitude >= 745) != (altitude >= 745 or voltage_mv < 5):
        t=1
    # 变异规则 134 - SVR
    if (voltage_mv < 5 or altitude >= 745) != (speed < 5 or altitude >= 745):
        triggered.add(100)
    # 变异规则 135 - ROR
    if (voltage_mv < 5 or altitude >= 745) != (voltage_mv < 5 or altitude >= 750):
        t=1
    # 变异规则 136 - CAR
    if (voltage_mv < 5 or altitude >= 745) != (voltage_mv < 5 or altitude >= 743):
        t=1
    # 变异规则 137 - ABS
    if (voltage_mv < 5 or altitude >= 745) != (voltage_mv < 5 or abs(altitude) >= 745):
        t=1
    # 变异规则 138 - RSR
    if (voltage_mv < 5 or altitude >= 745) != (not (voltage_mv < 5 or altitude >= 745)):
        triggered.add(101)
    # 变异规则 139 - SAR
    if (voltage_mv < 5 or altitude >= 745) != (5 > voltage_mv or altitude >= 745):
        t=1
    # 变异规则 140 - UOI
    if (voltage_mv < 5 or altitude >= 745) != (voltage_mv < 5 or -altitude >= 745):
        t=1
    # 原语句
    if voltage_mv < 5 or altitude >= 745:
        health_score += 17
    # 原语句15
    # 变异规则 141 - AOR
    if (6 <= speed <= 96) != (not (6 <= speed <= 96)):
        triggered.add(102)
    # 变异规则 142 - UOI
    if (6 <= speed <= 96) != (6 <= -speed <= 96):
        triggered.add(103)
    # 变异规则 143 - CAR
    if (6 <= speed <= 96) != (6 <= speed <= 98):
        triggered.add(104)
    # 变异规则 144 - CRP
    if (6 <= speed <= 96) != (12 <= speed <= 96):
        triggered.add(105)
    # 变异规则 145 - SRC
    if (6 <= speed <= 96) != (6 <= speed <= -96):
        triggered.add(106)
    # 变异规则 146 - RSR
    if (6 <= speed <= 96) != (not (6 <= speed <= 96)):
        triggered.add(107)
    # 变异规则 147 - SVR
    if (6 <= speed <= 96) != (6 <= altitude <= 96):
        triggered.add(108)
    # 变异规则 148 - SAR
    if (6 <= speed <= 96) != (speed >= 6 <= 96):
        triggered.add(109)
    # 变异规则 149 - ROR
    if (6 <= speed <= 96) != (6 <= -speed <= 96):
        triggered.add(110)
    # 变异规则 150 - LCR
    if (6 <= speed <= 96) != (not (6 <= speed <= 96)):
        triggered.add(111)
    # 原语句
    if 6 <= speed <= 96:
        health_score -= 23
        speed = max(speed - 10, 2)
    # 原语句16
    # 变异规则 151 - RSR
    if (327 <= altitude <= 830) != (not (327 <= altitude <= 830)):
        triggered.add(112)
    # 变异规则 152 - LCR
    if (327 <= altitude <= 830) != (327 <= altitude <= 820):
        t=1
    # 变异规则 153 - ROR
    if (327 <= altitude <= 830) != (327 <= -altitude <= 830):
        t=1
    # 变异规则 154 - AOR
    if (327 <= altitude <= 830) != (not (327) <= altitude <= 830):
        triggered.add(113)
    # 变异规则 155 - SVR
    if (327 <= altitude <= 830) != (327 <= voltage_mv <= 830):
        t=1
    # 变异规则 156 - CRP
    if (327 <= altitude <= 830) != (327 <= altitude <= 415):
        t=1
    # 变异规则 157 - CAR
    if (327 <= altitude <= 830) != (327 <= altitude <= 825):
        t=1
    # 变异规则 158 - CSR
    if (327 <= altitude <= 830) != (-327 <= altitude <= 830):
        triggered.add(114)
    # 变异规则 159 - SAR
    if (327 <= altitude <= 830) != (altitude >= 327 <= 830):
        t=1
    # 变异规则 160 - SCR
    if (327 <= altitude <= 830) != (not (327) <= altitude <= 830):
        triggered.add(115)
    # 原语句
    if 327 <= altitude <= 830:
        health_score -= 25
        voltage_mv = min(voltage_mv + 6, 100)
    # 原语句17
    # 变异规则 161 - AOR
    if (16 <= voltage_mv <= 53) != (18 <= voltage_mv <= 53):
        triggered.add(116)
    # 变异规则 162 - SRC
    if (16 <= voltage_mv <= 53) != (16 <= speed <= 53):
        triggered.add(117)
    # 变异规则 163 - CAR
    if (16 <= voltage_mv <= 53) != (21 <= voltage_mv <= 53):
        triggered.add(118)
    # 变异规则 164 - UOI
    if (16 <= voltage_mv <= 53) != (16 <= -voltage_mv <= 53):
        triggered.add(119)
    # 变异规则 165 - ABS
    if (16 <= voltage_mv <= 53) != (16 <= abs(voltage_mv) <= 53):
        t=1
    # 变异规则 166 - RSR
    if (16 <= voltage_mv <= 53) != (not (16 <= voltage_mv <= 53)):
        triggered.add(120)
    # 变异规则 167 - SCR
    if (16 <= voltage_mv <= 53) != (not (16) <= voltage_mv <= 53):
        triggered.add(121)
    # 变异规则 168 - CSR
    if (16 <= voltage_mv <= 53) != (-16 <= voltage_mv <= 53):
        triggered.add(122)
    # 变异规则 169 - SVR
    if (16 <= voltage_mv <= 53) != (16 <= altitude <= 53):
        triggered.add(123)
    # 变异规则 170 - CRP
    if (16 <= voltage_mv <= 53) != (8 <= voltage_mv <= 53):
        triggered.add(124)
    # 原语句
    if 16 <= voltage_mv <= 53:
        health_score -= 17
        speed = max(speed - 1, 2)
    # 原语句18
    # 变异规则 171 - LCR
    if (voltage_mv >= 50) != (altitude >= 50):
        triggered.add(125)
    # 变异规则 172 - CAR
    if (voltage_mv >= 50) != (voltage_mv >= 60):
        triggered.add(126)
    # 变异规则 173 - SVR
    if (voltage_mv >= 50) != (altitude >= 50):
        triggered.add(127)
    # 变异规则 174 - AOR
    if (voltage_mv >= 50) != (not (voltage_mv >= 50)):
        triggered.add(128)
    # 变异规则 175 - CSR
    if (voltage_mv >= 50) != (voltage_mv >= -50):
        triggered.add(129)
    # 变异规则 176 - SAR
    if (voltage_mv >= 50) != (50 <= voltage_mv):
        t=1
    # 变异规则 177 - CRP
    if (voltage_mv >= 50) != (voltage_mv >= 60):
        triggered.add(130)
    # 变异规则 178 - ROR
    if (voltage_mv >= 50) != (voltage_mv >= 43):
        triggered.add(131)
    # 变异规则 179 - SCR
    if (voltage_mv >= 50) != (altitude >= 50):
        triggered.add(132)
    # 变异规则 180 - ABS
    if (voltage_mv >= 50) != (abs(voltage_mv) >= 50):
        t=1
    # 原语句
    if voltage_mv >= 50:
        health_score -= 9
        altitude = min(altitude + 8, 1000)
    # 原语句19
    # 变异规则 181 - LCR
    if (voltage_mv - speed > 20) != (altitude - speed > 20):
        triggered.add(133)
    # 变异规则 182 - RSR
    if (voltage_mv - speed > 20) != (not (voltage_mv - speed > 20)):
        triggered.add(134)
    # 变异规则 183 - SVR
    if (voltage_mv - speed > 20) != (altitude - speed > 20):
        triggered.add(135)
    # 变异规则 184 - AOR
    if (voltage_mv - speed > 20) != (voltage_mv - speed > 25):
        triggered.add(136)
    # 变异规则 185 - UOI
    if (voltage_mv - speed > 20) != (voltage_mv - speed > 40):
        triggered.add(137)
    # 变异规则 186 - CRP
    if (voltage_mv - speed > 20) != (voltage_mv - speed > 14):
        triggered.add(138)
    # 变异规则 187 - CSR
    if (voltage_mv - speed > 20) != (voltage_mv - speed > -20):
        triggered.add(139)
    # 变异规则 188 - CAR
    if (voltage_mv - speed > 20) != (voltage_mv - speed > 30):
        triggered.add(140)
    # 变异规则 189 - SAR
    if (voltage_mv - speed > 20) != (voltage_mv - 20 < speed):
        triggered.add(141)
    # 变异规则 190 - SCR
    if (voltage_mv - speed > 20) != (speed - speed > 20):
        triggered.add(142)
    # 原语句
    if voltage_mv - speed > 20:
        health_score += 2
        speed = min(speed + 4, 100)
        altitude, speed = speed, altitude
    # 原语句20
    # 变异规则 191 - RSR
    if (altitude <= 347 and voltage_mv > 100) != (not (altitude <= 347 and voltage_mv > 100)):
        triggered.add(143)
    # 变异规则 192 - LCR
    if (altitude <= 347 and voltage_mv > 100) != (altitude <= 347 or voltage_mv > 100):
        triggered.add(144)
    # 变异规则 193 - SAR
    if (altitude <= 347 and voltage_mv > 100) != (altitude <= 347 and 100 < voltage_mv):
        t=1
    # 变异规则 194 - CSR
    if (altitude <= 347 and voltage_mv > 100) != (altitude <= 347 and voltage_mv > -100):
        triggered.add(145)
    # 变异规则 195 - CRP
    if (altitude <= 347 and voltage_mv > 100) != (altitude <= 173 and voltage_mv > 100):
        t=1
    # 变异规则 196 - SVR
    if (altitude <= 347 and voltage_mv > 100) != (voltage_mv <= 347 and voltage_mv > 100):
        t=1
    # 变异规则 197 - SRC
    if (altitude <= 347 and voltage_mv > 100) != (voltage_mv > 100 and altitude <= 347):
        t=1
    # 变异规则 198 - ABS
    if (altitude <= 347 and voltage_mv > 100) != (abs(altitude) <= 347 and voltage_mv > 100):
        t=1
    # 变异规则 199 - CAR
    if (altitude <= 347 and voltage_mv > 100) != (altitude <= 357 and voltage_mv > 100):
        t=1
    # 变异规则 200 - SCR
    if (altitude <= 347 and voltage_mv > 100) != (voltage_mv <= 347 and voltage_mv > 100):
        t=1
    # 原语句
    if altitude <= 347 and voltage_mv > 100:
        health_score -= 25
        altitude = max(altitude - 42, 2)
        speed, altitude = altitude, speed
    # 原语句21
    # 变异规则 201 - AOR
    if (altitude <= 915 and voltage_mv > 100) != (abs(altitude) <= 915 and voltage_mv > 100):
        t=1
    # 变异规则 202 - SVR
    if (altitude <= 915 and voltage_mv > 100) != (voltage_mv <= 915 and voltage_mv > 100):
        t=1
    # 变异规则 203 - SRC
    if (altitude <= 915 and voltage_mv > 100) != (voltage_mv > 100 and altitude <= 915):
        t=1
    # 变异规则 204 - CSR
    if (altitude <= 915 and voltage_mv > 100) != (altitude <= -915 and voltage_mv > 100):
        t=1
    # 变异规则 205 - SAR
    if (altitude <= 915 and voltage_mv > 100) != (altitude <= 915 and 100 < voltage_mv):
        t=1
    # 变异规则 206 - RSR
    if (altitude <= 915 and voltage_mv > 100) != (not (altitude <= 915 and voltage_mv > 100)):
        triggered.add(146)
    # 变异规则 207 - UOI
    if (altitude <= 915 and voltage_mv > 100) != (altitude <= 915 and -voltage_mv > 100):
        t=1
    # 变异规则 208 - LCR
    if (altitude <= 915 and voltage_mv > 100) != (altitude <= 915 or voltage_mv > 100):
        triggered.add(147)
    # 变异规则 209 - SCR
    if (altitude <= 915 and voltage_mv > 100) != (altitude <= 915 and -voltage_mv > 100):
        t=1
    # 变异规则 210 - ROR
    if (altitude <= 915 and voltage_mv > 100) != (abs(altitude) <= 915 and voltage_mv > 100):
        t=1
    # 原语句
    if altitude <= 915 and voltage_mv > 100:
        health_score -= 21
        voltage_mv = min(voltage_mv + 10, 100)
        speed, altitude = altitude, speed
    # 原语句22
    # 变异规则 211 - AOR
    if (altitude + voltage_mv != 20) != (altitude + -voltage_mv != 20):
        triggered.add(148)
    # 变异规则 212 - ABS
    if (altitude + voltage_mv != 20) != (abs(altitude) + voltage_mv != 20):
        t=1
    # 变异规则 213 - LCR
    if (altitude + voltage_mv != 20) != (abs(altitude) + voltage_mv != 20):
        t=1
    # 变异规则 214 - SCR
    if (altitude + voltage_mv != 20) != (speed + voltage_mv != 20):
        triggered.add(149)
    # 变异规则 215 - RSR
    if (altitude + voltage_mv != 20) != (not (altitude + voltage_mv != 20)):
        triggered.add(150)
    # 变异规则 216 - SAR
    if (altitude + voltage_mv != 20) != (altitude + 20 != voltage_mv):
        triggered.add(151)
    # 变异规则 217 - CAR
    if (altitude + voltage_mv != 20) != (altitude + voltage_mv != 25):
        triggered.add(152)
    # 变异规则 218 - SRC
    if (altitude + voltage_mv != 20) != (not (altitude + voltage_mv != 20)):
        triggered.add(153)
    # 变异规则 219 - SVR
    if (altitude + voltage_mv != 20) != (voltage_mv + voltage_mv != 20):
        triggered.add(154)
    # 变异规则 220 - UOI
    if (altitude + voltage_mv != 20) != (altitude + -voltage_mv != 20):
        triggered.add(155)
    # 原语句
    if altitude + voltage_mv != 20:
        health_score -= 28
    # 原语句23
    # 变异规则 221 - CRP
    if (speed - voltage_mv != 16) != (speed - voltage_mv != 8):
        triggered.add(156)
    # 变异规则 222 - CAR
    if (speed - voltage_mv != 16) != (speed - voltage_mv != 15):
        triggered.add(157)
    # 变异规则 223 - SCR
    if (speed - voltage_mv != 16) != (altitude - voltage_mv != 16):
        triggered.add(158)
    # 变异规则 224 - SAR
    if (speed - voltage_mv != 16) != (speed - 16 != voltage_mv):
        t=1
    # 变异规则 225 - SRC
    if (speed - voltage_mv != 16) != (not (speed - voltage_mv != 16)):
        triggered.add(159)
    # 变异规则 226 - CSR
    if (speed - voltage_mv != 16) != (speed - voltage_mv != -16):
        triggered.add(160)
    # 变异规则 227 - ABS
    if (speed - voltage_mv != 16) != (abs(speed) - voltage_mv != 16):
        t=1
    # 变异规则 228 - ROR
    if (speed - voltage_mv != 16) != (abs(speed) - voltage_mv != 16):
        t=1
    # 变异规则 229 - RSR
    if (speed - voltage_mv != 16) != (not (speed - voltage_mv != 16)):
        triggered.add(161)
    # 变异规则 230 - LCR
    if (speed - voltage_mv != 16) != (not (speed - voltage_mv != 16)):
        triggered.add(162)
    # 原语句
    if speed - voltage_mv != 16:
        health_score -= 3
    # 原语句24
    # 变异规则 231 - AOR
    if (speed != 30) != (not (speed != 30)):
        triggered.add(163)
    # 变异规则 232 - LCR
    if (speed != 30) != (not (speed != 30)):
        triggered.add(164)
    # 变异规则 233 - ABS
    if (speed != 30) != (abs(speed) != 30):
        t=1
    # 变异规则 234 - SVR
    if (speed != 30) != (voltage_mv != 30):
        triggered.add(165)
    # 变异规则 235 - CRP
    if (speed != 30) != (speed != 60):
        triggered.add(166)
    # 变异规则 236 - SAR
    if (speed != 30) != (30 != speed):
        t=1
    # 变异规则 237 - RSR
    if (speed != 30) != (not (speed != 30)):
        triggered.add(167)
    # 变异规则 238 - CSR
    if (speed != 30) != (speed != -30):
        triggered.add(168)
    # 变异规则 239 - SCR
    if (speed != 30) != (speed != 28):
        triggered.add(169)
    # 变异规则 240 - SRC
    if (speed != 30) != (speed != -30):
        triggered.add(170)
    # 原语句
    if speed != 30:
        health_score += 18
        altitude = min(altitude + 41, 1000)
    # 原语句25
    # 变异规则 241 - RSR
    if (voltage_mv * altitude != 35) != (not (voltage_mv * altitude != 35)):
        triggered.add(171)
    # 变异规则 242 - SRC
    if (voltage_mv * altitude != 35) != (voltage_mv * -altitude != 35):
        t=1
    # 变异规则 243 - ABS
    if (voltage_mv * altitude != 35) != (voltage_mv * abs(altitude) != 35):
        t=1
    # 变异规则 244 - SAR
    if (voltage_mv * altitude != 35) != (voltage_mv * 35 != altitude):
        t=1
    # 变异规则 245 - SCR
    if (voltage_mv * altitude != 35) != (not (voltage_mv * altitude != 35)):
        triggered.add(172)
    # 变异规则 246 - AOR
    if (voltage_mv * altitude != 35) != (voltage_mv * altitude != -35):
        t=1
    # 变异规则 247 - CSR
    if (voltage_mv * altitude != 35) != (voltage_mv * altitude != -35):
        t=1
    # 变异规则 248 - ROR
    if (voltage_mv * altitude != 35) != (voltage_mv * altitude != -35):
        t=1
    # 变异规则 249 - UOI
    if (voltage_mv * altitude != 35) != (voltage_mv * -altitude != 35):
        t=1
    # 变异规则 250 - CRP
    if (voltage_mv * altitude != 35) != (voltage_mv * altitude != 17):
        t=1
    # 原语句
    if voltage_mv * altitude != 35:
        health_score += 16
        speed = min(speed + 9, 100)
        voltage_mv = min(voltage_mv + 3, 100)
    # 原语句26
    # 变异规则 251 - CRP
    if (voltage_mv + 50 >= altitude) != (voltage_mv + 57 >= altitude):
        triggered.add(173)
    # 变异规则 252 - SVR
    if (voltage_mv + 50 >= altitude) != (altitude + 50 >= altitude):
        triggered.add(174)
    # 变异规则 253 - SRC
    if (voltage_mv + 50 >= altitude) != (speed + 50 >= altitude):
        triggered.add(175)
    # 变异规则 254 - AOR
    if (voltage_mv + 50 >= altitude) != (voltage_mv + 50 >= abs(altitude)):
        t=1
    # 变异规则 255 - RSR
    if (voltage_mv + 50 >= altitude) != (not (voltage_mv + 50 >= altitude)):
        triggered.add(176)
    # 变异规则 256 - ROR
    if (voltage_mv + 50 >= altitude) != (voltage_mv + 52 >= altitude):
        triggered.add(177)
    # 变异规则 257 - ABS
    if (voltage_mv + 50 >= altitude) != (voltage_mv + 50 >= abs(altitude)):
        t=1
    # 变异规则 258 - CSR
    if (voltage_mv + 50 >= altitude) != (voltage_mv + -50 >= altitude):
        triggered.add(178)
    # 变异规则 259 - LCR
    if (voltage_mv + 50 >= altitude) != (voltage_mv + 50 >= abs(altitude)):
        t=1
    # 变异规则 260 - UOI
    if (voltage_mv + 50 >= altitude) != (voltage_mv + 50 >= -altitude):
        triggered.add(179)
    # 原语句
    if voltage_mv + 50 >= altitude:
        health_score += 16
        speed = max(speed - 10, 2)
    # 原语句27
    # 变异规则 261 - SCR
    if (altitude == 5 or voltage_mv <= 100) != (abs(altitude) == 5 or voltage_mv <= 100):
        t=1
    # 变异规则 262 - SVR
    if (altitude == 5 or voltage_mv <= 100) != (speed == 5 or voltage_mv <= 100):
        t=1
    # 变异规则 263 - RSR
    if (altitude == 5 or voltage_mv <= 100) != (not (altitude == 5 or voltage_mv <= 100)):
        triggered.add(180)
    # 变异规则 264 - UOI
    if (altitude == 5 or voltage_mv <= 100) != (altitude == 5 or -voltage_mv <= 100):
        t=1
    # 变异规则 265 - CAR
    if (altitude == 5 or voltage_mv <= 100) != (altitude == 1 or voltage_mv <= 100):
        t=1
    # 变异规则 266 - SAR
    if (altitude == 5 or voltage_mv <= 100) != (altitude == 5 or 100 >= voltage_mv):
        t=1
    # 变异规则 267 - CSR
    if (altitude == 5 or voltage_mv <= 100) != (altitude == 5 or voltage_mv <= -100):
        triggered.add(181)
    # 变异规则 268 - LCR
    if (altitude == 5 or voltage_mv <= 100) != (altitude == 5 and voltage_mv <= 100):
        triggered.add(182)
    # 变异规则 269 - ROR
    if (altitude == 5 or voltage_mv <= 100) != (voltage_mv == 5 or voltage_mv <= 100):
        t=1
    # 变异规则 270 - ABS
    if (altitude == 5 or voltage_mv <= 100) != (abs(altitude) == 5 or voltage_mv <= 100):
        t=1
    # 原语句
    if altitude == 5 or voltage_mv <= 100:
        health_score -= 27
        altitude = max(altitude - 20, 2)
    # 原语句28
    # 变异规则 271 - SVR
    if (altitude > 863) != (voltage_mv > 863):
        t=1
    # 变异规则 272 - RSR
    if (altitude > 863) != (not (altitude > 863)):
        triggered.add(183)
    # 变异规则 273 - SCR
    if (altitude > 863) != (not (altitude > 863)):
        triggered.add(184)
    # 变异规则 274 - LCR
    if (altitude > 863) != (abs(altitude) > 863):
        t=1
    # 变异规则 275 - ABS
    if (altitude > 863) != (abs(altitude) > 863):
        t=1
    # 变异规则 276 - CSR
    if (altitude > 863) != (altitude > -863):
        triggered.add(185)
    # 变异规则 277 - CRP
    if (altitude > 863) != (altitude > 856):
        t=1
    # 变异规则 278 - ROR
    if (altitude > 863) != (altitude > 853):
        t=1
    # 变异规则 279 - AOR
    if (altitude > 863) != (abs(altitude) > 863):
        t=1
    # 变异规则 280 - SAR
    if (altitude > 863) != (863 < altitude):
        t=1
    # 原语句
    if altitude > 863:
        health_score -= 17
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句29
    # 变异规则 281 - ABS
    if (29 <= voltage_mv <= 76) != (29 <= abs(voltage_mv) <= 76):
        t=1
    # 变异规则 282 - CAR
    if (29 <= voltage_mv <= 76) != (29 <= voltage_mv <= 71):
        triggered.add(186)
    # 变异规则 283 - LCR
    if (29 <= voltage_mv <= 76) != (29 <= speed <= 76):
        triggered.add(187)
    # 变异规则 284 - RSR
    if (29 <= voltage_mv <= 76) != (not (29 <= voltage_mv <= 76)):
        triggered.add(188)
    # 变异规则 285 - SAR
    if (29 <= voltage_mv <= 76) != (voltage_mv >= 29 <= 76):
        triggered.add(189)
    # 变异规则 286 - AOR
    if (29 <= voltage_mv <= 76) != (29 <= -voltage_mv <= 76):
        triggered.add(190)
    # 变异规则 287 - SRC
    if (29 <= voltage_mv <= 76) != (29 <= voltage_mv <= -76):
        triggered.add(191)
    # 变异规则 288 - SCR
    if (29 <= voltage_mv <= 76) != (29 <= voltage_mv <= -76):
        triggered.add(192)
    # 变异规则 289 - SVR
    if (29 <= voltage_mv <= 76) != (29 <= speed <= 76):
        triggered.add(193)
    # 变异规则 290 - CRP
    if (29 <= voltage_mv <= 76) != (32 <= voltage_mv <= 76):
        triggered.add(194)
    # 原语句
    if 29 <= voltage_mv <= 76:
        health_score += 18
        altitude = max(altitude - 40, 2)
        voltage_mv = max(voltage_mv - 5, 2)
    # 原语句30
    # 变异规则 291 - ROR
    if (voltage_mv < 20) != (20 > voltage_mv):
        t=1
    # 变异规则 292 - RSR
    if (voltage_mv < 20) != (not (voltage_mv < 20)):
        triggered.add(195)
    # 变异规则 293 - CRP
    if (voltage_mv < 20) != (voltage_mv < 10):
        triggered.add(196)
    # 变异规则 294 - LCR
    if (voltage_mv < 20) != (abs(voltage_mv) < 20):
        t=1
    # 变异规则 295 - AOR
    if (voltage_mv < 20) != (20 > voltage_mv):
        t=1
    # 变异规则 296 - SVR
    if (voltage_mv < 20) != (speed < 20):
        triggered.add(197)
    # 变异规则 297 - CAR
    if (voltage_mv < 20) != (voltage_mv < 19):
        triggered.add(198)
    # 变异规则 298 - SRC
    if (voltage_mv < 20) != (voltage_mv < 25):
        triggered.add(199)
    # 变异规则 299 - SAR
    if (voltage_mv < 20) != (20 > voltage_mv):
        t=1
    # 变异规则 300 - ABS
    if (voltage_mv < 20) != (abs(voltage_mv) < 20):
        t=1
    # 原语句
    if voltage_mv < 20:
        health_score += 5
        voltage_mv = max(voltage_mv - 4, 2)
    return triggered

targetPaths = [
    {3, 12, 15, 21, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 100, 101, 102, 112, 113, 114, 120, 121, 122, 124, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196},
    {3, 11, 12, 15, 21, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 100, 101, 102, 112, 113, 114, 120, 121, 122, 124, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196},
    {3, 11, 12, 15, 19, 21, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 100, 101, 102, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196, 198},
    {3, 11, 12, 15, 19, 21, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 100, 101, 102, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 125, 128, 129, 133, 134, 138, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 197, 199},
    {3, 11, 12, 15, 19, 21, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 100, 101, 102, 112, 113, 114, 117, 118, 119, 120, 121, 123, 125, 128, 129, 133, 134, 138, 139, 141, 143, 144, 145, 146, 147, 149, 150, 159, 160, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 197, 199},
    {3, 12, 13, 16, 19, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 100, 101, 102, 112, 113, 114, 117, 118, 119, 120, 121, 123, 125, 128, 129, 133, 134, 138, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 197, 199},
    {3, 12, 13, 16, 18, 20, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 100, 101, 102, 112, 113, 114, 117, 119, 120, 121, 123, 125, 128, 129, 134, 136, 137, 140, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195},
    {3, 12, 13, 16, 18, 20, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 65, 66, 67, 68, 70, 74, 76, 77, 85, 93, 96, 97, 101, 102, 103, 106, 112, 113, 114, 120, 121, 122, 123, 124, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196, 197},
    {2, 3, 12, 13, 16, 18, 20, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 65, 66, 67, 68, 70, 74, 76, 77, 85, 93, 96, 97, 101, 102, 103, 106, 112, 113, 114, 120, 121, 122, 123, 124, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196, 197},
    {2, 3, 12, 13, 16, 18, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 68, 70, 74, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 122, 124, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 156, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 196},
    {2, 3, 12, 13, 16, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 122, 124, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 196},
    {2, 3, 12, 13, 16, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 122, 124, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 157, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 196, 197},
    {2, 3, 12, 13, 16, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 122, 124, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 156, 157, 158, 159, 160, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 196, 197},
    {2, 3, 12, 13, 16, 21, 22, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 122, 124, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 169, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 196, 197},
    {2, 3, 10, 12, 14, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 122, 124, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 196, 197},
    {2, 3, 10, 12, 14, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 122, 124, 128, 129, 134, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 165, 166, 168, 169, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 195, 196, 197},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 61, 64, 65, 66, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 120, 121, 122, 124, 128, 129, 134, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 195, 196, 197},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 61, 62, 64, 65, 66, 70, 74, 75, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 120, 121, 122, 124, 128, 129, 134, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 195, 196, 197},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 63, 64, 67, 69, 70, 74, 75, 79, 85, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 63, 64, 67, 69, 70, 73, 74, 77, 85, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 63, 64, 67, 69, 70, 73, 74, 77, 84, 88, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 40, 43, 45, 50, 54, 57, 60, 63, 64, 67, 69, 70, 73, 74, 77, 84, 88, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 40, 43, 45, 50, 54, 56, 57, 60, 63, 64, 67, 69, 70, 73, 74, 77, 84, 88, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 38, 40, 43, 45, 50, 54, 56, 57, 60, 63, 64, 67, 69, 70, 73, 74, 77, 84, 88, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 36, 38, 40, 43, 45, 50, 51, 53, 54, 56, 57, 60, 63, 64, 67, 69, 70, 73, 74, 77, 84, 88, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 35, 36, 38, 40, 43, 45, 50, 51, 53, 54, 56, 57, 60, 63, 64, 67, 69, 70, 73, 74, 77, 84, 88, 93, 96, 97, 100, 101, 102, 108, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {3, 10, 12, 15, 22, 25, 26, 27, 28, 30, 34, 37, 43, 45, 50, 51, 54, 57, 60, 63, 64, 66, 70, 73, 74, 75, 84, 88, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 125, 128, 133, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 175, 176, 178, 180, 181, 182, 183, 185, 188, 189, 195, 197},
    {2, 3, 10, 12, 15, 22, 28, 34, 36, 43, 45, 50, 54, 57, 60, 63, 64, 67, 69, 70, 74, 75, 79, 85, 93, 96, 97, 101, 102, 103, 105, 106, 112, 113, 114, 120, 121, 123, 125, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 189, 195},
    {2, 3, 12, 13, 16, 18, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 68, 70, 74, 76, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 118, 119, 120, 121, 123, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 197, 199},
    {2, 4, 7, 8, 12, 15, 21, 22, 28, 34, 36, 43, 45, 50, 54, 58, 60, 64, 69, 70, 74, 76, 84, 85, 93, 96, 97, 101, 102, 103, 105, 106, 108, 112, 113, 114, 120, 121, 122, 124, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196},
    {4, 7, 8, 12, 13, 16, 18, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 68, 70, 74, 76, 78, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 119, 120, 121, 123, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 197},
    {4, 7, 8, 12, 13, 16, 18, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 68, 70, 74, 76, 78, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 119, 120, 121, 123, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 190, 191, 194, 195, 197, 199},
    {4, 7, 8, 12, 13, 16, 18, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 67, 68, 70, 74, 75, 77, 79, 80, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 119, 120, 121, 123, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 165, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 190, 191, 195, 197},
    {4, 8, 12, 13, 16, 18, 20, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 58, 59, 60, 64, 65, 67, 68, 70, 74, 75, 79, 85, 93, 96, 97, 101, 102, 103, 106, 112, 113, 114, 117, 119, 120, 121, 125, 128, 129, 133, 134, 138, 139, 143, 144, 145, 146, 147, 150, 159, 163, 171, 173, 174, 176, 179, 180, 181, 182, 183, 185, 187, 188, 190, 191, 195},
    {4, 8, 12, 13, 16, 18, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 67, 68, 70, 74, 75, 77, 79, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 119, 120, 121, 123, 128, 129, 131, 133, 134, 137, 140, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 175, 176, 178, 180, 181, 182, 183, 185, 187, 188, 190, 191, 195, 197},
    {4, 8, 12, 13, 16, 18, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 67, 68, 70, 74, 75, 77, 79, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 119, 120, 121, 123, 125, 126, 128, 133, 134, 137, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 187, 188, 190, 191, 195, 197},
    {4, 8, 12, 13, 16, 18, 21, 22, 25, 28, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 67, 68, 70, 74, 75, 77, 79, 85, 93, 96, 97, 99, 101, 102, 103, 106, 108, 112, 113, 114, 117, 120, 121, 125, 128, 133, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 186, 187, 188, 190, 191, 195, 197},
    {2, 4, 8, 10, 12, 15, 22, 28, 34, 37, 43, 45, 46, 50, 51, 54, 57, 60, 63, 64, 66, 70, 73, 74, 75, 77, 84, 88, 93, 96, 97, 101, 102, 103, 106, 112, 113, 114, 117, 120, 121, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 189, 195},
    {2, 4, 8, 10, 12, 15, 22, 28, 34, 37, 43, 45, 46, 47, 50, 51, 54, 57, 60, 63, 64, 66, 70, 73, 74, 75, 77, 84, 88, 93, 96, 97, 101, 102, 103, 106, 112, 113, 114, 117, 120, 121, 128, 134, 141, 142, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 189, 195},
    {4, 8, 10, 12, 15, 22, 28, 34, 36, 43, 45, 50, 51, 54, 57, 60, 63, 64, 67, 70, 74, 75, 79, 85, 93, 96, 97, 101, 102, 104, 108, 109, 112, 113, 114, 120, 121, 123, 125, 128, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 189, 195},
    {1, 12, 15, 21, 22, 28, 34, 36, 43, 45, 50, 51, 54, 58, 60, 64, 70, 74, 76, 84, 85, 93, 96, 97, 101, 102, 103, 106, 108, 112, 113, 114, 120, 121, 122, 124, 125, 128, 129, 133, 134, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196, 197},
    {2, 3, 10, 12, 14, 15, 22, 25, 26, 27, 28, 30, 34, 36, 43, 45, 50, 54, 57, 60, 64, 65, 66, 70, 74, 75, 76, 85, 93, 96, 97, 101, 102, 103, 106, 112, 113, 114, 117, 120, 121, 122, 123, 124, 128, 129, 134, 139, 141, 143, 144, 145, 146, 147, 150, 154, 159, 163, 171, 173, 174, 175, 176, 177, 179, 180, 181, 182, 183, 185, 187, 188, 195, 196, 197},
    {3, 12, 15, 21, 22, 25, 26, 27, 28, 30, 34, 36, 45, 49, 50, 54, 58, 60, 64, 69, 70, 74, 76, 84, 85, 89, 93, 96, 97, 100, 101, 102, 112, 113, 114, 120, 121, 122, 124, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196},
    {3, 12, 15, 21, 22, 25, 26, 27, 28, 30, 34, 36, 45, 49, 50, 54, 58, 60, 64, 69, 70, 74, 76, 84, 85, 89, 91, 93, 96, 97, 100, 101, 102, 112, 113, 114, 120, 121, 122, 124, 125, 128, 129, 133, 134, 139, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 174, 176, 179, 180, 181, 182, 183, 185, 188, 195, 196},
    {3, 12, 15, 21, 22, 25, 26, 27, 28, 30, 34, 36, 45, 49, 50, 54, 58, 60, 64, 69, 70, 74, 76, 84, 85, 92, 93, 96, 99, 101, 102, 109, 112, 113, 114, 117, 118, 119, 120, 121, 123, 128, 129, 134, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 199},
    {3, 12, 15, 21, 22, 25, 26, 27, 28, 30, 34, 36, 45, 49, 50, 54, 58, 60, 64, 69, 70, 74, 76, 84, 85, 86, 92, 93, 96, 99, 101, 102, 109, 112, 113, 114, 117, 118, 119, 120, 121, 123, 128, 129, 134, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 199},
    {3, 12, 15, 21, 22, 25, 26, 27, 28, 30, 34, 36, 45, 49, 50, 54, 58, 60, 64, 69, 70, 74, 76, 82, 83, 88, 92, 93, 96, 99, 101, 102, 109, 112, 113, 114, 120, 121, 122, 124, 128, 129, 134, 141, 143, 144, 145, 146, 147, 150, 159, 163, 171, 176, 178, 180, 181, 182, 183, 185, 188, 195, 196, 197}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 12:11, 13:12, 14:13, 15:14, 16:15, 18:16, 19:17, 23:18, 25:19, 26:20, 27:21, 28:22, 29:23, 30:24, 31:25, 32:26, 33:27, 35:28, 36:29, 37:30, 38:31, 39:32, 40:33, 41:34, 42:35, 43:36, 44:37, 45:38, 47:39, 48:40, 49:41, 50:42, 52:43, 55:44, 57:45, 58:46, 59:47, 60:48, 61:49, 63:50, 64:51, 65:52, 66:53, 68:54, 69:55, 70:56, 75:57, 76:58, 78:59, 81:60, 82:61, 83:62, 84:63, 85:64, 87:65, 88:66, 89:67, 90:68, 93:69, 95:70, 96:71, 98:72, 101:73, 102:74, 103:75, 104:76, 105:77, 106:78, 107:79, 108:80, 110:81, 112:82, 114:83, 115:84, 116:85, 117:86, 118:87, 120:88, 121:89, 122:90, 123:91, 124:92, 125:93, 126:94, 127:95, 128:96, 129:97, 130:98, 131:99, 134:100, 138:101, 141:102, 142:103, 143:104, 144:105, 145:106, 146:107, 147:108, 148:109, 149:110, 150:111, 151:112, 154:113, 158:114, 160:115, 161:116, 162:117, 163:118, 164:119, 166:120, 167:121, 168:122, 169:123, 170:124, 171:125, 172:126, 173:127, 174:128, 175:129, 177:130, 178:131, 179:132, 181:133, 182:134, 183:135, 184:136, 185:137, 186:138, 187:139, 188:140, 189:141, 190:142, 191:143, 192:144, 194:145, 206:146, 208:147, 211:148, 214:149, 215:150, 216:151, 217:152, 218:153, 219:154, 220:155, 221:156, 222:157, 223:158, 225:159, 226:160, 229:161, 230:162, 231:163, 232:164, 234:165, 235:166, 237:167, 238:168, 239:169, 240:170, 241:171, 245:172, 251:173, 252:174, 253:175, 255:176, 256:177, 258:178, 260:179, 263:180, 267:181, 268:182, 272:183, 273:184, 276:185, 282:186, 283:187, 284:188, 285:189, 286:190, 287:191, 288:192, 289:193, 290:194, 292:195, 293:196, 296:197, 297:198, 298:199}

    rule_expressions[1] = "(15 <= speed <= 97) != (speed >= 15 <= 97)"
    rule_expressions[2] = "(15 <= speed <= 97) != (15 <= voltage_mv <= 97)"
    rule_expressions[3] = "(15 <= speed <= 97) != (-15 <= speed <= 97)"
    rule_expressions[4] = "(15 <= speed <= 97) != (15 <= speed <= -97)"
    rule_expressions[5] = "(15 <= speed <= 97) != (-15 <= speed <= 97)"
    rule_expressions[6] = "(15 <= speed <= 97) != (speed >= 15 <= 97)"
    rule_expressions[7] = "(15 <= speed <= 97) != (21 <= speed <= 97)"
    rule_expressions[8] = "(15 <= speed <= 97) != (15 <= -speed <= 97)"
    rule_expressions[9] = "(15 <= speed <= 97) != (15 <= -speed <= 97)"
    rule_expressions[10] = "(voltage_mv >= 30 or voltage_mv <= 9) != (altitude >= 30 or voltage_mv <= 9)"
    rule_expressions[11] = "(voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 or voltage_mv <= 4)"
    rule_expressions[12] = "(voltage_mv >= 30 or voltage_mv <= 9) != (not (voltage_mv >= 30 or voltage_mv <= 9))"
    rule_expressions[13] = "(voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 or -voltage_mv <= 9)"
    rule_expressions[14] = "(voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 34 or voltage_mv <= 9)"
    rule_expressions[15] = "(voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 and voltage_mv <= 9)"
    rule_expressions[16] = "(voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= -30 or voltage_mv <= 9)"
    rule_expressions[17] = "(voltage_mv >= 30 or voltage_mv <= 9) != (voltage_mv >= 30 or -voltage_mv <= 9)"
    rule_expressions[18] = "(voltage_mv > 10) != (voltage_mv > 20)"
    rule_expressions[19] = "(voltage_mv > 10) != (voltage_mv > 5)"
    rule_expressions[20] = "(voltage_mv > 10) != (voltage_mv > 15)"
    rule_expressions[21] = "(voltage_mv > 10) != (altitude > 10)"
    rule_expressions[22] = "(voltage_mv > 10) != (not (voltage_mv > 10))"
    rule_expressions[23] = "(voltage_mv > 10) != (altitude > 10)"
    rule_expressions[24] = "(voltage_mv > 10) != (not (voltage_mv > 10))"
    rule_expressions[25] = "(speed != 2) != (altitude != 2)"
    rule_expressions[26] = "(speed != 2) != (speed != -2)"
    rule_expressions[27] = "(speed != 2) != (speed != 7)"
    rule_expressions[28] = "(speed != 2) != (not (speed != 2))"
    rule_expressions[29] = "(speed != 2) != (not (speed != 2))"
    rule_expressions[30] = "(speed != 2) != (speed != 1)"
    rule_expressions[31] = "(speed != 2) != (not (speed != 2))"
    rule_expressions[32] = "(speed != 2) != (speed != 7)"
    rule_expressions[33] = "(speed != 2) != (not (speed != 2))"
    rule_expressions[34] = "(voltage_mv >= 100) != (not (voltage_mv >= 100))"
    rule_expressions[35] = "(voltage_mv >= 100) != (voltage_mv >= 99)"
    rule_expressions[36] = "(voltage_mv >= 100) != (voltage_mv >= -100)"
    rule_expressions[37] = "(voltage_mv >= 100) != (speed >= 100)"
    rule_expressions[38] = "(voltage_mv >= 100) != (voltage_mv >= 95)"
    rule_expressions[39] = "(voltage_mv >= 100) != (voltage_mv >= 95)"
    rule_expressions[40] = "(voltage_mv >= 100) != (voltage_mv >= 93)"
    rule_expressions[41] = "(voltage_mv >= 100) != (voltage_mv >= 99)"
    rule_expressions[42] = "(voltage_mv >= 100) != (voltage_mv >= -100)"
    rule_expressions[43] = "(altitude <= 100) != (altitude <= -100)"
    rule_expressions[44] = "(altitude <= 100) != (altitude <= -100)"
    rule_expressions[45] = "(altitude <= 100) != (not (altitude <= 100))"
    rule_expressions[46] = "(altitude <= 100) != (altitude <= 94)"
    rule_expressions[47] = "(altitude <= 100) != (altitude <= 98)"
    rule_expressions[48] = "(altitude <= 100) != (not (altitude <= 100))"
    rule_expressions[49] = "(voltage_mv < speed + 99) != (altitude < speed + 99)"
    rule_expressions[50] = "(voltage_mv < speed + 99) != (speed > voltage_mv + 99)"
    rule_expressions[51] = "(voltage_mv < speed + 99) != (voltage_mv < -speed + 99)"
    rule_expressions[52] = "(voltage_mv < speed + 99) != (speed > voltage_mv + 99)"
    rule_expressions[53] = "(voltage_mv < speed + 99) != (voltage_mv < speed + 95)"
    rule_expressions[54] = "(voltage_mv < speed + 99) != (not (voltage_mv < speed + 99))"
    rule_expressions[55] = "(voltage_mv < speed + 99) != (voltage_mv < -speed + 99)"
    rule_expressions[56] = "(voltage_mv < speed + 99) != (voltage_mv < speed + 92)"
    rule_expressions[57] = "(voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 2 or -voltage_mv <= 30)"
    rule_expressions[58] = "(voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 2 and voltage_mv <= 30)"
    rule_expressions[59] = "(voltage_mv < 2 or voltage_mv <= 30) != (voltage_mv < 2 or voltage_mv <= 15)"
    rule_expressions[60] = "(25 <= voltage_mv <= 77) != (not (25) <= voltage_mv <= 77)"
    rule_expressions[61] = "(25 <= voltage_mv <= 77) != (25 <= voltage_mv <= 67)"
    rule_expressions[62] = "(25 <= voltage_mv <= 77) != (25 <= voltage_mv <= 76)"
    rule_expressions[63] = "(25 <= voltage_mv <= 77) != (voltage_mv >= 25 <= 77)"
    rule_expressions[64] = "(25 <= voltage_mv <= 77) != (not (25 <= voltage_mv <= 77))"
    rule_expressions[65] = "(25 <= voltage_mv <= 77) != (25 <= voltage_mv <= -77)"
    rule_expressions[66] = "(25 <= voltage_mv <= 77) != (25 <= speed <= 77)"
    rule_expressions[67] = "(25 <= voltage_mv <= 77) != (25 <= altitude <= 77)"
    rule_expressions[68] = "(25 <= voltage_mv <= 77) != (33 <= voltage_mv <= 77)"
    rule_expressions[69] = "(speed >= 20 or voltage_mv > 5) != (speed >= 20 or -voltage_mv > 5)"
    rule_expressions[70] = "(speed >= 20 or voltage_mv > 5) != (not (speed >= 20 or voltage_mv > 5))"
    rule_expressions[71] = "(speed >= 20 or voltage_mv > 5) != (speed >= 20 or -voltage_mv > 5)"
    rule_expressions[72] = "(speed >= 20 or voltage_mv > 5) != (speed >= 20 or -voltage_mv > 5)"
    rule_expressions[73] = "(30 <= voltage_mv <= 90) != (voltage_mv >= 30 <= 90)"
    rule_expressions[74] = "(30 <= voltage_mv <= 90) != (not (30 <= voltage_mv <= 90))"
    rule_expressions[75] = "(30 <= voltage_mv <= 90) != (30 <= speed <= 90)"
    rule_expressions[76] = "(30 <= voltage_mv <= 90) != (-30 <= voltage_mv <= 90)"
    rule_expressions[77] = "(30 <= voltage_mv <= 90) != (30 <= altitude <= 90)"
    rule_expressions[78] = "(30 <= voltage_mv <= 90) != (25 <= voltage_mv <= 90)"
    rule_expressions[79] = "(30 <= voltage_mv <= 90) != (30 <= -voltage_mv <= 90)"
    rule_expressions[80] = "(30 <= voltage_mv <= 90) != (31 <= voltage_mv <= 90)"
    rule_expressions[81] = "(30 <= voltage_mv <= 90) != (not (30 <= voltage_mv <= 90))"
    rule_expressions[82] = "(voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or altitude >= 2000)"
    rule_expressions[83] = "(voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or -altitude >= 1000)"
    rule_expressions[84] = "(voltage_mv >= 94 or altitude >= 1000) != (altitude >= 94 or altitude >= 1000)"
    rule_expressions[85] = "(voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= -94 or altitude >= 1000)"
    rule_expressions[86] = "(voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or altitude >= 998)"
    rule_expressions[87] = "(voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 or -altitude >= 1000)"
    rule_expressions[88] = "(voltage_mv >= 94 or altitude >= 1000) != (voltage_mv >= 94 and altitude >= 1000)"
    rule_expressions[89] = "(altitude - 205 > voltage_mv) != (altitude - 205 > -voltage_mv)"
    rule_expressions[90] = "(altitude - 205 > voltage_mv) != (altitude - 205 > -voltage_mv)"
    rule_expressions[91] = "(altitude - 205 > voltage_mv) != (altitude - 196 > voltage_mv)"
    rule_expressions[92] = "(altitude - 205 > voltage_mv) != (speed - 205 > voltage_mv)"
    rule_expressions[93] = "(altitude - 205 > voltage_mv) != (not (altitude - 205 > voltage_mv))"
    rule_expressions[94] = "(altitude - 205 > voltage_mv) != (not (altitude - 205 > voltage_mv))"
    rule_expressions[95] = "(altitude - 205 > voltage_mv) != (not (altitude - 205 > voltage_mv))"
    rule_expressions[96] = "(altitude - 205 > voltage_mv) != (altitude - voltage_mv < 205)"
    rule_expressions[97] = "(altitude - 205 > voltage_mv) != (altitude - -205 > voltage_mv)"
    rule_expressions[98] = "(altitude - 205 > voltage_mv) != (altitude - voltage_mv < 205)"
    rule_expressions[99] = "(voltage_mv < 5 or altitude >= 745) != (altitude < 5 or altitude >= 745)"
    rule_expressions[100] = "(voltage_mv < 5 or altitude >= 745) != (speed < 5 or altitude >= 745)"
    rule_expressions[101] = "(voltage_mv < 5 or altitude >= 745) != (not (voltage_mv < 5 or altitude >= 745))"
    rule_expressions[102] = "(6 <= speed <= 96) != (not (6 <= speed <= 96))"
    rule_expressions[103] = "(6 <= speed <= 96) != (6 <= -speed <= 96)"
    rule_expressions[104] = "(6 <= speed <= 96) != (6 <= speed <= 98)"
    rule_expressions[105] = "(6 <= speed <= 96) != (12 <= speed <= 96)"
    rule_expressions[106] = "(6 <= speed <= 96) != (6 <= speed <= -96)"
    rule_expressions[107] = "(6 <= speed <= 96) != (not (6 <= speed <= 96))"
    rule_expressions[108] = "(6 <= speed <= 96) != (6 <= altitude <= 96)"
    rule_expressions[109] = "(6 <= speed <= 96) != (speed >= 6 <= 96)"
    rule_expressions[110] = "(6 <= speed <= 96) != (6 <= -speed <= 96)"
    rule_expressions[111] = "(6 <= speed <= 96) != (not (6 <= speed <= 96))"
    rule_expressions[112] = "(327 <= altitude <= 830) != (not (327 <= altitude <= 830))"
    rule_expressions[113] = "(327 <= altitude <= 830) != (not (327) <= altitude <= 830)"
    rule_expressions[114] = "(327 <= altitude <= 830) != (-327 <= altitude <= 830)"
    rule_expressions[115] = "(327 <= altitude <= 830) != (not (327) <= altitude <= 830)"
    rule_expressions[116] = "(16 <= voltage_mv <= 53) != (18 <= voltage_mv <= 53)"
    rule_expressions[117] = "(16 <= voltage_mv <= 53) != (16 <= speed <= 53)"
    rule_expressions[118] = "(16 <= voltage_mv <= 53) != (21 <= voltage_mv <= 53)"
    rule_expressions[119] = "(16 <= voltage_mv <= 53) != (16 <= -voltage_mv <= 53)"
    rule_expressions[120] = "(16 <= voltage_mv <= 53) != (not (16 <= voltage_mv <= 53))"
    rule_expressions[121] = "(16 <= voltage_mv <= 53) != (not (16) <= voltage_mv <= 53)"
    rule_expressions[122] = "(16 <= voltage_mv <= 53) != (-16 <= voltage_mv <= 53)"
    rule_expressions[123] = "(16 <= voltage_mv <= 53) != (16 <= altitude <= 53)"
    rule_expressions[124] = "(16 <= voltage_mv <= 53) != (8 <= voltage_mv <= 53)"
    rule_expressions[125] = "(voltage_mv >= 50) != (altitude >= 50)"
    rule_expressions[126] = "(voltage_mv >= 50) != (voltage_mv >= 60)"
    rule_expressions[127] = "(voltage_mv >= 50) != (altitude >= 50)"
    rule_expressions[128] = "(voltage_mv >= 50) != (not (voltage_mv >= 50))"
    rule_expressions[129] = "(voltage_mv >= 50) != (voltage_mv >= -50)"
    rule_expressions[130] = "(voltage_mv >= 50) != (voltage_mv >= 60)"
    rule_expressions[131] = "(voltage_mv >= 50) != (voltage_mv >= 43)"
    rule_expressions[132] = "(voltage_mv >= 50) != (altitude >= 50)"
    rule_expressions[133] = "(voltage_mv - speed > 20) != (altitude - speed > 20)"
    rule_expressions[134] = "(voltage_mv - speed > 20) != (not (voltage_mv - speed > 20))"
    rule_expressions[135] = "(voltage_mv - speed > 20) != (altitude - speed > 20)"
    rule_expressions[136] = "(voltage_mv - speed > 20) != (voltage_mv - speed > 25)"
    rule_expressions[137] = "(voltage_mv - speed > 20) != (voltage_mv - speed > 40)"
    rule_expressions[138] = "(voltage_mv - speed > 20) != (voltage_mv - speed > 14)"
    rule_expressions[139] = "(voltage_mv - speed > 20) != (voltage_mv - speed > -20)"
    rule_expressions[140] = "(voltage_mv - speed > 20) != (voltage_mv - speed > 30)"
    rule_expressions[141] = "(voltage_mv - speed > 20) != (voltage_mv - 20 < speed)"
    rule_expressions[142] = "(voltage_mv - speed > 20) != (speed - speed > 20)"
    rule_expressions[143] = "(altitude <= 347 and voltage_mv > 100) != (not (altitude <= 347 and voltage_mv > 100))"
    rule_expressions[144] = "(altitude <= 347 and voltage_mv > 100) != (altitude <= 347 or voltage_mv > 100)"
    rule_expressions[145] = "(altitude <= 347 and voltage_mv > 100) != (altitude <= 347 and voltage_mv > -100)"
    rule_expressions[146] = "(altitude <= 915 and voltage_mv > 100) != (not (altitude <= 915 and voltage_mv > 100))"
    rule_expressions[147] = "(altitude <= 915 and voltage_mv > 100) != (altitude <= 915 or voltage_mv > 100)"
    rule_expressions[148] = "(altitude + voltage_mv != 20) != (altitude + -voltage_mv != 20)"
    rule_expressions[149] = "(altitude + voltage_mv != 20) != (speed + voltage_mv != 20)"
    rule_expressions[150] = "(altitude + voltage_mv != 20) != (not (altitude + voltage_mv != 20))"
    rule_expressions[151] = "(altitude + voltage_mv != 20) != (altitude + 20 != voltage_mv)"
    rule_expressions[152] = "(altitude + voltage_mv != 20) != (altitude + voltage_mv != 25)"
    rule_expressions[153] = "(altitude + voltage_mv != 20) != (not (altitude + voltage_mv != 20))"
    rule_expressions[154] = "(altitude + voltage_mv != 20) != (voltage_mv + voltage_mv != 20)"
    rule_expressions[155] = "(altitude + voltage_mv != 20) != (altitude + -voltage_mv != 20)"
    rule_expressions[156] = "(speed - voltage_mv != 16) != (speed - voltage_mv != 8)"
    rule_expressions[157] = "(speed - voltage_mv != 16) != (speed - voltage_mv != 15)"
    rule_expressions[158] = "(speed - voltage_mv != 16) != (altitude - voltage_mv != 16)"
    rule_expressions[159] = "(speed - voltage_mv != 16) != (not (speed - voltage_mv != 16))"
    rule_expressions[160] = "(speed - voltage_mv != 16) != (speed - voltage_mv != -16)"
    rule_expressions[161] = "(speed - voltage_mv != 16) != (not (speed - voltage_mv != 16))"
    rule_expressions[162] = "(speed - voltage_mv != 16) != (not (speed - voltage_mv != 16))"
    rule_expressions[163] = "(speed != 30) != (not (speed != 30))"
    rule_expressions[164] = "(speed != 30) != (not (speed != 30))"
    rule_expressions[165] = "(speed != 30) != (voltage_mv != 30)"
    rule_expressions[166] = "(speed != 30) != (speed != 60)"
    rule_expressions[167] = "(speed != 30) != (not (speed != 30))"
    rule_expressions[168] = "(speed != 30) != (speed != -30)"
    rule_expressions[169] = "(speed != 30) != (speed != 28)"
    rule_expressions[170] = "(speed != 30) != (speed != -30)"
    rule_expressions[171] = "(voltage_mv * altitude != 35) != (not (voltage_mv * altitude != 35))"
    rule_expressions[172] = "(voltage_mv * altitude != 35) != (not (voltage_mv * altitude != 35))"
    rule_expressions[173] = "(voltage_mv + 50 >= altitude) != (voltage_mv + 57 >= altitude)"
    rule_expressions[174] = "(voltage_mv + 50 >= altitude) != (altitude + 50 >= altitude)"
    rule_expressions[175] = "(voltage_mv + 50 >= altitude) != (speed + 50 >= altitude)"
    rule_expressions[176] = "(voltage_mv + 50 >= altitude) != (not (voltage_mv + 50 >= altitude))"
    rule_expressions[177] = "(voltage_mv + 50 >= altitude) != (voltage_mv + 52 >= altitude)"
    rule_expressions[178] = "(voltage_mv + 50 >= altitude) != (voltage_mv + -50 >= altitude)"
    rule_expressions[179] = "(voltage_mv + 50 >= altitude) != (voltage_mv + 50 >= -altitude)"
    rule_expressions[180] = "(altitude == 5 or voltage_mv <= 100) != (not (altitude == 5 or voltage_mv <= 100))"
    rule_expressions[181] = "(altitude == 5 or voltage_mv <= 100) != (altitude == 5 or voltage_mv <= -100)"
    rule_expressions[182] = "(altitude == 5 or voltage_mv <= 100) != (altitude == 5 and voltage_mv <= 100)"
    rule_expressions[183] = "(altitude > 863) != (not (altitude > 863))"
    rule_expressions[184] = "(altitude > 863) != (not (altitude > 863))"
    rule_expressions[185] = "(altitude > 863) != (altitude > -863)"
    rule_expressions[186] = "(29 <= voltage_mv <= 76) != (29 <= voltage_mv <= 71)"
    rule_expressions[187] = "(29 <= voltage_mv <= 76) != (29 <= speed <= 76)"
    rule_expressions[188] = "(29 <= voltage_mv <= 76) != (not (29 <= voltage_mv <= 76))"
    rule_expressions[189] = "(29 <= voltage_mv <= 76) != (voltage_mv >= 29 <= 76)"
    rule_expressions[190] = "(29 <= voltage_mv <= 76) != (29 <= -voltage_mv <= 76)"
    rule_expressions[191] = "(29 <= voltage_mv <= 76) != (29 <= voltage_mv <= -76)"
    rule_expressions[192] = "(29 <= voltage_mv <= 76) != (29 <= voltage_mv <= -76)"
    rule_expressions[193] = "(29 <= voltage_mv <= 76) != (29 <= speed <= 76)"
    rule_expressions[194] = "(29 <= voltage_mv <= 76) != (32 <= voltage_mv <= 76)"
    rule_expressions[195] = "(voltage_mv < 20) != (not (voltage_mv < 20))"
    rule_expressions[196] = "(voltage_mv < 20) != (voltage_mv < 10)"
    rule_expressions[197] = "(voltage_mv < 20) != (speed < 20)"
    rule_expressions[198] = "(voltage_mv < 20) != (voltage_mv < 19)"
    rule_expressions[199] = "(voltage_mv < 20) != (voltage_mv < 25)"

    return rule_expressions