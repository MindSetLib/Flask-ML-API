from process_data import map_for_dict_Gender


def test_map_for_dict_Gender():
    assert map_for_dict_Gender('Male') == 0
    assert map_for_dict_Gender('Female') == 1
