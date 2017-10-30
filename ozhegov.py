file_read = open("/home/arsolga/Documents/Ozhegov/ozhegov_part.txt", "r+")
#print(file_read.read())
for line in file_read:
    #tmp_lst = line.replace("|||||", ": '").replace("||||!|", ": '")
    #tmp_lst = tmp_lst+"'"
    #tmp_lst.replace("\n", "")
    tmp_lst = line.split("|")
    tmp_lst = str(tmp_lst)
    tmp_sems = tmp_lst[1:(tmp_lst.find(","))]
    voc_entry = line[(line.find("|")):(line.rfind("\n"))].replace("|||||", " ")
    dict_o = dict.fromkeys([tmp_sems], voc_entry)
    def sum_dicts(*dicts):
        from collections import defaultdict
        ozhegov = defaultdict(list)
        for d in dicts:
            for k,v in d.items():
                ozhegov[k].append(v)
        return ozhegov
    a = sum_dicts(dict_o)
    #print(tmp_sems)
    #print(voc_entry)
print(a)
file_read.close()
