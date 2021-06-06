import csv
print("without-BOM-UTF8 / open with utf_8")
csv_file = open("./woBOM.csv","r",encoding="utf_8")
f = csv.DictReader(csv_file)
for row in f:
    print(row)
# OrderedDict([('#', '1'), ('a', 'あ'), ('b', '𦀗')])
csv_file.close()
print("without-BOM-UTF8 / open with utf_8_sig")
csv_file = open("./woBOM.csv","r",encoding="utf_8_sig")
f = csv.DictReader(csv_file)
for row in f:
    print(row)
# OrderedDict([('#', '1'), ('a', 'あ'), ('b', '𦀗')])
csv_file.close()
print("with-BOM-UTF8 / open with utf_8")
csv_file = open("./withBOM.csv","r",encoding="utf_8")
f = csv.DictReader(csv_file)
for row in f:
    print(row)
# OrderedDict([('\ufeff#', '1'), ('a', 'あ'), ('b', '𦀗')])
csv_file.close()
print("with-BOM-UTF8 / open with utf_8_sig")
csv_file = open("./withBOM.csv","r",encoding="utf_8_sig")
f = csv.DictReader(csv_file)
for row in f:
    print(row)
# OrderedDict([('#', '1'), ('a', 'あ'), ('b', '𦀗')])
csv_file.close()
