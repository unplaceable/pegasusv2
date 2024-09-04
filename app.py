import streamlit as st
from modules.format import format_list, format_json, format_sql, json_to_table
from modules.calculate import summary_count

st.set_page_config(page_title="Pegasus", 
                   page_icon="https://cdn-icons-png.flaticon.com/512/1218/1218659.png",
                   layout='wide',
                   initial_sidebar_state='collapsed')

col1, col2 = st.columns([2, 3])

with col1:
    commands = ['format_json', 'format_list', 'format_sql', 'summary_count', 'json_to_table']
    commands = st.multiselect("commands", options=commands, label_visibility='collapsed', placeholder='{ command }')
    input = st.text_area("inputs", placeholder='Inputs', height=300, label_visibility='collapsed')

with col2:
    for command in commands:
        if command:
            function = globals()[command]
            result = function(input, streamlit=st)

    