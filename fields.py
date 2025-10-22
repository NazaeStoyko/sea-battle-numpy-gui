import numpy as np


class Field_User():

    rng_user_field = np.random.default_rng(None)
    rng_bot_field = np.random.default_rng(None)
    field_user = rng_user_field.integers(low=0, high=1,size=(10,10))
    field_bot = rng_bot_field.integers(low=0, high=1,size=(10,10))
    print("\n")
    # print(field_user)
    print("\n")
       # print(field_bot)

# field = Field()