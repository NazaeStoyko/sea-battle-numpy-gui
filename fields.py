import numpy as np

rng_user_field = np.random.default_rng(seed=0)
rng_bot_field = np.random.default_rng(seed=0)
field_user = rng_user_field.integers(low=0, high=1,size=(10,10))
field_bot = rng_bot_field.integers(low=0, high=1,size=(10,10))


print(field_user)
print(np.ndim(field_user))

print("\n")

print(field_bot)
print(np.ndim(field_bot))