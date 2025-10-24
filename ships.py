import random
import numpy as np
import fields as fd


# class Greate_Sipes():


def get_choose_the_side(size,x,y,side_ships):

    true_values = {key: value for key, value in side_ships.items() if value is True}
    choose_the_side =  random.choice(list(true_values.keys()))
    location_shipes(size,x,y,choose_the_side)
    # plecement_ships()

def location_shipes(size,x,y,choose_the_side):

    if choose_the_side == 1:
       fd.Field_User.field_user[y][x] = 1
       fd.Field_User.field_user[y - 1][x] = 1
       fd.Field_User.field_user[y - 2][x] = 1
       fd.Field_User.field_user[y - 3][x] = 1
       fd.Field_User.field_user[y - 4][x] = 1
       print(fd.Field_User.field_user)

    elif choose_the_side == 2:
         fd.Field_User.field_user[y][x] = 1
         fd.Field_User.field_user[y + 1][x] = 1
         fd.Field_User.field_user[y + 2][x] = 1
         fd.Field_User.field_user[y + 3][x] = 1
         fd.Field_User.field_user[y + 4][x] = 1
         print(fd.Field_User.field_user)

    elif choose_the_side == 3:
         fd.Field_User.field_user[y][x - 1] = 1
         fd.Field_User.field_user[y][x - 2] = 1
         fd.Field_User.field_user[y][x - 3] = 1
         fd.Field_User.field_user[y][x - 4] = 1
         print(fd.Field_User.field_user)

    elif choose_the_side == 4:
         fd.Field_User.field_user[y][x + 1] = 1
         fd.Field_User.field_user[y][x + 2] = 1
         fd.Field_User.field_user[y][x + 3] = 1
         fd.Field_User.field_user[y][x + 4] = 1
         print(fd.Field_User.field_user)




def declaration_sides(y_up,y_down,x_left,x_right):

    side_ships_dic = {y_up: False, y_down: False, x_left: False, x_right: False}
    return side_ships_dic

def create_coordinates_ships_user():

    x = np.random.randint(fd.Field_User.field_user.shape[0])
    y = np.random.randint(fd.Field_User.field_user.shape[1])
    return y, x

def plecement_ships():
    y_up = 1
    y_down = 2
    x_left = 3
    x_right = 4
    create_ships_side = False
    size = 4
    x,y = create_coordinates_ships_user()
    print(x,y)

    side_ships = declaration_sides(y_up,y_down,x_left,x_right)

    while create_ships_side == False:

        if y - (size - 1) > 0 and side_ships[y_up] == False and fd.Field_User.field_user[x][y] != 1:
            side_ships[y_up] = True
            continue

        elif y + (size - 1) < 9 and  side_ships[y_down] == False and fd.Field_User.field_user[x][y] != 1:
            side_ships[y_down] = True
            continue

        elif x - (size - 1) > 0 and  side_ships[x_left] == False and fd.Field_User.field_user[x][y] != 1:
            side_ships[x_left] = True
            continue

        elif x + (size - 1) < 9 and side_ships[x_right] == False and fd.Field_User.field_user[x][y] != 1:
            side_ships[x_right] = True
            continue

        get_choose_the_side(size,x,y,side_ships)
        create_ships_side = True

plecement_ships()


    # count_ship = 0
    # while count_ship != 10:
    #     y, x = creat_coordinates_Shipes_user()
    #     if fd.Field_User.field_user[y][x] == 1| fd.Field_User.field_user[y][x] == 2 :
    #         creat_coordinates_Shipes_user()
    #
    #     elif random_coordinate_sides_ships() == 1 :
    #         if   y >= 3:
    #             fd.Field_User.field_user[y][x] = 1
    #             fd.Field_User.field_user[y - 1][x] = 1
    #             fd.Field_User.field_user[y - 2][x] = 1
    #             fd.Field_User.field_user[y - 3][x] = 1
    #             print(fd.Field_User.field_user)
    #             count_ship=4
    #
    #     elif random_coordinate_sides_ships() == 2 :
    #         if y >= 3:
    #             fd.Field_User.field_user[y][x] = 1
    #             fd.Field_User.field_user[y - 1][x] = 1
    #             fd.Field_User.field_user[y - 2][x] = 1
    #             fd.Field_User.field_user[y - 3][x] = 1
    #             print(fd.Field_User.field_user)
    # #             count_ship = 10
    #
    #
    #
    #     print(x,y)