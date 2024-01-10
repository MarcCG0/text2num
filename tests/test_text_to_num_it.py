from unittest import TestCase
from text_to_num import text2num


class TestTextToNumIT(TestCase):
    def test_text2num(self):
        self.assertEqual(text2num("zero", "it"), 0)
        self.assertEqual(text2num("uno", "it"), 1)
        self.assertEqual(text2num("nove", "it"), 9)
        self.assertEqual(text2num("dieci", "it"), 10)
        self.assertEqual(text2num("undici", "it"), 11)
        self.assertEqual(text2num("diciannove", "it"), 19)
        self.assertEqual(text2num("venti", "it"), 20)
        self.assertEqual(text2num("ventuno", "it"), 21)
        self.assertEqual(text2num("ventitré", "it"), 23)
        self.assertEqual(text2num("trenta", "it"), 30)
        self.assertEqual(text2num("trentuno", "it"), 31)
        self.assertEqual(text2num("trentadue", "it"), 32)
        self.assertEqual(text2num("trentanove", "it"), 39)
        self.assertEqual(text2num("ottantotto", "it"), 88)
        self.assertEqual(text2num("novantanove", "it"), 99)
        self.assertEqual(text2num("cento", "it"), 100)
        self.assertEqual(text2num("centouno", "it"), 101)
        self.assertEqual(text2num("duecento", "it"), 200)
        self.assertEqual(text2num("duecentouno", "it"), 201)
        self.assertEqual(text2num("mille", "it"), 1000)
        self.assertEqual(text2num("milleuno", "it"), 1001)
        self.assertEqual(text2num("duemila", "it"), 2000)
        self.assertEqual(text2num("duemila novantanove", "it"), 2099)
        self.assertEqual(text2num("novemila novecentonovantanove", "it"), 9999)
        self.assertEqual(text2num("novecentonovantanovemilanovecentonovantanove", "it"), 999999)
        self.assertEqual(text2num("cinquanta", "it"), 50)
        self.assertEqual(text2num("sessanta", "it"), 60)
        self.assertEqual(text2num("settanta", "it"), 70)
        self.assertEqual(text2num("ottanta", "it"), 80)
        self.assertEqual(text2num("novanta", "it"), 90)
        self.assertEqual(text2num("centodue", "it"), 102)
        self.assertEqual(text2num("centotre", "it"), 103)
        self.assertEqual(text2num("centoventotto", "it"), 128)
        self.assertEqual(text2num("centonovantacinque", "it"), 195)
        self.assertEqual(text2num("duecentosette", "it"), 207)
        self.assertEqual(text2num("duecentosessantuno", "it"), 261)
        self.assertEqual(text2num("trecentodieci", "it"), 310)
        self.assertEqual(text2num("trecentotrentuno", "it"), 331)
        self.assertEqual(text2num("quattrocentoquindici", "it"), 415)
        self.assertEqual(text2num("cinquecentosessantasette", "it"), 567)
        self.assertEqual(text2num("seicentosettantatre", "it"), 673)
        self.assertEqual(text2num("settecentonovantasei", "it"), 796)
        self.assertEqual(text2num("ottocentonovantanove", "it"), 899)
        self.assertEqual(text2num("millecentotrentuno", "it"), 1131)
        self.assertEqual(text2num("milleduecentoventicinque", "it"), 1225)
        self.assertEqual(text2num("milletrecentoquaranta", "it"), 1340)
        self.assertEqual(text2num("millequattrocentosessantasette", "it"), 1467)
        self.assertEqual(text2num("millecinquecentoottantatre", "it"), 1583)
        self.assertEqual(text2num("millesettecentosettantacinque", "it"), 1775)
        self.assertEqual(text2num("milleottocentonovantasei", "it"), 1896)
        self.assertEqual(text2num("millenovecentodieci", "it"), 1910)
        self.assertEqual(text2num("duemiladuecentoventicinque", "it"), 2225)
        self.assertEqual(text2num("duemilatrecentoquaranta", "it"), 2340)
        self.assertEqual(text2num("duemilaquattrocentosessantasette", "it"), 2467)
        self.assertEqual(text2num("duemilacinquecentoottantatre", "it"), 2583)
        self.assertEqual(text2num("duemilasettecentosettantacinque", "it"), 2775)
        self.assertEqual(text2num("duemilaottocentonovantasei", "it"), 2896)
        self.assertEqual(text2num("duemilanovecentodieci", "it"), 2910)
        self.assertEqual(text2num("tremilacinquecento", "it"), 3500)
        self.assertEqual(text2num("tremilaquattrocentonovanta", "it"), 3490)
        self.assertEqual(text2num("tremilacinquecentoventisette", "it"), 3527)
        self.assertEqual(text2num("quattromilaottocentonovanta", "it"), 4890)
        self.assertEqual(text2num("quattromilacinquecentoottantatre", "it"), 4583)
        self.assertEqual(text2num("quattromilasettecentosettantacinque", "it"), 4775)
        self.assertEqual(text2num("quattromilaottocentonovantasei", "it"), 4896)
        self.assertEqual(text2num("quattromilanovecentodieci", "it"), 4910)
        self.assertEqual(text2num("cinquemilaottocentosessantuno", "it"), 5861)
        self.assertEqual(text2num("cinquemilaottocentoventotto", "it"), 5828)
        self.assertEqual(text2num("seimilatrecentoquarantaquattro", "it"), 6344)
        self.assertEqual(text2num("settemilacentonovantasei", "it"), 7196)
        self.assertEqual(text2num("settemiladuecentodieci", "it"), 7210)
        self.assertEqual(text2num("settemilacinquecento", "it"), 7500)
        self.assertEqual(text2num("settemilaquattrocentonovanta", "it"), 7490)
        self.assertEqual(text2num("settemilacinquecentoventisette", "it"), 7527)
        self.assertEqual(text2num("ottomilaottocentonovanta", "it"), 8890)
        self.assertEqual(text2num("ottomilacinquecentoottantatre", "it"), 8583)
        self.assertEqual(text2num("ottomilasettecentosettantacinque", "it"), 8775)
        self.assertEqual(text2num("ottomilaottocentonovantasei", "it"), 8896)
        self.assertEqual(text2num("ottomilanovecentodieci", "it"), 8910)
        self.assertEqual(text2num("novemilacinquecentoottantatre", "it"), 9583)
        self.assertEqual(text2num("novemilasettecentosettantacinque", "it"), 9775)
        self.assertEqual(text2num("novemilaottocentonovantasei", "it"), 9896)
        self.assertEqual(text2num("novemilanovecentodieci", "it"), 9910)
        self.assertEqual(text2num("diecimila", "it"), 10000)
        self.assertEqual(text2num("centomila", "it"), 100000)
        # self.assertEqual(alpha2digit("uno virgola uno", "it"), '1.1')
        # self.assertEqual(alpha2digit("uno virgola quattrocentouno", "it"), '1.401')

        # test1 = "cinquantatre mila venti milioni duecentoquarantatre mila settecentoventiquattro"
        # self.assertEqual(text2num(test1, "it"), 53_020_243_724)

        # test2 = "cinquantun milioni cinquecentosettantottomila trecentodue"
        # self.assertEqual(text2num(test2, "it"), 51_578_302)

        # test3 = "ottantacinque"
        # self.assertEqual(text2num(test3, "it"), 85)

        # test4 = "ottantuno"
        # self.assertEqual(text2num(test4, "it"), 81)

        # self.assertEqual(text2num("quindici", "it"), 15)
        # self.assertEqual(text2num("centoquindici", "it"), 115)
        # self.assertEqual(text2num("settantacinquemila", "it"), 75000)
        # self.assertEqual(text2num("millenovecentoventi", "it"), 1920)

    # def test_text2num_exc(self):
    #     self.assertRaises(ValueError, text2num, "mille mille duecento", "it")
    #     self.assertRaises(ValueError, text2num, "sessanta quindici", "it")
    #     self.assertRaises(ValueError, text2num, "sessanta cento", "it")

    # def test_text2num_zeroes(self):
    #     self.assertEqual(text2num("zero", "it"), 0)
    #     self.assertEqual(text2num("zero otto", "it"), 8)
    #     self.assertEqual(text2num("zero zero centoventicinque", "it"), 125)
    #     self.assertRaises(ValueError, text2num, "cinque zero", "it")
    #     self.assertRaises(ValueError, text2num, "cinquantazero tre", "it")
    #     self.assertRaises(ValueError, text2num, "cinquantatre zero", "it")

    # def test_alpha2digit_integers(self):
    #     source = "venticinque mucche, dodici galline e centoventicinque kg di patate."
    #     expected = "25 mucche, 12 galline e 125 kg di patate."
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    #     source = "C'erano trecento uomini e cinquecento donne"
    #     expected = "C'erano 300 uomini e 500 donne"
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    #     source = "milleduecentosessantasei dollari."
    #     expected = "1266 dollari."
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    #     source = "uno due tre quattro venti quindici"
    #     expected = "1 2 3 4 20 15"
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    #     source = "ventuno, trentuno."
    #     expected = "21, 31."
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    # def test_relaxed(self):
    #     source = "uno due tre quattro trentacinque."
    #     expected = "1 2 3 4 35."
    #     self.assertEqual(alpha2digit(source, "it", relaxed=True), expected)

    #     source = "uno due tre quattro venti, cinque."
    #     expected = "1 2 3 4 20, 5."
    #     self.assertEqual(alpha2digit(source, "it", relaxed=True), expected)

    #     source = "trentaquattro = trenta quattro"
    #     expected = "34 = 34"
    #     self.assertEqual(alpha2digit(source, "it", relaxed=True), expected)

    # def test_alpha2digit_formal(self):
    #     source = "più trentatre nove sessanta zero sei dodici ventuno"
    #     expected = "+33 9 60 06 12 21"
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    #     source = "zero nove sessanta zero sei dodici ventuno"
    #     expected = "09 60 06 12 21"
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    # def test_and(self):
    #     source = "cinquanta sessanta trenta e undici"
    #     expected = "50 60 30 e 11"
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    # def test_alpha2digit_zero(self):
    #     source = "tredicimila zero novanta"
    #     expected = "13000 090"
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    #     self.assertEqual(alpha2digit("zero", "it"), "0")

    # def test_alpha2digit_decimals(self):
    #     source = (
    #         "dodici virgola novantanove, centoventi virgola zero cinque,"
    #         " uno virgola duecentotrentasei, uno virgola due tre sei."
    #     )
    #     expected = "12.99, 120.05, 1.236, 1.2 3 6."
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    #     self.assertEqual(alpha2digit("virgola quindici", "it"), "0.15")

    # def test_alpha2digit_signed(self):
    #     source = "Abbiamo più venti gradi dentro e meno quindici fuori."
    #     expected = "Abbiamo +20 gradi dentro e -15 fuori."
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    # def test_one_as_noun_or_article(self):
    #     source = "Un momento per favore! novantanove gatti. Uno due tre quattro!"
    #     expected = "Un momento per favore! 99 gatti. 1 2 3 4!"
    #     self.assertEqual(alpha2digit(source, "it"), expected)
    #     # End of segment
    #     source = "Né uno. Uno uno. Trentuno"
    #     expected = "Né uno. 1 1. 31"
    #     self.assertEqual(alpha2digit(source, "it"), expected)

    # # def test_accent(self):
    # #     self.assertEqual(text2num("un milione", "it"), 1000000)

