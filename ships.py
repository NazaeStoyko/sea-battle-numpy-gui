import random
import numpy as np
import fields as fd


# class Greate_Sipes():

def random_coordinate_sides_ships():
    # side_ship = random.randint(1, 4)
    side_ship = 1
    return side_ship

def creat_coordinates_Shipes_user():

    x = np.random.randint(fd.Field_User.field_user.shape[0])
    y = np.random.randint(fd.Field_User.field_user.shape[1])
    return y, x

def creat_ship_user():
    count_ship = 0
    while count_ship != 10:
        y, x = creat_coordinates_Shipes_user()
        if fd.Field_User.field_user[y][x] == 1| fd.Field_User.field_user[y][x] == 2 :
            creat_coordinates_Shipes_user()

        elif random_coordinate_sides_ships() == 1 :
            if   y >= 3:
                fd.Field_User.field_user[y][x] = 1
                fd.Field_User.field_user[y - 1][x] = 1
                fd.Field_User.field_user[y - 2][x] = 1
                fd.Field_User.field_user[y - 3][x] = 1
                print(fd.Field_User.field_user)
                count_ship=4

        # elif random_coordinate_sides_ships() == 2 :
        #     if y >= 3:
        #         fd.Field_User.field_user[y][x] = 1
        #         fd.Field_User.field_user[y - 1][x] = 1
        #         fd.Field_User.field_user[y - 2][x] = 1
        #         fd.Field_User.field_user[y - 3][x] = 1
        #         print(fd.Field_User.field_user)
        #         count_ship = 10



        print(x,y)



print(creat_ship_user())
