import pytz
import datetime
IST=pytz.timezone("asia/kolkata")
ct=datetime.datetime.now(IST)
debited_amount=int(input("withdraw amount"))
bank_name="ICICI Bank"
availblebalance=16000
balanceamount=availblebalance-debited_amount
statement=("an amount of INR {} has been debited to your account xxxxxx4985  on {}. Total avail.bal INR {}.-{}")
print(statement.format(debited_amount,ct,balanceamount,bank_name))
