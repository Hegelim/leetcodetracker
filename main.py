import os
import pandas as pd
from datetime import date
import time

CSV_DIR = "questions.csv"


def add_problem():
    while True:
        os.system("cls")
        question_number = int(input("Please enter the question number:\n"))
        if os.path.exists(CSV_DIR):
            df1 = pd.read_csv(CSV_DIR, index_col=False)
            df2 = pd.DataFrame({"question number": [question_number],
                                "date": [date.today().strftime("%m/%d/%y")]})
            df = pd.concat([df1, df2])
        else:
            df = pd.DataFrame({"question number": [question_number],
                               "date": [date.today().strftime("%m/%d/%y")]})
        df.to_csv(CSV_DIR, index=False)
        selection = input("Back to previous menu? yes/no\n")
        if selection != "no":
            break


def view_latest_problems():
    while True:
        if os.path.exists(CSV_DIR):
            df = pd.read_csv(CSV_DIR, index_col=False)
            df = df.sort_values(["date"], ascending=False)
            print(df.head(3))
        else:
            print("No questions yet :)")
        selection = input("Back to previous menu? yes/no\n")
        if selection != "no":
            break


def delete_question():
    while True:
        os.system("cls")
        print("Please select the following:\n"
              "1. Delete a question.\n"
              "2. Back to previous menu.\n")
        selection = int(input("Please type your selection:\n"))
        assert type(selection) == int
        if selection == "1":
            try:
                df = pd.read_csv(CSV_DIR)
                df = df.drop(df[df["question number"] == selection].index)
                df.to_csv(CSV_DIR, index=False)
            except FileNotFoundError:
                print("No questions yet :)")
        elif selection == "2":
            break


if __name__ == "__main__":
    while True:
        os.system("cls")
        print("====================================\n"
              "====                            ====\n"
              "=== WELCOME TO LEETCODE TRACKER! ===\n"
              "====                            ====\n"
              "====================================")
        print("Please select the following options: \n"
              "1. Add a problem\n"
              "2. View latest problems\n"
              "3. Edit existing problems\n"
              "4. Exit\n")
        selection = input("What's your choice today?\n")
        if selection == '1':
            add_problem()
        elif selection == '2':
            view_latest_problems()
        elif selection == '3':
            delete_question()
        elif selection == '4':
            print("Have a great day!")
            time.sleep(3)
            os.system("cls")
            break
        else:
            print("unknown choice, please type again")
