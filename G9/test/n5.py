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
    # 变异规则 1 - CAR
    if (voltage_mv - speed < 50) != (voltage_mv - speed < 51):
        triggered.add(1)
    # 变异规则 2 - UOI
    if (voltage_mv - speed < 50) != (altitude - speed < 50):
        triggered.add(2)
    # 变异规则 3 - SAR
    if (voltage_mv - speed < 50) != (voltage_mv - 50 > speed):
        triggered.add(3)
    # 变异规则 4 - AOR
    if (voltage_mv - speed < 50) != (voltage_mv - speed < -50):
        triggered.add(4)
    # 变异规则 5 - ABS
    if (voltage_mv - speed < 50) != (voltage_mv - abs(speed) < 50):
        t=1
    # 变异规则 6 - RSR
    if (voltage_mv - speed < 50) != (not (voltage_mv - speed < 50)):
        triggered.add(5)
    # 变异规则 7 - CRP
    if (voltage_mv - speed < 50) != (voltage_mv - speed < 25):
        triggered.add(6)
    # 变异规则 8 - LCR
    if (voltage_mv - speed < 50) != (speed - speed < 50):
        triggered.add(7)
    # 变异规则 9 - SRC
    if (voltage_mv - speed < 50) != (not (voltage_mv - speed < 50)):
        triggered.add(8)
    # 变异规则 10 - ROR
    if (voltage_mv - speed < 50) != (not (voltage_mv - speed < 50)):
        triggered.add(9)
    # 原语句
    if voltage_mv - speed < 50:
        altitude = max(altitude - 20, 2)
    # 原语句2
    # 变异规则 11 - SRC
    if (altitude // 50 <= voltage_mv) != (altitude // 50 <= -voltage_mv):
        triggered.add(10)
    # 变异规则 12 - RSR
    if (altitude // 50 <= voltage_mv) != (not (altitude // 50 <= voltage_mv)):
        triggered.add(11)
    # 变异规则 13 - ABS
    if (altitude // 50 <= voltage_mv) != (abs(altitude) // 50 <= voltage_mv):
        t=1
    # 变异规则 14 - CAR
    if (altitude // 50 <= voltage_mv) != (altitude // 40 <= voltage_mv):
        triggered.add(12)
    # 变异规则 15 - ROR
    if (altitude // 50 <= voltage_mv) != (not (altitude // 50 <= voltage_mv)):
        triggered.add(13)
    # 变异规则 16 - UOI
    if (altitude // 50 <= voltage_mv) != (altitude // 50 <= -voltage_mv):
        triggered.add(14)
    # 变异规则 17 - SCR
    if (altitude // 50 <= voltage_mv) != (altitude // 50 <= -voltage_mv):
        triggered.add(15)
    # 变异规则 18 - LCR
    if (altitude // 50 <= voltage_mv) != (altitude // voltage_mv >= 50):
        triggered.add(16)
    # 变异规则 19 - AOR
    if (altitude // 50 <= voltage_mv) != (altitude // voltage_mv >= 50):
        triggered.add(17)
    # 变异规则 20 - CRP
    if (altitude // 50 <= voltage_mv) != (altitude // 44 <= voltage_mv):
        triggered.add(18)
    # 原语句
    if altitude // 50 <= voltage_mv:
        health_score -= 9
        altitude = max(altitude - 46, 2)
        voltage_mv = max(voltage_mv - 6, 2)
    # 原语句3
    # 变异规则 21 - LCR
    if (16 <= speed <= 72) != (16 <= speed <= -72):
        triggered.add(19)
    # 变异规则 22 - RSR
    if (16 <= speed <= 72) != (not (16 <= speed <= 72)):
        triggered.add(20)
    # 变异规则 23 - ROR
    if (16 <= speed <= 72) != (16 <= altitude <= 72):
        triggered.add(21)
    # 变异规则 24 - UOI
    if (16 <= speed <= 72) != (16 <= -speed <= 72):
        triggered.add(22)
    # 变异规则 25 - CRP
    if (16 <= speed <= 72) != (16 <= speed <= 75):
        triggered.add(23)
    # 变异规则 26 - SRC
    if (16 <= speed <= 72) != (16 <= speed <= 77):
        triggered.add(24)
    # 变异规则 27 - SAR
    if (16 <= speed <= 72) != (speed >= 16 <= 72):
        triggered.add(25)
    # 变异规则 28 - CAR
    if (16 <= speed <= 72) != (16 <= speed <= 67):
        triggered.add(26)
    # 变异规则 29 - AOR
    if (16 <= speed <= 72) != (16 <= -speed <= 72):
        triggered.add(27)
    # 变异规则 30 - CSR
    if (16 <= speed <= 72) != (16 <= speed <= -72):
        triggered.add(28)
    # 原语句
    if 16 <= speed <= 72:
        health_score -= 24
        speed = min(speed + 2, 100)
    # 原语句4
    # 变异规则 31 - SRC
    if (altitude >= 200 or voltage_mv < 20) != (voltage_mv < 20 or altitude >= 200):
        t=1
    # 变异规则 32 - CRP
    if (altitude >= 200 or voltage_mv < 20) != (altitude >= 208 or voltage_mv < 20):
        triggered.add(29)
    # 变异规则 33 - UOI
    if (altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or -voltage_mv < 20):
        triggered.add(30)
    # 变异规则 34 - CAR
    if (altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or voltage_mv < 18):
        triggered.add(31)
    # 变异规则 35 - ABS
    if (altitude >= 200 or voltage_mv < 20) != (abs(altitude) >= 200 or voltage_mv < 20):
        t=1
    # 变异规则 36 - CSR
    if (altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or voltage_mv < -20):
        triggered.add(32)
    # 变异规则 37 - SCR
    if (altitude >= 200 or voltage_mv < 20) != (not (altitude >= 200 or voltage_mv < 20)):
        triggered.add(33)
    # 变异规则 38 - SAR
    if (altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or 20 > voltage_mv):
        t=1
    # 变异规则 39 - ROR
    if (altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or voltage_mv < 40):
        triggered.add(34)
    # 变异规则 40 - LCR
    if (altitude >= 200 or voltage_mv < 20) != (altitude >= 200 and voltage_mv < 20):
        triggered.add(35)
    # 原语句
    if altitude >= 200 or voltage_mv < 20:
        health_score -= 29
        speed = max(speed - 5, 2)
    # 原语句5
    # 变异规则 41 - SCR
    if (voltage_mv <= 73 or voltage_mv != 69) != (73 >= voltage_mv or voltage_mv != 69):
        t=1
    # 变异规则 42 - AOR
    if (voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 or -voltage_mv != 69):
        t=1
    # 变异规则 43 - CSR
    if (voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 or voltage_mv != -69):
        t=1
    # 变异规则 44 - SRC
    if (voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv != 69 or voltage_mv <= 73):
        t=1
    # 变异规则 45 - ROR
    if (voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 and voltage_mv != 69):
        triggered.add(36)
    # 变异规则 46 - SAR
    if (voltage_mv <= 73 or voltage_mv != 69) != (73 >= voltage_mv or voltage_mv != 69):
        t=1
    # 变异规则 47 - LCR
    if (voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 and voltage_mv != 69):
        triggered.add(37)
    # 变异规则 48 - ABS
    if (voltage_mv <= 73 or voltage_mv != 69) != (abs(voltage_mv) <= 73 or voltage_mv != 69):
        t=1
    # 变异规则 49 - UOI
    if (voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 or -voltage_mv != 69):
        t=1
    # 变异规则 50 - CAR
    if (voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 or voltage_mv != 74):
        triggered.add(38)
    # 原语句
    if voltage_mv <= 73 or voltage_mv != 69:
        health_score -= 11
        speed = min(speed + 6, 100)
    # 原语句6
    # 变异规则 51 - ROR
    if (altitude <= 420 and speed < 95) != (altitude <= 420 or speed < 95):
        triggered.add(39)
    # 变异规则 52 - RSR
    if (altitude <= 420 and speed < 95) != (not (altitude <= 420 and speed < 95)):
        triggered.add(40)
    # 变异规则 53 - LCR
    if (altitude <= 420 and speed < 95) != (altitude <= 420 or speed < 95):
        triggered.add(41)
    # 变异规则 54 - CSR
    if (altitude <= 420 and speed < 95) != (altitude <= -420 and speed < 95):
        triggered.add(42)
    # 变异规则 55 - CAR
    if (altitude <= 420 and speed < 95) != (altitude <= 410 and speed < 95):
        triggered.add(43)
    # 变异规则 56 - CRP
    if (altitude <= 420 and speed < 95) != (altitude <= 210 and speed < 95):
        triggered.add(44)
    # 变异规则 57 - AOR
    if (altitude <= 420 and speed < 95) != (altitude <= 415 and speed < 95):
        triggered.add(45)
    # 变异规则 58 - SCR
    if (altitude <= 420 and speed < 95) != (altitude <= 420 and speed < 97):
        triggered.add(46)
    # 变异规则 59 - ABS
    if (altitude <= 420 and speed < 95) != (abs(altitude) <= 420 and speed < 95):
        t=1
    # 变异规则 60 - SVR
    if (altitude <= 420 and speed < 95) != (voltage_mv <= 420 and speed < 95):
        triggered.add(47)
    # 原语句
    if altitude <= 420 and speed < 95:
        health_score -= 24
        voltage_mv = min(voltage_mv + 3, 100)
    # 原语句7
    # 变异规则 61 - CAR
    if (altitude != 5 and altitude != 5) != (altitude != 6 and altitude != 5):
        triggered.add(48)
    # 变异规则 62 - LCR
    if (altitude != 5 and altitude != 5) != (altitude != 5 or altitude != 5):
        t=1
    # 变异规则 63 - ABS
    if (altitude != 5 and altitude != 5) != (abs(altitude) != 5 and altitude != 5):
        t=1
    # 变异规则 64 - SAR
    if (altitude != 5 and altitude != 5) != (5 != altitude and altitude != 5):
        t=1
    # 变异规则 65 - UOI
    if (altitude != 5 and altitude != 5) != (altitude != 5 and -altitude != 5):
        t=1
    # 变异规则 66 - CRP
    if (altitude != 5 and altitude != 5) != (altitude != 4 and altitude != 5):
        triggered.add(49)
    # 变异规则 67 - SCR
    if (altitude != 5 and altitude != 5) != (speed != 5 and altitude != 5):
        t=1
    # 变异规则 68 - RSR
    if (altitude != 5 and altitude != 5) != (not (altitude != 5 and altitude != 5)):
        triggered.add(50)
    # 变异规则 69 - ROR
    if (altitude != 5 and altitude != 5) != (5 != altitude and altitude != 5):
        t=1
    # 变异规则 70 - SRC
    if (altitude != 5 and altitude != 5) != (altitude != 5 and -altitude != 5):
        t=1
    # 原语句
    if altitude != 5 and altitude != 5:
        health_score += 20
    # 原语句8
    # 变异规则 71 - CRP
    if (speed > 34) != (speed > 27):
        triggered.add(51)
    # 变异规则 72 - AOR
    if (speed > 34) != (abs(speed) > 34):
        t=1
    # 变异规则 73 - CAR
    if (speed > 34) != (speed > 24):
        triggered.add(52)
    # 变异规则 74 - SCR
    if (speed > 34) != (speed > 68):
        triggered.add(53)
    # 变异规则 75 - UOI
    if (speed > 34) != (speed > 35):
        triggered.add(54)
    # 变异规则 76 - SRC
    if (speed > 34) != (34 < speed):
        t=1
    # 变异规则 77 - LCR
    if (speed > 34) != (altitude > 34):
        triggered.add(55)
    # 变异规则 78 - ABS
    if (speed > 34) != (abs(speed) > 34):
        t=1
    # 变异规则 79 - SAR
    if (speed > 34) != (34 < speed):
        t=1
    # 变异规则 80 - ROR
    if (speed > 34) != (speed > 17):
        triggered.add(56)
    # 原语句
    if speed > 34:
        health_score -= 26
        voltage_mv = max(voltage_mv - 2, 2)
    # 原语句9
    # 变异规则 81 - CSR
    if (speed != 30 or altitude > 10) != (speed != -30 or altitude > 10):
        triggered.add(57)
    # 变异规则 82 - SAR
    if (speed != 30 or altitude > 10) != (speed != 30 or 10 < altitude):
        t=1
    # 变异规则 83 - UOI
    if (speed != 30 or altitude > 10) != (speed != 30 or -altitude > 10):
        triggered.add(58)
    # 变异规则 84 - AOR
    if (speed != 30 or altitude > 10) != (speed != 30 or 10 < altitude):
        t=1
    # 变异规则 85 - ABS
    if (speed != 30 or altitude > 10) != (speed != 30 or abs(altitude) > 10):
        t=1
    # 变异规则 86 - LCR
    if (speed != 30 or altitude > 10) != (speed != 30 and altitude > 10):
        triggered.add(59)
    # 变异规则 87 - ROR
    if (speed != 30 or altitude > 10) != (speed != 30 or -altitude > 10):
        triggered.add(60)
    # 变异规则 88 - SRC
    if (speed != 30 or altitude > 10) != (altitude > 10 or speed != 30):
        t=1
    # 变异规则 89 - SVR
    if (speed != 30 or altitude > 10) != (altitude != 30 or altitude > 10):
        triggered.add(61)
    # 变异规则 90 - CAR
    if (speed != 30 or altitude > 10) != (speed != 32 or altitude > 10):
        triggered.add(62)
    # 原语句
    if speed != 30 or altitude > 10:
        health_score -= 14
        voltage_mv, speed = speed, voltage_mv
    # 原语句10
    # 变异规则 91 - SAR
    if (altitude <= 863) != (863 >= altitude):
        t=1
    # 变异规则 92 - CRP
    if (altitude <= 863) != (altitude <= 862):
        triggered.add(63)
    # 变异规则 93 - ROR
    if (altitude <= 863) != (altitude <= -863):
        triggered.add(64)
    # 变异规则 94 - CAR
    if (altitude <= 863) != (altitude <= 873):
        triggered.add(65)
    # 变异规则 95 - CSR
    if (altitude <= 863) != (altitude <= -863):
        triggered.add(66)
    # 变异规则 96 - LCR
    if (altitude <= 863) != (not (altitude <= 863)):
        triggered.add(67)
    # 变异规则 97 - SCR
    if (altitude <= 863) != (altitude <= -863):
        triggered.add(68)
    # 变异规则 98 - SRC
    if (altitude <= 863) != (abs(altitude) <= 863):
        t=1
    # 变异规则 99 - AOR
    if (altitude <= 863) != (863 >= altitude):
        t=1
    # 变异规则 100 - RSR
    if (altitude <= 863) != (not (altitude <= 863)):
        triggered.add(69)
    # 原语句
    if altitude <= 863:
        health_score += 16
        altitude = min(altitude + 43, 1000)
    # 原语句11
    # 变异规则 101 - ROR
    if (voltage_mv % 99 < altitude) != (voltage_mv % 99 < abs(altitude)):
        t=1
    # 变异规则 102 - CRP
    if (voltage_mv % 99 < altitude) != (voltage_mv % 49 < altitude):
        triggered.add(70)
    # 变异规则 103 - RSR
    if (voltage_mv % 99 < altitude) != (not (voltage_mv % 99 < altitude)):
        triggered.add(71)
    # 变异规则 104 - CAR
    if (voltage_mv % 99 < altitude) != (voltage_mv % 100 < altitude):
        triggered.add(72)
    # 变异规则 105 - SCR
    if (voltage_mv % 99 < altitude) != (voltage_mv % 98 < altitude):
        triggered.add(73)
    # 变异规则 106 - SAR
    if (voltage_mv % 99 < altitude) != (voltage_mv % altitude > 99):
        triggered.add(74)
    # 变异规则 107 - UOI
    if (voltage_mv % 99 < altitude) != (voltage_mv % 99 < -altitude):
        triggered.add(75)
    # 变异规则 108 - CSR
    if (voltage_mv % 99 < altitude) != (voltage_mv % -99 < altitude):
        triggered.add(76)
    # 变异规则 109 - SRC
    if (voltage_mv % 99 < altitude) != (voltage_mv % 101 < altitude):
        triggered.add(77)
    # 变异规则 110 - SVR
    if (voltage_mv % 99 < altitude) != (altitude % 99 < altitude):
        triggered.add(78)
    # 原语句
    if voltage_mv % 99 < altitude:
        health_score += 6
        altitude = max(altitude - 40, 2)
    # 原语句12
    # 变异规则 111 - UOI
    if (31 <= voltage_mv <= 90) != (31 <= -voltage_mv <= 90):
        triggered.add(79)
    # 变异规则 112 - ABS
    if (31 <= voltage_mv <= 90) != (31 <= abs(voltage_mv) <= 90):
        t=1
    # 变异规则 113 - SAR
    if (31 <= voltage_mv <= 90) != (voltage_mv >= 31 <= 90):
        triggered.add(80)
    # 变异规则 114 - SVR
    if (31 <= voltage_mv <= 90) != (31 <= altitude <= 90):
        triggered.add(81)
    # 变异规则 115 - LCR
    if (31 <= voltage_mv <= 90) != (voltage_mv >= 31 <= 90):
        triggered.add(82)
    # 变异规则 116 - CAR
    if (31 <= voltage_mv <= 90) != (31 <= voltage_mv <= 91):
        triggered.add(83)
    # 变异规则 117 - SCR
    if (31 <= voltage_mv <= 90) != (31 <= speed <= 90):
        triggered.add(84)
    # 变异规则 118 - CRP
    if (31 <= voltage_mv <= 90) != (31 <= voltage_mv <= 83):
        triggered.add(85)
    # 变异规则 119 - CSR
    if (31 <= voltage_mv <= 90) != (31 <= voltage_mv <= -90):
        triggered.add(86)
    # 变异规则 120 - ROR
    if (31 <= voltage_mv <= 90) != (31 <= -voltage_mv <= 90):
        triggered.add(87)
    # 原语句
    if 31 <= voltage_mv <= 90:
        speed = min(speed + 5, 100)
        voltage_mv = max(voltage_mv - 6, 2)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句13
    # 变异规则 121 - CRP
    if (speed > voltage_mv + 50) != (speed > voltage_mv + 100):
        triggered.add(88)
    # 变异规则 122 - AOR
    if (speed > voltage_mv + 50) != (speed > voltage_mv + -50):
        triggered.add(89)
    # 变异规则 123 - CSR
    if (speed > voltage_mv + 50) != (speed > voltage_mv + -50):
        triggered.add(90)
    # 变异规则 124 - RSR
    if (speed > voltage_mv + 50) != (not (speed > voltage_mv + 50)):
        triggered.add(91)
    # 变异规则 125 - ABS
    if (speed > voltage_mv + 50) != (abs(speed) > voltage_mv + 50):
        t=1
    # 变异规则 126 - CAR
    if (speed > voltage_mv + 50) != (speed > voltage_mv + 60):
        triggered.add(92)
    # 变异规则 127 - SVR
    if (speed > voltage_mv + 50) != (altitude > voltage_mv + 50):
        triggered.add(93)
    # 变异规则 128 - ROR
    if (speed > voltage_mv + 50) != (not (speed > voltage_mv + 50)):
        triggered.add(94)
    # 变异规则 129 - SRC
    if (speed > voltage_mv + 50) != (abs(speed) > voltage_mv + 50):
        t=1
    # 变异规则 130 - LCR
    if (speed > voltage_mv + 50) != (not (speed > voltage_mv + 50)):
        triggered.add(95)
    # 原语句
    if speed > voltage_mv + 50:
        health_score -= 11
        speed = max(speed - 9, 2)
        voltage_mv = min(voltage_mv + 6, 100)
    # 原语句14
    # 变异规则 131 - UOI
    if (speed < 30) != (abs(speed) < 30):
        t=1
    # 变异规则 132 - LCR
    if (speed < 30) != (speed < -30):
        triggered.add(96)
    # 变异规则 133 - AOR
    if (speed < 30) != (abs(speed) < 30):
        t=1
    # 变异规则 134 - SCR
    if (speed < 30) != (altitude < 30):
        triggered.add(97)
    # 变异规则 135 - RSR
    if (speed < 30) != (not (speed < 30)):
        triggered.add(98)
    # 变异规则 136 - ABS
    if (speed < 30) != (abs(speed) < 30):
        t=1
    # 变异规则 137 - SRC
    if (speed < 30) != (voltage_mv < 30):
        triggered.add(99)
    # 变异规则 138 - CSR
    if (speed < 30) != (speed < -30):
        triggered.add(100)
    # 变异规则 139 - ROR
    if (speed < 30) != (not (speed < 30)):
        triggered.add(101)
    # 变异规则 140 - CAR
    if (speed < 30) != (speed < 28):
        triggered.add(102)
    # 原语句
    if speed < 30:
        health_score += 14
        speed = min(speed + 7, 100)
    # 原语句15
    # 变异规则 141 - UOI
    if (altitude <= 30) != (abs(altitude) <= 30):
        t=1
    # 变异规则 142 - SRC
    if (altitude <= 30) != (not (altitude <= 30)):
        triggered.add(103)
    # 变异规则 143 - ABS
    if (altitude <= 30) != (abs(altitude) <= 30):
        t=1
    # 变异规则 144 - SVR
    if (altitude <= 30) != (voltage_mv <= 30):
        triggered.add(104)
    # 变异规则 145 - RSR
    if (altitude <= 30) != (not (altitude <= 30)):
        triggered.add(105)
    # 变异规则 146 - CRP
    if (altitude <= 30) != (altitude <= 15):
        triggered.add(106)
    # 变异规则 147 - LCR
    if (altitude <= 30) != (abs(altitude) <= 30):
        t=1
    # 变异规则 148 - AOR
    if (altitude <= 30) != (speed <= 30):
        triggered.add(107)
    # 变异规则 149 - SCR
    if (altitude <= 30) != (altitude <= 15):
        triggered.add(108)
    # 变异规则 150 - ROR
    if (altitude <= 30) != (abs(altitude) <= 30):
        t=1
    # 原语句
    if altitude <= 30:
        health_score += 15
    # 原语句16
    # 变异规则 151 - SCR
    if (speed < 2) != (speed < -2):
        t=1
    # 变异规则 152 - CAR
    if (speed < 2) != (speed < 4):
        t=1
    # 变异规则 153 - ROR
    if (speed < 2) != (speed < 1):
        t=1
    # 变异规则 154 - ABS
    if (speed < 2) != (abs(speed) < 2):
        t=1
    # 变异规则 155 - CRP
    if (speed < 2) != (speed < 9):
        t=1
    # 变异规则 156 - CSR
    if (speed < 2) != (speed < -2):
        t=1
    # 变异规则 157 - AOR
    if (speed < 2) != (not (speed < 2)):
        triggered.add(109)
    # 变异规则 158 - RSR
    if (speed < 2) != (not (speed < 2)):
        triggered.add(110)
    # 变异规则 159 - SRC
    if (speed < 2) != (not (speed < 2)):
        triggered.add(111)
    # 变异规则 160 - UOI
    if (speed < 2) != (speed < 1):
        t=1
    # 原语句
    if speed < 2:
        health_score += 6
        speed = max(speed - 7, 2)
    # 原语句17
    # 变异规则 161 - SCR
    if (altitude == 1000 or voltage_mv > 30) != (abs(altitude) == 1000 or voltage_mv > 30):
        t=1
    # 变异规则 162 - SAR
    if (altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or 30 < voltage_mv):
        t=1
    # 变异规则 163 - RSR
    if (altitude == 1000 or voltage_mv > 30) != (not (altitude == 1000 or voltage_mv > 30)):
        triggered.add(112)
    # 变异规则 164 - UOI
    if (altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or -voltage_mv > 30):
        triggered.add(113)
    # 变异规则 165 - ABS
    if (altitude == 1000 or voltage_mv > 30) != (abs(altitude) == 1000 or voltage_mv > 30):
        t=1
    # 变异规则 166 - ROR
    if (altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or 30 < voltage_mv):
        t=1
    # 变异规则 167 - CRP
    if (altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or voltage_mv > 15):
        triggered.add(114)
    # 变异规则 168 - SVR
    if (altitude == 1000 or voltage_mv > 30) != (voltage_mv == 1000 or voltage_mv > 30):
        t=1
    # 变异规则 169 - LCR
    if (altitude == 1000 or voltage_mv > 30) != (altitude == 1000 and voltage_mv > 30):
        triggered.add(115)
    # 变异规则 170 - CAR
    if (altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or voltage_mv > 31):
        triggered.add(116)
    # 原语句
    if altitude == 1000 or voltage_mv > 30:
        health_score += 15
    # 原语句18
    # 变异规则 171 - ROR
    if (speed != voltage_mv + 53) != (speed != voltage_mv + 52):
        triggered.add(117)
    # 变异规则 172 - SVR
    if (speed != voltage_mv + 53) != (altitude != voltage_mv + 53):
        triggered.add(118)
    # 变异规则 173 - CAR
    if (speed != voltage_mv + 53) != (speed != voltage_mv + 43):
        triggered.add(119)
    # 变异规则 174 - SCR
    if (speed != voltage_mv + 53) != (voltage_mv != voltage_mv + 53):
        triggered.add(120)
    # 变异规则 175 - AOR
    if (speed != voltage_mv + 53) != (voltage_mv != speed + 53):
        triggered.add(121)
    # 变异规则 176 - LCR
    if (speed != voltage_mv + 53) != (speed != voltage_mv + 26):
        triggered.add(122)
    # 变异规则 177 - SAR
    if (speed != voltage_mv + 53) != (voltage_mv != speed + 53):
        triggered.add(123)
    # 变异规则 178 - ABS
    if (speed != voltage_mv + 53) != (abs(speed) != voltage_mv + 53):
        t=1
    # 变异规则 179 - CRP
    if (speed != voltage_mv + 53) != (speed != voltage_mv + 106):
        triggered.add(124)
    # 变异规则 180 - SRC
    if (speed != voltage_mv + 53) != (voltage_mv != voltage_mv + 53):
        triggered.add(125)
    # 原语句
    if speed != voltage_mv + 53:
        health_score -= 30
        speed = min(speed + 4, 100)
    # 原语句19
    # 变异规则 181 - SVR
    if (altitude != 30 or altitude != 100) != (speed != 30 or altitude != 100):
        triggered.add(126)
    # 变异规则 182 - CAR
    if (altitude != 30 or altitude != 100) != (altitude != 25 or altitude != 100):
        t=1
    # 变异规则 183 - AOR
    if (altitude != 30 or altitude != 100) != (altitude != 30 or altitude != 110):
        t=1
    # 变异规则 184 - SCR
    if (altitude != 30 or altitude != 100) != (30 != altitude or altitude != 100):
        t=1
    # 变异规则 185 - ROR
    if (altitude != 30 or altitude != 100) != (altitude != -30 or altitude != 100):
        t=1
    # 变异规则 186 - CRP
    if (altitude != 30 or altitude != 100) != (altitude != 30 or altitude != 110):
        t=1
    # 变异规则 187 - LCR
    if (altitude != 30 or altitude != 100) != (altitude != 30 and altitude != 100):
        triggered.add(127)
    # 变异规则 188 - SAR
    if (altitude != 30 or altitude != 100) != (30 != altitude or altitude != 100):
        t=1
    # 变异规则 189 - ABS
    if (altitude != 30 or altitude != 100) != (abs(altitude) != 30 or altitude != 100):
        t=1
    # 变异规则 190 - SRC
    if (altitude != 30 or altitude != 100) != (altitude != 100 or altitude != 30):
        t=1
    # 原语句
    if altitude != 30 or altitude != 100:
        health_score -= 20
    # 原语句20
    # 变异规则 191 - SAR
    if (voltage_mv < 5 and altitude == 424) != (5 > voltage_mv and altitude == 424):
        t=1
    # 变异规则 192 - ROR
    if (voltage_mv < 5 and altitude == 424) != (voltage_mv < -5 and altitude == 424):
        t=1
    # 变异规则 193 - SCR
    if (voltage_mv < 5 and altitude == 424) != (5 > voltage_mv and altitude == 424):
        t=1
    # 变异规则 194 - ABS
    if (voltage_mv < 5 and altitude == 424) != (voltage_mv < 5 and abs(altitude) == 424):
        t=1
    # 变异规则 195 - SVR
    if (voltage_mv < 5 and altitude == 424) != (speed < 5 and altitude == 424):
        t=1
    # 变异规则 196 - CAR
    if (voltage_mv < 5 and altitude == 424) != (voltage_mv < 5 and altitude == 426):
        t=1
    # 变异规则 197 - SRC
    if (voltage_mv < 5 and altitude == 424) != (altitude == 424 and voltage_mv < 5):
        t=1
    # 变异规则 198 - LCR
    if (voltage_mv < 5 and altitude == 424) != (voltage_mv < 5 or altitude == 424):
        triggered.add(128)
    # 变异规则 199 - CSR
    if (voltage_mv < 5 and altitude == 424) != (voltage_mv < 5 and altitude == -424):
        t=1
    # 变异规则 200 - RSR
    if (voltage_mv < 5 and altitude == 424) != (not (voltage_mv < 5 and altitude == 424)):
        triggered.add(129)
    # 原语句
    if voltage_mv < 5 and altitude == 424:
        health_score += 4
    # 原语句21
    # 变异规则 201 - SVR
    if (6 <= speed <= 86) != (6 <= voltage_mv <= 86):
        triggered.add(130)
    # 变异规则 202 - CRP
    if (6 <= speed <= 86) != (6 <= speed <= 43):
        triggered.add(131)
    # 变异规则 203 - UOI
    if (6 <= speed <= 86) != (6 <= -speed <= 86):
        triggered.add(132)
    # 变异规则 204 - ABS
    if (6 <= speed <= 86) != (6 <= abs(speed) <= 86):
        t=1
    # 变异规则 205 - AOR
    if (6 <= speed <= 86) != (6 <= speed <= 81):
        triggered.add(133)
    # 变异规则 206 - SRC
    if (6 <= speed <= 86) != (speed >= 6 <= 86):
        triggered.add(134)
    # 变异规则 207 - LCR
    if (6 <= speed <= 86) != (6 <= speed <= 172):
        triggered.add(135)
    # 变异规则 208 - SCR
    if (6 <= speed <= 86) != (6 <= abs(speed) <= 86):
        t=1
    # 变异规则 209 - CAR
    if (6 <= speed <= 86) != (6 <= speed <= 96):
        triggered.add(136)
    # 变异规则 210 - SAR
    if (6 <= speed <= 86) != (speed >= 6 <= 86):
        triggered.add(137)
    # 原语句
    if 6 <= speed <= 86:
        health_score -= 12
        altitude = min(altitude + 46, 1000)
        speed = max(speed - 6, 2)
    # 原语句22
    # 变异规则 211 - ABS
    if (2 <= speed <= 63) != (2 <= abs(speed) <= 63):
        t=1
    # 变异规则 212 - UOI
    if (2 <= speed <= 63) != (2 <= -speed <= 63):
        triggered.add(138)
    # 变异规则 213 - AOR
    if (2 <= speed <= 63) != (-2 <= speed <= 63):
        t=1
    # 变异规则 214 - ROR
    if (2 <= speed <= 63) != (not (2 <= speed <= 63)):
        triggered.add(139)
    # 变异规则 215 - RSR
    if (2 <= speed <= 63) != (not (2 <= speed <= 63)):
        triggered.add(140)
    # 变异规则 216 - LCR
    if (2 <= speed <= 63) != (2 <= abs(speed) <= 63):
        t=1
    # 变异规则 217 - SRC
    if (2 <= speed <= 63) != (2 <= altitude <= 63):
        triggered.add(141)
    # 变异规则 218 - CRP
    if (2 <= speed <= 63) != (4 <= speed <= 63):
        t=1
    # 变异规则 219 - SVR
    if (2 <= speed <= 63) != (2 <= voltage_mv <= 63):
        triggered.add(142)
    # 变异规则 220 - CAR
    if (2 <= speed <= 63) != (2 <= speed <= 73):
        triggered.add(143)
    # 原语句
    if 2 <= speed <= 63:
        health_score -= 26
        altitude = min(altitude + 28, 1000)
        speed = min(speed + 9, 100)
    # 原语句23
    # 变异规则 221 - LCR
    if (voltage_mv < 5) != (abs(voltage_mv) < 5):
        t=1
    # 变异规则 222 - RSR
    if (voltage_mv < 5) != (not (voltage_mv < 5)):
        triggered.add(144)
    # 变异规则 223 - AOR
    if (voltage_mv < 5) != (speed < 5):
        t=1
    # 变异规则 224 - SAR
    if (voltage_mv < 5) != (5 > voltage_mv):
        t=1
    # 变异规则 225 - UOI
    if (voltage_mv < 5) != (voltage_mv < 7):
        triggered.add(145)
    # 变异规则 226 - ABS
    if (voltage_mv < 5) != (abs(voltage_mv) < 5):
        t=1
    # 变异规则 227 - CSR
    if (voltage_mv < 5) != (voltage_mv < -5):
        t=1
    # 变异规则 228 - SVR
    if (voltage_mv < 5) != (speed < 5):
        t=1
    # 变异规则 229 - CRP
    if (voltage_mv < 5) != (voltage_mv < 11):
        triggered.add(146)
    # 变异规则 230 - SCR
    if (voltage_mv < 5) != (voltage_mv < 2):
        t=1
    # 原语句
    if voltage_mv < 5:
        health_score -= 29
        altitude = max(altitude - 37, 2)
    # 原语句24
    # 变异规则 231 - SCR
    if (altitude != 5 and altitude < 5) != (altitude < 5 and altitude != 5):
        t=1
    # 变异规则 232 - CRP
    if (altitude != 5 and altitude < 5) != (altitude != 5 and altitude < 13):
        triggered.add(147)
    # 变异规则 233 - AOR
    if (altitude != 5 and altitude < 5) != (altitude != 5 and -altitude < 5):
        triggered.add(148)
    # 变异规则 234 - SAR
    if (altitude != 5 and altitude < 5) != (altitude != 5 and 5 > altitude):
        t=1
    # 变异规则 235 - RSR
    if (altitude != 5 and altitude < 5) != (not (altitude != 5 and altitude < 5)):
        triggered.add(149)
    # 变异规则 236 - LCR
    if (altitude != 5 and altitude < 5) != (altitude != 5 or altitude < 5):
        triggered.add(150)
    # 变异规则 237 - SVR
    if (altitude != 5 and altitude < 5) != (voltage_mv != 5 and altitude < 5):
        t=1
    # 变异规则 238 - CSR
    if (altitude != 5 and altitude < 5) != (altitude != 5 and altitude < -5):
        t=1
    # 变异规则 239 - ABS
    if (altitude != 5 and altitude < 5) != (abs(altitude) != 5 and altitude < 5):
        t=1
    # 变异规则 240 - ROR
    if (altitude != 5 and altitude < 5) != (altitude != 5 and -altitude < 5):
        triggered.add(151)
    # 原语句
    if altitude != 5 and altitude < 5:
        health_score += 4
        speed = min(speed + 8, 100)
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句25
    # 变异规则 241 - SAR
    if (altitude > 2) != (2 < altitude):
        t=1
    # 变异规则 242 - SCR
    if (altitude > 2) != (altitude > -2):
        t=1
    # 变异规则 243 - CRP
    if (altitude > 2) != (altitude > 1):
        t=1
    # 变异规则 244 - UOI
    if (altitude > 2) != (altitude > 4):
        t=1
    # 变异规则 245 - CAR
    if (altitude > 2) != (altitude > 4):
        t=1
    # 变异规则 246 - ROR
    if (altitude > 2) != (altitude > -2):
        t=1
    # 变异规则 247 - LCR
    if (altitude > 2) != (altitude > 7):
        triggered.add(152)
    # 变异规则 248 - ABS
    if (altitude > 2) != (abs(altitude) > 2):
        t=1
    # 变异规则 249 - RSR
    if (altitude > 2) != (not (altitude > 2)):
        triggered.add(153)
    # 变异规则 250 - AOR
    if (altitude > 2) != (altitude > -2):
        t=1
    # 原语句
    if altitude > 2:
        health_score += 18
        speed = max(speed - 10, 2)
    # 原语句26
    # 变异规则 251 - SCR
    if (speed >= 10 and altitude <= 271) != (not (speed >= 10 and altitude <= 271)):
        triggered.add(154)
    # 变异规则 252 - ABS
    if (speed >= 10 and altitude <= 271) != (speed >= 10 and abs(altitude) <= 271):
        t=1
    # 变异规则 253 - UOI
    if (speed >= 10 and altitude <= 271) != (speed >= 10 and -altitude <= 271):
        triggered.add(155)
    # 变异规则 254 - SRC
    if (speed >= 10 and altitude <= 271) != (altitude <= 271 and speed >= 10):
        t=1
    # 变异规则 255 - SAR
    if (speed >= 10 and altitude <= 271) != (speed >= 10 and 271 >= altitude):
        t=1
    # 变异规则 256 - CRP
    if (speed >= 10 and altitude <= 271) != (speed >= 10 and altitude <= 276):
        triggered.add(156)
    # 变异规则 257 - SVR
    if (speed >= 10 and altitude <= 271) != (altitude >= 10 and altitude <= 271):
        triggered.add(157)
    # 变异规则 258 - CSR
    if (speed >= 10 and altitude <= 271) != (speed >= 10 and altitude <= -271):
        triggered.add(158)
    # 变异规则 259 - AOR
    if (speed >= 10 and altitude <= 271) != (voltage_mv >= 10 and altitude <= 271):
        triggered.add(159)
    # 变异规则 260 - LCR
    if (speed >= 10 and altitude <= 271) != (speed >= 10 or altitude <= 271):
        triggered.add(160)
    # 原语句
    if speed >= 10 and altitude <= 271:
        health_score += 3
    # 原语句27
    # 变异规则 261 - UOI
    if (speed <= 30 or altitude < 824) != (speed <= 30 or -altitude < 824):
        triggered.add(161)
    # 变异规则 262 - ABS
    if (speed <= 30 or altitude < 824) != (speed <= 30 or abs(altitude) < 824):
        t=1
    # 变异规则 263 - AOR
    if (speed <= 30 or altitude < 824) != (speed <= 30 or abs(altitude) < 824):
        t=1
    # 变异规则 264 - ROR
    if (speed <= 30 or altitude < 824) != (speed <= 30 or 824 > altitude):
        t=1
    # 变异规则 265 - CRP
    if (speed <= 30 or altitude < 824) != (speed <= 30 or altitude < 819):
        triggered.add(162)
    # 变异规则 266 - LCR
    if (speed <= 30 or altitude < 824) != (speed <= 30 and altitude < 824):
        triggered.add(163)
    # 变异规则 267 - CSR
    if (speed <= 30 or altitude < 824) != (speed <= 30 or altitude < -824):
        triggered.add(164)
    # 变异规则 268 - SCR
    if (speed <= 30 or altitude < 824) != (speed <= 30 or abs(altitude) < 824):
        t=1
    # 变异规则 269 - SAR
    if (speed <= 30 or altitude < 824) != (speed <= 30 or 824 > altitude):
        t=1
    # 变异规则 270 - CAR
    if (speed <= 30 or altitude < 824) != (speed <= 30 or altitude < 834):
        triggered.add(165)
    # 原语句
    if speed <= 30 or altitude < 824:
        health_score += 12
    # 原语句28
    # 变异规则 271 - SCR
    if (voltage_mv <= 5) != (altitude <= 5):
        triggered.add(166)
    # 变异规则 272 - UOI
    if (voltage_mv <= 5) != (altitude <= 5):
        triggered.add(167)
    # 变异规则 273 - CAR
    if (voltage_mv <= 5) != (voltage_mv <= 1):
        triggered.add(168)
    # 变异规则 274 - AOR
    if (voltage_mv <= 5) != (voltage_mv <= 10):
        triggered.add(169)
    # 变异规则 275 - LCR
    if (voltage_mv <= 5) != (voltage_mv <= 4):
        triggered.add(170)
    # 变异规则 276 - CRP
    if (voltage_mv <= 5) != (voltage_mv <= 1):
        triggered.add(171)
    # 变异规则 277 - SAR
    if (voltage_mv <= 5) != (5 >= voltage_mv):
        t=1
    # 变异规则 278 - SVR
    if (voltage_mv <= 5) != (speed <= 5):
        triggered.add(172)
    # 变异规则 279 - ABS
    if (voltage_mv <= 5) != (abs(voltage_mv) <= 5):
        t=1
    # 变异规则 280 - ROR
    if (voltage_mv <= 5) != (5 >= voltage_mv):
        t=1
    # 原语句
    if voltage_mv <= 5:
        health_score += 14
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句29
    # 变异规则 281 - SCR
    if (altitude >= 200) != (altitude >= -200):
        triggered.add(173)
    # 变异规则 282 - CSR
    if (altitude >= 200) != (altitude >= -200):
        triggered.add(174)
    # 变异规则 283 - UOI
    if (altitude >= 200) != (abs(altitude) >= 200):
        t=1
    # 变异规则 284 - SVR
    if (altitude >= 200) != (voltage_mv >= 200):
        triggered.add(175)
    # 变异规则 285 - AOR
    if (altitude >= 200) != (not (altitude >= 200)):
        triggered.add(176)
    # 变异规则 286 - ABS
    if (altitude >= 200) != (abs(altitude) >= 200):
        t=1
    # 变异规则 287 - CAR
    if (altitude >= 200) != (altitude >= 199):
        triggered.add(177)
    # 变异规则 288 - RSR
    if (altitude >= 200) != (not (altitude >= 200)):
        triggered.add(178)
    # 变异规则 289 - SRC
    if (altitude >= 200) != (200 <= altitude):
        t=1
    # 变异规则 290 - CRP
    if (altitude >= 200) != (altitude >= 198):
        triggered.add(179)
    # 原语句
    if altitude >= 200:
        health_score -= 28
        speed = min(speed + 10, 100)
        voltage_mv = min(voltage_mv + 10, 100)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句30
    # 变异规则 291 - CRP
    if (altitude != 839) != (altitude != 842):
        t=1
    # 变异规则 292 - RSR
    if (altitude != 839) != (not (altitude != 839)):
        triggered.add(180)
    # 变异规则 293 - SVR
    if (altitude != 839) != (voltage_mv != 839):
        triggered.add(181)
    # 变异规则 294 - SAR
    if (altitude != 839) != (839 != altitude):
        t=1
    # 变异规则 295 - ROR
    if (altitude != 839) != (not (altitude != 839)):
        triggered.add(182)
    # 变异规则 296 - LCR
    if (altitude != 839) != (not (altitude != 839)):
        triggered.add(183)
    # 变异规则 297 - CSR
    if (altitude != 839) != (altitude != -839):
        t=1
    # 变异规则 298 - CAR
    if (altitude != 839) != (altitude != 840):
        t=1
    # 变异规则 299 - ABS
    if (altitude != 839) != (abs(altitude) != 839):
        t=1
    # 变异规则 300 - SRC
    if (altitude != 839) != (speed != 839):
        t=1
    # 原语句
    if altitude != 839:
        health_score -= 3
        altitude = max(altitude - 50, 2)
    return triggered

targetPaths = [
    {3, 4, 5, 10, 11, 16, 20, 32, 33, 35, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 157, 160, 169, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 20, 32, 33, 35, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 169, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 20, 31, 32, 33, 35, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 169, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 169, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 107, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 169, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 107, 109, 112, 122, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 102, 103, 107, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 89, 91, 97, 98, 99, 103, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 169, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 89, 91, 97, 98, 99, 103, 107, 109, 112, 129, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 169, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 89, 91, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 180},
    {1, 2, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 89, 91, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 89, 91, 97, 98, 99, 103, 107, 109, 112, 119, 129, 131, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 92, 93, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 36, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 93, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 93, 97, 98, 99, 103, 107, 109, 112, 117, 129, 131, 132, 139, 141, 142, 143, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 93, 97, 98, 99, 103, 107, 109, 112, 117, 118, 119, 120, 121, 122, 124, 129, 131, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 36, 38, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 93, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 139, 141, 142, 143, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 36, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 93, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 133, 139, 141, 142, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 36, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 88, 91, 93, 97, 98, 99, 103, 107, 109, 112, 129, 130, 134, 135, 136, 139, 141, 142, 144, 149, 152, 153, 154, 157, 158, 163, 164, 166, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 92, 93, 97, 98, 99, 103, 107, 109, 112, 114, 129, 131, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 20, 30, 33, 34, 40, 42, 50, 56, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 114, 129, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 19, 20, 21, 22, 32, 33, 35, 40, 42, 50, 56, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 114, 129, 132, 138, 139, 144, 148, 149, 150, 153, 154, 157, 159, 160, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 19, 20, 21, 22, 30, 33, 34, 40, 42, 50, 52, 56, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 114, 129, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 19, 20, 21, 22, 30, 33, 40, 42, 50, 52, 56, 59, 64, 67, 71, 74, 75, 78, 84, 88, 91, 92, 93, 97, 98, 103, 104, 107, 109, 112, 113, 115, 116, 129, 131, 132, 139, 141, 142, 143, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 19, 20, 21, 22, 30, 33, 34, 40, 42, 50, 51, 52, 56, 59, 64, 67, 71, 74, 75, 78, 89, 91, 96, 98, 103, 109, 112, 114, 129, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 19, 20, 21, 22, 30, 33, 34, 40, 42, 50, 51, 52, 56, 57, 61, 62, 64, 67, 71, 74, 75, 78, 89, 91, 97, 98, 99, 103, 109, 112, 114, 129, 132, 138, 139, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 19, 20, 21, 22, 30, 33, 34, 40, 42, 50, 51, 52, 56, 57, 61, 62, 64, 67, 71, 74, 75, 78, 79, 81, 84, 86, 89, 91, 97, 98, 99, 103, 106, 107, 109, 112, 129, 130, 132, 138, 139, 141, 144, 145, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 166, 168, 170, 172, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 19, 20, 21, 22, 30, 33, 34, 40, 42, 50, 51, 52, 56, 57, 61, 62, 64, 67, 71, 74, 75, 78, 79, 81, 84, 86, 89, 91, 98, 99, 103, 106, 107, 109, 112, 127, 129, 130, 132, 138, 139, 141, 144, 145, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 166, 168, 170, 172, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 19, 20, 21, 22, 30, 33, 40, 42, 50, 51, 52, 56, 57, 61, 62, 64, 67, 71, 76, 79, 84, 86, 89, 91, 98, 103, 109, 112, 113, 115, 129, 132, 138, 139, 141, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {3, 4, 5, 6, 10, 11, 16, 19, 20, 21, 22, 30, 33, 40, 42, 50, 51, 52, 56, 57, 61, 62, 64, 67, 70, 71, 76, 79, 84, 86, 89, 91, 98, 103, 109, 112, 113, 115, 129, 132, 138, 139, 141, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 19, 20, 21, 22, 30, 33, 36, 40, 42, 50, 51, 52, 56, 57, 61, 62, 64, 67, 70, 71, 76, 79, 84, 85, 86, 89, 91, 98, 103, 109, 112, 113, 115, 129, 132, 138, 139, 141, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 19, 20, 21, 22, 30, 33, 36, 40, 42, 50, 51, 52, 56, 57, 61, 62, 64, 67, 70, 71, 76, 80, 81, 83, 91, 98, 103, 107, 109, 112, 113, 115, 129, 130, 132, 138, 139, 141, 142, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 4, 5, 10, 11, 16, 19, 20, 21, 22, 30, 33, 34, 40, 42, 50, 53, 54, 55, 59, 64, 67, 71, 74, 75, 78, 79, 81, 84, 86, 89, 91, 96, 98, 103, 106, 107, 109, 112, 129, 130, 132, 138, 139, 141, 144, 145, 146, 148, 149, 150, 153, 154, 158, 159, 166, 168, 170, 172, 173, 176, 180},
    {3, 5, 10, 11, 16, 19, 20, 21, 22, 26, 32, 33, 35, 40, 42, 50, 55, 59, 64, 67, 70, 71, 76, 79, 84, 86, 89, 91, 96, 97, 98, 99, 103, 107, 109, 112, 113, 115, 129, 132, 138, 139, 141, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 5, 10, 11, 16, 20, 23, 24, 25, 32, 33, 35, 40, 42, 50, 55, 59, 64, 67, 70, 71, 76, 79, 84, 86, 89, 91, 96, 97, 98, 99, 103, 107, 109, 112, 113, 115, 129, 132, 138, 139, 141, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 5, 10, 11, 16, 20, 25, 30, 33, 34, 39, 40, 46, 50, 55, 59, 64, 67, 71, 76, 80, 81, 91, 96, 97, 98, 99, 103, 107, 109, 112, 113, 115, 129, 130, 132, 138, 139, 141, 142, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 5, 10, 11, 16, 20, 25, 30, 33, 34, 39, 40, 50, 55, 59, 64, 67, 70, 71, 73, 76, 80, 81, 91, 96, 97, 98, 99, 103, 107, 109, 112, 113, 115, 129, 130, 132, 138, 139, 141, 142, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {3, 5, 10, 11, 16, 20, 25, 30, 33, 34, 39, 40, 50, 55, 59, 64, 67, 71, 72, 74, 75, 77, 78, 80, 91, 96, 98, 99, 103, 104, 109, 112, 113, 115, 129, 130, 132, 138, 139, 142, 144, 148, 149, 150, 153, 154, 158, 173, 176, 180},
    {2, 3, 5, 7, 10, 11, 16, 20, 30, 33, 36, 40, 42, 50, 59, 64, 67, 71, 74, 75, 78, 88, 91, 93, 97, 98, 99, 103, 107, 109, 112, 129, 130, 134, 135, 136, 139, 141, 142, 144, 147, 148, 149, 150, 152, 153, 154, 157, 158, 163, 164, 173, 176, 180},
    {1, 2, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 49, 50, 59, 64, 67, 71, 74, 75, 78, 84, 89, 91, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 180},
    {1, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 48, 50, 59, 64, 67, 71, 74, 75, 78, 84, 89, 91, 97, 98, 99, 103, 107, 109, 112, 129, 131, 132, 138, 139, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 180},
    {1, 2, 5, 7, 10, 11, 16, 19, 20, 21, 22, 30, 33, 40, 42, 50, 51, 52, 56, 58, 59, 64, 67, 71, 74, 75, 78, 84, 89, 91, 97, 98, 103, 107, 109, 112, 114, 129, 131, 132, 139, 141, 142, 143, 144, 148, 149, 150, 153, 154, 158, 163, 164, 173, 176, 180},
    {2, 3, 4, 5, 10, 11, 12, 20, 32, 33, 35, 40, 42, 50, 55, 64, 67, 71, 74, 75, 81, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 157, 160, 169, 173, 176, 180},
    {2, 3, 4, 5, 10, 11, 12, 18, 20, 32, 33, 35, 40, 42, 50, 55, 64, 67, 71, 74, 75, 81, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 157, 160, 169, 173, 176, 180},
    {2, 3, 4, 5, 10, 11, 16, 20, 32, 33, 35, 40, 42, 50, 55, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 126, 127, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 158, 159, 169, 173, 176, 180},
    {1, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 55, 64, 67, 71, 74, 75, 84, 89, 91, 93, 98, 99, 103, 104, 109, 112, 129, 131, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 179, 180},
    {1, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 55, 64, 67, 71, 74, 75, 84, 89, 91, 93, 98, 99, 103, 104, 109, 112, 129, 131, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 173, 176, 177, 179, 180},
    {1, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 55, 64, 67, 71, 74, 75, 84, 89, 91, 93, 98, 99, 103, 104, 109, 112, 129, 131, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 158, 159, 163, 164, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 40, 42, 50, 55, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 155, 160, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 40, 42, 44, 50, 55, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 169, 175, 176, 180},
    {1, 5, 7, 10, 11, 16, 20, 30, 33, 40, 42, 50, 55, 64, 67, 71, 74, 75, 84, 89, 91, 93, 98, 99, 103, 104, 109, 112, 129, 131, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 155, 156, 160, 163, 164, 169, 175, 176, 180},
    {1, 5, 7, 10, 11, 16, 20, 29, 33, 35, 40, 42, 50, 55, 64, 67, 71, 74, 75, 84, 89, 91, 93, 98, 99, 103, 104, 109, 112, 129, 131, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 155, 160, 163, 164, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 40, 42, 43, 44, 50, 55, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 40, 42, 43, 44, 45, 50, 55, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 39, 40, 47, 50, 55, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 128, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 39, 40, 47, 50, 55, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 163, 169, 175, 176, 180, 181},
    {1, 5, 7, 10, 11, 16, 20, 33, 35, 39, 40, 47, 50, 55, 64, 67, 71, 74, 75, 84, 89, 91, 93, 98, 99, 103, 104, 109, 112, 129, 131, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 155, 160, 162, 163, 164, 169, 175, 176, 180},
    {1, 5, 7, 10, 11, 16, 20, 33, 35, 39, 40, 47, 50, 55, 64, 67, 71, 74, 75, 84, 89, 91, 93, 98, 99, 103, 104, 109, 112, 129, 131, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 155, 160, 161, 165, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 39, 40, 47, 50, 55, 63, 64, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 163, 169, 175, 176, 180},
    {2, 3, 4, 5, 11, 16, 20, 33, 39, 40, 47, 50, 55, 65, 67, 71, 74, 75, 89, 91, 93, 96, 97, 98, 103, 104, 107, 109, 112, 129, 132, 138, 139, 141, 144, 146, 148, 149, 150, 153, 154, 163, 169, 175, 176, 180}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 3:3, 4:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 12:11, 14:12, 15:13, 16:14, 17:15, 18:16, 19:17, 20:18, 21:19, 22:20, 23:21, 24:22, 25:23, 26:24, 27:25, 28:26, 29:27, 30:28, 32:29, 33:30, 34:31, 36:32, 37:33, 39:34, 40:35, 45:36, 47:37, 50:38, 51:39, 52:40, 53:41, 54:42, 55:43, 56:44, 57:45, 58:46, 60:47, 61:48, 66:49, 68:50, 71:51, 73:52, 74:53, 75:54, 77:55, 80:56, 81:57, 83:58, 86:59, 87:60, 89:61, 90:62, 92:63, 93:64, 94:65, 95:66, 96:67, 97:68, 100:69, 102:70, 103:71, 104:72, 105:73, 106:74, 107:75, 108:76, 109:77, 110:78, 111:79, 113:80, 114:81, 115:82, 116:83, 117:84, 118:85, 119:86, 120:87, 121:88, 122:89, 123:90, 124:91, 126:92, 127:93, 128:94, 130:95, 132:96, 134:97, 135:98, 137:99, 138:100, 139:101, 140:102, 142:103, 144:104, 145:105, 146:106, 148:107, 149:108, 157:109, 158:110, 159:111, 163:112, 164:113, 167:114, 169:115, 170:116, 171:117, 172:118, 173:119, 174:120, 175:121, 176:122, 177:123, 179:124, 180:125, 181:126, 187:127, 198:128, 200:129, 201:130, 202:131, 203:132, 205:133, 206:134, 207:135, 209:136, 210:137, 212:138, 214:139, 215:140, 217:141, 219:142, 220:143, 222:144, 225:145, 229:146, 232:147, 233:148, 235:149, 236:150, 240:151, 247:152, 249:153, 251:154, 253:155, 256:156, 257:157, 258:158, 259:159, 260:160, 261:161, 265:162, 266:163, 267:164, 270:165, 271:166, 272:167, 273:168, 274:169, 275:170, 276:171, 278:172, 281:173, 282:174, 284:175, 285:176, 287:177, 288:178, 290:179, 292:180, 293:181, 295:182, 296:183}

    rule_expressions[1] = "(voltage_mv - speed < 50) != (voltage_mv - speed < 51)"
    rule_expressions[2] = "(voltage_mv - speed < 50) != (altitude - speed < 50)"
    rule_expressions[3] = "(voltage_mv - speed < 50) != (voltage_mv - 50 > speed)"
    rule_expressions[4] = "(voltage_mv - speed < 50) != (voltage_mv - speed < -50)"
    rule_expressions[5] = "(voltage_mv - speed < 50) != (not (voltage_mv - speed < 50))"
    rule_expressions[6] = "(voltage_mv - speed < 50) != (voltage_mv - speed < 25)"
    rule_expressions[7] = "(voltage_mv - speed < 50) != (speed - speed < 50)"
    rule_expressions[8] = "(voltage_mv - speed < 50) != (not (voltage_mv - speed < 50))"
    rule_expressions[9] = "(voltage_mv - speed < 50) != (not (voltage_mv - speed < 50))"
    rule_expressions[10] = "(altitude // 50 <= voltage_mv) != (altitude // 50 <= -voltage_mv)"
    rule_expressions[11] = "(altitude // 50 <= voltage_mv) != (not (altitude // 50 <= voltage_mv))"
    rule_expressions[12] = "(altitude // 50 <= voltage_mv) != (altitude // 40 <= voltage_mv)"
    rule_expressions[13] = "(altitude // 50 <= voltage_mv) != (not (altitude // 50 <= voltage_mv))"
    rule_expressions[14] = "(altitude // 50 <= voltage_mv) != (altitude // 50 <= -voltage_mv)"
    rule_expressions[15] = "(altitude // 50 <= voltage_mv) != (altitude // 50 <= -voltage_mv)"
    rule_expressions[16] = "(altitude // 50 <= voltage_mv) != (altitude // voltage_mv >= 50)"
    rule_expressions[17] = "(altitude // 50 <= voltage_mv) != (altitude // voltage_mv >= 50)"
    rule_expressions[18] = "(altitude // 50 <= voltage_mv) != (altitude // 44 <= voltage_mv)"
    rule_expressions[19] = "(16 <= speed <= 72) != (16 <= speed <= -72)"
    rule_expressions[20] = "(16 <= speed <= 72) != (not (16 <= speed <= 72))"
    rule_expressions[21] = "(16 <= speed <= 72) != (16 <= altitude <= 72)"
    rule_expressions[22] = "(16 <= speed <= 72) != (16 <= -speed <= 72)"
    rule_expressions[23] = "(16 <= speed <= 72) != (16 <= speed <= 75)"
    rule_expressions[24] = "(16 <= speed <= 72) != (16 <= speed <= 77)"
    rule_expressions[25] = "(16 <= speed <= 72) != (speed >= 16 <= 72)"
    rule_expressions[26] = "(16 <= speed <= 72) != (16 <= speed <= 67)"
    rule_expressions[27] = "(16 <= speed <= 72) != (16 <= -speed <= 72)"
    rule_expressions[28] = "(16 <= speed <= 72) != (16 <= speed <= -72)"
    rule_expressions[29] = "(altitude >= 200 or voltage_mv < 20) != (altitude >= 208 or voltage_mv < 20)"
    rule_expressions[30] = "(altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or -voltage_mv < 20)"
    rule_expressions[31] = "(altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or voltage_mv < 18)"
    rule_expressions[32] = "(altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or voltage_mv < -20)"
    rule_expressions[33] = "(altitude >= 200 or voltage_mv < 20) != (not (altitude >= 200 or voltage_mv < 20))"
    rule_expressions[34] = "(altitude >= 200 or voltage_mv < 20) != (altitude >= 200 or voltage_mv < 40)"
    rule_expressions[35] = "(altitude >= 200 or voltage_mv < 20) != (altitude >= 200 and voltage_mv < 20)"
    rule_expressions[36] = "(voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 and voltage_mv != 69)"
    rule_expressions[37] = "(voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 and voltage_mv != 69)"
    rule_expressions[38] = "(voltage_mv <= 73 or voltage_mv != 69) != (voltage_mv <= 73 or voltage_mv != 74)"
    rule_expressions[39] = "(altitude <= 420 and speed < 95) != (altitude <= 420 or speed < 95)"
    rule_expressions[40] = "(altitude <= 420 and speed < 95) != (not (altitude <= 420 and speed < 95))"
    rule_expressions[41] = "(altitude <= 420 and speed < 95) != (altitude <= 420 or speed < 95)"
    rule_expressions[42] = "(altitude <= 420 and speed < 95) != (altitude <= -420 and speed < 95)"
    rule_expressions[43] = "(altitude <= 420 and speed < 95) != (altitude <= 410 and speed < 95)"
    rule_expressions[44] = "(altitude <= 420 and speed < 95) != (altitude <= 210 and speed < 95)"
    rule_expressions[45] = "(altitude <= 420 and speed < 95) != (altitude <= 415 and speed < 95)"
    rule_expressions[46] = "(altitude <= 420 and speed < 95) != (altitude <= 420 and speed < 97)"
    rule_expressions[47] = "(altitude <= 420 and speed < 95) != (voltage_mv <= 420 and speed < 95)"
    rule_expressions[48] = "(altitude != 5 and altitude != 5) != (altitude != 6 and altitude != 5)"
    rule_expressions[49] = "(altitude != 5 and altitude != 5) != (altitude != 4 and altitude != 5)"
    rule_expressions[50] = "(altitude != 5 and altitude != 5) != (not (altitude != 5 and altitude != 5))"
    rule_expressions[51] = "(speed > 34) != (speed > 27)"
    rule_expressions[52] = "(speed > 34) != (speed > 24)"
    rule_expressions[53] = "(speed > 34) != (speed > 68)"
    rule_expressions[54] = "(speed > 34) != (speed > 35)"
    rule_expressions[55] = "(speed > 34) != (altitude > 34)"
    rule_expressions[56] = "(speed > 34) != (speed > 17)"
    rule_expressions[57] = "(speed != 30 or altitude > 10) != (speed != -30 or altitude > 10)"
    rule_expressions[58] = "(speed != 30 or altitude > 10) != (speed != 30 or -altitude > 10)"
    rule_expressions[59] = "(speed != 30 or altitude > 10) != (speed != 30 and altitude > 10)"
    rule_expressions[60] = "(speed != 30 or altitude > 10) != (speed != 30 or -altitude > 10)"
    rule_expressions[61] = "(speed != 30 or altitude > 10) != (altitude != 30 or altitude > 10)"
    rule_expressions[62] = "(speed != 30 or altitude > 10) != (speed != 32 or altitude > 10)"
    rule_expressions[63] = "(altitude <= 863) != (altitude <= 862)"
    rule_expressions[64] = "(altitude <= 863) != (altitude <= -863)"
    rule_expressions[65] = "(altitude <= 863) != (altitude <= 873)"
    rule_expressions[66] = "(altitude <= 863) != (altitude <= -863)"
    rule_expressions[67] = "(altitude <= 863) != (not (altitude <= 863))"
    rule_expressions[68] = "(altitude <= 863) != (altitude <= -863)"
    rule_expressions[69] = "(altitude <= 863) != (not (altitude <= 863))"
    rule_expressions[70] = "(voltage_mv % 99 < altitude) != (voltage_mv % 49 < altitude)"
    rule_expressions[71] = "(voltage_mv % 99 < altitude) != (not (voltage_mv % 99 < altitude))"
    rule_expressions[72] = "(voltage_mv % 99 < altitude) != (voltage_mv % 100 < altitude)"
    rule_expressions[73] = "(voltage_mv % 99 < altitude) != (voltage_mv % 98 < altitude)"
    rule_expressions[74] = "(voltage_mv % 99 < altitude) != (voltage_mv % altitude > 99)"
    rule_expressions[75] = "(voltage_mv % 99 < altitude) != (voltage_mv % 99 < -altitude)"
    rule_expressions[76] = "(voltage_mv % 99 < altitude) != (voltage_mv % -99 < altitude)"
    rule_expressions[77] = "(voltage_mv % 99 < altitude) != (voltage_mv % 101 < altitude)"
    rule_expressions[78] = "(voltage_mv % 99 < altitude) != (altitude % 99 < altitude)"
    rule_expressions[79] = "(31 <= voltage_mv <= 90) != (31 <= -voltage_mv <= 90)"
    rule_expressions[80] = "(31 <= voltage_mv <= 90) != (voltage_mv >= 31 <= 90)"
    rule_expressions[81] = "(31 <= voltage_mv <= 90) != (31 <= altitude <= 90)"
    rule_expressions[82] = "(31 <= voltage_mv <= 90) != (voltage_mv >= 31 <= 90)"
    rule_expressions[83] = "(31 <= voltage_mv <= 90) != (31 <= voltage_mv <= 91)"
    rule_expressions[84] = "(31 <= voltage_mv <= 90) != (31 <= speed <= 90)"
    rule_expressions[85] = "(31 <= voltage_mv <= 90) != (31 <= voltage_mv <= 83)"
    rule_expressions[86] = "(31 <= voltage_mv <= 90) != (31 <= voltage_mv <= -90)"
    rule_expressions[87] = "(31 <= voltage_mv <= 90) != (31 <= -voltage_mv <= 90)"
    rule_expressions[88] = "(speed > voltage_mv + 50) != (speed > voltage_mv + 100)"
    rule_expressions[89] = "(speed > voltage_mv + 50) != (speed > voltage_mv + -50)"
    rule_expressions[90] = "(speed > voltage_mv + 50) != (speed > voltage_mv + -50)"
    rule_expressions[91] = "(speed > voltage_mv + 50) != (not (speed > voltage_mv + 50))"
    rule_expressions[92] = "(speed > voltage_mv + 50) != (speed > voltage_mv + 60)"
    rule_expressions[93] = "(speed > voltage_mv + 50) != (altitude > voltage_mv + 50)"
    rule_expressions[94] = "(speed > voltage_mv + 50) != (not (speed > voltage_mv + 50))"
    rule_expressions[95] = "(speed > voltage_mv + 50) != (not (speed > voltage_mv + 50))"
    rule_expressions[96] = "(speed < 30) != (speed < -30)"
    rule_expressions[97] = "(speed < 30) != (altitude < 30)"
    rule_expressions[98] = "(speed < 30) != (not (speed < 30))"
    rule_expressions[99] = "(speed < 30) != (voltage_mv < 30)"
    rule_expressions[100] = "(speed < 30) != (speed < -30)"
    rule_expressions[101] = "(speed < 30) != (not (speed < 30))"
    rule_expressions[102] = "(speed < 30) != (speed < 28)"
    rule_expressions[103] = "(altitude <= 30) != (not (altitude <= 30))"
    rule_expressions[104] = "(altitude <= 30) != (voltage_mv <= 30)"
    rule_expressions[105] = "(altitude <= 30) != (not (altitude <= 30))"
    rule_expressions[106] = "(altitude <= 30) != (altitude <= 15)"
    rule_expressions[107] = "(altitude <= 30) != (speed <= 30)"
    rule_expressions[108] = "(altitude <= 30) != (altitude <= 15)"
    rule_expressions[109] = "(speed < 2) != (not (speed < 2))"
    rule_expressions[110] = "(speed < 2) != (not (speed < 2))"
    rule_expressions[111] = "(speed < 2) != (not (speed < 2))"
    rule_expressions[112] = "(altitude == 1000 or voltage_mv > 30) != (not (altitude == 1000 or voltage_mv > 30))"
    rule_expressions[113] = "(altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or -voltage_mv > 30)"
    rule_expressions[114] = "(altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or voltage_mv > 15)"
    rule_expressions[115] = "(altitude == 1000 or voltage_mv > 30) != (altitude == 1000 and voltage_mv > 30)"
    rule_expressions[116] = "(altitude == 1000 or voltage_mv > 30) != (altitude == 1000 or voltage_mv > 31)"
    rule_expressions[117] = "(speed != voltage_mv + 53) != (speed != voltage_mv + 52)"
    rule_expressions[118] = "(speed != voltage_mv + 53) != (altitude != voltage_mv + 53)"
    rule_expressions[119] = "(speed != voltage_mv + 53) != (speed != voltage_mv + 43)"
    rule_expressions[120] = "(speed != voltage_mv + 53) != (voltage_mv != voltage_mv + 53)"
    rule_expressions[121] = "(speed != voltage_mv + 53) != (voltage_mv != speed + 53)"
    rule_expressions[122] = "(speed != voltage_mv + 53) != (speed != voltage_mv + 26)"
    rule_expressions[123] = "(speed != voltage_mv + 53) != (voltage_mv != speed + 53)"
    rule_expressions[124] = "(speed != voltage_mv + 53) != (speed != voltage_mv + 106)"
    rule_expressions[125] = "(speed != voltage_mv + 53) != (voltage_mv != voltage_mv + 53)"
    rule_expressions[126] = "(altitude != 30 or altitude != 100) != (speed != 30 or altitude != 100)"
    rule_expressions[127] = "(altitude != 30 or altitude != 100) != (altitude != 30 and altitude != 100)"
    rule_expressions[128] = "(voltage_mv < 5 and altitude == 424) != (voltage_mv < 5 or altitude == 424)"
    rule_expressions[129] = "(voltage_mv < 5 and altitude == 424) != (not (voltage_mv < 5 and altitude == 424))"
    rule_expressions[130] = "(6 <= speed <= 86) != (6 <= voltage_mv <= 86)"
    rule_expressions[131] = "(6 <= speed <= 86) != (6 <= speed <= 43)"
    rule_expressions[132] = "(6 <= speed <= 86) != (6 <= -speed <= 86)"
    rule_expressions[133] = "(6 <= speed <= 86) != (6 <= speed <= 81)"
    rule_expressions[134] = "(6 <= speed <= 86) != (speed >= 6 <= 86)"
    rule_expressions[135] = "(6 <= speed <= 86) != (6 <= speed <= 172)"
    rule_expressions[136] = "(6 <= speed <= 86) != (6 <= speed <= 96)"
    rule_expressions[137] = "(6 <= speed <= 86) != (speed >= 6 <= 86)"
    rule_expressions[138] = "(2 <= speed <= 63) != (2 <= -speed <= 63)"
    rule_expressions[139] = "(2 <= speed <= 63) != (not (2 <= speed <= 63))"
    rule_expressions[140] = "(2 <= speed <= 63) != (not (2 <= speed <= 63))"
    rule_expressions[141] = "(2 <= speed <= 63) != (2 <= altitude <= 63)"
    rule_expressions[142] = "(2 <= speed <= 63) != (2 <= voltage_mv <= 63)"
    rule_expressions[143] = "(2 <= speed <= 63) != (2 <= speed <= 73)"
    rule_expressions[144] = "(voltage_mv < 5) != (not (voltage_mv < 5))"
    rule_expressions[145] = "(voltage_mv < 5) != (voltage_mv < 7)"
    rule_expressions[146] = "(voltage_mv < 5) != (voltage_mv < 11)"
    rule_expressions[147] = "(altitude != 5 and altitude < 5) != (altitude != 5 and altitude < 13)"
    rule_expressions[148] = "(altitude != 5 and altitude < 5) != (altitude != 5 and -altitude < 5)"
    rule_expressions[149] = "(altitude != 5 and altitude < 5) != (not (altitude != 5 and altitude < 5))"
    rule_expressions[150] = "(altitude != 5 and altitude < 5) != (altitude != 5 or altitude < 5)"
    rule_expressions[151] = "(altitude != 5 and altitude < 5) != (altitude != 5 and -altitude < 5)"
    rule_expressions[152] = "(altitude > 2) != (altitude > 7)"
    rule_expressions[153] = "(altitude > 2) != (not (altitude > 2))"
    rule_expressions[154] = "(speed >= 10 and altitude <= 271) != (not (speed >= 10 and altitude <= 271))"
    rule_expressions[155] = "(speed >= 10 and altitude <= 271) != (speed >= 10 and -altitude <= 271)"
    rule_expressions[156] = "(speed >= 10 and altitude <= 271) != (speed >= 10 and altitude <= 276)"
    rule_expressions[157] = "(speed >= 10 and altitude <= 271) != (altitude >= 10 and altitude <= 271)"
    rule_expressions[158] = "(speed >= 10 and altitude <= 271) != (speed >= 10 and altitude <= -271)"
    rule_expressions[159] = "(speed >= 10 and altitude <= 271) != (voltage_mv >= 10 and altitude <= 271)"
    rule_expressions[160] = "(speed >= 10 and altitude <= 271) != (speed >= 10 or altitude <= 271)"
    rule_expressions[161] = "(speed <= 30 or altitude < 824) != (speed <= 30 or -altitude < 824)"
    rule_expressions[162] = "(speed <= 30 or altitude < 824) != (speed <= 30 or altitude < 819)"
    rule_expressions[163] = "(speed <= 30 or altitude < 824) != (speed <= 30 and altitude < 824)"
    rule_expressions[164] = "(speed <= 30 or altitude < 824) != (speed <= 30 or altitude < -824)"
    rule_expressions[165] = "(speed <= 30 or altitude < 824) != (speed <= 30 or altitude < 834)"
    rule_expressions[166] = "(voltage_mv <= 5) != (altitude <= 5)"
    rule_expressions[167] = "(voltage_mv <= 5) != (altitude <= 5)"
    rule_expressions[168] = "(voltage_mv <= 5) != (voltage_mv <= 1)"
    rule_expressions[169] = "(voltage_mv <= 5) != (voltage_mv <= 10)"
    rule_expressions[170] = "(voltage_mv <= 5) != (voltage_mv <= 4)"
    rule_expressions[171] = "(voltage_mv <= 5) != (voltage_mv <= 1)"
    rule_expressions[172] = "(voltage_mv <= 5) != (speed <= 5)"
    rule_expressions[173] = "(altitude >= 200) != (altitude >= -200)"
    rule_expressions[174] = "(altitude >= 200) != (altitude >= -200)"
    rule_expressions[175] = "(altitude >= 200) != (voltage_mv >= 200)"
    rule_expressions[176] = "(altitude >= 200) != (not (altitude >= 200))"
    rule_expressions[177] = "(altitude >= 200) != (altitude >= 199)"
    rule_expressions[178] = "(altitude >= 200) != (not (altitude >= 200))"
    rule_expressions[179] = "(altitude >= 200) != (altitude >= 198)"
    rule_expressions[180] = "(altitude != 839) != (not (altitude != 839))"
    rule_expressions[181] = "(altitude != 839) != (voltage_mv != 839)"
    rule_expressions[182] = "(altitude != 839) != (not (altitude != 839))"
    rule_expressions[183] = "(altitude != 839) != (not (altitude != 839))"

    return rule_expressions