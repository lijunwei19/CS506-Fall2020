import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    # declear rows list
    rows = []

    # declear field list
    fields = []

    # reading csv file 
    with open (csv_file_path, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        
        #extracting field names through first row
        # fields = next(csvreader)

        #extracting each data row one by one
        for row in csvreader:
            new_row = []
            for i in row:
                try:
                    new_row.append(int(i))
                except:
                    new_row.append(i)
            rows.append( new_row )
    return rows


def main():
    print(read_csv('tests/test_files/dataset_2.csv'))



if __name__ == "__main__":
    main()
