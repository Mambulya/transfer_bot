"""
        MAIN
program for interpretation
         oop version 89 lines
                     130
                     128
upd: 31,5%  optimisation  (Velocity, linear complexity)
upd1: 89% 3 lines optimisation  (Velocity, linear complexity)
upd2: 99.9% 3 lines optimisation  (memory complexity)
"""
from sys import exit


class Transfer_bot:
    hex_letters = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    def __init__(self, number_arg, final_base_arg, base_arg, time=8):
        try:
            self.base = int(base_arg)
            self.number = float(number_arg)
            self.final_base = int(final_base_arg)
            self.max_time = int(time)
        except ValueError:
            self.answer_error = "Try to enter a number(not True, 'a' and etc)"
            return


        # beginning check
        for i in range(len(number_arg)):

            if self.base < 10 and number_arg[i] != "." and int(number_arg[i]) >= self.base:
                self.answer_error = "The number cannot contain digits => system. Please, try again"


            if self.base == self.final_base:
                self.answer_error = 'This work is already done for me. Please, check your data'

            if self.final_base == 0 or self.base == 0 or number_arg == '0':
                self.answer_error = "I cannot take zeros"
                return


            if self.final_base == 1 or self.base == 1 or number_arg == "1":
                self.answer_error = "I can't take 1"



    def from_decimal(self):
        """
            10 - ?
           for integer part - Uncorrected
           :returns:str
        """
        if self.base != 10:
            self.answer_error = "Sorry, I need a decimal number 👉👈"

        number_intermediate = self.number
        res, time, tem_res = "", 0, 0
        res_for_integer_part = []

        if (number_intermediate < self.final_base) and (int(number_intermediate) == number_intermediate):
            return number_intermediate

        if int(number_intermediate) != 0:
            integer_part = int(number_intermediate)
            while integer_part >= self.final_base:
                integer_part_new = integer_part // self.final_base
                tem_res = integer_part - integer_part_new * self.final_base
                # if there is a letter
                if (self.final_base >= 11) and (10 <= int(tem_res) <= 15):
                    key_list = list(Transfer_bot.hex_letters.keys())
                    val_list = list(Transfer_bot.hex_letters.values())
                    letter = key_list[val_list.index(tem_res)]
                    tem_res = letter

                res_for_integer_part.append(str(tem_res))
                integer_part = integer_part_new

        if not res_for_integer_part and not integer_part:
            res_for_integer_part = "0"

        fractional_part = float(
            "0." + str(number_intermediate)[str(number_intermediate).index('.') + 1:])

        # for fractional part -
        while number_intermediate != 0:
            fractional_part = fractional_part * self.final_base
            res_part = int(fractional_part)

            if (self.final_base >= 11) and (10 <= int(res_part) <= 15):
                key_list = list(Transfer_bot.hex_letters.keys())
                val_list = list(Transfer_bot.hex_letters.values())
                letter = key_list[val_list.index(res_part)]
                res += letter
            else:
                res += str(res_part)

            if res[-1] != '0':
                fractional_part = fractional_part - int(res_part)

            time = time + 1

            if time >= self.max_time:
                break

        if (self.final_base >= 11) and (10 <= int(integer_part) <= 15):
            key_list = list(Transfer_bot.hex_letters.keys())
            val_list = list(Transfer_bot.hex_letters.values())
            letter = key_list[val_list.index(integer_part)]
            integer_part = letter

        return str(integer_part) + "".join(res_for_integer_part[::-1]) + "." + res

    # ? - 10
    def get_decimal(self):
        """
            ? - 10
            :returns:float
        """
        final_base = 10
        res, res1 = 0, 0
        first_number = str(int(self.number))
        end_number = str(self.number)[str(self.number).index(".") + 1:]

        length = len(first_number)

        for digit in range(length):
            res = res + int(first_number[::-1][digit]) * self.base ** digit

        length = len(end_number)

        for digit in range(length):
            res1 = res1 + int(end_number[digit]) * self.base ** (-1 * (digit + 1))

        return res + res1

    def transform_other_sys(self):
        """
        :returns:float
        """
        step0 = Transfer_bot.get_decimal(self)  # .. - 10
        self.number = step0
        self.base = 10
        return Transfer_bot.from_decimal(self)
