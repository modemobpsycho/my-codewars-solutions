from re import compile, VERBOSE

regex = compile("""
^              
(?=.*?[a-z])   
(?=.*?[A-Z])   
(?=.*?[0-9])  
[A-Za-z\d]    
{6,}           
$             
""", VERBOSE)
