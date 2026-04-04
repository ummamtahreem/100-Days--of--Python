import random
rand_num=random.randint(1,10)

#this will produce a whole number between the 1 and 10

random_num_0_to_1= random.random()*10
print(random_num_0_to_1)


random_float=random.uniform(1,10)
print(random_float)

random_head_or_tails=random.randint(1,2)
if random_head_or_tails == 0:
    print("heads")
else:
    print("tails")
