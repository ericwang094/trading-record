# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import datetime

COL_TRADE_NUM = 0
COL_OPEN_TIME_DATE = 1
COL_OPEN_TIEM_DATE_TIME = 2
COL_TYPE = 3
COL_LOT = 4
COL_SYMBOL = 5
COL_OPEN = 6
COL_STOP_LOSS = 7
COL_TAKE_PROFIT = 8
COL_CLOSE_TIME_DATE = 9
COL_CLOSE_TIME_DATE_TIME = 10
COL_CLOSE = 11
COL_SWAP = 12
COL_PROFIT = 13
COL_PIP = 14


def main():
    total_num_of_trade = 0
    win_trade = 0
    lose_trade = 0
    total_profit = 0

    current_date = None
    total_num_of_current_month_trade = 0
    total_num_of_current_month_win_trade = 0
    total_num_of_current_month_lose_trade = 0
    total_profit_of_current_month = 0

    with open("record.txt", encoding="UTF-8") as f:
        f.readline()
        f.readline()
        line = f.readline().split(" ")

        while line and len(line) > 1:
            trade_date = datetime.strptime(line[COL_OPEN_TIME_DATE], "%Y.%m.%d")
            trade_month_date = trade_date.strftime("%Y-%m")

            profit = float(line[COL_PROFIT])

            if current_date is None or current_date != trade_month_date:

                if current_date is not None:
                    base = 10000 + total_profit - total_profit_of_current_month

                    print(
                        f"{current_date}, "
                        f"{total_num_of_current_month_win_trade/total_num_of_current_month_trade:.2%}, "
                        f"{round(total_profit_of_current_month, 2)}, "
                        f"{total_profit_of_current_month/base:.2%}")

                current_date = trade_month_date
                total_num_of_current_month_trade = 0
                total_num_of_current_month_win_trade = 0
                total_num_of_current_month_lose_trade = 0
                total_profit_of_current_month = 0

            total_num_of_current_month_trade += 1
            total_num_of_trade += 1
            total_profit_of_current_month += profit
            total_profit += profit
            if profit >= 0:
                total_num_of_current_month_win_trade += 1
                win_trade += 1
            else:
                total_num_of_current_month_lose_trade += 1
                lose_trade += 1

            line = f.readline().split(" ")

        print(
            f"{win_trade / total_num_of_trade:.2%}, {round(total_profit, 4)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
