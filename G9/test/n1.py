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
    if (altitude // speed != 200) != (altitude // speed != 400):
        triggered.add(1)
    # 变异规则 2 - UOI
    if (altitude // speed != 200) != (altitude // -speed != 200):
        triggered.add(2)
    # 变异规则 3 - RSR
    if (altitude // speed != 200) != (not (altitude // speed != 200)):
        triggered.add(3)
    # 变异规则 4 - CSR
    if (altitude // speed != 200) != (altitude // speed != -200):
        triggered.add(4)
    # 变异规则 5 - ABS
    if (altitude // speed != 200) != (abs(altitude) // speed != 200):
        t=1
    # 变异规则 6 - LCR
    if (altitude // speed != 200) != (voltage_mv // speed != 200):
        triggered.add(5)
    # 变异规则 7 - ROR
    if (altitude // speed != 200) != (altitude // speed != -200):
        triggered.add(6)
    # 变异规则 8 - AOR
    if (altitude // speed != 200) != (not (altitude // speed != 200)):
        triggered.add(7)
    # 变异规则 9 - SVR
    if (altitude // speed != 200) != (voltage_mv // speed != 200):
        triggered.add(8)
    # 变异规则 10 - SCR
    if (altitude // speed != 200) != (altitude // speed != 400):
        triggered.add(9)
    # 原语句
    if altitude // speed != 200:
        health_score += 17
    # 原语句2
    # 变异规则 11 - SRC
    if (208 <= altitude <= 626) != (215 <= altitude <= 626):
        triggered.add(10)
    # 变异规则 12 - SVR
    if (208 <= altitude <= 626) != (208 <= speed <= 626):
        triggered.add(11)
    # 变异规则 13 - ROR
    if (208 <= altitude <= 626) != (not (208 <= altitude <= 626)):
        triggered.add(12)
    # 变异规则 14 - AOR
    if (208 <= altitude <= 626) != (206 <= altitude <= 626):
        triggered.add(13)
    # 变异规则 15 - SCR
    if (208 <= altitude <= 626) != (not (208) <= altitude <= 626):
        triggered.add(14)
    # 变异规则 16 - RSR
    if (208 <= altitude <= 626) != (not (208 <= altitude <= 626)):
        triggered.add(15)
    # 变异规则 17 - CSR
    if (208 <= altitude <= 626) != (-208 <= altitude <= 626):
        triggered.add(16)
    # 变异规则 18 - SAR
    if (208 <= altitude <= 626) != (altitude >= 208 <= 626):
        triggered.add(17)
    # 变异规则 19 - CRP
    if (208 <= altitude <= 626) != (208 <= altitude <= 1252):
        triggered.add(18)
    # 变异规则 20 - LCR
    if (208 <= altitude <= 626) != (208 <= altitude <= -626):
        triggered.add(19)
    # 原语句
    if 208 <= altitude <= 626:
        speed = max(speed - 7, 2)
    # 原语句3
    # 变异规则 21 - SRC
    if (voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv == 65 and voltage_mv >= 2):
        t=1
    # 变异规则 22 - CSR
    if (voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 and voltage_mv == -65):
        triggered.add(20)
    # 变异规则 23 - CAR
    if (voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 and voltage_mv == 64):
        triggered.add(21)
    # 变异规则 24 - SCR
    if (voltage_mv >= 2 and voltage_mv == 65) != (2 <= voltage_mv and voltage_mv == 65):
        t=1
    # 变异规则 25 - UOI
    if (voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 and -voltage_mv == 65):
        triggered.add(22)
    # 变异规则 26 - LCR
    if (voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 or voltage_mv == 65):
        triggered.add(23)
    # 变异规则 27 - SVR
    if (voltage_mv >= 2 and voltage_mv == 65) != (speed >= 2 and voltage_mv == 65):
        t=1
    # 变异规则 28 - SAR
    if (voltage_mv >= 2 and voltage_mv == 65) != (2 <= voltage_mv and voltage_mv == 65):
        t=1
    # 变异规则 29 - CRP
    if (voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 1 and voltage_mv == 65):
        t=1
    # 变异规则 30 - RSR
    if (voltage_mv >= 2 and voltage_mv == 65) != (not (voltage_mv >= 2 and voltage_mv == 65)):
        triggered.add(24)
    # 原语句
    if voltage_mv >= 2 and voltage_mv == 65:
        health_score -= 4
        altitude = max(altitude - 34, 2)
        speed = max(speed - 9, 2)
    # 原语句4
    # 变异规则 31 - SAR
    if (altitude % 10 < voltage_mv) != (altitude % voltage_mv > 10):
        triggered.add(25)
    # 变异规则 32 - AOR
    if (altitude % 10 < voltage_mv) != (altitude % 19 < voltage_mv):
        triggered.add(26)
    # 变异规则 33 - ROR
    if (altitude % 10 < voltage_mv) != (voltage_mv % 10 < voltage_mv):
        triggered.add(27)
    # 变异规则 34 - CRP
    if (altitude % 10 < voltage_mv) != (altitude % 5 < voltage_mv):
        triggered.add(28)
    # 变异规则 35 - RSR
    if (altitude % 10 < voltage_mv) != (not (altitude % 10 < voltage_mv)):
        triggered.add(29)
    # 变异规则 36 - CSR
    if (altitude % 10 < voltage_mv) != (altitude % -10 < voltage_mv):
        triggered.add(30)
    # 变异规则 37 - SRC
    if (altitude % 10 < voltage_mv) != (speed % 10 < voltage_mv):
        triggered.add(31)
    # 变异规则 38 - LCR
    if (altitude % 10 < voltage_mv) != (altitude % 11 < voltage_mv):
        triggered.add(32)
    # 变异规则 39 - SCR
    if (altitude % 10 < voltage_mv) != (voltage_mv % 10 < voltage_mv):
        triggered.add(33)
    # 变异规则 40 - ABS
    if (altitude % 10 < voltage_mv) != (abs(altitude) % 10 < voltage_mv):
        t=1
    # 原语句
    if altitude % 10 < voltage_mv:
        health_score += 10
        altitude = max(altitude - 9, 2)
        speed = max(speed - 9, 2)
        voltage_mv = min(voltage_mv + 4, 100)
    # 原语句5
    # 变异规则 41 - SVR
    if (altitude < 984 or voltage_mv == 72) != (voltage_mv < 984 or voltage_mv == 72):
        triggered.add(34)
    # 变异规则 42 - CRP
    if (altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == 36):
        triggered.add(35)
    # 变异规则 43 - SCR
    if (altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == 74):
        triggered.add(36)
    # 变异规则 44 - SAR
    if (altitude < 984 or voltage_mv == 72) != (984 > altitude or voltage_mv == 72):
        t=1
    # 变异规则 45 - AOR
    if (altitude < 984 or voltage_mv == 72) != (altitude < 984 or -voltage_mv == 72):
        triggered.add(37)
    # 变异规则 46 - LCR
    if (altitude < 984 or voltage_mv == 72) != (altitude < 984 and voltage_mv == 72):
        triggered.add(38)
    # 变异规则 47 - UOI
    if (altitude < 984 or voltage_mv == 72) != (altitude < 984 or -voltage_mv == 72):
        triggered.add(39)
    # 变异规则 48 - CAR
    if (altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == 70):
        triggered.add(40)
    # 变异规则 49 - ABS
    if (altitude < 984 or voltage_mv == 72) != (abs(altitude) < 984 or voltage_mv == 72):
        t=1
    # 变异规则 50 - CSR
    if (altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == -72):
        triggered.add(41)
    # 原语句
    if altitude < 984 or voltage_mv == 72:
        health_score -= 11
        altitude = max(altitude - 16, 2)
        voltage_mv = max(voltage_mv - 5, 2)
        voltage_mv, speed = speed, voltage_mv
    # 原语句6
    # 变异规则 51 - SRC
    if (speed <= altitude * 48) != (altitude >= speed * 48):
        triggered.add(42)
    # 变异规则 52 - LCR
    if (speed <= altitude * 48) != (speed <= abs(altitude) * 48):
        t=1
    # 变异规则 53 - AOR
    if (speed <= altitude * 48) != (speed <= altitude * 24):
        triggered.add(43)
    # 变异规则 54 - CSR
    if (speed <= altitude * 48) != (speed <= altitude * -48):
        triggered.add(44)
    # 变异规则 55 - ROR
    if (speed <= altitude * 48) != (speed <= altitude * -48):
        triggered.add(45)
    # 变异规则 56 - SAR
    if (speed <= altitude * 48) != (altitude >= speed * 48):
        triggered.add(46)
    # 变异规则 57 - UOI
    if (speed <= altitude * 48) != (speed <= -altitude * 48):
        triggered.add(47)
    # 变异规则 58 - CAR
    if (speed <= altitude * 48) != (speed <= altitude * 46):
        triggered.add(48)
    # 变异规则 59 - SCR
    if (speed <= altitude * 48) != (not (speed <= altitude * 48)):
        triggered.add(49)
    # 变异规则 60 - RSR
    if (speed <= altitude * 48) != (not (speed <= altitude * 48)):
        triggered.add(50)
    # 原语句
    if speed <= altitude * 48:
        health_score -= 24
    # 原语句7
    # 变异规则 61 - ROR
    if (speed > 20) != (speed > -20):
        triggered.add(51)
    # 变异规则 62 - SCR
    if (speed > 20) != (not (speed > 20)):
        triggered.add(52)
    # 变异规则 63 - CSR
    if (speed > 20) != (speed > -20):
        triggered.add(53)
    # 变异规则 64 - AOR
    if (speed > 20) != (speed > 40):
        triggered.add(54)
    # 变异规则 65 - SVR
    if (speed > 20) != (voltage_mv > 20):
        triggered.add(55)
    # 变异规则 66 - CAR
    if (speed > 20) != (speed > 21):
        triggered.add(56)
    # 变异规则 67 - SRC
    if (speed > 20) != (speed > -20):
        triggered.add(57)
    # 变异规则 68 - SAR
    if (speed > 20) != (20 < speed):
        t=1
    # 变异规则 69 - CRP
    if (speed > 20) != (speed > 27):
        triggered.add(58)
    # 变异规则 70 - RSR
    if (speed > 20) != (not (speed > 20)):
        triggered.add(59)
    # 原语句
    if speed > 20:
        health_score -= 12
        speed = min(speed + 2, 100)
        speed, altitude = altitude, speed
    # 原语句8
    # 变异规则 71 - SRC
    if (speed * voltage_mv == 50) != (speed * voltage_mv == 40):
        triggered.add(60)
    # 变异规则 72 - ROR
    if (speed * voltage_mv == 50) != (abs(speed) * voltage_mv == 50):
        t=1
    # 变异规则 73 - CAR
    if (speed * voltage_mv == 50) != (speed * voltage_mv == 45):
        triggered.add(61)
    # 变异规则 74 - CRP
    if (speed * voltage_mv == 50) != (speed * voltage_mv == 25):
        triggered.add(62)
    # 变异规则 75 - ABS
    if (speed * voltage_mv == 50) != (abs(speed) * voltage_mv == 50):
        t=1
    # 变异规则 76 - UOI
    if (speed * voltage_mv == 50) != (speed * -voltage_mv == 50):
        triggered.add(63)
    # 变异规则 77 - AOR
    if (speed * voltage_mv == 50) != (speed * voltage_mv == -50):
        triggered.add(64)
    # 变异规则 78 - RSR
    if (speed * voltage_mv == 50) != (not (speed * voltage_mv == 50)):
        triggered.add(65)
    # 变异规则 79 - CSR
    if (speed * voltage_mv == 50) != (speed * voltage_mv == -50):
        triggered.add(66)
    # 变异规则 80 - SCR
    if (speed * voltage_mv == 50) != (speed * -voltage_mv == 50):
        triggered.add(67)
    # 原语句
    if speed * voltage_mv == 50:
        health_score -= 19
        altitude = min(altitude + 61, 1000)
    # 原语句9
    # 变异规则 81 - ROR
    if (speed == 96 or voltage_mv != 51) != (speed == 96 or voltage_mv != 25):
        triggered.add(68)
    # 变异规则 82 - SAR
    if (speed == 96 or voltage_mv != 51) != (96 == speed or voltage_mv != 51):
        t=1
    # 变异规则 83 - CSR
    if (speed == 96 or voltage_mv != 51) != (speed == 96 or voltage_mv != -51):
        triggered.add(69)
    # 变异规则 84 - LCR
    if (speed == 96 or voltage_mv != 51) != (speed == 96 and voltage_mv != 51):
        triggered.add(70)
    # 变异规则 85 - SRC
    if (speed == 96 or voltage_mv != 51) != (voltage_mv != 51 or speed == 96):
        t=1
    # 变异规则 86 - RSR
    if (speed == 96 or voltage_mv != 51) != (not (speed == 96 or voltage_mv != 51)):
        triggered.add(71)
    # 变异规则 87 - CRP
    if (speed == 96 or voltage_mv != 51) != (speed == 96 or voltage_mv != 56):
        triggered.add(72)
    # 变异规则 88 - UOI
    if (speed == 96 or voltage_mv != 51) != (speed == 96 or -voltage_mv != 51):
        triggered.add(73)
    # 变异规则 89 - AOR
    if (speed == 96 or voltage_mv != 51) != (speed == 96 and voltage_mv != 51):
        triggered.add(74)
    # 变异规则 90 - SCR
    if (speed == 96 or voltage_mv != 51) != (speed == 94 or voltage_mv != 51):
        triggered.add(75)
    # 原语句
    if speed == 96 or voltage_mv != 51:
        health_score += 8
    # 原语句10
    # 变异规则 91 - ABS
    if (altitude <= 1000 and voltage_mv <= 20) != (abs(altitude) <= 1000 and voltage_mv <= 20):
        t=1
    # 变异规则 92 - CSR
    if (altitude <= 1000 and voltage_mv <= 20) != (altitude <= -1000 and voltage_mv <= 20):
        triggered.add(76)
    # 变异规则 93 - SVR
    if (altitude <= 1000 and voltage_mv <= 20) != (voltage_mv <= 1000 and voltage_mv <= 20):
        t=1
    # 变异规则 94 - LCR
    if (altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 or voltage_mv <= 20):
        triggered.add(77)
    # 变异规则 95 - SRC
    if (altitude <= 1000 and voltage_mv <= 20) != (voltage_mv <= 20 and altitude <= 1000):
        t=1
    # 变异规则 96 - SCR
    if (altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 and -voltage_mv <= 20):
        triggered.add(78)
    # 变异规则 97 - ROR
    if (altitude <= 1000 and voltage_mv <= 20) != (not (altitude <= 1000 and voltage_mv <= 20)):
        triggered.add(79)
    # 变异规则 98 - UOI
    if (altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 and -voltage_mv <= 20):
        triggered.add(80)
    # 变异规则 99 - RSR
    if (altitude <= 1000 and voltage_mv <= 20) != (not (altitude <= 1000 and voltage_mv <= 20)):
        triggered.add(81)
    # 变异规则 100 - CAR
    if (altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 and voltage_mv <= 25):
        triggered.add(82)
    # 原语句
    if altitude <= 1000 and voltage_mv <= 20:
        health_score += 18
    # 原语句11
    # 变异规则 101 - CAR
    if (18 <= speed <= 76) != (18 <= speed <= 86):
        triggered.add(83)
    # 变异规则 102 - SRC
    if (18 <= speed <= 76) != (18 <= speed <= 69):
        triggered.add(84)
    # 变异规则 103 - SCR
    if (18 <= speed <= 76) != (not (18) <= speed <= 76):
        triggered.add(85)
    # 变异规则 104 - CSR
    if (18 <= speed <= 76) != (-18 <= speed <= 76):
        triggered.add(86)
    # 变异规则 105 - ABS
    if (18 <= speed <= 76) != (18 <= abs(speed) <= 76):
        t=1
    # 变异规则 106 - RSR
    if (18 <= speed <= 76) != (not (18 <= speed <= 76)):
        triggered.add(87)
    # 变异规则 107 - SAR
    if (18 <= speed <= 76) != (speed >= 18 <= 76):
        triggered.add(88)
    # 变异规则 108 - UOI
    if (18 <= speed <= 76) != (18 <= -speed <= 76):
        triggered.add(89)
    # 变异规则 109 - SVR
    if (18 <= speed <= 76) != (18 <= voltage_mv <= 76):
        triggered.add(90)
    # 变异规则 110 - AOR
    if (18 <= speed <= 76) != (not (18 <= speed <= 76)):
        triggered.add(91)
    # 原语句
    if 18 <= speed <= 76:
        health_score -= 6
    # 原语句12
    # 变异规则 111 - SVR
    if (altitude >= 200 or altitude <= 696) != (speed >= 200 or altitude <= 696):
        triggered.add(92)
    # 变异规则 112 - ABS
    if (altitude >= 200 or altitude <= 696) != (abs(altitude) >= 200 or altitude <= 696):
        t=1
    # 变异规则 113 - ROR
    if (altitude >= 200 or altitude <= 696) != (altitude >= 210 or altitude <= 696):
        t=1
    # 变异规则 114 - UOI
    if (altitude >= 200 or altitude <= 696) != (altitude >= 200 or -altitude <= 696):
        t=1
    # 变异规则 115 - SAR
    if (altitude >= 200 or altitude <= 696) != (altitude >= 200 or 696 >= altitude):
        t=1
    # 变异规则 116 - CAR
    if (altitude >= 200 or altitude <= 696) != (altitude >= 210 or altitude <= 696):
        t=1
    # 变异规则 117 - AOR
    if (altitude >= 200 or altitude <= 696) != (abs(altitude) >= 200 or altitude <= 696):
        t=1
    # 变异规则 118 - RSR
    if (altitude >= 200 or altitude <= 696) != (not (altitude >= 200 or altitude <= 696)):
        triggered.add(93)
    # 变异规则 119 - LCR
    if (altitude >= 200 or altitude <= 696) != (altitude >= 200 and altitude <= 696):
        triggered.add(94)
    # 变异规则 120 - SRC
    if (altitude >= 200 or altitude <= 696) != (altitude <= 696 or altitude >= 200):
        t=1
    # 原语句
    if altitude >= 200 or altitude <= 696:
        health_score -= 11
        speed = max(speed - 1, 2)
        voltage_mv = max(voltage_mv - 10, 2)
    # 原语句13
    # 变异规则 121 - UOI
    if (voltage_mv <= 5 and speed == 20) != (voltage_mv <= 5 and -speed == 20):
        triggered.add(95)
    # 变异规则 122 - SAR
    if (voltage_mv <= 5 and speed == 20) != (5 >= voltage_mv and speed == 20):
        t=1
    # 变异规则 123 - SCR
    if (voltage_mv <= 5 and speed == 20) != (speed <= 5 and speed == 20):
        triggered.add(96)
    # 变异规则 124 - SRC
    if (voltage_mv <= 5 and speed == 20) != (speed == 20 and voltage_mv <= 5):
        t=1
    # 变异规则 125 - CAR
    if (voltage_mv <= 5 and speed == 20) != (voltage_mv <= 3 and speed == 20):
        triggered.add(97)
    # 变异规则 126 - CRP
    if (voltage_mv <= 5 and speed == 20) != (voltage_mv <= 5 and speed == 13):
        triggered.add(98)
    # 变异规则 127 - SVR
    if (voltage_mv <= 5 and speed == 20) != (altitude <= 5 and speed == 20):
        triggered.add(99)
    # 变异规则 128 - ABS
    if (voltage_mv <= 5 and speed == 20) != (voltage_mv <= 5 and abs(speed) == 20):
        t=1
    # 变异规则 129 - ROR
    if (voltage_mv <= 5 and speed == 20) != (5 >= voltage_mv and speed == 20):
        t=1
    # 变异规则 130 - LCR
    if (voltage_mv <= 5 and speed == 20) != (voltage_mv <= 5 or speed == 20):
        triggered.add(100)
    # 原语句
    if voltage_mv <= 5 and speed == 20:
        health_score -= 20
        altitude = min(altitude + 82, 1000)
        speed, altitude = altitude, speed
    # 原语句14
    # 变异规则 131 - CSR
    if (speed >= 20) != (speed >= -20):
        triggered.add(101)
    # 变异规则 132 - UOI
    if (speed >= 20) != (altitude >= 20):
        triggered.add(102)
    # 变异规则 133 - SAR
    if (speed >= 20) != (20 <= speed):
        t=1
    # 变异规则 134 - RSR
    if (speed >= 20) != (not (speed >= 20)):
        triggered.add(103)
    # 变异规则 135 - ROR
    if (speed >= 20) != (speed >= 17):
        triggered.add(104)
    # 变异规则 136 - SVR
    if (speed >= 20) != (altitude >= 20):
        triggered.add(105)
    # 变异规则 137 - SRC
    if (speed >= 20) != (abs(speed) >= 20):
        t=1
    # 变异规则 138 - CRP
    if (speed >= 20) != (speed >= 10):
        triggered.add(106)
    # 变异规则 139 - ABS
    if (speed >= 20) != (abs(speed) >= 20):
        t=1
    # 变异规则 140 - SCR
    if (speed >= 20) != (20 <= speed):
        t=1
    # 原语句
    if speed >= 20:
        health_score -= 6
    # 原语句15
    # 变异规则 141 - CSR
    if (speed < 100) != (speed < -100):
        triggered.add(107)
    # 变异规则 142 - LCR
    if (speed < 100) != (speed < 99):
        triggered.add(108)
    # 变异规则 143 - SVR
    if (speed < 100) != (altitude < 100):
        triggered.add(109)
    # 变异规则 144 - SAR
    if (speed < 100) != (100 > speed):
        t=1
    # 变异规则 145 - RSR
    if (speed < 100) != (not (speed < 100)):
        triggered.add(110)
    # 变异规则 146 - SCR
    if (speed < 100) != (speed < -100):
        triggered.add(111)
    # 变异规则 147 - SRC
    if (speed < 100) != (speed < 101):
        triggered.add(112)
    # 变异规则 148 - CAR
    if (speed < 100) != (speed < 101):
        triggered.add(113)
    # 变异规则 149 - ABS
    if (speed < 100) != (abs(speed) < 100):
        t=1
    # 变异规则 150 - UOI
    if (speed < 100) != (voltage_mv < 100):
        triggered.add(114)
    # 原语句
    if speed < 100:
        health_score += 19
        speed = min(speed + 5, 100)
        voltage_mv = max(voltage_mv - 3, 2)
        altitude, speed = speed, altitude
    # 原语句16
    # 变异规则 151 - ROR
    if (speed == 5 and altitude > 194) != (altitude == 5 and altitude > 194):
        t=1
    # 变异规则 152 - SVR
    if (speed == 5 and altitude > 194) != (voltage_mv == 5 and altitude > 194):
        t=1
    # 变异规则 153 - SAR
    if (speed == 5 and altitude > 194) != (speed == 5 and 194 < altitude):
        t=1
    # 变异规则 154 - CSR
    if (speed == 5 and altitude > 194) != (speed == 5 and altitude > -194):
        triggered.add(115)
    # 变异规则 155 - RSR
    if (speed == 5 and altitude > 194) != (not (speed == 5 and altitude > 194)):
        triggered.add(116)
    # 变异规则 156 - LCR
    if (speed == 5 and altitude > 194) != (speed == 5 or altitude > 194):
        triggered.add(117)
    # 变异规则 157 - SCR
    if (speed == 5 and altitude > 194) != (speed == 1 and altitude > 194):
        t=1
    # 变异规则 158 - CRP
    if (speed == 5 and altitude > 194) != (speed == 2 and altitude > 194):
        t=1
    # 变异规则 159 - SRC
    if (speed == 5 and altitude > 194) != (altitude > 194 and speed == 5):
        t=1
    # 变异规则 160 - UOI
    if (speed == 5 and altitude > 194) != (speed == 5 and -altitude > 194):
        t=1
    # 原语句
    if speed == 5 and altitude > 194:
        health_score += 19
        speed = max(speed - 4, 2)
        voltage_mv = min(voltage_mv + 8, 100)
    # 原语句17
    # 变异规则 161 - SAR
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 and 30 < speed):
        t=1
    # 变异规则 162 - ABS
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 and abs(speed) > 30):
        t=1
    # 变异规则 163 - UOI
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 and -speed > 30):
        triggered.add(118)
    # 变异规则 164 - AOR
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 22 and speed > 30):
        triggered.add(119)
    # 变异规则 165 - SRC
    if (voltage_mv <= 20 and speed > 30) != (speed > 30 and voltage_mv <= 20):
        t=1
    # 变异规则 166 - CRP
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 40 and speed > 30):
        triggered.add(120)
    # 变异规则 167 - CAR
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 22 and speed > 30):
        triggered.add(121)
    # 变异规则 168 - CSR
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 and speed > -30):
        triggered.add(122)
    # 变异规则 169 - LCR
    if (voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 or speed > 30):
        triggered.add(123)
    # 变异规则 170 - RSR
    if (voltage_mv <= 20 and speed > 30) != (not (voltage_mv <= 20 and speed > 30)):
        triggered.add(124)
    # 原语句
    if voltage_mv <= 20 and speed > 30:
        health_score -= 30
        altitude = max(altitude - 1, 2)
        voltage_mv = min(voltage_mv + 10, 100)
    # 原语句18
    # 变异规则 171 - CRP
    if (voltage_mv != 10) != (voltage_mv != 20):
        triggered.add(125)
    # 变异规则 172 - SVR
    if (voltage_mv != 10) != (altitude != 10):
        triggered.add(126)
    # 变异规则 173 - ROR
    if (voltage_mv != 10) != (not (voltage_mv != 10)):
        triggered.add(127)
    # 变异规则 174 - CAR
    if (voltage_mv != 10) != (voltage_mv != 11):
        triggered.add(128)
    # 变异规则 175 - AOR
    if (voltage_mv != 10) != (voltage_mv != 11):
        triggered.add(129)
    # 变异规则 176 - LCR
    if (voltage_mv != 10) != (abs(voltage_mv) != 10):
        t=1
    # 变异规则 177 - UOI
    if (voltage_mv != 10) != (10 != voltage_mv):
        t=1
    # 变异规则 178 - SCR
    if (voltage_mv != 10) != (10 != voltage_mv):
        t=1
    # 变异规则 179 - SAR
    if (voltage_mv != 10) != (10 != voltage_mv):
        t=1
    # 变异规则 180 - ABS
    if (voltage_mv != 10) != (abs(voltage_mv) != 10):
        t=1
    # 原语句
    if voltage_mv != 10:
        health_score -= 6
        altitude, speed = speed, altitude
    # 原语句19
    # 变异规则 181 - RSR
    if (altitude != 2) != (not (altitude != 2)):
        triggered.add(130)
    # 变异规则 182 - SAR
    if (altitude != 2) != (2 != altitude):
        t=1
    # 变异规则 183 - ABS
    if (altitude != 2) != (abs(altitude) != 2):
        t=1
    # 变异规则 184 - SVR
    if (altitude != 2) != (speed != 2):
        triggered.add(131)
    # 变异规则 185 - UOI
    if (altitude != 2) != (voltage_mv != 2):
        triggered.add(132)
    # 变异规则 186 - LCR
    if (altitude != 2) != (abs(altitude) != 2):
        t=1
    # 变异规则 187 - AOR
    if (altitude != 2) != (abs(altitude) != 2):
        t=1
    # 变异规则 188 - CRP
    if (altitude != 2) != (altitude != 4):
        triggered.add(133)
    # 变异规则 189 - ROR
    if (altitude != 2) != (altitude != 7):
        triggered.add(134)
    # 变异规则 190 - CAR
    if (altitude != 2) != (altitude != 7):
        triggered.add(135)
    # 原语句
    if altitude != 2:
        health_score += 5
        voltage_mv = min(voltage_mv + 3, 100)
    # 原语句20
    # 变异规则 191 - SRC
    if (voltage_mv == 50) != (voltage_mv == -50):
        triggered.add(136)
    # 变异规则 192 - AOR
    if (voltage_mv == 50) != (voltage_mv == 100):
        triggered.add(137)
    # 变异规则 193 - SCR
    if (voltage_mv == 50) != (50 == voltage_mv):
        t=1
    # 变异规则 194 - ABS
    if (voltage_mv == 50) != (abs(voltage_mv) == 50):
        t=1
    # 变异规则 195 - CRP
    if (voltage_mv == 50) != (voltage_mv == 57):
        triggered.add(138)
    # 变异规则 196 - UOI
    if (voltage_mv == 50) != (voltage_mv == 49):
        triggered.add(139)
    # 变异规则 197 - ROR
    if (voltage_mv == 50) != (voltage_mv == -50):
        triggered.add(140)
    # 变异规则 198 - SAR
    if (voltage_mv == 50) != (50 == voltage_mv):
        t=1
    # 变异规则 199 - RSR
    if (voltage_mv == 50) != (not (voltage_mv == 50)):
        triggered.add(141)
    # 变异规则 200 - CAR
    if (voltage_mv == 50) != (voltage_mv == 45):
        triggered.add(142)
    # 原语句
    if voltage_mv == 50:
        health_score += 8
        speed = max(speed - 6, 2)
        speed, altitude = altitude, speed
    # 原语句21
    # 变异规则 201 - SAR
    if (24 <= speed <= 86) != (speed >= 24 <= 86):
        triggered.add(143)
    # 变异规则 202 - ROR
    if (24 <= speed <= 86) != (24 <= voltage_mv <= 86):
        triggered.add(144)
    # 变异规则 203 - SRC
    if (24 <= speed <= 86) != (24 <= -speed <= 86):
        triggered.add(145)
    # 变异规则 204 - LCR
    if (24 <= speed <= 86) != (-24 <= speed <= 86):
        triggered.add(146)
    # 变异规则 205 - CAR
    if (24 <= speed <= 86) != (24 <= speed <= 76):
        triggered.add(147)
    # 变异规则 206 - AOR
    if (24 <= speed <= 86) != (24 <= altitude <= 86):
        triggered.add(148)
    # 变异规则 207 - UOI
    if (24 <= speed <= 86) != (24 <= -speed <= 86):
        triggered.add(149)
    # 变异规则 208 - SCR
    if (24 <= speed <= 86) != (not (24) <= speed <= 86):
        triggered.add(150)
    # 变异规则 209 - RSR
    if (24 <= speed <= 86) != (not (24 <= speed <= 86)):
        triggered.add(151)
    # 变异规则 210 - ABS
    if (24 <= speed <= 86) != (24 <= abs(speed) <= 86):
        t=1
    # 原语句
    if 24 <= speed <= 86:
        health_score -= 9
    # 原语句22
    # 变异规则 211 - SAR
    if (altitude > 20 or altitude > 5) != (20 < altitude or altitude > 5):
        t=1
    # 变异规则 212 - ROR
    if (altitude > 20 or altitude > 5) != (altitude > 20 or altitude > 1):
        triggered.add(152)
    # 变异规则 213 - AOR
    if (altitude > 20 or altitude > 5) != (altitude > 20 or altitude > 14):
        triggered.add(153)
    # 变异规则 214 - SCR
    if (altitude > 20 or altitude > 5) != (not (altitude > 20 or altitude > 5)):
        triggered.add(154)
    # 变异规则 215 - UOI
    if (altitude > 20 or altitude > 5) != (altitude > 20 or -altitude > 5):
        triggered.add(155)
    # 变异规则 216 - SRC
    if (altitude > 20 or altitude > 5) != (altitude > 5 or altitude > 20):
        t=1
    # 变异规则 217 - SVR
    if (altitude > 20 or altitude > 5) != (voltage_mv > 20 or altitude > 5):
        triggered.add(156)
    # 变异规则 218 - CRP
    if (altitude > 20 or altitude > 5) != (altitude > 20 or altitude > 10):
        triggered.add(157)
    # 变异规则 219 - CAR
    if (altitude > 20 or altitude > 5) != (altitude > 18 or altitude > 5):
        t=1
    # 变异规则 220 - RSR
    if (altitude > 20 or altitude > 5) != (not (altitude > 20 or altitude > 5)):
        triggered.add(158)
    # 原语句
    if altitude > 20 or altitude > 5:
        health_score -= 2
        voltage_mv = max(voltage_mv - 7, 2)
        voltage_mv, speed = speed, voltage_mv
    # 原语句23
    # 变异规则 221 - RSR
    if (voltage_mv != 100 and speed <= 56) != (not (voltage_mv != 100 and speed <= 56)):
        triggered.add(159)
    # 变异规则 222 - SCR
    if (voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and -speed <= 56):
        triggered.add(160)
    # 变异规则 223 - ROR
    if (voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and speed <= -56):
        triggered.add(161)
    # 变异规则 224 - SVR
    if (voltage_mv != 100 and speed <= 56) != (altitude != 100 and speed <= 56):
        triggered.add(162)
    # 变异规则 225 - CRP
    if (voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and speed <= 53):
        triggered.add(163)
    # 变异规则 226 - LCR
    if (voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 or speed <= 56):
        triggered.add(164)
    # 变异规则 227 - CAR
    if (voltage_mv != 100 and speed <= 56) != (voltage_mv != 99 and speed <= 56):
        triggered.add(165)
    # 变异规则 228 - ABS
    if (voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and abs(speed) <= 56):
        t=1
    # 变异规则 229 - UOI
    if (voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and -speed <= 56):
        triggered.add(166)
    # 变异规则 230 - SRC
    if (voltage_mv != 100 and speed <= 56) != (speed <= 56 and voltage_mv != 100):
        t=1
    # 原语句
    if voltage_mv != 100 and speed <= 56:
        health_score -= 23
        speed = min(speed + 6, 100)
        voltage_mv = max(voltage_mv - 8, 2)
    # 原语句24
    # 变异规则 231 - RSR
    if (13 <= voltage_mv <= 59) != (not (13 <= voltage_mv <= 59)):
        triggered.add(167)
    # 变异规则 232 - UOI
    if (13 <= voltage_mv <= 59) != (13 <= -voltage_mv <= 59):
        triggered.add(168)
    # 变异规则 233 - LCR
    if (13 <= voltage_mv <= 59) != (not (13 <= voltage_mv <= 59)):
        triggered.add(169)
    # 变异规则 234 - CRP
    if (13 <= voltage_mv <= 59) != (13 <= voltage_mv <= 54):
        triggered.add(170)
    # 变异规则 235 - SCR
    if (13 <= voltage_mv <= 59) != (26 <= voltage_mv <= 59):
        triggered.add(171)
    # 变异规则 236 - ABS
    if (13 <= voltage_mv <= 59) != (13 <= abs(voltage_mv) <= 59):
        t=1
    # 变异规则 237 - SVR
    if (13 <= voltage_mv <= 59) != (13 <= speed <= 59):
        triggered.add(172)
    # 变异规则 238 - AOR
    if (13 <= voltage_mv <= 59) != (voltage_mv >= 13 <= 59):
        triggered.add(173)
    # 变异规则 239 - SRC
    if (13 <= voltage_mv <= 59) != (13 <= voltage_mv <= -59):
        triggered.add(174)
    # 变异规则 240 - CAR
    if (13 <= voltage_mv <= 59) != (13 <= voltage_mv <= 64):
        triggered.add(175)
    # 原语句
    if 13 <= voltage_mv <= 59:
        health_score -= 27
    # 原语句25
    # 变异规则 241 - ROR
    if (voltage_mv < 2 or altitude < 10) != (speed < 2 or altitude < 10):
        t=1
    # 变异规则 242 - SCR
    if (voltage_mv < 2 or altitude < 10) != (altitude < 10 or voltage_mv < 2):
        t=1
    # 变异规则 243 - SAR
    if (voltage_mv < 2 or altitude < 10) != (2 > voltage_mv or altitude < 10):
        t=1
    # 变异规则 244 - LCR
    if (voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 and altitude < 10):
        triggered.add(176)
    # 变异规则 245 - ABS
    if (voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 or abs(altitude) < 10):
        t=1
    # 变异规则 246 - CSR
    if (voltage_mv < 2 or altitude < 10) != (voltage_mv < -2 or altitude < 10):
        t=1
    # 变异规则 247 - UOI
    if (voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 or -altitude < 10):
        triggered.add(177)
    # 变异规则 248 - SVR
    if (voltage_mv < 2 or altitude < 10) != (speed < 2 or altitude < 10):
        t=1
    # 变异规则 249 - CAR
    if (voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 or altitude < 11):
        triggered.add(178)
    # 变异规则 250 - CRP
    if (voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 or altitude < 5):
        triggered.add(179)
    # 原语句
    if voltage_mv < 2 or altitude < 10:
        health_score -= 4
        speed = max(speed - 10, 2)
        voltage_mv, speed = speed, voltage_mv
    # 原语句26
    # 变异规则 251 - SCR
    if (speed < 10) != (altitude < 10):
        triggered.add(180)
    # 变异规则 252 - ROR
    if (speed < 10) != (altitude < 10):
        triggered.add(181)
    # 变异规则 253 - CSR
    if (speed < 10) != (speed < -10):
        triggered.add(182)
    # 变异规则 254 - SRC
    if (speed < 10) != (not (speed < 10)):
        triggered.add(183)
    # 变异规则 255 - LCR
    if (speed < 10) != (altitude < 10):
        triggered.add(184)
    # 变异规则 256 - CRP
    if (speed < 10) != (speed < 5):
        triggered.add(185)
    # 变异规则 257 - ABS
    if (speed < 10) != (abs(speed) < 10):
        t=1
    # 变异规则 258 - CAR
    if (speed < 10) != (speed < 9):
        triggered.add(186)
    # 变异规则 259 - AOR
    if (speed < 10) != (speed < 5):
        triggered.add(187)
    # 变异规则 260 - RSR
    if (speed < 10) != (not (speed < 10)):
        triggered.add(188)
    # 原语句
    if speed < 10:
        health_score += 1
        altitude = min(altitude + 18, 1000)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句27
    # 变异规则 261 - ROR
    if (voltage_mv == 70) != (voltage_mv == 71):
        triggered.add(189)
    # 变异规则 262 - CSR
    if (voltage_mv == 70) != (voltage_mv == -70):
        triggered.add(190)
    # 变异规则 263 - SRC
    if (voltage_mv == 70) != (not (voltage_mv == 70)):
        triggered.add(191)
    # 变异规则 264 - CRP
    if (voltage_mv == 70) != (voltage_mv == 71):
        triggered.add(192)
    # 变异规则 265 - CAR
    if (voltage_mv == 70) != (voltage_mv == 60):
        triggered.add(193)
    # 变异规则 266 - LCR
    if (voltage_mv == 70) != (voltage_mv == 69):
        triggered.add(194)
    # 变异规则 267 - SAR
    if (voltage_mv == 70) != (70 == voltage_mv):
        t=1
    # 变异规则 268 - SCR
    if (voltage_mv == 70) != (abs(voltage_mv) == 70):
        t=1
    # 变异规则 269 - UOI
    if (voltage_mv == 70) != (voltage_mv == -70):
        triggered.add(195)
    # 变异规则 270 - SVR
    if (voltage_mv == 70) != (speed == 70):
        triggered.add(196)
    # 原语句
    if voltage_mv == 70:
        health_score -= 20
    # 原语句28
    # 变异规则 271 - SVR
    if (altitude > 2) != (voltage_mv > 2):
        triggered.add(197)
    # 变异规则 272 - RSR
    if (altitude > 2) != (not (altitude > 2)):
        triggered.add(198)
    # 变异规则 273 - ABS
    if (altitude > 2) != (abs(altitude) > 2):
        t=1
    # 变异规则 274 - SCR
    if (altitude > 2) != (2 < altitude):
        t=1
    # 变异规则 275 - CRP
    if (altitude > 2) != (altitude > 1):
        triggered.add(199)
    # 变异规则 276 - UOI
    if (altitude > 2) != (altitude > 12):
        triggered.add(200)
    # 变异规则 277 - SRC
    if (altitude > 2) != (altitude > 1):
        triggered.add(201)
    # 变异规则 278 - SAR
    if (altitude > 2) != (2 < altitude):
        t=1
    # 变异规则 279 - ROR
    if (altitude > 2) != (altitude > -2):
        triggered.add(202)
    # 变异规则 280 - LCR
    if (altitude > 2) != (altitude > 12):
        triggered.add(203)
    # 原语句
    if altitude > 2:
        health_score -= 6
        altitude = max(altitude - 49, 2)
        speed = min(speed + 9, 100)
        voltage_mv = max(voltage_mv - 10, 2)
    # 原语句29
    # 变异规则 281 - SRC
    if (46 <= altitude <= 768) != (not (46 <= altitude <= 768)):
        triggered.add(204)
    # 变异规则 282 - AOR
    if (46 <= altitude <= 768) != (46 <= abs(altitude) <= 768):
        t=1
    # 变异规则 283 - RSR
    if (46 <= altitude <= 768) != (not (46 <= altitude <= 768)):
        triggered.add(205)
    # 变异规则 284 - ROR
    if (46 <= altitude <= 768) != (not (46 <= altitude <= 768)):
        triggered.add(206)
    # 变异规则 285 - UOI
    if (46 <= altitude <= 768) != (46 <= -altitude <= 768):
        triggered.add(207)
    # 变异规则 286 - SCR
    if (46 <= altitude <= 768) != (46 <= abs(altitude) <= 768):
        t=1
    # 变异规则 287 - CRP
    if (46 <= altitude <= 768) != (47 <= altitude <= 768):
        triggered.add(208)
    # 变异规则 288 - SAR
    if (46 <= altitude <= 768) != (altitude >= 46 <= 768):
        triggered.add(209)
    # 变异规则 289 - CSR
    if (46 <= altitude <= 768) != (-46 <= altitude <= 768):
        triggered.add(210)
    # 变异规则 290 - ABS
    if (46 <= altitude <= 768) != (46 <= abs(altitude) <= 768):
        t=1
    # 原语句
    if 46 <= altitude <= 768:
        health_score -= 30
        voltage_mv = max(voltage_mv - 1, 2)
    # 原语句30
    # 变异规则 291 - SAR
    if (altitude != 500 and altitude < 100) != (altitude != 500 and 100 > altitude):
        t=1
    # 变异规则 292 - AOR
    if (altitude != 500 and altitude < 100) != (not (altitude != 500 and altitude < 100)):
        triggered.add(211)
    # 变异规则 293 - CAR
    if (altitude != 500 and altitude < 100) != (altitude != 500 and altitude < 105):
        triggered.add(212)
    # 变异规则 294 - RSR
    if (altitude != 500 and altitude < 100) != (not (altitude != 500 and altitude < 100)):
        triggered.add(213)
    # 变异规则 295 - ABS
    if (altitude != 500 and altitude < 100) != (abs(altitude) != 500 and altitude < 100):
        t=1
    # 变异规则 296 - SCR
    if (altitude != 500 and altitude < 100) != (speed != 500 and altitude < 100):
        t=1
    # 变异规则 297 - SRC
    if (altitude != 500 and altitude < 100) != (altitude < 100 and altitude != 500):
        t=1
    # 变异规则 298 - SVR
    if (altitude != 500 and altitude < 100) != (voltage_mv != 500 and altitude < 100):
        triggered.add(214)
    # 变异规则 299 - CRP
    if (altitude != 500 and altitude < 100) != (altitude != 500 and altitude < 200):
        triggered.add(215)
    # 变异规则 300 - LCR
    if (altitude != 500 and altitude < 100) != (altitude != 500 or altitude < 100):
        triggered.add(216)
    # 原语句
    if altitude != 500 and altitude < 100:
        health_score -= 2
        voltage_mv = min(voltage_mv + 3, 100)
    return triggered

targetPaths = [
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 27, 29, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 27, 29, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 116, 122, 123, 124, 126, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 106, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 98, 100, 101, 103, 106, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 87, 89, 90, 93, 94, 100, 101, 103, 104, 106, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 51, 52, 60, 65, 70, 71, 76, 79, 85, 87, 89, 90, 93, 94, 100, 101, 103, 104, 106, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 144, 145, 148, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 110, 116, 122, 123, 124, 127, 130, 132, 141, 146, 150, 151, 154, 159, 161, 167, 177, 180, 182, 183, 185, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 55, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 110, 116, 118, 124, 127, 130, 141, 146, 148, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 55, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 110, 116, 118, 124, 127, 130, 141, 146, 148, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 210, 211},
    {3, 12, 14, 16, 21, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 55, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 110, 116, 118, 124, 127, 130, 141, 146, 148, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 210, 211},
    {3, 12, 14, 16, 20, 21, 22, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 55, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 110, 116, 118, 124, 127, 130, 141, 146, 148, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 48, 49, 52, 55, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 110, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 207, 208, 211},
    {3, 12, 14, 16, 23, 24, 25, 27, 29, 31, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 51, 52, 61, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 106, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 27, 29, 38, 42, 44, 47, 49, 51, 52, 62, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 51, 52, 60, 61, 62, 63, 64, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 110, 116, 118, 124, 127, 130, 141, 146, 148, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 31, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 122, 123, 124, 127, 130, 131, 132, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 122, 123, 124, 125, 126, 127, 128, 130, 131, 134, 141, 146, 150, 151, 153, 154, 155, 157, 159, 161, 167, 176, 179, 182, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 55, 60, 61, 62, 63, 64, 65, 68, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 118, 124, 127, 130, 141, 144, 146, 148, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 60, 65, 70, 71, 76, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 122, 123, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 177, 180, 182, 183, 185, 186, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 27, 29, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 122, 123, 124, 125, 127, 128, 130, 131, 141, 146, 150, 151, 153, 154, 155, 157, 159, 161, 167, 177, 178, 183, 191, 197, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 56, 58, 65, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 122, 123, 124, 125, 126, 127, 128, 130, 134, 141, 146, 150, 151, 153, 154, 155, 157, 159, 161, 167, 168, 171, 172, 174, 176, 179, 180, 183, 191, 197, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 124, 127, 130, 131, 132, 133, 134, 141, 146, 150, 151, 152, 154, 156, 159, 161, 167, 168, 171, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 60, 61, 62, 63, 64, 65, 68, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 144, 146, 150, 151, 154, 159, 161, 162, 167, 172, 177, 183, 191, 197, 198, 204, 207, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 60, 61, 62, 63, 64, 65, 68, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 144, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 207, 211, 212, 215, 216},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 119, 120, 123, 124, 127, 130, 141, 144, 146, 148, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 31, 38, 42, 44, 47, 49, 51, 52, 55, 65, 68, 69, 71, 72, 73, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 124, 127, 130, 131, 132, 133, 134, 141, 144, 146, 150, 151, 152, 154, 156, 159, 161, 167, 168, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 124, 127, 130, 131, 132, 133, 134, 141, 142, 144, 146, 150, 151, 152, 154, 156, 159, 161, 167, 168, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 124, 127, 130, 131, 132, 133, 134, 139, 141, 144, 146, 150, 151, 152, 154, 156, 159, 161, 167, 168, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 124, 127, 130, 131, 132, 133, 134, 136, 137, 138, 139, 141, 142, 144, 146, 150, 151, 152, 154, 156, 159, 161, 167, 168, 172, 174, 176, 180, 183, 191, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 145, 148, 150, 151, 152, 154, 156, 159, 161, 163, 167, 168, 172, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 145, 148, 150, 151, 152, 154, 156, 159, 160, 164, 167, 168, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 145, 148, 150, 151, 152, 154, 156, 159, 160, 164, 167, 168, 172, 174, 176, 180, 183, 191, 193, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 145, 147, 148, 150, 151, 152, 154, 156, 159, 160, 164, 167, 168, 172, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 145, 147, 148, 150, 151, 152, 154, 156, 159, 160, 164, 167, 168, 172, 174, 176, 180, 183, 191, 194, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 145, 147, 148, 150, 151, 152, 154, 156, 159, 160, 164, 167, 168, 172, 174, 176, 180, 183, 189, 190, 191, 193, 194, 196, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 43, 44, 47, 49, 52, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 102, 103, 107, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 143, 144, 150, 151, 152, 154, 156, 159, 160, 164, 167, 168, 172, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 94, 101, 103, 107, 110, 116, 124, 127, 130, 131, 132, 133, 134, 141, 144, 146, 150, 151, 152, 154, 156, 159, 161, 167, 168, 170, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 30, 31, 38, 42, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 93, 94, 101, 103, 107, 110, 116, 124, 127, 130, 131, 132, 133, 134, 141, 144, 146, 150, 151, 152, 154, 156, 159, 161, 167, 172, 173, 175, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 28, 29, 30, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 26, 27, 29, 31, 32, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 116, 122, 123, 124, 127, 130, 131, 133, 134, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 26, 27, 29, 31, 32, 38, 42, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 103, 107, 110, 115, 116, 117, 122, 123, 124, 127, 130, 132, 141, 146, 150, 151, 152, 154, 159, 161, 167, 172, 176, 179, 182, 183, 191, 198, 200, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 85, 87, 89, 90, 93, 94, 95, 96, 98, 99, 103, 109, 110, 114, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 198, 204, 207, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 85, 87, 89, 90, 93, 94, 95, 96, 97, 98, 99, 103, 109, 110, 114, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 198, 204, 207, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 84, 85, 87, 89, 90, 93, 94, 100, 103, 107, 110, 116, 122, 123, 124, 127, 130, 132, 141, 144, 145, 148, 150, 151, 154, 159, 161, 167, 173, 177, 180, 182, 183, 185, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 83, 85, 87, 88, 93, 94, 100, 103, 107, 110, 116, 122, 123, 124, 127, 130, 132, 141, 144, 145, 147, 148, 150, 151, 154, 159, 161, 167, 173, 177, 180, 182, 183, 185, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 56, 58, 65, 68, 69, 71, 72, 73, 75, 77, 78, 79, 85, 87, 88, 90, 93, 94, 103, 107, 110, 116, 124, 127, 130, 141, 143, 144, 150, 151, 154, 159, 161, 167, 172, 173, 177, 183, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 25, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 85, 87, 88, 93, 94, 100, 103, 107, 110, 116, 122, 123, 124, 127, 130, 132, 141, 143, 150, 151, 154, 159, 161, 165, 167, 173, 177, 180, 182, 183, 185, 191, 198, 204, 210, 211},
    {3, 12, 14, 16, 23, 24, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 85, 87, 88, 93, 94, 100, 103, 107, 108, 110, 116, 122, 123, 124, 127, 130, 132, 141, 143, 150, 151, 154, 159, 162, 164, 165, 167, 173, 177, 180, 182, 183, 191, 198, 204, 207, 211},
    {3, 12, 14, 16, 23, 24, 29, 38, 42, 44, 47, 49, 52, 54, 55, 56, 58, 65, 70, 71, 76, 79, 85, 87, 88, 93, 94, 100, 103, 109, 110, 112, 114, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 162, 167, 168, 171, 174, 177, 183, 191, 198, 204, 207, 211},
    {3, 12, 13, 14, 16, 23, 24, 28, 29, 30, 38, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 207, 211, 215, 216},
    {3, 10, 11, 12, 14, 19, 23, 24, 29, 30, 38, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 94, 100, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 207, 211, 215, 216},
    {1, 2, 3, 4, 5, 11, 12, 14, 19, 23, 24, 25, 27, 29, 31, 32, 38, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 100, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 207, 211, 216},
    {3, 11, 12, 14, 19, 23, 24, 28, 29, 30, 31, 38, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 93, 101, 102, 103, 107, 109, 110, 116, 123, 124, 127, 130, 136, 137, 138, 139, 141, 142, 143, 144, 150, 151, 152, 154, 156, 159, 160, 164, 167, 168, 172, 174, 176, 180, 183, 191, 197, 198, 199, 202, 204, 210, 211, 214},
    {3, 12, 14, 17, 18, 23, 24, 26, 29, 30, 32, 38, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 93, 100, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 207, 211, 216},
    {3, 12, 14, 17, 18, 23, 24, 29, 30, 38, 44, 47, 49, 51, 52, 55, 60, 61, 62, 63, 64, 65, 68, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 92, 93, 94, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 144, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 207, 211, 216},
    {3, 12, 14, 17, 18, 23, 24, 29, 30, 38, 44, 47, 49, 51, 52, 55, 60, 61, 62, 63, 64, 65, 68, 70, 71, 77, 78, 79, 82, 85, 86, 87, 90, 92, 93, 94, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 144, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 209, 211, 216},
    {3, 12, 14, 17, 18, 23, 24, 29, 30, 34, 44, 47, 49, 51, 52, 65, 70, 71, 76, 79, 85, 86, 87, 92, 93, 94, 100, 101, 102, 103, 107, 109, 110, 116, 118, 124, 127, 130, 141, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 209, 211, 216},
    {3, 12, 14, 17, 18, 23, 24, 25, 29, 34, 35, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 92, 93, 94, 101, 102, 103, 107, 109, 110, 116, 120, 123, 124, 127, 130, 141, 144, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 209, 211, 216},
    {3, 12, 14, 17, 18, 23, 24, 25, 29, 34, 40, 44, 47, 49, 51, 52, 55, 65, 70, 71, 77, 78, 79, 85, 86, 87, 90, 92, 93, 94, 101, 102, 103, 107, 109, 110, 116, 123, 124, 127, 130, 141, 144, 146, 150, 151, 154, 159, 161, 167, 172, 177, 183, 191, 197, 198, 204, 209, 211, 216},
    {3, 12, 14, 17, 18, 23, 24, 29, 35, 36, 37, 38, 40, 41, 42, 44, 47, 49, 52, 55, 65, 70, 71, 76, 79, 85, 87, 88, 93, 94, 100, 103, 109, 110, 114, 116, 118, 124, 127, 130, 141, 144, 145, 148, 150, 151, 154, 159, 161, 167, 172, 173, 175, 177, 183, 191, 193, 198, 204, 209, 211, 216}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 3:3, 4:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 12:11, 13:12, 14:13, 15:14, 16:15, 17:16, 18:17, 19:18, 20:19, 22:20, 23:21, 25:22, 26:23, 30:24, 31:25, 32:26, 33:27, 34:28, 35:29, 36:30, 37:31, 38:32, 39:33, 41:34, 42:35, 43:36, 45:37, 46:38, 47:39, 48:40, 50:41, 51:42, 53:43, 54:44, 55:45, 56:46, 57:47, 58:48, 59:49, 60:50, 61:51, 62:52, 63:53, 64:54, 65:55, 66:56, 67:57, 69:58, 70:59, 71:60, 73:61, 74:62, 76:63, 77:64, 78:65, 79:66, 80:67, 81:68, 83:69, 84:70, 86:71, 87:72, 88:73, 89:74, 90:75, 92:76, 94:77, 96:78, 97:79, 98:80, 99:81, 100:82, 101:83, 102:84, 103:85, 104:86, 106:87, 107:88, 108:89, 109:90, 110:91, 111:92, 118:93, 119:94, 121:95, 123:96, 125:97, 126:98, 127:99, 130:100, 131:101, 132:102, 134:103, 135:104, 136:105, 138:106, 141:107, 142:108, 143:109, 145:110, 146:111, 147:112, 148:113, 150:114, 154:115, 155:116, 156:117, 163:118, 164:119, 166:120, 167:121, 168:122, 169:123, 170:124, 171:125, 172:126, 173:127, 174:128, 175:129, 181:130, 184:131, 185:132, 188:133, 189:134, 190:135, 191:136, 192:137, 195:138, 196:139, 197:140, 199:141, 200:142, 201:143, 202:144, 203:145, 204:146, 205:147, 206:148, 207:149, 208:150, 209:151, 212:152, 213:153, 214:154, 215:155, 217:156, 218:157, 220:158, 221:159, 222:160, 223:161, 224:162, 225:163, 226:164, 227:165, 229:166, 231:167, 232:168, 233:169, 234:170, 235:171, 237:172, 238:173, 239:174, 240:175, 244:176, 247:177, 249:178, 250:179, 251:180, 252:181, 253:182, 254:183, 255:184, 256:185, 258:186, 259:187, 260:188, 261:189, 262:190, 263:191, 264:192, 265:193, 266:194, 269:195, 270:196, 271:197, 272:198, 275:199, 276:200, 277:201, 279:202, 280:203, 281:204, 283:205, 284:206, 285:207, 287:208, 288:209, 289:210, 292:211, 293:212, 294:213, 298:214, 299:215, 300:216}

    rule_expressions[1] = "(altitude // speed != 200) != (altitude // speed != 400)"
    rule_expressions[2] = "(altitude // speed != 200) != (altitude // -speed != 200)"
    rule_expressions[3] = "(altitude // speed != 200) != (not (altitude // speed != 200))"
    rule_expressions[4] = "(altitude // speed != 200) != (altitude // speed != -200)"
    rule_expressions[5] = "(altitude // speed != 200) != (voltage_mv // speed != 200)"
    rule_expressions[6] = "(altitude // speed != 200) != (altitude // speed != -200)"
    rule_expressions[7] = "(altitude // speed != 200) != (not (altitude // speed != 200))"
    rule_expressions[8] = "(altitude // speed != 200) != (voltage_mv // speed != 200)"
    rule_expressions[9] = "(altitude // speed != 200) != (altitude // speed != 400)"
    rule_expressions[10] = "(208 <= altitude <= 626) != (215 <= altitude <= 626)"
    rule_expressions[11] = "(208 <= altitude <= 626) != (208 <= speed <= 626)"
    rule_expressions[12] = "(208 <= altitude <= 626) != (not (208 <= altitude <= 626))"
    rule_expressions[13] = "(208 <= altitude <= 626) != (206 <= altitude <= 626)"
    rule_expressions[14] = "(208 <= altitude <= 626) != (not (208) <= altitude <= 626)"
    rule_expressions[15] = "(208 <= altitude <= 626) != (not (208 <= altitude <= 626))"
    rule_expressions[16] = "(208 <= altitude <= 626) != (-208 <= altitude <= 626)"
    rule_expressions[17] = "(208 <= altitude <= 626) != (altitude >= 208 <= 626)"
    rule_expressions[18] = "(208 <= altitude <= 626) != (208 <= altitude <= 1252)"
    rule_expressions[19] = "(208 <= altitude <= 626) != (208 <= altitude <= -626)"
    rule_expressions[20] = "(voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 and voltage_mv == -65)"
    rule_expressions[21] = "(voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 and voltage_mv == 64)"
    rule_expressions[22] = "(voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 and -voltage_mv == 65)"
    rule_expressions[23] = "(voltage_mv >= 2 and voltage_mv == 65) != (voltage_mv >= 2 or voltage_mv == 65)"
    rule_expressions[24] = "(voltage_mv >= 2 and voltage_mv == 65) != (not (voltage_mv >= 2 and voltage_mv == 65))"
    rule_expressions[25] = "(altitude % 10 < voltage_mv) != (altitude % voltage_mv > 10)"
    rule_expressions[26] = "(altitude % 10 < voltage_mv) != (altitude % 19 < voltage_mv)"
    rule_expressions[27] = "(altitude % 10 < voltage_mv) != (voltage_mv % 10 < voltage_mv)"
    rule_expressions[28] = "(altitude % 10 < voltage_mv) != (altitude % 5 < voltage_mv)"
    rule_expressions[29] = "(altitude % 10 < voltage_mv) != (not (altitude % 10 < voltage_mv))"
    rule_expressions[30] = "(altitude % 10 < voltage_mv) != (altitude % -10 < voltage_mv)"
    rule_expressions[31] = "(altitude % 10 < voltage_mv) != (speed % 10 < voltage_mv)"
    rule_expressions[32] = "(altitude % 10 < voltage_mv) != (altitude % 11 < voltage_mv)"
    rule_expressions[33] = "(altitude % 10 < voltage_mv) != (voltage_mv % 10 < voltage_mv)"
    rule_expressions[34] = "(altitude < 984 or voltage_mv == 72) != (voltage_mv < 984 or voltage_mv == 72)"
    rule_expressions[35] = "(altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == 36)"
    rule_expressions[36] = "(altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == 74)"
    rule_expressions[37] = "(altitude < 984 or voltage_mv == 72) != (altitude < 984 or -voltage_mv == 72)"
    rule_expressions[38] = "(altitude < 984 or voltage_mv == 72) != (altitude < 984 and voltage_mv == 72)"
    rule_expressions[39] = "(altitude < 984 or voltage_mv == 72) != (altitude < 984 or -voltage_mv == 72)"
    rule_expressions[40] = "(altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == 70)"
    rule_expressions[41] = "(altitude < 984 or voltage_mv == 72) != (altitude < 984 or voltage_mv == -72)"
    rule_expressions[42] = "(speed <= altitude * 48) != (altitude >= speed * 48)"
    rule_expressions[43] = "(speed <= altitude * 48) != (speed <= altitude * 24)"
    rule_expressions[44] = "(speed <= altitude * 48) != (speed <= altitude * -48)"
    rule_expressions[45] = "(speed <= altitude * 48) != (speed <= altitude * -48)"
    rule_expressions[46] = "(speed <= altitude * 48) != (altitude >= speed * 48)"
    rule_expressions[47] = "(speed <= altitude * 48) != (speed <= -altitude * 48)"
    rule_expressions[48] = "(speed <= altitude * 48) != (speed <= altitude * 46)"
    rule_expressions[49] = "(speed <= altitude * 48) != (not (speed <= altitude * 48))"
    rule_expressions[50] = "(speed <= altitude * 48) != (not (speed <= altitude * 48))"
    rule_expressions[51] = "(speed > 20) != (speed > -20)"
    rule_expressions[52] = "(speed > 20) != (not (speed > 20))"
    rule_expressions[53] = "(speed > 20) != (speed > -20)"
    rule_expressions[54] = "(speed > 20) != (speed > 40)"
    rule_expressions[55] = "(speed > 20) != (voltage_mv > 20)"
    rule_expressions[56] = "(speed > 20) != (speed > 21)"
    rule_expressions[57] = "(speed > 20) != (speed > -20)"
    rule_expressions[58] = "(speed > 20) != (speed > 27)"
    rule_expressions[59] = "(speed > 20) != (not (speed > 20))"
    rule_expressions[60] = "(speed * voltage_mv == 50) != (speed * voltage_mv == 40)"
    rule_expressions[61] = "(speed * voltage_mv == 50) != (speed * voltage_mv == 45)"
    rule_expressions[62] = "(speed * voltage_mv == 50) != (speed * voltage_mv == 25)"
    rule_expressions[63] = "(speed * voltage_mv == 50) != (speed * -voltage_mv == 50)"
    rule_expressions[64] = "(speed * voltage_mv == 50) != (speed * voltage_mv == -50)"
    rule_expressions[65] = "(speed * voltage_mv == 50) != (not (speed * voltage_mv == 50))"
    rule_expressions[66] = "(speed * voltage_mv == 50) != (speed * voltage_mv == -50)"
    rule_expressions[67] = "(speed * voltage_mv == 50) != (speed * -voltage_mv == 50)"
    rule_expressions[68] = "(speed == 96 or voltage_mv != 51) != (speed == 96 or voltage_mv != 25)"
    rule_expressions[69] = "(speed == 96 or voltage_mv != 51) != (speed == 96 or voltage_mv != -51)"
    rule_expressions[70] = "(speed == 96 or voltage_mv != 51) != (speed == 96 and voltage_mv != 51)"
    rule_expressions[71] = "(speed == 96 or voltage_mv != 51) != (not (speed == 96 or voltage_mv != 51))"
    rule_expressions[72] = "(speed == 96 or voltage_mv != 51) != (speed == 96 or voltage_mv != 56)"
    rule_expressions[73] = "(speed == 96 or voltage_mv != 51) != (speed == 96 or -voltage_mv != 51)"
    rule_expressions[74] = "(speed == 96 or voltage_mv != 51) != (speed == 96 and voltage_mv != 51)"
    rule_expressions[75] = "(speed == 96 or voltage_mv != 51) != (speed == 94 or voltage_mv != 51)"
    rule_expressions[76] = "(altitude <= 1000 and voltage_mv <= 20) != (altitude <= -1000 and voltage_mv <= 20)"
    rule_expressions[77] = "(altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 or voltage_mv <= 20)"
    rule_expressions[78] = "(altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 and -voltage_mv <= 20)"
    rule_expressions[79] = "(altitude <= 1000 and voltage_mv <= 20) != (not (altitude <= 1000 and voltage_mv <= 20))"
    rule_expressions[80] = "(altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 and -voltage_mv <= 20)"
    rule_expressions[81] = "(altitude <= 1000 and voltage_mv <= 20) != (not (altitude <= 1000 and voltage_mv <= 20))"
    rule_expressions[82] = "(altitude <= 1000 and voltage_mv <= 20) != (altitude <= 1000 and voltage_mv <= 25)"
    rule_expressions[83] = "(18 <= speed <= 76) != (18 <= speed <= 86)"
    rule_expressions[84] = "(18 <= speed <= 76) != (18 <= speed <= 69)"
    rule_expressions[85] = "(18 <= speed <= 76) != (not (18) <= speed <= 76)"
    rule_expressions[86] = "(18 <= speed <= 76) != (-18 <= speed <= 76)"
    rule_expressions[87] = "(18 <= speed <= 76) != (not (18 <= speed <= 76))"
    rule_expressions[88] = "(18 <= speed <= 76) != (speed >= 18 <= 76)"
    rule_expressions[89] = "(18 <= speed <= 76) != (18 <= -speed <= 76)"
    rule_expressions[90] = "(18 <= speed <= 76) != (18 <= voltage_mv <= 76)"
    rule_expressions[91] = "(18 <= speed <= 76) != (not (18 <= speed <= 76))"
    rule_expressions[92] = "(altitude >= 200 or altitude <= 696) != (speed >= 200 or altitude <= 696)"
    rule_expressions[93] = "(altitude >= 200 or altitude <= 696) != (not (altitude >= 200 or altitude <= 696))"
    rule_expressions[94] = "(altitude >= 200 or altitude <= 696) != (altitude >= 200 and altitude <= 696)"
    rule_expressions[95] = "(voltage_mv <= 5 and speed == 20) != (voltage_mv <= 5 and -speed == 20)"
    rule_expressions[96] = "(voltage_mv <= 5 and speed == 20) != (speed <= 5 and speed == 20)"
    rule_expressions[97] = "(voltage_mv <= 5 and speed == 20) != (voltage_mv <= 3 and speed == 20)"
    rule_expressions[98] = "(voltage_mv <= 5 and speed == 20) != (voltage_mv <= 5 and speed == 13)"
    rule_expressions[99] = "(voltage_mv <= 5 and speed == 20) != (altitude <= 5 and speed == 20)"
    rule_expressions[100] = "(voltage_mv <= 5 and speed == 20) != (voltage_mv <= 5 or speed == 20)"
    rule_expressions[101] = "(speed >= 20) != (speed >= -20)"
    rule_expressions[102] = "(speed >= 20) != (altitude >= 20)"
    rule_expressions[103] = "(speed >= 20) != (not (speed >= 20))"
    rule_expressions[104] = "(speed >= 20) != (speed >= 17)"
    rule_expressions[105] = "(speed >= 20) != (altitude >= 20)"
    rule_expressions[106] = "(speed >= 20) != (speed >= 10)"
    rule_expressions[107] = "(speed < 100) != (speed < -100)"
    rule_expressions[108] = "(speed < 100) != (speed < 99)"
    rule_expressions[109] = "(speed < 100) != (altitude < 100)"
    rule_expressions[110] = "(speed < 100) != (not (speed < 100))"
    rule_expressions[111] = "(speed < 100) != (speed < -100)"
    rule_expressions[112] = "(speed < 100) != (speed < 101)"
    rule_expressions[113] = "(speed < 100) != (speed < 101)"
    rule_expressions[114] = "(speed < 100) != (voltage_mv < 100)"
    rule_expressions[115] = "(speed == 5 and altitude > 194) != (speed == 5 and altitude > -194)"
    rule_expressions[116] = "(speed == 5 and altitude > 194) != (not (speed == 5 and altitude > 194))"
    rule_expressions[117] = "(speed == 5 and altitude > 194) != (speed == 5 or altitude > 194)"
    rule_expressions[118] = "(voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 and -speed > 30)"
    rule_expressions[119] = "(voltage_mv <= 20 and speed > 30) != (voltage_mv <= 22 and speed > 30)"
    rule_expressions[120] = "(voltage_mv <= 20 and speed > 30) != (voltage_mv <= 40 and speed > 30)"
    rule_expressions[121] = "(voltage_mv <= 20 and speed > 30) != (voltage_mv <= 22 and speed > 30)"
    rule_expressions[122] = "(voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 and speed > -30)"
    rule_expressions[123] = "(voltage_mv <= 20 and speed > 30) != (voltage_mv <= 20 or speed > 30)"
    rule_expressions[124] = "(voltage_mv <= 20 and speed > 30) != (not (voltage_mv <= 20 and speed > 30))"
    rule_expressions[125] = "(voltage_mv != 10) != (voltage_mv != 20)"
    rule_expressions[126] = "(voltage_mv != 10) != (altitude != 10)"
    rule_expressions[127] = "(voltage_mv != 10) != (not (voltage_mv != 10))"
    rule_expressions[128] = "(voltage_mv != 10) != (voltage_mv != 11)"
    rule_expressions[129] = "(voltage_mv != 10) != (voltage_mv != 11)"
    rule_expressions[130] = "(altitude != 2) != (not (altitude != 2))"
    rule_expressions[131] = "(altitude != 2) != (speed != 2)"
    rule_expressions[132] = "(altitude != 2) != (voltage_mv != 2)"
    rule_expressions[133] = "(altitude != 2) != (altitude != 4)"
    rule_expressions[134] = "(altitude != 2) != (altitude != 7)"
    rule_expressions[135] = "(altitude != 2) != (altitude != 7)"
    rule_expressions[136] = "(voltage_mv == 50) != (voltage_mv == -50)"
    rule_expressions[137] = "(voltage_mv == 50) != (voltage_mv == 100)"
    rule_expressions[138] = "(voltage_mv == 50) != (voltage_mv == 57)"
    rule_expressions[139] = "(voltage_mv == 50) != (voltage_mv == 49)"
    rule_expressions[140] = "(voltage_mv == 50) != (voltage_mv == -50)"
    rule_expressions[141] = "(voltage_mv == 50) != (not (voltage_mv == 50))"
    rule_expressions[142] = "(voltage_mv == 50) != (voltage_mv == 45)"
    rule_expressions[143] = "(24 <= speed <= 86) != (speed >= 24 <= 86)"
    rule_expressions[144] = "(24 <= speed <= 86) != (24 <= voltage_mv <= 86)"
    rule_expressions[145] = "(24 <= speed <= 86) != (24 <= -speed <= 86)"
    rule_expressions[146] = "(24 <= speed <= 86) != (-24 <= speed <= 86)"
    rule_expressions[147] = "(24 <= speed <= 86) != (24 <= speed <= 76)"
    rule_expressions[148] = "(24 <= speed <= 86) != (24 <= altitude <= 86)"
    rule_expressions[149] = "(24 <= speed <= 86) != (24 <= -speed <= 86)"
    rule_expressions[150] = "(24 <= speed <= 86) != (not (24) <= speed <= 86)"
    rule_expressions[151] = "(24 <= speed <= 86) != (not (24 <= speed <= 86))"
    rule_expressions[152] = "(altitude > 20 or altitude > 5) != (altitude > 20 or altitude > 1)"
    rule_expressions[153] = "(altitude > 20 or altitude > 5) != (altitude > 20 or altitude > 14)"
    rule_expressions[154] = "(altitude > 20 or altitude > 5) != (not (altitude > 20 or altitude > 5))"
    rule_expressions[155] = "(altitude > 20 or altitude > 5) != (altitude > 20 or -altitude > 5)"
    rule_expressions[156] = "(altitude > 20 or altitude > 5) != (voltage_mv > 20 or altitude > 5)"
    rule_expressions[157] = "(altitude > 20 or altitude > 5) != (altitude > 20 or altitude > 10)"
    rule_expressions[158] = "(altitude > 20 or altitude > 5) != (not (altitude > 20 or altitude > 5))"
    rule_expressions[159] = "(voltage_mv != 100 and speed <= 56) != (not (voltage_mv != 100 and speed <= 56))"
    rule_expressions[160] = "(voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and -speed <= 56)"
    rule_expressions[161] = "(voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and speed <= -56)"
    rule_expressions[162] = "(voltage_mv != 100 and speed <= 56) != (altitude != 100 and speed <= 56)"
    rule_expressions[163] = "(voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and speed <= 53)"
    rule_expressions[164] = "(voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 or speed <= 56)"
    rule_expressions[165] = "(voltage_mv != 100 and speed <= 56) != (voltage_mv != 99 and speed <= 56)"
    rule_expressions[166] = "(voltage_mv != 100 and speed <= 56) != (voltage_mv != 100 and -speed <= 56)"
    rule_expressions[167] = "(13 <= voltage_mv <= 59) != (not (13 <= voltage_mv <= 59))"
    rule_expressions[168] = "(13 <= voltage_mv <= 59) != (13 <= -voltage_mv <= 59)"
    rule_expressions[169] = "(13 <= voltage_mv <= 59) != (not (13 <= voltage_mv <= 59))"
    rule_expressions[170] = "(13 <= voltage_mv <= 59) != (13 <= voltage_mv <= 54)"
    rule_expressions[171] = "(13 <= voltage_mv <= 59) != (26 <= voltage_mv <= 59)"
    rule_expressions[172] = "(13 <= voltage_mv <= 59) != (13 <= speed <= 59)"
    rule_expressions[173] = "(13 <= voltage_mv <= 59) != (voltage_mv >= 13 <= 59)"
    rule_expressions[174] = "(13 <= voltage_mv <= 59) != (13 <= voltage_mv <= -59)"
    rule_expressions[175] = "(13 <= voltage_mv <= 59) != (13 <= voltage_mv <= 64)"
    rule_expressions[176] = "(voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 and altitude < 10)"
    rule_expressions[177] = "(voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 or -altitude < 10)"
    rule_expressions[178] = "(voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 or altitude < 11)"
    rule_expressions[179] = "(voltage_mv < 2 or altitude < 10) != (voltage_mv < 2 or altitude < 5)"
    rule_expressions[180] = "(speed < 10) != (altitude < 10)"
    rule_expressions[181] = "(speed < 10) != (altitude < 10)"
    rule_expressions[182] = "(speed < 10) != (speed < -10)"
    rule_expressions[183] = "(speed < 10) != (not (speed < 10))"
    rule_expressions[184] = "(speed < 10) != (altitude < 10)"
    rule_expressions[185] = "(speed < 10) != (speed < 5)"
    rule_expressions[186] = "(speed < 10) != (speed < 9)"
    rule_expressions[187] = "(speed < 10) != (speed < 5)"
    rule_expressions[188] = "(speed < 10) != (not (speed < 10))"
    rule_expressions[189] = "(voltage_mv == 70) != (voltage_mv == 71)"
    rule_expressions[190] = "(voltage_mv == 70) != (voltage_mv == -70)"
    rule_expressions[191] = "(voltage_mv == 70) != (not (voltage_mv == 70))"
    rule_expressions[192] = "(voltage_mv == 70) != (voltage_mv == 71)"
    rule_expressions[193] = "(voltage_mv == 70) != (voltage_mv == 60)"
    rule_expressions[194] = "(voltage_mv == 70) != (voltage_mv == 69)"
    rule_expressions[195] = "(voltage_mv == 70) != (voltage_mv == -70)"
    rule_expressions[196] = "(voltage_mv == 70) != (speed == 70)"
    rule_expressions[197] = "(altitude > 2) != (voltage_mv > 2)"
    rule_expressions[198] = "(altitude > 2) != (not (altitude > 2))"
    rule_expressions[199] = "(altitude > 2) != (altitude > 1)"
    rule_expressions[200] = "(altitude > 2) != (altitude > 12)"
    rule_expressions[201] = "(altitude > 2) != (altitude > 1)"
    rule_expressions[202] = "(altitude > 2) != (altitude > -2)"
    rule_expressions[203] = "(altitude > 2) != (altitude > 12)"
    rule_expressions[204] = "(46 <= altitude <= 768) != (not (46 <= altitude <= 768))"
    rule_expressions[205] = "(46 <= altitude <= 768) != (not (46 <= altitude <= 768))"
    rule_expressions[206] = "(46 <= altitude <= 768) != (not (46 <= altitude <= 768))"
    rule_expressions[207] = "(46 <= altitude <= 768) != (46 <= -altitude <= 768)"
    rule_expressions[208] = "(46 <= altitude <= 768) != (47 <= altitude <= 768)"
    rule_expressions[209] = "(46 <= altitude <= 768) != (altitude >= 46 <= 768)"
    rule_expressions[210] = "(46 <= altitude <= 768) != (-46 <= altitude <= 768)"
    rule_expressions[211] = "(altitude != 500 and altitude < 100) != (not (altitude != 500 and altitude < 100))"
    rule_expressions[212] = "(altitude != 500 and altitude < 100) != (altitude != 500 and altitude < 105)"
    rule_expressions[213] = "(altitude != 500 and altitude < 100) != (not (altitude != 500 and altitude < 100))"
    rule_expressions[214] = "(altitude != 500 and altitude < 100) != (voltage_mv != 500 and altitude < 100)"
    rule_expressions[215] = "(altitude != 500 and altitude < 100) != (altitude != 500 and altitude < 200)"
    rule_expressions[216] = "(altitude != 500 and altitude < 100) != (altitude != 500 or altitude < 100)"

    return rule_expressions