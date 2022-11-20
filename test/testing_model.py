from model.horse_data import HorseData
from model.percentage import Percentage

def testing_horse_data():
    left_horse_data = HorseData(0)
    right_horse_data = HorseData(3)

    print(left_horse_data.child_id, left_horse_data.parent_one_id, left_horse_data.parent_two_id)
    print(left_horse_data.child_info)
    print(left_horse_data.parent_one_info)
    print(left_horse_data.parent_two_info)
    print(left_horse_data.total_info)

    print(right_horse_data.child_id, right_horse_data.parent_one_id, right_horse_data.parent_two_id)
    print(right_horse_data.child_info)
    print(right_horse_data.parent_one_info)
    print(right_horse_data.parent_two_info)
    print(right_horse_data.total_info)

def testing_percentage():
    left_horse_data = HorseData(0)
    right_horse_data = HorseData(3)
    
    percentage = Percentage(left_horse_data.total_info, right_horse_data.total_info)
    percentage.cal_percentage()
    print(percentage.rate)

if __name__ == '__main__':
    # testing_horse_data()

    testing_percentage()