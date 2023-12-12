
while True:
    def convertor(num: int) -> str:



        if num==0:
            return " صفر "

        def three_digit_to_word(num: int) -> str:

            zero_nineteen = {
                0: '',
                1: 'یک',
                2: 'دو',
                3: 'سه',
                4: 'چهار',
                5: 'پنج',
                6: 'شش',
                7: 'هفت',
                8: 'هشت',
                9: 'نه',
                10: 'ده',
                11: 'یازده',
                12: 'دوازده',
                13: 'سیزده',
                14: 'چهارده',
                15: 'پانزده',
                16: 'شانزده',
                17: 'هفده',
                18: 'هجده',
                19: 'نوزده'
            }

            twenty_ninety = {
                0: '',
                1: '',
                2: 'بیست',
                3: 'سی',
                4: 'چهل',
                5: 'پنجاه',
                6: 'شصت',
                7: 'هفتاد',
                8: 'هشتاد',
                9: 'نود'
            }

            one_hun_nine_hun = {
                0: '',
                1: 'صد',
                2: 'دویست',
                3: 'سیصد',
                4: 'چهارصد',
                5: 'پانصد',
                6: 'ششصد',
                7: 'هفتصد',
                8: 'هشتصد',
                9: 'نهصد'
            }

            num = str(num).zfill(3)

            two_last_digit = int(num[-2:])

            first_digit = int(num[0])

            middle_digit = int(num[1])

            last_digit = int(num[2])

            final_res=""

            if two_last_digit in range(0, 20):

                final_res = zero_nineteen[two_last_digit]

            else:

                final_res = f"{twenty_ninety[middle_digit]}{
                    ' و ' if last_digit else ''}{zero_nineteen[last_digit]}"

            if first_digit:

                final_res = f"{one_hun_nine_hun[first_digit]}{
                    ' و ' if two_last_digit else ''}{final_res}"

            return final_res

        def split_num(num: int) -> tuple:


            num_list = []

            while num != 0:

                num_list.append(num % 1000)

                num //= 1000

            return tuple(num_list)

        unit = {
            0: '',
            1: ' هزار',
            2: ' میلیون',
            3: ' میلیارد',
            4: ' بیلیون',
            5: ' بیلیارد',
            6: ' تریلیون',
            7: ' تریلیارد',
            8: ' کوآدریلیون',
            9: ' کادریلیارد',
            10: ' کوینتیلیون',
            11: ' کوانتینیارد',
            12: ' سکستیلیون',
            13: ' سکستیلیارد',
            14: ' سپتیلیون',
            15: ' سپتیلیارد',
            16: ' اکتیلیون',
            17: ' اکتیلیارد',
            18: ' نانیلیون',
            19: ' نانیلیارد',
            20: ' دسیلیون',
            21: ' دسیلیارد',
            22: ' آندسیلیون',
            23: ' آندسیلیارد',
            24: ' دودسیلیون',
            25: ' دودسیلیارد',
            26: ' تریدسیلیون',
            27: ' تریدسیلیارد',
            28: ' کوادردسیلیون',
            29: ' کوادردسیلیارد',
            30: ' کویندسیلیون',
            31: ' کویندسیلیارد',
            32: ' سیدسیلیون',
            33: ' سیدسیلیارد',
            34: ' گوگول'
        }

        is_negative, num = (True, -num) if num < 0 else (False, num)

        num_list = split_num(num)

        num_to_word_list = []

        for index, three_digit in enumerate(num_list):

            three_digit_word = three_digit_to_word(three_digit)

            if three_digit_word:

                num_to_word_list.insert(0, F"{three_digit_word}{unit[index]}")

        return f"{'منفی' if is_negative else ''}{'و'.join(num_to_word_list)}"

    number = int(input("enter the number"))
    res = convertor(number)
    print(res)
