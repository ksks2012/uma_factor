from model.horse_data import HorseData

def testing_horse_data():
    left_horse_data = HorseData(0)
    right_horse_data = HorseData(3)

    print(left_horse_data.child_id, left_horse_data.parent_one_id, left_horse_data.parent_two_id)
    print(left_horse_data.child_info)
    print(left_horse_data.parent_one_info)
    print(left_horse_data.parent_two_info)
    print(left_horse_data.total_info)

if __name__ == '__main__':
    testing_horse_data()