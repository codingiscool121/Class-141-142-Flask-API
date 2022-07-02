import csv


with open('moviesreal.csv', encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    # print(data)


header=data[0]
all_movies=data[1:]

header.append("posterlink")
print(header)
print(len(header))

with open("final.csv", "a+", newline="", encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(header)

with open("movie_links.csv", encoding="utf-8") as f:
    reader= csv.reader(f)
    data=list(reader)
    header2=data[0]
    print(len(header2))
    all_movies_links=data[1:]


for i in all_movies:
    poster_found=any(i[8] in j for j in all_movies_links)
    # print(poster_found)
    if poster_found:
        for j in all_movies_links:
            #i[9]=original_tite j[0]=name(title)
            if i[8] == j[0]:
                i.append(j[1])
                if len(i)==28:
                    with open("final.csv", "a+", newline="", encoding="utf-8") as f:
                        writer=csv.writer(f)
                        writer.writerow(i)