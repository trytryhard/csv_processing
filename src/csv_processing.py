import pathlib
import os
import csv
from collections import defaultdict, Counter
from nested_dicts import flat_dict
from tabulate import tabulate

class CSV_Processing():
    files:list | None = None

    encoding: str | None = None
    sep: str | None = None

    groupby:list | None = None
    digital_col: str | None = None
    descending:bool = None

    def __init__(self):
        pass

    def output_table(self, output_list)->bool:
        output_list = sorted(output_list, reverse=self.descending, key=lambda x: x[1])
        for i in range(len(output_list)):
            output_list[i] = output_list[i][0] + output_list[i][1]

        header = self.groupby + [self.digital_col]
        print(tabulate(output_list, headers=header, tablefmt="grid"))
        return True

    def avg_func(self) -> bool:
        """
        calculate avg value from csv[-s]
        :return:
        """
        res_dict = defaultdict(lambda : defaultdict(dict))
        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)

                for row in reader:
                    cur_pos = res_dict

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    if any(["sum" not in cur_pos, "count" not in cur_pos]):
                        cur_pos["sum"] = 0
                        cur_pos["count"] = 0

                    cur_pos["sum"] += float(row[self.digital_col])
                    cur_pos["count"] += 1

        print(res_dict)
        res_list = flat_dict(res_dict)

        for calc_part in res_list:
            cnt_val = calc_part[1].pop()
            sum_val = calc_part[1].pop()
            calc_part[1].append(round(sum_val/cnt_val, 4))

        self.output_table(res_list)

        return True

    def sum_func(self) -> bool:
        """
        calculate sum value from csv[-s]
        :return:
        """
        res_dict = defaultdict(lambda : defaultdict(dict))

        print(self.digital_col)
        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)


                for row in reader:
                    cur_pos = res_dict

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    if "sum" not in cur_pos:
                        cur_pos["sum"] = 0

                    cur_pos["sum"] += float(row[self.digital_col])

        res_list = flat_dict(res_dict)
        self.output_table(res_list)

        return True

    def cnt_func(self) -> bool:
        """
        count group(report+groupby) of values from csv[-s]
        :return:
        """
        res_dict = defaultdict(lambda : defaultdict(dict))

        print(self.digital_col)
        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)


                for row in reader:
                    cur_pos = res_dict

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    if "cnt" not in cur_pos:
                        cur_pos["cnt"] = 0

                    cur_pos["cnt"] += 1

        res_list = flat_dict(res_dict)
        self.output_table(res_list)

        return True

    def mode_func(self) -> bool:
        """
        calculate mode value from csv[-s]
        :return:
        """
        res_dict = defaultdict(lambda : defaultdict(dict))

        print(self.digital_col)
        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)


                for row in reader:
                    cur_pos = res_dict

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    if cur_pos.values() is None:
                        cur_pos['cnt'] = Counter()

                    cur_pos['cnt'][row[self.digital_col]] += 1

        print(res_dict,'\n\n')
        res_list = flat_dict(res_dict)
        print(res_list)
        #for calc_part in res_list:


        self.output_table(res_list)

        return True