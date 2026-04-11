import re

def main(string):
    patternNumber = r'(?<=data#).\d+'
    patternLetters = r'\w+(?=</sect>)'
    #string = string.replace('\n', '')
    text = "".join(string.split())

    # print(text)

    numbers = re.findall(patternNumber, text)

    keys = re.findall(patternLetters, text)

    for i in range(len(numbers) - 1):
        numbers[i] = int(numbers[i])
    dictionary = dict(zip(keys, numbers))
    return dictionary

print(main(
     r"<% <sect>data #-5494 =: requ </sect>.<sect> data #-7891=: qura </sect>.<sect> data #7693 =:sozaon</sect>. " +
     r"<sect> data#-4459 =: quat_756</sect>. %>"))

print(main('<% <sect>data #-5494 =: requ </sect>.<sect> data #-7891=: qura\n</sect>.<sect> data #7693 =:sozaon</sect>. <sect> data#-4459 =:\nquat_756</sect>. %>'))
