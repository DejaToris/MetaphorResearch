import xlwings
import json
import DAL_Excel_interface as Ei


OUTPUT_EXCEL = 'ResultsComparison.xslx'
CONN_DATA = 'ConnotationsResult.json'
EVAL_DATA = 'Evaluations.json'


def excel_writer(data, start_row, start_column):
    excel_conn = Ei.XLConnection(OUTPUT_EXCEL, 'D:/code/MetaphorResearch/MetaphorResearch')
    



def main():
    pass