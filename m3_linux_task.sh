wget www.gigabyte.ru/media/list/news; cat news|grep  '"news_subtitle2' >news1;cat news1|sed -e 's/<div class="news_subtitle2">//g' >news2;cat news2| sed -e 's/div>//g' >news1; cat news|grep  '"news_date2' >news2;cat news2|sed -e 's/<div class="news_date2">//g' >news3;cat news3| sed -e 's/div>//g' >news2;paste news2  news1 >news5;  cat news5;rm news; rm news1; rm news2; rm news3

