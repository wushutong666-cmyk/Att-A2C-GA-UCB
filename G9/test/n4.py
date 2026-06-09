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
    if (speed == 47 and altitude >= 2) != (not (speed == 47 and altitude >= 2)):
        triggered.add(1)
    # 变异规则 2 - ROR
    if (speed == 47 and altitude >= 2) != (altitude == 47 and altitude >= 2):
        triggered.add(2)
    # 变异规则 3 - UOI
    if (speed == 47 and altitude >= 2) != (speed == 47 and -altitude >= 2):
        triggered.add(3)
    # 变异规则 4 - CRP
    if (speed == 47 and altitude >= 2) != (speed == 47 and altitude >= 8):
        triggered.add(4)
    # 变异规则 5 - ABS
    if (speed == 47 and altitude >= 2) != (speed == 47 and abs(altitude) >= 2):
        t=1
    # 变异规则 6 - AOR
    if (speed == 47 and altitude >= 2) != (speed == 47 and abs(altitude) >= 2):
        t=1
    # 变异规则 7 - CAR
    if (speed == 47 and altitude >= 2) != (speed == 47 and altitude >= 4):
        triggered.add(5)
    # 变异规则 8 - SCR
    if (speed == 47 and altitude >= 2) != (speed == -47 and altitude >= 2):
        triggered.add(6)
    # 变异规则 9 - SAR
    if (speed == 47 and altitude >= 2) != (speed == 47 and 2 <= altitude):
        t=1
    # 变异规则 10 - CSR
    if (speed == 47 and altitude >= 2) != (speed == 47 and altitude >= -2):
        t=1
    # 原语句
    if speed == 47 and altitude >= 2:
        health_score -= 5
    # 原语句2
    # 变异规则 11 - AOR
    if (voltage_mv + speed > 2) != (voltage_mv + speed > 7):
        triggered.add(7)
    # 变异规则 12 - SVR
    if (voltage_mv + speed > 2) != (altitude + speed > 2):
        t=1
    # 变异规则 13 - CAR
    if (voltage_mv + speed > 2) != (voltage_mv + speed > 12):
        triggered.add(8)
    # 变异规则 14 - SAR
    if (voltage_mv + speed > 2) != (voltage_mv + 2 < speed):
        triggered.add(9)
    # 变异规则 15 - UOI
    if (voltage_mv + speed > 2) != (voltage_mv + -speed > 2):
        triggered.add(10)
    # 变异规则 16 - SRC
    if (voltage_mv + speed > 2) != (voltage_mv + 2 < speed):
        triggered.add(11)
    # 变异规则 17 - CSR
    if (voltage_mv + speed > 2) != (voltage_mv + speed > -2):
        t=1
    # 变异规则 18 - SCR
    if (voltage_mv + speed > 2) != (speed + speed > 2):
        t=1
    # 变异规则 19 - ROR
    if (voltage_mv + speed > 2) != (not (voltage_mv + speed > 2)):
        triggered.add(12)
    # 变异规则 20 - ABS
    if (voltage_mv + speed > 2) != (voltage_mv + abs(speed) > 2):
        t=1
    # 原语句
    if voltage_mv + speed > 2:
        health_score += 18
        voltage_mv = min(voltage_mv + 6, 100)
    # 原语句3
    # 变异规则 21 - UOI
    if (altitude >= 500 and altitude != 500) != (altitude >= 500 and -altitude != 500):
        triggered.add(13)
    # 变异规则 22 - ABS
    if (altitude >= 500 and altitude != 500) != (abs(altitude) >= 500 and altitude != 500):
        t=1
    # 变异规则 23 - RSR
    if (altitude >= 500 and altitude != 500) != (not (altitude >= 500 and altitude != 500)):
        triggered.add(14)
    # 变异规则 24 - SAR
    if (altitude >= 500 and altitude != 500) != (500 <= altitude and altitude != 500):
        t=1
    # 变异规则 25 - LCR
    if (altitude >= 500 and altitude != 500) != (altitude >= 500 or altitude != 500):
        triggered.add(15)
    # 变异规则 26 - SCR
    if (altitude >= 500 and altitude != 500) != (altitude >= 500 or altitude != 500):
        triggered.add(16)
    # 变异规则 27 - ROR
    if (altitude >= 500 and altitude != 500) != (altitude >= 500 and altitude != -500):
        triggered.add(17)
    # 变异规则 28 - CSR
    if (altitude >= 500 and altitude != 500) != (altitude >= 500 and altitude != -500):
        triggered.add(18)
    # 变异规则 29 - CRP
    if (altitude >= 500 and altitude != 500) != (altitude >= 250 and altitude != 500):
        triggered.add(19)
    # 变异规则 30 - CAR
    if (altitude >= 500 and altitude != 500) != (altitude >= 500 and altitude != 502):
        triggered.add(20)
    # 原语句
    if altitude >= 500 and altitude != 500:
        health_score -= 18
    # 原语句4
    # 变异规则 31 - CAR
    if (voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 19 and voltage_mv > 5):
        triggered.add(21)
    # 变异规则 32 - SCR
    if (voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 20 and -voltage_mv > 5):
        triggered.add(22)
    # 变异规则 33 - AOR
    if (voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 30 and voltage_mv > 5):
        triggered.add(23)
    # 变异规则 34 - CSR
    if (voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 20 and voltage_mv > -5):
        t=1
    # 变异规则 35 - CRP
    if (voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 40 and voltage_mv > 5):
        triggered.add(24)
    # 变异规则 36 - LCR
    if (voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 20 or voltage_mv > 5):
        triggered.add(25)
    # 变异规则 37 - ABS
    if (voltage_mv < 20 and voltage_mv > 5) != (abs(voltage_mv) < 20 and voltage_mv > 5):
        t=1
    # 变异规则 38 - RSR
    if (voltage_mv < 20 and voltage_mv > 5) != (not (voltage_mv < 20 and voltage_mv > 5)):
        triggered.add(26)
    # 变异规则 39 - SRC
    if (voltage_mv < 20 and voltage_mv > 5) != (voltage_mv > 5 and voltage_mv < 20):
        t=1
    # 变异规则 40 - SAR
    if (voltage_mv < 20 and voltage_mv > 5) != (20 > voltage_mv and voltage_mv > 5):
        t=1
    # 原语句
    if voltage_mv < 20 and voltage_mv > 5:
        health_score -= 24
        speed = min(speed + 2, 100)
    # 原语句5
    # 变异规则 41 - RSR
    if (voltage_mv == 30 and voltage_mv <= 30) != (not (voltage_mv == 30 and voltage_mv <= 30)):
        triggered.add(27)
    # 变异规则 42 - SVR
    if (voltage_mv == 30 and voltage_mv <= 30) != (altitude == 30 and voltage_mv <= 30):
        triggered.add(28)
    # 变异规则 43 - UOI
    if (voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 and -voltage_mv <= 30):
        t=1
    # 变异规则 44 - CRP
    if (voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 and voltage_mv <= 60):
        t=1
    # 变异规则 45 - SRC
    if (voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv <= 30 and voltage_mv == 30):
        t=1
    # 变异规则 46 - CSR
    if (voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 and voltage_mv <= -30):
        triggered.add(29)
    # 变异规则 47 - LCR
    if (voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 or voltage_mv <= 30):
        triggered.add(30)
    # 变异规则 48 - ABS
    if (voltage_mv == 30 and voltage_mv <= 30) != (abs(voltage_mv) == 30 and voltage_mv <= 30):
        t=1
    # 变异规则 49 - CAR
    if (voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 and voltage_mv <= 40):
        t=1
    # 变异规则 50 - AOR
    if (voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 or voltage_mv <= 30):
        triggered.add(31)
    # 原语句
    if voltage_mv == 30 and voltage_mv <= 30:
        health_score -= 21
    # 原语句6
    # 变异规则 51 - SRC
    if (voltage_mv * 10 == speed) != (voltage_mv * -10 == speed):
        triggered.add(32)
    # 变异规则 52 - CSR
    if (voltage_mv * 10 == speed) != (voltage_mv * -10 == speed):
        triggered.add(33)
    # 变异规则 53 - RSR
    if (voltage_mv * 10 == speed) != (not (voltage_mv * 10 == speed)):
        triggered.add(34)
    # 变异规则 54 - AOR
    if (voltage_mv * 10 == speed) != (voltage_mv * 10 == -speed):
        triggered.add(35)
    # 变异规则 55 - CRP
    if (voltage_mv * 10 == speed) != (voltage_mv * 20 == speed):
        triggered.add(36)
    # 变异规则 56 - SAR
    if (voltage_mv * 10 == speed) != (voltage_mv * speed == 10):
        triggered.add(37)
    # 变异规则 57 - SVR
    if (voltage_mv * 10 == speed) != (speed * 10 == speed):
        triggered.add(38)
    # 变异规则 58 - ABS
    if (voltage_mv * 10 == speed) != (voltage_mv * 10 == abs(speed)):
        t=1
    # 变异规则 59 - ROR
    if (voltage_mv * 10 == speed) != (speed * 10 == speed):
        triggered.add(39)
    # 变异规则 60 - SCR
    if (voltage_mv * 10 == speed) != (speed * 10 == speed):
        triggered.add(40)
    # 原语句
    if voltage_mv * 10 == speed:
        health_score -= 12
        speed = min(speed + 5, 100)
    # 原语句7
    # 变异规则 61 - SRC
    if (altitude == 305) != (not (altitude == 305)):
        triggered.add(41)
    # 变异规则 62 - UOI
    if (altitude == 305) != (not (altitude == 305)):
        triggered.add(42)
    # 变异规则 63 - CAR
    if (altitude == 305) != (altitude == 303):
        triggered.add(43)
    # 变异规则 64 - CRP
    if (altitude == 305) != (altitude == 152):
        triggered.add(44)
    # 变异规则 65 - CSR
    if (altitude == 305) != (altitude == -305):
        triggered.add(45)
    # 变异规则 66 - SAR
    if (altitude == 305) != (305 == altitude):
        t=1
    # 变异规则 67 - RSR
    if (altitude == 305) != (not (altitude == 305)):
        triggered.add(46)
    # 变异规则 68 - ROR
    if (altitude == 305) != (altitude == 303):
        triggered.add(47)
    # 变异规则 69 - LCR
    if (altitude == 305) != (voltage_mv == 305):
        triggered.add(48)
    # 变异规则 70 - AOR
    if (altitude == 305) != (altitude == 304):
        triggered.add(49)
    # 原语句
    if altitude == 305:
        health_score -= 20
        speed = max(speed - 9, 2)
        voltage_mv, speed = speed, voltage_mv
    # 原语句8
    # 变异规则 71 - SRC
    if (speed > 28) != (speed > -28):
        triggered.add(50)
    # 变异规则 72 - SCR
    if (speed > 28) != (not (speed > 28)):
        triggered.add(51)
    # 变异规则 73 - ABS
    if (speed > 28) != (abs(speed) > 28):
        t=1
    # 变异规则 74 - CAR
    if (speed > 28) != (speed > 23):
        triggered.add(52)
    # 变异规则 75 - CRP
    if (speed > 28) != (speed > 29):
        triggered.add(53)
    # 变异规则 76 - SAR
    if (speed > 28) != (28 < speed):
        t=1
    # 变异规则 77 - ROR
    if (speed > 28) != (altitude > 28):
        triggered.add(54)
    # 变异规则 78 - AOR
    if (speed > 28) != (speed > 29):
        triggered.add(55)
    # 变异规则 79 - RSR
    if (speed > 28) != (not (speed > 28)):
        triggered.add(56)
    # 变异规则 80 - CSR
    if (speed > 28) != (speed > -28):
        triggered.add(57)
    # 原语句
    if speed > 28:
        health_score += 12
        voltage_mv = max(voltage_mv - 9, 2)
    # 原语句9
    # 变异规则 81 - CRP
    if (voltage_mv < altitude - 10) != (voltage_mv < altitude - 4):
        triggered.add(58)
    # 变异规则 82 - RSR
    if (voltage_mv < altitude - 10) != (not (voltage_mv < altitude - 10)):
        triggered.add(59)
    # 变异规则 83 - AOR
    if (voltage_mv < altitude - 10) != (voltage_mv < altitude - 20):
        triggered.add(60)
    # 变异规则 84 - CSR
    if (voltage_mv < altitude - 10) != (voltage_mv < altitude - -10):
        triggered.add(61)
    # 变异规则 85 - SCR
    if (voltage_mv < altitude - 10) != (altitude > voltage_mv - 10):
        triggered.add(62)
    # 变异规则 86 - SRC
    if (voltage_mv < altitude - 10) != (voltage_mv < altitude - 14):
        triggered.add(63)
    # 变异规则 87 - SAR
    if (voltage_mv < altitude - 10) != (altitude > voltage_mv - 10):
        triggered.add(64)
    # 变异规则 88 - UOI
    if (voltage_mv < altitude - 10) != (voltage_mv < -altitude - 10):
        triggered.add(65)
    # 变异规则 89 - SVR
    if (voltage_mv < altitude - 10) != (speed < altitude - 10):
        triggered.add(66)
    # 变异规则 90 - ROR
    if (voltage_mv < altitude - 10) != (voltage_mv < abs(altitude) - 10):
        t=1
    # 原语句
    if voltage_mv < altitude - 10:
        health_score -= 10
        altitude = max(altitude - 31, 2)
        speed = min(speed + 8, 100)
        voltage_mv = min(voltage_mv + 1, 100)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句10
    # 变异规则 91 - CRP
    if (speed + 3 == voltage_mv) != (speed + 1 == voltage_mv):
        triggered.add(67)
    # 变异规则 92 - SCR
    if (speed + 3 == voltage_mv) != (altitude + 3 == voltage_mv):
        triggered.add(68)
    # 变异规则 93 - SRC
    if (speed + 3 == voltage_mv) != (speed + 9 == voltage_mv):
        triggered.add(69)
    # 变异规则 94 - LCR
    if (speed + 3 == voltage_mv) != (not (speed + 3 == voltage_mv)):
        triggered.add(70)
    # 变异规则 95 - AOR
    if (speed + 3 == voltage_mv) != (speed + 3 == -voltage_mv):
        triggered.add(71)
    # 变异规则 96 - ROR
    if (speed + 3 == voltage_mv) != (not (speed + 3 == voltage_mv)):
        triggered.add(72)
    # 变异规则 97 - CSR
    if (speed + 3 == voltage_mv) != (speed + -3 == voltage_mv):
        triggered.add(73)
    # 变异规则 98 - SAR
    if (speed + 3 == voltage_mv) != (speed + voltage_mv == 3):
        triggered.add(74)
    # 变异规则 99 - RSR
    if (speed + 3 == voltage_mv) != (not (speed + 3 == voltage_mv)):
        triggered.add(75)
    # 变异规则 100 - ABS
    if (speed + 3 == voltage_mv) != (abs(speed) + 3 == voltage_mv):
        t=1
    # 原语句
    if speed + 3 == voltage_mv:
        health_score += 6
        speed = max(speed - 6, 2)
        voltage_mv = max(voltage_mv - 1, 2)
    # 原语句11
    # 变异规则 101 - SCR
    if (altitude >= 1000) != (altitude >= 1010):
        t=1
    # 变异规则 102 - CSR
    if (altitude >= 1000) != (altitude >= -1000):
        triggered.add(76)
    # 变异规则 103 - LCR
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 变异规则 104 - UOI
    if (altitude >= 1000) != (voltage_mv >= 1000):
        t=1
    # 变异规则 105 - SVR
    if (altitude >= 1000) != (speed >= 1000):
        t=1
    # 变异规则 106 - SRC
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 变异规则 107 - SAR
    if (altitude >= 1000) != (1000 <= altitude):
        t=1
    # 变异规则 108 - ROR
    if (altitude >= 1000) != (altitude >= 1001):
        t=1
    # 变异规则 109 - CRP
    if (altitude >= 1000) != (altitude >= 1009):
        t=1
    # 变异规则 110 - CAR
    if (altitude >= 1000) != (altitude >= 995):
        t=1
    # 原语句
    if altitude >= 1000:
        health_score -= 12
    # 原语句12
    # 变异规则 111 - ROR
    if (voltage_mv != 39) != (abs(voltage_mv) != 39):
        t=1
    # 变异规则 112 - RSR
    if (voltage_mv != 39) != (not (voltage_mv != 39)):
        triggered.add(77)
    # 变异规则 113 - SCR
    if (voltage_mv != 39) != (voltage_mv != 44):
        triggered.add(78)
    # 变异规则 114 - UOI
    if (voltage_mv != 39) != (voltage_mv != 40):
        triggered.add(79)
    # 变异规则 115 - LCR
    if (voltage_mv != 39) != (voltage_mv != 19):
        triggered.add(80)
    # 变异规则 116 - CSR
    if (voltage_mv != 39) != (voltage_mv != -39):
        triggered.add(81)
    # 变异规则 117 - CRP
    if (voltage_mv != 39) != (voltage_mv != 19):
        triggered.add(82)
    # 变异规则 118 - SAR
    if (voltage_mv != 39) != (39 != voltage_mv):
        t=1
    # 变异规则 119 - AOR
    if (voltage_mv != 39) != (39 != voltage_mv):
        t=1
    # 变异规则 120 - SVR
    if (voltage_mv != 39) != (speed != 39):
        triggered.add(83)
    # 原语句
    if voltage_mv != 39:
        health_score -= 29
    # 原语句13
    # 变异规则 121 - SRC
    if (voltage_mv - speed <= 10) != (speed - speed <= 10):
        triggered.add(84)
    # 变异规则 122 - ABS
    if (voltage_mv - speed <= 10) != (voltage_mv - abs(speed) <= 10):
        t=1
    # 变异规则 123 - ROR
    if (voltage_mv - speed <= 10) != (voltage_mv - speed <= 5):
        triggered.add(85)
    # 变异规则 124 - UOI
    if (voltage_mv - speed <= 10) != (voltage_mv - speed <= 11):
        triggered.add(86)
    # 变异规则 125 - SAR
    if (voltage_mv - speed <= 10) != (voltage_mv - 10 >= speed):
        triggered.add(87)
    # 变异规则 126 - AOR
    if (voltage_mv - speed <= 10) != (voltage_mv - speed <= 9):
        triggered.add(88)
    # 变异规则 127 - SCR
    if (voltage_mv - speed <= 10) != (voltage_mv - 10 >= speed):
        triggered.add(89)
    # 变异规则 128 - RSR
    if (voltage_mv - speed <= 10) != (not (voltage_mv - speed <= 10)):
        triggered.add(90)
    # 变异规则 129 - CAR
    if (voltage_mv - speed <= 10) != (voltage_mv - speed <= 15):
        triggered.add(91)
    # 变异规则 130 - SVR
    if (voltage_mv - speed <= 10) != (speed - speed <= 10):
        triggered.add(92)
    # 原语句
    if voltage_mv - speed <= 10:
        health_score += 8
        speed = max(speed - 5, 2)
    # 原语句14
    # 变异规则 131 - RSR
    if (speed > 87 and speed < 7) != (not (speed > 87 and speed < 7)):
        triggered.add(93)
    # 变异规则 132 - ABS
    if (speed > 87 and speed < 7) != (abs(speed) > 87 and speed < 7):
        t=1
    # 变异规则 133 - SAR
    if (speed > 87 and speed < 7) != (speed > 87 and 7 > speed):
        t=1
    # 变异规则 134 - SCR
    if (speed > 87 and speed < 7) != (speed > 87 or speed < 7):
        triggered.add(94)
    # 变异规则 135 - SRC
    if (speed > 87 and speed < 7) != (speed < 7 and speed > 87):
        t=1
    # 变异规则 136 - UOI
    if (speed > 87 and speed < 7) != (speed > 87 and -speed < 7):
        triggered.add(95)
    # 变异规则 137 - AOR
    if (speed > 87 and speed < 7) != (speed > 87 and speed < 17):
        t=1
    # 变异规则 138 - LCR
    if (speed > 87 and speed < 7) != (speed > 87 or speed < 7):
        triggered.add(96)
    # 变异规则 139 - ROR
    if (speed > 87 and speed < 7) != (speed > -87 and speed < 7):
        triggered.add(97)
    # 变异规则 140 - CRP
    if (speed > 87 and speed < 7) != (speed > 174 and speed < 7):
        t=1
    # 原语句
    if speed > 87 and speed < 7:
        health_score += 16
        speed = max(speed - 5, 2)
    # 原语句15
    # 变异规则 141 - CSR
    if (altitude < 128 or speed != 30) != (altitude < -128 or speed != 30):
        triggered.add(98)
    # 变异规则 142 - LCR
    if (altitude < 128 or speed != 30) != (altitude < 128 and speed != 30):
        triggered.add(99)
    # 变异规则 143 - CAR
    if (altitude < 128 or speed != 30) != (altitude < 128 or speed != 29):
        t=1
    # 变异规则 144 - CRP
    if (altitude < 128 or speed != 30) != (altitude < 128 or speed != 36):
        t=1
    # 变异规则 145 - SVR
    if (altitude < 128 or speed != 30) != (speed < 128 or speed != 30):
        t=1
    # 变异规则 146 - AOR
    if (altitude < 128 or speed != 30) != (voltage_mv < 128 or speed != 30):
        triggered.add(100)
    # 变异规则 147 - SAR
    if (altitude < 128 or speed != 30) != (128 > altitude or speed != 30):
        t=1
    # 变异规则 148 - ABS
    if (altitude < 128 or speed != 30) != (abs(altitude) < 128 or speed != 30):
        t=1
    # 变异规则 149 - UOI
    if (altitude < 128 or speed != 30) != (altitude < 128 or -speed != 30):
        t=1
    # 变异规则 150 - ROR
    if (altitude < 128 or speed != 30) != (128 > altitude or speed != 30):
        t=1
    # 原语句
    if altitude < 128 or speed != 30:
        health_score -= 2
        voltage_mv = min(voltage_mv + 1, 100)
    # 原语句16
    # 变异规则 151 - ABS
    if (altitude >= 200 or altitude > 30) != (abs(altitude) >= 200 or altitude > 30):
        t=1
    # 变异规则 152 - ROR
    if (altitude >= 200 or altitude > 30) != (altitude >= 200 or altitude > 29):
        triggered.add(101)
    # 变异规则 153 - AOR
    if (altitude >= 200 or altitude > 30) != (altitude >= 200 or -altitude > 30):
        triggered.add(102)
    # 变异规则 154 - CRP
    if (altitude >= 200 or altitude > 30) != (altitude >= 200 or altitude > 40):
        triggered.add(103)
    # 变异规则 155 - SVR
    if (altitude >= 200 or altitude > 30) != (speed >= 200 or altitude > 30):
        t=1
    # 变异规则 156 - CAR
    if (altitude >= 200 or altitude > 30) != (altitude >= 200 or altitude > 32):
        triggered.add(104)
    # 变异规则 157 - SRC
    if (altitude >= 200 or altitude > 30) != (altitude > 30 or altitude >= 200):
        t=1
    # 变异规则 158 - UOI
    if (altitude >= 200 or altitude > 30) != (altitude >= 200 or -altitude > 30):
        triggered.add(105)
    # 变异规则 159 - SAR
    if (altitude >= 200 or altitude > 30) != (altitude >= 200 or 30 < altitude):
        t=1
    # 变异规则 160 - SCR
    if (altitude >= 200 or altitude > 30) != (not (altitude >= 200 or altitude > 30)):
        triggered.add(106)
    # 原语句
    if altitude >= 200 or altitude > 30:
        health_score -= 11
        speed, altitude = altitude, speed
    # 原语句17
    # 变异规则 161 - SCR
    if (speed * voltage_mv != 20) != (abs(speed) * voltage_mv != 20):
        t=1
    # 变异规则 162 - CAR
    if (speed * voltage_mv != 20) != (speed * voltage_mv != 21):
        triggered.add(107)
    # 变异规则 163 - ROR
    if (speed * voltage_mv != 20) != (speed * voltage_mv != 24):
        triggered.add(108)
    # 变异规则 164 - RSR
    if (speed * voltage_mv != 20) != (not (speed * voltage_mv != 20)):
        triggered.add(109)
    # 变异规则 165 - SRC
    if (speed * voltage_mv != 20) != (speed * -voltage_mv != 20):
        triggered.add(110)
    # 变异规则 166 - ABS
    if (speed * voltage_mv != 20) != (abs(speed) * voltage_mv != 20):
        t=1
    # 变异规则 167 - AOR
    if (speed * voltage_mv != 20) != (speed * voltage_mv != 22):
        triggered.add(111)
    # 变异规则 168 - LCR
    if (speed * voltage_mv != 20) != (speed * voltage_mv != 26):
        triggered.add(112)
    # 变异规则 169 - CRP
    if (speed * voltage_mv != 20) != (speed * voltage_mv != 10):
        triggered.add(113)
    # 变异规则 170 - UOI
    if (speed * voltage_mv != 20) != (speed * -voltage_mv != 20):
        triggered.add(114)
    # 原语句
    if speed * voltage_mv != 20:
        health_score -= 29
        speed = min(speed + 8, 100)
    # 原语句18
    # 变异规则 171 - ABS
    if (320 <= altitude <= 939) != (320 <= abs(altitude) <= 939):
        t=1
    # 变异规则 172 - AOR
    if (320 <= altitude <= 939) != (altitude >= 320 <= 939):
        t=1
    # 变异规则 173 - CSR
    if (320 <= altitude <= 939) != (-320 <= altitude <= 939):
        triggered.add(115)
    # 变异规则 174 - SRC
    if (320 <= altitude <= 939) != (320 <= altitude <= 469):
        t=1
    # 变异规则 175 - RSR
    if (320 <= altitude <= 939) != (not (320 <= altitude <= 939)):
        triggered.add(116)
    # 变异规则 176 - SVR
    if (320 <= altitude <= 939) != (320 <= voltage_mv <= 939):
        t=1
    # 变异规则 177 - SCR
    if (320 <= altitude <= 939) != (not (320) <= altitude <= 939):
        triggered.add(117)
    # 变异规则 178 - UOI
    if (320 <= altitude <= 939) != (320 <= -altitude <= 939):
        t=1
    # 变异规则 179 - LCR
    if (320 <= altitude <= 939) != (-320 <= altitude <= 939):
        triggered.add(118)
    # 变异规则 180 - SAR
    if (320 <= altitude <= 939) != (altitude >= 320 <= 939):
        t=1
    # 原语句
    if 320 <= altitude <= 939:
        health_score += 16
        altitude = max(altitude - 10, 2)
    # 原语句19
    # 变异规则 181 - LCR
    if (speed == 99 or voltage_mv != 50) != (speed == 99 and voltage_mv != 50):
        triggered.add(119)
    # 变异规则 182 - UOI
    if (speed == 99 or voltage_mv != 50) != (speed == 99 or -voltage_mv != 50):
        triggered.add(120)
    # 变异规则 183 - CRP
    if (speed == 99 or voltage_mv != 50) != (speed == 98 or voltage_mv != 50):
        triggered.add(121)
    # 变异规则 184 - ROR
    if (speed == 99 or voltage_mv != 50) != (speed == 94 or voltage_mv != 50):
        triggered.add(122)
    # 变异规则 185 - RSR
    if (speed == 99 or voltage_mv != 50) != (not (speed == 99 or voltage_mv != 50)):
        triggered.add(123)
    # 变异规则 186 - SRC
    if (speed == 99 or voltage_mv != 50) != (voltage_mv != 50 or speed == 99):
        t=1
    # 变异规则 187 - CSR
    if (speed == 99 or voltage_mv != 50) != (speed == -99 or voltage_mv != 50):
        triggered.add(124)
    # 变异规则 188 - ABS
    if (speed == 99 or voltage_mv != 50) != (abs(speed) == 99 or voltage_mv != 50):
        t=1
    # 变异规则 189 - SAR
    if (speed == 99 or voltage_mv != 50) != (99 == speed or voltage_mv != 50):
        t=1
    # 变异规则 190 - SCR
    if (speed == 99 or voltage_mv != 50) != (speed == 99 or -voltage_mv != 50):
        triggered.add(125)
    # 原语句
    if speed == 99 or voltage_mv != 50:
        health_score -= 20
        speed = min(speed + 3, 100)
        voltage_mv = min(voltage_mv + 5, 100)
    # 原语句20
    # 变异规则 191 - SVR
    if (voltage_mv != altitude % 43) != (altitude != altitude % 43):
        triggered.add(126)
    # 变异规则 192 - CRP
    if (voltage_mv != altitude % 43) != (voltage_mv != altitude % 35):
        triggered.add(127)
    # 变异规则 193 - CSR
    if (voltage_mv != altitude % 43) != (voltage_mv != altitude % -43):
        triggered.add(128)
    # 变异规则 194 - ABS
    if (voltage_mv != altitude % 43) != (voltage_mv != abs(altitude) % 43):
        t=1
    # 变异规则 195 - SCR
    if (voltage_mv != altitude % 43) != (voltage_mv != abs(altitude) % 43):
        t=1
    # 变异规则 196 - LCR
    if (voltage_mv != altitude % 43) != (voltage_mv != -altitude % 43):
        triggered.add(129)
    # 变异规则 197 - RSR
    if (voltage_mv != altitude % 43) != (not (voltage_mv != altitude % 43)):
        triggered.add(130)
    # 变异规则 198 - SRC
    if (voltage_mv != altitude % 43) != (voltage_mv != altitude % -43):
        triggered.add(131)
    # 变异规则 199 - CAR
    if (voltage_mv != altitude % 43) != (voltage_mv != altitude % 41):
        triggered.add(132)
    # 变异规则 200 - AOR
    if (voltage_mv != altitude % 43) != (voltage_mv != altitude % -43):
        triggered.add(133)
    # 原语句
    if voltage_mv != altitude % 43:
        health_score += 7
    # 原语句21
    # 变异规则 201 - RSR
    if (speed >= altitude + 50) != (not (speed >= altitude + 50)):
        triggered.add(134)
    # 变异规则 202 - ABS
    if (speed >= altitude + 50) != (speed >= abs(altitude) + 50):
        t=1
    # 变异规则 203 - SRC
    if (speed >= altitude + 50) != (speed >= altitude + -50):
        triggered.add(135)
    # 变异规则 204 - SVR
    if (speed >= altitude + 50) != (voltage_mv >= altitude + 50):
        triggered.add(136)
    # 变异规则 205 - CRP
    if (speed >= altitude + 50) != (speed >= altitude + 100):
        triggered.add(137)
    # 变异规则 206 - UOI
    if (speed >= altitude + 50) != (speed >= -altitude + 50):
        triggered.add(138)
    # 变异规则 207 - AOR
    if (speed >= altitude + 50) != (speed >= altitude + 48):
        triggered.add(139)
    # 变异规则 208 - CSR
    if (speed >= altitude + 50) != (speed >= altitude + -50):
        triggered.add(140)
    # 变异规则 209 - SAR
    if (speed >= altitude + 50) != (altitude <= speed + 50):
        triggered.add(141)
    # 变异规则 210 - CAR
    if (speed >= altitude + 50) != (speed >= altitude + 40):
        triggered.add(142)
    # 原语句
    if speed >= altitude + 50:
        health_score += 2
        altitude = max(altitude - 3, 2)
    # 原语句22
    # 变异规则 211 - SAR
    if (4 <= voltage_mv <= 77) != (voltage_mv >= 4 <= 77):
        triggered.add(143)
    # 变异规则 212 - CSR
    if (4 <= voltage_mv <= 77) != (4 <= voltage_mv <= -77):
        triggered.add(144)
    # 变异规则 213 - SRC
    if (4 <= voltage_mv <= 77) != (4 <= speed <= 77):
        triggered.add(145)
    # 变异规则 214 - SVR
    if (4 <= voltage_mv <= 77) != (4 <= speed <= 77):
        triggered.add(146)
    # 变异规则 215 - ROR
    if (4 <= voltage_mv <= 77) != (4 <= -voltage_mv <= 77):
        triggered.add(147)
    # 变异规则 216 - LCR
    if (4 <= voltage_mv <= 77) != (4 <= voltage_mv <= 78):
        triggered.add(148)
    # 变异规则 217 - AOR
    if (4 <= voltage_mv <= 77) != (1 <= voltage_mv <= 77):
        t=1
    # 变异规则 218 - SCR
    if (4 <= voltage_mv <= 77) != (not (4) <= voltage_mv <= 77):
        triggered.add(149)
    # 变异规则 219 - ABS
    if (4 <= voltage_mv <= 77) != (4 <= abs(voltage_mv) <= 77):
        t=1
    # 变异规则 220 - CRP
    if (4 <= voltage_mv <= 77) != (1 <= voltage_mv <= 77):
        t=1
    # 原语句
    if 4 <= voltage_mv <= 77:
        health_score -= 9
        speed = min(speed + 2, 100)
        voltage_mv = min(voltage_mv + 8, 100)
    # 原语句23
    # 变异规则 221 - UOI
    if (altitude == 5) != (abs(altitude) == 5):
        t=1
    # 变异规则 222 - AOR
    if (altitude == 5) != (5 == altitude):
        t=1
    # 变异规则 223 - CRP
    if (altitude == 5) != (altitude == 3):
        triggered.add(150)
    # 变异规则 224 - CSR
    if (altitude == 5) != (altitude == -5):
        triggered.add(151)
    # 变异规则 225 - SCR
    if (altitude == 5) != (abs(altitude) == 5):
        t=1
    # 变异规则 226 - SRC
    if (altitude == 5) != (abs(altitude) == 5):
        t=1
    # 变异规则 227 - SVR
    if (altitude == 5) != (speed == 5):
        triggered.add(152)
    # 变异规则 228 - RSR
    if (altitude == 5) != (not (altitude == 5)):
        triggered.add(153)
    # 变异规则 229 - ROR
    if (altitude == 5) != (5 == altitude):
        t=1
    # 变异规则 230 - LCR
    if (altitude == 5) != (not (altitude == 5)):
        triggered.add(154)
    # 原语句
    if altitude == 5:
        health_score -= 27
        voltage_mv = max(voltage_mv - 2, 2)
    # 原语句24
    # 变异规则 231 - SAR
    if (speed <= 50 or altitude >= 100) != (50 >= speed or altitude >= 100):
        t=1
    # 变异规则 232 - AOR
    if (speed <= 50 or altitude >= 100) != (altitude <= 50 or altitude >= 100):
        triggered.add(155)
    # 变异规则 233 - SVR
    if (speed <= 50 or altitude >= 100) != (altitude <= 50 or altitude >= 100):
        triggered.add(156)
    # 变异规则 234 - CRP
    if (speed <= 50 or altitude >= 100) != (speed <= 47 or altitude >= 100):
        triggered.add(157)
    # 变异规则 235 - SCR
    if (speed <= 50 or altitude >= 100) != (50 >= speed or altitude >= 100):
        t=1
    # 变异规则 236 - ABS
    if (speed <= 50 or altitude >= 100) != (speed <= 50 or abs(altitude) >= 100):
        t=1
    # 变异规则 237 - ROR
    if (speed <= 50 or altitude >= 100) != (speed <= 50 and altitude >= 100):
        triggered.add(158)
    # 变异规则 238 - RSR
    if (speed <= 50 or altitude >= 100) != (not (speed <= 50 or altitude >= 100)):
        triggered.add(159)
    # 变异规则 239 - CSR
    if (speed <= 50 or altitude >= 100) != (speed <= 50 or altitude >= -100):
        triggered.add(160)
    # 变异规则 240 - UOI
    if (speed <= 50 or altitude >= 100) != (speed <= 50 or -altitude >= 100):
        triggered.add(161)
    # 原语句
    if speed <= 50 or altitude >= 100:
        health_score += 9
        altitude = min(altitude + 67, 1000)
    # 原语句25
    # 变异规则 241 - CRP
    if (speed == 20) != (speed == 30):
        triggered.add(162)
    # 变异规则 242 - SAR
    if (speed == 20) != (20 == speed):
        t=1
    # 变异规则 243 - AOR
    if (speed == 20) != (speed == -20):
        triggered.add(163)
    # 变异规则 244 - ROR
    if (speed == 20) != (altitude == 20):
        triggered.add(164)
    # 变异规则 245 - RSR
    if (speed == 20) != (not (speed == 20)):
        triggered.add(165)
    # 变异规则 246 - CSR
    if (speed == 20) != (speed == -20):
        triggered.add(166)
    # 变异规则 247 - SVR
    if (speed == 20) != (voltage_mv == 20):
        triggered.add(167)
    # 变异规则 248 - ABS
    if (speed == 20) != (abs(speed) == 20):
        t=1
    # 变异规则 249 - CAR
    if (speed == 20) != (speed == 21):
        triggered.add(168)
    # 变异规则 250 - SRC
    if (speed == 20) != (not (speed == 20)):
        triggered.add(169)
    # 原语句
    if speed == 20:
        health_score += 2
        altitude = min(altitude + 15, 1000)
        speed = min(speed + 8, 100)
    # 原语句26
    # 变异规则 251 - SAR
    if (altitude * 100 == voltage_mv) != (altitude * voltage_mv == 100):
        triggered.add(170)
    # 变异规则 252 - AOR
    if (altitude * 100 == voltage_mv) != (altitude * 100 == -voltage_mv):
        t=1
    # 变异规则 253 - RSR
    if (altitude * 100 == voltage_mv) != (not (altitude * 100 == voltage_mv)):
        triggered.add(171)
    # 变异规则 254 - CAR
    if (altitude * 100 == voltage_mv) != (altitude * 90 == voltage_mv):
        t=1
    # 变异规则 255 - SVR
    if (altitude * 100 == voltage_mv) != (voltage_mv * 100 == voltage_mv):
        t=1
    # 变异规则 256 - UOI
    if (altitude * 100 == voltage_mv) != (altitude * 100 == -voltage_mv):
        t=1
    # 变异规则 257 - CSR
    if (altitude * 100 == voltage_mv) != (altitude * -100 == voltage_mv):
        t=1
    # 变异规则 258 - SCR
    if (altitude * 100 == voltage_mv) != (altitude * 90 == voltage_mv):
        t=1
    # 变异规则 259 - ABS
    if (altitude * 100 == voltage_mv) != (abs(altitude) * 100 == voltage_mv):
        t=1
    # 变异规则 260 - SRC
    if (altitude * 100 == voltage_mv) != (altitude * 101 == voltage_mv):
        t=1
    # 原语句
    if altitude * 100 == voltage_mv:
        health_score -= 24
        voltage_mv = min(voltage_mv + 7, 100)
    # 原语句27
    # 变异规则 261 - SCR
    if (9 <= voltage_mv <= 86) != (-9 <= voltage_mv <= 86):
        t=1
    # 变异规则 262 - ROR
    if (9 <= voltage_mv <= 86) != (9 <= abs(voltage_mv) <= 86):
        t=1
    # 变异规则 263 - CRP
    if (9 <= voltage_mv <= 86) != (7 <= voltage_mv <= 86):
        t=1
    # 变异规则 264 - UOI
    if (9 <= voltage_mv <= 86) != (9 <= -voltage_mv <= 86):
        triggered.add(172)
    # 变异规则 265 - LCR
    if (9 <= voltage_mv <= 86) != (voltage_mv >= 9 <= 86):
        triggered.add(173)
    # 变异规则 266 - SRC
    if (9 <= voltage_mv <= 86) != (9 <= -voltage_mv <= 86):
        triggered.add(174)
    # 变异规则 267 - SVR
    if (9 <= voltage_mv <= 86) != (9 <= altitude <= 86):
        triggered.add(175)
    # 变异规则 268 - RSR
    if (9 <= voltage_mv <= 86) != (not (9 <= voltage_mv <= 86)):
        triggered.add(176)
    # 变异规则 269 - AOR
    if (9 <= voltage_mv <= 86) != (9 <= abs(voltage_mv) <= 86):
        t=1
    # 变异规则 270 - ABS
    if (9 <= voltage_mv <= 86) != (9 <= abs(voltage_mv) <= 86):
        t=1
    # 原语句
    if 9 <= voltage_mv <= 86:
        health_score -= 14
        altitude = max(altitude - 43, 2)
        speed = max(speed - 4, 2)
    # 原语句28
    # 变异规则 271 - SRC
    if (146 <= altitude <= 776) != (altitude >= 146 <= 776):
        t=1
    # 变异规则 272 - SAR
    if (146 <= altitude <= 776) != (altitude >= 146 <= 776):
        t=1
    # 变异规则 273 - ROR
    if (146 <= altitude <= 776) != (146 <= altitude <= 786):
        t=1
    # 变异规则 274 - LCR
    if (146 <= altitude <= 776) != (146 <= altitude <= -776):
        triggered.add(177)
    # 变异规则 275 - RSR
    if (146 <= altitude <= 776) != (not (146 <= altitude <= 776)):
        triggered.add(178)
    # 变异规则 276 - CRP
    if (146 <= altitude <= 776) != (146 <= altitude <= 1552):
        t=1
    # 变异规则 277 - ABS
    if (146 <= altitude <= 776) != (146 <= abs(altitude) <= 776):
        t=1
    # 变异规则 278 - CAR
    if (146 <= altitude <= 776) != (145 <= altitude <= 776):
        triggered.add(179)
    # 变异规则 279 - AOR
    if (146 <= altitude <= 776) != (146 <= -altitude <= 776):
        triggered.add(180)
    # 变异规则 280 - SVR
    if (146 <= altitude <= 776) != (146 <= speed <= 776):
        triggered.add(181)
    # 原语句
    if 146 <= altitude <= 776:
        health_score += 19
        altitude = min(altitude + 19, 1000)
        voltage_mv = min(voltage_mv + 3, 100)
    # 原语句29
    # 变异规则 281 - CSR
    if (speed == 50 and altitude <= 247) != (speed == -50 and altitude <= 247):
        triggered.add(182)
    # 变异规则 282 - SCR
    if (speed == 50 and altitude <= 247) != (not (speed == 50 and altitude <= 247)):
        triggered.add(183)
    # 变异规则 283 - AOR
    if (speed == 50 and altitude <= 247) != (speed == 50 and 247 >= altitude):
        t=1
    # 变异规则 284 - CAR
    if (speed == 50 and altitude <= 247) != (speed == 45 and altitude <= 247):
        triggered.add(184)
    # 变异规则 285 - UOI
    if (speed == 50 and altitude <= 247) != (speed == 50 and -altitude <= 247):
        t=1
    # 变异规则 286 - SAR
    if (speed == 50 and altitude <= 247) != (speed == 50 and 247 >= altitude):
        t=1
    # 变异规则 287 - LCR
    if (speed == 50 and altitude <= 247) != (speed == 50 or altitude <= 247):
        triggered.add(185)
    # 变异规则 288 - CRP
    if (speed == 50 and altitude <= 247) != (speed == 47 and altitude <= 247):
        triggered.add(186)
    # 变异规则 289 - SVR
    if (speed == 50 and altitude <= 247) != (altitude == 50 and altitude <= 247):
        triggered.add(187)
    # 变异规则 290 - RSR
    if (speed == 50 and altitude <= 247) != (not (speed == 50 and altitude <= 247)):
        triggered.add(188)
    # 原语句
    if speed == 50 and altitude <= 247:
        health_score += 20
    # 原语句30
    # 变异规则 291 - SCR
    if (voltage_mv <= 30) != (voltage_mv <= -30):
        triggered.add(189)
    # 变异规则 292 - SAR
    if (voltage_mv <= 30) != (30 >= voltage_mv):
        t=1
    # 变异规则 293 - AOR
    if (voltage_mv <= 30) != (voltage_mv <= 35):
        triggered.add(190)
    # 变异规则 294 - UOI
    if (voltage_mv <= 30) != (voltage_mv <= 31):
        triggered.add(191)
    # 变异规则 295 - CAR
    if (voltage_mv <= 30) != (voltage_mv <= 20):
        triggered.add(192)
    # 变异规则 296 - ABS
    if (voltage_mv <= 30) != (abs(voltage_mv) <= 30):
        t=1
    # 变异规则 297 - SRC
    if (voltage_mv <= 30) != (30 >= voltage_mv):
        t=1
    # 变异规则 298 - LCR
    if (voltage_mv <= 30) != (abs(voltage_mv) <= 30):
        t=1
    # 变异规则 299 - CSR
    if (voltage_mv <= 30) != (voltage_mv <= -30):
        triggered.add(193)
    # 变异规则 300 - CRP
    if (voltage_mv <= 30) != (voltage_mv <= 60):
        triggered.add(194)
    # 原语句
    if voltage_mv <= 30:
        health_score -= 28
    return triggered

targetPaths = [
    {1, 7, 8, 9, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 61, 62, 70, 76, 77, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 7, 8, 9, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 61, 62, 70, 76, 77, 87, 90, 93, 94, 97, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 7, 8, 9, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 61, 62, 70, 76, 77, 85, 87, 90, 93, 94, 97, 106, 109, 111, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 8, 9, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 69, 70, 76, 77, 85, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 8, 9, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 70, 76, 77, 85, 88, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 8, 9, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 9, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 91, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 190, 191, 194},
    {1, 9, 12, 14, 15, 21, 22, 26, 27, 30, 34, 41, 50, 51, 59, 70, 76, 77, 80, 84, 87, 90, 91, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 190, 194},
    {1, 9, 12, 14, 15, 23, 24, 25, 26, 27, 30, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 190, 194},
    {1, 9, 12, 14, 15, 24, 25, 26, 27, 28, 29, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 24, 25, 26, 27, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 129, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 24, 25, 26, 27, 34, 41, 50, 51, 59, 70, 76, 77, 78, 79, 80, 81, 83, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 120, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 148, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 50, 51, 59, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185},
    {1, 7, 8, 9, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 61, 62, 67, 68, 69, 70, 71, 73, 74, 76, 77, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 9, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 162, 163, 164, 165, 167, 168, 171, 172, 176, 178, 183, 185, 190, 194},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 52, 59, 61, 62, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 51, 53, 54, 59, 61, 62, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 98, 99, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 142, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 142, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 184, 185},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 142, 144, 147, 149, 153, 157, 158, 159, 165, 171, 172, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 142, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185, 186},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 138, 141, 142, 144, 147, 149, 153, 157, 158, 159, 165, 171, 172, 176, 178, 183, 185},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 87, 90, 91, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 138, 141, 142, 144, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185, 186},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 83, 84, 86, 87, 90, 91, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 138, 139, 141, 142, 144, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 83, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 138, 139, 141, 142, 143, 145, 149, 153, 157, 158, 159, 165, 171, 173, 175, 176, 178, 182, 183, 184, 186, 187},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 137, 144, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 182, 183, 184, 186, 187},
    {1, 10, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 138, 141, 142, 144, 147, 149, 153, 155, 159, 160, 165, 170, 171, 172, 175, 176, 178, 183, 185, 186, 194},
    {1, 2, 3, 4, 5, 6, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 51, 54, 59, 61, 62, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 136, 137, 144, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185, 189},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 32, 34, 35, 36, 37, 38, 41, 51, 54, 59, 61, 62, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 136, 137, 144, 145, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185, 189},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 32, 34, 35, 36, 37, 38, 41, 51, 54, 59, 61, 62, 70, 76, 77, 87, 90, 93, 94, 95, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 136, 137, 144, 145, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185, 189},
    {1, 10, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 120, 122, 123, 126, 130, 134, 136, 137, 144, 145, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185, 194},
    {1, 10, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 87, 90, 93, 94, 95, 106, 109, 115, 116, 117, 120, 121, 123, 126, 130, 134, 136, 137, 144, 145, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185, 194},
    {1, 10, 12, 14, 15, 25, 26, 27, 34, 41, 51, 54, 59, 70, 76, 77, 87, 90, 93, 94, 95, 106, 109, 115, 116, 117, 119, 121, 122, 123, 124, 126, 130, 134, 137, 144, 145, 147, 149, 153, 155, 159, 160, 165, 171, 172, 175, 176, 178, 183, 185},
    {1, 7, 8, 9, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 61, 62, 70, 76, 77, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 150, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189, 192},
    {1, 7, 8, 9, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 59, 61, 62, 68, 70, 76, 77, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 150, 151, 152, 153, 158, 159, 165, 167, 171, 172, 176, 178, 183, 185, 189},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 51, 53, 54, 58, 59, 61, 62, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 51, 53, 54, 58, 59, 61, 62, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 128, 129, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189},
    {1, 9, 12, 14, 15, 23, 24, 25, 26, 27, 30, 34, 41, 50, 51, 59, 61, 62, 66, 70, 76, 77, 84, 87, 90, 93, 94, 97, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 190, 194},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 51, 53, 54, 59, 60, 63, 65, 66, 70, 76, 77, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 142, 144, 147, 149, 150, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 189},
    {1, 9, 12, 14, 15, 23, 24, 25, 26, 27, 28, 30, 34, 41, 50, 51, 54, 58, 59, 61, 62, 66, 70, 76, 77, 84, 87, 90, 93, 94, 97, 101, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 175, 176, 178, 183, 185, 190, 194},
    {1, 9, 12, 14, 15, 23, 24, 25, 26, 27, 30, 34, 41, 50, 51, 54, 58, 59, 61, 62, 66, 70, 76, 77, 84, 87, 90, 93, 94, 97, 102, 103, 104, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 141, 142, 144, 147, 149, 153, 158, 159, 165, 171, 172, 176, 178, 183, 185, 190, 194},
    {1, 10, 12, 14, 15, 24, 25, 26, 27, 34, 41, 51, 59, 61, 62, 70, 76, 77, 87, 90, 93, 102, 103, 104, 106, 109, 115, 116, 117, 119, 123, 127, 128, 129, 130, 134, 135, 138, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 175, 176, 178, 183, 185, 194},
    {1, 10, 12, 14, 15, 25, 26, 27, 34, 41, 51, 59, 61, 62, 70, 76, 77, 87, 90, 93, 102, 103, 104, 106, 109, 115, 116, 117, 119, 123, 127, 128, 129, 130, 132, 134, 135, 138, 141, 144, 147, 149, 153, 158, 159, 165, 171, 172, 175, 176, 178, 183, 185, 194},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 102, 103, 104, 106, 109, 115, 116, 117, 119, 123, 130, 134, 135, 138, 141, 143, 145, 149, 153, 155, 158, 159, 165, 171, 173, 176, 178, 179, 183, 185},
    {1, 9, 12, 14, 15, 25, 26, 27, 34, 41, 51, 59, 70, 76, 77, 84, 86, 87, 90, 91, 93, 102, 103, 104, 106, 109, 115, 116, 117, 119, 123, 130, 134, 135, 138, 141, 143, 145, 149, 153, 155, 158, 159, 165, 171, 173, 176, 177, 178, 180, 181, 183, 185},
    {1, 10, 12, 14, 15, 25, 26, 27, 34, 41, 51, 59, 65, 70, 76, 77, 84, 86, 87, 90, 91, 93, 94, 95, 102, 103, 106, 109, 115, 116, 117, 119, 123, 130, 134, 135, 138, 141, 143, 145, 149, 153, 158, 159, 161, 165, 171, 173, 176, 177, 178, 180, 181, 183, 185},
    {1, 7, 8, 9, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 44, 50, 51, 54, 59, 65, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185},
    {1, 10, 12, 14, 15, 22, 26, 27, 30, 34, 41, 50, 51, 54, 59, 65, 70, 76, 77, 84, 87, 90, 93, 98, 99, 100, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 138, 141, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185},
    {1, 7, 8, 9, 10, 12, 14, 15, 19, 22, 26, 27, 30, 34, 41, 50, 51, 54, 59, 65, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185},
    {1, 7, 8, 9, 10, 12, 14, 15, 19, 22, 26, 27, 30, 34, 41, 43, 50, 51, 54, 59, 65, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185},
    {1, 7, 8, 9, 10, 12, 14, 15, 19, 22, 26, 27, 30, 34, 41, 49, 50, 51, 54, 59, 65, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185},
    {1, 7, 8, 9, 10, 12, 14, 15, 19, 22, 26, 27, 30, 34, 41, 43, 44, 45, 48, 49, 50, 51, 54, 59, 65, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 149, 150, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185},
    {1, 7, 8, 9, 10, 12, 13, 14, 15, 17, 20, 22, 26, 27, 30, 34, 41, 50, 51, 54, 59, 65, 70, 76, 77, 84, 87, 90, 93, 106, 109, 115, 116, 117, 119, 123, 126, 130, 134, 135, 136, 141, 143, 145, 149, 153, 158, 159, 165, 171, 173, 175, 176, 178, 183, 185}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 3:3, 4:4, 7:5, 8:6, 11:7, 13:8, 14:9, 15:10, 16:11, 19:12, 21:13, 23:14, 25:15, 26:16, 27:17, 28:18, 29:19, 30:20, 31:21, 32:22, 33:23, 35:24, 36:25, 38:26, 41:27, 42:28, 46:29, 47:30, 50:31, 51:32, 52:33, 53:34, 54:35, 55:36, 56:37, 57:38, 59:39, 60:40, 61:41, 62:42, 63:43, 64:44, 65:45, 67:46, 68:47, 69:48, 70:49, 71:50, 72:51, 74:52, 75:53, 77:54, 78:55, 79:56, 80:57, 81:58, 82:59, 83:60, 84:61, 85:62, 86:63, 87:64, 88:65, 89:66, 91:67, 92:68, 93:69, 94:70, 95:71, 96:72, 97:73, 98:74, 99:75, 102:76, 112:77, 113:78, 114:79, 115:80, 116:81, 117:82, 120:83, 121:84, 123:85, 124:86, 125:87, 126:88, 127:89, 128:90, 129:91, 130:92, 131:93, 134:94, 136:95, 138:96, 139:97, 141:98, 142:99, 146:100, 152:101, 153:102, 154:103, 156:104, 158:105, 160:106, 162:107, 163:108, 164:109, 165:110, 167:111, 168:112, 169:113, 170:114, 173:115, 175:116, 177:117, 179:118, 181:119, 182:120, 183:121, 184:122, 185:123, 187:124, 190:125, 191:126, 192:127, 193:128, 196:129, 197:130, 198:131, 199:132, 200:133, 201:134, 203:135, 204:136, 205:137, 206:138, 207:139, 208:140, 209:141, 210:142, 211:143, 212:144, 213:145, 214:146, 215:147, 216:148, 218:149, 223:150, 224:151, 227:152, 228:153, 230:154, 232:155, 233:156, 234:157, 237:158, 238:159, 239:160, 240:161, 241:162, 243:163, 244:164, 245:165, 246:166, 247:167, 249:168, 250:169, 251:170, 253:171, 264:172, 265:173, 266:174, 267:175, 268:176, 274:177, 275:178, 278:179, 279:180, 280:181, 281:182, 282:183, 284:184, 287:185, 288:186, 289:187, 290:188, 291:189, 293:190, 294:191, 295:192, 299:193, 300:194}

    rule_expressions[1] = "(speed == 47 and altitude >= 2) != (not (speed == 47 and altitude >= 2))"
    rule_expressions[2] = "(speed == 47 and altitude >= 2) != (altitude == 47 and altitude >= 2)"
    rule_expressions[3] = "(speed == 47 and altitude >= 2) != (speed == 47 and -altitude >= 2)"
    rule_expressions[4] = "(speed == 47 and altitude >= 2) != (speed == 47 and altitude >= 8)"
    rule_expressions[5] = "(speed == 47 and altitude >= 2) != (speed == 47 and altitude >= 4)"
    rule_expressions[6] = "(speed == 47 and altitude >= 2) != (speed == -47 and altitude >= 2)"
    rule_expressions[7] = "(voltage_mv + speed > 2) != (voltage_mv + speed > 7)"
    rule_expressions[8] = "(voltage_mv + speed > 2) != (voltage_mv + speed > 12)"
    rule_expressions[9] = "(voltage_mv + speed > 2) != (voltage_mv + 2 < speed)"
    rule_expressions[10] = "(voltage_mv + speed > 2) != (voltage_mv + -speed > 2)"
    rule_expressions[11] = "(voltage_mv + speed > 2) != (voltage_mv + 2 < speed)"
    rule_expressions[12] = "(voltage_mv + speed > 2) != (not (voltage_mv + speed > 2))"
    rule_expressions[13] = "(altitude >= 500 and altitude != 500) != (altitude >= 500 and -altitude != 500)"
    rule_expressions[14] = "(altitude >= 500 and altitude != 500) != (not (altitude >= 500 and altitude != 500))"
    rule_expressions[15] = "(altitude >= 500 and altitude != 500) != (altitude >= 500 or altitude != 500)"
    rule_expressions[16] = "(altitude >= 500 and altitude != 500) != (altitude >= 500 or altitude != 500)"
    rule_expressions[17] = "(altitude >= 500 and altitude != 500) != (altitude >= 500 and altitude != -500)"
    rule_expressions[18] = "(altitude >= 500 and altitude != 500) != (altitude >= 500 and altitude != -500)"
    rule_expressions[19] = "(altitude >= 500 and altitude != 500) != (altitude >= 250 and altitude != 500)"
    rule_expressions[20] = "(altitude >= 500 and altitude != 500) != (altitude >= 500 and altitude != 502)"
    rule_expressions[21] = "(voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 19 and voltage_mv > 5)"
    rule_expressions[22] = "(voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 20 and -voltage_mv > 5)"
    rule_expressions[23] = "(voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 30 and voltage_mv > 5)"
    rule_expressions[24] = "(voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 40 and voltage_mv > 5)"
    rule_expressions[25] = "(voltage_mv < 20 and voltage_mv > 5) != (voltage_mv < 20 or voltage_mv > 5)"
    rule_expressions[26] = "(voltage_mv < 20 and voltage_mv > 5) != (not (voltage_mv < 20 and voltage_mv > 5))"
    rule_expressions[27] = "(voltage_mv == 30 and voltage_mv <= 30) != (not (voltage_mv == 30 and voltage_mv <= 30))"
    rule_expressions[28] = "(voltage_mv == 30 and voltage_mv <= 30) != (altitude == 30 and voltage_mv <= 30)"
    rule_expressions[29] = "(voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 and voltage_mv <= -30)"
    rule_expressions[30] = "(voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 or voltage_mv <= 30)"
    rule_expressions[31] = "(voltage_mv == 30 and voltage_mv <= 30) != (voltage_mv == 30 or voltage_mv <= 30)"
    rule_expressions[32] = "(voltage_mv * 10 == speed) != (voltage_mv * -10 == speed)"
    rule_expressions[33] = "(voltage_mv * 10 == speed) != (voltage_mv * -10 == speed)"
    rule_expressions[34] = "(voltage_mv * 10 == speed) != (not (voltage_mv * 10 == speed))"
    rule_expressions[35] = "(voltage_mv * 10 == speed) != (voltage_mv * 10 == -speed)"
    rule_expressions[36] = "(voltage_mv * 10 == speed) != (voltage_mv * 20 == speed)"
    rule_expressions[37] = "(voltage_mv * 10 == speed) != (voltage_mv * speed == 10)"
    rule_expressions[38] = "(voltage_mv * 10 == speed) != (speed * 10 == speed)"
    rule_expressions[39] = "(voltage_mv * 10 == speed) != (speed * 10 == speed)"
    rule_expressions[40] = "(voltage_mv * 10 == speed) != (speed * 10 == speed)"
    rule_expressions[41] = "(altitude == 305) != (not (altitude == 305))"
    rule_expressions[42] = "(altitude == 305) != (not (altitude == 305))"
    rule_expressions[43] = "(altitude == 305) != (altitude == 303)"
    rule_expressions[44] = "(altitude == 305) != (altitude == 152)"
    rule_expressions[45] = "(altitude == 305) != (altitude == -305)"
    rule_expressions[46] = "(altitude == 305) != (not (altitude == 305))"
    rule_expressions[47] = "(altitude == 305) != (altitude == 303)"
    rule_expressions[48] = "(altitude == 305) != (voltage_mv == 305)"
    rule_expressions[49] = "(altitude == 305) != (altitude == 304)"
    rule_expressions[50] = "(speed > 28) != (speed > -28)"
    rule_expressions[51] = "(speed > 28) != (not (speed > 28))"
    rule_expressions[52] = "(speed > 28) != (speed > 23)"
    rule_expressions[53] = "(speed > 28) != (speed > 29)"
    rule_expressions[54] = "(speed > 28) != (altitude > 28)"
    rule_expressions[55] = "(speed > 28) != (speed > 29)"
    rule_expressions[56] = "(speed > 28) != (not (speed > 28))"
    rule_expressions[57] = "(speed > 28) != (speed > -28)"
    rule_expressions[58] = "(voltage_mv < altitude - 10) != (voltage_mv < altitude - 4)"
    rule_expressions[59] = "(voltage_mv < altitude - 10) != (not (voltage_mv < altitude - 10))"
    rule_expressions[60] = "(voltage_mv < altitude - 10) != (voltage_mv < altitude - 20)"
    rule_expressions[61] = "(voltage_mv < altitude - 10) != (voltage_mv < altitude - -10)"
    rule_expressions[62] = "(voltage_mv < altitude - 10) != (altitude > voltage_mv - 10)"
    rule_expressions[63] = "(voltage_mv < altitude - 10) != (voltage_mv < altitude - 14)"
    rule_expressions[64] = "(voltage_mv < altitude - 10) != (altitude > voltage_mv - 10)"
    rule_expressions[65] = "(voltage_mv < altitude - 10) != (voltage_mv < -altitude - 10)"
    rule_expressions[66] = "(voltage_mv < altitude - 10) != (speed < altitude - 10)"
    rule_expressions[67] = "(speed + 3 == voltage_mv) != (speed + 1 == voltage_mv)"
    rule_expressions[68] = "(speed + 3 == voltage_mv) != (altitude + 3 == voltage_mv)"
    rule_expressions[69] = "(speed + 3 == voltage_mv) != (speed + 9 == voltage_mv)"
    rule_expressions[70] = "(speed + 3 == voltage_mv) != (not (speed + 3 == voltage_mv))"
    rule_expressions[71] = "(speed + 3 == voltage_mv) != (speed + 3 == -voltage_mv)"
    rule_expressions[72] = "(speed + 3 == voltage_mv) != (not (speed + 3 == voltage_mv))"
    rule_expressions[73] = "(speed + 3 == voltage_mv) != (speed + -3 == voltage_mv)"
    rule_expressions[74] = "(speed + 3 == voltage_mv) != (speed + voltage_mv == 3)"
    rule_expressions[75] = "(speed + 3 == voltage_mv) != (not (speed + 3 == voltage_mv))"
    rule_expressions[76] = "(altitude >= 1000) != (altitude >= -1000)"
    rule_expressions[77] = "(voltage_mv != 39) != (not (voltage_mv != 39))"
    rule_expressions[78] = "(voltage_mv != 39) != (voltage_mv != 44)"
    rule_expressions[79] = "(voltage_mv != 39) != (voltage_mv != 40)"
    rule_expressions[80] = "(voltage_mv != 39) != (voltage_mv != 19)"
    rule_expressions[81] = "(voltage_mv != 39) != (voltage_mv != -39)"
    rule_expressions[82] = "(voltage_mv != 39) != (voltage_mv != 19)"
    rule_expressions[83] = "(voltage_mv != 39) != (speed != 39)"
    rule_expressions[84] = "(voltage_mv - speed <= 10) != (speed - speed <= 10)"
    rule_expressions[85] = "(voltage_mv - speed <= 10) != (voltage_mv - speed <= 5)"
    rule_expressions[86] = "(voltage_mv - speed <= 10) != (voltage_mv - speed <= 11)"
    rule_expressions[87] = "(voltage_mv - speed <= 10) != (voltage_mv - 10 >= speed)"
    rule_expressions[88] = "(voltage_mv - speed <= 10) != (voltage_mv - speed <= 9)"
    rule_expressions[89] = "(voltage_mv - speed <= 10) != (voltage_mv - 10 >= speed)"
    rule_expressions[90] = "(voltage_mv - speed <= 10) != (not (voltage_mv - speed <= 10))"
    rule_expressions[91] = "(voltage_mv - speed <= 10) != (voltage_mv - speed <= 15)"
    rule_expressions[92] = "(voltage_mv - speed <= 10) != (speed - speed <= 10)"
    rule_expressions[93] = "(speed > 87 and speed < 7) != (not (speed > 87 and speed < 7))"
    rule_expressions[94] = "(speed > 87 and speed < 7) != (speed > 87 or speed < 7)"
    rule_expressions[95] = "(speed > 87 and speed < 7) != (speed > 87 and -speed < 7)"
    rule_expressions[96] = "(speed > 87 and speed < 7) != (speed > 87 or speed < 7)"
    rule_expressions[97] = "(speed > 87 and speed < 7) != (speed > -87 and speed < 7)"
    rule_expressions[98] = "(altitude < 128 or speed != 30) != (altitude < -128 or speed != 30)"
    rule_expressions[99] = "(altitude < 128 or speed != 30) != (altitude < 128 and speed != 30)"
    rule_expressions[100] = "(altitude < 128 or speed != 30) != (voltage_mv < 128 or speed != 30)"
    rule_expressions[101] = "(altitude >= 200 or altitude > 30) != (altitude >= 200 or altitude > 29)"
    rule_expressions[102] = "(altitude >= 200 or altitude > 30) != (altitude >= 200 or -altitude > 30)"
    rule_expressions[103] = "(altitude >= 200 or altitude > 30) != (altitude >= 200 or altitude > 40)"
    rule_expressions[104] = "(altitude >= 200 or altitude > 30) != (altitude >= 200 or altitude > 32)"
    rule_expressions[105] = "(altitude >= 200 or altitude > 30) != (altitude >= 200 or -altitude > 30)"
    rule_expressions[106] = "(altitude >= 200 or altitude > 30) != (not (altitude >= 200 or altitude > 30))"
    rule_expressions[107] = "(speed * voltage_mv != 20) != (speed * voltage_mv != 21)"
    rule_expressions[108] = "(speed * voltage_mv != 20) != (speed * voltage_mv != 24)"
    rule_expressions[109] = "(speed * voltage_mv != 20) != (not (speed * voltage_mv != 20))"
    rule_expressions[110] = "(speed * voltage_mv != 20) != (speed * -voltage_mv != 20)"
    rule_expressions[111] = "(speed * voltage_mv != 20) != (speed * voltage_mv != 22)"
    rule_expressions[112] = "(speed * voltage_mv != 20) != (speed * voltage_mv != 26)"
    rule_expressions[113] = "(speed * voltage_mv != 20) != (speed * voltage_mv != 10)"
    rule_expressions[114] = "(speed * voltage_mv != 20) != (speed * -voltage_mv != 20)"
    rule_expressions[115] = "(320 <= altitude <= 939) != (-320 <= altitude <= 939)"
    rule_expressions[116] = "(320 <= altitude <= 939) != (not (320 <= altitude <= 939))"
    rule_expressions[117] = "(320 <= altitude <= 939) != (not (320) <= altitude <= 939)"
    rule_expressions[118] = "(320 <= altitude <= 939) != (-320 <= altitude <= 939)"
    rule_expressions[119] = "(speed == 99 or voltage_mv != 50) != (speed == 99 and voltage_mv != 50)"
    rule_expressions[120] = "(speed == 99 or voltage_mv != 50) != (speed == 99 or -voltage_mv != 50)"
    rule_expressions[121] = "(speed == 99 or voltage_mv != 50) != (speed == 98 or voltage_mv != 50)"
    rule_expressions[122] = "(speed == 99 or voltage_mv != 50) != (speed == 94 or voltage_mv != 50)"
    rule_expressions[123] = "(speed == 99 or voltage_mv != 50) != (not (speed == 99 or voltage_mv != 50))"
    rule_expressions[124] = "(speed == 99 or voltage_mv != 50) != (speed == -99 or voltage_mv != 50)"
    rule_expressions[125] = "(speed == 99 or voltage_mv != 50) != (speed == 99 or -voltage_mv != 50)"
    rule_expressions[126] = "(voltage_mv != altitude % 43) != (altitude != altitude % 43)"
    rule_expressions[127] = "(voltage_mv != altitude % 43) != (voltage_mv != altitude % 35)"
    rule_expressions[128] = "(voltage_mv != altitude % 43) != (voltage_mv != altitude % -43)"
    rule_expressions[129] = "(voltage_mv != altitude % 43) != (voltage_mv != -altitude % 43)"
    rule_expressions[130] = "(voltage_mv != altitude % 43) != (not (voltage_mv != altitude % 43))"
    rule_expressions[131] = "(voltage_mv != altitude % 43) != (voltage_mv != altitude % -43)"
    rule_expressions[132] = "(voltage_mv != altitude % 43) != (voltage_mv != altitude % 41)"
    rule_expressions[133] = "(voltage_mv != altitude % 43) != (voltage_mv != altitude % -43)"
    rule_expressions[134] = "(speed >= altitude + 50) != (not (speed >= altitude + 50))"
    rule_expressions[135] = "(speed >= altitude + 50) != (speed >= altitude + -50)"
    rule_expressions[136] = "(speed >= altitude + 50) != (voltage_mv >= altitude + 50)"
    rule_expressions[137] = "(speed >= altitude + 50) != (speed >= altitude + 100)"
    rule_expressions[138] = "(speed >= altitude + 50) != (speed >= -altitude + 50)"
    rule_expressions[139] = "(speed >= altitude + 50) != (speed >= altitude + 48)"
    rule_expressions[140] = "(speed >= altitude + 50) != (speed >= altitude + -50)"
    rule_expressions[141] = "(speed >= altitude + 50) != (altitude <= speed + 50)"
    rule_expressions[142] = "(speed >= altitude + 50) != (speed >= altitude + 40)"
    rule_expressions[143] = "(4 <= voltage_mv <= 77) != (voltage_mv >= 4 <= 77)"
    rule_expressions[144] = "(4 <= voltage_mv <= 77) != (4 <= voltage_mv <= -77)"
    rule_expressions[145] = "(4 <= voltage_mv <= 77) != (4 <= speed <= 77)"
    rule_expressions[146] = "(4 <= voltage_mv <= 77) != (4 <= speed <= 77)"
    rule_expressions[147] = "(4 <= voltage_mv <= 77) != (4 <= -voltage_mv <= 77)"
    rule_expressions[148] = "(4 <= voltage_mv <= 77) != (4 <= voltage_mv <= 78)"
    rule_expressions[149] = "(4 <= voltage_mv <= 77) != (not (4) <= voltage_mv <= 77)"
    rule_expressions[150] = "(altitude == 5) != (altitude == 3)"
    rule_expressions[151] = "(altitude == 5) != (altitude == -5)"
    rule_expressions[152] = "(altitude == 5) != (speed == 5)"
    rule_expressions[153] = "(altitude == 5) != (not (altitude == 5))"
    rule_expressions[154] = "(altitude == 5) != (not (altitude == 5))"
    rule_expressions[155] = "(speed <= 50 or altitude >= 100) != (altitude <= 50 or altitude >= 100)"
    rule_expressions[156] = "(speed <= 50 or altitude >= 100) != (altitude <= 50 or altitude >= 100)"
    rule_expressions[157] = "(speed <= 50 or altitude >= 100) != (speed <= 47 or altitude >= 100)"
    rule_expressions[158] = "(speed <= 50 or altitude >= 100) != (speed <= 50 and altitude >= 100)"
    rule_expressions[159] = "(speed <= 50 or altitude >= 100) != (not (speed <= 50 or altitude >= 100))"
    rule_expressions[160] = "(speed <= 50 or altitude >= 100) != (speed <= 50 or altitude >= -100)"
    rule_expressions[161] = "(speed <= 50 or altitude >= 100) != (speed <= 50 or -altitude >= 100)"
    rule_expressions[162] = "(speed == 20) != (speed == 30)"
    rule_expressions[163] = "(speed == 20) != (speed == -20)"
    rule_expressions[164] = "(speed == 20) != (altitude == 20)"
    rule_expressions[165] = "(speed == 20) != (not (speed == 20))"
    rule_expressions[166] = "(speed == 20) != (speed == -20)"
    rule_expressions[167] = "(speed == 20) != (voltage_mv == 20)"
    rule_expressions[168] = "(speed == 20) != (speed == 21)"
    rule_expressions[169] = "(speed == 20) != (not (speed == 20))"
    rule_expressions[170] = "(altitude * 100 == voltage_mv) != (altitude * voltage_mv == 100)"
    rule_expressions[171] = "(altitude * 100 == voltage_mv) != (not (altitude * 100 == voltage_mv))"
    rule_expressions[172] = "(9 <= voltage_mv <= 86) != (9 <= -voltage_mv <= 86)"
    rule_expressions[173] = "(9 <= voltage_mv <= 86) != (voltage_mv >= 9 <= 86)"
    rule_expressions[174] = "(9 <= voltage_mv <= 86) != (9 <= -voltage_mv <= 86)"
    rule_expressions[175] = "(9 <= voltage_mv <= 86) != (9 <= altitude <= 86)"
    rule_expressions[176] = "(9 <= voltage_mv <= 86) != (not (9 <= voltage_mv <= 86))"
    rule_expressions[177] = "(146 <= altitude <= 776) != (146 <= altitude <= -776)"
    rule_expressions[178] = "(146 <= altitude <= 776) != (not (146 <= altitude <= 776))"
    rule_expressions[179] = "(146 <= altitude <= 776) != (145 <= altitude <= 776)"
    rule_expressions[180] = "(146 <= altitude <= 776) != (146 <= -altitude <= 776)"
    rule_expressions[181] = "(146 <= altitude <= 776) != (146 <= speed <= 776)"
    rule_expressions[182] = "(speed == 50 and altitude <= 247) != (speed == -50 and altitude <= 247)"
    rule_expressions[183] = "(speed == 50 and altitude <= 247) != (not (speed == 50 and altitude <= 247))"
    rule_expressions[184] = "(speed == 50 and altitude <= 247) != (speed == 45 and altitude <= 247)"
    rule_expressions[185] = "(speed == 50 and altitude <= 247) != (speed == 50 or altitude <= 247)"
    rule_expressions[186] = "(speed == 50 and altitude <= 247) != (speed == 47 and altitude <= 247)"
    rule_expressions[187] = "(speed == 50 and altitude <= 247) != (altitude == 50 and altitude <= 247)"
    rule_expressions[188] = "(speed == 50 and altitude <= 247) != (not (speed == 50 and altitude <= 247))"
    rule_expressions[189] = "(voltage_mv <= 30) != (voltage_mv <= -30)"
    rule_expressions[190] = "(voltage_mv <= 30) != (voltage_mv <= 35)"
    rule_expressions[191] = "(voltage_mv <= 30) != (voltage_mv <= 31)"
    rule_expressions[192] = "(voltage_mv <= 30) != (voltage_mv <= 20)"
    rule_expressions[193] = "(voltage_mv <= 30) != (voltage_mv <= -30)"
    rule_expressions[194] = "(voltage_mv <= 30) != (voltage_mv <= 60)"

    return rule_expressions