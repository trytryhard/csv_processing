"""CSV Processing logic-file"""

import csv
from collections import Counter, defaultdict

from tabulate import tabulate

import to_log


class CSVProcessing:
    """class as contanier for calc funcs"""

    sensitive_data: dict | list | None = None
    files: list | None = None
    encoding: str | None = None
    sep: str | None = None
    report: str | None = None
    groupby: list | None = None
    digital_col: str | None = None
    descending: bool = None

    def __init__(self):
        pass

    def output_table(self) -> list:
        """
        block of code that use tabulate for printing resulted table
        """
        self.sensitive_data = sorted(self.sensitive_data, reverse=self.descending, key=lambda x: x[1])
        for i in range(len(self.sensitive_data)):  # pylint: disable=C0200
            self.sensitive_data[i] = self.sensitive_data[i][0] + self.sensitive_data[i][1]

        header = self.groupby + [self.digital_col + "(" + self.report + ")"]

        print(tabulate(self.sensitive_data, headers=header, tablefmt="grid"))

        return [header, self.sensitive_data]

    def flat_dict(self, dictionary=None, path=None) -> list:
        """
        :param dictionary: start-dict
        :param path: helps in cerusion for flatting dict
        :return: resulted list
        """
        if dictionary is None:
            dictionary = self.sensitive_data

        if path is None:
            path = []

        result = []

        for key, value in dictionary.items():
            new_path = path + [key]

            if isinstance(value, dict):
                if all(not isinstance(v, dict) for v in value.values()):
                    result.append([new_path, list(value.values())])
                else:
                    result.extend(self.flat_dict(value, new_path))

        return result

    def avg_func(self) -> list:
        """
        calculate avg value from csv[-s]
        :return:
        """
        self.sensitive_data = defaultdict(lambda: defaultdict(dict))
        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)

                for row in reader:
                    cur_pos = self.sensitive_data

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    if any(["sum" not in cur_pos, "count" not in cur_pos]):
                        cur_pos["sum"] = 0
                        cur_pos["count"] = 0

                    try:
                        cur_pos["sum"] += float(row[self.digital_col])
                    except Exception as e:  # pylint: disable=W0707
                        to_log.log_message("===Corrupted numeric value===\n")
                        to_log.log_message(
                            f"At file {file} was found corrupted numeric: "
                            f"'{row[self.digital_col]}' "
                            f"in '{self.digital_col}' column.\n"
                        )
                        to_log.log_message(str(e) + "\n")
                        raise NameError("Corrupted numeric value")  # pylint: disable=W0707

                    cur_pos["count"] += 1

        self.sensitive_data = self.flat_dict()

        for calc_part in self.sensitive_data:
            cnt_val = calc_part[1].pop()
            sum_val = calc_part[1].pop()
            calc_part[1].append(round(sum_val / cnt_val, 4))

        return self.output_table()

    def sum_func(self) -> list:
        """
        calculate sum value from csv[-s]
        :return:
        """
        self.sensitive_data = defaultdict(lambda: defaultdict(dict))
        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)

                for row in reader:
                    cur_pos = self.sensitive_data

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    if "sum" not in cur_pos:
                        cur_pos["sum"] = 0
                    try:
                        cur_pos["sum"] += float(row[self.digital_col])
                    except Exception as e:  # pylint: disable=W0707
                        to_log.log_message("===Corrupted numeric value===\n")
                        to_log.log_message(
                            f"At file {file} was found corrupted numeric: "
                            f"'{row[self.digital_col]}' "
                            f"in '{self.digital_col}' column.\n"
                        )
                        to_log.log_message(str(e) + "\n")
                        raise NameError("Corrupted numeric value")  # pylint: disable=W0707

        self.sensitive_data = self.flat_dict()

        return self.output_table()

    def cnt_func(self) -> list:
        """
        count group(report+groupby) of values from csv[-s]
        :return:
        """
        self.sensitive_data = defaultdict(lambda: defaultdict(dict))

        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)

                for row in reader:
                    cur_pos = self.sensitive_data

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    if "cnt" not in cur_pos:
                        cur_pos["cnt"] = 0

                    cur_pos["cnt"] += 1

        self.sensitive_data = self.flat_dict()

        return self.output_table()

    def mode_func(self) -> list:
        """
        calculate mode value from csv[-s]
        :return:
        """
        self.sensitive_data = defaultdict(lambda: defaultdict(dict))

        for file in self.files:
            with open(file, newline="", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter=self.sep)
                for row in reader:
                    cur_pos = self.sensitive_data

                    for key in self.groupby:
                        group_val = row[key]

                        if group_val not in cur_pos:
                            cur_pos[group_val] = {}

                        cur_pos = cur_pos[group_val]

                    # if cur_pos.values() is None:
                    if "repeats" not in cur_pos:
                        cur_pos["repeats"] = []
                    cur_pos["repeats"].append(row[self.digital_col])

        self.sensitive_data = self.flat_dict()

        for i in self.sensitive_data:
            repeats_cnt = Counter(i[1][0])
            max_rep = repeats_cnt.most_common(1)[0][1]

            res_mode = []
            for rep_items in repeats_cnt:
                if repeats_cnt[rep_items] != max_rep:
                    continue
                res_mode.append(rep_items)

            i[1] = [", ".join(res_mode)]

        return self.output_table()
