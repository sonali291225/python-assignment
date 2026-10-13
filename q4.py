experience = int(input("Enter experience:"))
rating = float(input("Enter rating:")) 

promotion = experience >=2 and rating >=4
training = rating < 3 or experience < 1

print("Experience:",experience)
print("Rating:",rating)
print("promotion eligible:",promotion)
print("Training needed:",training)