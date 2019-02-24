# -*- coding: utf8 -*-

# File: tableutils.py
# Author: Doug Rudolph
# Created: October 19, 2018


def _table_metadata(objects):
    """ Goal of this function is collect metadata that helps generate the table

    Params:
        objects (list): list of objects being printed in table

    Returns:
        len_dict (dict): dictionary that maps the column names to the longest value in said column
        longest_object (int): returns the length of the longest object name inside the `objects` list
        columns (set): all the column names to be printed in the tableA

    Todo:
        * Not needed to return `columns`. Instead we can get the columns from `len_dict.keys()`
    """
    if objects is None or len(objects) == 0:
        return None

    # Objects that are being returned
    len_dict = {}
    longest_object = 0
    columns = set()

    for obj in objects:
        for key, val in vars(obj).items():

            # itr vars
            val = str(val)
            length = len(val) if len(val) > len(key) else len(key)
            cur_length = len_dict.get(key, None)

            # if column name isn't dictionary, add the length of the column
            # or the column name is in dict and the value is longer, update the length
            if cur_length is None or cur_length < length:
                len_dict[key] = length

            # used for populating `longest_object`
            # will check for the largest key every iteration,
            # will update `longest_object` if a larger key name was found
            if len(key) > longest_object:
                longest_object = len(key)

            # Add all unique column names to the `columns` set
            columns.add(key)

    return len_dict, longest_object, columns


def _header(longest_var, longest_column_vals, column_names):
    """ Takes in table metadata and creates the header of the table.
    The header is the top part of the table that shows the variables
    stored among the objects.

    Example:
        An example of a table header:

        +----------------------------------+
        |       | var1  |  var2   | var3   |
        +----------------------------------+

    Attributes:
        The first box doesn't contain any data because the first
        column stores the name of all the objects.

    Params:
        longest_var (int): length of the longest class name among the objects
        longest_column_vals (dict): stores the longest value in each column
        column_names (set): all unique column names among each object

    Returns:
        header (str): The header of the table

    Todo:
        * column_names is not needed in
            - can be collected from `longest_column_vals.keys()`
    """
    header = ''
    var_col_padding = longest_var + 1

    header += '|{}|'.format(' '*var_col_padding)
    for col in sorted(column_names):
        padding = longest_column_vals[col] - len(col)
        col_str = ' {}{} |'.format(col, ' '*padding)
        header += col_str

    row_split = '+{}+\n'.format('-'*(len(header)-2))
    header = row_split + header + '\n' + row_split

    return header


def _body(longest_var, longest_column_vals, column_names, objects):
    """ Takes in table metadata and creates the body of the table.
    The body is the part of the table that comes after the header.
    Each row of the body contains the object name, and data inside
    each class variable.

    Example:
        An example of a table body would be:

        +---------------------+
        | obj1  | 3    |      |
        +---------------------+
        | obj2  | 3    | 4    |
        +---------------------+

    Attributes:
        Note that if an object doesn't have an instance of
        a variable, the box for that variable is left
        empty.

    Params:
        objects (list): list of objects with class variables
        longest_var (int): length of the longest class name among the objects
        longest_column_vals (dict): stores the longest value in each column
        column_names (set): all unique column names among each object

    Returns:
        body (str): the body of the table represented as a string

    Todo:
        * column_names is not needed in

    """
    body = ''

    # iterate over all the objects
    for obj in objects:

        # calculate the padding
        obj_name = str(obj)
        obj_name_padding = longest_var - len(obj_name)

        # prepare `row` for the next iteration by reseting it to `None`
        # append the object name to the first column of the row
        row = None
        row = '| {}{}|'.format(str(obj), ' '*obj_name_padding)

        # iterate through the columns in alphanumeric order
        # TODO: can get column names from `longest_column_vals.keys()`
        for col in sorted(column_names):
            var_dict = vars(obj)
            val = None

            # if the column exists in the object, add to row
            if var_dict.get(col):
                var = str(var_dict[col])
                padding = longest_column_vals[col] - len(var)
                val = ' {}{} |'.format(var, ' '*padding)

            # otherwise, make spaces that is the length of the longest column value
            else:
                padding = longest_column_vals[col]
                val = ' {} |'.format(' '*padding)

            row += val

        row_split = '+{}+\n'.format('-'*(len(row)-2))
        body += row + '\n' + row_split

    return body


def construct_table(objects):
    if len(objects) == 0 or objects is None:
        raise ValueError

    longest_column_vals, longest_object, column_names = _table_metadata(objects=objects)
    header = _header(longest_object, longest_column_vals, column_names)
    body = _body(longest_object, longest_column_vals, column_names, objects=objects)

    return header+body
