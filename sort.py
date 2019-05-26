import csv

with open('2019-05-26T2013_Grades-JS.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[4] == 'MC17':
                row = [row[6]]
                with open('sorted_grades.csv', mode='a') as sorted_grades:
                    sorted_grading = csv.writer(
                        sorted_grades, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    sorted_grading.writerow(row)
                    print(f'\t{row[0]} .')
                    line_count += 1
    # print(f'\t{row[4]} .')
    # line_count += 1
    print(f'Processed {line_count} lines.')
