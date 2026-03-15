from datetime import date, timedelta

def main():
    today = date.today()
    spaced_list = [1,3,7,15,30,60]

    print("To revise\n")

    for i in spaced_list:
        past_date = today - timedelta(days=i)
        print(past_date.strftime("%B %d, %Y"))