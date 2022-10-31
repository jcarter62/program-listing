from windows_tools.installed_software import *


# method to generate list of installed software on this system
def get_software() -> list:
    # get list of installed software
    installed_software = get_installed_software()
    # print list of installed software
    return installed_software


# method to write list of installed software to csv file
def print_installed_software(installed_software: list):
    qt = '"'
    # write header line
    print('name, version, publisher')
    # write each line of installed software to console
    for software in installed_software:
        t = qt + software['name'] + qt + ',' + qt + software['version'] + qt + ',' + qt + software['publisher'] + qt
        print(t)


def main():
    # define installed_software as dictionary

    # create list of installed software
    installed_software = get_software()

    # sort installed_software by name descending
    installed_software.sort(key=lambda x: (x['name'] + x['version']).lower(), reverse=True)

    last_name = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    results = []
    for i in installed_software:
        if last_name == i['name'].lower():
            pass
        else:
            results.append(i)
            last_name = i['name'].lower()

    results.sort(key=lambda x: x['name'].lower(), reverse=False)

    # write list of installed software to csv file
    print_installed_software(results)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

