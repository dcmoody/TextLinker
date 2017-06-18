#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import codecs
text = codecs.open('txt name','r+','utf-8') #first text
content = text.read()
result = codecs.open('raw4.html', 'w+','utf-8') #output text
result.write("""
<!DOCTYPE html>
<html>
<head><title>translation test</title>
<meta charset="UTF-8">
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.7/angular.min.js"></script>


<script type="text/javascript">

var app = angular.module("translator", []);

app.controller("Highlight",function($scope){

    $scope.GClass = function(gc) {
		$scope.hovered = gc;
	};

    $scope.EClass = function(ec) {
		if( ec === $scope.hovered ){
            return "highlight";}
	 else {return "";
        }
	}
});
</script>
<style>hr { border: 1px dotted #DDD; }
.translation span:hover {background-color:yellow; }
.highlight {background-color:yellow; }
div#wrapper{
display:flex;}
div#idbox1 {
  flex: 0 0 50%;
margin-right: 10px;}
div#idbox2 {
  flex: 1;
}
</style>

</head>

<body> <div id="wrapper" data-ng-controller="Highlight" data-ng-app="translator">
   """)
rep=re.sub('''      ''','''</br></br>&nbsp;&nbsp;&nbsp;&nbsp;''',content)
sentences=re.split('''((?!\. Jahrhundert)(?!cf\. )(?!\. Weltkrieg)(?!\. [a-z])(?![\.\?\!]\s[\-,?!])[\.\?\!\. ]\s|\.\[)''', rep) #splits into a list based on punction
result.write("""<div class="translation" id="idbox1" style="border:1px solid black;"> """)
end=sentences[-1]
sentences[0::2]
sentences[1::2]
sentences =[i+j for i,j in zip(sentences[::2], sentences[1::2])] #binds every two splits together, letting punction be placed in the same tag as the preceding sentence.  
b=0
for i in sentences:
    b=b+1
    result.write('<span data-ng-mouseover="GClass(%s)">%s</span>' %(b,i)+"\n")
result.write('<span data-ng-mouseover="GClass(%s)">%s</span>' %(b+1,end)) #separate statement for closing. no punctuation follows it, so it wouldn't get written otherwise
text = codecs.open('txt name.txt','r+','utf-8') #second text
content = text.read()
rep=re.sub('''      ''','''</br></br>&nbsp;&nbsp;&nbsp;&nbsp;''',content)
sentences=re.split('''((?!\. Jahrhundert)(?<!Mr)(?<!circa)(?<!cf)(?!"\s[a-z|I])(?![\.\!\?]\)[\.\!\?])(?![\.\?\!]\s[\-,?!])[\.\?\!"]\s)''', rep) #splits into a list based on punction
result.write('''<div></br></br></div>''')

result.write("""</div><div class="original" id="idbox2" style="border:1px solid black;"> """)
end=sentences[-1]
sentences[0::2]
sentences[1::2]
sentences =[i+j for i,j in zip(sentences[::2], sentences[1::2])] #binds every two splits together, letting punction be placed in the same tag as the preceding sentence. 
b=0
for i  in sentences:
        b=b+1
        result.write('<span data-ng-class="EClass(%s)">%s</span>' %(b, i)+"\n")
result.write('<span data-ng-class="EClass(%s)">%s</span>' %(b+1,end))
result.write('</div> </body></html>')
print "done"
result.close()
