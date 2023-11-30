# ALGORITHMS & COMPLEXITY -- University Of Ioannina
#
#                       PROJECT 1

import numpy as np #install numpy
import random
import time

time_start = time.time() # capture start time

# variables/constants
CCN_LIMIT = 20000
TRANSACTIONS = 1000000


# functions 
# Function that generates 20.000 different
# 16-digit numbers that represent credit
# card info (16-digit code). Returns: ccn(string)
def ccn_generator():
    ccn = ''.join(str(random.randint(0, 9)) for _ in range(16))
    return ccn


# main program
random.seed(2545) # generate a seed for random number generator
credit_cards = [ccn_generator() for _ in range(CCN_LIMIT)] # call the function to generate 20k ccns

transaction_history = {ccn: [] for ccn in credit_cards} # save transactions in a dictionairy
for _ in range(TRANSACTIONS):
    ccn = random.choice(credit_cards)
    amount = round(random.uniform(10,1000), 2) # amount is between $10.00 and $10000.00 
    transaction_history[ccn].append(amount) # append amount to corressponding credit card number (ccn)


# Create an array of total charges for each card number
total_charges = np.array([sum(transactions) for transactions in transaction_history.values()])
# Create an array of counts of charges for each card number
count_charges = np.array([len(transactions) for transactions in transaction_history.values()])
# Find the index of the smallest total charges and retrieve the corresponding card number
smallest_total_charges_index = np.argmin(total_charges)
smallest_total_charges_number = list(transaction_history.keys())[smallest_total_charges_index]
# Find the index of the biggest total charges and retrieve the corresponding card number
biggest_total_charges_index = np.argmax(total_charges)
biggest_total_charges_number = list(transaction_history.keys())[biggest_total_charges_index]
# Find the index of the smallest count of charges and retrieve the corresponding card number
smallest_count_charges_index = np.argmin(count_charges)
smallest_count_charges_number = list(transaction_history.keys())[smallest_count_charges_index]
# Find the index of the biggest count of charges and retrieve the corresponding card number
biggest_count_charges_index = np.argmax(count_charges)
biggest_count_charges_number = list(transaction_history.keys())[biggest_count_charges_index]

print(f"1. Smallest total charge: {smallest_total_charges_number} (Total charges: {total_charges[smallest_total_charges_index]})")
print(f"2. Biggest total charge: {biggest_total_charges_number} (Total charges: {total_charges[biggest_total_charges_index]})")
print(f"3. Least amount of charges: {smallest_count_charges_number} (Count of charges: {count_charges[smallest_count_charges_index]})")
print(f"4. Most amount of charges: {biggest_count_charges_number} (Count of charges: {count_charges[biggest_count_charges_index]})")

time_end = time.time() # capture end time

time_elapsed = time_end - time_start
print(f"Time elapsed: {time_elapsed:.3f} seconds")
