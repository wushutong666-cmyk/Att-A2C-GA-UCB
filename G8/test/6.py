def execute_Tr(a):
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
    if (altitude <= 500) != (500 >= altitude):
        t = 1
    # 变异规则 2 - RSR
    if (altitude <= 500) != (not (altitude <= 500)):
        triggered.add(1)
    # 变异规则 3 - SCR
    if (altitude <= 500) != (500 >= altitude):
        t = 1
    # 变异规则 4 - CRP
    if (altitude <= 500) != (altitude <= 499):
        triggered.add(2)
    # 变异规则 5 - SVR
    if (altitude <= 500) != (speed <= 500):
        triggered.add(3)
    # 变异规则 6 - AOR
    if (altitude <= 500) != (altitude <= 494):
        triggered.add(4)
    # 变异规则 7 - ROR
    if (altitude <= 500) != (abs(altitude) <= 500):
        t = 1
    # 变异规则 8 - ABS
    if (altitude <= 500) != (abs(altitude) <= 500):
        t = 1
    # 变异规则 9 - CAR
    if (altitude <= 500) != (altitude <= 499):
        triggered.add(5)
    # 变异规则 10 - LCR
    if (altitude <= 500) != (speed <= 500):
        triggered.add(6)
    # 原语句
    if altitude <= 500:
        health_score -= 5
    # 原语句2
    # 变异规则 11 - SAR
    if (201 <= altitude <= 626) != (altitude >= 201 <= 626):
        triggered.add(7)
    # 变异规则 12 - SVR
    if (201 <= altitude <= 626) != (201 <= speed <= 626):
        triggered.add(8)
    # 变异规则 13 - ABS
    if (201 <= altitude <= 626) != (201 <= abs(altitude) <= 626):
        t = 1
    # 变异规则 14 - SCR
    if (201 <= altitude <= 626) != (not (201 <= altitude <= 626)):
        triggered.add(9)
    # 变异规则 15 - RSR
    if (201 <= altitude <= 626) != (not (201 <= altitude <= 626)):
        triggered.add(10)
    # 变异规则 16 - ROR
    if (201 <= altitude <= 626) != (altitude >= 201 <= 626):
        triggered.add(11)
    # 变异规则 17 - LCR
    if (201 <= altitude <= 626) != (201 <= altitude <= 625):
        triggered.add(12)
    # 变异规则 18 - AOR
    if (201 <= altitude <= 626) != (-201 <= altitude <= 626):
        triggered.add(13)
    # 变异规则 19 - UOI
    if (201 <= altitude <= 626) != (201 <= -altitude <= 626):
        triggered.add(14)
    # 变异规则 20 - SRC
    if (201 <= altitude <= 626) != (201 <= altitude <= -626):
        triggered.add(15)
    # 原语句
    if 201 <= altitude <= 626:
        health_score += 8
        altitude = min(altitude + 4, 1000)
    # 原语句3
    # 变异规则 21 - SRC
    if (3 <= speed <= 76) != (3 <= voltage_mv <= 76):
        triggered.add(16)
    # 变异规则 22 - SVR
    if (3 <= speed <= 76) != (3 <= voltage_mv <= 76):
        triggered.add(17)
    # 变异规则 23 - AOR
    if (3 <= speed <= 76) != (1 <= speed <= 76):
        triggered.add(18)
    # 变异规则 24 - UOI
    if (3 <= speed <= 76) != (3 <= -speed <= 76):
        triggered.add(19)
    # 变异规则 25 - CAR
    if (3 <= speed <= 76) != (4 <= speed <= 76):
        triggered.add(20)
    # 变异规则 26 - ROR
    if (3 <= speed <= 76) != (3 <= voltage_mv <= 76):
        triggered.add(21)
    # 变异规则 27 - SAR
    if (3 <= speed <= 76) != (speed >= 3 <= 76):
        triggered.add(22)
    # 变异规则 28 - CSR
    if (3 <= speed <= 76) != (-3 <= speed <= 76):
        triggered.add(23)
    # 变异规则 29 - LCR
    if (3 <= speed <= 76) != (3 <= speed <= 66):
        triggered.add(24)
    # 变异规则 30 - CRP
    if (3 <= speed <= 76) != (6 <= speed <= 76):
        triggered.add(25)
    # 原语句
    if 3 <= speed <= 76:
        health_score -= 26
        speed = max(speed - 2, 2)
        voltage_mv = max(voltage_mv - 8, 2)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句4
    # 变异规则 31 - SRC
    if (speed > 20 and speed < 10) != (speed < 10 and speed > 20):
        t = 1
    # 变异规则 32 - ROR
    if (speed > 20 and speed < 10) != (speed > 20 or speed < 10):
        triggered.add(26)
    # 变异规则 33 - SVR
    if (speed > 20 and speed < 10) != (altitude > 20 and speed < 10):
        triggered.add(27)
    # 变异规则 34 - CSR
    if (speed > 20 and speed < 10) != (speed > -20 and speed < 10):
        triggered.add(28)
    # 变异规则 35 - SAR
    if (speed > 20 and speed < 10) != (speed > 20 and 10 > speed):
        t = 1
    # 变异规则 36 - LCR
    if (speed > 20 and speed < 10) != (speed > 20 or speed < 10):
        triggered.add(29)
    # 变异规则 37 - SCR
    if (speed > 20 and speed < 10) != (voltage_mv > 20 and speed < 10):
        triggered.add(30)
    # 变异规则 38 - UOI
    if (speed > 20 and speed < 10) != (speed > 20 and -speed < 10):
        triggered.add(31)
    # 变异规则 39 - ABS
    if (speed > 20 and speed < 10) != (abs(speed) > 20 and speed < 10):
        t = 1
    # 变异规则 40 - AOR
    if (speed > 20 and speed < 10) != (not (speed > 20 and speed < 10)):
        triggered.add(32)
    # 原语句
    if speed > 20 and speed < 10:
        health_score -= 12
    # 原语句5
    # 变异规则 41 - CSR
    if (voltage_mv > 55) != (voltage_mv > -55):
        triggered.add(33)
    # 变异规则 42 - SVR
    if (voltage_mv > 55) != (altitude > 55):
        triggered.add(34)
    # 变异规则 43 - CRP
    if (voltage_mv > 55) != (voltage_mv > 110):
        triggered.add(35)
    # 变异规则 44 - CAR
    if (voltage_mv > 55) != (voltage_mv > 53):
        triggered.add(36)
    # 变异规则 45 - ROR
    if (voltage_mv > 55) != (not (voltage_mv > 55)):
        triggered.add(37)
    # 变异规则 46 - SRC
    if (voltage_mv > 55) != (abs(voltage_mv) > 55):
        t = 1
    # 变异规则 47 - LCR
    if (voltage_mv > 55) != (voltage_mv > -55):
        triggered.add(38)
    # 变异规则 48 - AOR
    if (voltage_mv > 55) != (abs(voltage_mv) > 55):
        t = 1
    # 变异规则 49 - UOI
    if (voltage_mv > 55) != (voltage_mv > 50):
        triggered.add(39)
    # 变异规则 50 - ABS
    if (voltage_mv > 55) != (abs(voltage_mv) > 55):
        t = 1
    # 原语句
    if voltage_mv > 55:
        health_score += 10
    # 原语句6
    # 变异规则 51 - LCR
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 and altitude > 500):
        triggered.add(40)
    # 变异规则 52 - UOI
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 or -altitude > 500):
        triggered.add(41)
    # 变异规则 53 - SVR
    if (voltage_mv <= 78 or altitude > 500) != (speed <= 78 or altitude > 500):
        triggered.add(42)
    # 变异规则 54 - SCR
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 156 or altitude > 500):
        triggered.add(43)
    # 变异规则 55 - CSR
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= -78 or altitude > 500):
        triggered.add(44)
    # 变异规则 56 - SRC
    if (voltage_mv <= 78 or altitude > 500) != (altitude > 500 or voltage_mv <= 78):
        t = 1
    # 变异规则 57 - CAR
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 83 or altitude > 500):
        triggered.add(45)
    # 变异规则 58 - AOR
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 or altitude > -500):
        triggered.add(46)
    # 变异规则 59 - ROR
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 or -altitude > 500):
        triggered.add(47)
    # 变异规则 60 - ABS
    if (voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 or abs(altitude) > 500):
        t = 1
    # 原语句
    if voltage_mv <= 78 or altitude > 500:
        health_score -= 24
        altitude = min(altitude + 81, 1000)
        speed = max(speed - 8, 2)
        voltage_mv = min(voltage_mv + 6, 100)
        speed, voltage_mv = voltage_mv, speed
    # 原语句7
    # 变异规则 61 - SCR
    if (altitude > 297 or speed <= 30) != (altitude > 297 and speed <= 30):
        triggered.add(48)
    # 变异规则 62 - LCR
    if (altitude > 297 or speed <= 30) != (altitude > 297 and speed <= 30):
        triggered.add(49)
    # 变异规则 63 - UOI
    if (altitude > 297 or speed <= 30) != (altitude > 297 or -speed <= 30):
        triggered.add(50)
    # 变异规则 64 - AOR
    if (altitude > 297 or speed <= 30) != (297 < altitude or speed <= 30):
        t = 1
    # 变异规则 65 - ABS
    if (altitude > 297 or speed <= 30) != (abs(altitude) > 297 or speed <= 30):
        t = 1
    # 变异规则 66 - SRC
    if (altitude > 297 or speed <= 30) != (speed <= 30 or altitude > 297):
        t = 1
    # 变异规则 67 - RSR
    if (altitude > 297 or speed <= 30) != (not (altitude > 297 or speed <= 30)):
        triggered.add(51)
    # 变异规则 68 - ROR
    if (altitude > 297 or speed <= 30) != (297 < altitude or speed <= 30):
        t = 1
    # 变异规则 69 - SVR
    if (altitude > 297 or speed <= 30) != (speed > 297 or speed <= 30):
        triggered.add(52)
    # 变异规则 70 - CSR
    if (altitude > 297 or speed <= 30) != (altitude > -297 or speed <= 30):
        triggered.add(53)
    # 原语句
    if altitude > 297 or speed <= 30:
        health_score += 10
        altitude = min(altitude + 7, 1000)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句8
    # 变异规则 71 - RSR
    if (speed <= 92 or speed != 50) != (not (speed <= 92 or speed != 50)):
        triggered.add(54)
    # 变异规则 72 - SCR
    if (speed <= 92 or speed != 50) != (altitude <= 92 or speed != 50):
        triggered.add(55)
    # 变异规则 73 - SVR
    if (speed <= 92 or speed != 50) != (altitude <= 92 or speed != 50):
        triggered.add(56)
    # 变异规则 74 - AOR
    if (speed <= 92 or speed != 50) != (speed <= 92 and speed != 50):
        triggered.add(57)
    # 变异规则 75 - LCR
    if (speed <= 92 or speed != 50) != (speed <= 92 and speed != 50):
        triggered.add(58)
    # 变异规则 76 - ABS
    if (speed <= 92 or speed != 50) != (abs(speed) <= 92 or speed != 50):
        t = 1
    # 变异规则 77 - CSR
    if (speed <= 92 or speed != 50) != (speed <= -92 or speed != 50):
        triggered.add(59)
    # 变异规则 78 - CAR
    if (speed <= 92 or speed != 50) != (speed <= 92 or speed != 52):
        t = 1
    # 变异规则 79 - ROR
    if (speed <= 92 or speed != 50) != (92 >= speed or speed != 50):
        t = 1
    # 变异规则 80 - UOI
    if (speed <= 92 or speed != 50) != (speed <= 92 or -speed != 50):
        t = 1
    # 原语句
    if speed <= 92 or speed != 50:
        health_score -= 1
        altitude = max(altitude - 20, 2)
        speed = min(speed + 5, 100)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句9
    # 变异规则 81 - ABS
    if (speed > 100) != (abs(speed) > 100):
        t = 1
    # 变异规则 82 - SVR
    if (speed > 100) != (voltage_mv > 100):
        triggered.add(60)
    # 变异规则 83 - SCR
    if (speed > 100) != (not (speed > 100)):
        triggered.add(61)
    # 变异规则 84 - SRC
    if (speed > 100) != (not (speed > 100)):
        triggered.add(62)
    # 变异规则 85 - LCR
    if (speed > 100) != (not (speed > 100)):
        triggered.add(63)
    # 变异规则 86 - RSR
    if (speed > 100) != (not (speed > 100)):
        triggered.add(64)
    # 变异规则 87 - SAR
    if (speed > 100) != (100 < speed):
        t = 1
    # 变异规则 88 - UOI
    if (speed > 100) != (voltage_mv > 100):
        triggered.add(65)
    # 变异规则 89 - ROR
    if (speed > 100) != (speed > 102):
        t = 1
    # 变异规则 90 - CSR
    if (speed > 100) != (speed > -100):
        triggered.add(66)
    # 原语句
    if speed > 100:
        health_score -= 29
        altitude = min(altitude + 63, 1000)
        speed = min(speed + 8, 100)
    # 原语句10
    # 变异规则 91 - SVR
    if (voltage_mv >= 100 and speed >= 100) != (speed >= 100 and speed >= 100):
        triggered.add(67)
    # 变异规则 92 - ROR
    if (voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 98 and speed >= 100):
        triggered.add(68)
    # 变异规则 93 - SAR
    if (voltage_mv >= 100 and speed >= 100) != (100 <= voltage_mv and speed >= 100):
        t = 1
    # 变异规则 94 - CRP
    if (voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 100 and speed >= 200):
        triggered.add(69)
    # 变异规则 95 - SRC
    if (voltage_mv >= 100 and speed >= 100) != (speed >= 100 and voltage_mv >= 100):
        t = 1
    # 变异规则 96 - CAR
    if (voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 100 and speed >= 98):
        triggered.add(70)
    # 变异规则 97 - AOR
    if (voltage_mv >= 100 and speed >= 100) != (speed >= 100 and voltage_mv >= 100):
        t = 1
    # 变异规则 98 - ABS
    if (voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 100 and abs(speed) >= 100):
        t = 1
    # 变异规则 99 - LCR
    if (voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 100 or speed >= 100):
        triggered.add(71)
    # 变异规则 100 - RSR
    if (voltage_mv >= 100 and speed >= 100) != (not (voltage_mv >= 100 and speed >= 100)):
        triggered.add(72)
    # 原语句
    if voltage_mv >= 100 and speed >= 100:
        health_score -= 28
        speed = max(speed - 2, 2)
    # 原语句11
    # 变异规则 101 - SCR
    if (voltage_mv >= 20) != (voltage_mv >= -20):
        triggered.add(73)
    # 变异规则 102 - LCR
    if (voltage_mv >= 20) != (not (voltage_mv >= 20)):
        triggered.add(74)
    # 变异规则 103 - RSR
    if (voltage_mv >= 20) != (not (voltage_mv >= 20)):
        triggered.add(75)
    # 变异规则 104 - ABS
    if (voltage_mv >= 20) != (abs(voltage_mv) >= 20):
        t = 1
    # 变异规则 105 - SVR
    if (voltage_mv >= 20) != (altitude >= 20):
        triggered.add(76)
    # 变异规则 106 - CAR
    if (voltage_mv >= 20) != (voltage_mv >= 21):
        triggered.add(77)
    # 变异规则 107 - CSR
    if (voltage_mv >= 20) != (voltage_mv >= -20):
        triggered.add(78)
    # 变异规则 108 - SAR
    if (voltage_mv >= 20) != (20 <= voltage_mv):
        t = 1
    # 变异规则 109 - AOR
    if (voltage_mv >= 20) != (abs(voltage_mv) >= 20):
        t = 1
    # 变异规则 110 - UOI
    if (voltage_mv >= 20) != (abs(voltage_mv) >= 20):
        t = 1
    # 原语句
    if voltage_mv >= 20:
        health_score -= 20
    # 原语句12
    # 变异规则 111 - SRC
    if (speed != 100 or altitude <= 538) != (altitude <= 538 or speed != 100):
        t = 1
    # 变异规则 112 - ROR
    if (speed != 100 or altitude <= 538) != (speed != -100 or altitude <= 538):
        triggered.add(79)
    # 变异规则 113 - LCR
    if (speed != 100 or altitude <= 538) != (speed != 100 and altitude <= 538):
        triggered.add(80)
    # 变异规则 114 - CSR
    if (speed != 100 or altitude <= 538) != (speed != 100 or altitude <= -538):
        triggered.add(81)
    # 变异规则 115 - UOI
    if (speed != 100 or altitude <= 538) != (speed != 100 or -altitude <= 538):
        triggered.add(82)
    # 变异规则 116 - SAR
    if (speed != 100 or altitude <= 538) != (speed != 100 or 538 >= altitude):
        t = 1
    # 变异规则 117 - RSR
    if (speed != 100 or altitude <= 538) != (not (speed != 100 or altitude <= 538)):
        triggered.add(83)
    # 变异规则 118 - CAR
    if (speed != 100 or altitude <= 538) != (speed != 100 or altitude <= 537):
        t = 1
    # 变异规则 119 - CRP
    if (speed != 100 or altitude <= 538) != (speed != 200 or altitude <= 538):
        triggered.add(84)
    # 变异规则 120 - ABS
    if (speed != 100 or altitude <= 538) != (speed != 100 or abs(altitude) <= 538):
        t = 1
    # 原语句
    if speed != 100 or altitude <= 538:
        health_score += 14
        altitude = min(altitude + 50, 1000)
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句13
    # 变异规则 121 - SCR
    if (speed != 2) != (2 != speed):
        t = 1
    # 变异规则 122 - SAR
    if (speed != 2) != (2 != speed):
        t = 1
    # 变异规则 123 - CAR
    if (speed != 2) != (speed != 7):
        triggered.add(85)
    # 变异规则 124 - AOR
    if (speed != 2) != (not (speed != 2)):
        triggered.add(86)
    # 变异规则 125 - ABS
    if (speed != 2) != (abs(speed) != 2):
        t = 1
    # 变异规则 126 - SVR
    if (speed != 2) != (voltage_mv != 2):
        triggered.add(87)
    # 变异规则 127 - CSR
    if (speed != 2) != (speed != -2):
        t = 1
    # 变异规则 128 - SRC
    if (speed != 2) != (abs(speed) != 2):
        t = 1
    # 变异规则 129 - CRP
    if (speed != 2) != (speed != 4):
        t = 1
    # 变异规则 130 - ROR
    if (speed != 2) != (not (speed != 2)):
        triggered.add(88)
    # 原语句
    if speed != 2:
        health_score -= 7
    # 原语句14
    # 变异规则 131 - CRP
    if (speed <= 20 and voltage_mv > 50) != (speed <= 20 and voltage_mv > 25):
        t = 1
    # 变异规则 132 - SCR
    if (speed <= 20 and voltage_mv > 50) != (voltage_mv > 50 and speed <= 20):
        t = 1
    # 变异规则 133 - ABS
    if (speed <= 20 and voltage_mv > 50) != (abs(speed) <= 20 and voltage_mv > 50):
        t = 1
    # 变异规则 134 - CAR
    if (speed <= 20 and voltage_mv > 50) != (speed <= 20 and voltage_mv > 51):
        t = 1
    # 变异规则 135 - SVR
    if (speed <= 20 and voltage_mv > 50) != (voltage_mv <= 20 and voltage_mv > 50):
        triggered.add(89)
    # 变异规则 136 - UOI
    if (speed <= 20 and voltage_mv > 50) != (speed <= 20 and -voltage_mv > 50):
        triggered.add(90)
    # 变异规则 137 - AOR
    if (speed <= 20 and voltage_mv > 50) != (voltage_mv <= 20 and voltage_mv > 50):
        triggered.add(91)
    # 变异规则 138 - ROR
    if (speed <= 20 and voltage_mv > 50) != (speed <= 20 or voltage_mv > 50):
        triggered.add(92)
    # 变异规则 139 - RSR
    if (speed <= 20 and voltage_mv > 50) != (not (speed <= 20 and voltage_mv > 50)):
        triggered.add(93)
    # 变异规则 140 - CSR
    if (speed <= 20 and voltage_mv > 50) != (speed <= 20 and voltage_mv > -50):
        t = 1
    # 原语句
    if speed <= 20 and voltage_mv > 50:
        health_score -= 5
        voltage_mv = max(voltage_mv - 2, 2)
    # 原语句15
    # 变异规则 141 - SRC
    if (33 <= speed <= 73) != (31 <= speed <= 73):
        triggered.add(94)
    # 变异规则 142 - CRP
    if (33 <= speed <= 73) != (33 <= speed <= 78):
        triggered.add(95)
    # 变异规则 143 - SCR
    if (33 <= speed <= 73) != (33 <= speed <= 72):
        triggered.add(96)
    # 变异规则 144 - AOR
    if (33 <= speed <= 73) != (33 <= speed <= 75):
        triggered.add(97)
    # 变异规则 145 - SAR
    if (33 <= speed <= 73) != (speed >= 33 <= 73):
        triggered.add(98)
    # 变异规则 146 - CAR
    if (33 <= speed <= 73) != (34 <= speed <= 73):
        triggered.add(99)
    # 变异规则 147 - ABS
    if (33 <= speed <= 73) != (33 <= abs(speed) <= 73):
        t = 1
    # 变异规则 148 - CSR
    if (33 <= speed <= 73) != (33 <= speed <= -73):
        triggered.add(100)
    # 变异规则 149 - SVR
    if (33 <= speed <= 73) != (33 <= voltage_mv <= 73):
        triggered.add(101)
    # 变异规则 150 - RSR
    if (33 <= speed <= 73) != (not (33 <= speed <= 73)):
        triggered.add(102)
    # 原语句
    if 33 <= speed <= 73:
        health_score -= 14
        altitude = max(altitude - 25, 2)
        speed = max(speed - 10, 2)
    # 原语句16
    # 变异规则 151 - LCR
    if (altitude != speed + 20) != (altitude != speed + 26):
        triggered.add(103)
    # 变异规则 152 - ABS
    if (altitude != speed + 20) != (abs(altitude) != speed + 20):
        t = 1
    # 变异规则 153 - UOI
    if (altitude != speed + 20) != (altitude != -speed + 20):
        triggered.add(104)
    # 变异规则 154 - CSR
    if (altitude != speed + 20) != (altitude != speed + -20):
        triggered.add(105)
    # 变异规则 155 - CRP
    if (altitude != speed + 20) != (altitude != speed + 10):
        triggered.add(106)
    # 变异规则 156 - AOR
    if (altitude != speed + 20) != (altitude != speed + -20):
        triggered.add(107)
    # 变异规则 157 - SCR
    if (altitude != speed + 20) != (abs(altitude) != speed + 20):
        t = 1
    # 变异规则 158 - ROR
    if (altitude != speed + 20) != (altitude != speed + 10):
        triggered.add(108)
    # 变异规则 159 - SVR
    if (altitude != speed + 20) != (voltage_mv != speed + 20):
        triggered.add(109)
    # 变异规则 160 - CAR
    if (altitude != speed + 20) != (altitude != speed + 18):
        triggered.add(110)
    # 原语句
    if altitude != speed + 20:
        health_score -= 28
        altitude = max(altitude - 11, 2)
        speed, voltage_mv = voltage_mv, speed
    # 原语句17
    # 变异规则 161 - UOI
    if (voltage_mv == 5) != (not (voltage_mv == 5)):
        triggered.add(111)
    # 变异规则 162 - CAR
    if (voltage_mv == 5) != (voltage_mv == 15):
        triggered.add(112)
    # 变异规则 163 - SAR
    if (voltage_mv == 5) != (5 == voltage_mv):
        t = 1
    # 变异规则 164 - SCR
    if (voltage_mv == 5) != (5 == voltage_mv):
        t = 1
    # 变异规则 165 - CSR
    if (voltage_mv == 5) != (voltage_mv == -5):
        t = 1
    # 变异规则 166 - AOR
    if (voltage_mv == 5) != (not (voltage_mv == 5)):
        triggered.add(113)
    # 变异规则 167 - SVR
    if (voltage_mv == 5) != (altitude == 5):
        triggered.add(114)
    # 变异规则 168 - CRP
    if (voltage_mv == 5) != (voltage_mv == 2):
        t = 1
    # 变异规则 169 - ROR
    if (voltage_mv == 5) != (speed == 5):
        t = 1
    # 变异规则 170 - LCR
    if (voltage_mv == 5) != (voltage_mv == 15):
        triggered.add(115)
    # 原语句
    if voltage_mv == 5:
        health_score -= 27
        speed = max(speed - 2, 2)
    # 原语句18
    # 变异规则 171 - SRC
    if (altitude == 500 and speed != 5) != (speed != 5 and altitude == 500):
        t = 1
    # 变异规则 172 - ROR
    if (altitude == 500 and speed != 5) != (altitude == -500 and speed != 5):
        triggered.add(116)
    # 变异规则 173 - RSR
    if (altitude == 500 and speed != 5) != (not (altitude == 500 and speed != 5)):
        triggered.add(117)
    # 变异规则 174 - SVR
    if (altitude == 500 and speed != 5) != (speed == 500 and speed != 5):
        triggered.add(118)
    # 变异规则 175 - CSR
    if (altitude == 500 and speed != 5) != (altitude == -500 and speed != 5):
        triggered.add(119)
    # 变异规则 176 - LCR
    if (altitude == 500 and speed != 5) != (altitude == 500 or speed != 5):
        triggered.add(120)
    # 变异规则 177 - SAR
    if (altitude == 500 and speed != 5) != (500 == altitude and speed != 5):
        t = 1
    # 变异规则 178 - SCR
    if (altitude == 500 and speed != 5) != (altitude == 499 and speed != 5):
        triggered.add(121)
    # 变异规则 179 - ABS
    if (altitude == 500 and speed != 5) != (abs(altitude) == 500 and speed != 5):
        t = 1
    # 变异规则 180 - AOR
    if (altitude == 500 and speed != 5) != (500 == altitude and speed != 5):
        t = 1
    # 原语句
    if altitude == 500 and speed != 5:
        health_score += 7
        altitude = max(altitude - 48, 2)
        speed = min(speed + 2, 100)
        voltage_mv = max(voltage_mv - 4, 2)
    # 原语句19
    # 变异规则 181 - ABS
    if (voltage_mv <= 20) != (abs(voltage_mv) <= 20):
        t = 1
    # 变异规则 182 - ROR
    if (voltage_mv <= 20) != (voltage_mv <= -20):
        triggered.add(122)
    # 变异规则 183 - CAR
    if (voltage_mv <= 20) != (voltage_mv <= 21):
        triggered.add(123)
    # 变异规则 184 - RSR
    if (voltage_mv <= 20) != (not (voltage_mv <= 20)):
        triggered.add(124)
    # 变异规则 185 - SRC
    if (voltage_mv <= 20) != (voltage_mv <= 25):
        triggered.add(125)
    # 变异规则 186 - SAR
    if (voltage_mv <= 20) != (20 >= voltage_mv):
        t = 1
    # 变异规则 187 - UOI
    if (voltage_mv <= 20) != (voltage_mv <= 40):
        triggered.add(126)
    # 变异规则 188 - CSR
    if (voltage_mv <= 20) != (voltage_mv <= -20):
        triggered.add(127)
    # 变异规则 189 - SCR
    if (voltage_mv <= 20) != (voltage_mv <= 10):
        triggered.add(128)
    # 变异规则 190 - AOR
    if (voltage_mv <= 20) != (abs(voltage_mv) <= 20):
        t = 1
    # 原语句
    if voltage_mv <= 20:
        health_score -= 30
        voltage_mv = min(voltage_mv + 7, 100)
        altitude, voltage_mv = voltage_mv, altitude
    # 原语句20
    # 变异规则 191 - CAR
    if (voltage_mv <= speed - 50) != (voltage_mv <= speed - 51):
        triggered.add(129)
    # 变异规则 192 - SRC
    if (voltage_mv <= speed - 50) != (not (voltage_mv <= speed - 50)):
        triggered.add(130)
    # 变异规则 193 - SAR
    if (voltage_mv <= speed - 50) != (speed >= voltage_mv - 50):
        triggered.add(131)
    # 变异规则 194 - SCR
    if (voltage_mv <= speed - 50) != (voltage_mv <= speed - 100):
        triggered.add(132)
    # 变异规则 195 - CSR
    if (voltage_mv <= speed - 50) != (voltage_mv <= speed - -50):
        triggered.add(133)
    # 变异规则 196 - RSR
    if (voltage_mv <= speed - 50) != (not (voltage_mv <= speed - 50)):
        triggered.add(134)
    # 变异规则 197 - UOI
    if (voltage_mv <= speed - 50) != (voltage_mv <= -speed - 50):
        triggered.add(135)
    # 变异规则 198 - AOR
    if (voltage_mv <= speed - 50) != (voltage_mv <= abs(speed) - 50):
        t = 1
    # 变异规则 199 - ABS
    if (voltage_mv <= speed - 50) != (voltage_mv <= abs(speed) - 50):
        t = 1
    # 变异规则 200 - LCR
    if (voltage_mv <= speed - 50) != (voltage_mv <= speed - 48):
        triggered.add(136)
    # 原语句
    if voltage_mv <= speed - 50:
        health_score += 14
    # 原语句21
    # 变异规则 201 - SRC
    if (altitude != speed * 2) != (speed != altitude * 2):
        triggered.add(137)
    # 变异规则 202 - LCR
    if (altitude != speed * 2) != (speed != speed * 2):
        triggered.add(138)
    # 变异规则 203 - AOR
    if (altitude != speed * 2) != (altitude != speed * -2):
        triggered.add(139)
    # 变异规则 204 - CAR
    if (altitude != speed * 2) != (altitude != speed * 4):
        triggered.add(140)
    # 变异规则 205 - CRP
    if (altitude != speed * 2) != (altitude != speed * 4):
        triggered.add(141)
    # 变异规则 206 - ABS
    if (altitude != speed * 2) != (abs(altitude) != speed * 2):
        t = 1
    # 变异规则 207 - SCR
    if (altitude != speed * 2) != (not (altitude != speed * 2)):
        triggered.add(142)
    # 变异规则 208 - CSR
    if (altitude != speed * 2) != (altitude != speed * -2):
        triggered.add(143)
    # 变异规则 209 - SAR
    if (altitude != speed * 2) != (speed != altitude * 2):
        triggered.add(144)
    # 变异规则 210 - RSR
    if (altitude != speed * 2) != (not (altitude != speed * 2)):
        triggered.add(145)
    # 原语句
    if altitude != speed * 2:
        health_score -= 25
    # 原语句22
    # 变异规则 211 - CRP
    if (voltage_mv + speed == 50) != (voltage_mv + speed == 42):
        t = 1
    # 变异规则 212 - RSR
    if (voltage_mv + speed == 50) != (not (voltage_mv + speed == 50)):
        triggered.add(146)
    # 变异规则 213 - CSR
    if (voltage_mv + speed == 50) != (voltage_mv + speed == -50):
        t = 1
    # 变异规则 214 - ROR
    if (voltage_mv + speed == 50) != (voltage_mv + 50 == speed):
        triggered.add(147)
    # 变异规则 215 - SRC
    if (voltage_mv + speed == 50) != (not (voltage_mv + speed == 50)):
        triggered.add(148)
    # 变异规则 216 - UOI
    if (voltage_mv + speed == 50) != (voltage_mv + -speed == 50):
        triggered.add(149)
    # 变异规则 217 - LCR
    if (voltage_mv + speed == 50) != (altitude + speed == 50):
        triggered.add(150)
    # 变异规则 218 - CAR
    if (voltage_mv + speed == 50) != (voltage_mv + speed == 45):
        t = 1
    # 变异规则 219 - SCR
    if (voltage_mv + speed == 50) != (voltage_mv + abs(speed) == 50):
        t = 1
    # 变异规则 220 - SVR
    if (voltage_mv + speed == 50) != (altitude + speed == 50):
        triggered.add(151)
    # 原语句
    if voltage_mv + speed == 50:
        health_score -= 17
        speed = max(speed - 7, 2)
        voltage_mv, altitude = altitude, voltage_mv
    # 原语句23
    # 变异规则 221 - CAR
    if (altitude == 5 or voltage_mv != 20) != (altitude == 4 or voltage_mv != 20):
        t = 1
    # 变异规则 222 - SCR
    if (altitude == 5 or voltage_mv != 20) != (abs(altitude) == 5 or voltage_mv != 20):
        t = 1
    # 变异规则 223 - SAR
    if (altitude == 5 or voltage_mv != 20) != (5 == altitude or voltage_mv != 20):
        t = 1
    # 变异规则 224 - RSR
    if (altitude == 5 or voltage_mv != 20) != (not (altitude == 5 or voltage_mv != 20)):
        triggered.add(152)
    # 变异规则 225 - ROR
    if (altitude == 5 or voltage_mv != 20) != (voltage_mv == 5 or voltage_mv != 20):
        t = 1
    # 变异规则 226 - ABS
    if (altitude == 5 or voltage_mv != 20) != (abs(altitude) == 5 or voltage_mv != 20):
        t = 1
    # 变异规则 227 - LCR
    if (altitude == 5 or voltage_mv != 20) != (altitude == 5 and voltage_mv != 20):
        triggered.add(153)
    # 变异规则 228 - UOI
    if (altitude == 5 or voltage_mv != 20) != (altitude == 5 or -voltage_mv != 20):
        triggered.add(154)
    # 变异规则 229 - SVR
    if (altitude == 5 or voltage_mv != 20) != (voltage_mv == 5 or voltage_mv != 20):
        t = 1
    # 变异规则 230 - CSR
    if (altitude == 5 or voltage_mv != 20) != (altitude == 5 or voltage_mv != -20):
        triggered.add(155)
    # 原语句
    if altitude == 5 or voltage_mv != 20:
        health_score += 2
    # 原语句24
    # 变异规则 231 - SCR
    if (voltage_mv > 20) != (altitude > 20):
        triggered.add(156)
    # 变异规则 232 - AOR
    if (voltage_mv > 20) != (not (voltage_mv > 20)):
        triggered.add(157)
    # 变异规则 233 - SRC
    if (voltage_mv > 20) != (voltage_mv > -20):
        triggered.add(158)
    # 变异规则 234 - CSR
    if (voltage_mv > 20) != (voltage_mv > -20):
        triggered.add(159)
    # 变异规则 235 - ROR
    if (voltage_mv > 20) != (voltage_mv > 23):
        triggered.add(160)
    # 变异规则 236 - CRP
    if (voltage_mv > 20) != (voltage_mv > 18):
        triggered.add(161)
    # 变异规则 237 - UOI
    if (voltage_mv > 20) != (abs(voltage_mv) > 20):
        t = 1
    # 变异规则 238 - SVR
    if (voltage_mv > 20) != (altitude > 20):
        triggered.add(162)
    # 变异规则 239 - RSR
    if (voltage_mv > 20) != (not (voltage_mv > 20)):
        triggered.add(163)
    # 变异规则 240 - ABS
    if (voltage_mv > 20) != (abs(voltage_mv) > 20):
        t = 1
    # 原语句
    if voltage_mv > 20:
        health_score += 18
        voltage_mv = min(voltage_mv + 1, 100)
    # 原语句25
    # 变异规则 241 - SVR
    if (258 <= altitude <= 691) != (258 <= speed <= 691):
        triggered.add(164)
    # 变异规则 242 - ROR
    if (258 <= altitude <= 691) != (not (258 <= altitude <= 691)):
        triggered.add(165)
    # 变异规则 243 - CAR
    if (258 <= altitude <= 691) != (257 <= altitude <= 691):
        triggered.add(166)
    # 变异规则 244 - AOR
    if (258 <= altitude <= 691) != (258 <= altitude <= -691):
        triggered.add(167)
    # 变异规则 245 - CSR
    if (258 <= altitude <= 691) != (-258 <= altitude <= 691):
        triggered.add(168)
    # 变异规则 246 - CRP
    if (258 <= altitude <= 691) != (251 <= altitude <= 691):
        triggered.add(169)
    # 变异规则 247 - ABS
    if (258 <= altitude <= 691) != (258 <= abs(altitude) <= 691):
        t = 1
    # 变异规则 248 - LCR
    if (258 <= altitude <= 691) != (258 <= -altitude <= 691):
        triggered.add(170)
    # 变异规则 249 - RSR
    if (258 <= altitude <= 691) != (not (258 <= altitude <= 691)):
        triggered.add(171)
    # 变异规则 250 - SAR
    if (258 <= altitude <= 691) != (altitude >= 258 <= 691):
        triggered.add(172)
    # 原语句
    if 258 <= altitude <= 691:
        health_score -= 13
        voltage_mv = max(voltage_mv - 9, 2)
        speed, altitude = altitude, speed
    # 原语句26
    # 变异规则 251 - AOR
    if (speed != 10) != (10 != speed):
        t = 1
    # 变异规则 252 - SCR
    if (speed != 10) != (speed != 20):
        triggered.add(173)
    # 变异规则 253 - SAR
    if (speed != 10) != (10 != speed):
        t = 1
    # 变异规则 254 - LCR
    if (speed != 10) != (not (speed != 10)):
        triggered.add(174)
    # 变异规则 255 - ABS
    if (speed != 10) != (abs(speed) != 10):
        t = 1
    # 变异规则 256 - SRC
    if (speed != 10) != (not (speed != 10)):
        triggered.add(175)
    # 变异规则 257 - ROR
    if (speed != 10) != (abs(speed) != 10):
        t = 1
    # 变异规则 258 - SVR
    if (speed != 10) != (voltage_mv != 10):
        triggered.add(176)
    # 变异规则 259 - UOI
    if (speed != 10) != (voltage_mv != 10):
        triggered.add(177)
    # 变异规则 260 - CSR
    if (speed != 10) != (speed != -10):
        t = 1
    # 原语句
    if speed != 10:
        health_score -= 30
        speed = min(speed + 7, 100)
    # 原语句27
    # 变异规则 261 - LCR
    if (altitude < 20) != (not (altitude < 20)):
        triggered.add(178)
    # 变异规则 262 - UOI
    if (altitude < 20) != (altitude < 25):
        triggered.add(179)
    # 变异规则 263 - SCR
    if (altitude < 20) != (voltage_mv < 20):
        triggered.add(180)
    # 变异规则 264 - ROR
    if (altitude < 20) != (abs(altitude) < 20):
        t = 1
    # 变异规则 265 - CSR
    if (altitude < 20) != (altitude < -20):
        triggered.add(181)
    # 变异规则 266 - SRC
    if (altitude < 20) != (not (altitude < 20)):
        triggered.add(182)
    # 变异规则 267 - AOR
    if (altitude < 20) != (altitude < 10):
        triggered.add(183)
    # 变异规则 268 - CRP
    if (altitude < 20) != (altitude < 25):
        triggered.add(184)
    # 变异规则 269 - SVR
    if (altitude < 20) != (speed < 20):
        triggered.add(185)
    # 变异规则 270 - RSR
    if (altitude < 20) != (not (altitude < 20)):
        triggered.add(186)
    # 原语句
    if altitude < 20:
        health_score -= 8
        voltage_mv = min(voltage_mv + 5, 100)
    # 原语句28
    # 变异规则 271 - CAR
    if (speed < 2) != (speed < 1):
        t = 1
    # 变异规则 272 - SCR
    if (speed < 2) != (speed < -2):
        t = 1
    # 变异规则 273 - RSR
    if (speed < 2) != (not (speed < 2)):
        triggered.add(187)
    # 变异规则 274 - CRP
    if (speed < 2) != (speed < 4):
        t = 1
    # 变异规则 275 - UOI
    if (speed < 2) != (speed < -2):
        t = 1
    # 变异规则 276 - ABS
    if (speed < 2) != (abs(speed) < 2):
        t = 1
    # 变异规则 277 - SVR
    if (speed < 2) != (voltage_mv < 2):
        t = 1
    # 变异规则 278 - CSR
    if (speed < 2) != (speed < -2):
        t = 1
    # 变异规则 279 - SRC
    if (speed < 2) != (altitude < 2):
        t = 1
    # 变异规则 280 - LCR
    if (speed < 2) != (not (speed < 2)):
        triggered.add(188)
    # 原语句
    if speed < 2:
        health_score += 16
        voltage_mv = max(voltage_mv - 6, 2)
    # 原语句29
    # 变异规则 281 - SAR
    if (altitude >= 472 and speed >= 100) != (472 <= altitude and speed >= 100):
        t = 1
    # 变异规则 282 - RSR
    if (altitude >= 472 and speed >= 100) != (not (altitude >= 472 and speed >= 100)):
        triggered.add(189)
    # 变异规则 283 - ABS
    if (altitude >= 472 and speed >= 100) != (abs(altitude) >= 472 and speed >= 100):
        t = 1
    # 变异规则 284 - CSR
    if (altitude >= 472 and speed >= 100) != (altitude >= 472 and speed >= -100):
        triggered.add(190)
    # 变异规则 285 - SCR
    if (altitude >= 472 and speed >= 100) != (not (altitude >= 472 and speed >= 100)):
        triggered.add(191)
    # 变异规则 286 - UOI
    if (altitude >= 472 and speed >= 100) != (altitude >= 472 and -speed >= 100):
        triggered.add(192)
    # 变异规则 287 - SRC
    if (altitude >= 472 and speed >= 100) != (speed >= 100 and altitude >= 472):
        t = 1
    # 变异规则 288 - CRP
    if (altitude >= 472 and speed >= 100) != (altitude >= 944 and speed >= 100):
        triggered.add(193)
    # 变异规则 289 - LCR
    if (altitude >= 472 and speed >= 100) != (altitude >= 472 or speed >= 100):
        triggered.add(194)
    # 变异规则 290 - CAR
    if (altitude >= 472 and speed >= 100) != (altitude >= 477 and speed >= 100):
        t = 1
    # 原语句
    if altitude >= 472 and speed >= 100:
        health_score -= 28
        speed = max(speed - 9, 2)
    # 原语句30
    # 变异规则 291 - AOR
    if (voltage_mv <= 2) != (speed <= 2):
        triggered.add(195)
    # 变异规则 292 - LCR
    if (voltage_mv <= 2) != (voltage_mv <= 12):
        triggered.add(196)
    # 变异规则 293 - CSR
    if (voltage_mv <= 2) != (voltage_mv <= -2):
        triggered.add(197)
    # 变异规则 294 - SVR
    if (voltage_mv <= 2) != (speed <= 2):
        triggered.add(198)
    # 变异规则 295 - UOI
    if (voltage_mv <= 2) != (altitude <= 2):
        triggered.add(199)
    # 变异规则 296 - SCR
    if (voltage_mv <= 2) != (voltage_mv <= -2):
        triggered.add(200)
    # 变异规则 297 - ABS
    if (voltage_mv <= 2) != (abs(voltage_mv) <= 2):
        t = 1
    # 变异规则 298 - SRC
    if (voltage_mv <= 2) != (abs(voltage_mv) <= 2):
        t = 1
    # 变异规则 299 - CAR
    if (voltage_mv <= 2) != (voltage_mv <= 3):
        triggered.add(201)
    # 变异规则 300 - ROR
    if (voltage_mv <= 2) != (not (voltage_mv <= 2)):
        triggered.add(202)
    # 原语句
    if voltage_mv <= 2:
        voltage_mv = min(voltage_mv + 1, 100)
    return triggered

targetPaths = [
    {1, 9, 13, 18, 23, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 156, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 112, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 156, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 104, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 156, 157, 158, 165, 168, 174, 178, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 102, 111, 117, 120, 123, 124, 125, 126, 130, 135, 142, 146, 152, 153, 156, 157, 160, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 102, 105, 111, 117, 120, 124, 125, 126, 130, 135, 142, 146, 152, 153, 156, 157, 160, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 94, 102, 111, 117, 120, 124, 126, 130, 135, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 94, 102, 111, 117, 120, 124, 126, 130, 135, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 99, 100, 101, 102, 111, 117, 120, 124, 125, 126, 130, 135, 142, 146, 152, 153, 156, 157, 160, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 111, 117, 120, 124, 126, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 106, 111, 117, 120, 124, 126, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 109, 111, 117, 120, 124, 126, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 40, 44, 50, 51, 53, 54, 57, 59, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 39, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 36, 37, 39, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 34, 35, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 34, 35, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 96, 100, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 34, 35, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 76, 83, 86, 92, 93, 95, 97, 98, 101, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 18, 23, 26, 28, 30, 32, 34, 35, 37, 42, 43, 45, 46, 48, 51, 54, 61, 66, 72, 74, 76, 83, 85, 86, 89, 90, 93, 101, 102, 111, 117, 120, 122, 124, 130, 131, 133, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 183, 185, 187, 189, 202},
    {1, 9, 13, 16, 19, 20, 25, 26, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 9, 13, 19, 20, 25, 26, 27, 28, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 196, 201, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 114, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 196, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 77, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 196, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 176, 178, 179, 180, 187, 189, 194, 196, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 161, 165, 168, 174, 178, 179, 180, 187, 189, 194, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 110, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 154, 155, 157, 158, 161, 165, 168, 174, 178, 179, 187, 189, 194, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 103, 104, 105, 106, 109, 110, 111, 117, 120, 124, 130, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 19, 24, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 179, 187, 189, 194, 202},
    {1, 9, 13, 22, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 179, 187, 189, 194, 202},
    {1, 9, 13, 16, 22, 26, 31, 32, 33, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 83, 86, 92, 93, 100, 101, 102, 111, 117, 120, 124, 126, 130, 132, 135, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 194, 202},
    {1, 9, 13, 22, 26, 31, 32, 34, 35, 37, 42, 43, 45, 46, 50, 51, 53, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 98, 102, 111, 117, 120, 124, 130, 131, 133, 136, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 22, 26, 31, 32, 34, 35, 37, 42, 43, 45, 46, 50, 51, 53, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 98, 102, 111, 117, 120, 124, 129, 130, 132, 135, 142, 146, 147, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 22, 26, 31, 32, 34, 35, 37, 43, 45, 46, 50, 51, 53, 54, 57, 61, 66, 67, 71, 72, 73, 74, 76, 80, 81, 83, 86, 92, 93, 98, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 16, 19, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 103, 104, 105, 106, 109, 110, 111, 117, 120, 124, 130, 142, 146, 150, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 19, 24, 26, 31, 32, 33, 37, 40, 44, 48, 51, 54, 61, 66, 72, 74, 83, 86, 89, 90, 93, 102, 103, 104, 105, 106, 109, 110, 111, 117, 120, 124, 130, 137, 138, 139, 140, 142, 146, 152, 153, 157, 165, 168, 173, 174, 178, 187, 189, 202},
    {1, 9, 13, 16, 18, 23, 26, 28, 30, 32, 33, 37, 40, 44, 50, 51, 53, 54, 55, 57, 59, 61, 66, 72, 74, 76, 83, 86, 92, 93, 100, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 19, 20, 25, 26, 27, 28, 30, 32, 33, 37, 40, 44, 50, 51, 53, 54, 60, 61, 66, 71, 72, 74, 76, 83, 86, 92, 93, 100, 102, 111, 117, 120, 124, 126, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 19, 26, 31, 32, 33, 37, 40, 44, 50, 51, 53, 54, 61, 66, 72, 74, 83, 86, 92, 93, 100, 101, 102, 103, 104, 105, 106, 109, 110, 111, 117, 120, 124, 130, 131, 133, 142, 146, 149, 152, 153, 157, 165, 168, 174, 178, 187, 189, 202},
    {1, 9, 13, 22, 26, 31, 32, 35, 37, 43, 45, 46, 50, 51, 53, 54, 57, 61, 66, 67, 68, 71, 72, 74, 80, 81, 83, 86, 92, 93, 98, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 194, 202},
    {1, 9, 13, 16, 18, 23, 26, 27, 28, 32, 33, 34, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 102, 111, 117, 120, 123, 124, 125, 126, 130, 135, 142, 146, 152, 153, 156, 157, 160, 164, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 9, 13, 22, 26, 31, 32, 35, 37, 43, 45, 46, 50, 51, 53, 54, 57, 61, 66, 70, 71, 72, 74, 83, 86, 92, 93, 98, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 194, 202},
    {1, 9, 13, 22, 26, 31, 32, 35, 37, 43, 45, 46, 50, 51, 53, 54, 57, 61, 66, 69, 72, 74, 83, 86, 92, 93, 98, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 174, 178, 187, 189, 194, 202},
    {1, 8, 9, 14, 15, 18, 23, 26, 27, 28, 32, 33, 34, 37, 40, 44, 48, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 164, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 8, 9, 14, 15, 16, 18, 23, 26, 27, 28, 30, 32, 35, 37, 40, 44, 50, 51, 53, 54, 60, 61, 66, 71, 72, 74, 76, 83, 86, 92, 93, 95, 97, 98, 101, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 168, 169, 174, 178, 187, 189, 202},
    {1, 8, 9, 14, 15, 16, 18, 23, 26, 27, 28, 30, 32, 35, 37, 40, 44, 50, 51, 53, 54, 60, 61, 66, 71, 72, 74, 76, 83, 86, 92, 93, 95, 97, 98, 101, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 165, 166, 168, 169, 174, 178, 187, 189, 202},
    {1, 8, 9, 14, 15, 16, 18, 23, 26, 27, 28, 30, 32, 35, 37, 40, 44, 50, 51, 53, 54, 60, 61, 66, 71, 72, 74, 76, 83, 86, 92, 93, 95, 97, 98, 101, 102, 111, 117, 120, 124, 130, 131, 133, 142, 146, 152, 153, 157, 164, 165, 167, 170, 174, 178, 187, 189, 194, 202},
    {1, 8, 9, 14, 15, 16, 18, 23, 26, 27, 28, 30, 32, 33, 34, 37, 40, 44, 48, 51, 52, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 100, 101, 102, 111, 117, 120, 124, 126, 130, 135, 142, 146, 152, 153, 156, 157, 164, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 8, 9, 14, 15, 16, 18, 23, 26, 27, 28, 32, 33, 34, 37, 40, 44, 51, 54, 61, 66, 72, 73, 74, 76, 83, 86, 92, 93, 102, 111, 117, 118, 120, 123, 124, 125, 126, 130, 135, 142, 146, 152, 153, 156, 157, 160, 164, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 4, 8, 9, 14, 15, 18, 23, 26, 27, 28, 32, 33, 34, 37, 40, 44, 51, 54, 61, 66, 72, 73, 74, 76, 80, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 164, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 4, 8, 9, 14, 15, 18, 23, 26, 27, 28, 30, 32, 35, 37, 40, 41, 48, 51, 52, 54, 61, 66, 72, 73, 74, 76, 80, 83, 86, 92, 93, 98, 102, 111, 117, 120, 124, 130, 135, 142, 146, 152, 153, 156, 157, 164, 165, 168, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 4, 8, 9, 14, 15, 18, 23, 26, 27, 28, 30, 32, 35, 37, 40, 41, 48, 51, 52, 54, 57, 61, 66, 67, 71, 72, 73, 74, 76, 79, 82, 83, 84, 86, 87, 93, 98, 102, 111, 117, 120, 124, 130, 142, 146, 152, 153, 157, 164, 165, 167, 170, 174, 178, 180, 181, 185, 187, 189, 194, 199, 202},
    {1, 2, 4, 8, 9, 14, 15, 18, 23, 26, 27, 28, 32, 33, 34, 37, 51, 54, 61, 66, 72, 73, 74, 76, 80, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 164, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 3, 8, 9, 14, 15, 18, 23, 26, 27, 28, 32, 33, 34, 37, 51, 54, 61, 66, 72, 73, 74, 76, 80, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 164, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 3, 8, 9, 14, 15, 16, 19, 20, 25, 26, 28, 30, 32, 34, 37, 42, 46, 48, 51, 54, 60, 61, 66, 71, 72, 74, 76, 83, 85, 86, 89, 90, 93, 101, 102, 111, 117, 120, 121, 122, 124, 130, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 183, 185, 187, 189, 202},
    {1, 3, 8, 9, 14, 15, 16, 19, 20, 25, 26, 28, 30, 32, 34, 37, 42, 46, 48, 51, 54, 60, 61, 66, 71, 72, 74, 76, 83, 85, 86, 89, 90, 93, 101, 102, 111, 116, 117, 118, 121, 122, 124, 130, 142, 146, 152, 153, 156, 157, 165, 168, 174, 178, 180, 181, 183, 185, 187, 189, 202},
    {1, 3, 8, 9, 14, 15, 18, 23, 26, 27, 28, 30, 32, 35, 37, 40, 41, 48, 51, 52, 54, 57, 61, 66, 67, 71, 72, 73, 74, 76, 79, 82, 83, 84, 86, 87, 93, 98, 102, 111, 117, 120, 124, 130, 142, 146, 152, 153, 157, 165, 172, 174, 178, 185, 187, 189, 190, 194, 202},
    {1, 3, 8, 9, 12, 14, 15, 18, 23, 26, 27, 28, 32, 33, 34, 37, 51, 54, 61, 66, 72, 73, 74, 76, 80, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 3, 7, 9, 18, 23, 26, 27, 28, 32, 33, 34, 37, 51, 54, 61, 66, 72, 73, 74, 76, 80, 83, 86, 89, 90, 93, 102, 111, 117, 120, 122, 124, 128, 130, 135, 142, 146, 152, 153, 157, 158, 165, 168, 174, 178, 179, 180, 187, 189, 194, 195, 197, 199, 202},
    {1, 3, 7, 9, 19, 32, 34, 37, 42, 46, 48, 51, 54, 60, 61, 66, 71, 72, 74, 83, 86, 92, 93, 102, 111, 117, 120, 123, 124, 125, 126, 130, 132, 135, 142, 146, 152, 153, 157, 160, 165, 172, 174, 178, 187, 189, 192, 193, 202}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {2:1, 4:2, 5:3, 6:4, 9:5, 10:6, 11:7, 12:8, 14:9, 15:10, 16:11, 17:12, 18:13, 19:14, 20:15, 21:16, 22:17, 23:18, 24:19, 25:20, 26:21, 27:22, 28:23, 29:24, 30:25, 32:26, 33:27, 34:28, 36:29, 37:30, 38:31, 40:32, 41:33, 42:34, 43:35, 44:36, 45:37, 47:38, 49:39, 51:40, 52:41, 53:42, 54:43, 55:44, 57:45, 58:46, 59:47, 61:48, 62:49, 63:50, 67:51, 69:52, 70:53, 71:54, 72:55, 73:56, 74:57, 75:58, 77:59, 82:60, 83:61, 84:62, 85:63, 86:64, 88:65, 90:66, 91:67, 92:68, 94:69, 96:70, 99:71, 100:72, 101:73, 102:74, 103:75, 105:76, 106:77, 107:78, 112:79, 113:80, 114:81, 115:82, 117:83, 119:84, 123:85, 124:86, 126:87, 130:88, 135:89, 136:90, 137:91, 138:92, 139:93, 141:94, 142:95, 143:96, 144:97, 145:98, 146:99, 148:100, 149:101, 150:102, 151:103, 153:104, 154:105, 155:106, 156:107, 158:108, 159:109, 160:110, 161:111, 162:112, 166:113, 167:114, 170:115, 172:116, 173:117, 174:118, 175:119, 176:120, 178:121, 182:122, 183:123, 184:124, 185:125, 187:126, 188:127, 189:128, 191:129, 192:130, 193:131, 194:132, 195:133, 196:134, 197:135, 200:136, 201:137, 202:138, 203:139, 204:140, 205:141, 207:142, 208:143, 209:144, 210:145, 212:146, 214:147, 215:148, 216:149, 217:150, 220:151, 224:152, 227:153, 228:154, 230:155, 231:156, 232:157, 233:158, 234:159, 235:160, 236:161, 238:162, 239:163, 241:164, 242:165, 243:166, 244:167, 245:168, 246:169, 248:170, 249:171, 250:172, 252:173, 254:174, 256:175, 258:176, 259:177, 261:178, 262:179, 263:180, 265:181, 266:182, 267:183, 268:184, 269:185, 270:186, 273:187, 280:188, 282:189, 284:190, 285:191, 286:192, 288:193, 289:194, 291:195, 292:196, 293:197, 294:198, 295:199, 296:200, 299:201, 300:202}

    rule_expressions[1] = "(altitude <= 500) != (not (altitude <= 500))"
    rule_expressions[2] = "(altitude <= 500) != (altitude <= 499)"
    rule_expressions[3] = "(altitude <= 500) != (speed <= 500)"
    rule_expressions[4] = "(altitude <= 500) != (altitude <= 494)"
    rule_expressions[5] = "(altitude <= 500) != (altitude <= 499)"
    rule_expressions[6] = "(altitude <= 500) != (speed <= 500)"
    rule_expressions[7] = "(201 <= altitude <= 626) != (altitude >= 201 <= 626)"
    rule_expressions[8] = "(201 <= altitude <= 626) != (201 <= speed <= 626)"
    rule_expressions[9] = "(201 <= altitude <= 626) != (not (201 <= altitude <= 626))"
    rule_expressions[10] = "(201 <= altitude <= 626) != (not (201 <= altitude <= 626))"
    rule_expressions[11] = "(201 <= altitude <= 626) != (altitude >= 201 <= 626)"
    rule_expressions[12] = "(201 <= altitude <= 626) != (201 <= altitude <= 625)"
    rule_expressions[13] = "(201 <= altitude <= 626) != (-201 <= altitude <= 626)"
    rule_expressions[14] = "(201 <= altitude <= 626) != (201 <= -altitude <= 626)"
    rule_expressions[15] = "(201 <= altitude <= 626) != (201 <= altitude <= -626)"
    rule_expressions[16] = "(3 <= speed <= 76) != (3 <= voltage_mv <= 76)"
    rule_expressions[17] = "(3 <= speed <= 76) != (3 <= voltage_mv <= 76)"
    rule_expressions[18] = "(3 <= speed <= 76) != (1 <= speed <= 76)"
    rule_expressions[19] = "(3 <= speed <= 76) != (3 <= -speed <= 76)"
    rule_expressions[20] = "(3 <= speed <= 76) != (4 <= speed <= 76)"
    rule_expressions[21] = "(3 <= speed <= 76) != (3 <= voltage_mv <= 76)"
    rule_expressions[22] = "(3 <= speed <= 76) != (speed >= 3 <= 76)"
    rule_expressions[23] = "(3 <= speed <= 76) != (-3 <= speed <= 76)"
    rule_expressions[24] = "(3 <= speed <= 76) != (3 <= speed <= 66)"
    rule_expressions[25] = "(3 <= speed <= 76) != (6 <= speed <= 76)"
    rule_expressions[26] = "(speed > 20 and speed < 10) != (speed > 20 or speed < 10)"
    rule_expressions[27] = "(speed > 20 and speed < 10) != (altitude > 20 and speed < 10)"
    rule_expressions[28] = "(speed > 20 and speed < 10) != (speed > -20 and speed < 10)"
    rule_expressions[29] = "(speed > 20 and speed < 10) != (speed > 20 or speed < 10)"
    rule_expressions[30] = "(speed > 20 and speed < 10) != (voltage_mv > 20 and speed < 10)"
    rule_expressions[31] = "(speed > 20 and speed < 10) != (speed > 20 and -speed < 10)"
    rule_expressions[32] = "(speed > 20 and speed < 10) != (not (speed > 20 and speed < 10))"
    rule_expressions[33] = "(voltage_mv > 55) != (voltage_mv > -55)"
    rule_expressions[34] = "(voltage_mv > 55) != (altitude > 55)"
    rule_expressions[35] = "(voltage_mv > 55) != (voltage_mv > 110)"
    rule_expressions[36] = "(voltage_mv > 55) != (voltage_mv > 53)"
    rule_expressions[37] = "(voltage_mv > 55) != (not (voltage_mv > 55))"
    rule_expressions[38] = "(voltage_mv > 55) != (voltage_mv > -55)"
    rule_expressions[39] = "(voltage_mv > 55) != (voltage_mv > 50)"
    rule_expressions[40] = "(voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 and altitude > 500)"
    rule_expressions[41] = "(voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 or -altitude > 500)"
    rule_expressions[42] = "(voltage_mv <= 78 or altitude > 500) != (speed <= 78 or altitude > 500)"
    rule_expressions[43] = "(voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 156 or altitude > 500)"
    rule_expressions[44] = "(voltage_mv <= 78 or altitude > 500) != (voltage_mv <= -78 or altitude > 500)"
    rule_expressions[45] = "(voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 83 or altitude > 500)"
    rule_expressions[46] = "(voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 or altitude > -500)"
    rule_expressions[47] = "(voltage_mv <= 78 or altitude > 500) != (voltage_mv <= 78 or -altitude > 500)"
    rule_expressions[48] = "(altitude > 297 or speed <= 30) != (altitude > 297 and speed <= 30)"
    rule_expressions[49] = "(altitude > 297 or speed <= 30) != (altitude > 297 and speed <= 30)"
    rule_expressions[50] = "(altitude > 297 or speed <= 30) != (altitude > 297 or -speed <= 30)"
    rule_expressions[51] = "(altitude > 297 or speed <= 30) != (not (altitude > 297 or speed <= 30))"
    rule_expressions[52] = "(altitude > 297 or speed <= 30) != (speed > 297 or speed <= 30)"
    rule_expressions[53] = "(altitude > 297 or speed <= 30) != (altitude > -297 or speed <= 30)"
    rule_expressions[54] = "(speed <= 92 or speed != 50) != (not (speed <= 92 or speed != 50))"
    rule_expressions[55] = "(speed <= 92 or speed != 50) != (altitude <= 92 or speed != 50)"
    rule_expressions[56] = "(speed <= 92 or speed != 50) != (altitude <= 92 or speed != 50)"
    rule_expressions[57] = "(speed <= 92 or speed != 50) != (speed <= 92 and speed != 50)"
    rule_expressions[58] = "(speed <= 92 or speed != 50) != (speed <= 92 and speed != 50)"
    rule_expressions[59] = "(speed <= 92 or speed != 50) != (speed <= -92 or speed != 50)"
    rule_expressions[60] = "(speed > 100) != (voltage_mv > 100)"
    rule_expressions[61] = "(speed > 100) != (not (speed > 100))"
    rule_expressions[62] = "(speed > 100) != (not (speed > 100))"
    rule_expressions[63] = "(speed > 100) != (not (speed > 100))"
    rule_expressions[64] = "(speed > 100) != (not (speed > 100))"
    rule_expressions[65] = "(speed > 100) != (voltage_mv > 100)"
    rule_expressions[66] = "(speed > 100) != (speed > -100)"
    rule_expressions[67] = "(voltage_mv >= 100 and speed >= 100) != (speed >= 100 and speed >= 100)"
    rule_expressions[68] = "(voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 98 and speed >= 100)"
    rule_expressions[69] = "(voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 100 and speed >= 200)"
    rule_expressions[70] = "(voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 100 and speed >= 98)"
    rule_expressions[71] = "(voltage_mv >= 100 and speed >= 100) != (voltage_mv >= 100 or speed >= 100)"
    rule_expressions[72] = "(voltage_mv >= 100 and speed >= 100) != (not (voltage_mv >= 100 and speed >= 100))"
    rule_expressions[73] = "(voltage_mv >= 20) != (voltage_mv >= -20)"
    rule_expressions[74] = "(voltage_mv >= 20) != (not (voltage_mv >= 20))"
    rule_expressions[75] = "(voltage_mv >= 20) != (not (voltage_mv >= 20))"
    rule_expressions[76] = "(voltage_mv >= 20) != (altitude >= 20)"
    rule_expressions[77] = "(voltage_mv >= 20) != (voltage_mv >= 21)"
    rule_expressions[78] = "(voltage_mv >= 20) != (voltage_mv >= -20)"
    rule_expressions[79] = "(speed != 100 or altitude <= 538) != (speed != -100 or altitude <= 538)"
    rule_expressions[80] = "(speed != 100 or altitude <= 538) != (speed != 100 and altitude <= 538)"
    rule_expressions[81] = "(speed != 100 or altitude <= 538) != (speed != 100 or altitude <= -538)"
    rule_expressions[82] = "(speed != 100 or altitude <= 538) != (speed != 100 or -altitude <= 538)"
    rule_expressions[83] = "(speed != 100 or altitude <= 538) != (not (speed != 100 or altitude <= 538))"
    rule_expressions[84] = "(speed != 100 or altitude <= 538) != (speed != 200 or altitude <= 538)"
    rule_expressions[85] = "(speed != 2) != (speed != 7)"
    rule_expressions[86] = "(speed != 2) != (not (speed != 2))"
    rule_expressions[87] = "(speed != 2) != (voltage_mv != 2)"
    rule_expressions[88] = "(speed != 2) != (not (speed != 2))"
    rule_expressions[89] = "(speed <= 20 and voltage_mv > 50) != (voltage_mv <= 20 and voltage_mv > 50)"
    rule_expressions[90] = "(speed <= 20 and voltage_mv > 50) != (speed <= 20 and -voltage_mv > 50)"
    rule_expressions[91] = "(speed <= 20 and voltage_mv > 50) != (voltage_mv <= 20 and voltage_mv > 50)"
    rule_expressions[92] = "(speed <= 20 and voltage_mv > 50) != (speed <= 20 or voltage_mv > 50)"
    rule_expressions[93] = "(speed <= 20 and voltage_mv > 50) != (not (speed <= 20 and voltage_mv > 50))"
    rule_expressions[94] = "(33 <= speed <= 73) != (31 <= speed <= 73)"
    rule_expressions[95] = "(33 <= speed <= 73) != (33 <= speed <= 78)"
    rule_expressions[96] = "(33 <= speed <= 73) != (33 <= speed <= 72)"
    rule_expressions[97] = "(33 <= speed <= 73) != (33 <= speed <= 75)"
    rule_expressions[98] = "(33 <= speed <= 73) != (speed >= 33 <= 73)"
    rule_expressions[99] = "(33 <= speed <= 73) != (34 <= speed <= 73)"
    rule_expressions[100] = "(33 <= speed <= 73) != (33 <= speed <= -73)"
    rule_expressions[101] = "(33 <= speed <= 73) != (33 <= voltage_mv <= 73)"
    rule_expressions[102] = "(33 <= speed <= 73) != (not (33 <= speed <= 73))"
    rule_expressions[103] = "(altitude != speed + 20) != (altitude != speed + 26)"
    rule_expressions[104] = "(altitude != speed + 20) != (altitude != -speed + 20)"
    rule_expressions[105] = "(altitude != speed + 20) != (altitude != speed + -20)"
    rule_expressions[106] = "(altitude != speed + 20) != (altitude != speed + 10)"
    rule_expressions[107] = "(altitude != speed + 20) != (altitude != speed + -20)"
    rule_expressions[108] = "(altitude != speed + 20) != (altitude != speed + 10)"
    rule_expressions[109] = "(altitude != speed + 20) != (voltage_mv != speed + 20)"
    rule_expressions[110] = "(altitude != speed + 20) != (altitude != speed + 18)"
    rule_expressions[111] = "(voltage_mv == 5) != (not (voltage_mv == 5))"
    rule_expressions[112] = "(voltage_mv == 5) != (voltage_mv == 15)"
    rule_expressions[113] = "(voltage_mv == 5) != (not (voltage_mv == 5))"
    rule_expressions[114] = "(voltage_mv == 5) != (altitude == 5)"
    rule_expressions[115] = "(voltage_mv == 5) != (voltage_mv == 15)"
    rule_expressions[116] = "(altitude == 500 and speed != 5) != (altitude == -500 and speed != 5)"
    rule_expressions[117] = "(altitude == 500 and speed != 5) != (not (altitude == 500 and speed != 5))"
    rule_expressions[118] = "(altitude == 500 and speed != 5) != (speed == 500 and speed != 5)"
    rule_expressions[119] = "(altitude == 500 and speed != 5) != (altitude == -500 and speed != 5)"
    rule_expressions[120] = "(altitude == 500 and speed != 5) != (altitude == 500 or speed != 5)"
    rule_expressions[121] = "(altitude == 500 and speed != 5) != (altitude == 499 and speed != 5)"
    rule_expressions[122] = "(voltage_mv <= 20) != (voltage_mv <= -20)"
    rule_expressions[123] = "(voltage_mv <= 20) != (voltage_mv <= 21)"
    rule_expressions[124] = "(voltage_mv <= 20) != (not (voltage_mv <= 20))"
    rule_expressions[125] = "(voltage_mv <= 20) != (voltage_mv <= 25)"
    rule_expressions[126] = "(voltage_mv <= 20) != (voltage_mv <= 40)"
    rule_expressions[127] = "(voltage_mv <= 20) != (voltage_mv <= -20)"
    rule_expressions[128] = "(voltage_mv <= 20) != (voltage_mv <= 10)"
    rule_expressions[129] = "(voltage_mv <= speed - 50) != (voltage_mv <= speed - 51)"
    rule_expressions[130] = "(voltage_mv <= speed - 50) != (not (voltage_mv <= speed - 50))"
    rule_expressions[131] = "(voltage_mv <= speed - 50) != (speed >= voltage_mv - 50)"
    rule_expressions[132] = "(voltage_mv <= speed - 50) != (voltage_mv <= speed - 100)"
    rule_expressions[133] = "(voltage_mv <= speed - 50) != (voltage_mv <= speed - -50)"
    rule_expressions[134] = "(voltage_mv <= speed - 50) != (not (voltage_mv <= speed - 50))"
    rule_expressions[135] = "(voltage_mv <= speed - 50) != (voltage_mv <= -speed - 50)"
    rule_expressions[136] = "(voltage_mv <= speed - 50) != (voltage_mv <= speed - 48)"
    rule_expressions[137] = "(altitude != speed * 2) != (speed != altitude * 2)"
    rule_expressions[138] = "(altitude != speed * 2) != (speed != speed * 2)"
    rule_expressions[139] = "(altitude != speed * 2) != (altitude != speed * -2)"
    rule_expressions[140] = "(altitude != speed * 2) != (altitude != speed * 4)"
    rule_expressions[141] = "(altitude != speed * 2) != (altitude != speed * 4)"
    rule_expressions[142] = "(altitude != speed * 2) != (not (altitude != speed * 2))"
    rule_expressions[143] = "(altitude != speed * 2) != (altitude != speed * -2)"
    rule_expressions[144] = "(altitude != speed * 2) != (speed != altitude * 2)"
    rule_expressions[145] = "(altitude != speed * 2) != (not (altitude != speed * 2))"
    rule_expressions[146] = "(voltage_mv + speed == 50) != (not (voltage_mv + speed == 50))"
    rule_expressions[147] = "(voltage_mv + speed == 50) != (voltage_mv + 50 == speed)"
    rule_expressions[148] = "(voltage_mv + speed == 50) != (not (voltage_mv + speed == 50))"
    rule_expressions[149] = "(voltage_mv + speed == 50) != (voltage_mv + -speed == 50)"
    rule_expressions[150] = "(voltage_mv + speed == 50) != (altitude + speed == 50)"
    rule_expressions[151] = "(voltage_mv + speed == 50) != (altitude + speed == 50)"
    rule_expressions[152] = "(altitude == 5 or voltage_mv != 20) != (not (altitude == 5 or voltage_mv != 20))"
    rule_expressions[153] = "(altitude == 5 or voltage_mv != 20) != (altitude == 5 and voltage_mv != 20)"
    rule_expressions[154] = "(altitude == 5 or voltage_mv != 20) != (altitude == 5 or -voltage_mv != 20)"
    rule_expressions[155] = "(altitude == 5 or voltage_mv != 20) != (altitude == 5 or voltage_mv != -20)"
    rule_expressions[156] = "(voltage_mv > 20) != (altitude > 20)"
    rule_expressions[157] = "(voltage_mv > 20) != (not (voltage_mv > 20))"
    rule_expressions[158] = "(voltage_mv > 20) != (voltage_mv > -20)"
    rule_expressions[159] = "(voltage_mv > 20) != (voltage_mv > -20)"
    rule_expressions[160] = "(voltage_mv > 20) != (voltage_mv > 23)"
    rule_expressions[161] = "(voltage_mv > 20) != (voltage_mv > 18)"
    rule_expressions[162] = "(voltage_mv > 20) != (altitude > 20)"
    rule_expressions[163] = "(voltage_mv > 20) != (not (voltage_mv > 20))"
    rule_expressions[164] = "(258 <= altitude <= 691) != (258 <= speed <= 691)"
    rule_expressions[165] = "(258 <= altitude <= 691) != (not (258 <= altitude <= 691))"
    rule_expressions[166] = "(258 <= altitude <= 691) != (257 <= altitude <= 691)"
    rule_expressions[167] = "(258 <= altitude <= 691) != (258 <= altitude <= -691)"
    rule_expressions[168] = "(258 <= altitude <= 691) != (-258 <= altitude <= 691)"
    rule_expressions[169] = "(258 <= altitude <= 691) != (251 <= altitude <= 691)"
    rule_expressions[170] = "(258 <= altitude <= 691) != (258 <= -altitude <= 691)"
    rule_expressions[171] = "(258 <= altitude <= 691) != (not (258 <= altitude <= 691))"
    rule_expressions[172] = "(258 <= altitude <= 691) != (altitude >= 258 <= 691)"
    rule_expressions[173] = "(speed != 10) != (speed != 20)"
    rule_expressions[174] = "(speed != 10) != (not (speed != 10))"
    rule_expressions[175] = "(speed != 10) != (not (speed != 10))"
    rule_expressions[176] = "(speed != 10) != (voltage_mv != 10)"
    rule_expressions[177] = "(speed != 10) != (voltage_mv != 10)"
    rule_expressions[178] = "(altitude < 20) != (not (altitude < 20))"
    rule_expressions[179] = "(altitude < 20) != (altitude < 25)"
    rule_expressions[180] = "(altitude < 20) != (voltage_mv < 20)"
    rule_expressions[181] = "(altitude < 20) != (altitude < -20)"
    rule_expressions[182] = "(altitude < 20) != (not (altitude < 20))"
    rule_expressions[183] = "(altitude < 20) != (altitude < 10)"
    rule_expressions[184] = "(altitude < 20) != (altitude < 25)"
    rule_expressions[185] = "(altitude < 20) != (speed < 20)"
    rule_expressions[186] = "(altitude < 20) != (not (altitude < 20))"
    rule_expressions[187] = "(speed < 2) != (not (speed < 2))"
    rule_expressions[188] = "(speed < 2) != (not (speed < 2))"
    rule_expressions[189] = "(altitude >= 472 and speed >= 100) != (not (altitude >= 472 and speed >= 100))"
    rule_expressions[190] = "(altitude >= 472 and speed >= 100) != (altitude >= 472 and speed >= -100)"
    rule_expressions[191] = "(altitude >= 472 and speed >= 100) != (not (altitude >= 472 and speed >= 100))"
    rule_expressions[192] = "(altitude >= 472 and speed >= 100) != (altitude >= 472 and -speed >= 100)"
    rule_expressions[193] = "(altitude >= 472 and speed >= 100) != (altitude >= 944 and speed >= 100)"
    rule_expressions[194] = "(altitude >= 472 and speed >= 100) != (altitude >= 472 or speed >= 100)"
    rule_expressions[195] = "(voltage_mv <= 2) != (speed <= 2)"
    rule_expressions[196] = "(voltage_mv <= 2) != (voltage_mv <= 12)"
    rule_expressions[197] = "(voltage_mv <= 2) != (voltage_mv <= -2)"
    rule_expressions[198] = "(voltage_mv <= 2) != (speed <= 2)"
    rule_expressions[199] = "(voltage_mv <= 2) != (altitude <= 2)"
    rule_expressions[200] = "(voltage_mv <= 2) != (voltage_mv <= -2)"
    rule_expressions[201] = "(voltage_mv <= 2) != (voltage_mv <= 3)"
    rule_expressions[202] = "(voltage_mv <= 2) != (not (voltage_mv <= 2))"

    return rule_expressions