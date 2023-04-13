def atm_notes(amount):
    notes = [500, 200, 100, 50]
    counts = [0, 0, 0, 0]
    remaining_amount = amount
    
    for i in range(len(notes)):
        counts[i] = remaining_amount // notes[i]
        remaining_amount = remaining_amount % notes[i]
    
    if remaining_amount != 0:
        print("Amount cannot be dispensed using available notes.")
    else:
        print("#500 notes:", counts[0])
        print("#200 notes:", counts[1])
        print("#100 notes:", counts[2])
        print("#50 notes:", counts[3])

amount = int(input("Enter the amount to be dispensed: "))
atm_notes(amount)