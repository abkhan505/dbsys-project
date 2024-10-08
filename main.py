#db-wrapper

# step1) import csv/text file

# step2) sanitization
    # identify the header of each column as a attribute in the table
    # allow input to identify ensure all data matches desired data type of each field
    # filter/set default values for null data, use markers 
    # ensure each attribute entry is within a valid range of values, such as glucose not being negative

# step3) push to db

# we want to identify primary key but the primary key may be a constraint, since db's are
# atomic, is there a way for db to check if primary key is redundant 