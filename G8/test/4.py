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
    if (voltage_mv == 5) != (voltage_mv == 6):
        triggered.add(1)
    # 变异规则 2 - ABS
    if (voltage_mv == 5) != (abs(voltage_mv) == 5):
        t = 1
    # 变异规则 3 - LCR
    if (voltage_mv == 5) != (voltage_mv == 10):
        triggered.add(2)
    # 变异规则 4 - SVR
    if (voltage_mv == 5) != (altitude == 5):
        triggered.add(3)
    # 变异规则 5 - RSR
    if (voltage_mv == 5) != (not (voltage_mv == 5)):
        triggered.add(4)
    # 变异规则 6 - ROR
    if (voltage_mv == 5) != (voltage_mv == 3):
        triggered.add(5)
    # 变异规则 7 - CSR
    if (voltage_mv == 5) != (voltage_mv == -5):
        triggered.add(6)
    # 变异规则 8 - SAR
    if (voltage_mv == 5) != (5 == voltage_mv):
        t = 1
    # 变异规则 9 - SRC
    if (voltage_mv == 5) != (voltage_mv == 9):
        triggered.add(7)
    # 变异规则 10 - CAR
    if (voltage_mv == 5) != (voltage_mv == 10):
        triggered.add(8)
    # 原语句
    if voltage_mv == 5:
        health_score += 8
    # 原语句2
    # 变异规则 11 - AOR
    if (18 <= voltage_mv <= 98) != (18 <= -voltage_mv <= 98):
        triggered.add(9)
    # 变异规则 12 - LCR
    if (18 <= voltage_mv <= 98) != (not (18 <= voltage_mv <= 98)):
        triggered.add(10)
    # 变异规则 13 - SRC
    if (18 <= voltage_mv <= 98) != (26 <= voltage_mv <= 98):
        triggered.add(11)
    # 变异规则 14 - ROR
    if (18 <= voltage_mv <= 98) != (17 <= voltage_mv <= 98):
        triggered.add(12)
    # 变异规则 15 - CAR
    if (18 <= voltage_mv <= 98) != (20 <= voltage_mv <= 98):
        triggered.add(13)
    # 变异规则 16 - CRP
    if (18 <= voltage_mv <= 98) != (9 <= voltage_mv <= 98):
        triggered.add(14)
    # 变异规则 17 - SAR
    if (18 <= voltage_mv <= 98) != (voltage_mv >= 18 <= 98):
        triggered.add(15)
    # 变异规则 18 - SCR
    if (18 <= voltage_mv <= 98) != (23 <= voltage_mv <= 98):
        triggered.add(16)
    # 变异规则 19 - UOI
    if (18 <= voltage_mv <= 98) != (18 <= -voltage_mv <= 98):
        triggered.add(17)
    # 变异规则 20 - RSR
    if (18 <= voltage_mv <= 98) != (not (18 <= voltage_mv <= 98)):
        triggered.add(18)
    # 原语句
    if 18 <= voltage_mv <= 98:
        health_score -= 21
        speed = min(speed + 2, 100)
    # 原语句3
    # 变异规则 21 - LCR
    if (speed < 30) != (speed < -30):
        triggered.add(19)
    # 变异规则 22 - SVR
    if (speed < 30) != (altitude < 30):
        triggered.add(20)
    # 变异规则 23 - CSR
    if (speed < 30) != (speed < -30):
        triggered.add(21)
    # 变异规则 24 - SCR
    if (speed < 30) != (speed < 60):
        triggered.add(22)
    # 变异规则 25 - ABS
    if (speed < 30) != (abs(speed) < 30):
        t = 1
    # 变异规则 26 - SAR
    if (speed < 30) != (30 > speed):
        t = 1
    # 变异规则 27 - AOR
    if (speed < 30) != (speed < 27):
        triggered.add(23)
    # 变异规则 28 - CAR
    if (speed < 30) != (speed < 32):
        triggered.add(24)
    # 变异规则 29 - ROR
    if (speed < 30) != (speed < -30):
        triggered.add(25)
    # 变异规则 30 - SRC
    if (speed < 30) != (speed < 38):
        triggered.add(26)
    # 原语句
    if speed < 30:
        health_score -= 18
        altitude = max(altitude - 49, 2)
        voltage_mv = max(voltage_mv - 2, 2)
    # 原语句4
    # 变异规则 31 - RSR
    if (voltage_mv >= 10 and voltage_mv >= 50) != (not (voltage_mv >= 10 and voltage_mv >= 50)):
        triggered.add(27)
    # 变异规则 32 - AOR
    if (voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 or voltage_mv >= 50):
        triggered.add(28)
    # 变异规则 33 - ABS
    if (voltage_mv >= 10 and voltage_mv >= 50) != (abs(voltage_mv) >= 10 and voltage_mv >= 50):
        t = 1
    # 变异规则 34 - SCR
    if (voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 1 and voltage_mv >= 50):
        t = 1
    # 变异规则 35 - SAR
    if (voltage_mv >= 10 and voltage_mv >= 50) != (10 <= voltage_mv and voltage_mv >= 50):
        t = 1
    # 变异规则 36 - CAR
    if (voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 and voltage_mv >= 48):
        triggered.add(29)
    # 变异规则 37 - CRP
    if (voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 and voltage_mv >= 54):
        triggered.add(30)
    # 变异规则 38 - ROR
    if (voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 50 and voltage_mv >= 10):
        t = 1
    # 变异规则 39 - SRC
    if (voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 50 and voltage_mv >= 10):
        t = 1
    # 变异规则 40 - LCR
    if (voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 or voltage_mv >= 50):
        triggered.add(31)
    # 原语句
    if voltage_mv >= 10 and voltage_mv >= 50:
        health_score += 14
        altitude = min(altitude + 22, 1000)
        voltage_mv, speed = speed, voltage_mv
    # 原语句5
    # 变异规则 41 - CSR
    if (altitude > 500) != (altitude > -500):
        triggered.add(32)
    # 变异规则 42 - ABS
    if (altitude > 500) != (abs(altitude) > 500):
        t = 1
    # 变异规则 43 - RSR
    if (altitude > 500) != (not (altitude > 500)):
        triggered.add(33)
    # 变异规则 44 - SAR
    if (altitude > 500) != (500 < altitude):
        t = 1
    # 变异规则 45 - AOR
    if (altitude > 500) != (altitude > 505):
        triggered.add(34)
    # 变异规则 46 - SVR
    if (altitude > 500) != (speed > 500):
        triggered.add(35)
    # 变异规则 47 - CAR
    if (altitude > 500) != (altitude > 510):
        triggered.add(36)
    # 变异规则 48 - LCR
    if (altitude > 500) != (speed > 500):
        triggered.add(37)
    # 变异规则 49 - SRC
    if (altitude > 500) != (altitude > 502):
        triggered.add(38)
    # 变异规则 50 - UOI
    if (altitude > 500) != (abs(altitude) > 500):
        t = 1
    # 原语句
    if altitude > 500:
        health_score -= 30
        altitude = min(altitude + 56, 1000)
    # 原语句6
    # 变异规则 51 - ROR
    if (altitude == speed * 200) != (altitude == -speed * 200):
        triggered.add(39)
    # 变异规则 52 - CRP
    if (altitude == speed * 200) != (altitude == speed * 202):
        triggered.add(40)
    # 变异规则 53 - SVR
    if (altitude == speed * 200) != (speed == speed * 200):
        triggered.add(41)
    # 变异规则 54 - CSR
    if (altitude == speed * 200) != (altitude == speed * -200):
        triggered.add(42)
    # 变异规则 55 - ABS
    if (altitude == speed * 200) != (abs(altitude) == speed * 200):
        t = 1
    # 变异规则 56 - SRC
    if (altitude == speed * 200) != (not (altitude == speed * 200)):
        triggered.add(43)
    # 变异规则 57 - UOI
    if (altitude == speed * 200) != (altitude == -speed * 200):
        triggered.add(44)
    # 变异规则 58 - AOR
    if (altitude == speed * 200) != (altitude == -speed * 200):
        triggered.add(45)
    # 变异规则 59 - RSR
    if (altitude == speed * 200) != (not (altitude == speed * 200)):
        triggered.add(46)
    # 变异规则 60 - SAR
    if (altitude == speed * 200) != (speed == altitude * 200):
        triggered.add(47)
    # 原语句
    if altitude == speed * 200:
        health_score -= 25
    # 原语句7
    # 变异规则 61 - SAR
    if (voltage_mv // 5 <= speed) != (voltage_mv // speed >= 5):
        triggered.add(48)
    # 变异规则 62 - CRP
    if (voltage_mv // 5 <= speed) != (voltage_mv // 10 <= speed):
        triggered.add(49)
    # 变异规则 63 - CSR
    if (voltage_mv // 5 <= speed) != (voltage_mv // -5 <= speed):
        triggered.add(50)
    # 变异规则 64 - SVR
    if (voltage_mv // 5 <= speed) != (speed // 5 <= speed):
        triggered.add(51)
    # 变异规则 65 - CAR
    if (voltage_mv // 5 <= speed) != (voltage_mv // 6 <= speed):
        triggered.add(52)
    # 变异规则 66 - LCR
    if (voltage_mv // 5 <= speed) != (altitude // 5 <= speed):
        triggered.add(53)
    # 变异规则 67 - SCR
    if (voltage_mv // 5 <= speed) != (voltage_mv // 3 <= speed):
        triggered.add(54)
    # 变异规则 68 - ABS
    if (voltage_mv // 5 <= speed) != (voltage_mv // 5 <= abs(speed)):
        t = 1
    # 变异规则 69 - AOR
    if (voltage_mv // 5 <= speed) != (voltage_mv // 5 <= abs(speed)):
        t = 1
    # 变异规则 70 - RSR
    if (voltage_mv // 5 <= speed) != (not (voltage_mv // 5 <= speed)):
        triggered.add(55)
    # 原语句
    if voltage_mv // 5 <= speed:
        health_score += 16
        speed = max(speed - 1, 2)
    # 原语句8
    # 变异规则 71 - LCR
    if (altitude == voltage_mv // 497) != (abs(altitude) == voltage_mv // 497):
        t = 1
    # 变异规则 72 - CSR
    if (altitude == voltage_mv // 497) != (altitude == voltage_mv // -497):
        t = 1
    # 变异规则 73 - SVR
    if (altitude == voltage_mv // 497) != (voltage_mv == voltage_mv // 497):
        t = 1
    # 变异规则 74 - ROR
    if (altitude == voltage_mv // 497) != (altitude == voltage_mv // 488):
        t = 1
    # 变异规则 75 - SAR
    if (altitude == voltage_mv // 497) != (voltage_mv == altitude // 497):
        triggered.add(56)
    # 变异规则 76 - CRP
    if (altitude == voltage_mv // 497) != (altitude == voltage_mv // 489):
        t = 1
    # 变异规则 77 - CAR
    if (altitude == voltage_mv // 497) != (altitude == voltage_mv // 498):
        t = 1
    # 变异规则 78 - ABS
    if (altitude == voltage_mv // 497) != (abs(altitude) == voltage_mv // 497):
        t = 1
    # 变异规则 79 - AOR
    if (altitude == voltage_mv // 497) != (speed == voltage_mv // 497):
        t = 1
    # 变异规则 80 - RSR
    if (altitude == voltage_mv // 497) != (not (altitude == voltage_mv // 497)):
        triggered.add(57)
    # 原语句
    if altitude == voltage_mv // 497:
        health_score += 2
        voltage_mv = min(voltage_mv + 1, 100)
    # 原语句9
    # 变异规则 81 - RSR
    if (voltage_mv >= 71 and speed > 13) != (not (voltage_mv >= 71 and speed > 13)):
        triggered.add(58)
    # 变异规则 82 - CSR
    if (voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 and speed > -13):
        t = 1
    # 变异规则 83 - UOI
    if (voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 and -speed > 13):
        triggered.add(59)
    # 变异规则 84 - SRC
    if (voltage_mv >= 71 and speed > 13) != (speed > 13 and voltage_mv >= 71):
        t = 1
    # 变异规则 85 - AOR
    if (voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 or speed > 13):
        triggered.add(60)
    # 变异规则 86 - ABS
    if (voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 and abs(speed) > 13):
        t = 1
    # 变异规则 87 - CAR
    if (voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 and speed > 3):
        t = 1
    # 变异规则 88 - SAR
    if (voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 and 13 < speed):
        t = 1
    # 变异规则 89 - CRP
    if (voltage_mv >= 71 and speed > 13) != (voltage_mv >= 35 and speed > 13):
        triggered.add(61)
    # 变异规则 90 - SCR
    if (voltage_mv >= 71 and speed > 13) != (speed >= 71 and speed > 13):
        triggered.add(62)
    # 原语句
    if voltage_mv >= 71 and speed > 13:
        health_score -= 6
    # 原语句10
    # 变异规则 91 - CRP
    if (voltage_mv <= 100) != (voltage_mv <= 104):
        t = 1
    # 变异规则 92 - SVR
    if (voltage_mv <= 100) != (speed <= 100):
        t = 1
    # 变异规则 93 - SCR
    if (voltage_mv <= 100) != (voltage_mv <= 50):
        triggered.add(63)
    # 变异规则 94 - CAR
    if (voltage_mv <= 100) != (voltage_mv <= 102):
        t = 1
    # 变异规则 95 - LCR
    if (voltage_mv <= 100) != (not (voltage_mv <= 100)):
        triggered.add(64)
    # 变异规则 96 - UOI
    if (voltage_mv <= 100) != (altitude <= 100):
        triggered.add(65)
    # 变异规则 97 - RSR
    if (voltage_mv <= 100) != (not (voltage_mv <= 100)):
        triggered.add(66)
    # 变异规则 98 - ABS
    if (voltage_mv <= 100) != (abs(voltage_mv) <= 100):
        t = 1
    # 变异规则 99 - ROR
    if (voltage_mv <= 100) != (voltage_mv <= -100):
        triggered.add(67)
    # 变异规则 100 - SAR
    if (voltage_mv <= 100) != (100 >= voltage_mv):
        t = 1
    # 原语句
    if voltage_mv <= 100:
        health_score += 20
        speed, altitude = altitude, speed
    # 原语句11
    # 变异规则 101 - CAR
    if (voltage_mv < 30) != (voltage_mv < 25):
        triggered.add(68)
    # 变异规则 102 - CSR
    if (voltage_mv < 30) != (voltage_mv < -30):
        triggered.add(69)
    # 变异规则 103 - SVR
    if (voltage_mv < 30) != (altitude < 30):
        triggered.add(70)
    # 变异规则 104 - ROR
    if (voltage_mv < 30) != (voltage_mv < 35):
        triggered.add(71)
    # 变异规则 105 - LCR
    if (voltage_mv < 30) != (voltage_mv < 29):
        triggered.add(72)
    # 变异规则 106 - SAR
    if (voltage_mv < 30) != (30 > voltage_mv):
        t = 1
    # 变异规则 107 - CRP
    if (voltage_mv < 30) != (voltage_mv < 38):
        triggered.add(73)
    # 变异规则 108 - SRC
    if (voltage_mv < 30) != (not (voltage_mv < 30)):
        triggered.add(74)
    # 变异规则 109 - ABS
    if (voltage_mv < 30) != (abs(voltage_mv) < 30):
        t = 1
    # 变异规则 110 - UOI
    if (voltage_mv < 30) != (not (voltage_mv < 30)):
        triggered.add(75)
    # 原语句
    if voltage_mv < 30:
        health_score -= 4
        altitude = min(altitude + 99, 1000)
        speed = min(speed + 4, 100)
        voltage_mv = min(voltage_mv + 1, 100)
    # 原语句12
    # 变异规则 111 - CSR
    if (altitude >= 728) != (altitude >= -728):
        triggered.add(76)
    # 变异规则 112 - SCR
    if (altitude >= 728) != (voltage_mv >= 728):
        t = 1
    # 变异规则 113 - AOR
    if (altitude >= 728) != (altitude >= 731):
        t = 1
    # 变异规则 114 - SAR
    if (altitude >= 728) != (728 <= altitude):
        t = 1
    # 变异规则 115 - LCR
    if (altitude >= 728) != (altitude >= 723):
        t = 1
    # 变异规则 116 - SVR
    if (altitude >= 728) != (speed >= 728):
        triggered.add(77)
    # 变异规则 117 - RSR
    if (altitude >= 728) != (not (altitude >= 728)):
        triggered.add(78)
    # 变异规则 118 - CAR
    if (altitude >= 728) != (altitude >= 727):
        t = 1
    # 变异规则 119 - SRC
    if (altitude >= 728) != (728 <= altitude):
        t = 1
    # 变异规则 120 - ROR
    if (altitude >= 728) != (voltage_mv >= 728):
        t = 1
    # 原语句
    if altitude >= 728:
        health_score -= 18
        speed = min(speed + 6, 100)
        speed, altitude = altitude, speed
    # 原语句13
    # 变异规则 121 - LCR
    if (altitude <= speed // 455) != (not (altitude <= speed // 455)):
        triggered.add(79)
    # 变异规则 122 - ROR
    if (altitude <= speed // 455) != (altitude <= speed // 450):
        t = 1
    # 变异规则 123 - CRP
    if (altitude <= speed // 455) != (altitude <= speed // 910):
        t = 1
    # 变异规则 124 - SCR
    if (altitude <= speed // 455) != (abs(altitude) <= speed // 455):
        t = 1
    # 变异规则 125 - ABS
    if (altitude <= speed // 455) != (abs(altitude) <= speed // 455):
        t = 1
    # 变异规则 126 - SVR
    if (altitude <= speed // 455) != (voltage_mv <= speed // 455):
        t = 1
    # 变异规则 127 - RSR
    if (altitude <= speed // 455) != (not (altitude <= speed // 455)):
        triggered.add(80)
    # 变异规则 128 - AOR
    if (altitude <= speed // 455) != (voltage_mv <= speed // 455):
        t = 1
    # 变异规则 129 - SRC
    if (altitude <= speed // 455) != (voltage_mv <= speed // 455):
        t = 1
    # 变异规则 130 - UOI
    if (altitude <= speed // 455) != (altitude <= -speed // 455):
        t = 1
    # 原语句
    if altitude <= speed // 455:
        health_score -= 30
        altitude = max(altitude - 35, 2)
    # 原语句14
    # 变异规则 131 - AOR
    if (201 <= altitude <= 803) != (201 <= -altitude <= 803):
        t = 1
    # 变异规则 132 - SAR
    if (201 <= altitude <= 803) != (altitude >= 201 <= 803):
        t = 1
    # 变异规则 133 - UOI
    if (201 <= altitude <= 803) != (201 <= -altitude <= 803):
        t = 1
    # 变异规则 134 - SVR
    if (201 <= altitude <= 803) != (201 <= speed <= 803):
        triggered.add(81)
    # 变异规则 135 - CAR
    if (201 <= altitude <= 803) != (200 <= altitude <= 803):
        t = 1
    # 变异规则 136 - SCR
    if (201 <= altitude <= 803) != (not (201 <= altitude <= 803)):
        triggered.add(82)
    # 变异规则 137 - RSR
    if (201 <= altitude <= 803) != (not (201 <= altitude <= 803)):
        triggered.add(83)
    # 变异规则 138 - CRP
    if (201 <= altitude <= 803) != (201 <= altitude <= 401):
        t = 1
    # 变异规则 139 - CSR
    if (201 <= altitude <= 803) != (201 <= altitude <= -803):
        t = 1
    # 变异规则 140 - ROR
    if (201 <= altitude <= 803) != (201 <= speed <= 803):
        triggered.add(84)
    # 原语句
    if 201 <= altitude <= 803:
        health_score -= 30
        speed = min(speed + 5, 100)
        voltage_mv = max(voltage_mv - 8, 2)
    # 原语句15
    # 变异规则 141 - ABS
    if (speed + 30 >= voltage_mv) != (abs(speed) + 30 >= voltage_mv):
        t = 1
    # 变异规则 142 - SAR
    if (speed + 30 >= voltage_mv) != (speed + voltage_mv <= 30):
        triggered.add(85)
    # 变异规则 143 - CSR
    if (speed + 30 >= voltage_mv) != (speed + -30 >= voltage_mv):
        triggered.add(86)
    # 变异规则 144 - CAR
    if (speed + 30 >= voltage_mv) != (speed + 20 >= voltage_mv):
        triggered.add(87)
    # 变异规则 145 - SCR
    if (speed + 30 >= voltage_mv) != (speed + -30 >= voltage_mv):
        triggered.add(88)
    # 变异规则 146 - RSR
    if (speed + 30 >= voltage_mv) != (not (speed + 30 >= voltage_mv)):
        triggered.add(89)
    # 变异规则 147 - UOI
    if (speed + 30 >= voltage_mv) != (speed + 30 >= -voltage_mv):
        triggered.add(90)
    # 变异规则 148 - AOR
    if (speed + 30 >= voltage_mv) != (abs(speed) + 30 >= voltage_mv):
        t = 1
    # 变异规则 149 - CRP
    if (speed + 30 >= voltage_mv) != (speed + 15 >= voltage_mv):
        triggered.add(91)
    # 变异规则 150 - SVR
    if (speed + 30 >= voltage_mv) != (altitude + 30 >= voltage_mv):
        triggered.add(92)
    # 原语句
    if speed + 30 >= voltage_mv:
        health_score -= 23
    # 原语句16
    # 变异规则 151 - ROR
    if (2 <= speed <= 42) != (1 <= speed <= 42):
        t = 1
    # 变异规则 152 - CSR
    if (2 <= speed <= 42) != (-2 <= speed <= 42):
        t = 1
    # 变异规则 153 - AOR
    if (2 <= speed <= 42) != (2 <= abs(speed) <= 42):
        t = 1
    # 变异规则 154 - ABS
    if (2 <= speed <= 42) != (2 <= abs(speed) <= 42):
        t = 1
    # 变异规则 155 - CAR
    if (2 <= speed <= 42) != (4 <= speed <= 42):
        triggered.add(93)
    # 变异规则 156 - SAR
    if (2 <= speed <= 42) != (speed >= 2 <= 42):
        triggered.add(94)
    # 变异规则 157 - UOI
    if (2 <= speed <= 42) != (2 <= -speed <= 42):
        triggered.add(95)
    # 变异规则 158 - SRC
    if (2 <= speed <= 42) != (2 <= voltage_mv <= 42):
        triggered.add(96)
    # 变异规则 159 - LCR
    if (2 <= speed <= 42) != (2 <= abs(speed) <= 42):
        t = 1
    # 变异规则 160 - CRP
    if (2 <= speed <= 42) != (2 <= speed <= 36):
        triggered.add(97)
    # 原语句
    if 2 <= speed <= 42:
        health_score -= 7
    # 原语句17
    # 变异规则 161 - ROR
    if (speed >= 10 and voltage_mv == 50) != (speed >= 10 and voltage_mv == 51):
        triggered.add(98)
    # 变异规则 162 - AOR
    if (speed >= 10 and voltage_mv == 50) != (speed >= 10 and -voltage_mv == 50):
        triggered.add(99)
    # 变异规则 163 - CAR
    if (speed >= 10 and voltage_mv == 50) != (speed >= 10 and voltage_mv == 45):
        triggered.add(100)
    # 变异规则 164 - ABS
    if (speed >= 10 and voltage_mv == 50) != (abs(speed) >= 10 and voltage_mv == 50):
        t = 1
    # 变异规则 165 - UOI
    if (speed >= 10 and voltage_mv == 50) != (speed >= 10 and -voltage_mv == 50):
        triggered.add(101)
    # 变异规则 166 - SRC
    if (speed >= 10 and voltage_mv == 50) != (voltage_mv == 50 and speed >= 10):
        t = 1
    # 变异规则 167 - CRP
    if (speed >= 10 and voltage_mv == 50) != (speed >= 6 and voltage_mv == 50):
        t = 1
    # 变异规则 168 - SVR
    if (speed >= 10 and voltage_mv == 50) != (voltage_mv >= 10 and voltage_mv == 50):
        t = 1
    # 变异规则 169 - SAR
    if (speed >= 10 and voltage_mv == 50) != (10 <= speed and voltage_mv == 50):
        t = 1
    # 变异规则 170 - CSR
    if (speed >= 10 and voltage_mv == 50) != (speed >= 10 and voltage_mv == -50):
        triggered.add(102)
    # 原语句
    if speed >= 10 and voltage_mv == 50:
        health_score += 7
        voltage_mv = min(voltage_mv + 10, 100)
        altitude, speed = speed, altitude
    # 原语句18
    # 变异规则 171 - ROR
    if (altitude < 670 and voltage_mv <= 17) != (altitude < 670 or voltage_mv <= 17):
        triggered.add(103)
    # 变异规则 172 - SVR
    if (altitude < 670 and voltage_mv <= 17) != (speed < 670 and voltage_mv <= 17):
        t = 1
    # 变异规则 173 - LCR
    if (altitude < 670 and voltage_mv <= 17) != (altitude < 670 or voltage_mv <= 17):
        triggered.add(104)
    # 变异规则 174 - SAR
    if (altitude < 670 and voltage_mv <= 17) != (670 > altitude and voltage_mv <= 17):
        t = 1
    # 变异规则 175 - CSR
    if (altitude < 670 and voltage_mv <= 17) != (altitude < -670 and voltage_mv <= 17):
        triggered.add(105)
    # 变异规则 176 - CRP
    if (altitude < 670 and voltage_mv <= 17) != (altitude < 335 and voltage_mv <= 17):
        t = 1
    # 变异规则 177 - SRC
    if (altitude < 670 and voltage_mv <= 17) != (voltage_mv <= 17 and altitude < 670):
        t = 1
    # 变异规则 178 - RSR
    if (altitude < 670 and voltage_mv <= 17) != (not (altitude < 670 and voltage_mv <= 17)):
        triggered.add(106)
    # 变异规则 179 - AOR
    if (altitude < 670 and voltage_mv <= 17) != (not (altitude < 670 and voltage_mv <= 17)):
        triggered.add(107)
    # 变异规则 180 - SCR
    if (altitude < 670 and voltage_mv <= 17) != (altitude < 670 or voltage_mv <= 17):
        triggered.add(108)
    # 原语句
    if altitude < 670 and voltage_mv <= 17:
        health_score -= 29
        altitude = max(altitude - 16, 2)
    # 原语句19
    # 变异规则 181 - SCR
    if (voltage_mv < 30 and speed < 44) != (speed < 44 and voltage_mv < 30):
        t = 1
    # 变异规则 182 - CSR
    if (voltage_mv < 30 and speed < 44) != (voltage_mv < 30 and speed < -44):
        triggered.add(109)
    # 变异规则 183 - CRP
    if (voltage_mv < 30 and speed < 44) != (voltage_mv < 30 and speed < 43):
        triggered.add(110)
    # 变异规则 184 - ABS
    if (voltage_mv < 30 and speed < 44) != (voltage_mv < 30 and abs(speed) < 44):
        t = 1
    # 变异规则 185 - AOR
    if (voltage_mv < 30 and speed < 44) != (speed < 44 and voltage_mv < 30):
        t = 1
    # 变异规则 186 - ROR
    if (voltage_mv < 30 and speed < 44) != (30 > voltage_mv and speed < 44):
        t = 1
    # 变异规则 187 - SVR
    if (voltage_mv < 30 and speed < 44) != (speed < 30 and speed < 44):
        triggered.add(111)
    # 变异规则 188 - CAR
    if (voltage_mv < 30 and speed < 44) != (voltage_mv < 29 and speed < 44):
        triggered.add(112)
    # 变异规则 189 - SAR
    if (voltage_mv < 30 and speed < 44) != (30 > voltage_mv and speed < 44):
        t = 1
    # 变异规则 190 - UOI
    if (voltage_mv < 30 and speed < 44) != (voltage_mv < 30 and -speed < 44):
        triggered.add(113)
    # 原语句
    if voltage_mv < 30 and speed < 44:
        health_score += 20
    # 原语句20
    # 变异规则 191 - CAR
    if (voltage_mv != 68) != (voltage_mv != 63):
        triggered.add(114)
    # 变异规则 192 - SVR
    if (voltage_mv != 68) != (speed != 68):
        triggered.add(115)
    # 变异规则 193 - ABS
    if (voltage_mv != 68) != (abs(voltage_mv) != 68):
        t = 1
    # 变异规则 194 - AOR
    if (voltage_mv != 68) != (not (voltage_mv != 68)):
        triggered.add(116)
    # 变异规则 195 - UOI
    if (voltage_mv != 68) != (voltage_mv != -68):
        triggered.add(117)
    # 变异规则 196 - ROR
    if (voltage_mv != 68) != (speed != 68):
        triggered.add(118)
    # 变异规则 197 - CSR
    if (voltage_mv != 68) != (voltage_mv != -68):
        triggered.add(119)
    # 变异规则 198 - CRP
    if (voltage_mv != 68) != (voltage_mv != 136):
        triggered.add(120)
    # 变异规则 199 - SRC
    if (voltage_mv != 68) != (voltage_mv != 136):
        triggered.add(121)
    # 变异规则 200 - RSR
    if (voltage_mv != 68) != (not (voltage_mv != 68)):
        triggered.add(122)
    # 原语句
    if voltage_mv != 68:
        health_score += 7
        voltage_mv, speed = speed, voltage_mv
    # 原语句21
    # 变异规则 201 - ROR
    if (voltage_mv >= 49) != (not (voltage_mv >= 49)):
        triggered.add(123)
    # 变异规则 202 - AOR
    if (voltage_mv >= 49) != (altitude >= 49):
        triggered.add(124)
    # 变异规则 203 - SVR
    if (voltage_mv >= 49) != (speed >= 49):
        triggered.add(125)
    # 变异规则 204 - CAR
    if (voltage_mv >= 49) != (voltage_mv >= 54):
        triggered.add(126)
    # 变异规则 205 - SCR
    if (voltage_mv >= 49) != (voltage_mv >= -49):
        triggered.add(127)
    # 变异规则 206 - CRP
    if (voltage_mv >= 49) != (voltage_mv >= 24):
        triggered.add(128)
    # 变异规则 207 - RSR
    if (voltage_mv >= 49) != (not (voltage_mv >= 49)):
        triggered.add(129)
    # 变异规则 208 - UOI
    if (voltage_mv >= 49) != (not (voltage_mv >= 49)):
        triggered.add(130)
    # 变异规则 209 - LCR
    if (voltage_mv >= 49) != (voltage_mv >= 56):
        triggered.add(131)
    # 变异规则 210 - SRC
    if (voltage_mv >= 49) != (not (voltage_mv >= 49)):
        triggered.add(132)
    # 原语句
    if voltage_mv >= 49:
        health_score -= 13
        altitude, speed = speed, altitude
    # 原语句22
    # 变异规则 211 - UOI
    if (24 <= voltage_mv <= 61) != (24 <= -voltage_mv <= 61):
        triggered.add(133)
    # 变异规则 212 - CSR
    if (24 <= voltage_mv <= 61) != (-24 <= voltage_mv <= 61):
        triggered.add(134)
    # 变异规则 213 - LCR
    if (24 <= voltage_mv <= 61) != (12 <= voltage_mv <= 61):
        triggered.add(135)
    # 变异规则 214 - SAR
    if (24 <= voltage_mv <= 61) != (voltage_mv >= 24 <= 61):
        triggered.add(136)
    # 变异规则 215 - RSR
    if (24 <= voltage_mv <= 61) != (not (24 <= voltage_mv <= 61)):
        triggered.add(137)
    # 变异规则 216 - SCR
    if (24 <= voltage_mv <= 61) != (not (24) <= voltage_mv <= 61):
        triggered.add(138)
    # 变异规则 217 - CAR
    if (24 <= voltage_mv <= 61) != (25 <= voltage_mv <= 61):
        triggered.add(139)
    # 变异规则 218 - SVR
    if (24 <= voltage_mv <= 61) != (24 <= altitude <= 61):
        triggered.add(140)
    # 变异规则 219 - CRP
    if (24 <= voltage_mv <= 61) != (12 <= voltage_mv <= 61):
        triggered.add(141)
    # 变异规则 220 - SRC
    if (24 <= voltage_mv <= 61) != (24 <= speed <= 61):
        triggered.add(142)
    # 原语句
    if 24 <= voltage_mv <= 61:
        health_score -= 14
    # 原语句23
    # 变异规则 221 - RSR
    if (altitude % speed < 20) != (not (altitude % speed < 20)):
        triggered.add(143)
    # 变异规则 222 - SCR
    if (altitude % speed < 20) != (altitude % 20 > speed):
        triggered.add(144)
    # 变异规则 223 - LCR
    if (altitude % speed < 20) != (altitude % speed < 13):
        triggered.add(145)
    # 变异规则 224 - ROR
    if (altitude % speed < 20) != (altitude % speed < -20):
        triggered.add(146)
    # 变异规则 225 - SRC
    if (altitude % speed < 20) != (not (altitude % speed < 20)):
        triggered.add(147)
    # 变异规则 226 - CAR
    if (altitude % speed < 20) != (altitude % speed < 18):
        triggered.add(148)
    # 变异规则 227 - SAR
    if (altitude % speed < 20) != (altitude % 20 > speed):
        triggered.add(149)
    # 变异规则 228 - CSR
    if (altitude % speed < 20) != (altitude % speed < -20):
        triggered.add(150)
    # 变异规则 229 - AOR
    if (altitude % speed < 20) != (altitude % 20 > speed):
        triggered.add(151)
    # 变异规则 230 - SVR
    if (altitude % speed < 20) != (voltage_mv % speed < 20):
        triggered.add(152)
    # 原语句
    if altitude % speed < 20:
        health_score += 18
    # 原语句24
    # 变异规则 231 - RSR
    if (voltage_mv >= 10 or altitude != 1000) != (not (voltage_mv >= 10 or altitude != 1000)):
        triggered.add(153)
    # 变异规则 232 - SRC
    if (voltage_mv >= 10 or altitude != 1000) != (altitude != 1000 or voltage_mv >= 10):
        t = 1
    # 变异规则 233 - SCR
    if (voltage_mv >= 10 or altitude != 1000) != (voltage_mv >= 10 or -altitude != 1000):
        t = 1
    # 变异规则 234 - SVR
    if (voltage_mv >= 10 or altitude != 1000) != (altitude >= 10 or altitude != 1000):
        t = 1
    # 变异规则 235 - ROR
    if (voltage_mv >= 10 or altitude != 1000) != (altitude >= 10 or altitude != 1000):
        t = 1
    # 变异规则 236 - AOR
    if (voltage_mv >= 10 or altitude != 1000) != (voltage_mv >= 1 or altitude != 1000):
        t = 1
    # 变异规则 237 - LCR
    if (voltage_mv >= 10 or altitude != 1000) != (voltage_mv >= 10 and altitude != 1000):
        triggered.add(154)
    # 变异规则 238 - SAR
    if (voltage_mv >= 10 or altitude != 1000) != (10 <= voltage_mv or altitude != 1000):
        t = 1
    # 变异规则 239 - UOI
    if (voltage_mv >= 10 or altitude != 1000) != (voltage_mv >= 10 or -altitude != 1000):
        t = 1
    # 变异规则 240 - CRP
    if (voltage_mv >= 10 or altitude != 1000) != (voltage_mv >= 5 or altitude != 1000):
        t = 1
    # 原语句
    if voltage_mv >= 10 or altitude != 1000:
        health_score -= 28
        speed = min(speed + 8, 100)
    # 原语句25
    # 变异规则 241 - SRC
    if (speed % 99 > altitude) != (not (speed % 99 > altitude)):
        triggered.add(155)
    # 变异规则 242 - ROR
    if (speed % 99 > altitude) != (not (speed % 99 > altitude)):
        triggered.add(156)
    # 变异规则 243 - SAR
    if (speed % 99 > altitude) != (speed % altitude < 99):
        triggered.add(157)
    # 变异规则 244 - CSR
    if (speed % 99 > altitude) != (speed % -99 > altitude):
        triggered.add(158)
    # 变异规则 245 - CAR
    if (speed % 99 > altitude) != (speed % 109 > altitude):
        triggered.add(159)
    # 变异规则 246 - AOR
    if (speed % 99 > altitude) != (speed % altitude < 99):
        triggered.add(160)
    # 变异规则 247 - LCR
    if (speed % 99 > altitude) != (not (speed % 99 > altitude)):
        triggered.add(161)
    # 变异规则 248 - UOI
    if (speed % 99 > altitude) != (speed % 99 > -altitude):
        triggered.add(162)
    # 变异规则 249 - SCR
    if (speed % 99 > altitude) != (speed % 89 > altitude):
        triggered.add(163)
    # 变异规则 250 - SVR
    if (speed % 99 > altitude) != (altitude % 99 > altitude):
        triggered.add(164)
    # 原语句
    if speed % 99 > altitude:
        health_score += 12
        speed = max(speed - 2, 2)
    # 原语句26
    # 变异规则 251 - SAR
    if (speed < 79 and voltage_mv == 50) != (79 > speed and voltage_mv == 50):
        t = 1
    # 变异规则 252 - CAR
    if (speed < 79 and voltage_mv == 50) != (speed < 79 and voltage_mv == 55):
        triggered.add(165)
    # 变异规则 253 - SCR
    if (speed < 79 and voltage_mv == 50) != (not (speed < 79 and voltage_mv == 50)):
        triggered.add(166)
    # 变异规则 254 - LCR
    if (speed < 79 and voltage_mv == 50) != (speed < 79 or voltage_mv == 50):
        triggered.add(167)
    # 变异规则 255 - SRC
    if (speed < 79 and voltage_mv == 50) != (voltage_mv == 50 and speed < 79):
        t = 1
    # 变异规则 256 - CRP
    if (speed < 79 and voltage_mv == 50) != (speed < 158 and voltage_mv == 50):
        triggered.add(168)
    # 变异规则 257 - CSR
    if (speed < 79 and voltage_mv == 50) != (speed < -79 and voltage_mv == 50):
        triggered.add(169)
    # 变异规则 258 - UOI
    if (speed < 79 and voltage_mv == 50) != (speed < 79 and -voltage_mv == 50):
        triggered.add(170)
    # 变异规则 259 - ABS
    if (speed < 79 and voltage_mv == 50) != (abs(speed) < 79 and voltage_mv == 50):
        t = 1
    # 变异规则 260 - ROR
    if (speed < 79 and voltage_mv == 50) != (speed < 79 and voltage_mv == -50):
        triggered.add(171)
    # 原语句
    if speed < 79 and voltage_mv == 50:
        health_score -= 15
        speed, altitude = altitude, speed
    # 原语句27
    # 变异规则 261 - ROR
    if (voltage_mv <= speed - 94) != (voltage_mv <= speed - 47):
        triggered.add(172)
    # 变异规则 262 - CRP
    if (voltage_mv <= speed - 94) != (voltage_mv <= speed - 188):
        t = 1
    # 变异规则 263 - CSR
    if (voltage_mv <= speed - 94) != (voltage_mv <= speed - -94):
        triggered.add(173)
    # 变异规则 264 - LCR
    if (voltage_mv <= speed - 94) != (voltage_mv <= speed - 92):
        t = 1
    # 变异规则 265 - ABS
    if (voltage_mv <= speed - 94) != (voltage_mv <= abs(speed) - 94):
        t = 1
    # 变异规则 266 - SAR
    if (voltage_mv <= speed - 94) != (speed >= voltage_mv - 94):
        triggered.add(174)
    # 变异规则 267 - SVR
    if (voltage_mv <= speed - 94) != (altitude <= speed - 94):
        triggered.add(175)
    # 变异规则 268 - SRC
    if (voltage_mv <= speed - 94) != (voltage_mv <= abs(speed) - 94):
        t = 1
    # 变异规则 269 - SCR
    if (voltage_mv <= speed - 94) != (voltage_mv <= speed - -94):
        triggered.add(176)
    # 变异规则 270 - AOR
    if (voltage_mv <= speed - 94) != (altitude <= speed - 94):
        triggered.add(177)
    # 原语句
    if voltage_mv <= speed - 94:
        health_score += 18
        speed = min(speed + 6, 100)
        voltage_mv = min(voltage_mv + 5, 100)
        speed, voltage_mv = voltage_mv, speed
    # 原语句28
    # 变异规则 271 - CSR
    if (15 <= speed <= 62) != (15 <= speed <= -62):
        triggered.add(178)
    # 变异规则 272 - SCR
    if (15 <= speed <= 62) != (not (15) <= speed <= 62):
        triggered.add(179)
    # 变异规则 273 - CAR
    if (15 <= speed <= 62) != (10 <= speed <= 62):
        triggered.add(180)
    # 变异规则 274 - UOI
    if (15 <= speed <= 62) != (15 <= -speed <= 62):
        triggered.add(181)
    # 变异规则 275 - ROR
    if (15 <= speed <= 62) != (not (15) <= speed <= 62):
        triggered.add(182)
    # 变异规则 276 - SAR
    if (15 <= speed <= 62) != (speed >= 15 <= 62):
        triggered.add(183)
    # 变异规则 277 - SRC
    if (15 <= speed <= 62) != (not (15 <= speed <= 62)):
        triggered.add(184)
    # 变异规则 278 - LCR
    if (15 <= speed <= 62) != (not (15 <= speed <= 62)):
        triggered.add(185)
    # 变异规则 279 - RSR
    if (15 <= speed <= 62) != (not (15 <= speed <= 62)):
        triggered.add(186)
    # 变异规则 280 - CRP
    if (15 <= speed <= 62) != (30 <= speed <= 62):
        triggered.add(187)
    # 原语句
    if 15 <= speed <= 62:
        health_score -= 24
        altitude = min(altitude + 29, 1000)
    # 原语句29
    # 变异规则 281 - CAR
    if (voltage_mv != 20) != (voltage_mv != 21):
        triggered.add(188)
    # 变异规则 282 - AOR
    if (voltage_mv != 20) != (not (voltage_mv != 20)):
        triggered.add(189)
    # 变异规则 283 - ROR
    if (voltage_mv != 20) != (20 != voltage_mv):
        t = 1
    # 变异规则 284 - RSR
    if (voltage_mv != 20) != (not (voltage_mv != 20)):
        triggered.add(190)
    # 变异规则 285 - SCR
    if (voltage_mv != 20) != (abs(voltage_mv) != 20):
        t = 1
    # 变异规则 286 - ABS
    if (voltage_mv != 20) != (abs(voltage_mv) != 20):
        t = 1
    # 变异规则 287 - CSR
    if (voltage_mv != 20) != (voltage_mv != -20):
        triggered.add(191)
    # 变异规则 288 - SAR
    if (voltage_mv != 20) != (20 != voltage_mv):
        t = 1
    # 变异规则 289 - CRP
    if (voltage_mv != 20) != (voltage_mv != 12):
        triggered.add(192)
    # 变异规则 290 - SRC
    if (voltage_mv != 20) != (abs(voltage_mv) != 20):
        t = 1
    # 原语句
    if voltage_mv != 20:
        health_score += 3
    # 原语句30
    # 变异规则 291 - ABS
    if (altitude == speed * 10) != (abs(altitude) == speed * 10):
        t = 1
    # 变异规则 292 - CAR
    if (altitude == speed * 10) != (altitude == speed * 8):
        triggered.add(193)
    # 变异规则 293 - CRP
    if (altitude == speed * 10) != (altitude == speed * 20):
        triggered.add(194)
    # 变异规则 294 - CSR
    if (altitude == speed * 10) != (altitude == speed * -10):
        triggered.add(195)
    # 变异规则 295 - UOI
    if (altitude == speed * 10) != (altitude == -speed * 10):
        triggered.add(196)
    # 变异规则 296 - ROR
    if (altitude == speed * 10) != (altitude == -speed * 10):
        triggered.add(197)
    # 变异规则 297 - SAR
    if (altitude == speed * 10) != (speed == altitude * 10):
        triggered.add(198)
    # 变异规则 298 - RSR
    if (altitude == speed * 10) != (not (altitude == speed * 10)):
        triggered.add(199)
    # 变异规则 299 - SRC
    if (altitude == speed * 10) != (abs(altitude) == speed * 10):
        t = 1
    # 变异规则 300 - SCR
    if (altitude == speed * 10) != (speed == altitude * 10):
        triggered.add(200)
    # 原语句
    if altitude == speed * 10:
        health_score -= 21
    return triggered

targetPaths = [
    {4, 10, 19, 27, 32, 33, 43, 48, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 199},
    {4, 5, 10, 19, 27, 32, 33, 43, 48, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 199},
    {1, 2, 3, 4, 5, 6, 7, 10, 19, 27, 32, 33, 43, 48, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 199},
    {1, 4, 10, 19, 27, 32, 33, 43, 48, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 199},
    {4, 10, 19, 27, 32, 33, 43, 48, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 7, 10, 14, 19, 27, 32, 33, 43, 48, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 10, 14, 19, 27, 32, 33, 43, 48, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 10, 14, 19, 27, 28, 32, 33, 43, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 10, 12, 14, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 52, 53, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 9, 10, 11, 13, 16, 19, 27, 28, 32, 33, 43, 48, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 9, 10, 11, 13, 16, 19, 27, 28, 32, 33, 43, 48, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 9, 10, 11, 16, 19, 27, 28, 32, 33, 43, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 145, 146, 148, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 9, 10, 11, 19, 27, 28, 32, 33, 43, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 91, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 145, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 11, 19, 27, 28, 32, 33, 43, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 91, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 142, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 54, 55, 57, 58, 64, 67, 69, 74, 76, 78, 79, 82, 85, 86, 89, 91, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 142, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 52, 53, 55, 57, 58, 64, 67, 68, 69, 74, 76, 78, 79, 82, 85, 86, 89, 91, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 142, 143, 152, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 52, 53, 55, 57, 58, 64, 67, 68, 69, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 142, 143, 152, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 52, 53, 55, 57, 58, 64, 67, 68, 69, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 103, 106, 109, 112, 116, 123, 124, 127, 134, 137, 138, 142, 143, 144, 145, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 52, 53, 55, 57, 58, 64, 67, 68, 69, 72, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 103, 106, 111, 116, 123, 124, 127, 134, 137, 138, 142, 143, 144, 145, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 53, 55, 57, 58, 64, 67, 70, 71, 73, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 93, 95, 103, 106, 111, 116, 123, 127, 134, 137, 138, 142, 143, 144, 146, 153, 154, 155, 158, 164, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 53, 55, 57, 58, 64, 67, 70, 71, 73, 74, 76, 78, 79, 82, 89, 90, 92, 93, 95, 103, 106, 111, 116, 123, 127, 134, 137, 138, 142, 143, 144, 146, 153, 154, 155, 158, 164, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 49, 50, 51, 53, 55, 57, 58, 64, 67, 70, 74, 76, 78, 79, 82, 89, 90, 93, 95, 96, 103, 106, 111, 116, 123, 127, 134, 137, 138, 142, 143, 144, 146, 153, 154, 155, 158, 164, 166, 167, 172, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 29, 32, 33, 43, 48, 49, 50, 51, 53, 55, 57, 58, 64, 67, 70, 74, 76, 78, 79, 82, 89, 90, 93, 95, 96, 103, 106, 111, 116, 123, 127, 134, 137, 138, 142, 143, 144, 146, 153, 154, 155, 158, 164, 166, 167, 172, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 28, 29, 32, 33, 43, 48, 49, 50, 51, 53, 55, 57, 58, 64, 67, 70, 74, 76, 78, 79, 82, 89, 90, 93, 95, 96, 103, 106, 111, 116, 123, 125, 127, 134, 137, 138, 142, 143, 144, 146, 153, 154, 155, 158, 164, 166, 167, 172, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 19, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 70, 74, 76, 78, 79, 82, 85, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 128, 133, 137, 138, 140, 142, 143, 146, 153, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 199},
    {4, 9, 10, 19, 27, 32, 33, 43, 48, 55, 57, 58, 60, 62, 64, 67, 69, 70, 74, 76, 78, 79, 82, 85, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 128, 133, 137, 138, 140, 142, 143, 146, 153, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 199},
    {4, 10, 15, 19, 27, 32, 33, 43, 48, 55, 57, 58, 60, 62, 64, 67, 69, 70, 74, 76, 78, 79, 82, 85, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 128, 133, 137, 138, 140, 142, 143, 146, 153, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 199},
    {4, 9, 10, 19, 27, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 70, 74, 76, 78, 79, 82, 85, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 128, 133, 137, 138, 140, 142, 143, 144, 146, 153, 155, 157, 162, 166, 167, 173, 174, 179, 180, 184, 189, 193, 194, 195, 196, 198, 199},
    {4, 9, 10, 19, 27, 28, 32, 33, 43, 48, 55, 57, 58, 60, 61, 64, 67, 70, 73, 74, 76, 78, 79, 82, 89, 90, 92, 93, 95, 103, 106, 111, 116, 123, 127, 134, 137, 138, 142, 143, 144, 145, 146, 153, 154, 155, 158, 164, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 11, 13, 16, 19, 23, 27, 28, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 105, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 9, 10, 11, 13, 16, 20, 22, 24, 26, 27, 28, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 74, 76, 78, 79, 82, 86, 89, 95, 103, 106, 109, 116, 123, 124, 127, 134, 137, 138, 143, 144, 145, 146, 153, 154, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 9, 10, 20, 22, 24, 26, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 71, 73, 74, 76, 78, 79, 82, 85, 86, 89, 95, 103, 106, 111, 116, 123, 124, 127, 128, 133, 137, 138, 139, 143, 144, 145, 146, 148, 152, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 61, 64, 67, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 96, 100, 103, 106, 111, 116, 123, 124, 127, 128, 133, 137, 138, 139, 143, 144, 146, 152, 153, 155, 158, 164, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 61, 64, 67, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 96, 98, 99, 100, 102, 103, 106, 116, 123, 124, 126, 131, 133, 137, 138, 143, 144, 146, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 61, 64, 67, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 96, 98, 99, 100, 102, 103, 106, 116, 123, 124, 126, 131, 133, 137, 138, 143, 144, 146, 153, 155, 157, 162, 165, 166, 169, 170, 171, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 27, 32, 33, 43, 48, 55, 57, 58, 60, 61, 64, 67, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 96, 98, 99, 100, 102, 103, 106, 116, 123, 124, 136, 137, 138, 140, 142, 143, 144, 146, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 27, 32, 33, 43, 48, 55, 57, 58, 60, 61, 64, 67, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 96, 98, 99, 100, 102, 103, 106, 115, 116, 123, 124, 136, 137, 138, 140, 142, 143, 144, 146, 152, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 61, 63, 64, 67, 74, 76, 78, 79, 82, 85, 86, 87, 89, 91, 95, 96, 98, 103, 106, 111, 116, 123, 124, 125, 127, 128, 133, 137, 138, 139, 143, 153, 155, 158, 164, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 27, 32, 33, 43, 48, 55, 57, 58, 60, 61, 63, 64, 67, 74, 76, 78, 79, 82, 89, 90, 92, 95, 96, 103, 106, 111, 116, 123, 124, 125, 127, 128, 133, 137, 138, 139, 140, 143, 144, 146, 152, 153, 155, 157, 162, 166, 167, 173, 174, 179, 183, 184, 189, 199},
    {4, 9, 10, 20, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 61, 63, 64, 67, 74, 76, 78, 79, 82, 89, 90, 92, 95, 96, 103, 106, 111, 114, 116, 123, 124, 125, 127, 128, 133, 137, 138, 139, 142, 143, 153, 155, 158, 164, 166, 167, 173, 174, 179, 183, 184, 189, 199},
    {4, 9, 10, 20, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 61, 63, 64, 67, 74, 76, 78, 79, 82, 89, 90, 92, 95, 96, 103, 106, 111, 114, 115, 116, 117, 120, 123, 125, 136, 137, 138, 140, 142, 143, 152, 153, 155, 158, 164, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 27, 32, 33, 43, 48, 55, 57, 58, 60, 61, 62, 63, 64, 67, 74, 76, 78, 79, 82, 89, 90, 92, 95, 96, 103, 106, 111, 114, 115, 116, 117, 120, 123, 125, 136, 137, 138, 140, 143, 153, 155, 158, 163, 164, 166, 173, 174, 179, 183, 184, 189, 199},
    {4, 9, 10, 20, 27, 32, 33, 43, 48, 55, 57, 58, 60, 61, 62, 63, 64, 67, 74, 76, 78, 79, 82, 89, 90, 92, 95, 96, 103, 106, 111, 114, 115, 116, 117, 120, 123, 125, 136, 137, 138, 140, 143, 153, 155, 157, 159, 162, 166, 173, 174, 179, 183, 184, 189, 199},
    {4, 9, 10, 20, 27, 30, 32, 33, 43, 48, 55, 57, 58, 59, 62, 63, 64, 67, 74, 76, 78, 79, 82, 89, 90, 92, 95, 96, 103, 106, 111, 116, 123, 124, 125, 127, 128, 133, 137, 138, 139, 142, 143, 153, 155, 158, 164, 166, 167, 172, 173, 174, 179, 183, 184, 189, 199},
    {4, 9, 10, 11, 13, 16, 20, 22, 24, 26, 27, 28, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 74, 76, 78, 79, 82, 85, 86, 89, 95, 103, 106, 109, 116, 123, 124, 127, 134, 135, 137, 138, 143, 144, 145, 146, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 192, 199},
    {4, 9, 10, 20, 22, 24, 26, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 71, 73, 74, 76, 78, 79, 82, 85, 86, 89, 95, 97, 103, 106, 116, 123, 124, 127, 128, 133, 137, 138, 143, 144, 145, 146, 148, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 11, 13, 16, 20, 22, 24, 26, 27, 28, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 74, 76, 78, 79, 82, 85, 86, 89, 95, 103, 106, 109, 116, 123, 124, 127, 134, 135, 137, 138, 143, 144, 145, 146, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 188, 189, 191, 192, 199},
    {4, 9, 10, 20, 22, 24, 26, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 71, 73, 74, 76, 78, 79, 82, 85, 86, 89, 94, 96, 103, 106, 116, 123, 124, 127, 128, 133, 137, 138, 143, 144, 145, 146, 148, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 20, 22, 24, 26, 27, 32, 33, 43, 48, 55, 57, 58, 60, 62, 64, 67, 71, 73, 74, 76, 78, 79, 82, 85, 86, 89, 94, 96, 103, 106, 116, 123, 125, 126, 131, 133, 137, 138, 142, 143, 153, 155, 158, 164, 166, 167, 168, 173, 174, 179, 183, 184, 189, 199},
    {4, 9, 10, 11, 13, 16, 22, 24, 26, 27, 28, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 74, 76, 78, 79, 82, 85, 86, 89, 94, 96, 103, 106, 109, 110, 111, 116, 123, 124, 127, 128, 133, 137, 138, 140, 142, 143, 144, 145, 146, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 9, 10, 11, 13, 16, 22, 24, 26, 27, 28, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 74, 76, 78, 79, 82, 85, 86, 89, 94, 96, 103, 106, 113, 116, 123, 124, 127, 128, 133, 137, 138, 140, 142, 143, 144, 145, 146, 153, 155, 157, 162, 166, 167, 173, 174, 178, 179, 181, 184, 187, 189, 199},
    {4, 10, 22, 24, 26, 27, 32, 33, 43, 48, 55, 57, 58, 60, 64, 67, 69, 74, 76, 78, 79, 82, 85, 89, 94, 96, 105, 106, 113, 116, 123, 125, 126, 131, 133, 137, 138, 140, 142, 143, 144, 146, 152, 153, 155, 157, 159, 162, 163, 166, 172, 173, 174, 175, 179, 183, 184, 189, 199},
    {4, 9, 10, 22, 24, 26, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 64, 65, 67, 71, 73, 74, 76, 78, 79, 82, 85, 89, 94, 96, 103, 106, 116, 123, 125, 136, 137, 138, 140, 142, 143, 152, 153, 155, 158, 164, 166, 167, 173, 174, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 22, 24, 26, 27, 30, 32, 33, 43, 48, 55, 57, 58, 60, 64, 65, 67, 71, 73, 74, 76, 78, 79, 81, 82, 85, 89, 94, 96, 103, 106, 116, 123, 125, 136, 137, 138, 140, 142, 143, 152, 153, 155, 158, 164, 166, 167, 178, 179, 181, 184, 189, 199},
    {4, 10, 19, 20, 27, 32, 33, 39, 40, 41, 42, 43, 47, 48, 53, 55, 57, 58, 64, 65, 67, 69, 74, 76, 78, 79, 82, 85, 89, 94, 96, 105, 106, 113, 116, 123, 125, 136, 137, 138, 143, 144, 146, 153, 155, 158, 164, 166, 173, 174, 179, 183, 184, 189, 199},
    {4, 9, 10, 22, 24, 26, 27, 30, 33, 34, 35, 36, 38, 43, 48, 53, 55, 57, 58, 60, 64, 65, 67, 71, 73, 74, 76, 78, 79, 81, 82, 85, 89, 94, 96, 103, 106, 116, 123, 125, 136, 137, 138, 140, 142, 143, 152, 153, 155, 158, 164, 166, 167, 178, 179, 181, 184, 189, 199},
    {4, 9, 10, 22, 24, 26, 27, 30, 33, 35, 43, 48, 53, 55, 57, 58, 60, 64, 65, 67, 71, 73, 74, 76, 77, 78, 79, 81, 82, 85, 89, 94, 96, 103, 106, 116, 123, 125, 136, 137, 138, 140, 142, 143, 153, 155, 158, 164, 166, 167, 178, 179, 181, 184, 189, 199},
    {4, 10, 22, 24, 26, 27, 33, 35, 43, 48, 53, 55, 56, 57, 58, 60, 64, 65, 67, 69, 74, 76, 78, 79, 82, 85, 89, 94, 96, 105, 106, 113, 116, 123, 125, 136, 137, 138, 143, 144, 146, 152, 153, 155, 157, 159, 162, 163, 166, 173, 174, 175, 179, 183, 184, 189, 199}
]

def build_complete_rule_expressions() -> dict:
    """构建完整的规则表达式映射（筛选后版本）"""
    rule_expressions = {}

    # 原始规则编号到新编号的映射
    # 原始编号 -> 新编号: {1:1, 3:2, 4:3, 5:4, 6:5, 7:6, 9:7, 10:8, 11:9, 12:10, 13:11, 14:12, 15:13, 16:14, 17:15, 18:16, 19:17, 20:18, 21:19, 22:20, 23:21, 24:22, 27:23, 28:24, 29:25, 30:26, 31:27, 32:28, 36:29, 37:30, 40:31, 41:32, 43:33, 45:34, 46:35, 47:36, 48:37, 49:38, 51:39, 52:40, 53:41, 54:42, 56:43, 57:44, 58:45, 59:46, 60:47, 61:48, 62:49, 63:50, 64:51, 65:52, 66:53, 67:54, 70:55, 75:56, 80:57, 81:58, 83:59, 85:60, 89:61, 90:62, 93:63, 95:64, 96:65, 97:66, 99:67, 101:68, 102:69, 103:70, 104:71, 105:72, 107:73, 108:74, 110:75, 111:76, 116:77, 117:78, 121:79, 127:80, 134:81, 136:82, 137:83, 140:84, 142:85, 143:86, 144:87, 145:88, 146:89, 147:90, 149:91, 150:92, 155:93, 156:94, 157:95, 158:96, 160:97, 161:98, 162:99, 163:100, 165:101, 170:102, 171:103, 173:104, 175:105, 178:106, 179:107, 180:108, 182:109, 183:110, 187:111, 188:112, 190:113, 191:114, 192:115, 194:116, 195:117, 196:118, 197:119, 198:120, 199:121, 200:122, 201:123, 202:124, 203:125, 204:126, 205:127, 206:128, 207:129, 208:130, 209:131, 210:132, 211:133, 212:134, 213:135, 214:136, 215:137, 216:138, 217:139, 218:140, 219:141, 220:142, 221:143, 222:144, 223:145, 224:146, 225:147, 226:148, 227:149, 228:150, 229:151, 230:152, 231:153, 237:154, 241:155, 242:156, 243:157, 244:158, 245:159, 246:160, 247:161, 248:162, 249:163, 250:164, 252:165, 253:166, 254:167, 256:168, 257:169, 258:170, 260:171, 261:172, 263:173, 266:174, 267:175, 269:176, 270:177, 271:178, 272:179, 273:180, 274:181, 275:182, 276:183, 277:184, 278:185, 279:186, 280:187, 281:188, 282:189, 284:190, 287:191, 289:192, 292:193, 293:194, 294:195, 295:196, 296:197, 297:198, 298:199, 300:200}

    rule_expressions[1] = "(voltage_mv == 5) != (voltage_mv == 6)"
    rule_expressions[2] = "(voltage_mv == 5) != (voltage_mv == 10)"
    rule_expressions[3] = "(voltage_mv == 5) != (altitude == 5)"
    rule_expressions[4] = "(voltage_mv == 5) != (not (voltage_mv == 5))"
    rule_expressions[5] = "(voltage_mv == 5) != (voltage_mv == 3)"
    rule_expressions[6] = "(voltage_mv == 5) != (voltage_mv == -5)"
    rule_expressions[7] = "(voltage_mv == 5) != (voltage_mv == 9)"
    rule_expressions[8] = "(voltage_mv == 5) != (voltage_mv == 10)"
    rule_expressions[9] = "(18 <= voltage_mv <= 98) != (18 <= -voltage_mv <= 98)"
    rule_expressions[10] = "(18 <= voltage_mv <= 98) != (not (18 <= voltage_mv <= 98))"
    rule_expressions[11] = "(18 <= voltage_mv <= 98) != (26 <= voltage_mv <= 98)"
    rule_expressions[12] = "(18 <= voltage_mv <= 98) != (17 <= voltage_mv <= 98)"
    rule_expressions[13] = "(18 <= voltage_mv <= 98) != (20 <= voltage_mv <= 98)"
    rule_expressions[14] = "(18 <= voltage_mv <= 98) != (9 <= voltage_mv <= 98)"
    rule_expressions[15] = "(18 <= voltage_mv <= 98) != (voltage_mv >= 18 <= 98)"
    rule_expressions[16] = "(18 <= voltage_mv <= 98) != (23 <= voltage_mv <= 98)"
    rule_expressions[17] = "(18 <= voltage_mv <= 98) != (18 <= -voltage_mv <= 98)"
    rule_expressions[18] = "(18 <= voltage_mv <= 98) != (not (18 <= voltage_mv <= 98))"
    rule_expressions[19] = "(speed < 30) != (speed < -30)"
    rule_expressions[20] = "(speed < 30) != (altitude < 30)"
    rule_expressions[21] = "(speed < 30) != (speed < -30)"
    rule_expressions[22] = "(speed < 30) != (speed < 60)"
    rule_expressions[23] = "(speed < 30) != (speed < 27)"
    rule_expressions[24] = "(speed < 30) != (speed < 32)"
    rule_expressions[25] = "(speed < 30) != (speed < -30)"
    rule_expressions[26] = "(speed < 30) != (speed < 38)"
    rule_expressions[27] = "(voltage_mv >= 10 and voltage_mv >= 50) != (not (voltage_mv >= 10 and voltage_mv >= 50))"
    rule_expressions[28] = "(voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 or voltage_mv >= 50)"
    rule_expressions[29] = "(voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 and voltage_mv >= 48)"
    rule_expressions[30] = "(voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 and voltage_mv >= 54)"
    rule_expressions[31] = "(voltage_mv >= 10 and voltage_mv >= 50) != (voltage_mv >= 10 or voltage_mv >= 50)"
    rule_expressions[32] = "(altitude > 500) != (altitude > -500)"
    rule_expressions[33] = "(altitude > 500) != (not (altitude > 500))"
    rule_expressions[34] = "(altitude > 500) != (altitude > 505)"
    rule_expressions[35] = "(altitude > 500) != (speed > 500)"
    rule_expressions[36] = "(altitude > 500) != (altitude > 510)"
    rule_expressions[37] = "(altitude > 500) != (speed > 500)"
    rule_expressions[38] = "(altitude > 500) != (altitude > 502)"
    rule_expressions[39] = "(altitude == speed * 200) != (altitude == -speed * 200)"
    rule_expressions[40] = "(altitude == speed * 200) != (altitude == speed * 202)"
    rule_expressions[41] = "(altitude == speed * 200) != (speed == speed * 200)"
    rule_expressions[42] = "(altitude == speed * 200) != (altitude == speed * -200)"
    rule_expressions[43] = "(altitude == speed * 200) != (not (altitude == speed * 200))"
    rule_expressions[44] = "(altitude == speed * 200) != (altitude == -speed * 200)"
    rule_expressions[45] = "(altitude == speed * 200) != (altitude == -speed * 200)"
    rule_expressions[46] = "(altitude == speed * 200) != (not (altitude == speed * 200))"
    rule_expressions[47] = "(altitude == speed * 200) != (speed == altitude * 200)"
    rule_expressions[48] = "(voltage_mv // 5 <= speed) != (voltage_mv // speed >= 5)"
    rule_expressions[49] = "(voltage_mv // 5 <= speed) != (voltage_mv // 10 <= speed)"
    rule_expressions[50] = "(voltage_mv // 5 <= speed) != (voltage_mv // -5 <= speed)"
    rule_expressions[51] = "(voltage_mv // 5 <= speed) != (speed // 5 <= speed)"
    rule_expressions[52] = "(voltage_mv // 5 <= speed) != (voltage_mv // 6 <= speed)"
    rule_expressions[53] = "(voltage_mv // 5 <= speed) != (altitude // 5 <= speed)"
    rule_expressions[54] = "(voltage_mv // 5 <= speed) != (voltage_mv // 3 <= speed)"
    rule_expressions[55] = "(voltage_mv // 5 <= speed) != (not (voltage_mv // 5 <= speed))"
    rule_expressions[56] = "(altitude == voltage_mv // 497) != (voltage_mv == altitude // 497)"
    rule_expressions[57] = "(altitude == voltage_mv // 497) != (not (altitude == voltage_mv // 497))"
    rule_expressions[58] = "(voltage_mv >= 71 and speed > 13) != (not (voltage_mv >= 71 and speed > 13))"
    rule_expressions[59] = "(voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 and -speed > 13)"
    rule_expressions[60] = "(voltage_mv >= 71 and speed > 13) != (voltage_mv >= 71 or speed > 13)"
    rule_expressions[61] = "(voltage_mv >= 71 and speed > 13) != (voltage_mv >= 35 and speed > 13)"
    rule_expressions[62] = "(voltage_mv >= 71 and speed > 13) != (speed >= 71 and speed > 13)"
    rule_expressions[63] = "(voltage_mv <= 100) != (voltage_mv <= 50)"
    rule_expressions[64] = "(voltage_mv <= 100) != (not (voltage_mv <= 100))"
    rule_expressions[65] = "(voltage_mv <= 100) != (altitude <= 100)"
    rule_expressions[66] = "(voltage_mv <= 100) != (not (voltage_mv <= 100))"
    rule_expressions[67] = "(voltage_mv <= 100) != (voltage_mv <= -100)"
    rule_expressions[68] = "(voltage_mv < 30) != (voltage_mv < 25)"
    rule_expressions[69] = "(voltage_mv < 30) != (voltage_mv < -30)"
    rule_expressions[70] = "(voltage_mv < 30) != (altitude < 30)"
    rule_expressions[71] = "(voltage_mv < 30) != (voltage_mv < 35)"
    rule_expressions[72] = "(voltage_mv < 30) != (voltage_mv < 29)"
    rule_expressions[73] = "(voltage_mv < 30) != (voltage_mv < 38)"
    rule_expressions[74] = "(voltage_mv < 30) != (not (voltage_mv < 30))"
    rule_expressions[75] = "(voltage_mv < 30) != (not (voltage_mv < 30))"
    rule_expressions[76] = "(altitude >= 728) != (altitude >= -728)"
    rule_expressions[77] = "(altitude >= 728) != (speed >= 728)"
    rule_expressions[78] = "(altitude >= 728) != (not (altitude >= 728))"
    rule_expressions[79] = "(altitude <= speed // 455) != (not (altitude <= speed // 455))"
    rule_expressions[80] = "(altitude <= speed // 455) != (not (altitude <= speed // 455))"
    rule_expressions[81] = "(201 <= altitude <= 803) != (201 <= speed <= 803)"
    rule_expressions[82] = "(201 <= altitude <= 803) != (not (201 <= altitude <= 803))"
    rule_expressions[83] = "(201 <= altitude <= 803) != (not (201 <= altitude <= 803))"
    rule_expressions[84] = "(201 <= altitude <= 803) != (201 <= speed <= 803)"
    rule_expressions[85] = "(speed + 30 >= voltage_mv) != (speed + voltage_mv <= 30)"
    rule_expressions[86] = "(speed + 30 >= voltage_mv) != (speed + -30 >= voltage_mv)"
    rule_expressions[87] = "(speed + 30 >= voltage_mv) != (speed + 20 >= voltage_mv)"
    rule_expressions[88] = "(speed + 30 >= voltage_mv) != (speed + -30 >= voltage_mv)"
    rule_expressions[89] = "(speed + 30 >= voltage_mv) != (not (speed + 30 >= voltage_mv))"
    rule_expressions[90] = "(speed + 30 >= voltage_mv) != (speed + 30 >= -voltage_mv)"
    rule_expressions[91] = "(speed + 30 >= voltage_mv) != (speed + 15 >= voltage_mv)"
    rule_expressions[92] = "(speed + 30 >= voltage_mv) != (altitude + 30 >= voltage_mv)"
    rule_expressions[93] = "(2 <= speed <= 42) != (4 <= speed <= 42)"
    rule_expressions[94] = "(2 <= speed <= 42) != (speed >= 2 <= 42)"
    rule_expressions[95] = "(2 <= speed <= 42) != (2 <= -speed <= 42)"
    rule_expressions[96] = "(2 <= speed <= 42) != (2 <= voltage_mv <= 42)"
    rule_expressions[97] = "(2 <= speed <= 42) != (2 <= speed <= 36)"
    rule_expressions[98] = "(speed >= 10 and voltage_mv == 50) != (speed >= 10 and voltage_mv == 51)"
    rule_expressions[99] = "(speed >= 10 and voltage_mv == 50) != (speed >= 10 and -voltage_mv == 50)"
    rule_expressions[100] = "(speed >= 10 and voltage_mv == 50) != (speed >= 10 and voltage_mv == 45)"
    rule_expressions[101] = "(speed >= 10 and voltage_mv == 50) != (speed >= 10 and -voltage_mv == 50)"
    rule_expressions[102] = "(speed >= 10 and voltage_mv == 50) != (speed >= 10 and voltage_mv == -50)"
    rule_expressions[103] = "(altitude < 670 and voltage_mv <= 17) != (altitude < 670 or voltage_mv <= 17)"
    rule_expressions[104] = "(altitude < 670 and voltage_mv <= 17) != (altitude < 670 or voltage_mv <= 17)"
    rule_expressions[105] = "(altitude < 670 and voltage_mv <= 17) != (altitude < -670 and voltage_mv <= 17)"
    rule_expressions[106] = "(altitude < 670 and voltage_mv <= 17) != (not (altitude < 670 and voltage_mv <= 17))"
    rule_expressions[107] = "(altitude < 670 and voltage_mv <= 17) != (not (altitude < 670 and voltage_mv <= 17))"
    rule_expressions[108] = "(altitude < 670 and voltage_mv <= 17) != (altitude < 670 or voltage_mv <= 17)"
    rule_expressions[109] = "(voltage_mv < 30 and speed < 44) != (voltage_mv < 30 and speed < -44)"
    rule_expressions[110] = "(voltage_mv < 30 and speed < 44) != (voltage_mv < 30 and speed < 43)"
    rule_expressions[111] = "(voltage_mv < 30 and speed < 44) != (speed < 30 and speed < 44)"
    rule_expressions[112] = "(voltage_mv < 30 and speed < 44) != (voltage_mv < 29 and speed < 44)"
    rule_expressions[113] = "(voltage_mv < 30 and speed < 44) != (voltage_mv < 30 and -speed < 44)"
    rule_expressions[114] = "(voltage_mv != 68) != (voltage_mv != 63)"
    rule_expressions[115] = "(voltage_mv != 68) != (speed != 68)"
    rule_expressions[116] = "(voltage_mv != 68) != (not (voltage_mv != 68))"
    rule_expressions[117] = "(voltage_mv != 68) != (voltage_mv != -68)"
    rule_expressions[118] = "(voltage_mv != 68) != (speed != 68)"
    rule_expressions[119] = "(voltage_mv != 68) != (voltage_mv != -68)"
    rule_expressions[120] = "(voltage_mv != 68) != (voltage_mv != 136)"
    rule_expressions[121] = "(voltage_mv != 68) != (voltage_mv != 136)"
    rule_expressions[122] = "(voltage_mv != 68) != (not (voltage_mv != 68))"
    rule_expressions[123] = "(voltage_mv >= 49) != (not (voltage_mv >= 49))"
    rule_expressions[124] = "(voltage_mv >= 49) != (altitude >= 49)"
    rule_expressions[125] = "(voltage_mv >= 49) != (speed >= 49)"
    rule_expressions[126] = "(voltage_mv >= 49) != (voltage_mv >= 54)"
    rule_expressions[127] = "(voltage_mv >= 49) != (voltage_mv >= -49)"
    rule_expressions[128] = "(voltage_mv >= 49) != (voltage_mv >= 24)"
    rule_expressions[129] = "(voltage_mv >= 49) != (not (voltage_mv >= 49))"
    rule_expressions[130] = "(voltage_mv >= 49) != (not (voltage_mv >= 49))"
    rule_expressions[131] = "(voltage_mv >= 49) != (voltage_mv >= 56)"
    rule_expressions[132] = "(voltage_mv >= 49) != (not (voltage_mv >= 49))"
    rule_expressions[133] = "(24 <= voltage_mv <= 61) != (24 <= -voltage_mv <= 61)"
    rule_expressions[134] = "(24 <= voltage_mv <= 61) != (-24 <= voltage_mv <= 61)"
    rule_expressions[135] = "(24 <= voltage_mv <= 61) != (12 <= voltage_mv <= 61)"
    rule_expressions[136] = "(24 <= voltage_mv <= 61) != (voltage_mv >= 24 <= 61)"
    rule_expressions[137] = "(24 <= voltage_mv <= 61) != (not (24 <= voltage_mv <= 61))"
    rule_expressions[138] = "(24 <= voltage_mv <= 61) != (not (24) <= voltage_mv <= 61)"
    rule_expressions[139] = "(24 <= voltage_mv <= 61) != (25 <= voltage_mv <= 61)"
    rule_expressions[140] = "(24 <= voltage_mv <= 61) != (24 <= altitude <= 61)"
    rule_expressions[141] = "(24 <= voltage_mv <= 61) != (12 <= voltage_mv <= 61)"
    rule_expressions[142] = "(24 <= voltage_mv <= 61) != (24 <= speed <= 61)"
    rule_expressions[143] = "(altitude % speed < 20) != (not (altitude % speed < 20))"
    rule_expressions[144] = "(altitude % speed < 20) != (altitude % 20 > speed)"
    rule_expressions[145] = "(altitude % speed < 20) != (altitude % speed < 13)"
    rule_expressions[146] = "(altitude % speed < 20) != (altitude % speed < -20)"
    rule_expressions[147] = "(altitude % speed < 20) != (not (altitude % speed < 20))"
    rule_expressions[148] = "(altitude % speed < 20) != (altitude % speed < 18)"
    rule_expressions[149] = "(altitude % speed < 20) != (altitude % 20 > speed)"
    rule_expressions[150] = "(altitude % speed < 20) != (altitude % speed < -20)"
    rule_expressions[151] = "(altitude % speed < 20) != (altitude % 20 > speed)"
    rule_expressions[152] = "(altitude % speed < 20) != (voltage_mv % speed < 20)"
    rule_expressions[153] = "(voltage_mv >= 10 or altitude != 1000) != (not (voltage_mv >= 10 or altitude != 1000))"
    rule_expressions[154] = "(voltage_mv >= 10 or altitude != 1000) != (voltage_mv >= 10 and altitude != 1000)"
    rule_expressions[155] = "(speed % 99 > altitude) != (not (speed % 99 > altitude))"
    rule_expressions[156] = "(speed % 99 > altitude) != (not (speed % 99 > altitude))"
    rule_expressions[157] = "(speed % 99 > altitude) != (speed % altitude < 99)"
    rule_expressions[158] = "(speed % 99 > altitude) != (speed % -99 > altitude)"
    rule_expressions[159] = "(speed % 99 > altitude) != (speed % 109 > altitude)"
    rule_expressions[160] = "(speed % 99 > altitude) != (speed % altitude < 99)"
    rule_expressions[161] = "(speed % 99 > altitude) != (not (speed % 99 > altitude))"
    rule_expressions[162] = "(speed % 99 > altitude) != (speed % 99 > -altitude)"
    rule_expressions[163] = "(speed % 99 > altitude) != (speed % 89 > altitude)"
    rule_expressions[164] = "(speed % 99 > altitude) != (altitude % 99 > altitude)"
    rule_expressions[165] = "(speed < 79 and voltage_mv == 50) != (speed < 79 and voltage_mv == 55)"
    rule_expressions[166] = "(speed < 79 and voltage_mv == 50) != (not (speed < 79 and voltage_mv == 50))"
    rule_expressions[167] = "(speed < 79 and voltage_mv == 50) != (speed < 79 or voltage_mv == 50)"
    rule_expressions[168] = "(speed < 79 and voltage_mv == 50) != (speed < 158 and voltage_mv == 50)"
    rule_expressions[169] = "(speed < 79 and voltage_mv == 50) != (speed < -79 and voltage_mv == 50)"
    rule_expressions[170] = "(speed < 79 and voltage_mv == 50) != (speed < 79 and -voltage_mv == 50)"
    rule_expressions[171] = "(speed < 79 and voltage_mv == 50) != (speed < 79 and voltage_mv == -50)"
    rule_expressions[172] = "(voltage_mv <= speed - 94) != (voltage_mv <= speed - 47)"
    rule_expressions[173] = "(voltage_mv <= speed - 94) != (voltage_mv <= speed - -94)"
    rule_expressions[174] = "(voltage_mv <= speed - 94) != (speed >= voltage_mv - 94)"
    rule_expressions[175] = "(voltage_mv <= speed - 94) != (altitude <= speed - 94)"
    rule_expressions[176] = "(voltage_mv <= speed - 94) != (voltage_mv <= speed - -94)"
    rule_expressions[177] = "(voltage_mv <= speed - 94) != (altitude <= speed - 94)"
    rule_expressions[178] = "(15 <= speed <= 62) != (15 <= speed <= -62)"
    rule_expressions[179] = "(15 <= speed <= 62) != (not (15) <= speed <= 62)"
    rule_expressions[180] = "(15 <= speed <= 62) != (10 <= speed <= 62)"
    rule_expressions[181] = "(15 <= speed <= 62) != (15 <= -speed <= 62)"
    rule_expressions[182] = "(15 <= speed <= 62) != (not (15) <= speed <= 62)"
    rule_expressions[183] = "(15 <= speed <= 62) != (speed >= 15 <= 62)"
    rule_expressions[184] = "(15 <= speed <= 62) != (not (15 <= speed <= 62))"
    rule_expressions[185] = "(15 <= speed <= 62) != (not (15 <= speed <= 62))"
    rule_expressions[186] = "(15 <= speed <= 62) != (not (15 <= speed <= 62))"
    rule_expressions[187] = "(15 <= speed <= 62) != (30 <= speed <= 62)"
    rule_expressions[188] = "(voltage_mv != 20) != (voltage_mv != 21)"
    rule_expressions[189] = "(voltage_mv != 20) != (not (voltage_mv != 20))"
    rule_expressions[190] = "(voltage_mv != 20) != (not (voltage_mv != 20))"
    rule_expressions[191] = "(voltage_mv != 20) != (voltage_mv != -20)"
    rule_expressions[192] = "(voltage_mv != 20) != (voltage_mv != 12)"
    rule_expressions[193] = "(altitude == speed * 10) != (altitude == speed * 8)"
    rule_expressions[194] = "(altitude == speed * 10) != (altitude == speed * 20)"
    rule_expressions[195] = "(altitude == speed * 10) != (altitude == speed * -10)"
    rule_expressions[196] = "(altitude == speed * 10) != (altitude == -speed * 10)"
    rule_expressions[197] = "(altitude == speed * 10) != (altitude == -speed * 10)"
    rule_expressions[198] = "(altitude == speed * 10) != (speed == altitude * 10)"
    rule_expressions[199] = "(altitude == speed * 10) != (not (altitude == speed * 10))"
    rule_expressions[200] = "(altitude == speed * 10) != (speed == altitude * 10)"

    return rule_expressions
