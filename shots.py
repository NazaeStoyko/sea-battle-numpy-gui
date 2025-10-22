import numpy as np
import fields as fd

class Shot_Bot():


    coordinates_used_bot = np.array([[None,None]])
    shot = True

    def shot_coordinates_bot(self):
        x = np.random.randint(fd.Field_User.field_user.shape[0])
        y = np.random.randint(fd.Field_User.field_user.shape[1])
        return x,y


shot_bot = Shot_Bot()

while shot_bot.shot == True:

    x,y = shot_bot.shot_coordinates_bot()

    if fd.Field_User.field_user[x][y] == 3:
        shot_bot.shot_coordinates_bot()

    else:
        fd.Field_User.field_user[x][y] = 3
        coordinates_used_bot = np.array([[x,y]])


        print(fd.Field_User.field_user)
        print("\n")
        print(coordinates_used_bot)