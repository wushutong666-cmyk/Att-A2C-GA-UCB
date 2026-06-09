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
    # 变异规则 1 - SCR
    if (altitude + speed != 616) != (voltage_mv + speed != 616):
        triggered.add(1)
    # 变异规则 2 - SAR
    if (altitude + speed != 616) != (altitude + 616 != speed):
        triggered.add(2)
    # 变异规则 3 - ABS
    if (altitude + speed != 616) != (abs(altitude) + speed != 616):
        t = 1
    # 变异规则 4 - ROR
    if (altitude + speed != 616) != (altitude + speed != 621):
        triggered.add(3)
    # 变异规则 5 - UOI
    if (altitude + speed != 616) != (altitude + -speed != 616):
        triggered.add(4)
    # 变异规则 6 - LCR
    if (altitude + speed != 616) != (not (altitude + speed != 616)):
        triggered.add(5)
    # 变异规则 7 - AOR
    if (altitude + speed != 616) != (altitude + speed != 615):
        triggered.add(6)
    # 变异规则 8 - CAR
    if (altitude + speed != 616) != (altitude + speed != 626):
        triggered.add(7)
    # 变异规则 9 - CRP
    if (altitude + speed != 616) != (altitude + speed != 617):
        triggered.add(8)
    # 变异规则 10 - RSR
    if (altitude + speed != 616) != (not (altitude + speed != 616)):
        triggered.add(9)
    # 原语句
    if altitude + speed != 616:
        health_score -= 4
        altitude = max(altitude - 41, 2)
    # 原语句2
    # 变异规则 11 - CAR
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 5 and speed != 20):
        triggered.add(10)
    # 变异规则 12 - SVR
    if (voltage_mv > 15 and speed != 20) != (speed > 15 and speed != 20):
        triggered.add(11)
    # 变异规则 13 - ROR
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and -speed != 20):
        triggered.add(12)
    # 变异规则 14 - SAR
    if (voltage_mv > 15 and speed != 20) != (15 < voltage_mv and speed != 20):
        t = 1
    # 变异规则 15 - SCR
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and speed != 28):
        triggered.add(13)
    # 变异规则 16 - LCR
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 15 or speed != 20):
        triggered.add(14)
    # 变异规则 17 - ABS
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and abs(speed) != 20):
        t = 1
    # 变异规则 18 - CRP
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 11 and speed != 20):
        triggered.add(15)
    # 变异规则 19 - CSR
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and speed != -20):
        triggered.add(16)
    # 变异规则 20 - UOI
    if (voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and -speed != 20):
        triggered.add(17)
    # 原语句
    if voltage_mv > 15 and speed != 20:
        health_score += 15
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句3
    # 变异规则 21 - ROR
    if (voltage_mv > 20) != (voltage_mv > -20):
        triggered.add(18)
    # 变异规则 22 - AOR
    if (voltage_mv > 20) != (not (voltage_mv > 20)):
        triggered.add(19)
    # 变异规则 23 - SCR
    if (voltage_mv > 20) != (20 < voltage_mv):
        t = 1
    # 变异规则 24 - SVR
    if (voltage_mv > 20) != (altitude > 20):
        triggered.add(20)
    # 变异规则 25 - CSR
    if (voltage_mv > 20) != (voltage_mv > -20):
        triggered.add(21)
    # 变异规则 26 - UOI
    if (voltage_mv > 20) != (voltage_mv > -20):
        triggered.add(22)
    # 变异规则 27 - SAR
    if (voltage_mv > 20) != (20 < voltage_mv):
        t = 1
    # 变异规则 28 - CAR
    if (voltage_mv > 20) != (voltage_mv > 15):
        triggered.add(23)
    # 变异规则 29 - CRP
    if (voltage_mv > 20) != (voltage_mv > 26):
        triggered.add(24)
    # 变异规则 30 - SRC
    if (voltage_mv > 20) != (abs(voltage_mv) > 20):
        t = 1
    # 原语句
    if voltage_mv > 20:
        health_score += 16
        altitude = min(altitude + 18, 1000)
    # 原语句4
    # 变异规则 31 - ROR
    if (voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 30 or voltage_mv > 98):
        t = 1
    # 变异规则 32 - LCR
    if (voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 30 and voltage_mv > 100):
        triggered.add(25)
    # 变异规则 33 - ABS
    if (voltage_mv > 30 or voltage_mv > 100) != (abs(voltage_mv) > 30 or voltage_mv > 100):
        t = 1
    # 变异规则 34 - UOI
    if (voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 30 or -voltage_mv > 100):
        t = 1
    # 变异规则 35 - CAR
    if (voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 31 or voltage_mv > 100):
        triggered.add(26)
    # 变异规则 36 - CRP
    if (voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 26 or voltage_mv > 100):
        triggered.add(27)
    # 变异规则 37 - SAR
    if (voltage_mv > 30 or voltage_mv > 100) != (30 < voltage_mv or voltage_mv > 100):
        t = 1
    # 变异规则 38 - SCR
    if (voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > -30 or voltage_mv > 100):
        triggered.add(28)
    # 变异规则 39 - RSR
    if (voltage_mv > 30 or voltage_mv > 100) != (not (voltage_mv > 30 or voltage_mv > 100)):
        triggered.add(29)
    # 变异规则 40 - CSR
    if (voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > -30 or voltage_mv > 100):
        triggered.add(30)
    # 原语句
    if voltage_mv > 30 or voltage_mv > 100:
        health_score += 13
        voltage_mv = max(voltage_mv - 4, 2)
    # 原语句5
    # 变异规则 41 - LCR
    if (speed * voltage_mv == 30) != (altitude * voltage_mv == 30):
        triggered.add(31)
    # 变异规则 42 - SVR
    if (speed * voltage_mv == 30) != (altitude * voltage_mv == 30):
        triggered.add(32)
    # 变异规则 43 - CAR
    if (speed * voltage_mv == 30) != (speed * voltage_mv == 31):
        triggered.add(33)
    # 变异规则 44 - SRC
    if (speed * voltage_mv == 30) != (not (speed * voltage_mv == 30)):
        triggered.add(34)
    # 变异规则 45 - SCR
    if (speed * voltage_mv == 30) != (altitude * voltage_mv == 30):
        triggered.add(35)
    # 变异规则 46 - UOI
    if (speed * voltage_mv == 30) != (speed * -voltage_mv == 30):
        triggered.add(36)
    # 变异规则 47 - SAR
    if (speed * voltage_mv == 30) != (speed * 30 == voltage_mv):
        triggered.add(37)
    # 变异规则 48 - CRP
    if (speed * voltage_mv == 30) != (speed * voltage_mv == 28):
        triggered.add(38)
    # 变异规则 49 - ABS
    if (speed * voltage_mv == 30) != (abs(speed) * voltage_mv == 30):
        t = 1
    # 变异规则 50 - AOR
    if (speed * voltage_mv == 30) != (not (speed * voltage_mv == 30)):
        triggered.add(39)
    # 原语句
    if speed * voltage_mv == 30:
        health_score -= 20
        altitude = min(altitude + 66, 1000)
    # 原语句6
    # 变异规则 51 - SAR
    if (altitude == 200 or speed >= 96) != (altitude == 200 or 96 <= speed):
        t = 1
    # 变异规则 52 - CSR
    if (altitude == 200 or speed >= 96) != (altitude == -200 or speed >= 96):
        triggered.add(40)
    # 变异规则 53 - ROR
    if (altitude == 200 or speed >= 96) != (altitude == 200 or -speed >= 96):
        triggered.add(41)
    # 变异规则 54 - AOR
    if (altitude == 200 or speed >= 96) != (altitude == 200 or speed >= -96):
        triggered.add(42)
    # 变异规则 55 - UOI
    if (altitude == 200 or speed >= 96) != (altitude == 200 or -speed >= 96):
        triggered.add(43)
    # 变异规则 56 - SVR
    if (altitude == 200 or speed >= 96) != (speed == 200 or speed >= 96):
        triggered.add(44)
    # 变异规则 57 - CRP
    if (altitude == 200 or speed >= 96) != (altitude == 200 or speed >= 93):
        triggered.add(45)
    # 变异规则 58 - LCR
    if (altitude == 200 or speed >= 96) != (altitude == 200 and speed >= 96):
        triggered.add(46)
    # 变异规则 59 - CAR
    if (altitude == 200 or speed >= 96) != (altitude == 200 or speed >= 86):
        triggered.add(47)
    # 变异规则 60 - SCR
    if (altitude == 200 or speed >= 96) != (altitude == 200 and speed >= 96):
        triggered.add(48)
    # 原语句
    if altitude == 200 or speed >= 96:
        health_score -= 20
        speed = min(speed + 7, 100)
    # 原语句7
    # 变异规则 61 - RSR
    if (speed > 20 and speed == 63) != (not (speed > 20 and speed == 63)):
        triggered.add(49)
    # 变异规则 62 - SAR
    if (speed > 20 and speed == 63) != (20 < speed and speed == 63):
        t = 1
    # 变异规则 63 - ROR
    if (speed > 20 and speed == 63) != (speed == 63 and speed > 20):
        t = 1
    # 变异规则 64 - SRC
    if (speed > 20 and speed == 63) != (speed == 63 and speed > 20):
        t = 1
    # 变异规则 65 - AOR
    if (speed > 20 and speed == 63) != (speed > 22 and speed == 63):
        t = 1
    # 变异规则 66 - CRP
    if (speed > 20 and speed == 63) != (speed > 20 and speed == 126):
        triggered.add(50)
    # 变异规则 67 - CSR
    if (speed > 20 and speed == 63) != (speed > -20 and speed == 63):
        t = 1
    # 变异规则 68 - LCR
    if (speed > 20 and speed == 63) != (speed > 20 or speed == 63):
        triggered.add(51)
    # 变异规则 69 - CAR
    if (speed > 20 and speed == 63) != (speed > 30 and speed == 63):
        t = 1
    # 变异规则 70 - UOI
    if (speed > 20 and speed == 63) != (speed > 20 and -speed == 63):
        triggered.add(52)
    # 原语句
    if speed > 20 and speed == 63:
        health_score += 18
    # 原语句8
    # 变异规则 71 - CSR
    if (speed > 16) != (speed > -16):
        triggered.add(53)
    # 变异规则 72 - CRP
    if (speed > 16) != (speed > 9):
        triggered.add(54)
    # 变异规则 73 - ROR
    if (speed > 16) != (voltage_mv > 16):
        triggered.add(55)
    # 变异规则 74 - SCR
    if (speed > 16) != (speed > -16):
        triggered.add(56)
    # 变异规则 75 - RSR
    if (speed > 16) != (not (speed > 16)):
        triggered.add(57)
    # 变异规则 76 - SRC
    if (speed > 16) != (16 < speed):
        t = 1
    # 变异规则 77 - LCR
    if (speed > 16) != (16 < speed):
        t = 1
    # 变异规则 78 - SVR
    if (speed > 16) != (altitude > 16):
        triggered.add(58)
    # 变异规则 79 - SAR
    if (speed > 16) != (16 < speed):
        t = 1
    # 变异规则 80 - ABS
    if (speed > 16) != (abs(speed) > 16):
        t = 1
    # 原语句
    if speed > 16:
        health_score -= 8
        altitude = min(altitude + 59, 1000)
        voltage_mv = max(voltage_mv - 4, 2)
    # 原语句9
    # 变异规则 81 - SVR
    if (12 <= voltage_mv <= 86) != (12 <= speed <= 86):
        triggered.add(59)
    # 变异规则 82 - AOR
    if (12 <= voltage_mv <= 86) != (voltage_mv >= 12 <= 86):
        triggered.add(60)
    # 变异规则 83 - SAR
    if (12 <= voltage_mv <= 86) != (voltage_mv >= 12 <= 86):
        triggered.add(61)
    # 变异规则 84 - LCR
    if (12 <= voltage_mv <= 86) != (12 <= altitude <= 86):
        triggered.add(62)
    # 变异规则 85 - ROR
    if (12 <= voltage_mv <= 86) != (12 <= abs(voltage_mv) <= 86):
        t = 1
    # 变异规则 86 - CAR
    if (12 <= voltage_mv <= 86) != (22 <= voltage_mv <= 86):
        triggered.add(63)
    # 变异规则 87 - UOI
    if (12 <= voltage_mv <= 86) != (12 <= -voltage_mv <= 86):
        triggered.add(64)
    # 变异规则 88 - SCR
    if (12 <= voltage_mv <= 86) != (not (12) <= voltage_mv <= 86):
        triggered.add(65)
    # 变异规则 89 - RSR
    if (12 <= voltage_mv <= 86) != (not (12 <= voltage_mv <= 86)):
        triggered.add(66)
    # 变异规则 90 - CSR
    if (12 <= voltage_mv <= 86) != (12 <= voltage_mv <= -86):
        triggered.add(67)
    # 原语句
    if 12 <= voltage_mv <= 86:
        health_score += 7
        altitude = max(altitude - 28, 2)
        voltage_mv = min(voltage_mv + 1, 100)
    # 原语句10
    # 变异规则 91 - SAR
    if (speed < 100) != (100 > speed):
        t = 1
    # 变异规则 92 - CSR
    if (speed < 100) != (speed < -100):
        triggered.add(68)
    # 变异规则 93 - SCR
    if (speed < 100) != (speed < 99):
        triggered.add(69)
    # 变异规则 94 - LCR
    if (speed < 100) != (100 > speed):
        t = 1
    # 变异规则 95 - SVR
    if (speed < 100) != (altitude < 100):
        triggered.add(70)
    # 变异规则 96 - SRC
    if (speed < 100) != (speed < 101):
        triggered.add(71)
    # 变异规则 97 - UOI
    if (speed < 100) != (speed < 102):
        triggered.add(72)
    # 变异规则 98 - AOR
    if (speed < 100) != (100 > speed):
        t = 1
    # 变异规则 99 - CRP
    if (speed < 100) != (speed < 200):
        triggered.add(73)
    # 变异规则 100 - RSR
    if (speed < 100) != (not (speed < 100)):
        triggered.add(74)
    # 原语句
    if speed < 100:
        health_score += 11
        voltage_mv = max(voltage_mv - 4, 2)
    # 原语句11
    # 变异规则 101 - RSR
    if (speed % 30 <= voltage_mv) != (not (speed % 30 <= voltage_mv)):
        triggered.add(75)
    # 变异规则 102 - CRP
    if (speed % 30 <= voltage_mv) != (speed % 26 <= voltage_mv):
        triggered.add(76)
    # 变异规则 103 - SCR
    if (speed % 30 <= voltage_mv) != (speed % 31 <= voltage_mv):
        triggered.add(77)
    # 变异规则 104 - UOI
    if (speed % 30 <= voltage_mv) != (speed % 30 <= -voltage_mv):
        triggered.add(78)
    # 变异规则 105 - SVR
    if (speed % 30 <= voltage_mv) != (altitude % 30 <= voltage_mv):
        triggered.add(79)
    # 变异规则 106 - ABS
    if (speed % 30 <= voltage_mv) != (abs(speed) % 30 <= voltage_mv):
        t = 1
    # 变异规则 107 - CAR
    if (speed % 30 <= voltage_mv) != (speed % 20 <= voltage_mv):
        triggered.add(80)
    # 变异规则 108 - CSR
    if (speed % 30 <= voltage_mv) != (speed % -30 <= voltage_mv):
        triggered.add(81)
    # 变异规则 109 - AOR
    if (speed % 30 <= voltage_mv) != (speed % -30 <= voltage_mv):
        triggered.add(82)
    # 变异规则 110 - SAR
    if (speed % 30 <= voltage_mv) != (speed % voltage_mv >= 30):
        triggered.add(83)
    # 原语句
    if speed % 30 <= voltage_mv:
        health_score -= 29
    # 原语句12
    # 变异规则 111 - LCR
    if (altitude == 500 and voltage_mv > 20) != (altitude == 500 or voltage_mv > 20):
        triggered.add(84)
    # 变异规则 112 - ABS
    if (altitude == 500 and voltage_mv > 20) != (abs(altitude) == 500 and voltage_mv > 20):
        t = 1
    # 变异规则 113 - ROR
    if (altitude == 500 and voltage_mv > 20) != (altitude == 500 and voltage_mv > -20):
        triggered.add(85)
    # 变异规则 114 - AOR
    if (altitude == 500 and voltage_mv > 20) != (abs(altitude) == 500 and voltage_mv > 20):
        t = 1
    # 变异规则 115 - SVR
    if (altitude == 500 and voltage_mv > 20) != (voltage_mv == 500 and voltage_mv > 20):
        triggered.add(86)
    # 变异规则 116 - SAR
    if (altitude == 500 and voltage_mv > 20) != (altitude == 500 and 20 < voltage_mv):
        t = 1
    # 变异规则 117 - UOI
    if (altitude == 500 and voltage_mv > 20) != (altitude == 500 and -voltage_mv > 20):
        triggered.add(87)
    # 变异规则 118 - RSR
    if (altitude == 500 and voltage_mv > 20) != (not (altitude == 500 and voltage_mv > 20)):
        triggered.add(88)
    # 变异规则 119 - SRC
    if (altitude == 500 and voltage_mv > 20) != (voltage_mv > 20 and altitude == 500):
        t = 1
    # 变异规则 120 - CAR
    if (altitude == 500 and voltage_mv > 20) != (altitude == 500 and voltage_mv > 19):
        triggered.add(89)
    # 原语句
    if altitude == 500 and voltage_mv > 20:
        health_score -= 17
        altitude = max(altitude - 48, 2)
        altitude, speed = speed, altitude
    # 原语句13
    # 变异规则 121 - CRP
    if (speed <= 2 and voltage_mv > 100) != (speed <= 2 and voltage_mv > 200):
        triggered.add(90)
    # 变异规则 122 - AOR
    if (speed <= 2 and voltage_mv > 100) != (speed <= -2 and voltage_mv > 100):
        triggered.add(91)
    # 变异规则 123 - CAR
    if (speed <= 2 and voltage_mv > 100) != (speed <= 2 and voltage_mv > 110):
        triggered.add(92)
    # 变异规则 124 - SRC
    if (speed <= 2 and voltage_mv > 100) != (voltage_mv > 100 and speed <= 2):
        t = 1
    # 变异规则 125 - SVR
    if (speed <= 2 and voltage_mv > 100) != (altitude <= 2 and voltage_mv > 100):
        triggered.add(93)
    # 变异规则 126 - CSR
    if (speed <= 2 and voltage_mv > 100) != (speed <= 2 and voltage_mv > -100):
        triggered.add(94)
    # 变异规则 127 - UOI
    if (speed <= 2 and voltage_mv > 100) != (speed <= 2 and -voltage_mv > 100):
        triggered.add(95)
    # 变异规则 128 - ABS
    if (speed <= 2 and voltage_mv > 100) != (abs(speed) <= 2 and voltage_mv > 100):
        t = 1
    # 变异规则 129 - SAR
    if (speed <= 2 and voltage_mv > 100) != (speed <= 2 and 100 < voltage_mv):
        t = 1
    # 变异规则 130 - ROR
    if (speed <= 2 and voltage_mv > 100) != (not (speed <= 2 and voltage_mv > 100)):
        triggered.add(96)
    # 原语句
    if speed <= 2 and voltage_mv > 100:
        health_score -= 24
        speed = min(speed + 3, 100)
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句14
    # 变异规则 131 - SCR
    if (speed != 30 or voltage_mv < 50) != (speed != 30 or -voltage_mv < 50):
        triggered.add(97)
    # 变异规则 132 - SAR
    if (speed != 30 or voltage_mv < 50) != (speed != 30 or 50 > voltage_mv):
        t = 1
    # 变异规则 133 - RSR
    if (speed != 30 or voltage_mv < 50) != (not (speed != 30 or voltage_mv < 50)):
        triggered.add(98)
    # 变异规则 134 - ROR
    if (speed != 30 or voltage_mv < 50) != (voltage_mv < 50 or speed != 30):
        t = 1
    # 变异规则 135 - SRC
    if (speed != 30 or voltage_mv < 50) != (voltage_mv < 50 or speed != 30):
        t = 1
    # 变异规则 136 - CAR
    if (speed != 30 or voltage_mv < 50) != (speed != 25 or voltage_mv < 50):
        triggered.add(99)
    # 变异规则 137 - LCR
    if (speed != 30 or voltage_mv < 50) != (speed != 30 and voltage_mv < 50):
        triggered.add(100)
    # 变异规则 138 - UOI
    if (speed != 30 or voltage_mv < 50) != (speed != 30 or -voltage_mv < 50):
        triggered.add(101)
    # 变异规则 139 - SVR
    if (speed != 30 or voltage_mv < 50) != (voltage_mv != 30 or voltage_mv < 50):
        triggered.add(102)
    # 变异规则 140 - AOR
    if (speed != 30 or voltage_mv < 50) != (speed != -30 or voltage_mv < 50):
        triggered.add(103)
    # 原语句
    if speed != 30 or voltage_mv < 50:
        health_score += 2
        voltage_mv = max(voltage_mv - 10, 2)
    # 原语句15
    # 变异规则 141 - LCR
    if (voltage_mv != 10 or voltage_mv > 5) != (voltage_mv != 10 and voltage_mv > 5):
        triggered.add(104)
    # 变异规则 142 - ROR
    if (voltage_mv != 10 or voltage_mv > 5) != (abs(voltage_mv) != 10 or voltage_mv > 5):
        t = 1
    # 变异规则 143 - CSR
    if (voltage_mv != 10 or voltage_mv > 5) != (voltage_mv != -10 or voltage_mv > 5):
        t = 1
    # 变异规则 144 - RSR
    if (voltage_mv != 10 or voltage_mv > 5) != (not (voltage_mv != 10 or voltage_mv > 5)):
        triggered.add(105)
    # 变异规则 145 - SAR
    if (voltage_mv != 10 or voltage_mv > 5) != (voltage_mv != 10 or 5 < voltage_mv):
        t = 1
    # 变异规则 146 - SRC
    if (voltage_mv != 10 or voltage_mv > 5) != (voltage_mv > 5 or voltage_mv != 10):
        t = 1
    # 变异规则 147 - SCR
    if (voltage_mv != 10 or voltage_mv > 5) != (voltage_mv != 10 or 5 < voltage_mv):
        t = 1
    # 变异规则 148 - AOR
    if (voltage_mv != 10 or voltage_mv > 5) != (voltage_mv != 5 or voltage_mv > 5):
        triggered.add(106)
    # 变异规则 149 - ABS
    if (voltage_mv != 10 or voltage_mv > 5) != (abs(voltage_mv) != 10 or voltage_mv > 5):
        t = 1
    # 变异规则 150 - SVR
    if (voltage_mv != 10 or voltage_mv > 5) != (altitude != 10 or voltage_mv > 5):
        triggered.add(107)
    # 原语句
    if voltage_mv != 10 or voltage_mv > 5:
        health_score += 8
        speed = max(speed - 10, 2)
        voltage_mv = min(voltage_mv + 10, 100)
    # 原语句16
    # 变异规则 151 - SVR
    if (altitude >= 39) != (speed >= 39):
        triggered.add(108)
    # 变异规则 152 - CAR
    if (altitude >= 39) != (altitude >= 34):
        triggered.add(109)
    # 变异规则 153 - ABS
    if (altitude >= 39) != (abs(altitude) >= 39):
        t = 1
    # 变异规则 154 - SRC
    if (altitude >= 39) != (39 <= altitude):
        t = 1
    # 变异规则 155 - CRP
    if (altitude >= 39) != (altitude >= 78):
        triggered.add(110)
    # 变异规则 156 - LCR
    if (altitude >= 39) != (39 <= altitude):
        t = 1
    # 变异规则 157 - ROR
    if (altitude >= 39) != (altitude >= -39):
        triggered.add(111)
    # 变异规则 158 - SAR
    if (altitude >= 39) != (39 <= altitude):
        t = 1
    # 变异规则 159 - RSR
    if (altitude >= 39) != (not (altitude >= 39)):
        triggered.add(112)
    # 变异规则 160 - AOR
    if (altitude >= 39) != (abs(altitude) >= 39):
        t = 1
    # 原语句
    if altitude >= 39:
        health_score += 2
        voltage_mv = min(voltage_mv + 5, 100)
    # 原语句17
    # 变异规则 161 - ROR
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and abs(speed) < 50):
        t = 1
    # 变异规则 162 - ABS
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and abs(speed) < 50):
        t = 1
    # 变异规则 163 - UOI
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and -speed < 50):
        triggered.add(113)
    # 变异规则 164 - CRP
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and speed < 59):
        triggered.add(114)
    # 变异规则 165 - LCR
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != 10 or speed < 50):
        triggered.add(115)
    # 变异规则 166 - SCR
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and 50 > speed):
        t = 1
    # 变异规则 167 - SAR
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and 50 > speed):
        t = 1
    # 变异规则 168 - SRC
    if (voltage_mv != 10 and speed < 50) != (speed < 50 and voltage_mv != 10):
        t = 1
    # 变异规则 169 - RSR
    if (voltage_mv != 10 and speed < 50) != (not (voltage_mv != 10 and speed < 50)):
        triggered.add(116)
    # 变异规则 170 - CSR
    if (voltage_mv != 10 and speed < 50) != (voltage_mv != -10 and speed < 50):
        t = 1
    # 原语句
    if voltage_mv != 10 and speed < 50:
        health_score += 7
        altitude = max(altitude - 26, 2)
        speed = max(speed - 8, 2)
    # 原语句18
    # 变异规则 171 - CRP
    if (12 <= speed <= 54) != (19 <= speed <= 54):
        triggered.add(117)
    # 变异规则 172 - CAR
    if (12 <= speed <= 54) != (12 <= speed <= 59):
        triggered.add(118)
    # 变异规则 173 - SVR
    if (12 <= speed <= 54) != (12 <= altitude <= 54):
        triggered.add(119)
    # 变异规则 174 - CSR
    if (12 <= speed <= 54) != (12 <= speed <= -54):
        triggered.add(120)
    # 变异规则 175 - LCR
    if (12 <= speed <= 54) != (12 <= speed <= 49):
        triggered.add(121)
    # 变异规则 176 - ROR
    if (12 <= speed <= 54) != (-12 <= speed <= 54):
        triggered.add(122)
    # 变异规则 177 - SAR
    if (12 <= speed <= 54) != (speed >= 12 <= 54):
        triggered.add(123)
    # 变异规则 178 - ABS
    if (12 <= speed <= 54) != (12 <= abs(speed) <= 54):
        t = 1
    # 变异规则 179 - RSR
    if (12 <= speed <= 54) != (not (12 <= speed <= 54)):
        triggered.add(124)
    # 变异规则 180 - AOR
    if (12 <= speed <= 54) != (12 <= -speed <= 54):
        triggered.add(125)
    # 原语句
    if 12 <= speed <= 54:
        health_score += 19
        altitude = min(altitude + 1, 1000)
    # 原语句19
    # 变异规则 181 - ROR
    if (261 <= altitude <= 844) != (-261 <= altitude <= 844):
        triggered.add(126)
    # 变异规则 182 - CAR
    if (261 <= altitude <= 844) != (251 <= altitude <= 844):
        triggered.add(127)
    # 变异规则 183 - ABS
    if (261 <= altitude <= 844) != (261 <= abs(altitude) <= 844):
        t = 1
    # 变异规则 184 - CSR
    if (261 <= altitude <= 844) != (261 <= altitude <= -844):
        triggered.add(128)
    # 变异规则 185 - AOR
    if (261 <= altitude <= 844) != (not (261 <= altitude <= 844)):
        triggered.add(129)
    # 变异规则 186 - UOI
    if (261 <= altitude <= 844) != (261 <= -altitude <= 844):
        triggered.add(130)
    # 变异规则 187 - SVR
    if (261 <= altitude <= 844) != (261 <= speed <= 844):
        triggered.add(131)
    # 变异规则 188 - CRP
    if (261 <= altitude <= 844) != (522 <= altitude <= 844):
        triggered.add(132)
    # 变异规则 189 - SRC
    if (261 <= altitude <= 844) != (261 <= altitude <= 849):
        triggered.add(133)
    # 变异规则 190 - LCR
    if (261 <= altitude <= 844) != (261 <= speed <= 844):
        triggered.add(134)
    # 原语句
    if 261 <= altitude <= 844:
        health_score += 10
        altitude = min(altitude + 37, 1000)
        speed = max(speed - 8, 2)
        voltage_mv = max(voltage_mv - 9, 2)
    # 原语句20
    # 变异规则 191 - SCR
    if (31 <= speed <= 98) != (not (31) <= speed <= 98):
        triggered.add(135)
    # 变异规则 192 - SVR
    if (31 <= speed <= 98) != (31 <= voltage_mv <= 98):
        triggered.add(136)
    # 变异规则 193 - ROR
    if (31 <= speed <= 98) != (31 <= voltage_mv <= 98):
        triggered.add(137)
    # 变异规则 194 - CAR
    if (31 <= speed <= 98) != (31 <= speed <= 97):
        t = 1
    # 变异规则 195 - AOR
    if (31 <= speed <= 98) != (31 <= voltage_mv <= 98):
        triggered.add(138)
    # 变异规则 196 - SRC
    if (31 <= speed <= 98) != (not (31 <= speed <= 98)):
        triggered.add(139)
    # 变异规则 197 - UOI
    if (31 <= speed <= 98) != (31 <= -speed <= 98):
        triggered.add(140)
    # 变异规则 198 - RSR
    if (31 <= speed <= 98) != (not (31 <= speed <= 98)):
        triggered.add(141)
    # 变异规则 199 - LCR
    if (31 <= speed <= 98) != (31 <= speed <= 49):
        triggered.add(142)
    # 变异规则 200 - ABS
    if (31 <= speed <= 98) != (31 <= abs(speed) <= 98):
        t = 1
    # 原语句
    if 31 <= speed <= 98:
        health_score += 4
        speed = min(speed + 1, 100)
    # 原语句21
    # 变异规则 201 - ROR
    if (voltage_mv >= 56) != (voltage_mv >= 59):
        triggered.add(143)
    # 变异规则 202 - LCR
    if (voltage_mv >= 56) != (voltage_mv >= 54):
        triggered.add(144)
    # 变异规则 203 - SVR
    if (voltage_mv >= 56) != (speed >= 56):
        triggered.add(145)
    # 变异规则 204 - SCR
    if (voltage_mv >= 56) != (voltage_mv >= 61):
        triggered.add(146)
    # 变异规则 205 - SRC
    if (voltage_mv >= 56) != (not (voltage_mv >= 56)):
        triggered.add(147)
    # 变异规则 206 - CRP
    if (voltage_mv >= 56) != (voltage_mv >= 28):
        triggered.add(148)
    # 变异规则 207 - UOI
    if (voltage_mv >= 56) != (voltage_mv >= -56):
        triggered.add(149)
    # 变异规则 208 - AOR
    if (voltage_mv >= 56) != (abs(voltage_mv) >= 56):
        t = 1
    # 变异规则 209 - RSR
    if (voltage_mv >= 56) != (not (voltage_mv >= 56)):
        triggered.add(150)
    # 变异规则 210 - CSR
    if (voltage_mv >= 56) != (voltage_mv >= -56):
        triggered.add(151)
    # 原语句
    if voltage_mv >= 56:
        health_score -= 22
        voltage_mv = min(voltage_mv + 4, 100)
        altitude, speed = speed, altitude
    # 原语句22
    # 变异规则 211 - ROR
    if (speed * 80 != altitude) != (speed * altitude != 80):
        triggered.add(152)
    # 变异规则 212 - SCR
    if (speed * 80 != altitude) != (speed * 80 != -altitude):
        triggered.add(153)
    # 变异规则 213 - CAR
    if (speed * 80 != altitude) != (speed * 75 != altitude):
        triggered.add(154)
    # 变异规则 214 - AOR
    if (speed * 80 != altitude) != (not (speed * 80 != altitude)):
        triggered.add(155)
    # 变异规则 215 - SVR
    if (speed * 80 != altitude) != (altitude * 80 != altitude):
        triggered.add(156)
    # 变异规则 216 - UOI
    if (speed * 80 != altitude) != (speed * 80 != -altitude):
        triggered.add(157)
    # 变异规则 217 - CSR
    if (speed * 80 != altitude) != (speed * -80 != altitude):
        triggered.add(158)
    # 变异规则 218 - LCR
    if (speed * 80 != altitude) != (speed * 80 != -altitude):
        triggered.add(159)
    # 变异规则 219 - RSR
    if (speed * 80 != altitude) != (not (speed * 80 != altitude)):
        triggered.add(160)
    # 变异规则 220 - SAR
    if (speed * 80 != altitude) != (speed * altitude != 80):
        triggered.add(161)
    # 原语句
    if speed * 80 != altitude:
        health_score -= 22
        altitude = min(altitude + 83, 1000)
        speed = max(speed - 7, 2)
        speed, voltage_mv = voltage_mv, speed
    # 原语句23
    # 变异规则 221 - AOR
    if (voltage_mv <= 5 or voltage_mv > 91) != (altitude <= 5 or voltage_mv > 91):
        triggered.add(162)
    # 变异规则 222 - SCR
    if (voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 and voltage_mv > 91):
        triggered.add(163)
    # 变异规则 223 - SVR
    if (voltage_mv <= 5 or voltage_mv > 91) != (altitude <= 5 or voltage_mv > 91):
        triggered.add(164)
    # 变异规则 224 - ABS
    if (voltage_mv <= 5 or voltage_mv > 91) != (abs(voltage_mv) <= 5 or voltage_mv > 91):
        t = 1
    # 变异规则 225 - LCR
    if (voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 and voltage_mv > 91):
        triggered.add(165)
    # 变异规则 226 - UOI
    if (voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or -voltage_mv > 91):
        triggered.add(166)
    # 变异规则 227 - CRP
    if (voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or voltage_mv > 81):
        triggered.add(167)
    # 变异规则 228 - SAR
    if (voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or 91 < voltage_mv):
        t = 1
    # 变异规则 229 - CAR
    if (voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or voltage_mv > 96):
        triggered.add(168)
    # 变异规则 230 - ROR
    if (voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or -voltage_mv > 91):
        triggered.add(169)
    # 原语句
    if voltage_mv <= 5 or voltage_mv > 91:
        health_score -= 23
        altitude = min(altitude + 11, 1000)
        speed = max(speed - 9, 2)
        voltage_mv = max(voltage_mv - 1, 2)
        speed, voltage_mv = voltage_mv, speed
    # 原语句24
    # 变异规则 231 - ABS
    if (speed > 20) != (abs(speed) > 20):
        t = 1
    # 变异规则 232 - SCR
    if (speed > 20) != (speed > -20):
        triggered.add(170)
    # 变异规则 233 - CRP
    if (speed > 20) != (speed > 21):
        triggered.add(171)
    # 变异规则 234 - SVR
    if (speed > 20) != (altitude > 20):
        triggered.add(172)
    # 变异规则 235 - RSR
    if (speed > 20) != (not (speed > 20)):
        triggered.add(173)
    # 变异规则 236 - LCR
    if (speed > 20) != (speed > -20):
        triggered.add(174)
    # 变异规则 237 - CAR
    if (speed > 20) != (speed > 30):
        triggered.add(175)
    # 变异规则 238 - SAR
    if (speed > 20) != (20 < speed):
        t = 1
    # 变异规则 239 - AOR
    if (speed > 20) != (speed > 40):
        triggered.add(176)
    # 变异规则 240 - ROR
    if (speed > 20) != (20 < speed):
        t = 1
    # 原语句
    if speed > 20:
        health_score -= 26
        altitude = max(altitude - 2, 2)
    # 原语句25
    # 变异规则 241 - ABS
    if (5 <= voltage_mv <= 93) != (5 <= abs(voltage_mv) <= 93):
        t = 1
    # 变异规则 242 - SVR
    if (5 <= voltage_mv <= 93) != (5 <= altitude <= 93):
        triggered.add(177)
    # 变异规则 243 - SRC
    if (5 <= voltage_mv <= 93) != (not (5) <= voltage_mv <= 93):
        triggered.add(178)
    # 变异规则 244 - CRP
    if (5 <= voltage_mv <= 93) != (5 <= voltage_mv <= 186):
        t = 1
    # 变异规则 245 - CSR
    if (5 <= voltage_mv <= 93) != (-5 <= voltage_mv <= 93):
        triggered.add(179)
    # 变异规则 246 - SAR
    if (5 <= voltage_mv <= 93) != (voltage_mv >= 5 <= 93):
        t = 1
    # 变异规则 247 - ROR
    if (5 <= voltage_mv <= 93) != (5 <= -voltage_mv <= 93):
        triggered.add(180)
    # 变异规则 248 - AOR
    if (5 <= voltage_mv <= 93) != (voltage_mv >= 5 <= 93):
        t = 1
    # 变异规则 249 - RSR
    if (5 <= voltage_mv <= 93) != (not (5 <= voltage_mv <= 93)):
        triggered.add(181)
    # 变异规则 250 - UOI
    if (5 <= voltage_mv <= 93) != (5 <= -voltage_mv <= 93):
        triggered.add(182)
    # 原语句
    if 5 <= voltage_mv <= 93:
        health_score -= 27
    # 原语句26
    # 变异规则 251 - CRP
    if (altitude < 2) != (altitude < 3):
        t = 1
    # 变异规则 252 - CSR
    if (altitude < 2) != (altitude < -2):
        t = 1
    # 变异规则 253 - SCR
    if (altitude < 2) != (abs(altitude) < 2):
        t = 1
    # 变异规则 254 - SRC
    if (altitude < 2) != (voltage_mv < 2):
        t = 1
    # 变异规则 255 - ABS
    if (altitude < 2) != (abs(altitude) < 2):
        t = 1
    # 变异规则 256 - UOI
    if (altitude < 2) != (altitude < -2):
        t = 1
    # 变异规则 257 - RSR
    if (altitude < 2) != (not (altitude < 2)):
        triggered.add(183)
    # 变异规则 258 - LCR
    if (altitude < 2) != (not (altitude < 2)):
        triggered.add(184)
    # 变异规则 259 - ROR
    if (altitude < 2) != (speed < 2):
        t = 1
    # 变异规则 260 - SAR
    if (altitude < 2) != (2 > altitude):
        t = 1
    # 原语句
    if altitude < 2:
        health_score -= 29
        voltage_mv = min(voltage_mv + 7, 100)
    # 原语句27
    # 变异规则 261 - AOR
    if (altitude != 1000) != (speed != 1000):
        triggered.add(185)
    # 变异规则 262 - SAR
    if (altitude != 1000) != (1000 != altitude):
        t = 1
    # 变异规则 263 - CAR
    if (altitude != 1000) != (altitude != 1002):
        triggered.add(186)
    # 变异规则 264 - SVR
    if (altitude != 1000) != (voltage_mv != 1000):
        triggered.add(187)
    # 变异规则 265 - RSR
    if (altitude != 1000) != (not (altitude != 1000)):
        triggered.add(188)
    # 变异规则 266 - SCR
    if (altitude != 1000) != (altitude != 995):
        triggered.add(189)
    # 变异规则 267 - ABS
    if (altitude != 1000) != (abs(altitude) != 1000):
        t = 1
    # 变异规则 268 - UOI
    if (altitude != 1000) != (not (altitude != 1000)):
        triggered.add(190)
    # 变异规则 269 - ROR
    if (altitude != 1000) != (voltage_mv != 1000):
        triggered.add(191)
    # 变异规则 270 - CRP
    if (altitude != 1000) != (altitude != 1009):
        triggered.add(192)
    # 原语句
    if altitude != 1000:
        health_score += 19
    # 原语句28
    # 变异规则 271 - AOR
    if (altitude == 513) != (altitude == 518):
        triggered.add(193)
    # 变异规则 272 - CRP
    if (altitude == 513) != (altitude == 509):
        triggered.add(194)
    # 变异规则 273 - SCR
    if (altitude == 513) != (abs(altitude) == 513):
        t = 1
    # 变异规则 274 - LCR
    if (altitude == 513) != (513 == altitude):
        t = 1
    # 变异规则 275 - CAR
    if (altitude == 513) != (altitude == 515):
        triggered.add(195)
    # 变异规则 276 - UOI
    if (altitude == 513) != (altitude == -513):
        triggered.add(196)
    # 变异规则 277 - RSR
    if (altitude == 513) != (not (altitude == 513)):
        triggered.add(197)
    # 变异规则 278 - SVR
    if (altitude == 513) != (voltage_mv == 513):
        triggered.add(198)
    # 变异规则 279 - SRC
    if (altitude == 513) != (altitude == 512):
        triggered.add(199)
    # 变异规则 280 - SAR
    if (altitude == 513) != (513 == altitude):
        t = 1
    # 原语句
    if altitude == 513:
        health_score -= 4
    # 原语句29
    # 变异规则 281 - LCR
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != 10 or speed < 96):
        triggered.add(200)
    # 变异规则 282 - RSR
    if (voltage_mv != 10 and speed < 96) != (not (voltage_mv != 10 and speed < 96)):
        triggered.add(201)
    # 变异规则 283 - SRC
    if (voltage_mv != 10 and speed < 96) != (speed < 96 and voltage_mv != 10):
        t = 1
    # 变异规则 284 - UOI
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != 10 and -speed < 96):
        triggered.add(202)
    # 变异规则 285 - SAR
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != 10 and 96 > speed):
        t = 1
    # 变异规则 286 - CRP
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != 6 and speed < 96):
        triggered.add(203)
    # 变异规则 287 - CAR
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != 10 and speed < 94):
        triggered.add(204)
    # 变异规则 288 - ABS
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != 10 and abs(speed) < 96):
        t = 1
    # 变异规则 289 - AOR
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != -10 and speed < 96):
        triggered.add(205)
    # 变异规则 290 - CSR
    if (voltage_mv != 10 and speed < 96) != (voltage_mv != -10 and speed < 96):
        triggered.add(206)
    # 原语句
    if voltage_mv != 10 and speed < 96:
        health_score -= 24
    # 原语句30
    # 变异规则 291 - RSR
    if (speed >= 2) != (not (speed >= 2)):
        triggered.add(207)
    # 变异规则 292 - AOR
    if (speed >= 2) != (not (speed >= 2)):
        triggered.add(208)
    # 变异规则 293 - UOI
    if (speed >= 2) != (not (speed >= 2)):
        triggered.add(209)
    # 变异规则 294 - CAR
    if (speed >= 2) != (speed >= 1):
        t = 1
    # 变异规则 295 - SVR
    if (speed >= 2) != (altitude >= 2):
        t = 1
    # 变异规则 296 - SAR
    if (speed >= 2) != (2 <= speed):
        t = 1
    # 变异规则 297 - CSR
    if (speed >= 2) != (speed >= -2):
        t = 1
    # 变异规则 298 - CRP
    if (speed >= 2) != (speed >= 4):
        triggered.add(210)
    # 变异规则 299 - ROR
    if (speed >= 2) != (2 <= speed):
        t = 1
    # 变异规则 300 - SCR
    if (speed >= 2) != (speed >= 4):
        triggered.add(211)
    # 原语句
    if speed >= 2:
        health_score -= 21
        speed = max(speed - 8, 2)
        altitude, speed = speed, altitude
    return triggered


targetPaths = [
    {5, 14, 18, 19, 28, 29, 34, 42, 49, 53, 57, 65, 66, 68, 74, 75, 78, 83, 88, 94, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 18, 19, 28, 29, 34, 42, 49, 53, 57, 65, 66, 68, 74, 75, 78, 83, 88, 94, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 15, 18, 19, 28, 29, 34, 42, 49, 53, 57, 59, 62, 63, 64, 65, 66, 67, 68, 74, 75, 78, 83, 88, 94, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 15, 18, 19, 28, 29, 34, 38, 42, 49, 53, 57, 59, 62, 63, 64, 65, 66, 67, 68, 74, 75, 78, 83, 88, 94, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 15, 18, 19, 28, 29, 33, 34, 36, 37, 38, 42, 49, 53, 57, 58, 59, 63, 64, 65, 66, 67, 68, 74, 75, 78, 83, 88, 94, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 18, 19, 28, 29, 34, 42, 49, 53, 57, 62, 65, 66, 68, 74, 75, 78, 79, 83, 88, 94, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 18, 19, 20, 28, 29, 34, 42, 49, 53, 57, 58, 62, 65, 66, 68, 74, 75, 78, 79, 83, 88, 94, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 18, 19, 20, 28, 29, 34, 42, 49, 53, 57, 58, 62, 65, 66, 68, 74, 75, 78, 79, 83, 88, 94, 96, 98, 104, 105, 109, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 18, 19, 20, 28, 29, 34, 42, 49, 53, 57, 58, 62, 65, 66, 68, 74, 75, 78, 79, 83, 88, 94, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 152, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 14, 18, 19, 28, 29, 34, 42, 49, 53, 57, 65, 66, 68, 74, 75, 79, 81, 88, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 18, 19, 28, 29, 31, 33, 34, 36, 37, 38, 42, 49, 53, 57, 58, 62, 65, 66, 68, 74, 75, 78, 79, 83, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 14, 18, 19, 28, 29, 34, 42, 49, 53, 54, 57, 65, 66, 68, 74, 75, 79, 81, 88, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 18, 19, 20, 28, 29, 31, 33, 34, 36, 37, 38, 42, 49, 53, 54, 57, 58, 59, 65, 66, 68, 70, 74, 75, 81, 88, 96, 98, 104, 105, 108, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 79, 81, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 18, 19, 28, 29, 34, 42, 49, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 79, 80, 81, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 18, 19, 23, 28, 29, 34, 42, 49, 55, 57, 58, 63, 64, 65, 66, 67, 68, 74, 75, 79, 80, 81, 88, 96, 98, 104, 105, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 24, 28, 29, 34, 42, 49, 57, 63, 64, 65, 66, 67, 68, 74, 75, 80, 81, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 200, 201, 203, 205, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 24, 28, 29, 34, 42, 49, 57, 63, 64, 65, 66, 67, 68, 74, 75, 80, 81, 88, 96, 98, 104, 105, 106, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 27, 28, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 79, 83, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 27, 28, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 83, 84, 88, 96, 98, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 27, 28, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 83, 84, 88, 96, 98, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 148, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 25, 26, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 79, 83, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 25, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 83, 84, 88, 96, 98, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 147, 148, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 25, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 83, 84, 88, 96, 98, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 144, 147, 148, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 25, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 83, 84, 88, 96, 98, 100, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 144, 147, 148, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 20, 25, 29, 34, 42, 49, 57, 64, 65, 66, 67, 68, 74, 75, 78, 83, 84, 88, 96, 98, 100, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 143, 145, 146, 147, 155, 173, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 12, 13, 14, 16, 19, 20, 25, 29, 34, 42, 49, 57, 59, 60, 62, 65, 66, 68, 74, 75, 78, 83, 84, 88, 96, 98, 100, 105, 108, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 145, 147, 155, 173, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 12, 13, 14, 16, 19, 20, 25, 29, 34, 42, 49, 57, 59, 60, 62, 65, 66, 68, 74, 75, 78, 83, 84, 88, 96, 98, 100, 105, 108, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 145, 147, 155, 173, 178, 180, 181, 183, 188, 197, 201, 204, 207},
    {5, 12, 13, 14, 16, 19, 20, 25, 29, 34, 42, 49, 57, 59, 60, 62, 65, 66, 68, 74, 75, 78, 83, 84, 88, 96, 98, 100, 105, 108, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 145, 147, 155, 173, 178, 180, 181, 183, 188, 197, 200, 201, 202, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 51, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 79, 80, 81, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 51, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 76, 79, 81, 88, 96, 98, 104, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 51, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 76, 77, 78, 80, 83, 88, 96, 98, 100, 104, 105, 108, 110, 112, 116, 117, 120, 124, 125, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 51, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 79, 81, 88, 96, 98, 104, 105, 110, 112, 116, 120, 124, 125, 126, 129, 135, 136, 139, 140, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 51, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 76, 77, 78, 83, 88, 96, 98, 104, 105, 110, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 126, 129, 135, 136, 139, 140, 142, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 50, 52, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 77, 79, 81, 88, 96, 98, 104, 105, 110, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 126, 129, 135, 136, 139, 140, 142, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 49, 51, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 79, 81, 88, 96, 98, 104, 105, 110, 112, 113, 114, 115, 116, 118, 123, 124, 126, 129, 135, 136, 139, 140, 142, 145, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 47, 49, 51, 55, 57, 58, 59, 62, 65, 66, 68, 74, 75, 79, 81, 88, 96, 98, 104, 105, 110, 112, 113, 115, 116, 123, 124, 126, 129, 135, 136, 139, 140, 142, 145, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 42, 45, 47, 49, 51, 55, 57, 58, 62, 65, 66, 68, 74, 75, 77, 79, 81, 88, 96, 98, 104, 105, 110, 112, 113, 115, 116, 123, 124, 126, 129, 135, 136, 139, 140, 142, 145, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 28, 29, 34, 41, 46, 49, 51, 55, 57, 58, 62, 65, 66, 70, 71, 72, 73, 74, 75, 79, 80, 81, 88, 96, 98, 104, 105, 110, 112, 113, 115, 116, 123, 124, 126, 129, 135, 136, 139, 140, 142, 145, 147, 149, 155, 167, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 14, 18, 19, 28, 29, 34, 42, 49, 53, 57, 65, 66, 68, 74, 75, 78, 79, 83, 88, 94, 96, 98, 104, 105, 107, 111, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 18, 19, 23, 28, 29, 34, 41, 46, 49, 51, 57, 58, 59, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 78, 79, 83, 88, 96, 98, 105, 110, 112, 113, 115, 116, 119, 123, 124, 126, 129, 135, 136, 139, 140, 142, 145, 147, 149, 155, 167, 171, 173, 175, 176, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 12, 13, 14, 16, 19, 25, 29, 34, 42, 49, 57, 59, 60, 65, 66, 68, 70, 74, 75, 78, 83, 84, 88, 96, 98, 100, 105, 108, 112, 116, 122, 124, 126, 129, 135, 136, 139, 145, 147, 155, 163, 166, 168, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 19, 20, 25, 29, 34, 42, 49, 51, 57, 62, 64, 65, 66, 67, 68, 74, 75, 78, 83, 84, 88, 96, 98, 99, 100, 105, 108, 110, 112, 116, 119, 122, 124, 126, 129, 135, 136, 139, 144, 147, 148, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 19, 20, 25, 29, 34, 42, 49, 51, 57, 62, 64, 65, 66, 67, 68, 74, 75, 78, 84, 88, 96, 97, 98, 99, 102, 103, 105, 108, 110, 112, 116, 117, 120, 124, 125, 126, 129, 135, 136, 139, 145, 147, 155, 173, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 19, 20, 29, 34, 42, 49, 53, 55, 57, 58, 60, 62, 65, 66, 68, 74, 75, 78, 83, 84, 88, 90, 91, 92, 93, 95, 96, 98, 105, 108, 112, 116, 122, 124, 126, 129, 135, 136, 139, 147, 148, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 18, 19, 20, 28, 29, 31, 33, 34, 36, 37, 38, 42, 49, 53, 57, 58, 65, 66, 68, 70, 74, 75, 78, 79, 83, 88, 96, 98, 104, 105, 108, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 154, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 18, 19, 20, 28, 29, 31, 33, 34, 36, 37, 38, 42, 49, 53, 57, 58, 65, 66, 68, 70, 74, 75, 78, 83, 88, 96, 98, 104, 105, 108, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 152, 153, 154, 155, 156, 158, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 10, 14, 15, 18, 19, 20, 28, 29, 31, 33, 34, 36, 37, 38, 40, 44, 46, 49, 53, 57, 58, 59, 62, 63, 64, 65, 66, 67, 68, 70, 74, 75, 78, 79, 83, 88, 96, 98, 104, 105, 108, 112, 116, 122, 124, 126, 129, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 79, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 126, 127, 129, 135, 136, 139, 140, 142, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 40, 44, 46, 49, 51, 55, 57, 65, 66, 68, 69, 70, 74, 75, 81, 88, 96, 98, 104, 105, 112, 113, 115, 116, 123, 124, 126, 127, 129, 135, 136, 139, 140, 142, 145, 147, 149, 155, 167, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 79, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 128, 129, 130, 131, 132, 135, 136, 139, 140, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 79, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 128, 129, 130, 131, 132, 135, 136, 139, 140, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 194, 197, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 128, 129, 130, 131, 132, 135, 136, 139, 140, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 199, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 128, 129, 130, 131, 132, 135, 136, 139, 140, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 193, 194, 195, 196, 197, 198, 199, 201, 207},
    {5, 12, 13, 14, 16, 19, 25, 29, 34, 42, 49, 57, 59, 60, 65, 66, 68, 70, 74, 75, 78, 83, 86, 87, 88, 96, 98, 100, 105, 108, 111, 112, 113, 115, 116, 119, 123, 124, 126, 129, 131, 135, 136, 139, 147, 155, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 10, 14, 18, 19, 20, 28, 29, 31, 33, 34, 36, 37, 38, 42, 49, 53, 57, 58, 65, 66, 68, 70, 74, 75, 78, 79, 83, 84, 85, 88, 96, 98, 104, 105, 108, 112, 116, 122, 124, 128, 129, 130, 131, 132, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 178, 179, 181, 183, 188, 197, 201, 207, 210},
    {5, 12, 13, 14, 16, 19, 27, 28, 29, 34, 42, 49, 57, 62, 64, 65, 66, 67, 68, 70, 74, 75, 78, 83, 84, 85, 88, 89, 96, 98, 104, 105, 108, 112, 116, 122, 124, 128, 129, 130, 131, 132, 135, 139, 147, 149, 155, 162, 163, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207, 210},
    {5, 6, 11, 14, 18, 19, 20, 28, 29, 34, 41, 46, 49, 51, 55, 57, 65, 66, 71, 72, 73, 74, 75, 80, 81, 88, 96, 98, 104, 105, 112, 113, 115, 116, 123, 124, 128, 129, 130, 131, 135, 136, 139, 140, 142, 145, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {1, 2, 3, 4, 5, 6, 7, 8, 11, 14, 18, 19, 20, 28, 29, 34, 41, 46, 49, 51, 55, 57, 65, 66, 71, 72, 73, 74, 75, 80, 81, 88, 96, 98, 104, 105, 112, 113, 115, 116, 123, 124, 128, 129, 130, 131, 135, 136, 139, 140, 142, 145, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 79, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 129, 133, 135, 136, 139, 140, 142, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 197, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 79, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 129, 135, 136, 139, 140, 142, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 188, 189, 197, 201, 207},
    {5, 11, 14, 18, 19, 20, 28, 29, 34, 42, 49, 51, 55, 57, 59, 65, 66, 68, 70, 74, 75, 76, 77, 78, 79, 83, 88, 96, 98, 104, 105, 112, 113, 114, 115, 116, 119, 120, 121, 124, 125, 129, 135, 136, 139, 140, 142, 147, 149, 155, 170, 172, 173, 177, 178, 180, 181, 183, 185, 186, 187, 188, 189, 192, 197, 201, 207}
]


def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 2:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 12:11, 13:12, 15:13, 16:14, 18:15, 19:16, 20:17, 21:18, 22:19, 24:20, 25:21, 26:22, 28:23, 29:24, 32:25, 35:26, 36:27, 38:28, 39:29, 40:30, 41:31, 42:32, 43:33, 44:34, 45:35, 46:36, 47:37, 48:38, 50:39, 52:40, 53:41, 54:42, 55:43, 56:44, 57:45, 58:46, 59:47, 60:48, 61:49, 66:50, 68:51, 70:52, 71:53, 72:54, 73:55, 74:56, 75:57, 78:58, 81:59, 82:60, 83:61, 84:62, 86:63, 87:64, 88:65, 89:66, 90:67, 92:68, 93:69, 95:70, 96:71, 97:72, 99:73, 100:74, 101:75, 102:76, 103:77, 104:78, 105:79, 107:80, 108:81, 109:82, 110:83, 111:84, 113:85, 115:86, 117:87, 118:88, 120:89, 121:90, 122:91, 123:92, 125:93, 126:94, 127:95, 130:96, 131:97, 133:98, 136:99, 137:100, 138:101, 139:102, 140:103, 141:104, 144:105, 148:106, 150:107, 151:108, 152:109, 155:110, 157:111, 159:112, 163:113, 164:114, 165:115, 169:116, 171:117, 172:118, 173:119, 174:120, 175:121, 176:122, 177:123, 179:124, 180:125, 181:126, 182:127, 184:128, 185:129, 186:130, 187:131, 188:132, 189:133, 190:134, 191:135, 192:136, 193:137, 195:138, 196:139, 197:140, 198:141, 199:142, 201:143, 202:144, 203:145, 204:146, 205:147, 206:148, 207:149, 209:150, 210:151, 211:152, 212:153, 213:154, 214:155, 215:156, 216:157, 217:158, 218:159, 219:160, 220:161, 221:162, 222:163, 223:164, 225:165, 226:166, 227:167, 229:168, 230:169, 232:170, 233:171, 234:172, 235:173, 236:174, 237:175, 239:176, 242:177, 243:178, 245:179, 247:180, 249:181, 250:182, 257:183, 258:184, 261:185, 263:186, 264:187, 265:188, 266:189, 268:190, 269:191, 270:192, 271:193, 272:194, 275:195, 276:196, 277:197, 278:198, 279:199, 281:200, 282:201, 284:202, 286:203, 287:204, 289:205, 290:206, 291:207, 292:208, 293:209, 298:210, 300:211}

    rule_expressions[1] = "(altitude + speed != 616) != (voltage_mv + speed != 616)"
    rule_expressions[2] = "(altitude + speed != 616) != (altitude + 616 != speed)"
    rule_expressions[3] = "(altitude + speed != 616) != (altitude + speed != 621)"
    rule_expressions[4] = "(altitude + speed != 616) != (altitude + -speed != 616)"
    rule_expressions[5] = "(altitude + speed != 616) != (not (altitude + speed != 616))"
    rule_expressions[6] = "(altitude + speed != 616) != (altitude + speed != 615)"
    rule_expressions[7] = "(altitude + speed != 616) != (altitude + speed != 626)"
    rule_expressions[8] = "(altitude + speed != 616) != (altitude + speed != 617)"
    rule_expressions[9] = "(altitude + speed != 616) != (not (altitude + speed != 616))"
    rule_expressions[10] = "(voltage_mv > 15 and speed != 20) != (voltage_mv > 5 and speed != 20)"
    rule_expressions[11] = "(voltage_mv > 15 and speed != 20) != (speed > 15 and speed != 20)"
    rule_expressions[12] = "(voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and -speed != 20)"
    rule_expressions[13] = "(voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and speed != 28)"
    rule_expressions[14] = "(voltage_mv > 15 and speed != 20) != (voltage_mv > 15 or speed != 20)"
    rule_expressions[15] = "(voltage_mv > 15 and speed != 20) != (voltage_mv > 11 and speed != 20)"
    rule_expressions[16] = "(voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and speed != -20)"
    rule_expressions[17] = "(voltage_mv > 15 and speed != 20) != (voltage_mv > 15 and -speed != 20)"
    rule_expressions[18] = "(voltage_mv > 20) != (voltage_mv > -20)"
    rule_expressions[19] = "(voltage_mv > 20) != (not (voltage_mv > 20))"
    rule_expressions[20] = "(voltage_mv > 20) != (altitude > 20)"
    rule_expressions[21] = "(voltage_mv > 20) != (voltage_mv > -20)"
    rule_expressions[22] = "(voltage_mv > 20) != (voltage_mv > -20)"
    rule_expressions[23] = "(voltage_mv > 20) != (voltage_mv > 15)"
    rule_expressions[24] = "(voltage_mv > 20) != (voltage_mv > 26)"
    rule_expressions[25] = "(voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 30 and voltage_mv > 100)"
    rule_expressions[26] = "(voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 31 or voltage_mv > 100)"
    rule_expressions[27] = "(voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > 26 or voltage_mv > 100)"
    rule_expressions[28] = "(voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > -30 or voltage_mv > 100)"
    rule_expressions[29] = "(voltage_mv > 30 or voltage_mv > 100) != (not (voltage_mv > 30 or voltage_mv > 100))"
    rule_expressions[30] = "(voltage_mv > 30 or voltage_mv > 100) != (voltage_mv > -30 or voltage_mv > 100)"
    rule_expressions[31] = "(speed * voltage_mv == 30) != (altitude * voltage_mv == 30)"
    rule_expressions[32] = "(speed * voltage_mv == 30) != (altitude * voltage_mv == 30)"
    rule_expressions[33] = "(speed * voltage_mv == 30) != (speed * voltage_mv == 31)"
    rule_expressions[34] = "(speed * voltage_mv == 30) != (not (speed * voltage_mv == 30))"
    rule_expressions[35] = "(speed * voltage_mv == 30) != (altitude * voltage_mv == 30)"
    rule_expressions[36] = "(speed * voltage_mv == 30) != (speed * -voltage_mv == 30)"
    rule_expressions[37] = "(speed * voltage_mv == 30) != (speed * 30 == voltage_mv)"
    rule_expressions[38] = "(speed * voltage_mv == 30) != (speed * voltage_mv == 28)"
    rule_expressions[39] = "(speed * voltage_mv == 30) != (not (speed * voltage_mv == 30))"
    rule_expressions[40] = "(altitude == 200 or speed >= 96) != (altitude == -200 or speed >= 96)"
    rule_expressions[41] = "(altitude == 200 or speed >= 96) != (altitude == 200 or -speed >= 96)"
    rule_expressions[42] = "(altitude == 200 or speed >= 96) != (altitude == 200 or speed >= -96)"
    rule_expressions[43] = "(altitude == 200 or speed >= 96) != (altitude == 200 or -speed >= 96)"
    rule_expressions[44] = "(altitude == 200 or speed >= 96) != (speed == 200 or speed >= 96)"
    rule_expressions[45] = "(altitude == 200 or speed >= 96) != (altitude == 200 or speed >= 93)"
    rule_expressions[46] = "(altitude == 200 or speed >= 96) != (altitude == 200 and speed >= 96)"
    rule_expressions[47] = "(altitude == 200 or speed >= 96) != (altitude == 200 or speed >= 86)"
    rule_expressions[48] = "(altitude == 200 or speed >= 96) != (altitude == 200 and speed >= 96)"
    rule_expressions[49] = "(speed > 20 and speed == 63) != (not (speed > 20 and speed == 63))"
    rule_expressions[50] = "(speed > 20 and speed == 63) != (speed > 20 and speed == 126)"
    rule_expressions[51] = "(speed > 20 and speed == 63) != (speed > 20 or speed == 63)"
    rule_expressions[52] = "(speed > 20 and speed == 63) != (speed > 20 and -speed == 63)"
    rule_expressions[53] = "(speed > 16) != (speed > -16)"
    rule_expressions[54] = "(speed > 16) != (speed > 9)"
    rule_expressions[55] = "(speed > 16) != (voltage_mv > 16)"
    rule_expressions[56] = "(speed > 16) != (speed > -16)"
    rule_expressions[57] = "(speed > 16) != (not (speed > 16))"
    rule_expressions[58] = "(speed > 16) != (altitude > 16)"
    rule_expressions[59] = "(12 <= voltage_mv <= 86) != (12 <= speed <= 86)"
    rule_expressions[60] = "(12 <= voltage_mv <= 86) != (voltage_mv >= 12 <= 86)"
    rule_expressions[61] = "(12 <= voltage_mv <= 86) != (voltage_mv >= 12 <= 86)"
    rule_expressions[62] = "(12 <= voltage_mv <= 86) != (12 <= altitude <= 86)"
    rule_expressions[63] = "(12 <= voltage_mv <= 86) != (22 <= voltage_mv <= 86)"
    rule_expressions[64] = "(12 <= voltage_mv <= 86) != (12 <= -voltage_mv <= 86)"
    rule_expressions[65] = "(12 <= voltage_mv <= 86) != (not (12) <= voltage_mv <= 86)"
    rule_expressions[66] = "(12 <= voltage_mv <= 86) != (not (12 <= voltage_mv <= 86))"
    rule_expressions[67] = "(12 <= voltage_mv <= 86) != (12 <= voltage_mv <= -86)"
    rule_expressions[68] = "(speed < 100) != (speed < -100)"
    rule_expressions[69] = "(speed < 100) != (speed < 99)"
    rule_expressions[70] = "(speed < 100) != (altitude < 100)"
    rule_expressions[71] = "(speed < 100) != (speed < 101)"
    rule_expressions[72] = "(speed < 100) != (speed < 102)"
    rule_expressions[73] = "(speed < 100) != (speed < 200)"
    rule_expressions[74] = "(speed < 100) != (not (speed < 100))"
    rule_expressions[75] = "(speed % 30 <= voltage_mv) != (not (speed % 30 <= voltage_mv))"
    rule_expressions[76] = "(speed % 30 <= voltage_mv) != (speed % 26 <= voltage_mv)"
    rule_expressions[77] = "(speed % 30 <= voltage_mv) != (speed % 31 <= voltage_mv)"
    rule_expressions[78] = "(speed % 30 <= voltage_mv) != (speed % 30 <= -voltage_mv)"
    rule_expressions[79] = "(speed % 30 <= voltage_mv) != (altitude % 30 <= voltage_mv)"
    rule_expressions[80] = "(speed % 30 <= voltage_mv) != (speed % 20 <= voltage_mv)"
    rule_expressions[81] = "(speed % 30 <= voltage_mv) != (speed % -30 <= voltage_mv)"
    rule_expressions[82] = "(speed % 30 <= voltage_mv) != (speed % -30 <= voltage_mv)"
    rule_expressions[83] = "(speed % 30 <= voltage_mv) != (speed % voltage_mv >= 30)"
    rule_expressions[84] = "(altitude == 500 and voltage_mv > 20) != (altitude == 500 or voltage_mv > 20)"
    rule_expressions[85] = "(altitude == 500 and voltage_mv > 20) != (altitude == 500 and voltage_mv > -20)"
    rule_expressions[86] = "(altitude == 500 and voltage_mv > 20) != (voltage_mv == 500 and voltage_mv > 20)"
    rule_expressions[87] = "(altitude == 500 and voltage_mv > 20) != (altitude == 500 and -voltage_mv > 20)"
    rule_expressions[88] = "(altitude == 500 and voltage_mv > 20) != (not (altitude == 500 and voltage_mv > 20))"
    rule_expressions[89] = "(altitude == 500 and voltage_mv > 20) != (altitude == 500 and voltage_mv > 19)"
    rule_expressions[90] = "(speed <= 2 and voltage_mv > 100) != (speed <= 2 and voltage_mv > 200)"
    rule_expressions[91] = "(speed <= 2 and voltage_mv > 100) != (speed <= -2 and voltage_mv > 100)"
    rule_expressions[92] = "(speed <= 2 and voltage_mv > 100) != (speed <= 2 and voltage_mv > 110)"
    rule_expressions[93] = "(speed <= 2 and voltage_mv > 100) != (altitude <= 2 and voltage_mv > 100)"
    rule_expressions[94] = "(speed <= 2 and voltage_mv > 100) != (speed <= 2 and voltage_mv > -100)"
    rule_expressions[95] = "(speed <= 2 and voltage_mv > 100) != (speed <= 2 and -voltage_mv > 100)"
    rule_expressions[96] = "(speed <= 2 and voltage_mv > 100) != (not (speed <= 2 and voltage_mv > 100))"
    rule_expressions[97] = "(speed != 30 or voltage_mv < 50) != (speed != 30 or -voltage_mv < 50)"
    rule_expressions[98] = "(speed != 30 or voltage_mv < 50) != (not (speed != 30 or voltage_mv < 50))"
    rule_expressions[99] = "(speed != 30 or voltage_mv < 50) != (speed != 25 or voltage_mv < 50)"
    rule_expressions[100] = "(speed != 30 or voltage_mv < 50) != (speed != 30 and voltage_mv < 50)"
    rule_expressions[101] = "(speed != 30 or voltage_mv < 50) != (speed != 30 or -voltage_mv < 50)"
    rule_expressions[102] = "(speed != 30 or voltage_mv < 50) != (voltage_mv != 30 or voltage_mv < 50)"
    rule_expressions[103] = "(speed != 30 or voltage_mv < 50) != (speed != -30 or voltage_mv < 50)"
    rule_expressions[104] = "(voltage_mv != 10 or voltage_mv > 5) != (voltage_mv != 10 and voltage_mv > 5)"
    rule_expressions[105] = "(voltage_mv != 10 or voltage_mv > 5) != (not (voltage_mv != 10 or voltage_mv > 5))"
    rule_expressions[106] = "(voltage_mv != 10 or voltage_mv > 5) != (voltage_mv != 5 or voltage_mv > 5)"
    rule_expressions[107] = "(voltage_mv != 10 or voltage_mv > 5) != (altitude != 10 or voltage_mv > 5)"
    rule_expressions[108] = "(altitude >= 39) != (speed >= 39)"
    rule_expressions[109] = "(altitude >= 39) != (altitude >= 34)"
    rule_expressions[110] = "(altitude >= 39) != (altitude >= 78)"
    rule_expressions[111] = "(altitude >= 39) != (altitude >= -39)"
    rule_expressions[112] = "(altitude >= 39) != (not (altitude >= 39))"
    rule_expressions[113] = "(voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and -speed < 50)"
    rule_expressions[114] = "(voltage_mv != 10 and speed < 50) != (voltage_mv != 10 and speed < 59)"
    rule_expressions[115] = "(voltage_mv != 10 and speed < 50) != (voltage_mv != 10 or speed < 50)"
    rule_expressions[116] = "(voltage_mv != 10 and speed < 50) != (not (voltage_mv != 10 and speed < 50))"
    rule_expressions[117] = "(12 <= speed <= 54) != (19 <= speed <= 54)"
    rule_expressions[118] = "(12 <= speed <= 54) != (12 <= speed <= 59)"
    rule_expressions[119] = "(12 <= speed <= 54) != (12 <= altitude <= 54)"
    rule_expressions[120] = "(12 <= speed <= 54) != (12 <= speed <= -54)"
    rule_expressions[121] = "(12 <= speed <= 54) != (12 <= speed <= 49)"
    rule_expressions[122] = "(12 <= speed <= 54) != (-12 <= speed <= 54)"
    rule_expressions[123] = "(12 <= speed <= 54) != (speed >= 12 <= 54)"
    rule_expressions[124] = "(12 <= speed <= 54) != (not (12 <= speed <= 54))"
    rule_expressions[125] = "(12 <= speed <= 54) != (12 <= -speed <= 54)"
    rule_expressions[126] = "(261 <= altitude <= 844) != (-261 <= altitude <= 844)"
    rule_expressions[127] = "(261 <= altitude <= 844) != (251 <= altitude <= 844)"
    rule_expressions[128] = "(261 <= altitude <= 844) != (261 <= altitude <= -844)"
    rule_expressions[129] = "(261 <= altitude <= 844) != (not (261 <= altitude <= 844))"
    rule_expressions[130] = "(261 <= altitude <= 844) != (261 <= -altitude <= 844)"
    rule_expressions[131] = "(261 <= altitude <= 844) != (261 <= speed <= 844)"
    rule_expressions[132] = "(261 <= altitude <= 844) != (522 <= altitude <= 844)"
    rule_expressions[133] = "(261 <= altitude <= 844) != (261 <= altitude <= 849)"
    rule_expressions[134] = "(261 <= altitude <= 844) != (261 <= speed <= 844)"
    rule_expressions[135] = "(31 <= speed <= 98) != (not (31) <= speed <= 98)"
    rule_expressions[136] = "(31 <= speed <= 98) != (31 <= voltage_mv <= 98)"
    rule_expressions[137] = "(31 <= speed <= 98) != (31 <= voltage_mv <= 98)"
    rule_expressions[138] = "(31 <= speed <= 98) != (31 <= voltage_mv <= 98)"
    rule_expressions[139] = "(31 <= speed <= 98) != (not (31 <= speed <= 98))"
    rule_expressions[140] = "(31 <= speed <= 98) != (31 <= -speed <= 98)"
    rule_expressions[141] = "(31 <= speed <= 98) != (not (31 <= speed <= 98))"
    rule_expressions[142] = "(31 <= speed <= 98) != (31 <= speed <= 49)"
    rule_expressions[143] = "(voltage_mv >= 56) != (voltage_mv >= 59)"
    rule_expressions[144] = "(voltage_mv >= 56) != (voltage_mv >= 54)"
    rule_expressions[145] = "(voltage_mv >= 56) != (speed >= 56)"
    rule_expressions[146] = "(voltage_mv >= 56) != (voltage_mv >= 61)"
    rule_expressions[147] = "(voltage_mv >= 56) != (not (voltage_mv >= 56))"
    rule_expressions[148] = "(voltage_mv >= 56) != (voltage_mv >= 28)"
    rule_expressions[149] = "(voltage_mv >= 56) != (voltage_mv >= -56)"
    rule_expressions[150] = "(voltage_mv >= 56) != (not (voltage_mv >= 56))"
    rule_expressions[151] = "(voltage_mv >= 56) != (voltage_mv >= -56)"
    rule_expressions[152] = "(speed * 80 != altitude) != (speed * altitude != 80)"
    rule_expressions[153] = "(speed * 80 != altitude) != (speed * 80 != -altitude)"
    rule_expressions[154] = "(speed * 80 != altitude) != (speed * 75 != altitude)"
    rule_expressions[155] = "(speed * 80 != altitude) != (not (speed * 80 != altitude))"
    rule_expressions[156] = "(speed * 80 != altitude) != (altitude * 80 != altitude)"
    rule_expressions[157] = "(speed * 80 != altitude) != (speed * 80 != -altitude)"
    rule_expressions[158] = "(speed * 80 != altitude) != (speed * -80 != altitude)"
    rule_expressions[159] = "(speed * 80 != altitude) != (speed * 80 != -altitude)"
    rule_expressions[160] = "(speed * 80 != altitude) != (not (speed * 80 != altitude))"
    rule_expressions[161] = "(speed * 80 != altitude) != (speed * altitude != 80)"
    rule_expressions[162] = "(voltage_mv <= 5 or voltage_mv > 91) != (altitude <= 5 or voltage_mv > 91)"
    rule_expressions[163] = "(voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 and voltage_mv > 91)"
    rule_expressions[164] = "(voltage_mv <= 5 or voltage_mv > 91) != (altitude <= 5 or voltage_mv > 91)"
    rule_expressions[165] = "(voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 and voltage_mv > 91)"
    rule_expressions[166] = "(voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or -voltage_mv > 91)"
    rule_expressions[167] = "(voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or voltage_mv > 81)"
    rule_expressions[168] = "(voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or voltage_mv > 96)"
    rule_expressions[169] = "(voltage_mv <= 5 or voltage_mv > 91) != (voltage_mv <= 5 or -voltage_mv > 91)"
    rule_expressions[170] = "(speed > 20) != (speed > -20)"
    rule_expressions[171] = "(speed > 20) != (speed > 21)"
    rule_expressions[172] = "(speed > 20) != (altitude > 20)"
    rule_expressions[173] = "(speed > 20) != (not (speed > 20))"
    rule_expressions[174] = "(speed > 20) != (speed > -20)"
    rule_expressions[175] = "(speed > 20) != (speed > 30)"
    rule_expressions[176] = "(speed > 20) != (speed > 40)"
    rule_expressions[177] = "(5 <= voltage_mv <= 93) != (5 <= altitude <= 93)"
    rule_expressions[178] = "(5 <= voltage_mv <= 93) != (not (5) <= voltage_mv <= 93)"
    rule_expressions[179] = "(5 <= voltage_mv <= 93) != (-5 <= voltage_mv <= 93)"
    rule_expressions[180] = "(5 <= voltage_mv <= 93) != (5 <= -voltage_mv <= 93)"
    rule_expressions[181] = "(5 <= voltage_mv <= 93) != (not (5 <= voltage_mv <= 93))"
    rule_expressions[182] = "(5 <= voltage_mv <= 93) != (5 <= -voltage_mv <= 93)"
    rule_expressions[183] = "(altitude < 2) != (not (altitude < 2))"
    rule_expressions[184] = "(altitude < 2) != (not (altitude < 2))"
    rule_expressions[185] = "(altitude != 1000) != (speed != 1000)"
    rule_expressions[186] = "(altitude != 1000) != (altitude != 1002)"
    rule_expressions[187] = "(altitude != 1000) != (voltage_mv != 1000)"
    rule_expressions[188] = "(altitude != 1000) != (not (altitude != 1000))"
    rule_expressions[189] = "(altitude != 1000) != (altitude != 995)"
    rule_expressions[190] = "(altitude != 1000) != (not (altitude != 1000))"
    rule_expressions[191] = "(altitude != 1000) != (voltage_mv != 1000)"
    rule_expressions[192] = "(altitude != 1000) != (altitude != 1009)"
    rule_expressions[193] = "(altitude == 513) != (altitude == 518)"
    rule_expressions[194] = "(altitude == 513) != (altitude == 509)"
    rule_expressions[195] = "(altitude == 513) != (altitude == 515)"
    rule_expressions[196] = "(altitude == 513) != (altitude == -513)"
    rule_expressions[197] = "(altitude == 513) != (not (altitude == 513))"
    rule_expressions[198] = "(altitude == 513) != (voltage_mv == 513)"
    rule_expressions[199] = "(altitude == 513) != (altitude == 512)"
    rule_expressions[200] = "(voltage_mv != 10 and speed < 96) != (voltage_mv != 10 or speed < 96)"
    rule_expressions[201] = "(voltage_mv != 10 and speed < 96) != (not (voltage_mv != 10 and speed < 96))"
    rule_expressions[202] = "(voltage_mv != 10 and speed < 96) != (voltage_mv != 10 and -speed < 96)"
    rule_expressions[203] = "(voltage_mv != 10 and speed < 96) != (voltage_mv != 6 and speed < 96)"
    rule_expressions[204] = "(voltage_mv != 10 and speed < 96) != (voltage_mv != 10 and speed < 94)"
    rule_expressions[205] = "(voltage_mv != 10 and speed < 96) != (voltage_mv != -10 and speed < 96)"
    rule_expressions[206] = "(voltage_mv != 10 and speed < 96) != (voltage_mv != -10 and speed < 96)"
    rule_expressions[207] = "(speed >= 2) != (not (speed >= 2))"
    rule_expressions[208] = "(speed >= 2) != (not (speed >= 2))"
    rule_expressions[209] = "(speed >= 2) != (not (speed >= 2))"
    rule_expressions[210] = "(speed >= 2) != (speed >= 4)"
    rule_expressions[211] = "(speed >= 2) != (speed >= 4)"

    return rule_expressions