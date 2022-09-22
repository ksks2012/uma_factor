from test_code.horse_info import HorseInfoApp

HORSE_INFO = {'horse_name': '神鷹☆Numero1', 'blue': {'智力': 2}, 'red': {'中距離': 1}, 'white': {'路況差勁': 1, '彎道靈巧': 1, 'URA劇本': 1, '陰天': 1, '集中力': 1}}

def testing_horse_info_app():
    HorseInfoApp(horse_info=HORSE_INFO).run()

if __name__ == '__main__':
    testing_horse_info_app()