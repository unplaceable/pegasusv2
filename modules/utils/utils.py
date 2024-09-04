def search_dict(data, search_text):
    """
    Recursively searches for a search_text in both keys and values of a nested dictionary.
    
    :param data: The dictionary to search through.
    :param search_text: The text to search for in keys or values.
    :return: A dictionary containing matched items or full sub-dictionaries for matched keys.
    """
    if not isinstance(data, dict):
        return {}

    def matches(item):
        """Checks if a key or value matches the search_text."""
        return search_text in str(item)

    result = {}
    for key, value in data.items():
        # Check if the key matches
        key_match = matches(key)

        # If the key matches, include the entire sub-dictionary or value without further filtering
        if key_match:
            result[key] = value
        else:
            # Check if the value matches or contains matching nested dictionaries
            value_match = matches(value) if not isinstance(value, dict) else bool(search_dict(value, search_text))
            
            # If the value matches, add the matched result or sub-items
            if value_match:
                if isinstance(value, dict):
                    # Recursively search within the nested dictionary
                    nested_result = search_dict(value, search_text)
                    result[key] = nested_result if nested_result else value
                else:
                    result[key] = value

    return result
