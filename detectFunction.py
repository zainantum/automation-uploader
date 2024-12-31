import re

with open('/Users/apple/kerja/web-accounting-trial/application/libraries/Browserou.php', 'r') as file:
    php_content = file.read()
    
function_pattern = r'function\s+(\w+)\s*\((.*?)\)\s*{\s*# start of function #\s*(.*?)\s*# end of function #\s*}'

matches = re.findall(function_pattern, php_content, re.DOTALL | re.MULTILINE)

functions = []
for match in matches:
    function_name, parameters, body = match
    functions.append({
        'name': function_name,
        'parameters': parameters,
        'body': body.strip()
    })
    
    print(f'Function: {function_name}')
    print(f'Parameters: {parameters}')
    print(f'Body: {body}')
    print("<?php function [function_name]("+parameters+") {\n"+body+"} ?>")
