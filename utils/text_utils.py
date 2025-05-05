def clean_text(raw_list):
    start_index = raw_list.find('{')
    end_index = raw_list.rfind('}') + 1

    if start_index == -1 or end_index == -1:
        return "[]"

    return raw_list[start_index:end_index]