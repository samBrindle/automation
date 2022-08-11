import re

with open("./potential-contacts.txt") as file:
    text_from_file = file.read()


def validate(file):

    phone_number_regex = r"\d{3}[-| |.]\d{3}[-| |.]\d{4}|[(]\d{3}[)]\d{3}[-| |.]\d{4}"
    need_areacode_regex = r"\d{3}[-| |.]\d{4}"
    email_regex = r"\S+[@]\S+[.com|.biz|.org|.edu|.net|.info]"

    phone_number_list = re.findall(phone_number_regex, file)
    need_areacode_phone_numbers = re.findall(need_areacode_regex, file)
    emails_list = re.findall(email_regex, file)

    return phone_number_list, need_areacode_phone_numbers, emails_list


valid_results = validate(text_from_file)

filter_non_dash_regex = r"[.| |)]"


def remove_open_paren(list):
    phone_number_list = []
    for num in list:
        num = num.replace('(', "")
        phone_number_list.append(num)
    return phone_number_list


phone_numbers_list = remove_open_paren(valid_results[0])


def fix_non_dashes(list):
    updated_number_list = []
    for num in list:
        num = re.sub(filter_non_dash_regex, "-", num)
        updated_number_list.append(num)
    return updated_number_list


phone_numbers_list = fix_non_dashes(phone_numbers_list)
phone_numbers_list = set(phone_numbers_list)
phone_numbers_list = list(phone_numbers_list)
phone_numbers_list.sort()

email_list = valid_results[2].sort()

# def fix_non_dashes(list):
#     for num in list:
#         num = re.sub(filter_non_dash_regex, "-", num)
#         num = '206-' + num

with open("./emails.txt", "w") as email_file:
    for email in email_list:
        email_file.write(str(email + "\n"))

with open("./phone_numbers.txt", "w") as number_file:
    for number in phone_numbers_list:
        number_file.write(str(number + "\n"))