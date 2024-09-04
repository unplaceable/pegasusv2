import json
import sqlparse

from modules.utils.utils import search_dict

def format_list(csv_string, streamlit=None):
    # Split the string into a list based on newlines
    items = csv_string.strip().split('\n')
    # Convert each item to a string literal and join with commas
    sql_list = ','.join(f"'{item.strip()}'" for item in items)
    # Format the SQL list
    formatted_sql_list = f"({sql_list})"
    
    # Split the formatted SQL list into lines of no more than 50 characters
    lines = []
    while len(formatted_sql_list) > 50:
        # Find the last comma within the first 50 characters
        split_index = formatted_sql_list[:50].rfind(',')
        if split_index == -1:
            split_index = 50  # If no comma is found, split at 50 characters
        lines.append(formatted_sql_list[:split_index + 1])
        formatted_sql_list = formatted_sql_list[split_index + 1:].strip()
    lines.append(formatted_sql_list)  # Add the remaining part

    streamlit.code(f'Total: {len(items)}')
    streamlit.code('\n'.join(lines))


def format_json(json_string, streamlit=None):

    search_text = streamlit.text_input('Search', label_visibility='collapsed', placeholder='Search...')

    try:
        # Parse the JSON string
        parsed_json = json.loads(json_string)

        if search_text:
            parsed_json=search_dict(data=parsed_json, search_text=search_text)
        # Format the JSON with indentation for readability
        formatted_json = json.dumps(parsed_json, indent=4)
    except json.JSONDecodeError as e:
        streamlit.code(f"Invalid JSON: {e}")
        return False
    
    streamlit.code(formatted_json)
    



def format_sql(sql_query, streamlit=None):
    try:
        # Use sqlparse to format the SQL query
        formatted_query = sqlparse.format(sql_query, reindent=True, keyword_case='upper')
    except Exception as e:
        return f"Error formatting SQL: {e}"

    streamlit.code(formatted_query)



import json

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def json_to_table(json_string, streamlit=None):


    try:
        json_data = json.loads(json_string)
    except json.JSONDecodeError as e:
        streamlit.code(f"Invalid JSON: {e}")
        return False

    # Parse the JSON string
    json_data = json.loads(json_string)
    
    # Flatten the JSON data
    flat_data = [flatten_json(item) for item in json_data]
    streamlit.table(flat_data)
