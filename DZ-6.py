def parse_log(pth_file):

    if pth_file:
        with open(pth_file,"r",encoding="utf-8") asfile:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)


def find_spamer(parsed_log):
    pass



if __name__ == "__main__":
   a = parse_log("./nginx_logs.txt")
   for e in a:
       print(e)

def find_spamer(parsed_log):

    if not parsed_log:
        return None

    db = {}

    for log in  parsed_log:
        if not db.get(log[0]):
            db[log[0]] = {"count":1, "files":set([log[2]])}
        else:
            db[log[0]]["count"] += 1
            db[log[0]]["files"].add(log[2])

    return max(db.items(), key=lambda x: x[1]["count"])


if __name__ == "__main__":
   parsed_log = parse_log("./nginx_logs.txt")
   spamer = find_spamer(parsed_log)

import json

from myutils import my_zip_gen


def groping(
        output_pth="./out.txt",
        user_pth="./users.csv",
        hobby_pth="./hobby.csv"):

    if not (user_pth or hobby_pth):
        return -1

    user_lines = None
    hobby_lines = None

    with open(user_pth, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()

    with open(hobby_pth, "r", encoding="utf-8") as hobby_file:
        hobby_lines = hobby_file.readlines()

    if len(user_lines) < len(hobby_lines):
        return 1

    group = {}

    for fio, hobby in my_zip_gen(user_lines, hobby_lines):
        fio = fio.replace("\n", "").replace(",", " ")
        group[fio] = hobby.replace("\n", "") if hobby else None

    with open(output_pth, "w+", encoding="utf-8") as out_file:
        out_file.writelines(json.dumps(group))
    #print(group)


    return 0


    import sys

    input_prices = list(map(lambda y:  f"{float(y):100.2f}", filter(
        lambda x: x.replace(".", "").isdigit(), sys.argv[1:])))

    with open(PRICE_FILE, "a", encoding="utf-8") as price_list:
        print(*input_prices, sep="\n", file=price_list)
        pos = sys.argv[1]
        new_price = sys.argv[2]

        if not (pos.isdigit() and new_price.replace(".", "").isdigit()):
            sys.exit(1)

        pos = int(pos)
        new_price = float(new_price)

        with open(PRICE_FILE, "r+", encoding="utf-8") as price_list:

            skip_chars = 0

            for _ in range(pos - 1):

                try:
                    skip_chars += len(next(price_list))
                except StopIteration:
                    print("out of index")
                    sys.exit(1)

            price_list.seek(skip_chars)
            price_list.writelines(f"{new_price:100.2f}")

PRICE_FILE = "./bakery.csv"


def file_reader(start=-1, end=-1):

    with open(PRICE_FILE, "r", encoding="utf-8") as price_list:

        # skip
        if start > 0:
            for _ in range(start - 1):
                price_list.readline()

        # stop
        if end > 0:
            for _ in range(abs(end - start) + 1):
                yield price_list.readline().replace("\n", "")
        else:
            for line in price_list:
                yield line.replace("\n", "")


if __name__ == "__main__":

    import sys

    start_pos = -1
    end_pos = -1

    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        start_pos = int(sys.argv[1])

    if len(sys.argv) == 3 and sys.argv[2].isdigit():
        end_pos = int(sys.argv[2])

    for l in file_reader(start_pos, end_pos):
        print(f"{float(l):.2f}")