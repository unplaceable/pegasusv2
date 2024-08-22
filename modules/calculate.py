def summary_count(input_string, streamlit):
    item_list = input_string.strip().split('\n')

    summary = {}
    counter = 0
    # Count occurrences
    for item in item_list:
        counter+=1
        if item in summary:
            summary[item] += 1
        else:
            summary[item] = 1
    
    total_items = len(item_list)
    result = []
    
    # Create output with percentages
    for item, count in summary.items():
        percentage = (count / total_items) * 100
        result.append({'Unique items': item, 'COUNT': count, 'As %': f"{percentage:.2f}%"})
    
    # Change COUNTs to be comma-separated for easier reading
    for row in result:
        row['COUNT'] = "{:,}".format(row['COUNT'])
    
    result.sort(key=lambda x: x['COUNT'], reverse=True)

    streamlit.table([
        {
            'Unique': "{:,}".format(len(result)),
            'Total': "{:,}".format(counter)
        }
    ])
    streamlit.table(result)







