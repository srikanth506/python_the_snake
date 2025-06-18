import csv
with open("C:\\Users\\srika\\Downloads\\Iris.csv","r") as iris_file:
    csv_reader = csv.DictReader(iris_file,delimiter=",")
    with open("new_iris.csv","w") as new_iris:
        csv_writer = csv.DictWriter(new_iris,fieldnames=["Id", "SepalLengthCm"],delimiter="\t" )
        
        csv_writer.writeheader()

        for row in csv_reader:
            csv_writer.writerow(row.keys[0:2])
