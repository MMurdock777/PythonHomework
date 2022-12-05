def sentences_with_num(sent: str) -> int:
    sent_list = sent.split('.')
    sent_with_num = 0
    for i in sent_list:
        for j in i:
            if j.isnumeric():
                sent_with_num += 1
                break
    return sent_with_num


sentences = "This sentence has a 0. This sentence has a one. This sentence has a 2."

print(sentences_with_num(sentences))
