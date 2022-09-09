import yaml

def read_yaml(file_name: str):
	""" Read yaml return dict """
	with open(file_name, 'r', encoding='utf-8') as fp:
		yaml_file = yaml.safe_load(fp)

	if yaml_file is None:
		return dict()

	return yaml_file

def read_static_data():
    horse_name_dict = read_yaml("./etc/horse_name.yaml")
    blue_list = read_yaml("./etc/blue.yaml")
    red_list = read_yaml("./etc/red.yaml")
    green_list = read_yaml("./etc/green.yaml")
    factor_list = read_yaml("./etc/factor.yaml")

    return horse_name_dict, blue_list, red_list, green_list, factor_list