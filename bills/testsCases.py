import unittest
import calculator
import cases_tests
import amortization
import extraAmount


class TestCreditCard(unittest.TestCase):

    """
    7 Payment Test Cases
    """

    def testPayment(self):
        answer = 9297.96
        self.assertEqual(round(calculator.monthly_bills(200000, 3.1, 36), 2), answer)

    def testPaymentTwo(self):
        answer = 52377.50
        self.assertEqual(round(calculator.monthly_bills(850000, 3.4, 24), 2), answer)

    def testPaymentNoInteres(self):
        answer = 10000
        self.assertEqual(calculator.monthly_bills(480000, 0, 48), answer)

    def testUsura(self):
        amount: float = 50000
        interest = 12.4
        payment = 48
        self.assertRaises(cases_tests.Usura, calculator.monthly_bills, amount, interest, payment)

    def testPaymentOneQuote(self):
        answer = 90000
        self.assertEqual(calculator.monthly_bills(90000, 2.4, 1), answer)

    def testPaymentNoPayment(self):
        amount = 0
        interest = 2.4
        payment = 0
        self.assertRaises(cases_tests.ZeroAmount, calculator.monthly_bills, amount, interest, payment)

    def testNoamount(self):
        amount = 0
        interest = 2.4
        payment = 60
        self.assertRaises(cases_tests.ZeroAmount, calculator.monthly_bills, amount, interest, payment)

    def testpaymentNegativas(self):
        amount = 2
        interest = 3.1
        payment = -2
        self.assertRaises(cases_tests.NegativePayment, calculator.monthly_bills, amount, interest, payment)

    """
    5 Amortization Test Cases
    """

    def testAmortizationOnePayment(self):
        amount: float = 90000
        interest: float = 2.4
        payment: int = 1
        answer: list = [['Cuota', 'balance', 'Pago interés', 'Abono capital'], ['#', 90000, 2.4, 90000], [1, 90000, 0.0, 90000.0]]
        self.assertEqual(amortization.ModelCalculator(amount, interest, payment).amortization(), answer)

    def testAmortizationOne(self):
        amount: float = 200000
        interest: float = 3.1
        payment: int = 36
        answer: list = [['Cuota', 'balance', 'Pago interés', 'Abono capital'], ['#', 9297.95911564735, 3.1, 200000], [1, 196902.04088435264, 6200.0, 3097.9591156473507], [2, 193708.04503612022, 6103.963267414932, 3193.995848232419], [3, 190415.0353165926, 6004.949396119727, 3293.009719527624], [4, 187019.94229575963, 5902.866094814371, 3395.09302083298], [5, 183519.60139128083, 5797.618211168548, 3500.3409044788023], [6, 179910.74991876318, 5689.107643129705, 3608.8514725176456], [7, 176190.02405059748, 5577.2332474816585, 3720.725868165692], [8, 172353.95568051864, 5461.890745568522, 3836.0683700788286], [9, 168398.9691909674, 5342.972626096078, 3954.986489551273], [10, 164321.37812024003, 5220.368044919989, 4077.5910707273615], [11, 160117.3817263201, 5093.962721727441, 4203.99639391991], [12, 155783.06144418867, 4963.638833515924, 4334.320282131427], [13, 151314.37723331118, 4829.274904769849, 4468.684210877502], [14, 146707.1638118965, 4690.745694232647, 4607.213421414704], [15, 141957.12677441793, 4547.922078168791, 4750.03703747856], [16, 137059.83858877755, 4400.670930006956, 4897.288185640395], [17, 132010.7344693823, 4248.854996252104, 5049.104119395247], [18, 126805.10812228579, 4092.332768550851, 5205.6263470965], [19, 121438.1073584293, 3930.9583517908595, 5367.000763856491], [20, 115904.72957089327, 3764.5813281113083, 5533.377787536043], [21, 110199.8170719436, 3593.046616697691, 5704.9124989496595], [22, 104318.0522855265, 3416.1943292302517, 5881.7647864170995], [23, 98253.95279073047, 3233.8596208513213, 6064.09949479603], [24, 92001.86621159577, 3045.8725365126447, 6252.086579134706], [25, 85555.96494850788, 2852.0578525594688, 6445.901263087882], [26, 78910.24074626427, 2652.2349134037445, 6645.724202243606], [27, 72058.49909375112, 2446.2174631341923, 6851.741652513158], [28, 64994.35345001005, 2233.8134719062846, 7064.145643741066], [29, 57711.21929131301, 2014.8249569503116, 7283.134158697039], [30, 50202.30797369636, 1789.0477980307035, 7508.9113176166475], [31, 42460.620405233596, 1556.2715471845872, 7741.687568462763], [32, 34478.940522148485, 1316.2792325622415, 7981.679883085109], [33, 26249.828562687737, 1068.8471561866031, 8229.111959460748], [34, 17765.614132483708, 813.7446854433198, 8484.21443020403], [35, 9018.389054943353, 550.734038106995, 8747.225077540355], [36, 9297.95911564735, 279.57006070324394, 0]]

        self.assertEqual(amortization.ModelCalculator(amount, interest, payment).amortization(), answer)

    def testAmortizationTwo(self):
        amount: float = 850000
        interest: float = 3.4
        payment: int = 24
        answer: list = [['Cuota', 'balance', 'Pago interés', 'Abono capital'], ['#', 52377.49863983651, 3.4, 850000], [1, 826522.5013601634, 28900.000000000004, 23477.498639836504], [2, 802246.7677665725, 28101.76504624556, 24275.733593590947], [3, 777145.6592307995, 27276.390104063466, 25101.10853577304], [4, 751191.1130048102, 26422.952413847186, 25954.54622598932], [5, 724354.1122071372, 25540.49784216355, 26837.000797672958], [6, 696604.6533823434, 24628.039815042666, 27749.45882479384], [7, 667911.7129575065, 23684.558214999677, 28692.94042483683], [8, 638243.2125582253, 22708.998240555225, 29668.50039928128], [9, 607565.9831453684, 21700.26922697966, 30677.229412856846], [10, 575845.7279324745, 20657.24342694253, 31720.25521289398], [11, 543046.984042342, 19578.754749704134, 32798.74389013238], [12, 509133.0828599452, 18463.59745743963, 33913.901182396876], [13, 474066.1090373468, 17310.524817238136, 35066.973822598375], [14, 437806.8581047801, 16118.247707269791, 36259.25093256672], [15, 400314.7926405061, 14885.433175562524, 37492.06546427398], [16, 361547.9969504468, 13610.70294977721, 38766.7956900593], [17, 321463.1302069255, 12292.631896315192, 40084.866743521314], [18, 280015.3779941245, 10929.746427035469, 41447.75221280104], [19, 237158.4022060882, 9520.522851800233, 42856.975788036274], [20, 192844.2892412587, 8063.385675007, 44314.11296482951], [21, 147023.49643562498, 6556.705834202796, 45820.79280563371], [22, 99644.79667459973, 4998.79887881125, 47378.69976102526], [23, 50655.22112169961, 3387.923086936391, 48989.57555290012], [24, 52377.49863983651, 1722.2775181377867, 0]]

        self.assertEqual(amortization.ModelCalculator(amount, interest, payment).amortization(), answer)

    def testAmortizationNoInterest(self):
        amount: float = 480000
        interest: float = 0
        payment: int = 48
        answer: list = [['Cuota', 'balance', 'Pago interés', 'Abono capital'], ['#', 10000.0, 0, 480000], [1, 470000.0, 0.0, 10000.0], [2, 460000.0, 0.0, 10000.0], [3, 450000.0, 0.0, 10000.0], [4, 440000.0, 0.0, 10000.0], [5, 430000.0, 0.0, 10000.0], [6, 420000.0, 0.0, 10000.0], [7, 410000.0, 0.0, 10000.0], [8, 400000.0, 0.0, 10000.0], [9, 390000.0, 0.0, 10000.0], [10, 380000.0, 0.0, 10000.0], [11, 370000.0, 0.0, 10000.0], [12, 360000.0, 0.0, 10000.0], [13, 350000.0, 0.0, 10000.0], [14, 340000.0, 0.0, 10000.0], [15, 330000.0, 0.0, 10000.0], [16, 320000.0, 0.0, 10000.0], [17, 310000.0, 0.0, 10000.0], [18, 300000.0, 0.0, 10000.0], [19, 290000.0, 0.0, 10000.0], [20, 280000.0, 0.0, 10000.0], [21, 270000.0, 0.0, 10000.0], [22, 260000.0, 0.0, 10000.0], [23, 250000.0, 0.0, 10000.0], [24, 240000.0, 0.0, 10000.0], [25, 230000.0, 0.0, 10000.0], [26, 220000.0, 0.0, 10000.0], [27, 210000.0, 0.0, 10000.0], [28, 200000.0, 0.0, 10000.0], [29, 190000.0, 0.0, 10000.0], [30, 180000.0, 0.0, 10000.0], [31, 170000.0, 0.0, 10000.0], [32, 160000.0, 0.0, 10000.0], [33, 150000.0, 0.0, 10000.0], [34, 140000.0, 0.0, 10000.0], [35, 130000.0, 0.0, 10000.0], [36, 120000.0, 0.0, 10000.0], [37, 110000.0, 0.0, 10000.0], [38, 100000.0, 0.0, 10000.0], [39, 90000.0, 0.0, 10000.0], [40, 80000.0, 0.0, 10000.0], [41, 70000.0, 0.0, 10000.0], [42, 60000.0, 0.0, 10000.0], [43, 50000.0, 0.0, 10000.0], [44, 40000.0, 0.0, 10000.0], [45, 30000.0, 0.0, 10000.0], [46, 20000.0, 0.0, 10000.0], [47, 10000.0, 0.0, 10000.0], [48, 10000.0, 0.0, 0]]

        self.assertEqual(amortization.ModelCalculator(amount, interest, payment).amortization(), answer)

    def testAmortizacionUsura(self):
        amount: float = 50000
        interest: float = 12.4
        payment: int = 60

        self.assertRaises(cases_tests.Usura, calculator.monthly_bills, amount, interest, payment)

    """
    4 Amortization with Extra Payment
    """

    def testAmortizationExtraPaymentOne(self):
        amount: float = 200000
        interest: float = 3.10
        payment: int = 36
        number_amount_to_pay: int = 10
        extrapayment: float = 53000

        answer: list = [['Cuota', 'balance', 'Pago interés', 'Abono capital'], ['#', 9297.95911564735, 3.1, 200000], [1, 196902.04088435264, 6200.0, 3097.9591156473507], [2, 193708.04503612022, 6103.963267414932, 3193.995848232419], [3, 190415.0353165926, 6004.949396119727, 3293.009719527624], [4, 187019.94229575963, 5902.866094814371, 3395.09302083298], [5, 183519.60139128083, 5797.618211168548, 3500.3409044788023], [6, 179910.74991876318, 5689.107643129705, 3608.8514725176456], [7, 176190.02405059748, 5577.2332474816585, 3720.725868165692], [8, 172353.95568051864, 5461.890745568522, 3836.0683700788286], [9, 168398.9691909674, 5342.972626096078, 3954.986489551273], [10, 120619.33723588737, 5220.368044919989, 47779.63195508001], [11, 115060.57757455253, 3739.199454312509, 5558.759661334841], [12, 109329.49636371632, 3566.8779048111282, 5731.081210836222], [13, 103420.75163534418, 3389.214387275206, 5908.744728372145], [14, 97328.8358203925, 3206.0433006956696, 6091.915814951681], [15, 91048.07061517732, 3017.1939104321677, 6280.7652052151825], [16, 84572.60168860047, 2822.490189070497, 6475.468926576854], [17, 77896.39322529973, 2621.7506523466145, 6676.208463300736], [18, 71013.22229963668, 2414.788189984292, 6883.170925663058], [19, 63916.673075278064, 2201.409891288737, 7096.549224358614], [20, 56600.13082496433, 1981.41686533362, 7316.542250313731], [21, 49056.775764890874, 1754.6040555738944, 7543.355060073456], [22, 41279.57669795514, 1520.7600487116172, 7777.199066935734], [23, 33261.2844599444, 1279.6668776366093, 8018.292238010741], [24, 24994.425162555326, 1031.0998182582764, 8266.859297389074], [25, 16471.293226947193, 774.8271800392151, 8523.131935608135], [26, 7683.944201335205, 510.610090035363, 8787.349025611988], [27, 0, 238.20227024139137, 7922.146471576597]]

        self.assertEqual(extraAmount.ModelExtraAmount(amount, interest, payment).amortization_extra_amount(number_amount_to_pay, extrapayment), answer)

    def testAmortizationExtraPaymentTwo(self):
        amount: float = 850000
        interest: float = 3.4
        payment: int = 24
        number_amount_to_pay: int = 5
        extrapayment: float = 90000

        answer: list = [['Cuota', 'balance', 'Pago interés', 'Abono capital'], ['#', 52377.49863983651, 3.4, 850000], [1, 826522.5013601634, 28900.000000000004, 23477.498639836504], [2, 802246.7677665725, 28101.76504624556, 24275.733593590947], [3, 777145.6592307995, 27276.390104063466, 25101.10853577304], [4, 751191.1130048102, 26422.952413847186, 25954.54622598932], [5, 686731.6108469737, 25540.49784216355, 64459.502157836454], [6, 657702.9869759344, 23348.874768797108, 29028.6238710394], [7, 627687.3898932796, 22361.90155718177, 30015.59708265474], [8, 596651.2625098147, 21341.37125637151, 31036.127383465], [9, 564559.9067953118, 20286.1429253337, 32091.355714502806], [10, 531377.4449865159, 19195.036831040605, 33182.4618087959], [11, 497066.77947622095, 18066.83312954154, 34310.665510294966], [12, 461589.55133857596, 16900.270502191514, 35477.228137645], [13, 424906.09744425106, 15694.044745511583, 36683.45389432492], [14, 386975.4061175191, 14446.807313104537, 37930.69132673197], [15, 347755.0712856782, 13157.16380799565, 39220.33483184085], [16, 307201.2450695548, 11823.67242371306, 40553.826216123445], [17, 265268.58876208315, 10444.842332364864, 41932.65630747164], [18, 221910.22214015748, 9019.132017910828, 43358.36662192568], [19, 177077.67105308632, 7544.947552765355, 44832.55108707115], [20, 130720.81322905475, 6020.640815804935, 46356.85782403157], [21, 82787.82223900611, 4444.507649787862, 47932.990990048645], [22, 33225.109555295814, 2814.785956126208, 49562.7126837103], [23, 0, 1129.6537248800578, 34354.763280175874]]

        self.assertEqual(extraAmount.ModelExtraAmount(amount, interest, payment).amortization_extra_amount(number_amount_to_pay,extrapayment), answer)
