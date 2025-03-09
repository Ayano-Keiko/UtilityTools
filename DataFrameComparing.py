import numpy
import pandas

def TwoTableisSame(df_a, df_b):
    '''
    Check if two table is same
    :param df_a: First table
    :param df_b: Second Table
    :return: boolen, true all same, false difference
    '''
    equalflag = [False] * df_a.shape[0]

    if df_a.equals(df_b):
        # completely same
        return True
    else:
        # check if shape is same
        if df_a.shape[0] != df_b.shape[0] or df_a.shape[1] != df_b.shape[1]:
            return False
        else:

            index = 0
            for a_row in df_a.values:
                for b_row in df_b.values:
                    if numpy.array_equal(a_row, b_row):
                        equalflag[index] = True
                        break

                index += 1

    if False in equalflag:
        return False
    else:
        return True