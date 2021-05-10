# Get first and last element of list


def get_first_and_last_elements(query_list) -> list:
    return [query_list[0], query_list[-1]] if len(query_list) > 0 else []
