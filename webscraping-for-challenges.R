setwd("C:/Users/tompo/OneDrive/Documents/Tom Potter/General Programming/Cipher Challenge 2018")

library("rvest")

year <- "2015"
challenge <- "1"

url <- paste("https://", year, ".cipherchallenge.org/challenges/challenge-", challenge, "/", sep = "")

#Reading the HTML code from the website
webpage <- read_html(url)

#Get only the sections with the scores in
data_html <- html_nodes(webpage, '.challenge__content')

Encoded <- html_text(data_html)

data_html <- html_nodes(webpage, '.challenge--a')

Decoded <- html_text(data_html)

data_html <- html_nodes(webpage, '.challenge__answer')

Decoded <- append(Decoded, html_text(data_html))

files <- c(paste(year, "-challenge-", challenge, "a-question", sep = ""), 
           paste(year, "-challenge-", challenge, "a-answer", sep = ""),
           paste(year, "-challenge-", challenge, "b-question", sep = ""),
           paste(year, "-challenge-", challenge, "b-answer", sep = ""))

writeLines(Encoded[1], files[1])
writeLines(Decoded[2], files[2])
writeLines(Encoded[2], files[3])
writeLines(Decoded[3], files[4])

print(year)
print(challenge)