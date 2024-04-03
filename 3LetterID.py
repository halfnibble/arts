#!/usr/bin/env python

from LetterID_parser import IDENTIFIER, LOCATION, ID_NAME

print 'Content-type: text/html\r'
print '\r'
print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">"""
print '<TITLE>ZKC 3 Letter Identifiers</TITLE>'

print """
<style type="text/css">
<!--
	body {
		background-color: #000;
		}
		
	.webtitle {
		font-family: Arial, Helvetica, sans-serif;
		font-size: 16pt;
		color: #FFF;
		}



	.centerdiv {
		width: 500px;
		margin-left: auto;
		margin-right: auto;
		}
	
	.card_box {
		background-color: #FFF;
		width: 480px;
		border: 1px dashed #CC0033;
		padding: 15px;
		margin: 10px;
		}
		
	#identifier {
		height: 50px;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 22pt;
		}
		
	#answer {
		height: 100px;
		border: 1px solid #C8C8C8;
		padding: 10px;
		margin: 10px;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 20px;
		color: #0066CC;
		}
	
	#Flip_button  {
		float: left;
		width: 100px;
		border: 1px dashed #CC0033;
		background-color: #CCFFFF;
		padding-left: 20px;
		padding-right: 20px;
		padding-top: 10px;
		padding-bottom: 10px;
		margin: 20px;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 16pt;
		}
		
	#Next_button {
		float: right;
		width: 100px;
		border: 1px dashed #CC0033;
		background-color: #CCFFFF;
		padding-left: 20px;
		padding-right: 20px;
		padding-top: 10px;
		padding-bottom: 10px;
		margin: 20px;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 16pt;
		}
		
	#Flip_button:hover {
		background-color: #FFCCFF;
		}	
		
	#Next_button:hover {
		background-color: #FFCCFF;
		}
	
        .FlipNext_button:link {
                color: #000;
                text-decoration: none;
                }

        .FlipNext_button:visited {
                color: #000;
                text-decoration: none;
                }

        .FlipNext_button:active {
                color: #000;
                text-decoration: none;
                }

        .FlipNext_button:hover {
                color: #000;
                text-decoration: none;
                }



	
-->	
</style>
	
<script type="text/javascript">
<!--
	
	var Identifier;
	var Location;
	var ID_Name;
	
	"""
	
print 'Identifier = "' + IDENTIFIER + '";'
print 'Location ="' + LOCATION + '";'
print 'ID_Name ="' + ID_NAME + '";'

print """

	function displayanswer() {
		document.getElementById('answer').innerHTML = Location + "<BR /><BR /> " + ID_Name;
		}
-->
</script>

<body>

<p align="center" class="webtitle">ZKC 3 Letter Identifiers. </p>

<div class="centerdiv" align="center">

	<div class="card_box">

		<div id="identifier"> """
print IDENTIFIER
print """
		</div>
	
		<HR />
	
		<div id="answer">
                     &nbsp;
		</div>
		
	</div>
	
	<a href="javascript:displayanswer()" class="FlipNext_button"><div id="Flip_button" ONCLICK="javascript:displayanswer()">
	FLIP
	</div></a>
	
	<a href="http://www.ajaxkc.com/ATC/3LetterID.py" class="FlipNext_button"><div id="Next_button" ONCLICK="javascript:window.location.href='http://www.ajaxkc.com/ATC/3LetterID.py'">
	NEXT >>
	</div></a>

</div>


</body>
"""
