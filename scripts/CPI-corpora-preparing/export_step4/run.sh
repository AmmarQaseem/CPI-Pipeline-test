#cd DS3

#File_num="$(ls -1 | wc -l)"
#let "num = $File_num"
#for i in $( ls -1 | wc -l ); 
for i in `seq 1  $( ls DS3 -1 | wc -l ) `; 
do
    let "j = $i -1 "
    java -jar step_4_BracketingTokenMapper.jar DS3/$j.xml
    cat DS3/$j.xml-bracketing-tokens.txt >> DS3.xml.inj1-bracketing-tokens.txt

done
#cat $(ls DS3/*.txt -tr) > final.txt
#java -jar step_4_BracketingTokenMapper.jar 0.xml 
