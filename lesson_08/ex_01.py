import hashlib


s = b'qqazazazazaxkfdshksdfjkdfshkhfjdsjkfdshfkdhjkfdhjfdfjhkjkdhsjhfdshfdjfdsjfdsjkd' \
    b'fsdfsrewuyiriueywuireywerwierrewiuerwxccvvvvbgasdfghjkjhgfdsdfghjkpoiuytrewqasd' \
    b'fghjklmnbvcxzaqwsxcderfvqazwsxedcrfvtgbyhnujmikokmijnuhbygvtfcrdxeszqapafghdfgd' \
    b'fgfkdjgasdfghjkjhhdflkgjhdlkfjbnvdflkjghldfkjghdfljghdflkjghdfljgkhdflgjhdflkdf' \
    b'gjdfjkldsfhsdlkfjhdsjfhriutyreoiutyoeiwrtuyfjdlkghfdlkjgmmnbvjhguytqwersdafcxvg' \
    b'lkjdfhglkdfjghdflkjghdflkjghdlfkjghdflkjghdflkjghlfdkjghdflskjghdslkfgjhldfkjgh' \
    b'jgfhjdfgdfgnhgfjhgfhjgbdfgjghdfgdvfrfgytnhdfghfghjfghfghjfghjfgjfghjfghjfghjfgh' \
    b'jfghjfghjfghjfghjhjhfgjfghjfghjfghjfghjfghjfhgjfghjhgjghjfghjfghjfghjdghfghgfhj' \
    b'gfjhfghjfgdfgdfgdfgdsfgdsfgsdretewrtwertwertwertwertwertwertwretwrtwertwertwets' \
    b'dfgdsfgdfsgsdfgfdsgsdfgdfsgdfgdfsgfdgsdfgdfsgdsfgdfsgfsdgfdsgfsdgfdsdfgsdfgsdgj' \
    b'ertewrtwertretgdfsgdsfgdsfgsdfgxcvbcxvbxvcbvcbdfgfdgsdfgsdfgfdgsdfgsdfgfdgdsfpa'


def count_substrings(string):
    len_str = len(string)
    subs = set()
    for i in range(len_str - 1):
        for j in range(i + 1, len_str + 1):
            h_subs = hashlib.sha1(string[i:j]).hexdigest()
            if h_subs == hashlib.sha1(string).hexdigest():
                continue
            subs.add(h_subs)

    return len(subs)


print(count_substrings(s))










#
# for k in range(len_str - (i - j) + 1):
#     if h_subs == hashlib.sha1(string[i:i + (i - j)]):