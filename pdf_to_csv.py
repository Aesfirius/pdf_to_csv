import argparse
import tabula
from info_path_sys import path_to_project


def pdf_to_csv_all_in_one(input_file_pdf, output_file_csv):
    # convert PDF into CSV
    tabula.convert_into(input_file_pdf, output_file_csv, output_format="csv", pages='all')
    print(f"Output file path {path_to_project() + output_file_csv}")


def pdf_to_csv(input_file_pdf, output_file_csv):
    # Read a PDF File
    df = tabula.read_pdf(path_to_project() + input_file_pdf, pages='all')
    # convert PDF into CSV
    for i, page in enumerate(df):
        iter_output_file_csv = f"__{i}.".join(output_file_csv.split('.'))
        page.to_csv(path_to_project() + iter_output_file_csv, encoding='utf-8')
        print(f"Output file path {path_to_project() + iter_output_file_csv}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to CSV")
    parser.add_argument("--input_file_pdf", action="store", default=None, help="PDF file name")
    parser.add_argument("--output_file_csv", action="store", default=None, help="CSV file name")
    parser.add_argument("--all_in_one", action="store", default=False, help="All pages in oneCSVtable")
    args = parser.parse_args()
    input_file_pdf = args.input_file_pdf
    output_file_csv = args.output_file_csv
    all_in_one = args.all_in_one
    if all_in_one:
        pdf_to_csv_all_in_one(input_file_pdf, output_file_csv)
    else:
        pdf_to_csv(input_file_pdf, output_file_csv)
