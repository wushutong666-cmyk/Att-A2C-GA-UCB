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
    # 变异规则 1 - SVR
    if (voltage_mv < 41) != (speed < 41):
        triggered.add(1)
    # 变异规则 2 - SRC
    if (voltage_mv < 41) != (speed < 41):
        triggered.add(2)
    # 变异规则 3 - CRP
    if (voltage_mv < 41) != (voltage_mv < 82):
        triggered.add(3)
    # 变异规则 4 - RSR
    if (voltage_mv < 41) != (not (voltage_mv < 41)):
        triggered.add(4)
    # 变异规则 5 - ROR
    if (voltage_mv < 41) != (abs(voltage_mv) < 41):
        t = 1
    # 变异规则 6 - AOR
    if (voltage_mv < 41) != (not (voltage_mv < 41)):
        triggered.add(5)
    # 变异规则 7 - ABS
    if (voltage_mv < 41) != (abs(voltage_mv) < 41):
        t = 1
    # 变异规则 8 - UOI
    if (voltage_mv < 41) != (not (voltage_mv < 41)):
        triggered.add(6)
    # 变异规则 9 - CAR
    if (voltage_mv < 41) != (voltage_mv < 51):
        triggered.add(7)
    # 变异规则 10 - LCR
    if (voltage_mv < 41) != (41 > voltage_mv):
        t = 1
    # 原语句
    if voltage_mv < 41:
        health_score -= 19
    # 原语句2
    # 变异规则 11 - LCR
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 100 or voltage_mv < 10):
        triggered.add(8)
    # 变异规则 12 - RSR
    if (altitude <= 100 and voltage_mv < 10) != (not (altitude <= 100 and voltage_mv < 10)):
        triggered.add(9)
    # 变异规则 13 - ROR
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and 10 > voltage_mv):
        t = 1
    # 变异规则 14 - AOR
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 100 or voltage_mv < 10):
        triggered.add(10)
    # 变异规则 15 - CRP
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and voltage_mv < 5):
        triggered.add(11)
    # 变异规则 16 - CAR
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 110 and voltage_mv < 10):
        triggered.add(12)
    # 变异规则 17 - SAR
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and 10 > voltage_mv):
        t = 1
    # 变异规则 18 - CSR
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and voltage_mv < -10):
        triggered.add(13)
    # 变异规则 19 - SCR
    if (altitude <= 100 and voltage_mv < 10) != (voltage_mv < 10 and altitude <= 100):
        t = 1
    # 变异规则 20 - UOI
    if (altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and -voltage_mv < 10):
        triggered.add(14)
    # 原语句
    if altitude <= 100 and voltage_mv < 10:
        health_score -= 9
        altitude = min(altitude + 88, 1000)
    # 原语句3
    # 变异规则 21 - LCR
    if (speed > 5) != (not (speed > 5)):
        triggered.add(15)
    # 变异规则 22 - ROR
    if (speed > 5) != (abs(speed) > 5):
        t = 1
    # 变异规则 23 - UOI
    if (speed > 5) != (speed > 10):
        triggered.add(16)
    # 变异规则 24 - RSR
    if (speed > 5) != (not (speed > 5)):
        triggered.add(17)
    # 变异规则 25 - CSR
    if (speed > 5) != (speed > -5):
        triggered.add(18)
    # 变异规则 26 - SAR
    if (speed > 5) != (5 < speed):
        t = 1
    # 变异规则 27 - SRC
    if (speed > 5) != (speed > 2):
        triggered.add(19)
    # 变异规则 28 - AOR
    if (speed > 5) != (5 < speed):
        t = 1
    # 变异规则 29 - SCR
    if (speed > 5) != (speed > 7):
        triggered.add(20)
    # 变异规则 30 - SVR
    if (speed > 5) != (altitude > 5):
        triggered.add(21)
    # 原语句
    if speed > 5:
        health_score -= 16
    # 原语句4
    # 变异规则 31 - CSR
    if (19 <= voltage_mv <= 93) != (-19 <= voltage_mv <= 93):
        triggered.add(22)
    # 变异规则 32 - SAR
    if (19 <= voltage_mv <= 93) != (voltage_mv >= 19 <= 93):
        triggered.add(23)
    # 变异规则 33 - SCR
    if (19 <= voltage_mv <= 93) != (not (19) <= voltage_mv <= 93):
        triggered.add(24)
    # 变异规则 34 - RSR
    if (19 <= voltage_mv <= 93) != (not (19 <= voltage_mv <= 93)):
        triggered.add(25)
    # 变异规则 35 - CRP
    if (19 <= voltage_mv <= 93) != (15 <= voltage_mv <= 93):
        triggered.add(26)
    # 变异规则 36 - SRC
    if (19 <= voltage_mv <= 93) != (19 <= altitude <= 93):
        triggered.add(27)
    # 变异规则 37 - CAR
    if (19 <= voltage_mv <= 93) != (20 <= voltage_mv <= 93):
        triggered.add(28)
    # 变异规则 38 - UOI
    if (19 <= voltage_mv <= 93) != (19 <= -voltage_mv <= 93):
        triggered.add(29)
    # 变异规则 39 - SVR
    if (19 <= voltage_mv <= 93) != (19 <= altitude <= 93):
        triggered.add(30)
    # 变异规则 40 - ABS
    if (19 <= voltage_mv <= 93) != (19 <= abs(voltage_mv) <= 93):
        t = 1
    # 原语句
    if 19 <= voltage_mv <= 93:
        health_score += 7
        voltage_mv = max(voltage_mv - 7, 2)
    # 原语句5
    # 变异规则 41 - SVR
    if (voltage_mv > 5) != (altitude > 5):
        triggered.add(31)
    # 变异规则 42 - CSR
    if (voltage_mv > 5) != (voltage_mv > -5):
        triggered.add(32)
    # 变异规则 43 - RSR
    if (voltage_mv > 5) != (not (voltage_mv > 5)):
        triggered.add(33)
    # 变异规则 44 - SRC
    if (voltage_mv > 5) != (5 < voltage_mv):
        t = 1
    # 变异规则 45 - SAR
    if (voltage_mv > 5) != (5 < voltage_mv):
        t = 1
    # 变异规则 46 - SCR
    if (voltage_mv > 5) != (speed > 5):
        triggered.add(34)
    # 变异规则 47 - LCR
    if (voltage_mv > 5) != (voltage_mv > -5):
        triggered.add(35)
    # 变异规则 48 - CRP
    if (voltage_mv > 5) != (voltage_mv > 1):
        triggered.add(36)
    # 变异规则 49 - ABS
    if (voltage_mv > 5) != (abs(voltage_mv) > 5):
        t = 1
    # 变异规则 50 - AOR
    if (voltage_mv > 5) != (not (voltage_mv > 5)):
        triggered.add(37)
    # 原语句
    if voltage_mv > 5:
        health_score -= 11
        voltage_mv = min(voltage_mv + 7, 100)
        speed, voltage_mv = voltage_mv, speed
    # 原语句6
    # 变异规则 51 - ABS
    if (voltage_mv <= altitude % 100) != (voltage_mv <= abs(altitude) % 100):
        t = 1
    # 变异规则 52 - SCR
    if (voltage_mv <= altitude % 100) != (not (voltage_mv <= altitude % 100)):
        triggered.add(38)
    # 变异规则 53 - CAR
    if (voltage_mv <= altitude % 100) != (voltage_mv <= altitude % 101):
        triggered.add(39)
    # 变异规则 54 - RSR
    if (voltage_mv <= altitude % 100) != (not (voltage_mv <= altitude % 100)):
        triggered.add(40)
    # 变异规则 55 - SVR
    if (voltage_mv <= altitude % 100) != (speed <= altitude % 100):
        triggered.add(41)
    # 变异规则 56 - LCR
    if (voltage_mv <= altitude % 100) != (voltage_mv <= altitude % -100):
        triggered.add(42)
    # 变异规则 57 - SRC
    if (voltage_mv <= altitude % 100) != (voltage_mv <= altitude % 200):
        triggered.add(43)
    # 变异规则 58 - CSR
    if (voltage_mv <= altitude % 100) != (voltage_mv <= altitude % -100):
        triggered.add(44)
    # 变异规则 59 - UOI
    if (voltage_mv <= altitude % 100) != (voltage_mv <= -altitude % 100):
        triggered.add(45)
    # 变异规则 60 - AOR
    if (voltage_mv <= altitude % 100) != (voltage_mv <= altitude % 200):
        triggered.add(46)
    # 原语句
    if voltage_mv <= altitude % 100:
        health_score += 3
        altitude = max(altitude - 12, 2)
        voltage_mv = max(voltage_mv - 8, 2)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句7
    # 变异规则 61 - SAR
    if (voltage_mv > 20) != (20 < voltage_mv):
        t = 1
    # 变异规则 62 - ABS
    if (voltage_mv > 20) != (abs(voltage_mv) > 20):
        t = 1
    # 变异规则 63 - SCR
    if (voltage_mv > 20) != (20 < voltage_mv):
        t = 1
    # 变异规则 64 - RSR
    if (voltage_mv > 20) != (not (voltage_mv > 20)):
        triggered.add(47)
    # 变异规则 65 - AOR
    if (voltage_mv > 20) != (abs(voltage_mv) > 20):
        t = 1
    # 变异规则 66 - ROR
    if (voltage_mv > 20) != (not (voltage_mv > 20)):
        triggered.add(48)
    # 变异规则 67 - SVR
    if (voltage_mv > 20) != (altitude > 20):
        triggered.add(49)
    # 变异规则 68 - LCR
    if (voltage_mv > 20) != (voltage_mv > 29):
        triggered.add(50)
    # 变异规则 69 - CRP
    if (voltage_mv > 20) != (voltage_mv > 26):
        triggered.add(51)
    # 变异规则 70 - CAR
    if (voltage_mv > 20) != (voltage_mv > 19):
        triggered.add(52)
    # 原语句
    if voltage_mv > 20:
        health_score += 10
    # 原语句8
    # 变异规则 71 - SVR
    if (speed + 20 != voltage_mv) != (voltage_mv + 20 != voltage_mv):
        triggered.add(53)
    # 变异规则 72 - SCR
    if (speed + 20 != voltage_mv) != (speed + 20 != -voltage_mv):
        triggered.add(54)
    # 变异规则 73 - SRC
    if (speed + 20 != voltage_mv) != (speed + 40 != voltage_mv):
        triggered.add(55)
    # 变异规则 74 - CRP
    if (speed + 20 != voltage_mv) != (speed + 10 != voltage_mv):
        triggered.add(56)
    # 变异规则 75 - CAR
    if (speed + 20 != voltage_mv) != (speed + 18 != voltage_mv):
        triggered.add(57)
    # 变异规则 76 - ROR
    if (speed + 20 != voltage_mv) != (not (speed + 20 != voltage_mv)):
        triggered.add(58)
    # 变异规则 77 - LCR
    if (speed + 20 != voltage_mv) != (speed + 10 != voltage_mv):
        triggered.add(59)
    # 变异规则 78 - ABS
    if (speed + 20 != voltage_mv) != (abs(speed) + 20 != voltage_mv):
        t = 1
    # 变异规则 79 - CSR
    if (speed + 20 != voltage_mv) != (speed + -20 != voltage_mv):
        triggered.add(60)
    # 变异规则 80 - SAR
    if (speed + 20 != voltage_mv) != (speed + voltage_mv != 20):
        triggered.add(61)
    # 原语句
    if speed + 20 != voltage_mv:
        health_score += 20
    # 原语句9
    # 变异规则 81 - AOR
    if (speed != 30) != (30 != speed):
        t = 1
    # 变异规则 82 - CSR
    if (speed != 30) != (speed != -30):
        triggered.add(62)
    # 变异规则 83 - UOI
    if (speed != 30) != (voltage_mv != 30):
        triggered.add(63)
    # 变异规则 84 - CAR
    if (speed != 30) != (speed != 31):
        triggered.add(64)
    # 变异规则 85 - LCR
    if (speed != 30) != (speed != -30):
        triggered.add(65)
    # 变异规则 86 - ROR
    if (speed != 30) != (speed != 15):
        triggered.add(66)
    # 变异规则 87 - ABS
    if (speed != 30) != (abs(speed) != 30):
        t = 1
    # 变异规则 88 - SRC
    if (speed != 30) != (not (speed != 30)):
        triggered.add(67)
    # 变异规则 89 - RSR
    if (speed != 30) != (not (speed != 30)):
        triggered.add(68)
    # 变异规则 90 - SAR
    if (speed != 30) != (30 != speed):
        t = 1
    # 原语句
    if speed != 30:
        altitude = min(altitude + 79, 1000)
    # 原语句10
    # 变异规则 91 - UOI
    if (altitude >= 1000 and speed <= 21) != (altitude >= 1000 and -speed <= 21):
        triggered.add(69)
    # 变异规则 92 - CAR
    if (altitude >= 1000 and speed <= 21) != (altitude >= 1000 and speed <= 16):
        triggered.add(70)
    # 变异规则 93 - CSR
    if (altitude >= 1000 and speed <= 21) != (altitude >= -1000 and speed <= 21):
        triggered.add(71)
    # 变异规则 94 - SCR
    if (altitude >= 1000 and speed <= 21) != (altitude >= 1000 and speed <= -21):
        triggered.add(72)
    # 变异规则 95 - ABS
    if (altitude >= 1000 and speed <= 21) != (abs(altitude) >= 1000 and speed <= 21):
        t = 1
    # 变异规则 96 - SAR
    if (altitude >= 1000 and speed <= 21) != (altitude >= 1000 and 21 >= speed):
        t = 1
    # 变异规则 97 - ROR
    if (altitude >= 1000 and speed <= 21) != (speed <= 21 and altitude >= 1000):
        t = 1
    # 变异规则 98 - RSR
    if (altitude >= 1000 and speed <= 21) != (not (altitude >= 1000 and speed <= 21)):
        triggered.add(73)
    # 变异规则 99 - CRP
    if (altitude >= 1000 and speed <= 21) != (altitude >= 1000 and speed <= 17):
        triggered.add(74)
    # 变异规则 100 - LCR
    if (altitude >= 1000 and speed <= 21) != (altitude >= 1000 or speed <= 21):
        triggered.add(75)
    # 原语句
    if altitude >= 1000 and speed <= 21:
        health_score += 13
    # 原语句11
    # 变异规则 101 - AOR
    if (speed + 38 != voltage_mv) != (speed + -38 != voltage_mv):
        triggered.add(76)
    # 变异规则 102 - SCR
    if (speed + 38 != voltage_mv) != (speed + 39 != voltage_mv):
        triggered.add(77)
    # 变异规则 103 - LCR
    if (speed + 38 != voltage_mv) != (not (speed + 38 != voltage_mv)):
        triggered.add(78)
    # 变异规则 104 - CSR
    if (speed + 38 != voltage_mv) != (speed + -38 != voltage_mv):
        triggered.add(79)
    # 变异规则 105 - CRP
    if (speed + 38 != voltage_mv) != (speed + 45 != voltage_mv):
        triggered.add(80)
    # 变异规则 106 - CAR
    if (speed + 38 != voltage_mv) != (speed + 36 != voltage_mv):
        triggered.add(81)
    # 变异规则 107 - ABS
    if (speed + 38 != voltage_mv) != (abs(speed) + 38 != voltage_mv):
        t = 1
    # 变异规则 108 - ROR
    if (speed + 38 != voltage_mv) != (not (speed + 38 != voltage_mv)):
        triggered.add(82)
    # 变异规则 109 - SRC
    if (speed + 38 != voltage_mv) != (voltage_mv + 38 != voltage_mv):
        triggered.add(83)
    # 变异规则 110 - RSR
    if (speed + 38 != voltage_mv) != (not (speed + 38 != voltage_mv)):
        triggered.add(84)
    # 原语句
    if speed + 38 != voltage_mv:
        health_score += 3
        altitude = min(altitude + 42, 1000)
    # 原语句12
    # 变异规则 111 - SRC
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv == 51 and voltage_mv > 30):
        t = 1
    # 变异规则 112 - CSR
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and voltage_mv == -51):
        triggered.add(85)
    # 变异规则 113 - ROR
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and voltage_mv == 25):
        triggered.add(86)
    # 变异规则 114 - AOR
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and -voltage_mv == 51):
        triggered.add(87)
    # 变异规则 115 - CRP
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 26 and voltage_mv == 51):
        t = 1
    # 变异规则 116 - RSR
    if (voltage_mv > 30 and voltage_mv == 51) != (not (voltage_mv > 30 and voltage_mv == 51)):
        triggered.add(88)
    # 变异规则 117 - SVR
    if (voltage_mv > 30 and voltage_mv == 51) != (speed > 30 and voltage_mv == 51):
        triggered.add(89)
    # 变异规则 118 - LCR
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 or voltage_mv == 51):
        triggered.add(90)
    # 变异规则 119 - CAR
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and voltage_mv == 41):
        triggered.add(91)
    # 变异规则 120 - UOI
    if (voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and -voltage_mv == 51):
        triggered.add(92)
    # 原语句
    if voltage_mv > 30 and voltage_mv == 51:
        health_score += 20
        altitude = max(altitude - 25, 2)
        speed = max(speed - 5, 2)
    # 原语句13
    # 变异规则 121 - ROR
    if (speed >= 30 or speed == 30) != (speed >= 30 or speed == -30):
        t = 1
    # 变异规则 122 - AOR
    if (speed >= 30 or speed == 30) != (speed >= 30 and speed == 30):
        triggered.add(93)
    # 变异规则 123 - SVR
    if (speed >= 30 or speed == 30) != (voltage_mv >= 30 or speed == 30):
        triggered.add(94)
    # 变异规则 124 - CAR
    if (speed >= 30 or speed == 30) != (speed >= 35 or speed == 30):
        triggered.add(95)
    # 变异规则 125 - SCR
    if (speed >= 30 or speed == 30) != (30 <= speed or speed == 30):
        t = 1
    # 变异规则 126 - ABS
    if (speed >= 30 or speed == 30) != (abs(speed) >= 30 or speed == 30):
        t = 1
    # 变异规则 127 - SRC
    if (speed >= 30 or speed == 30) != (speed == 30 or speed >= 30):
        t = 1
    # 变异规则 128 - CSR
    if (speed >= 30 or speed == 30) != (speed >= 30 or speed == -30):
        t = 1
    # 变异规则 129 - CRP
    if (speed >= 30 or speed == 30) != (speed >= 60 or speed == 30):
        triggered.add(96)
    # 变异规则 130 - LCR
    if (speed >= 30 or speed == 30) != (speed >= 30 and speed == 30):
        triggered.add(97)
    # 原语句
    if speed >= 30 or speed == 30:
        health_score += 16
    # 原语句14
    # 变异规则 131 - SRC
    if (voltage_mv >= 10) != (10 <= voltage_mv):
        t = 1
    # 变异规则 132 - ROR
    if (voltage_mv >= 10) != (voltage_mv >= 7):
        triggered.add(98)
    # 变异规则 133 - CRP
    if (voltage_mv >= 10) != (voltage_mv >= 2):
        triggered.add(99)
    # 变异规则 134 - CAR
    if (voltage_mv >= 10) != (voltage_mv >= 12):
        triggered.add(100)
    # 变异规则 135 - SVR
    if (voltage_mv >= 10) != (altitude >= 10):
        triggered.add(101)
    # 变异规则 136 - ABS
    if (voltage_mv >= 10) != (abs(voltage_mv) >= 10):
        t = 1
    # 变异规则 137 - AOR
    if (voltage_mv >= 10) != (altitude >= 10):
        triggered.add(102)
    # 变异规则 138 - SAR
    if (voltage_mv >= 10) != (10 <= voltage_mv):
        t = 1
    # 变异规则 139 - CSR
    if (voltage_mv >= 10) != (voltage_mv >= -10):
        triggered.add(103)
    # 变异规则 140 - UOI
    if (voltage_mv >= 10) != (not (voltage_mv >= 10)):
        triggered.add(104)
    # 原语句
    if voltage_mv >= 10:
        health_score -= 20
        speed = min(speed + 6, 100)
    # 原语句15
    # 变异规则 141 - ABS
    if (voltage_mv > 100) != (abs(voltage_mv) > 100):
        t = 1
    # 变异规则 142 - SVR
    if (voltage_mv > 100) != (altitude > 100):
        triggered.add(105)
    # 变异规则 143 - RSR
    if (voltage_mv > 100) != (not (voltage_mv > 100)):
        triggered.add(106)
    # 变异规则 144 - CSR
    if (voltage_mv > 100) != (voltage_mv > -100):
        triggered.add(107)
    # 变异规则 145 - ROR
    if (voltage_mv > 100) != (voltage_mv > -100):
        triggered.add(108)
    # 变异规则 146 - SAR
    if (voltage_mv > 100) != (100 < voltage_mv):
        t = 1
    # 变异规则 147 - SRC
    if (voltage_mv > 100) != (voltage_mv > 200):
        triggered.add(109)
    # 变异规则 148 - SCR
    if (voltage_mv > 100) != (voltage_mv > 50):
        triggered.add(110)
    # 变异规则 149 - CAR
    if (voltage_mv > 100) != (voltage_mv > 98):
        triggered.add(111)
    # 变异规则 150 - LCR
    if (voltage_mv > 100) != (100 < voltage_mv):
        t = 1
    # 原语句
    if voltage_mv > 100:
        health_score -= 13
        altitude = max(altitude - 16, 2)
        voltage_mv = min(voltage_mv + 6, 100)
    # 原语句16
    # 变异规则 151 - AOR
    if (speed >= voltage_mv * 10) != (altitude >= voltage_mv * 10):
        triggered.add(112)
    # 变异规则 152 - SVR
    if (speed >= voltage_mv * 10) != (voltage_mv >= voltage_mv * 10):
        triggered.add(113)
    # 变异规则 153 - SAR
    if (speed >= voltage_mv * 10) != (voltage_mv <= speed * 10):
        triggered.add(114)
    # 变异规则 154 - RSR
    if (speed >= voltage_mv * 10) != (not (speed >= voltage_mv * 10)):
        triggered.add(115)
    # 变异规则 155 - LCR
    if (speed >= voltage_mv * 10) != (speed >= -voltage_mv * 10):
        triggered.add(116)
    # 变异规则 156 - SCR
    if (speed >= voltage_mv * 10) != (speed >= voltage_mv * 20):
        triggered.add(117)
    # 变异规则 157 - CSR
    if (speed >= voltage_mv * 10) != (speed >= voltage_mv * -10):
        triggered.add(118)
    # 变异规则 158 - UOI
    if (speed >= voltage_mv * 10) != (speed >= -voltage_mv * 10):
        triggered.add(119)
    # 变异规则 159 - CRP
    if (speed >= voltage_mv * 10) != (speed >= voltage_mv * 15):
        triggered.add(120)
    # 变异规则 160 - ROR
    if (speed >= voltage_mv * 10) != (voltage_mv <= speed * 10):
        triggered.add(121)
    # 原语句
    if speed >= voltage_mv * 10:
        health_score += 13
        altitude = min(altitude + 93, 1000)
    # 原语句17
    # 变异规则 161 - ABS
    if (speed < 50) != (abs(speed) < 50):
        t = 1
    # 变异规则 162 - SAR
    if (speed < 50) != (50 > speed):
        t = 1
    # 变异规则 163 - RSR
    if (speed < 50) != (not (speed < 50)):
        triggered.add(122)
    # 变异规则 164 - CRP
    if (speed < 50) != (speed < 100):
        triggered.add(123)
    # 变异规则 165 - SRC
    if (speed < 50) != (speed < 100):
        triggered.add(124)
    # 变异规则 166 - UOI
    if (speed < 50) != (not (speed < 50)):
        triggered.add(125)
    # 变异规则 167 - SVR
    if (speed < 50) != (voltage_mv < 50):
        triggered.add(126)
    # 变异规则 168 - LCR
    if (speed < 50) != (speed < -50):
        triggered.add(127)
    # 变异规则 169 - AOR
    if (speed < 50) != (speed < 40):
        triggered.add(128)
    # 变异规则 170 - ROR
    if (speed < 50) != (altitude < 50):
        triggered.add(129)
    # 原语句
    if speed < 50:
        health_score -= 30
        altitude = min(altitude + 92, 1000)
        speed, altitude = altitude, speed
    # 原语句18
    # 变异规则 171 - CAR
    if (speed != voltage_mv - 30) != (speed != voltage_mv - 35):
        triggered.add(130)
    # 变异规则 172 - UOI
    if (speed != voltage_mv - 30) != (speed != -voltage_mv - 30):
        triggered.add(131)
    # 变异规则 173 - SRC
    if (speed != voltage_mv - 30) != (speed != -voltage_mv - 30):
        triggered.add(132)
    # 变异规则 174 - RSR
    if (speed != voltage_mv - 30) != (not (speed != voltage_mv - 30)):
        triggered.add(133)
    # 变异规则 175 - LCR
    if (speed != voltage_mv - 30) != (speed != voltage_mv - 28):
        triggered.add(134)
    # 变异规则 176 - SAR
    if (speed != voltage_mv - 30) != (voltage_mv != speed - 30):
        triggered.add(135)
    # 变异规则 177 - ROR
    if (speed != voltage_mv - 30) != (abs(speed) != voltage_mv - 30):
        t = 1
    # 变异规则 178 - CRP
    if (speed != voltage_mv - 30) != (speed != voltage_mv - 33):
        triggered.add(136)
    # 变异规则 179 - ABS
    if (speed != voltage_mv - 30) != (abs(speed) != voltage_mv - 30):
        t = 1
    # 变异规则 180 - AOR
    if (speed != voltage_mv - 30) != (abs(speed) != voltage_mv - 30):
        t = 1
    # 原语句
    if speed != voltage_mv - 30:
        health_score -= 13
        altitude = min(altitude + 81, 1000)
        voltage_mv = max(voltage_mv - 3, 2)
    # 原语句19
    # 变异规则 181 - LCR
    if (30 <= voltage_mv <= 70) != (30 <= voltage_mv <= 68):
        triggered.add(137)
    # 变异规则 182 - SAR
    if (30 <= voltage_mv <= 70) != (voltage_mv >= 30 <= 70):
        triggered.add(138)
    # 变异规则 183 - ABS
    if (30 <= voltage_mv <= 70) != (30 <= abs(voltage_mv) <= 70):
        t = 1
    # 变异规则 184 - ROR
    if (30 <= voltage_mv <= 70) != (27 <= voltage_mv <= 70):
        triggered.add(139)
    # 变异规则 185 - RSR
    if (30 <= voltage_mv <= 70) != (not (30 <= voltage_mv <= 70)):
        triggered.add(140)
    # 变异规则 186 - CSR
    if (30 <= voltage_mv <= 70) != (-30 <= voltage_mv <= 70):
        triggered.add(141)
    # 变异规则 187 - AOR
    if (30 <= voltage_mv <= 70) != (30 <= voltage_mv <= -70):
        triggered.add(142)
    # 变异规则 188 - SCR
    if (30 <= voltage_mv <= 70) != (not (30) <= voltage_mv <= 70):
        triggered.add(143)
    # 变异规则 189 - CAR
    if (30 <= voltage_mv <= 70) != (29 <= voltage_mv <= 70):
        triggered.add(144)
    # 变异规则 190 - SRC
    if (30 <= voltage_mv <= 70) != (-30 <= voltage_mv <= 70):
        triggered.add(145)
    # 原语句
    if 30 <= voltage_mv <= 70:
        health_score -= 28
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句20
    # 变异规则 191 - CAR
    if (altitude <= 50 or speed >= 5) != (altitude <= 50 or speed >= 4):
        t = 1
    # 变异规则 192 - LCR
    if (altitude <= 50 or speed >= 5) != (altitude <= 50 and speed >= 5):
        triggered.add(146)
    # 变异规则 193 - UOI
    if (altitude <= 50 or speed >= 5) != (altitude <= 50 or -speed >= 5):
        triggered.add(147)
    # 变异规则 194 - ABS
    if (altitude <= 50 or speed >= 5) != (abs(altitude) <= 50 or speed >= 5):
        t = 1
    # 变异规则 195 - CSR
    if (altitude <= 50 or speed >= 5) != (altitude <= -50 or speed >= 5):
        t = 1
    # 变异规则 196 - SVR
    if (altitude <= 50 or speed >= 5) != (voltage_mv <= 50 or speed >= 5):
        t = 1
    # 变异规则 197 - AOR
    if (altitude <= 50 or speed >= 5) != (50 >= altitude or speed >= 5):
        t = 1
    # 变异规则 198 - SAR
    if (altitude <= 50 or speed >= 5) != (50 >= altitude or speed >= 5):
        t = 1
    # 变异规则 199 - ROR
    if (altitude <= 50 or speed >= 5) != (50 >= altitude or speed >= 5):
        t = 1
    # 变异规则 200 - SRC
    if (altitude <= 50 or speed >= 5) != (speed >= 5 or altitude <= 50):
        t = 1
    # 原语句
    if altitude <= 50 or speed >= 5:
        health_score -= 11
    # 原语句21
    # 变异规则 201 - SRC
    if (voltage_mv % 18 != altitude) != (voltage_mv % 18 != abs(altitude)):
        t = 1
    # 变异规则 202 - SCR
    if (voltage_mv % 18 != altitude) != (speed % 18 != altitude):
        t = 1
    # 变异规则 203 - CRP
    if (voltage_mv % 18 != altitude) != (voltage_mv % 9 != altitude):
        t = 1
    # 变异规则 204 - ROR
    if (voltage_mv % 18 != altitude) != (voltage_mv % 18 != abs(altitude)):
        t = 1
    # 变异规则 205 - CSR
    if (voltage_mv % 18 != altitude) != (voltage_mv % -18 != altitude):
        t = 1
    # 变异规则 206 - UOI
    if (voltage_mv % 18 != altitude) != (voltage_mv % 18 != -altitude):
        t = 1
    # 变异规则 207 - ABS
    if (voltage_mv % 18 != altitude) != (voltage_mv % 18 != abs(altitude)):
        t = 1
    # 变异规则 208 - LCR
    if (voltage_mv % 18 != altitude) != (voltage_mv % 18 != abs(altitude)):
        t = 1
    # 变异规则 209 - AOR
    if (voltage_mv % 18 != altitude) != (voltage_mv % 18 != -altitude):
        t = 1
    # 变异规则 210 - SVR
    if (voltage_mv % 18 != altitude) != (speed % 18 != altitude):
        t = 1
    # 原语句
    if voltage_mv % 18 != altitude:
        health_score -= 13
    # 原语句22
    # 变异规则 211 - CAR
    if (25 <= altitude <= 776) != (30 <= altitude <= 776):
        t = 1
    # 变异规则 212 - ROR
    if (25 <= altitude <= 776) != (25 <= abs(altitude) <= 776):
        t = 1
    # 变异规则 213 - SCR
    if (25 <= altitude <= 776) != (25 <= -altitude <= 776):
        triggered.add(148)
    # 变异规则 214 - ABS
    if (25 <= altitude <= 776) != (25 <= abs(altitude) <= 776):
        t = 1
    # 变异规则 215 - UOI
    if (25 <= altitude <= 776) != (25 <= -altitude <= 776):
        triggered.add(149)
    # 变异规则 216 - RSR
    if (25 <= altitude <= 776) != (not (25 <= altitude <= 776)):
        triggered.add(150)
    # 变异规则 217 - SVR
    if (25 <= altitude <= 776) != (25 <= speed <= 776):
        triggered.add(151)
    # 变异规则 218 - CSR
    if (25 <= altitude <= 776) != (-25 <= altitude <= 776):
        t = 1
    # 变异规则 219 - CRP
    if (25 <= altitude <= 776) != (50 <= altitude <= 776):
        triggered.add(152)
    # 变异规则 220 - LCR
    if (25 <= altitude <= 776) != (25 <= speed <= 776):
        triggered.add(153)
    # 原语句
    if 25 <= altitude <= 776:
        health_score -= 8
    # 原语句23
    # 变异规则 221 - CAR
    if (6 <= speed <= 96) != (6 <= speed <= 91):
        triggered.add(154)
    # 变异规则 222 - SRC
    if (6 <= speed <= 96) != (8 <= speed <= 96):
        t = 1
    # 变异规则 223 - SVR
    if (6 <= speed <= 96) != (6 <= voltage_mv <= 96):
        triggered.add(155)
    # 变异规则 224 - UOI
    if (6 <= speed <= 96) != (6 <= -speed <= 96):
        triggered.add(156)
    # 变异规则 225 - CRP
    if (6 <= speed <= 96) != (3 <= speed <= 96):
        t = 1
    # 变异规则 226 - AOR
    if (6 <= speed <= 96) != (speed >= 6 <= 96):
        triggered.add(157)
    # 变异规则 227 - CSR
    if (6 <= speed <= 96) != (6 <= speed <= -96):
        triggered.add(158)
    # 变异规则 228 - ROR
    if (6 <= speed <= 96) != (6 <= speed <= -96):
        triggered.add(159)
    # 变异规则 229 - SAR
    if (6 <= speed <= 96) != (speed >= 6 <= 96):
        triggered.add(160)
    # 变异规则 230 - SCR
    if (6 <= speed <= 96) != (not (6) <= speed <= 96):
        triggered.add(161)
    # 原语句
    if 6 <= speed <= 96:
        health_score += 7
    # 原语句24
    # 变异规则 231 - ROR
    if (speed < 51 or voltage_mv > 100) != (speed < -51 or voltage_mv > 100):
        triggered.add(162)
    # 变异规则 232 - RSR
    if (speed < 51 or voltage_mv > 100) != (not (speed < 51 or voltage_mv > 100)):
        triggered.add(163)
    # 变异规则 233 - SVR
    if (speed < 51 or voltage_mv > 100) != (voltage_mv < 51 or voltage_mv > 100):
        triggered.add(164)
    # 变异规则 234 - SCR
    if (speed < 51 or voltage_mv > 100) != (speed < 25 or voltage_mv > 100):
        triggered.add(165)
    # 变异规则 235 - UOI
    if (speed < 51 or voltage_mv > 100) != (speed < 51 or -voltage_mv > 100):
        triggered.add(166)
    # 变异规则 236 - AOR
    if (speed < 51 or voltage_mv > 100) != (speed < 51 or voltage_mv > 50):
        triggered.add(167)
    # 变异规则 237 - SAR
    if (speed < 51 or voltage_mv > 100) != (51 > speed or voltage_mv > 100):
        t = 1
    # 变异规则 238 - ABS
    if (speed < 51 or voltage_mv > 100) != (abs(speed) < 51 or voltage_mv > 100):
        t = 1
    # 变异规则 239 - CSR
    if (speed < 51 or voltage_mv > 100) != (speed < 51 or voltage_mv > -100):
        triggered.add(168)
    # 变异规则 240 - LCR
    if (speed < 51 or voltage_mv > 100) != (speed < 51 and voltage_mv > 100):
        triggered.add(169)
    # 原语句
    if speed < 51 or voltage_mv > 100:
        health_score += 14
        voltage_mv = max(voltage_mv - 6, 2)
    # 原语句25
    # 变异规则 241 - SCR
    if (speed - 10 < altitude) != (not (speed - 10 < altitude)):
        triggered.add(170)
    # 变异规则 242 - ABS
    if (speed - 10 < altitude) != (speed - 10 < abs(altitude)):
        t = 1
    # 变异规则 243 - LCR
    if (speed - 10 < altitude) != (speed - 20 < altitude):
        triggered.add(171)
    # 变异规则 244 - CRP
    if (speed - 10 < altitude) != (speed - 15 < altitude):
        triggered.add(172)
    # 变异规则 245 - ROR
    if (speed - 10 < altitude) != (not (speed - 10 < altitude)):
        triggered.add(173)
    # 变异规则 246 - SAR
    if (speed - 10 < altitude) != (speed - altitude > 10):
        triggered.add(174)
    # 变异规则 247 - UOI
    if (speed - 10 < altitude) != (speed - 10 < -altitude):
        triggered.add(175)
    # 变异规则 248 - CAR
    if (speed - 10 < altitude) != (speed - 15 < altitude):
        triggered.add(176)
    # 变异规则 249 - SRC
    if (speed - 10 < altitude) != (speed - 14 < altitude):
        triggered.add(177)
    # 变异规则 250 - RSR
    if (speed - 10 < altitude) != (not (speed - 10 < altitude)):
        triggered.add(178)
    # 原语句
    if speed - 10 < altitude:
        health_score -= 11
        voltage_mv = max(voltage_mv - 3, 2)
    # 原语句26
    # 变异规则 251 - CSR
    if (18 <= speed <= 69) != (-18 <= speed <= 69):
        t = 1
    # 变异规则 252 - ROR
    if (18 <= speed <= 69) != (18 <= altitude <= 69):
        triggered.add(179)
    # 变异规则 253 - AOR
    if (18 <= speed <= 69) != (18 <= abs(speed) <= 69):
        t = 1
    # 变异规则 254 - SVR
    if (18 <= speed <= 69) != (18 <= altitude <= 69):
        triggered.add(180)
    # 变异规则 255 - SCR
    if (18 <= speed <= 69) != (not (18) <= speed <= 69):
        triggered.add(181)
    # 变异规则 256 - UOI
    if (18 <= speed <= 69) != (18 <= -speed <= 69):
        triggered.add(182)
    # 变异规则 257 - SRC
    if (18 <= speed <= 69) != (not (18) <= speed <= 69):
        triggered.add(183)
    # 变异规则 258 - CAR
    if (18 <= speed <= 69) != (20 <= speed <= 69):
        t = 1
    # 变异规则 259 - ABS
    if (18 <= speed <= 69) != (18 <= abs(speed) <= 69):
        t = 1
    # 变异规则 260 - CRP
    if (18 <= speed <= 69) != (18 <= speed <= 34):
        triggered.add(184)
    # 原语句
    if 18 <= speed <= 69:
        health_score += 1
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句27
    # 变异规则 261 - ABS
    if (voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 and abs(altitude) >= 2):
        t = 1
    # 变异规则 262 - CAR
    if (voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 and altitude >= 1):
        t = 1
    # 变异规则 263 - ROR
    if (voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 and altitude >= 4):
        triggered.add(185)
    # 变异规则 264 - SRC
    if (voltage_mv > 20 and altitude >= 2) != (altitude >= 2 and voltage_mv > 20):
        t = 1
    # 变异规则 265 - SCR
    if (voltage_mv > 20 and altitude >= 2) != (speed > 20 and altitude >= 2):
        triggered.add(186)
    # 变异规则 266 - SAR
    if (voltage_mv > 20 and altitude >= 2) != (20 < voltage_mv and altitude >= 2):
        t = 1
    # 变异规则 267 - AOR
    if (voltage_mv > 20 and altitude >= 2) != (voltage_mv > 18 and altitude >= 2):
        triggered.add(187)
    # 变异规则 268 - LCR
    if (voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 or altitude >= 2):
        triggered.add(188)
    # 变异规则 269 - CRP
    if (voltage_mv > 20 and altitude >= 2) != (voltage_mv > 40 and altitude >= 2):
        triggered.add(189)
    # 变异规则 270 - UOI
    if (voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 and -altitude >= 2):
        triggered.add(190)
    # 原语句
    if voltage_mv > 20 and altitude >= 2:
        health_score -= 11
    # 原语句28
    # 变异规则 271 - CAR
    if (25 <= voltage_mv <= 73) != (26 <= voltage_mv <= 73):
        triggered.add(191)
    # 变异规则 272 - SVR
    if (25 <= voltage_mv <= 73) != (25 <= altitude <= 73):
        triggered.add(192)
    # 变异规则 273 - SCR
    if (25 <= voltage_mv <= 73) != (not (25) <= voltage_mv <= 73):
        triggered.add(193)
    # 变异规则 274 - LCR
    if (25 <= voltage_mv <= 73) != (-25 <= voltage_mv <= 73):
        triggered.add(194)
    # 变异规则 275 - AOR
    if (25 <= voltage_mv <= 73) != (not (25 <= voltage_mv <= 73)):
        triggered.add(195)
    # 变异规则 276 - UOI
    if (25 <= voltage_mv <= 73) != (25 <= -voltage_mv <= 73):
        triggered.add(196)
    # 变异规则 277 - CRP
    if (25 <= voltage_mv <= 73) != (50 <= voltage_mv <= 73):
        triggered.add(197)
    # 变异规则 278 - ABS
    if (25 <= voltage_mv <= 73) != (25 <= abs(voltage_mv) <= 73):
        t = 1
    # 变异规则 279 - ROR
    if (25 <= voltage_mv <= 73) != (not (25 <= voltage_mv <= 73)):
        triggered.add(198)
    # 变异规则 280 - SAR
    if (25 <= voltage_mv <= 73) != (voltage_mv >= 25 <= 73):
        triggered.add(199)
    # 原语句
    if 25 <= voltage_mv <= 73:
        health_score += 8
        speed = max(speed - 5, 2)
    # 原语句29
    # 变异规则 281 - SVR
    if (28 <= speed <= 81) != (28 <= voltage_mv <= 81):
        triggered.add(200)
    # 变异规则 282 - RSR
    if (28 <= speed <= 81) != (not (28 <= speed <= 81)):
        triggered.add(201)
    # 变异规则 283 - LCR
    if (28 <= speed <= 81) != (28 <= abs(speed) <= 81):
        t = 1
    # 变异规则 284 - ROR
    if (28 <= speed <= 81) != (28 <= abs(speed) <= 81):
        t = 1
    # 变异规则 285 - UOI
    if (28 <= speed <= 81) != (28 <= -speed <= 81):
        triggered.add(202)
    # 变异规则 286 - CSR
    if (28 <= speed <= 81) != (28 <= speed <= -81):
        triggered.add(203)
    # 变异规则 287 - ABS
    if (28 <= speed <= 81) != (28 <= abs(speed) <= 81):
        t = 1
    # 变异规则 288 - AOR
    if (28 <= speed <= 81) != (28 <= -speed <= 81):
        triggered.add(204)
    # 变异规则 289 - SRC
    if (28 <= speed <= 81) != (28 <= -speed <= 81):
        triggered.add(205)
    # 变异规则 290 - CAR
    if (28 <= speed <= 81) != (28 <= speed <= 80):
        triggered.add(206)
    # 原语句
    if 28 <= speed <= 81:
        health_score -= 17
        altitude = max(altitude - 40, 2)
        speed = max(speed - 2, 2)
        voltage_mv = min(voltage_mv + 1, 100)
    # 原语句30
    # 变异规则 291 - SCR
    if (voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 and speed <= 2):
        triggered.add(207)
    # 变异规则 292 - CAR
    if (voltage_mv < 20 or speed <= 2) != (voltage_mv < 19 or speed <= 2):
        triggered.add(208)
    # 变异规则 293 - SVR
    if (voltage_mv < 20 or speed <= 2) != (speed < 20 or speed <= 2):
        triggered.add(209)
    # 变异规则 294 - UOI
    if (voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 or -speed <= 2):
        triggered.add(210)
    # 变异规则 295 - ABS
    if (voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 or abs(speed) <= 2):
        t = 1
    # 变异规则 296 - AOR
    if (voltage_mv < 20 or speed <= 2) != (speed <= 2 or voltage_mv < 20):
        t = 1
    # 变异规则 297 - SAR
    if (voltage_mv < 20 or speed <= 2) != (20 > voltage_mv or speed <= 2):
        t = 1
    # 变异规则 298 - LCR
    if (voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 and speed <= 2):
        triggered.add(211)
    # 变异规则 299 - SRC
    if (voltage_mv < 20 or speed <= 2) != (speed <= 2 or voltage_mv < 20):
        t = 1
    # 变异规则 300 - ROR
    if (voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 or -speed <= 2):
        triggered.add(212)
    # 原语句
    if voltage_mv < 20 or speed <= 2:
        health_score -= 4
        altitude = max(altitude - 31, 2)
        speed = max(speed - 4, 2)
    return triggered

targetPaths = [
    {4, 9, 13, 15, 18, 21, 22, 24, 25, 27, 31, 32, 33, 36, 38, 42, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {4, 9, 11, 13, 15, 18, 21, 22, 24, 25, 27, 31, 32, 33, 36, 38, 42, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {4, 9, 11, 13, 15, 18, 21, 22, 24, 25, 27, 33, 34, 38, 42, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {4, 9, 11, 13, 15, 18, 21, 22, 24, 25, 27, 33, 34, 38, 42, 47, 49, 58, 66, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {4, 8, 9, 14, 15, 18, 22, 24, 25, 31, 33, 34, 38, 41, 42, 47, 58, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 18, 22, 24, 25, 31, 33, 34, 38, 41, 42, 47, 58, 61, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 18, 22, 24, 25, 31, 33, 34, 38, 41, 42, 47, 58, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 113, 115, 117, 120, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 18, 22, 24, 25, 26, 31, 33, 34, 38, 41, 42, 47, 58, 60, 67, 73, 78, 88, 99, 101, 103, 104, 105, 106, 107, 113, 115, 117, 120, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 18, 24, 25, 27, 28, 29, 31, 33, 34, 38, 41, 42, 47, 58, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 18, 24, 25, 27, 29, 31, 33, 34, 38, 41, 42, 47, 58, 62, 63, 64, 66, 67, 73, 78, 88, 99, 101, 103, 104, 106, 107, 113, 115, 117, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 18, 24, 25, 27, 29, 31, 33, 34, 38, 41, 42, 47, 58, 64, 67, 73, 78, 88, 93, 94, 95, 96, 99, 101, 103, 104, 105, 106, 107, 113, 115, 117, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 18, 24, 25, 27, 29, 31, 33, 34, 38, 41, 42, 47, 58, 67, 73, 76, 78, 88, 93, 94, 96, 99, 101, 103, 104, 105, 106, 107, 113, 115, 122, 127, 128, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {1, 3, 4, 7, 8, 9, 14, 15, 18, 24, 25, 27, 29, 31, 33, 34, 38, 41, 42, 47, 58, 67, 73, 78, 88, 93, 94, 96, 99, 101, 103, 104, 105, 106, 107, 113, 115, 122, 127, 128, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {1, 3, 4, 7, 8, 9, 14, 15, 18, 24, 25, 27, 29, 31, 33, 34, 38, 41, 42, 47, 58, 67, 73, 78, 88, 93, 94, 96, 99, 101, 103, 104, 105, 106, 107, 113, 115, 122, 123, 126, 133, 140, 141, 143, 146, 147, 148, 150, 155, 156, 158, 161, 162, 163, 165, 169, 170, 174, 175, 179, 181, 182, 184, 185, 190, 193, 195, 199, 200, 201, 202, 203, 210},
    {1, 3, 4, 8, 9, 14, 15, 18, 24, 25, 27, 29, 31, 33, 34, 38, 41, 42, 47, 58, 67, 73, 78, 88, 93, 94, 99, 101, 103, 104, 105, 106, 107, 113, 115, 122, 123, 126, 133, 140, 141, 143, 146, 147, 148, 150, 155, 156, 158, 161, 163, 164, 168, 170, 174, 175, 181, 186, 188, 193, 194, 195, 200, 201, 202, 203, 206, 207, 209},
    {1, 4, 8, 9, 14, 15, 18, 24, 25, 27, 29, 31, 33, 34, 38, 41, 42, 47, 58, 67, 73, 78, 88, 93, 94, 99, 101, 103, 104, 105, 106, 107, 113, 115, 122, 123, 126, 133, 140, 141, 143, 146, 147, 148, 150, 154, 155, 156, 158, 161, 163, 164, 168, 170, 174, 175, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {1, 4, 8, 9, 14, 15, 18, 23, 24, 25, 31, 33, 34, 38, 41, 42, 47, 58, 67, 73, 78, 88, 93, 94, 99, 101, 103, 104, 105, 106, 107, 113, 115, 122, 126, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 175, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 9, 13, 15, 18, 19, 21, 22, 24, 25, 27, 31, 32, 33, 36, 38, 42, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {4, 8, 9, 14, 15, 18, 19, 22, 24, 25, 31, 33, 34, 38, 45, 47, 58, 61, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 9, 13, 15, 16, 20, 22, 24, 25, 27, 31, 32, 33, 34, 36, 38, 42, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {4, 8, 9, 14, 15, 16, 20, 21, 22, 24, 25, 31, 33, 38, 45, 47, 58, 67, 71, 73, 75, 78, 88, 98, 99, 101, 103, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 16, 21, 22, 24, 25, 31, 33, 38, 45, 47, 58, 67, 71, 73, 75, 78, 88, 100, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 16, 21, 24, 25, 27, 29, 31, 33, 38, 45, 47, 58, 60, 62, 63, 64, 66, 67, 73, 78, 88, 100, 104, 106, 107, 114, 115, 116, 118, 122, 127, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 171, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 52, 58, 67, 71, 73, 75, 78, 88, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {1, 3, 4, 7, 8, 9, 14, 15, 21, 24, 25, 27, 29, 31, 33, 38, 45, 47, 52, 58, 67, 73, 78, 88, 93, 94, 96, 104, 105, 106, 107, 114, 115, 116, 118, 122, 123, 126, 133, 135, 140, 141, 143, 146, 147, 148, 150, 156, 158, 161, 162, 163, 165, 169, 170, 174, 175, 179, 181, 182, 184, 190, 193, 195, 199, 200, 201, 202, 203, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 50, 51, 58, 67, 71, 73, 75, 78, 88, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 50, 51, 58, 67, 71, 73, 75, 78, 88, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 187, 188, 193, 194, 195, 201, 207, 208, 209},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 50, 51, 58, 67, 71, 73, 75, 78, 88, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 189, 190, 193, 194, 195, 201, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 50, 56, 58, 67, 71, 73, 75, 78, 88, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 189, 190, 193, 194, 195, 201, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 50, 58, 67, 71, 73, 75, 78, 88, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 189, 190, 191, 192, 193, 195, 196, 197, 201, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 58, 63, 67, 71, 73, 75, 78, 88, 94, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 139, 140, 141, 143, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 189, 190, 192, 193, 195, 196, 197, 201, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 139, 140, 141, 143, 144, 146, 147, 148, 150, 155, 157, 161, 163, 164, 168, 170, 174, 181, 189, 190, 192, 193, 195, 196, 197, 200, 201, 210},
    {4, 9, 13, 15, 22, 24, 25, 27, 31, 32, 33, 34, 36, 38, 42, 47, 49, 58, 67, 73, 78, 80, 88, 90, 93, 95, 96, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 142, 143, 148, 150, 152, 157, 161, 163, 166, 169, 170, 174, 179, 181, 190, 192, 193, 195, 199, 201, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 57, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 142, 143, 148, 150, 152, 157, 161, 163, 166, 169, 170, 174, 179, 181, 190, 192, 193, 195, 199, 201, 210},
    {4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 53, 54, 55, 56, 57, 58, 60, 61, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 142, 143, 148, 150, 152, 157, 161, 163, 166, 169, 170, 174, 179, 181, 190, 192, 193, 195, 199, 201, 210},
    {4, 9, 13, 15, 22, 24, 25, 27, 31, 32, 33, 34, 36, 38, 42, 47, 49, 58, 67, 73, 77, 78, 88, 90, 93, 96, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 128, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {1, 3, 4, 7, 8, 9, 14, 15, 21, 24, 25, 27, 29, 31, 33, 38, 45, 47, 49, 58, 67, 73, 78, 88, 90, 93, 96, 104, 105, 106, 107, 114, 115, 116, 118, 122, 123, 126, 133, 140, 142, 143, 148, 150, 152, 155, 156, 158, 161, 163, 170, 171, 172, 174, 181, 182, 184, 189, 190, 192, 193, 195, 196, 197, 201, 202, 203, 210},
    {4, 9, 13, 15, 22, 24, 25, 27, 31, 32, 33, 34, 36, 38, 42, 47, 49, 58, 67, 73, 76, 77, 78, 80, 81, 83, 88, 90, 93, 96, 104, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 128, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 200, 201, 210},
    {1, 3, 4, 7, 8, 9, 14, 15, 21, 24, 25, 27, 29, 31, 33, 38, 45, 47, 49, 58, 67, 73, 78, 88, 90, 93, 96, 104, 105, 106, 107, 114, 115, 116, 118, 122, 123, 126, 133, 140, 142, 143, 148, 150, 152, 155, 156, 158, 161, 163, 170, 171, 172, 174, 177, 181, 182, 184, 189, 190, 192, 193, 195, 196, 197, 201, 202, 203, 210},
    {1, 4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 91, 94, 104, 105, 106, 107, 114, 115, 116, 118, 122, 127, 129, 133, 140, 142, 143, 148, 150, 152, 157, 161, 163, 166, 169, 170, 174, 179, 181, 190, 192, 193, 195, 199, 201, 210},
    {1, 4, 9, 13, 15, 22, 24, 25, 27, 31, 32, 33, 34, 36, 38, 42, 47, 49, 58, 67, 73, 78, 88, 90, 93, 96, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 123, 133, 134, 138, 140, 143, 146, 147, 148, 150, 156, 158, 161, 162, 163, 164, 165, 169, 170, 174, 175, 179, 181, 182, 184, 190, 192, 193, 195, 199, 200, 201, 202, 203, 210},
    {1, 4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 58, 67, 71, 73, 75, 78, 85, 86, 87, 88, 89, 91, 94, 104, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 140, 142, 143, 148, 150, 152, 157, 161, 163, 167, 168, 170, 174, 179, 181, 190, 192, 193, 195, 199, 201, 210},
    {1, 4, 8, 9, 14, 15, 21, 22, 24, 25, 31, 33, 38, 45, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 126, 127, 129, 133, 137, 140, 142, 143, 146, 147, 148, 150, 157, 161, 163, 166, 169, 170, 174, 179, 181, 190, 192, 193, 195, 199, 201, 210},
    {3, 4, 7, 8, 9, 14, 15, 21, 24, 25, 27, 29, 31, 33, 38, 45, 47, 49, 58, 67, 73, 78, 81, 88, 90, 93, 96, 104, 105, 106, 107, 110, 114, 115, 116, 118, 122, 123, 130, 131, 133, 134, 135, 136, 138, 140, 143, 146, 147, 148, 150, 156, 158, 161, 162, 163, 164, 165, 169, 170, 174, 175, 179, 181, 182, 184, 190, 192, 193, 195, 199, 200, 201, 202, 203, 210},
    {1, 4, 9, 11, 13, 15, 22, 24, 25, 27, 33, 38, 41, 47, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 105, 106, 107, 110, 111, 114, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 155, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 201, 210},
    {4, 9, 13, 15, 18, 21, 22, 24, 25, 31, 32, 33, 36, 38, 39, 43, 47, 49, 58, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 9, 13, 15, 18, 21, 22, 24, 25, 31, 32, 33, 36, 38, 42, 47, 49, 58, 67, 71, 73, 75, 78, 88, 90, 94, 104, 106, 109, 115, 116, 118, 122, 126, 127, 129, 133, 138, 140, 143, 146, 147, 148, 150, 157, 161, 163, 167, 168, 170, 174, 181, 190, 193, 195, 199, 201, 210},
    {4, 8, 9, 12, 15, 18, 21, 22, 24, 25, 31, 32, 33, 36, 38, 43, 45, 47, 49, 58, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 9, 15, 18, 21, 22, 24, 25, 33, 34, 38, 39, 43, 47, 49, 58, 67, 71, 73, 75, 78, 88, 99, 101, 103, 104, 105, 106, 107, 113, 115, 117, 120, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 151, 157, 161, 163, 164, 168, 170, 174, 181, 186, 188, 193, 194, 195, 201, 207, 209},
    {4, 8, 9, 15, 22, 24, 25, 33, 38, 41, 43, 45, 47, 50, 51, 58, 67, 72, 73, 78, 88, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 151, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 187, 188, 193, 194, 195, 201, 207, 208, 209},
    {4, 9, 15, 22, 24, 25, 33, 38, 41, 43, 45, 47, 50, 51, 58, 67, 70, 72, 73, 78, 88, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 151, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 187, 188, 193, 194, 195, 201, 207, 208, 209},
    {4, 9, 15, 22, 24, 25, 33, 38, 41, 43, 45, 47, 50, 51, 58, 67, 70, 72, 73, 74, 78, 88, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 151, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 187, 188, 193, 194, 195, 201, 207, 208, 209},
    {4, 9, 15, 22, 24, 25, 26, 33, 38, 43, 45, 47, 50, 51, 58, 67, 69, 73, 75, 78, 88, 104, 105, 106, 107, 112, 114, 115, 116, 118, 122, 127, 129, 133, 140, 141, 143, 146, 147, 148, 150, 151, 155, 157, 161, 163, 164, 168, 170, 174, 181, 186, 187, 188, 193, 194, 195, 201, 207, 208, 209}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 3:3, 4:4, 6:5, 8:6, 9:7, 11:8, 12:9, 14:10, 15:11, 16:12, 18:13, 20:14, 21:15, 23:16, 24:17, 25:18, 27:19, 29:20, 30:21, 31:22, 32:23, 33:24, 34:25, 35:26, 36:27, 37:28, 38:29, 39:30, 41:31, 42:32, 43:33, 46:34, 47:35, 48:36, 50:37, 52:38, 53:39, 54:40, 55:41, 56:42, 57:43, 58:44, 59:45, 60:46, 64:47, 66:48, 67:49, 68:50, 69:51, 70:52, 71:53, 72:54, 73:55, 74:56, 75:57, 76:58, 77:59, 79:60, 80:61, 82:62, 83:63, 84:64, 85:65, 86:66, 88:67, 89:68, 91:69, 92:70, 93:71, 94:72, 98:73, 99:74, 100:75, 101:76, 102:77, 103:78, 104:79, 105:80, 106:81, 108:82, 109:83, 110:84, 112:85, 113:86, 114:87, 116:88, 117:89, 118:90, 119:91, 120:92, 122:93, 123:94, 124:95, 129:96, 130:97, 132:98, 133:99, 134:100, 135:101, 137:102, 139:103, 140:104, 142:105, 143:106, 144:107, 145:108, 147:109, 148:110, 149:111, 151:112, 152:113, 153:114, 154:115, 155:116, 156:117, 157:118, 158:119, 159:120, 160:121, 163:122, 164:123, 165:124, 166:125, 167:126, 168:127, 169:128, 170:129, 171:130, 172:131, 173:132, 174:133, 175:134, 176:135, 178:136, 181:137, 182:138, 184:139, 185:140, 186:141, 187:142, 188:143, 189:144, 190:145, 192:146, 193:147, 213:148, 215:149, 216:150, 217:151, 219:152, 220:153, 221:154, 223:155, 224:156, 226:157, 227:158, 228:159, 229:160, 230:161, 231:162, 232:163, 233:164, 234:165, 235:166, 236:167, 239:168, 240:169, 241:170, 243:171, 244:172, 245:173, 246:174, 247:175, 248:176, 249:177, 250:178, 252:179, 254:180, 255:181, 256:182, 257:183, 260:184, 263:185, 265:186, 267:187, 268:188, 269:189, 270:190, 271:191, 272:192, 273:193, 274:194, 275:195, 276:196, 277:197, 279:198, 280:199, 281:200, 282:201, 285:202, 286:203, 288:204, 289:205, 290:206, 291:207, 292:208, 293:209, 294:210, 298:211, 300:212}

    rule_expressions[1] = "(voltage_mv < 41) != (speed < 41)"
    rule_expressions[2] = "(voltage_mv < 41) != (speed < 41)"
    rule_expressions[3] = "(voltage_mv < 41) != (voltage_mv < 82)"
    rule_expressions[4] = "(voltage_mv < 41) != (not (voltage_mv < 41))"
    rule_expressions[5] = "(voltage_mv < 41) != (not (voltage_mv < 41))"
    rule_expressions[6] = "(voltage_mv < 41) != (not (voltage_mv < 41))"
    rule_expressions[7] = "(voltage_mv < 41) != (voltage_mv < 51)"
    rule_expressions[8] = "(altitude <= 100 and voltage_mv < 10) != (altitude <= 100 or voltage_mv < 10)"
    rule_expressions[9] = "(altitude <= 100 and voltage_mv < 10) != (not (altitude <= 100 and voltage_mv < 10))"
    rule_expressions[10] = "(altitude <= 100 and voltage_mv < 10) != (altitude <= 100 or voltage_mv < 10)"
    rule_expressions[11] = "(altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and voltage_mv < 5)"
    rule_expressions[12] = "(altitude <= 100 and voltage_mv < 10) != (altitude <= 110 and voltage_mv < 10)"
    rule_expressions[13] = "(altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and voltage_mv < -10)"
    rule_expressions[14] = "(altitude <= 100 and voltage_mv < 10) != (altitude <= 100 and -voltage_mv < 10)"
    rule_expressions[15] = "(speed > 5) != (not (speed > 5))"
    rule_expressions[16] = "(speed > 5) != (speed > 10)"
    rule_expressions[17] = "(speed > 5) != (not (speed > 5))"
    rule_expressions[18] = "(speed > 5) != (speed > -5)"
    rule_expressions[19] = "(speed > 5) != (speed > 2)"
    rule_expressions[20] = "(speed > 5) != (speed > 7)"
    rule_expressions[21] = "(speed > 5) != (altitude > 5)"
    rule_expressions[22] = "(19 <= voltage_mv <= 93) != (-19 <= voltage_mv <= 93)"
    rule_expressions[23] = "(19 <= voltage_mv <= 93) != (voltage_mv >= 19 <= 93)"
    rule_expressions[24] = "(19 <= voltage_mv <= 93) != (not (19) <= voltage_mv <= 93)"
    rule_expressions[25] = "(19 <= voltage_mv <= 93) != (not (19 <= voltage_mv <= 93))"
    rule_expressions[26] = "(19 <= voltage_mv <= 93) != (15 <= voltage_mv <= 93)"
    rule_expressions[27] = "(19 <= voltage_mv <= 93) != (19 <= altitude <= 93)"
    rule_expressions[28] = "(19 <= voltage_mv <= 93) != (20 <= voltage_mv <= 93)"
    rule_expressions[29] = "(19 <= voltage_mv <= 93) != (19 <= -voltage_mv <= 93)"
    rule_expressions[30] = "(19 <= voltage_mv <= 93) != (19 <= altitude <= 93)"
    rule_expressions[31] = "(voltage_mv > 5) != (altitude > 5)"
    rule_expressions[32] = "(voltage_mv > 5) != (voltage_mv > -5)"
    rule_expressions[33] = "(voltage_mv > 5) != (not (voltage_mv > 5))"
    rule_expressions[34] = "(voltage_mv > 5) != (speed > 5)"
    rule_expressions[35] = "(voltage_mv > 5) != (voltage_mv > -5)"
    rule_expressions[36] = "(voltage_mv > 5) != (voltage_mv > 1)"
    rule_expressions[37] = "(voltage_mv > 5) != (not (voltage_mv > 5))"
    rule_expressions[38] = "(voltage_mv <= altitude % 100) != (not (voltage_mv <= altitude % 100))"
    rule_expressions[39] = "(voltage_mv <= altitude % 100) != (voltage_mv <= altitude % 101)"
    rule_expressions[40] = "(voltage_mv <= altitude % 100) != (not (voltage_mv <= altitude % 100))"
    rule_expressions[41] = "(voltage_mv <= altitude % 100) != (speed <= altitude % 100)"
    rule_expressions[42] = "(voltage_mv <= altitude % 100) != (voltage_mv <= altitude % -100)"
    rule_expressions[43] = "(voltage_mv <= altitude % 100) != (voltage_mv <= altitude % 200)"
    rule_expressions[44] = "(voltage_mv <= altitude % 100) != (voltage_mv <= altitude % -100)"
    rule_expressions[45] = "(voltage_mv <= altitude % 100) != (voltage_mv <= -altitude % 100)"
    rule_expressions[46] = "(voltage_mv <= altitude % 100) != (voltage_mv <= altitude % 200)"
    rule_expressions[47] = "(voltage_mv > 20) != (not (voltage_mv > 20))"
    rule_expressions[48] = "(voltage_mv > 20) != (not (voltage_mv > 20))"
    rule_expressions[49] = "(voltage_mv > 20) != (altitude > 20)"
    rule_expressions[50] = "(voltage_mv > 20) != (voltage_mv > 29)"
    rule_expressions[51] = "(voltage_mv > 20) != (voltage_mv > 26)"
    rule_expressions[52] = "(voltage_mv > 20) != (voltage_mv > 19)"
    rule_expressions[53] = "(speed + 20 != voltage_mv) != (voltage_mv + 20 != voltage_mv)"
    rule_expressions[54] = "(speed + 20 != voltage_mv) != (speed + 20 != -voltage_mv)"
    rule_expressions[55] = "(speed + 20 != voltage_mv) != (speed + 40 != voltage_mv)"
    rule_expressions[56] = "(speed + 20 != voltage_mv) != (speed + 10 != voltage_mv)"
    rule_expressions[57] = "(speed + 20 != voltage_mv) != (speed + 18 != voltage_mv)"
    rule_expressions[58] = "(speed + 20 != voltage_mv) != (not (speed + 20 != voltage_mv))"
    rule_expressions[59] = "(speed + 20 != voltage_mv) != (speed + 10 != voltage_mv)"
    rule_expressions[60] = "(speed + 20 != voltage_mv) != (speed + -20 != voltage_mv)"
    rule_expressions[61] = "(speed + 20 != voltage_mv) != (speed + voltage_mv != 20)"
    rule_expressions[62] = "(speed != 30) != (speed != -30)"
    rule_expressions[63] = "(speed != 30) != (voltage_mv != 30)"
    rule_expressions[64] = "(speed != 30) != (speed != 31)"
    rule_expressions[65] = "(speed != 30) != (speed != -30)"
    rule_expressions[66] = "(speed != 30) != (speed != 15)"
    rule_expressions[67] = "(speed != 30) != (not (speed != 30))"
    rule_expressions[68] = "(speed != 30) != (not (speed != 30))"
    rule_expressions[69] = "(altitude >= 1000 and speed <= 21) != (altitude >= 1000 and -speed <= 21)"
    rule_expressions[70] = "(altitude >= 1000 and speed <= 21) != (altitude >= 1000 and speed <= 16)"
    rule_expressions[71] = "(altitude >= 1000 and speed <= 21) != (altitude >= -1000 and speed <= 21)"
    rule_expressions[72] = "(altitude >= 1000 and speed <= 21) != (altitude >= 1000 and speed <= -21)"
    rule_expressions[73] = "(altitude >= 1000 and speed <= 21) != (not (altitude >= 1000 and speed <= 21))"
    rule_expressions[74] = "(altitude >= 1000 and speed <= 21) != (altitude >= 1000 and speed <= 17)"
    rule_expressions[75] = "(altitude >= 1000 and speed <= 21) != (altitude >= 1000 or speed <= 21)"
    rule_expressions[76] = "(speed + 38 != voltage_mv) != (speed + -38 != voltage_mv)"
    rule_expressions[77] = "(speed + 38 != voltage_mv) != (speed + 39 != voltage_mv)"
    rule_expressions[78] = "(speed + 38 != voltage_mv) != (not (speed + 38 != voltage_mv))"
    rule_expressions[79] = "(speed + 38 != voltage_mv) != (speed + -38 != voltage_mv)"
    rule_expressions[80] = "(speed + 38 != voltage_mv) != (speed + 45 != voltage_mv)"
    rule_expressions[81] = "(speed + 38 != voltage_mv) != (speed + 36 != voltage_mv)"
    rule_expressions[82] = "(speed + 38 != voltage_mv) != (not (speed + 38 != voltage_mv))"
    rule_expressions[83] = "(speed + 38 != voltage_mv) != (voltage_mv + 38 != voltage_mv)"
    rule_expressions[84] = "(speed + 38 != voltage_mv) != (not (speed + 38 != voltage_mv))"
    rule_expressions[85] = "(voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and voltage_mv == -51)"
    rule_expressions[86] = "(voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and voltage_mv == 25)"
    rule_expressions[87] = "(voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and -voltage_mv == 51)"
    rule_expressions[88] = "(voltage_mv > 30 and voltage_mv == 51) != (not (voltage_mv > 30 and voltage_mv == 51))"
    rule_expressions[89] = "(voltage_mv > 30 and voltage_mv == 51) != (speed > 30 and voltage_mv == 51)"
    rule_expressions[90] = "(voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 or voltage_mv == 51)"
    rule_expressions[91] = "(voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and voltage_mv == 41)"
    rule_expressions[92] = "(voltage_mv > 30 and voltage_mv == 51) != (voltage_mv > 30 and -voltage_mv == 51)"
    rule_expressions[93] = "(speed >= 30 or speed == 30) != (speed >= 30 and speed == 30)"
    rule_expressions[94] = "(speed >= 30 or speed == 30) != (voltage_mv >= 30 or speed == 30)"
    rule_expressions[95] = "(speed >= 30 or speed == 30) != (speed >= 35 or speed == 30)"
    rule_expressions[96] = "(speed >= 30 or speed == 30) != (speed >= 60 or speed == 30)"
    rule_expressions[97] = "(speed >= 30 or speed == 30) != (speed >= 30 and speed == 30)"
    rule_expressions[98] = "(voltage_mv >= 10) != (voltage_mv >= 7)"
    rule_expressions[99] = "(voltage_mv >= 10) != (voltage_mv >= 2)"
    rule_expressions[100] = "(voltage_mv >= 10) != (voltage_mv >= 12)"
    rule_expressions[101] = "(voltage_mv >= 10) != (altitude >= 10)"
    rule_expressions[102] = "(voltage_mv >= 10) != (altitude >= 10)"
    rule_expressions[103] = "(voltage_mv >= 10) != (voltage_mv >= -10)"
    rule_expressions[104] = "(voltage_mv >= 10) != (not (voltage_mv >= 10))"
    rule_expressions[105] = "(voltage_mv > 100) != (altitude > 100)"
    rule_expressions[106] = "(voltage_mv > 100) != (not (voltage_mv > 100))"
    rule_expressions[107] = "(voltage_mv > 100) != (voltage_mv > -100)"
    rule_expressions[108] = "(voltage_mv > 100) != (voltage_mv > -100)"
    rule_expressions[109] = "(voltage_mv > 100) != (voltage_mv > 200)"
    rule_expressions[110] = "(voltage_mv > 100) != (voltage_mv > 50)"
    rule_expressions[111] = "(voltage_mv > 100) != (voltage_mv > 98)"
    rule_expressions[112] = "(speed >= voltage_mv * 10) != (altitude >= voltage_mv * 10)"
    rule_expressions[113] = "(speed >= voltage_mv * 10) != (voltage_mv >= voltage_mv * 10)"
    rule_expressions[114] = "(speed >= voltage_mv * 10) != (voltage_mv <= speed * 10)"
    rule_expressions[115] = "(speed >= voltage_mv * 10) != (not (speed >= voltage_mv * 10))"
    rule_expressions[116] = "(speed >= voltage_mv * 10) != (speed >= -voltage_mv * 10)"
    rule_expressions[117] = "(speed >= voltage_mv * 10) != (speed >= voltage_mv * 20)"
    rule_expressions[118] = "(speed >= voltage_mv * 10) != (speed >= voltage_mv * -10)"
    rule_expressions[119] = "(speed >= voltage_mv * 10) != (speed >= -voltage_mv * 10)"
    rule_expressions[120] = "(speed >= voltage_mv * 10) != (speed >= voltage_mv * 15)"
    rule_expressions[121] = "(speed >= voltage_mv * 10) != (voltage_mv <= speed * 10)"
    rule_expressions[122] = "(speed < 50) != (not (speed < 50))"
    rule_expressions[123] = "(speed < 50) != (speed < 100)"
    rule_expressions[124] = "(speed < 50) != (speed < 100)"
    rule_expressions[125] = "(speed < 50) != (not (speed < 50))"
    rule_expressions[126] = "(speed < 50) != (voltage_mv < 50)"
    rule_expressions[127] = "(speed < 50) != (speed < -50)"
    rule_expressions[128] = "(speed < 50) != (speed < 40)"
    rule_expressions[129] = "(speed < 50) != (altitude < 50)"
    rule_expressions[130] = "(speed != voltage_mv - 30) != (speed != voltage_mv - 35)"
    rule_expressions[131] = "(speed != voltage_mv - 30) != (speed != -voltage_mv - 30)"
    rule_expressions[132] = "(speed != voltage_mv - 30) != (speed != -voltage_mv - 30)"
    rule_expressions[133] = "(speed != voltage_mv - 30) != (not (speed != voltage_mv - 30))"
    rule_expressions[134] = "(speed != voltage_mv - 30) != (speed != voltage_mv - 28)"
    rule_expressions[135] = "(speed != voltage_mv - 30) != (voltage_mv != speed - 30)"
    rule_expressions[136] = "(speed != voltage_mv - 30) != (speed != voltage_mv - 33)"
    rule_expressions[137] = "(30 <= voltage_mv <= 70) != (30 <= voltage_mv <= 68)"
    rule_expressions[138] = "(30 <= voltage_mv <= 70) != (voltage_mv >= 30 <= 70)"
    rule_expressions[139] = "(30 <= voltage_mv <= 70) != (27 <= voltage_mv <= 70)"
    rule_expressions[140] = "(30 <= voltage_mv <= 70) != (not (30 <= voltage_mv <= 70))"
    rule_expressions[141] = "(30 <= voltage_mv <= 70) != (-30 <= voltage_mv <= 70)"
    rule_expressions[142] = "(30 <= voltage_mv <= 70) != (30 <= voltage_mv <= -70)"
    rule_expressions[143] = "(30 <= voltage_mv <= 70) != (not (30) <= voltage_mv <= 70)"
    rule_expressions[144] = "(30 <= voltage_mv <= 70) != (29 <= voltage_mv <= 70)"
    rule_expressions[145] = "(30 <= voltage_mv <= 70) != (-30 <= voltage_mv <= 70)"
    rule_expressions[146] = "(altitude <= 50 or speed >= 5) != (altitude <= 50 and speed >= 5)"
    rule_expressions[147] = "(altitude <= 50 or speed >= 5) != (altitude <= 50 or -speed >= 5)"
    rule_expressions[148] = "(25 <= altitude <= 776) != (25 <= -altitude <= 776)"
    rule_expressions[149] = "(25 <= altitude <= 776) != (25 <= -altitude <= 776)"
    rule_expressions[150] = "(25 <= altitude <= 776) != (not (25 <= altitude <= 776))"
    rule_expressions[151] = "(25 <= altitude <= 776) != (25 <= speed <= 776)"
    rule_expressions[152] = "(25 <= altitude <= 776) != (50 <= altitude <= 776)"
    rule_expressions[153] = "(25 <= altitude <= 776) != (25 <= speed <= 776)"
    rule_expressions[154] = "(6 <= speed <= 96) != (6 <= speed <= 91)"
    rule_expressions[155] = "(6 <= speed <= 96) != (6 <= voltage_mv <= 96)"
    rule_expressions[156] = "(6 <= speed <= 96) != (6 <= -speed <= 96)"
    rule_expressions[157] = "(6 <= speed <= 96) != (speed >= 6 <= 96)"
    rule_expressions[158] = "(6 <= speed <= 96) != (6 <= speed <= -96)"
    rule_expressions[159] = "(6 <= speed <= 96) != (6 <= speed <= -96)"
    rule_expressions[160] = "(6 <= speed <= 96) != (speed >= 6 <= 96)"
    rule_expressions[161] = "(6 <= speed <= 96) != (not (6) <= speed <= 96)"
    rule_expressions[162] = "(speed < 51 or voltage_mv > 100) != (speed < -51 or voltage_mv > 100)"
    rule_expressions[163] = "(speed < 51 or voltage_mv > 100) != (not (speed < 51 or voltage_mv > 100))"
    rule_expressions[164] = "(speed < 51 or voltage_mv > 100) != (voltage_mv < 51 or voltage_mv > 100)"
    rule_expressions[165] = "(speed < 51 or voltage_mv > 100) != (speed < 25 or voltage_mv > 100)"
    rule_expressions[166] = "(speed < 51 or voltage_mv > 100) != (speed < 51 or -voltage_mv > 100)"
    rule_expressions[167] = "(speed < 51 or voltage_mv > 100) != (speed < 51 or voltage_mv > 50)"
    rule_expressions[168] = "(speed < 51 or voltage_mv > 100) != (speed < 51 or voltage_mv > -100)"
    rule_expressions[169] = "(speed < 51 or voltage_mv > 100) != (speed < 51 and voltage_mv > 100)"
    rule_expressions[170] = "(speed - 10 < altitude) != (not (speed - 10 < altitude))"
    rule_expressions[171] = "(speed - 10 < altitude) != (speed - 20 < altitude)"
    rule_expressions[172] = "(speed - 10 < altitude) != (speed - 15 < altitude)"
    rule_expressions[173] = "(speed - 10 < altitude) != (not (speed - 10 < altitude))"
    rule_expressions[174] = "(speed - 10 < altitude) != (speed - altitude > 10)"
    rule_expressions[175] = "(speed - 10 < altitude) != (speed - 10 < -altitude)"
    rule_expressions[176] = "(speed - 10 < altitude) != (speed - 15 < altitude)"
    rule_expressions[177] = "(speed - 10 < altitude) != (speed - 14 < altitude)"
    rule_expressions[178] = "(speed - 10 < altitude) != (not (speed - 10 < altitude))"
    rule_expressions[179] = "(18 <= speed <= 69) != (18 <= altitude <= 69)"
    rule_expressions[180] = "(18 <= speed <= 69) != (18 <= altitude <= 69)"
    rule_expressions[181] = "(18 <= speed <= 69) != (not (18) <= speed <= 69)"
    rule_expressions[182] = "(18 <= speed <= 69) != (18 <= -speed <= 69)"
    rule_expressions[183] = "(18 <= speed <= 69) != (not (18) <= speed <= 69)"
    rule_expressions[184] = "(18 <= speed <= 69) != (18 <= speed <= 34)"
    rule_expressions[185] = "(voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 and altitude >= 4)"
    rule_expressions[186] = "(voltage_mv > 20 and altitude >= 2) != (speed > 20 and altitude >= 2)"
    rule_expressions[187] = "(voltage_mv > 20 and altitude >= 2) != (voltage_mv > 18 and altitude >= 2)"
    rule_expressions[188] = "(voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 or altitude >= 2)"
    rule_expressions[189] = "(voltage_mv > 20 and altitude >= 2) != (voltage_mv > 40 and altitude >= 2)"
    rule_expressions[190] = "(voltage_mv > 20 and altitude >= 2) != (voltage_mv > 20 and -altitude >= 2)"
    rule_expressions[191] = "(25 <= voltage_mv <= 73) != (26 <= voltage_mv <= 73)"
    rule_expressions[192] = "(25 <= voltage_mv <= 73) != (25 <= altitude <= 73)"
    rule_expressions[193] = "(25 <= voltage_mv <= 73) != (not (25) <= voltage_mv <= 73)"
    rule_expressions[194] = "(25 <= voltage_mv <= 73) != (-25 <= voltage_mv <= 73)"
    rule_expressions[195] = "(25 <= voltage_mv <= 73) != (not (25 <= voltage_mv <= 73))"
    rule_expressions[196] = "(25 <= voltage_mv <= 73) != (25 <= -voltage_mv <= 73)"
    rule_expressions[197] = "(25 <= voltage_mv <= 73) != (50 <= voltage_mv <= 73)"
    rule_expressions[198] = "(25 <= voltage_mv <= 73) != (not (25 <= voltage_mv <= 73))"
    rule_expressions[199] = "(25 <= voltage_mv <= 73) != (voltage_mv >= 25 <= 73)"
    rule_expressions[200] = "(28 <= speed <= 81) != (28 <= voltage_mv <= 81)"
    rule_expressions[201] = "(28 <= speed <= 81) != (not (28 <= speed <= 81))"
    rule_expressions[202] = "(28 <= speed <= 81) != (28 <= -speed <= 81)"
    rule_expressions[203] = "(28 <= speed <= 81) != (28 <= speed <= -81)"
    rule_expressions[204] = "(28 <= speed <= 81) != (28 <= -speed <= 81)"
    rule_expressions[205] = "(28 <= speed <= 81) != (28 <= -speed <= 81)"
    rule_expressions[206] = "(28 <= speed <= 81) != (28 <= speed <= 80)"
    rule_expressions[207] = "(voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 and speed <= 2)"
    rule_expressions[208] = "(voltage_mv < 20 or speed <= 2) != (voltage_mv < 19 or speed <= 2)"
    rule_expressions[209] = "(voltage_mv < 20 or speed <= 2) != (speed < 20 or speed <= 2)"
    rule_expressions[210] = "(voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 or -speed <= 2)"
    rule_expressions[211] = "(voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 and speed <= 2)"
    rule_expressions[212] = "(voltage_mv < 20 or speed <= 2) != (voltage_mv < 20 or -speed <= 2)"

    return rule_expressions

