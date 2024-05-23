# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"B58y5","system":"readv2"},{"code":"B46","system":"readv2"},{"code":"EMISNQPR140","system":"readv2"},{"code":"ZV104-5","system":"readv2"},{"code":"B8340","system":"readv2"},{"code":"B915","system":"readv2"},{"code":"B8341","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('prostate-cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["prostate-cancer-neoplasia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["prostate-cancer-neoplasia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["prostate-cancer-neoplasia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
