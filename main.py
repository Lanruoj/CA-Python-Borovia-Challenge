GRAMS = 1
ML = 1

crepes_ordered = float(input("How many crepes were ordered?:  "))
omelets_ordered = float(input("How many omelets were ordered?:  "))

eggs_required = (2*crepes_ordered) + (4*omelets_ordered)
milk_required = 250*crepes_ordered
flour_required = 300*crepes_ordered
butter_required = 20*crepes_ordered
shallots_required = 30*omelets_ordered
peppers_required = 50*omelets_ordered

eggs_ordered = 40
milk_ordered = 5000*ML
flour_ordered = 20000*GRAMS
butter_ordered = 1000*GRAMS
shallots_ordered = 1000*GRAMS
peppers_ordered = 20000*GRAMS

print(f"Sufficient eggs: {eggs_required <= eggs_ordered}\nSufficient milk: {milk_required <= milk_ordered}\nSufficient flour: {flour_required <= flour_ordered}\nSufficient butter: {butter_required <= butter_ordered}\nSufficient shallots: {shallots_required <= shallots_ordered}\nSufficient peppers: {peppers_required <= peppers_ordered}")