def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"fistname": "Ian", "lastname": "Lecona"}

    super_list = [
        {"fistname": "Ian", "lastname": "Lecona"},
        {"fistname": "Ia", "lastname": "Leona"},
        {"fistname": "an", "lastname": "Econa"},
        {"fistname": "Nai", "lastname": "Anocel"},
        {"fistname": "Fernado", "lastname": "Lara"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integrer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

        
if __name__ == '__main__':
    run()