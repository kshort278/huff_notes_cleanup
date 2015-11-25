#Source: http://www.nyu.edu/projects/wke/byseries/huff50s.php


def main():
    #define old file and new file to write to
    source_file = "huff_program_notes_1950s.txt"
    target_file = "huff_program_notes_1950s_goodData.txt"

    #open both files and read source, write to target
    s = open(source_file, 'r')
    t = open(target_file, 'w')
    
    count = 0

    #for each line of data in the file
    for line in s:

        #take off "new line" and add a * as a marker for the end of each line
        text_line = line.rstrip('\n')
        text_line = text_line + '*'

        #to get rid of "Program Date" column in header
        #then strip * and add new line then write to new file
        if (text_line[:12] == "Program Date" ):
            new_text = text_line[13:]
            new_text = new_text.rstrip("*")
            new_text += "\n"
            t.write(new_text)

        #for four digit date format M/D/YY
        #and statement to exclude records with "n.d." in year column
        #then split the rest by tabs, remove the * and new line
        elif (text_line[5].isdigit() and (text_line[-5:-1].isdigit())):
            text_line = text_line[7:]
            values = text_line.split("\t")
            new_text = ''
            for i in range(len(values)):
                new_text += values[i]+"\t"
            new_text = new_text.rstrip("\t")
            new_text = new_text.rstrip("*")
            new_text += "\n"
            t.write(new_text)
            count +=1

        #for five digit date format M/DD/YY
        #and statement to exclude records with "n.d." in year column
        #then split the rest by tabs, remove the * and new line
        elif (text_line[6].isdigit() and (text_line[-5:-1].isdigit())):
            text_line = text_line[8:]
            values = text_line.split("\t")
            new_text = ''
            for i in range(len(values)):
                new_text += values[i]+"\t"
            new_text = new_text.lstrip("\t")
            new_text = new_text.rstrip("\t")
            new_text = new_text.rstrip("*")
            new_text += "\n"
            t.write(new_text)
            count +=1

        #for six digit date form MM/DD/YY
        #exclude records with "n.d." in year column
        #split lines by tabs, remove * and add new line
        elif (text_line[-5:-1].isdigit()):
            values = text_line.split("\t")
            new_text = ''
            for i in range(len(values)):
                new_text += values[i]+"\t"
            new_text = new_text.rstrip("\t")
            new_text = new_text.rstrip("*")
            new_text += "\n"
            t.write(new_text)
            count +=1

    #each record formatted besides header is written to new file
    #then counted using "count+=1"

    #close both files
    s.close()
    t.close

    #print how many records were written to the new file
    print("File written. %d records. " % count)

main()
