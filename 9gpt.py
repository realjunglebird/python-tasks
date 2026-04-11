import re

def main(string):
    pattern = r'data\s*#(-?\d+)\s*=:\s*([\w_]+)'

    matches = re.findall(pattern, string)

    result = {key: int(num) for num, key in matches}

    return result

print(main(
     r"<% <sect>data #-5494 =: requ </sect>.<sect> data #-7891=: qura </sect>.<sect> data #7693 =:sozaon</sect>. " +
     r"<sect> data#-4459 =: quat_756</sect>. %>"))

print(main('<% <sect>data #-5494 =: requ </sect>.<sect> data #-7891=: qura\n</sect>.<sect> data #7693 =:sozaon</sect>. <sect> data#-4459 =:\nquat_756</sect>. %>'))
